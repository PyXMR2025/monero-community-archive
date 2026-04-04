---
title: Raspberry Pi 3 B+ ARMv8 build with NO_AES
source_url: https://github.com/monero-project/monero/issues/5782
author: Kryptoxic
assignees: []
labels: []
created_at: '2019-07-30T04:46:31+00:00'
updated_at: '2019-08-05T01:15:41+00:00'
type: issue
status: closed
closed_at: '2019-08-05T01:15:41+00:00'
---

# Original Description
Hi, I have been having trouble with the armv8 prebuilt binaries so I decided to do some research and I ended up finding the following issue.

https://github.com/monero-project/monero/issues/2858

One of the solution that was mentioned in that particular issue is to build monero with NO_AES. I was just wondering, how do I run cmake with the NO_AES flag. I have tried "cmake NO_AES ." and it does not work. Thanks in advance!

# Discussion History
## vtnerd | 2019-07-31T03:01:51+00:00
Try `cmake -DNO_AES`.

## Kryptoxic | 2019-08-05T01:15:41+00:00
It didn't work. After it compiled, I kept getting a core dumped. Either way, I switched back to using armv7 on my raspberry pi

# Action History
- Created by: Kryptoxic | 2019-07-30T04:46:31+00:00
- Closed at: 2019-08-05T01:15:41+00:00
