---
title: Update build instructions for Fedora
source_url: https://github.com/xmrig/xmrig/issues/1682
author: mssc89
assignees: []
labels: []
created_at: '2020-05-20T05:59:08+00:00'
updated_at: '2020-08-28T16:26:32+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:26:32+00:00'
---

# Original Description
Build instructions for Fedora are stuck on version 25/26, they are quite ancient. I've compiled xmrig on Fedora 32, and there are two new depediencies which need to be installed with dnf before building:
`hwloc-devel openssl-devel`
Since i cannot make pull requests to wiki, can someone from team please update it to include these depediencies? Adding `-DUV_LIBRARY=/usr/lib64/libuv.a` to the cmake is also not required anymore.

# Discussion History
## downystreet | 2020-06-01T13:18:18+00:00
I agree.

## agentpatience | 2020-08-02T15:43:27+00:00
Hi Mssc89:

 #1796 I added a documentation update request for this. Can you share your instructions on a XMRig Build on Fedora 32?


## mssc89 | 2020-08-07T10:21:04+00:00
@agentpatience  you need to install `hwloc-devel openssl-devel` and remove `-DUV_LIBRARY=/usr/lib64/libuv.a` flag from the cmake. The rest is exactly the same as in wiki.

## xmrig | 2020-08-28T16:26:32+00:00
https://xmrig.com/docs/miner/build/fedora

# Action History
- Created by: mssc89 | 2020-05-20T05:59:08+00:00
- Closed at: 2020-08-28T16:26:32+00:00
