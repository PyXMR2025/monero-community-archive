---
title: Tracking Issue for `cuprated 0.0.6 Molybdenite` release
source_url: https://github.com/Cuprate/cuprate/issues/517
author: hinto-janai
assignees: []
labels:
- C-tracking-issue
created_at: '2025-07-16T23:58:41+00:00'
updated_at: '2025-10-11T13:36:39+00:00'
type: issue
status: closed
closed_at: '2025-10-11T13:36:38+00:00'
---

# Original Description
<!-- Consider keeping the following section in the issue. -->
### About tracking issues
Tracking issues are used to record the overall progress of implementation.
They are also used as hubs connecting to other relevant issues, e.g., bugs or open design questions.
A tracking issue is however not meant for large scale discussion, questions, or bug reports about a feature.
Instead, open a dedicated issue for the specific matter.

### What
This is a tracking issue for the `cuprated 0.0.6 Molybdenite` release.

### Steps
- Changelog
  - [ ] Relevant changes added to `misc/changelogs/cuprated/$VERSION.md`
- Fast sync
  - [ ] Update hashes, see `misc/FAST_SYNC_HASHES.md`
- User Book
  - [ ] Update necessary documentation
  - [ ] Book title reflects `cuprated`'s version
- `cuprated`
  - [ ] Killswitch timestamp updated
- Repository
  - [ ] Decide specific commit
  - [ ] Create draft release
  - [ ] Create version tag
  - [ ] Build CI binaries
- `cuprated` testing
  - Full-sync from scratch
    - [ ] x64 Windows
    - [ ] x64 Linux
    - [ ] ARM64 macOS
    - [ ] ARM64 Linux
- Release
    - [ ] Add binaries to release
    - [ ] Publish `Cuprate/user-book`
    - [ ] Release
- Release announcements
  - [ ] Reddit
  - [ ] Matrix

# Discussion History
## hinto-janai | 2025-10-11T13:36:38+00:00
https://github.com/Cuprate/cuprate/releases/tag/cuprated-0.0.6

# Action History
- Created by: hinto-janai | 2025-07-16T23:58:41+00:00
- Closed at: 2025-10-11T13:36:38+00:00
