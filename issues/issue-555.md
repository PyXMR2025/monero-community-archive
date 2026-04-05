---
title: Tracking Issue for `cuprated 0.0.7 Molybdenite` release
source_url: https://github.com/Cuprate/cuprate/issues/555
author: hinto-janai
assignees: []
labels:
- C-tracking-issue
created_at: '2025-10-11T13:36:56+00:00'
updated_at: '2025-10-12T13:56:55+00:00'
type: issue
status: closed
closed_at: '2025-10-12T13:56:55+00:00'
---

# Original Description
<!-- Consider keeping the following section in the issue. -->
### About tracking issues
Tracking issues are used to record the overall progress of implementation.
They are also used as hubs connecting to other relevant issues, e.g., bugs or open design questions.
A tracking issue is however not meant for large scale discussion, questions, or bug reports about a feature.
Instead, open a dedicated issue for the specific matter.

### What
This is a tracking issue for the `cuprated 0.0.7 Molybdenite` release.

### Steps
- Changelog
  - [x] Relevant changes added to `misc/changelogs/cuprated/$VERSION.md`
- Fast sync
  - [x] Update hashes, see `misc/FAST_SYNC_HASHES.md`
- User Book
  - [x] Update necessary documentation
  - [x] Book title reflects `cuprated`'s version
- `cuprated`
  - [x] Killswitch timestamp updated
- Repository
  - [x] Decide specific commit
  - [x] Create draft release
  - [x] Create version tag
  - [x] Build CI binaries: https://github.com/Cuprate/cuprate/actions/runs/18436516465
- `cuprated` testing
  - Full-sync from scratch
    - [ ] x64 Windows
    - [x] x64 Linux
    - [x] ARM64 macOS
    - [x] ARM64 Linux
- Release
    - [x] Add binaries to release
    - [x] Publish `Cuprate/user-book`
    - [x] Release
- Release announcements
  - [x] Reddit: https://www.reddit.com/r/Monero/comments/1o4pk49/cuprate_v007_released
  - [x] Matrix

# Discussion History
# Action History
- Created by: hinto-janai | 2025-10-11T13:36:56+00:00
- Closed at: 2025-10-12T13:56:55+00:00
