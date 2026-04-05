---
title: some questions
source_url: https://github.com/xmrig/xmrig/issues/2471
author: APT-ZERO
assignees: []
labels: []
created_at: '2021-07-04T22:53:44+00:00'
updated_at: '2021-07-06T20:39:59+00:00'
type: issue
status: closed
closed_at: '2021-07-06T20:39:59+00:00'
---

# Original Description
1- is it better to enable KeepAlive or not? what is the benefits?

2- in old versions of xmrig, i had to use --cpu-affinity on CPUs with Hyperthreading
in new versions hash rate is good without using --cpu-affinity
do xmrig detect real cores and only uses them by default?
is this because of autoconfig feature? will autoconfig disabled when i config it myself?

3- can DMI/SMBIOS reader make problems [BSOD, Anti virus false positive,etc.]? is there any report about it?

4- how --pause-on-active works?
will miner stop when user is active but mouse cursor is idle for some minutes/hours?
will it stop when a user is running xmrig and it's disconnected but another user is active?
will it stop miner when user is active but session is rdp or console?
is miner tracking windows events to work or stop, or it will check users like qwinsta?

# Discussion History
## SChernykh | 2021-07-04T22:58:14+00:00
Anti viruses always detect xmrig no matter what you do.
Re 4: https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getlastinputinfo


## APT-ZERO | 2021-07-06T09:49:40+00:00
no other answers? :(

## snipeTR | 2021-07-06T17:19:13+00:00
1-https://xmrig.com/docs/extensions/keepalive
2-https://github.com/xmrig/xmrig/issues/1077
4-https://github.com/xmrig/xmrig/issues/1781
all the answers are already here, you need to know how to search.

# Action History
- Created by: APT-ZERO | 2021-07-04T22:53:44+00:00
- Closed at: 2021-07-06T20:39:59+00:00
