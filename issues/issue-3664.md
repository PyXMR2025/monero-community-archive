---
title: Amd ryzen 5600gt on new release 2.22.3
source_url: https://github.com/xmrig/xmrig/issues/3664
author: tomaselpepe25
assignees: []
labels:
- bug
- randomx
created_at: '2025-06-07T03:06:51+00:00'
updated_at: '2025-06-21T05:00:59+00:00'
type: issue
status: closed
closed_at: '2025-06-16T18:51:17+00:00'
---

# Original Description
**Describe the bug**
hashrate drop 1000 hashes and pc comsumption is 100%

**To Reproduce**
Just execute xmrig as usual but cpu performance is at 100% (normally is in 69% or 75% in between

**Expected behavior**
I expected to have more hashrate , or less ping.

**Required data**
 - XMRig version
2.22.3

just the normal wizard 



# Discussion History
## tomaselpepe25 | 2025-06-07T03:07:19+00:00
now im using an older version of xmrig and it works fine, will try again in a time 

## SChernykh | 2025-06-07T07:24:46+00:00
How many threads does XMRig run with the old and the new versions?

## tomaselpepe25 | 2025-06-07T20:48:31+00:00
Let me check that I will answer shortly!!

## Flussig29 | 2025-06-11T12:48:15+00:00
this bug is a problem for me also. I added a new build with latest version 6.22.3 and i was getting 3.567kH. Used a test flight sheet to force 6.22.2 and getting 4.789kH.

![Image](https://github.com/user-attachments/assets/b92ad3a2-2cbb-41bd-a2bb-507c966db5c6)
![Image](https://github.com/user-attachments/assets/b803ce32-84c0-40bb-b243-fc163a2e0b67)

## SChernykh | 2025-06-11T12:54:45+00:00
@Flussig29  what CPU? v6.22.2 uses 8 threads, and v6.22.3 uses 10 threads, right?

## Flussig29 | 2025-06-11T12:57:17+00:00
cpu i'm using is Ryzen 5 5600G, 6/12

## SChernykh | 2025-06-11T16:38:40+00:00
This should be fixed in #3665

## tomaselpepe25 | 2025-06-21T05:00:59+00:00
thank you guys. Checking it now !!! 

# Action History
- Created by: tomaselpepe25 | 2025-06-07T03:06:51+00:00
- Closed at: 2025-06-16T18:51:17+00:00
