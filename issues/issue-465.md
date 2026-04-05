---
title: Please add OpenBSD support
source_url: https://github.com/Cuprate/cuprate/issues/465
author: hiddener
assignees: []
labels: []
created_at: '2025-05-09T20:34:03+00:00'
updated_at: '2025-05-09T20:50:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi, testing `cuprate` build on OpenBSD 7.7, and here it fails:

```
thread 'main' panicked at /home/test/.cargo/git/checkouts/randomx-rs-13f25e53eb0ddfb7/e09955c/build.rs:303:9:
not implemented
```
Played with `target.contains("openbsd")` and still fails, so should be more than that :D

# Discussion History
## SyntheticBird45 | 2025-05-09T20:50:06+00:00
I definitely want OpenBSD support in the future. I can't guarantee anything however since the issue is related to randomx-rs bindings and Tari hasn't added (up to this date) OpenBSD support. I'm not saying it shouldn't be done, but it's low priority in regard to other work being done.
Be sure it won't be forgotten tho.

# Action History
- Created by: hiddener | 2025-05-09T20:34:03+00:00
