# Morgantown St recording — source verification update

Filed: 2026-08-20

## Newly supplied source material

The operator supplied the following two files directly in this session:

- `Morgantown St.m4a` — the audio recording itself.

- `[00_00_00] Speaker 1.txt` — a 611-line, timestamped speaker-labelled transcript supplied as evidence for the audio.

The transcript has been filed verbatim as:

- `raw/self/audio/2026-08-16_Morgantown_St_call-transcript.txt`

No wording, speaker label, or timestamp in the supplied transcript has been silently corrected in the raw copy. Interpretation belongs in analysis pages, not in this raw artifact.

## File-level checks performed on the supplied audio

- Size: `13,097,702` bytes

- SHA-256: `f656b6abd5c676a001eaf1f9a207cbc1fad262b3dbc3e9b145618d2bc307a4ec`

- MD5: `96bd3df46d4b0f4c5278cc9d6978621d`

- Container: M4A / QuickTime

- Audio codec: AAC-LC

- Sample rate: 44.1 kHz

- Channels: stereo

- Duration: `927.242449` s (15:27.24)

- Creation time atom: `2026-08-17T03:54:50Z`

- Voice Memos UUID: `5B51561B-0110-4FDD-98B8-B41DB654CFDD`

- Encoder: `com.apple.VoiceMemos (Dan’s MacBook Pro (null))`

- Title: `Morgantown St`

The MD5 and byte size match the values already recorded in the pre-existing provenance README. This is strong file-identity corroboration for the supplied copy; SHA-256 is added here as the stronger modern integrity identifier.

## Transcript-level checks

- Lines: `611`

- Last supplied timestamp: `00:14:59`

- Audio duration: `00:15:27.24`

- Therefore the supplied transcript does not purport to cover the final ~28 seconds of the audio, and this is not treated as a contradiction.

- The transcript begins at `00:00:00` and contains continuous timestamped speaker turns through `00:14:59`.

## What is now established vs. what is not

### Established at the source/provenance level

1. A concrete audio file has been supplied and its container metadata can be inspected directly.

1. A concrete timestamped speaker-labelled transcript has been supplied alongside it.

1. The transcript is now a first-order transcription artifact in the corpus rather than a quotation copied only from an agent-authored analysis.

1. The existing AI-secondary analysis should no longer be described as the sole or immediate source of the call's transcript.

### Not claimed by this update

This update does **not** independently establish that the audio recording is an unedited original, that every transcript word is acoustically correct, or that the speaker labels are objectively identified. Those are different forensic questions. The audio itself is the T0 primary artifact; the supplied transcript is a source-derived transcription that can now be checked directly against that artifact.

## Consequence for the wiki

The old provenance language saying the recording was "unheard" / "NOT TRANSCRIBED" is obsolete. Future analysis should cite the audio as T0 primary and the newly filed transcript as the direct transcription aid, while retaining the older Hermes/PDF transcript as a secondary comparison source.

The important methodological correction is simple: **do not silently promote the transcript into an independently authenticated fact pattern.** Preserve the raw transcript, identify speaker attribution as transcript-level attribution, and let claims that depend on exact wording be checked against the audio when needed.
