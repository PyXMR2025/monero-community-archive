---
title: armv7l architecture once again gives bus error
source_url: https://github.com/xmrig/xmrig/issues/3657
author: allisonmeow
assignees: []
labels:
- arm
created_at: '2025-05-14T19:27:58+00:00'
updated_at: '2025-06-28T10:24:47+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:24:47+00:00'
---

# Original Description
**Describe the bug**
bus error on armv7l on latest build

**To Reproduce**
- `qemu-arm xmrig-armv7l -o pool:80`
- wait one second
- `uncaught target signal 7 (Bus error) - core dumped`
- `terminated by signal SIGBUS (Misaligned address error)`
- profit

**Expected behavior**
that it would run?

**Required data**
 - XMRig version: latest (6.22.2)
- OS: doesnt matter, tried on android and recreated in qemu-arm

**Additional context**
none


# Discussion History
## allisonmeow | 2025-05-14T22:11:06+00:00
compiled a static version from the most recent related "fix" (#2904)  and still, same issue
(this took an 1 hour and 51 minutes off my life 👍)

## SChernykh | 2025-05-15T06:18:05+00:00
Did it work before? armv7l is not something we ever tested.

## allisonmeow | 2025-05-15T15:57:55+00:00
unsure I think I remember it working at some point? theres github issues regarding armv7l 

## allisonmeow | 2025-05-15T16:03:24+00:00
also i think the vast majority of low end android phones run armv7l i think i remember compiling it on an old phone with armv7l 

# Action History
- Created by: allisonmeow | 2025-05-14T19:27:58+00:00
- Closed at: 2025-06-28T10:24:47+00:00
