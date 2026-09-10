Two 2026-08-13 whole-device exports — provenance notes
Filed 2026-08-13. Read this before citing either file.
imessage_export_deep_20260813.csv
15 columns: DATE/TIME, DATE READ, DATE DELIVERED, SENT OR RECEIVED, HANDLE, SERVICE, CHAT NAME, CHAT ID, IS GROUP CHAT, MESSAGE TYPE, MESSAGE CONTENT, IN RESPONSE TO, HAS ATTACHMENT, ATTACHMENT COUNT, MESSAGE GUID. 186,671 data rows, 499 handles, 598 chats.


* DATE/TIME IS UTC. Every other message source in this repo is America/New_York. Validated on 42,895 uniquely text-matched pairs against imessage_7244346811+7249204125+2124702449_both_all_now.csv: 23,158 at exactly +5.00h (EST), 19,692 at +4.00h (EDT), 45 outliers (0.1%). Convert before comparing to any published figure.
* HANDLE == 'Me' is outbound.
* This file is LOSSY relative to raw/self/dox-scan/all_imessages_complete_dump.txt (217,573 dated lines, through 2025-08-10). 41.8% of the older dump's records have no row here. For any window in 2019–2025 the older dump is the better source.
* Contains a ~833-day zero-row window (2021-04-27 → 2023-08-09 local) that is an export artifact, not silence — the location record logs ~690 work shifts inside it.
* Contains a separate bidirectional SMS void, 2020-07-30 → 2024-05-24.
imessage_export_flat_20260813.csv
3 columns: DATE/TIME, SENT OR RECEIVED, MESSAGE CONTENT. Same underlying extract, attribution stripped. It has no handle column and therefore cannot attribute any message to any person. It cannot settle an attribution question by itself and must never be used for one. It is filed only because it is the artifact that produced a documented misattribution during the 2026-08-13 audit, and is retained as the worked example behind the handle set field of the provenance preflight in EXTRACTION_SPEC.md.