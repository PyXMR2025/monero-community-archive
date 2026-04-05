---
title: Tracking Issue for `cuprated 0.0.1 Molybdenite` release
source_url: https://github.com/Cuprate/cuprate/issues/371
author: hinto-janai
assignees: []
labels:
- C-tracking-issue
created_at: '2025-01-19T16:29:07+00:00'
updated_at: '2025-03-12T13:40:36+00:00'
type: issue
status: closed
closed_at: '2025-03-12T13:35:26+00:00'
---

# Original Description
<!-- Consider keeping the following section in the issue. -->
### About tracking issues
Tracking issues are used to record the overall progress of implementation.
They are also used as hubs connecting to other relevant issues, e.g., bugs or open design questions.
A tracking issue is however not meant for large scale discussion, questions, or bug reports about a feature.
Instead, open a dedicated issue for the specific matter.

### What
This is a tracking issue for the `v0.0.1 Molybdenite` release.

### Steps
- Changelog
  - [x] Relevant changes added to `misc/changelogs/cuprated/$VERSION.md`: https://github.com/Cuprate/cuprate/pull/370
- Fast sync
  - [x] Update hashes, see `misc/FAST_SYNC_HASHES.md`
- User Book
  - [x] Update necessary documentation
  - [x] Book title reflects `cuprated`'s version
- `cuprated`
  - [x] Killswitch timestamp updated: https://github.com/Cuprate/cuprate/pull/391
- Repository
  - [x] Decide specific commit: https://github.com/Cuprate/cuprate/commit/11d4f290c35e51397880d55bae78348dbe211a7b
  - [x] Create draft release
  - [x] Create version tag
  - [x] Build CI binaries: https://github.com/Cuprate/cuprate/actions/runs/13800462346
- `cuprated` testing
  - (Fast) sync from scratch
    - [x] x64 Linux
    - [x] ARM64 macOS
    - [x] ARM64 Linux
- Release
    - [x] Add binaries to release
    - [x] Publish `Cuprate/user-book`: https://github.com/Cuprate/user-book/actions/runs/13811579378
    - [x] Release: https://github.com/Cuprate/cuprate/releases/tag/cuprated-0.0.1
- Release announcements
  - [x] Reddit: https://www.reddit.com/r/Monero/comments/1j9k1n8/cuprate_v001_released/
  - [x] Matrix

## Related
Related links for this release of `cuprated`:
- https://github.com/Cuprate/cuprate/milestone/1

# Discussion History
## SyntheticBird45 | 2025-01-19T19:06:55+00:00
https://matrix.to/#/!zPLCnZSsyeFFxUiqUZ:monero.social/$Gmn0d-IWCDAGyzeyo0CgK0OqXejdc2mx0hQjBDlks3k?via=monero.social&via=matrix.org&via=unredacted.org

```rs
const NAME_OF_METAL: &str = "Molybdenite"
```

# Action History
- Created by: hinto-janai | 2025-01-19T16:29:07+00:00
- Closed at: 2025-03-12T13:35:26+00:00
