---
title: Crash on macOS after entering password to enter wallet
source_url: https://github.com/monero-project/monero-gui/issues/1122
author: rex4539
assignees: []
labels: []
created_at: '2018-02-19T16:48:11+00:00'
updated_at: '2018-02-21T22:15:43+00:00'
type: issue
status: closed
closed_at: '2018-02-21T22:15:43+00:00'
---

# Original Description
git @ bd173c9 (or later)

Reproducibility: always

Steps:
1. Launch GUI.
2. Enter password and hit enter.

What happened:
```
Error: memset_s failed
Process 99924 exited with status = 1 (0x00000001)
```

Expected result:
GUI does not crash.

Notes:
Looks like the crash was introduced sometime after git @ bd173c9
For example, git @ 4bf0bef does not crash.

# Discussion History
## leonklingele | 2018-02-19T17:14:10+00:00
https://github.com/monero-project/monero/pull/3289 should fix it

## rex4539 | 2018-02-21T22:15:42+00:00
Fixed with git @ 084c1c8

# Action History
- Created by: rex4539 | 2018-02-19T16:48:11+00:00
- Closed at: 2018-02-21T22:15:43+00:00
