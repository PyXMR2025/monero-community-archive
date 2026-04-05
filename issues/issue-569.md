---
title: Tracking Issue for `cuprated 0.0.8 Molybdenite` release
source_url: https://github.com/Cuprate/cuprate/issues/569
author: hinto-janai
assignees: []
labels:
- C-tracking-issue
created_at: '2025-11-26T19:43:47+00:00'
updated_at: '2026-02-26T23:35:50+00:00'
type: issue
status: closed
closed_at: '2025-11-26T21:05:39+00:00'
---

# Original Description
<!-- Consider keeping the following section in the issue. -->
### About tracking issues
Tracking issues are used to record the overall progress of implementation.
They are also used as hubs connecting to other relevant issues, e.g., bugs or open design questions.
A tracking issue is however not meant for large scale discussion, questions, or bug reports about a feature.
Instead, open a dedicated issue for the specific matter.

### What
This is a tracking issue for the `cuprated 0.0.8 Molybdenite` release.

### Steps
- Changelog
  - [x] Relevant changes added to `misc/changelogs/cuprated/$VERSION.md`
- Fast sync
  - [x] Update hashes, see `misc/FAST_SYNC_HASHES.md`
- User Book
  - [x] Update necessary documentation
  - [x] Book title reflects `cuprated`'s version
- Repository
  - [x] Decide specific commit: c0c68f526ec76286fa6d3bf2afcea9ae85c7c4b5
  - [x] Create draft release
  - [x] Create version tag
  - [x] Build CI binaries: https://github.com/Cuprate/cuprate/actions/runs/19715568081
- `cuprated` testing
  - Full-sync from scratch
    - [ ] x64 Windows
    - [ ] x64 Linux
    - [ ] ARM64 macOS
    - [ ] ARM64 Linux
- Release
    - [x] Add binaries to release
    - [x] Publish `Cuprate/user-book`
    - [x] Release: https://github.com/Cuprate/cuprate/releases/tag/cuprated-0.0.8
- Release announcements
  - [x] Reddit: https://www.reddit.com/r/Monero/comments/1p7jh34/cuprate_v008_released/
  - [x] Matrix

# Discussion History
# Action History
- Created by: hinto-janai | 2025-11-26T19:43:47+00:00
- Closed at: 2025-11-26T21:05:39+00:00
