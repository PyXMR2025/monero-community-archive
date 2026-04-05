---
title: DeroKnight Algo addition
source_url: https://github.com/xmrig/xmrig/issues/1311
author: Notoriousjoshyb
assignees: []
labels:
- wontfix
created_at: '2019-11-24T09:50:20+00:00'
updated_at: '2019-12-22T19:38:52+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:38:52+00:00'
---

# Original Description
Hey, Please can you add ability to mine DeroKnight CPU/GPU. Thanks https://github.com/deroproject/documentation/blob/master/testnet/DeroKnight.md

DeroKnight is same as original CryptoNight but works by decreasing the efficiency of ASICs to match with GPUs.
Efficiency of ASICs are decreased by adding an extra rule in DeroKnight to force nonce to be multiples of 101.
Assuming that all ASICs generate nonce sequentially or randomly but do not have the capability to generate nonce of specific series and cannot be reprogrammed.
This extra rule can be implemented in few lines for CPUs and GPUs without any extra load.

So with (nonce mod 101 == 0) current ASICs effcacy will be down to 1/100 times.

Current CryptoNight Asic of 200KHs will deliver 2KHs of DeroKnight.
GPU/CPU will have no extra performance cost and will deliver almost similar hashrate on CryptoNight and DeroKnight.

Note For GPU/CPU software developers:

DeroKnight POW is CryptoNight original only, There is no change in POW.
To support DeroKnight in your miner softwares increment nonce in steps of 101.
Take initial point whose mod 101 is == 0.


# Discussion History
## SChernykh | 2019-11-24T13:42:23+00:00
There are bitstreams for FPGAs that can do 22-28 KH/s on original Cryptonight @ 150 watts, CPU/GPU won't be competitive. There are a few thousand BCU1525s that will just dominate your network from day 1, I don't see a point to add support to XMRig. And I'm not sure that original Cryptonight ASICs can't change their nonce selection logic. Yes, the whole algorithm is hardwired there, but nonce selection is a separate logic, it can be anything there.

# Action History
- Created by: Notoriousjoshyb | 2019-11-24T09:50:20+00:00
- Closed at: 2019-12-22T19:38:52+00:00
