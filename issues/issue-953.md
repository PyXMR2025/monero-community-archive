---
title: v2.13.1 inconsistent Hash Rate
source_url: https://github.com/xmrig/xmrig/issues/953
author: asylum119
assignees: []
labels: []
created_at: '2019-02-27T03:24:09+00:00'
updated_at: '2019-05-16T11:42:43+00:00'
type: issue
status: closed
closed_at: '2019-05-16T11:42:42+00:00'
---

# Original Description
Ubuntu 16 | Ryzen Thread Ripper | cn-pico/trtle | command line
same settings but seeing drastic hash rate drops (from 20KHs down to 3KHs), need to restart the xmrig commands until the hash rate is what is expected on xmrig load. 

asm ryzen and no asm command makes no difference to inconsistent hash rate on load

Been a bumpy road for AMD + cn-pico/trtle

# Discussion History
## asylum119 | 2019-03-03T08:24:45+00:00
Doesn't make sense for one load to be 3KHs and another exact same load to be the expected 20KHs.

I have rolled xmrig back and turned off automatic xmrig updates while mining the cn-pico/trtle algo, not a fan of removing automation but can now be confident in hash rate if unattended-upgrades triggers a system reboot.

## asylum119 | 2019-03-06T04:52:16+00:00
Editing my startup script to wait for the CPU temp to be at a cold boot value and adding extended sleep times before and after loading xmrig is giving me some confidence that the hash rate will load and stay in the ball park with each load.

Although a stable hash rate without so much wait time would be great, **feel free to squish this issue**







## asylum119 | 2019-03-07T07:38:23+00:00
Just upgraded to 2.14 and again low hash rate, am I loading it wrong or AMD just not supported properly ?

xmrig compiled/build/./xmrig --algo=cn-pico/trtl --threads=24 --url=<pool:port> --user=<wallet> --pass=<name>--keepalive --background

New Version loads at 6KHs or 20KHs and is again unpredictable, just need to keep restarting it until it works as expected lol

## asylum119 | 2019-03-11T18:08:12+00:00
V2.14.1
First load 700 Hs
Second load 2.20 KHs
Third load 1 KHs
Forth load is expected 20KHs




## asylum119 | 2019-03-18T07:47:04+00:00
Replaced --background with & to then load xmrig-amd. Have had three system reboots with the expected hash rate which would never had been the case when using --background to then load the and miner. 





## asylum119 | 2019-05-16T11:42:42+00:00
upgraded Ubuntu 16  to Ubuntu 18 and switched from OpenCL + AMDGPU-PRO  to ROCm
CPU now loads with expected hash rate mining cn-pico/trtle on every boot

# Action History
- Created by: asylum119 | 2019-02-27T03:24:09+00:00
- Closed at: 2019-05-16T11:42:42+00:00
