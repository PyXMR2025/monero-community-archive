---
title: File log problem in 2.6.2
source_url: https://github.com/xmrig/xmrig/issues/622
author: JustHoldit
assignees: []
labels: []
created_at: '2018-05-09T20:42:28+00:00'
updated_at: '2018-06-17T18:05:13+00:00'
type: issue
status: closed
closed_at: '2018-06-17T18:05:13+00:00'
---

# Original Description

XMRig 2.6.2
 built on May  9 2018 with GCC 7.2.1
 features: 64-bit AES
libuv/1.18.0

I have been using the following command line for a long time but after upgrading to 2.6.2 it fails. The process goes to the background but nothing ever writes to the file. I can't seem to figure out why.

--log-file=/var/log/rig.log --background

# Discussion History
## JustHoldit | 2018-05-09T20:51:39+00:00
I added:
    "log-file": "/var/log/rig.log",

to config.json and it is now working.

I will continue to mess around with getting it to work on the command line tonight.

# Action History
- Created by: JustHoldit | 2018-05-09T20:42:28+00:00
- Closed at: 2018-06-17T18:05:13+00:00
