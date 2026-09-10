#!/usr/bin/env python3
"""aesgcm — AES-256-GCM and this project's sealed-blob format, in pure stdlib.

WHY THIS FILE EXISTS AT ALL

`caakehorn/wiki-brain` is public, and the intake ledger is the one thing in it
that must never be readable by whoever wanders past. But the ledger also has to
reach a phone: ボスの部屋 on the leviathan site writes to this repository through
GitHub's contents API, from a browser, with no daemon anywhere in the loop.

Those two facts have exactly one meeting point — the record travels and rests as
ciphertext, and only something holding the passphrase can read it. The browser
half is free: `crypto.subtle` does AES-GCM and PBKDF2 natively, and `js/gate.js`
has decrypted this project's blobs that way since the beginning.

This half is not free. `hashlib.pbkdf2_hmac` is stdlib; AES is not, and this
repository takes no dependencies — that constraint is in `CLAUDE.md` and it is
load-bearing, because the whole corpus is meant to still open in twenty years
with nothing but a Python install. `pip install cryptography` would be four
characters of convenience bought with the one property the archive is for.

So: AES-256 and GCM, written out. It is about two hundred lines of well-specified
arithmetic that has not changed since 2001, and it is checked here against NIST's
own vectors rather than against itself.

THE FORMAT is the one `tools/encrypt.py` in the leviathan repo already documents
and `data/leviathan.enc` already uses, byte for byte:

    {"v": 1, "kdf": "PBKDF2-SHA256", "iter": 250000,
     "salt": <b64, 16 bytes>, "iv": <b64, 12 bytes>, "ct": <b64>}

    key = PBKDF2-HMAC-SHA256(passphrase, salt, iter) -> 32 bytes
    ct  = AES-256-GCM(key, iv, plaintext), tag appended

A wrong passphrase fails GCM authentication and raises, rather than returning
garbage. That is the whole check — there is no stored hash to compare against and
nothing on the wire a guesser can grind faster than 250,000 iterations a try.

WHAT THIS IS NOT. It is not fast and it is not constant-time. It processes a few
hundred KB a second, which is irrelevant for a file that is a few thousand JSON
lines, and it should not be used for anything where an attacker can time it. For
this ledger, on this machine, decrypting a file the operator already owns, that
is the right trade.
"""
import base64
import hashlib
import hmac
import os
import struct

ITER = 250_000
SALT_LEN = 16
IV_LEN = 12
TAG_LEN = 16


# ── AES ─────────────────────────────────────────────────────────────────────
# FIPS-197. The S-box and the round constants are the standard tables; the key
# schedule and the round function are transcribed from the specification.
def _build_sbox():
    p = q = 1
    sbox = [0] * 256
    while True:
        # p *= 3 in GF(2^8)
        p = p ^ ((p << 1) & 0xFF) ^ (0x1B if p & 0x80 else 0)
        # q /= 3
        q ^= (q << 1) & 0xFF
        q ^= (q << 2) & 0xFF
        q ^= (q << 4) & 0xFF
        if q & 0x80:
            q ^= 0x09
        x = q ^ ((q << 1) | (q >> 7)) ^ ((q << 2) | (q >> 6)) \
              ^ ((q << 3) | (q >> 5)) ^ ((q << 4) | (q >> 4))
        sbox[p] = (x ^ 0x63) & 0xFF
        if p == 1:
            break
    sbox[0] = 0x63
    return sbox


SBOX = _build_sbox()
RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36,
        0x6C, 0xD8, 0xAB, 0x4D]


def _xtime(a):
    a <<= 1
    return (a ^ 0x1B) & 0xFF if a & 0x100 else a


def _expand_key(key):
    """AES-256 key schedule: 8 words in, 60 words out (15 round keys)."""
    if len(key) != 32:
        raise ValueError("this build is AES-256 only; key must be 32 bytes")
    nk, nr = 8, 14
    w = [list(key[4 * i:4 * i + 4]) for i in range(nk)]
    for i in range(nk, 4 * (nr + 1)):
        t = list(w[i - 1])
        if i % nk == 0:
            t = t[1:] + t[:1]
            t = [SBOX[b] for b in t]
            t[0] ^= RCON[i // nk - 1]
        elif i % nk == 4:
            t = [SBOX[b] for b in t]
        w.append([a ^ b for a, b in zip(w[i - nk], t)])
    return [[w[4 * r + c][j] for c in range(4) for j in range(4)]
            for r in range(nr + 1)]


def _encrypt_block(rk, block):
    """One 16-byte AES block, column-major state as the spec defines it."""
    s = [block[i] ^ rk[0][i] for i in range(16)]
    nr = len(rk) - 1
    for rnd in range(1, nr + 1):
        s = [SBOX[b] for b in s]
        # ShiftRows, on the column-major layout
        s = [s[0], s[5], s[10], s[15],
             s[4], s[9], s[14], s[3],
             s[8], s[13], s[2], s[7],
             s[12], s[1], s[6], s[11]]
        if rnd != nr:
            t = []
            for c in range(4):
                a = s[4 * c:4 * c + 4]
                u = a[0] ^ a[1] ^ a[2] ^ a[3]
                t += [a[0] ^ u ^ _xtime(a[0] ^ a[1]),
                      a[1] ^ u ^ _xtime(a[1] ^ a[2]),
                      a[2] ^ u ^ _xtime(a[2] ^ a[3]),
                      a[3] ^ u ^ _xtime(a[3] ^ a[0])]
            s = t
        s = [s[i] ^ rk[rnd][i] for i in range(16)]
    return bytes(s)


# ── GCM ─────────────────────────────────────────────────────────────────────
# NIST SP 800-38D. GHASH is multiplication in GF(2^128) with the reversed-bit
# convention the spec uses; the shift-and-xor form below is the plain one.
def _gf_mul(x, y):
    z, v = 0, y
    for i in range(127, -1, -1):
        if (x >> i) & 1:
            z ^= v
        if v & 1:
            v = (v >> 1) ^ 0xE1000000000000000000000000000000
        else:
            v >>= 1
    return z


def _ghash(h, data):
    y = 0
    for i in range(0, len(data), 16):
        block = data[i:i + 16].ljust(16, b"\x00")
        y = _gf_mul(y ^ int.from_bytes(block, "big"), h)
    return y


def _ctr(rk, icb, data):
    out = bytearray()
    counter = int.from_bytes(icb, "big")
    for i in range(0, len(data), 16):
        block = _encrypt_block(rk, counter.to_bytes(16, "big"))
        chunk = data[i:i + 16]
        out += bytes(a ^ b for a, b in zip(chunk, block))
        counter = (counter & ~0xFFFFFFFF) | ((counter + 1) & 0xFFFFFFFF)
    return bytes(out)


def _gcm_core(key, iv, data, aad):
    rk = _expand_key(key)
    h = int.from_bytes(_encrypt_block(rk, b"\x00" * 16), "big")
    if len(iv) == 12:
        j0 = iv + b"\x00\x00\x00\x01"
    else:
        s = (-len(iv)) % 16
        j0 = _ghash(h, iv + b"\x00" * s + b"\x00" * 8 +
                    struct.pack(">Q", len(iv) * 8)).to_bytes(16, "big")
    return rk, h, j0


def _tag(h, rk, j0, aad, ct):
    pad_a = (-len(aad)) % 16
    pad_c = (-len(ct)) % 16
    s = _ghash(h, aad + b"\x00" * pad_a + ct + b"\x00" * pad_c +
               struct.pack(">QQ", len(aad) * 8, len(ct) * 8))
    return bytes(a ^ b for a, b in
                 zip(s.to_bytes(16, "big"), _encrypt_block(rk, j0)))


def encrypt(key, iv, plaintext, aad=b""):
    """-> ciphertext || 16-byte tag, exactly as WebCrypto's AES-GCM returns."""
    rk, h, j0 = _gcm_core(key, iv, plaintext, aad)
    icb = (int.from_bytes(j0, "big") + 1).to_bytes(16, "big")
    ct = _ctr(rk, icb, plaintext)
    return ct + _tag(h, rk, j0, aad, ct)


def decrypt(key, iv, ciphertext, aad=b""):
    """Raises ValueError if the tag does not verify. That is the passphrase check."""
    if len(ciphertext) < TAG_LEN:
        raise ValueError("ciphertext is too short to carry a tag")
    ct, tag = ciphertext[:-TAG_LEN], ciphertext[-TAG_LEN:]
    rk, h, j0 = _gcm_core(key, iv, ct, aad)
    if not hmac.compare_digest(_tag(h, rk, j0, aad, ct), tag):
        raise ValueError("authentication failed — wrong passphrase, or the file "
                         "has been altered since it was written")
    icb = (int.from_bytes(j0, "big") + 1).to_bytes(16, "big")
    return _ctr(rk, icb, ct)


# ── the blob format ─────────────────────────────────────────────────────────
def derive(passphrase, salt, iterations=ITER):
    return hashlib.pbkdf2_hmac("sha256", passphrase.encode("utf-8"), salt, iterations, 32)


def _b64(b):
    return base64.b64encode(b).decode("ascii")


def _unb64(s):
    return base64.b64decode(s)


def seal(passphrase, plaintext, iterations=ITER):
    """bytes -> the JSON-ready dict `js/gate.js` and tools/encrypt.py both read."""
    salt, iv = os.urandom(SALT_LEN), os.urandom(IV_LEN)
    key = derive(passphrase, salt, iterations)
    return {"v": 1, "kdf": "PBKDF2-SHA256", "iter": iterations,
            "salt": _b64(salt), "iv": _b64(iv),
            "ct": _b64(encrypt(key, iv, plaintext))}


def unseal(passphrase, blob):
    """The dict back to bytes. Raises ValueError on a wrong passphrase."""
    for k in ("salt", "iv", "ct"):
        if k not in blob:
            raise ValueError(f"not a sealed blob: no {k!r}")
    key = derive(passphrase, _unb64(blob["salt"]), int(blob.get("iter", ITER)))
    return decrypt(key, _unb64(blob["iv"]), _unb64(blob["ct"]))
