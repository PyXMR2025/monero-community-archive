---
title: BUG Report , Taskkill wont work with xmrig
source_url: https://github.com/xmrig/xmrig/issues/2950
author: mr-459
assignees: []
labels: []
created_at: '2022-03-01T10:01:49+00:00'
updated_at: '2022-04-03T08:01:21+00:00'
type: issue
status: closed
closed_at: '2022-04-03T08:01:21+00:00'
---

# Original Description
**Describe the bug**
when you run taskkill /IM xmrig.exe /T
it wont kill xmrig and you need to force xmrig to kill
witch is not what i want

**To Reproduce**
i have no idea

**Expected behavior**
xmrig gets killed like when you press ctrl+c

**Required data**
 - video of explaining bug : https://ufile.io/jioondsw
 - OS: Windows 11.




# Discussion History
## timk74 | 2022-03-01T11:13:53+00:00
taskkill /im xmrig.exe /f

## mr-459 | 2022-03-01T12:00:24+00:00


> taskkill /im xmrig.exe /f

bro , are you idiot?
i dont want to kill by force
because an upstream will remain on my xmrig-proxy server (because of simple mode)
im not searching for way to kill , im searching for fix of bug

## Spudz76 | 2022-03-01T14:25:38+00:00
Connections do not outlive a dead process regardless which way you kill it?

## mr-459 | 2022-03-01T18:49:17+00:00
> 

when i exit xmrig.exe by ctrl+c , they outlive
but when i force it , they dont
and i see many many workers on my xmrig-proxy , while they are not really workers

# Action History
- Created by: mr-459 | 2022-03-01T10:01:49+00:00
- Closed at: 2022-04-03T08:01:21+00:00
