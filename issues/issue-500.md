---
title: Tracking Issue for `cuprated 0.0.5 Molybdenite` release
source_url: https://github.com/Cuprate/cuprate/issues/500
author: hinto-janai
assignees: []
labels:
- C-tracking-issue
created_at: '2025-06-04T19:18:45+00:00'
updated_at: '2025-07-16T23:57:18+00:00'
type: issue
status: closed
closed_at: '2025-07-16T23:57:18+00:00'
---

# Original Description
<!-- Consider keeping the following section in the issue. -->
### About tracking issues
Tracking issues are used to record the overall progress of implementation.
They are also used as hubs connecting to other relevant issues, e.g., bugs or open design questions.
A tracking issue is however not meant for large scale discussion, questions, or bug reports about a feature.
Instead, open a dedicated issue for the specific matter.

### What
This is a tracking issue for the `cuprated 0.0.5 Molybdenite` release.

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
  - [x] Decide specific commit: https://github.com/Cuprate/cuprate/commit/97e539559a244609057c3593287e29d910941227
  - [x] Create draft release
  - [x] Create version tag
  - [x] Build CI binaries: https://github.com/Cuprate/cuprate/actions/runs/16332578662
- `cuprated` testing
  - Full-sync from scratch
    - [ ] x64 Windows
    - [x] x64 Linux
    - [x] ARM64 macOS
    - [x] ARM64 Linux
- Release
    - [x] Add binaries to release
    - [x] Publish `Cuprate/user-book`: https://github.com/Cuprate/user-book/actions/runs/16332693025
    - [x] Release
- Release announcements
  - [x] Reddit
  - [x] Matrix

# Discussion History
# Action History
- Created by: hinto-janai | 2025-06-04T19:18:45+00:00
- Closed at: 2025-07-16T23:57:18+00:00
