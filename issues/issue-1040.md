---
title: Memory leak in setProtocolMetadataWithSignature
source_url: https://github.com/monero-project/monero-gui/issues/1040
author: rex4539
assignees: []
labels:
- wontfix
created_at: '2017-12-23T06:59:26+00:00'
updated_at: '2018-03-30T12:00:24+00:00'
type: issue
status: closed
closed_at: '2018-03-30T12:00:24+00:00'
---

# Original Description
GUI version: v0.11.1.0
Embedded Monero version: v0.11.1.0-2-gc328163

Steps:
Launch Monero GUI.

What happened:
Memory leak in setProtocolMetadataWithSignature

https://www.dropbox.com/s/c2orrbv5vionwnh/Monero%20leaks.trace.zip?dl=0

Expected result:
No leaks.

Notes:
Unzip and open file with Apple Instruments (part of Xcode tools).

# Discussion History
## sanderfoobar | 2018-03-30T10:51:14+00:00
Thanks for your submission(s).

Please collect all memory leaks you have submitted into one big issue. This is better for visibility. I also believe most of the issues you submitted are out of scope, as they're QT related. Tagging this as wontfix.

## sanderfoobar | 2018-03-30T10:51:20+00:00
+wontfix

# Action History
- Created by: rex4539 | 2017-12-23T06:59:26+00:00
- Closed at: 2018-03-30T12:00:24+00:00
