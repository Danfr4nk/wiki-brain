# ihatedanfrank-20260623.zip — split for GitHub's blob API

The original 82,687,521-byte Facebook export archive could not be uploaded
as a single blob (GitHub's Git Data API rejects payloads this large), so
it is stored here in two parts. The bytes are preserved exactly.

To reassemble:

    cat ihatedanfrank-20260623.zip.parta* > ihatedanfrank-20260623.zip
    sha256sum ihatedanfrank-20260623.zip   # must match SHA256SUM.txt

The extracted contents of this archive are also present in
`../facebook-ihatedanfrank/` in this same directory.
