---
title: Topology became empty, aborting!
source_url: https://github.com/xmrig/xmrig/issues/3340
author: fohnbit
assignees: []
labels: []
created_at: '2023-09-29T08:00:55+00:00'
updated_at: '2025-06-16T19:56:27+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:56:27+00:00'
---

# Original Description
Hello!

I try to build on my Ubuntu Server:
 **cat /etc/*release**

```
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.7 LTS"
NAME="Ubuntu"
VERSION="16.04.7 LTS (Xenial Xerus)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 16.04.7 LTS"
VERSION_ID="16.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
VERSION_CODENAME=xenial
UBUNTU_CODENAME=xenial
18.0.21.5
Plesk Obsidian 18.0

```

I used this commands:
```
sudo apt-get install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build && cd xmrig/build
cmake ..
make -j$(nproc)
```

I get this error:
`root@dlc:/xmrig# /xmrig/xmrig
Topology became empty, aborting!
Aborted
`

I don´t find anything in the web about this error

# Discussion History
## fohnbit | 2023-09-29T08:22:12+00:00
edit: seems it is a problem with hwloc

## SChernykh | 2023-09-29T08:47:29+00:00
Ubuntu 16.04 is not supported anymore, and I don't know how old is the hwloc version that they use. You could try to manually build all dependencies: https://xmrig.com/docs/miner/build/ubuntu - use "Advanced build" steps.

## fohnbit | 2023-09-29T08:51:10+00:00
Oh, ok. Thank you!

# Action History
- Created by: fohnbit | 2023-09-29T08:00:55+00:00
- Closed at: 2025-06-16T19:56:27+00:00
