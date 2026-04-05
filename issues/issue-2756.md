---
title: --rig-id not compatible with RTM and flockpool
source_url: https://github.com/xmrig/xmrig/issues/2756
author: duhd1993
assignees: []
labels: []
created_at: '2021-11-29T22:50:10+00:00'
updated_at: '2021-11-29T23:04:22+00:00'
type: issue
status: closed
closed_at: '2021-11-29T23:04:22+00:00'
---

# Original Description
**Describe the bug**
A clear and concise description of what the bug is.

When specifying worker name with --rig-id using xmrig, the name is not reflected on flockpool. While using the cpuminer, the name is reflected on flockpool.

**To Reproduce**
Steps to reproduce the behavior.

``./xmrig -a gr -o us.flockpool.com:5555 --tls -u xxxx --rig-id worker1``

**Expected behavior**
A clear and concise description of what you expected to happen.

The name worker1 is shown on flockpool

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## Lonnegan | 2021-11-29T23:00:48+00:00
Please read the help section of the pool! Flockpool doesn't support --rig-id. You have to put the worker's name behind the RTM address, separated by a point.

And: other miners are exclusively managed by command line options. xmrig instead has the config.json. It's better to config everything there and just start xmrig without any parameters!

## duhd1993 | 2021-11-29T23:04:22+00:00
OK. Thanks. I know that. I thought that's just different command line format of different miners. 

# Action History
- Created by: duhd1993 | 2021-11-29T22:50:10+00:00
- Closed at: 2021-11-29T23:04:22+00:00
