---
title: Tracking Issue for `cuprated 0.0.2 Molybdenite` release
source_url: https://github.com/Cuprate/cuprate/issues/401
author: hinto-janai
assignees: []
labels:
- C-tracking-issue
created_at: '2025-03-12T13:41:20+00:00'
updated_at: '2025-04-09T20:28:53+00:00'
type: issue
status: closed
closed_at: '2025-04-09T20:28:52+00:00'
---

# Original Description
<!-- Consider keeping the following section in the issue. -->
### About tracking issues
Tracking issues are used to record the overall progress of implementation.
They are also used as hubs connecting to other relevant issues, e.g., bugs or open design questions.
A tracking issue is however not meant for large scale discussion, questions, or bug reports about a feature.
Instead, open a dedicated issue for the specific matter.

### What
This is a tracking issue for the `cuprated 0.0.2 Molybdenite` release.

### Steps
- Changelog
  - [x] Relevant changes added to `misc/changelogs/cuprated/$VERSION.md`: https://github.com/Cuprate/cuprate/pull/413
- Fast sync
  - [x] Update hashes, see `misc/FAST_SYNC_HASHES.md`: https://github.com/Cuprate/cuprate/pull/427
- User Book
  - [x] Update necessary documentation: https://github.com/Cuprate/cuprate/pull/402
  - [x] Book title reflects `cuprated`'s version
- `cuprated`
  - [x] Killswitch timestamp updated: https://github.com/Cuprate/cuprate/pull/403
- Repository
  - [x] Decide specific commit: https://github.com/Cuprate/cuprate/commit/95aca1d4a52c56975ab9e859cfb283be8a7d4838
  - [x] Create draft release
  - [x] Create version tag
  - [x] Build CI binaries: https://github.com/Cuprate/cuprate/actions/runs/14360523317/job/40260566103
- `cuprated` testing
  - Full-sync from scratch
    - [ ] x64 Linux
    - [x] ARM64 macOS
    - [ ] ARM64 Linux
- Release
    - [x] Add binaries to release
    - [x] Publish `Cuprate/user-book`: https://github.com/Cuprate/user-book/actions/runs/14366006078
    - [x] Release: https://github.com/Cuprate/cuprate/releases/tag/cuprated-0.0.2
- Release announcements
  - [x] Reddit: https://www.reddit.com/r/Monero/comments/1jvfrgl/cuprate_v002_released/
  - [x] Matrix

### Related
- https://github.com/Cuprate/cuprate/milestone/2


# Discussion History
# Action History
- Created by: hinto-janai | 2025-03-12T13:41:20+00:00
- Closed at: 2025-04-09T20:28:52+00:00
