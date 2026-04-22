---
title: Tracking Issue for `cuprated 0.0.9 Molybdenite` release
source_url: https://github.com/Cuprate/cuprate/issues/589
author: hinto-janai
assignees: []
labels:
- C-tracking-issue
created_at: '2026-02-26T23:37:09+00:00'
updated_at: '2026-04-21T20:33:10+00:00'
type: issue
status: closed
closed_at: '2026-04-21T20:33:10+00:00'
---

# Original Description
<!-- Consider keeping the following section in the issue. -->
### About tracking issues
Tracking issues are used to record the overall progress of implementation.
They are also used as hubs connecting to other relevant issues, e.g., bugs or open design questions.
A tracking issue is however not meant for large scale discussion, questions, or bug reports about a feature.
Instead, open a dedicated issue for the specific matter.

### What

This is a tracking issue for the `cuprated 0.0.9 Molybdenite` release.

Last release: https://github.com/Cuprate/cuprate/issues/569.

### Steps
- Changelog
  - [x] Relevant changes added to `misc/changelogs/cuprated/$VERSION.md`
- Fast sync
  - [x] Update hashes, see `misc/FAST_SYNC_HASHES.md`
- User Book
  - [x] Update necessary documentation
  - [x] Book title reflects `cuprated`'s version
- Repository
  - [x] Decide specific commit: bc059f047651a743565330e8fe533e4f5a81d388
  - [x] Create draft release
  - [x] Create version tag
  - [x] Build CI binaries: https://github.com/Cuprate/cuprate/actions/runs/24743661283
- `cuprated` testing
  - Full-sync from scratch
    - [ ] x64 Windows
    - [x] x64 Linux
    - [x] ARM64 macOS
    - [x] ARM64 Linux
- Release
    - [x] Add binaries to release
    - [x] Publish `Cuprate/user-book`: https://github.com/Cuprate/user-book/actions/runs/24744053796
    - [x] Release: https://github.com/Cuprate/cuprate/releases/tag/cuprated-0.0.9
- Release announcements
  - [x] Reddit: https://www.reddit.com/r/Monero/comments/1srzuzg/cuprate_v009_released/
  - [x] Matrix

# Discussion History
# Action History
- Created by: hinto-janai | 2026-02-26T23:37:09+00:00
- Closed at: 2026-04-21T20:33:10+00:00
