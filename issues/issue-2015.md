---
title: sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
source_url: https://github.com/xmrig/xmrig/issues/2015
author: spitrip82
assignees: []
labels: []
created_at: '2020-12-30T19:39:11+00:00'
updated_at: '2021-01-10T01:00:53+00:00'
type: issue
status: closed
closed_at: '2021-01-10T01:00:53+00:00'
---

# Original Description
i have this error :

root@cloud-7761d2:~# sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-devsudo: unable to resolve host cloud-7761d2.managed-vps.net: Invalid argument
Reading package lists... Done
Building dependency tree
Reading state information... Done
build-essential is already the newest version (12.5ubuntu2).
git is already the newest version (1:2.19.1-1ubuntu1.1).
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 cmake : Depends: libstdc++6 (>= 9) but 8.3.0-6ubuntu1~18.10.1 is to be installed
E: Unable to correct problems, you have held broken packages.
root@cloud-7761d2:~#

how can i fix it ?

# Discussion History
# Action History
- Created by: spitrip82 | 2020-12-30T19:39:11+00:00
- Closed at: 2021-01-10T01:00:53+00:00
