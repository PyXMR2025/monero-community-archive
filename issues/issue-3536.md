---
title: Stop your software to be usable as malware
source_url: https://github.com/xmrig/xmrig/issues/3536
author: zettberlin
assignees: []
labels:
- av
created_at: '2024-08-23T09:11:40+00:00'
updated_at: '2025-06-16T19:40:47+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:40:47+00:00'
---

# Original Description
**Describe the bug**
The software is used as cryptominer without permission or knowledge of the user

**To Reproduce**
Thousands of cases on all kinds of servers

**Expected behavior**
The software needs to announce its activity and implement some mechanism that forbids automatical installation

**Required data**
All versions

**Additional context**
Be aware, that the usage of your software is criminal.


# Discussion History
## geekwilliams | 2024-08-23T16:04:47+00:00
Most implementations use a modified version of xmrig or another miner bundled inside a malware payload.  Xmrig itself is not malware.  

## zettberlin | 2024-08-23T17:43:59+00:00
This is understood.
But can you think of any mechanism in xmrig, that makes it harder to abuse?

## SChernykh | 2024-08-23T19:46:55+00:00
XMRig is open source. Whatever "warning/confirmation" is implemented, will be easily removed by malware versions, because they will change the source code. XMRig itself doesn't try to hide in any way and it doesn't have an "automatic installation" feature.

## furinabagimlisibirisi | 2024-09-06T14:48:06+00:00
stfu lil bro

## TekuSP | 2024-09-28T13:45:09+00:00
Anything open source can turn into malware by just compiling it yourself.....

# Action History
- Created by: zettberlin | 2024-08-23T09:11:40+00:00
- Closed at: 2025-06-16T19:40:47+00:00
