---
title: permission denied in truenas
source_url: https://github.com/xmrig/xmrig/issues/3656
author: cqw-acq
assignees: []
labels:
- question
created_at: '2025-05-14T11:20:51+00:00'
updated_at: '2025-06-16T15:08:12+00:00'
type: issue
status: closed
closed_at: '2025-06-16T15:08:12+00:00'
---

# Original Description
**Describe the bug**
it is just aways permission denied
**To Reproduce**
Steps to reproduce the behavior.

wget https://github.com/xmrig/xmrig/releases/download/v6.22.2/xmrig-6.22.2-linux-static-x64.tar.gz
tar -xvf xmrig-6.22.2-linux-static-x64.tar.gz
cd xmrig-6.22.2
./xmrig-6.22.2
now it will show zsh: permission denied: ./xmrig
after i use chmod 777 xmrig
and sudo ./xmrig it is aways permission denied

**Expected behavior**
A clear and concise description of what you expected to happen.

it should work

**Required data**
 - XMRig version 6.22.2
    - Either the exact link to a release you downloaded from https://github.com/xmrig/xmrig/releases
    - Or the exact command lines that you used to build XMRig
 - Miner log as text or screenshot
 zsh: permission denied: ./xmrig
 sudo: unable to execute ./xmrig: Permission denied

 - Config file or command line (without wallets)
 -  ./xmrig
 -  sudo ./xmrig
 - OS: [e.g. Windows] truenas 25.04
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2025-05-15T06:20:08+00:00
`chmod -R 755 xmrig-6.22.2` - this will change permission on the folder and everything in it. Also double check that your server is based on an x86 CPU (Intel/AMD) and not some ARM CPU. If it's ARM, you'll have to build XMRig from source.

# Action History
- Created by: cqw-acq | 2025-05-14T11:20:51+00:00
- Closed at: 2025-06-16T15:08:12+00:00
