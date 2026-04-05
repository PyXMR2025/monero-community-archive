---
title: xmrig does`t stop without devices
source_url: https://github.com/xmrig/xmrig/issues/1550
author: Amf1k
assignees: []
labels:
- bug
created_at: '2020-02-13T04:48:32+00:00'
updated_at: '2021-04-12T15:01:34+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:01:34+00:00'
---

# Original Description
**Describe the bug**
When trying to start Xmrig, when it cannot find the devices (for example, the CPU is disabled and could not find the CUDA device), the miner starts to constantly reconnect to the pool

**To Reproduce**
Run xmrig with command "-o pool-url -u wallet --coin monero --no-cpu"

**Expected behavior**
Stop Xmrig with error "no devices"

**Required data**
![1](https://user-images.githubusercontent.com/4735986/74402404-f77b8a00-4e45-11ea-8ddd-b1b3fa6e8717.png)
 - Config file or command line (without wallets): -o pool-url -u wallet --coin monero --no-cpu
 - OS: Windows 10 v1903 build 18362.592

# Discussion History
# Action History
- Created by: Amf1k | 2020-02-13T04:48:32+00:00
- Closed at: 2021-04-12T15:01:34+00:00
