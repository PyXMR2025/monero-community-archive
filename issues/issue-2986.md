---
title: Killed process due to oomkiller on ubuntu 21
source_url: https://github.com/xmrig/xmrig/issues/2986
author: nlzrk
assignees: []
labels:
- question
created_at: '2022-03-23T03:24:19+00:00'
updated_at: '2022-04-03T07:45:11+00:00'
type: issue
status: closed
closed_at: '2022-04-03T07:45:11+00:00'
---

# Original Description

A clear and concise description of what the bug is.
So whenever I boot up xmrig it runs for a few seconds then it stops working with the simple message: Killed. Ive discovered with dmesg that oomkiller has been stopping the process. (Running i5 5th gen, 4GB ram. (old macbook))





# Discussion History
## Spudz76 | 2022-03-23T07:00:42+00:00
RandomX requires 2.5GB+ so it's probably not lying...

## nlzrk | 2022-03-23T07:23:26+00:00
I have 4GB of ddr3

## SChernykh | 2022-03-23T10:32:37+00:00
And these 4 GB are most likely already taken by OS and other programs. You need 2.5 GB of **free** memory.

# Action History
- Created by: nlzrk | 2022-03-23T03:24:19+00:00
- Closed at: 2022-04-03T07:45:11+00:00
