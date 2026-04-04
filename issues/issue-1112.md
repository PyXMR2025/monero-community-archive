---
title: Memory leak in TSMInputSource
source_url: https://github.com/monero-project/monero-gui/issues/1112
author: rex4539
assignees: []
labels:
- wontfix
created_at: '2018-02-05T14:55:24+00:00'
updated_at: '2018-03-30T10:54:19+00:00'
type: issue
status: closed
closed_at: '2018-03-30T10:54:19+00:00'
---

# Original Description
GUI version: v0.11.1.0-190-g75bc37e
Embedded Monero version: v0.10.3.1-1575-ged67e5c

Steps:
Launch Monero GUI.

What happened:
Memory leak in TSMInputSource

https://www.dropbox.com/s/icdw0bicbo3mzts/Monero%20leaks%202.trace.zip?dl=0

Expected result:
No leaks.

Notes:
Unzip and open file with Apple Instruments (part of Xcode tools).

# Discussion History
## sanderfoobar | 2018-03-30T10:49:58+00:00
Thanks for your submission(s).

Please collect all memory leaks you have submitted into one big issue. This is better for visibility. I also believe most of the issues you submitted are out of scope, as they're QT related. Tagging this as wontfix.

## sanderfoobar | 2018-03-30T10:50:03+00:00
+wontfix

# Action History
- Created by: rex4539 | 2018-02-05T14:55:24+00:00
- Closed at: 2018-03-30T10:54:19+00:00
