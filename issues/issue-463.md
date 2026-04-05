---
title: Tracking Issue for `cuprated 0.0.4 Molybdenite` release
source_url: https://github.com/Cuprate/cuprate/issues/463
author: hinto-janai
assignees: []
labels:
- C-tracking-issue
created_at: '2025-05-07T23:22:59+00:00'
updated_at: '2025-06-04T19:12:33+00:00'
type: issue
status: closed
closed_at: '2025-06-04T19:12:33+00:00'
---

# Original Description
<!-- Consider keeping the following section in the issue. -->
### About tracking issues
Tracking issues are used to record the overall progress of implementation.
They are also used as hubs connecting to other relevant issues, e.g., bugs or open design questions.
A tracking issue is however not meant for large scale discussion, questions, or bug reports about a feature.
Instead, open a dedicated issue for the specific matter.

### What
This is a tracking issue for the `cuprated 0.0.4 Molybdenite` release.

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
  - [x] Decide specific commit: https://github.com/Cuprate/cuprate/commit/640ac1bc1cb8e167c6b1c29c3fd3d30458f3096c
  - [x] Create draft release
  - [x] Create version tag
  - [x] Build CI binaries: https://github.com/Cuprate/cuprate/actions/runs/15448910788
- `cuprated` testing
  - Full-sync from scratch
    - [ ] x64 Linux
    - [x] ARM64 macOS
    - [x] ARM64 Linux
- Release
    - [x] Add binaries to release
    - [x] Publish `Cuprate/user-book`: 
    - [x] Release: https://github.com/Cuprate/cuprate/releases/tag/cuprated-0.0.4
- Release announcements
  - [x] Reddit: https://www.reddit.com/r/Monero/comments/1l3e1pj/cuprate_v004_released_initial_rpc_integration
  - [x] Matrix

### Related

# Discussion History
# Action History
- Created by: hinto-janai | 2025-05-07T23:22:59+00:00
- Closed at: 2025-06-04T19:12:33+00:00
