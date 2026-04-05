---
title: segmentation fault on centos 6.01
source_url: https://github.com/xmrig/xmrig/issues/2248
author: NirHeaven
assignees: []
labels:
- question
- need feedback
created_at: '2021-04-08T16:15:54+00:00'
updated_at: '2022-04-03T14:40:55+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:40:55+00:00'
---

# Original Description
I download xmrig-6.11.1-linux-x64.tar.gz and run ./xmrig on centos 6.1, I get segmentation fault

# Discussion History
## xmrig | 2021-04-08T16:27:59+00:00
You should use `xmrig-6.11.1-linux-static-x64.tar.gz` on such old system.
Thank you.

## NirHeaven | 2021-04-09T02:08:59+00:00
I have tried, but also got segmentation fault, by the way , the centos version is release 7.2.1511 (Core)

## NirHeaven | 2021-04-12T02:08:33+00:00
hello, is there anyone can help me?

## xmrig | 2021-04-12T13:33:52+00:00
Unlikely, you did not provide any other details and the OS is very old.

## NirHeaven | 2021-04-13T06:24:28+00:00
How can I get the informations you want to check this problem?all I get is segmentation fault when I ran the bin

## NirHeaven | 2021-04-13T06:32:58+00:00
CPU version is Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz


## NirHeaven | 2021-04-13T06:34:16+00:00
the number of unique physical cpu id is [0,1] and the number of processor is 16

# Action History
- Created by: NirHeaven | 2021-04-08T16:15:54+00:00
- Closed at: 2022-04-03T14:40:55+00:00
