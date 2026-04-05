---
title: Tracking Issue for `cuprated 0.0.9 Molybdenite` release
source_url: https://github.com/Cuprate/cuprate/issues/589
author: hinto-janai
assignees: []
labels:
- C-tracking-issue
created_at: '2026-02-26T23:37:09+00:00'
updated_at: '2026-02-26T23:37:36+00:00'
type: issue
status: open
closed_at: null
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
  - [ ] Relevant changes added to `misc/changelogs/cuprated/$VERSION.md`
- Fast sync
  - [ ] Update hashes, see `misc/FAST_SYNC_HASHES.md`
- User Book
  - [ ] Update necessary documentation
  - [ ] Book title reflects `cuprated`'s version
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
    - [ ] Release: https://github.com/Cuprate/cuprate/releases/tag/cuprated-0.0.8
- Release announcements
  - [ ] Reddit
  - [ ] Matrix

# Discussion History
# Action History
- Created by: hinto-janai | 2026-02-26T23:37:09+00:00
