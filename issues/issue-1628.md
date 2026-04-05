---
title: latest xmrig does not freeup memory on exit
source_url: https://github.com/xmrig/xmrig/issues/1628
author: thagrisu
assignees: []
labels: []
created_at: '2020-04-01T09:49:42+00:00'
updated_at: '2021-04-12T14:58:51+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:58:51+00:00'
---

# Original Description
**Describe the bug**
In current version when killing the xmrig process the memory for randomx algo is still allocated.
XMRig 5.3.0 doesn't have this issue.

**To Reproduce**
free -h before xmrig
start xmrig check memory again with free -h (arround 2,1G will be allocated by xmrig)
kill xmrig and check with free -h -> Memory still allocated

**Expected behavior**
Freeup memory on exit

**Required data**
- Randomx CPU Algo with hugepages enabled
 - Linux ubuntu 16.04 OS


# Discussion History
## thagrisu | 2020-04-01T12:42:27+00:00
i can confirm that this issue only occurs when u start xmrig as root.  Which seems to be necessary in order for wrmsr options to take affect

otherwise u need to load module manualy and apply wrmsr -a 0x1a4 6  as root then starting xmrig as normal user to gain max speed on randomx

# Action History
- Created by: thagrisu | 2020-04-01T09:49:42+00:00
- Closed at: 2021-04-12T14:58:51+00:00
