---
title: v0.17.1.7 private Monero Node dumps itself with a "killed" message.
source_url: https://github.com/xmrig/xmrig/issues/2006
author: agentpatience
assignees: []
labels:
- invalid
created_at: '2020-12-24T23:47:08+00:00'
updated_at: '2020-12-25T08:25:06+00:00'
type: issue
status: closed
closed_at: '2020-12-25T08:25:06+00:00'
---

# Original Description
**Describe the bug**

Node is "killed" unexpectedly when starting the node and running a miner on localhost to the listening node on the same hardware.

**To Reproduce**
Start a node with Ubuntu 20.10 and mine to it on the same machine using XMrig?

**Expected behavior**

After about 10 minutes system will dump "Killed" to listening shell

Required data**
 - Miner log as text or screenshot ----- See attached.
 - Config file or command line (without wallets)
 - OS: Linux Ubuntu 20.10

**Additional context**

I reduced miner thread count to 34 instead of 36 for E5-2695 V4 via --threads=34 

The problem with node dumping and "killed" message persists.

![killed](https://user-images.githubusercontent.com/36264810/103111186-41153380-4618-11eb-94b7-ff08b1fa935e.jpg)


# Discussion History
## agentpatience | 2020-12-24T23:56:02+00:00
start.sh consists of the following:
./xmrig --donate-level 1 --threads=34 -o 192.168.2.166:18081 -u <address> --coin monero --daemon --daemon-poll interval=5000


## agentpatience | 2020-12-25T02:09:17+00:00
This bug report relates to a current Monero network attack.

## xmrig | 2020-12-25T08:25:06+00:00
Small hint for future, please don't use `--threads` option without `--cpu-affinity` on NUMA hardware like yours, without proper affinity miner will not be able to bind memory to specific node and you will lose benefit of multiple RandomX datasets.
Thank you.

# Action History
- Created by: agentpatience | 2020-12-24T23:47:08+00:00
- Closed at: 2020-12-25T08:25:06+00:00
