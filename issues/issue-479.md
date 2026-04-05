---
title: Change release asset naming scheme
source_url: https://github.com/Cuprate/cuprate/issues/479
author: hinto-janai
assignees: []
labels:
- C-proposal
created_at: '2025-05-14T21:53:12+00:00'
updated_at: '2025-05-30T18:38:55+00:00'
type: issue
status: closed
closed_at: '2025-05-30T18:38:55+00:00'
---

# Original Description
<!--
Note: Please search to see if an issue already exists for this proposal.
-->

## What
Change the release asset naming scheme from the current:
```
cuprated-$VERSION-$OS-$ABBREVIATED_ARCH.$ARCHIVE_EXT
```
to:
```
cuprated-$VERSION-$RUST_TARGET_TRIPLE.$ARCHIVE_EXT
```

For example, the current targets would be renamed:
```
cuprated-0.0.3-x86_64-pc-windows-msvc.zip
cuprated-0.0.3-x86_64-apple-darwin.tar.gz
cuprated-0.0.3-aarch64-apple-darwin.tar.gz
cuprated-0.0.3-aarch64-unknown-linux.tar.gz
cuprated-0.0.3-x86_64-unknown-linux.tar.gz
```

## Pros
- [Follows a known standard](https://doc.rust-lang.org/rustc/platform-support.html)
- Less naming decisions required as the build target list grows

## Con
May be confusing to end users.

# Discussion History
## SyntheticBird45 | 2025-05-14T22:20:54+00:00
sounds good to me

## hinto-janai | 2025-05-20T23:35:27+00:00
Discussed here: https://github.com/monero-project/meta/issues/1203#issuecomment-2895515999.

# Action History
- Created by: hinto-janai | 2025-05-14T21:53:12+00:00
- Closed at: 2025-05-30T18:38:55+00:00
