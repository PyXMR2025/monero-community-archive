---
title: fix FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW xmrig on ubuntu
source_url: https://github.com/xmrig/xmrig/issues/2617
author: MCLB961
assignees: []
labels: []
created_at: '2021-10-06T05:22:57+00:00'
updated_at: '2022-05-17T15:48:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
hello, everyone
I run my miner on ubuntu os and I have this error  FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW. 
anyone can help me 

# Discussion History
## Lonnegan | 2021-10-06T05:29:56+00:00
You have to run xmrig as root with full rights and bare metal, not in a VM. Otherwise MSR mod can't be applied.

## MCLB961 | 2021-10-06T05:31:45+00:00
i running on VPS on Digital ocean. it's profitable or not ?

## someview | 2021-10-29T06:31:03+00:00
I have the same problem.vps ubuntu18.04,use root to run sh,but mentioned  
'cannot read MSR 0x000001a4
 FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
'


## SChernykh | 2021-10-29T06:34:31+00:00
MSR mod needs real hardware to work. Not a virtual machine, not a VPS, not a "Memory integrity on" in Windows - these all turn virtualization on and disable MSR.

## SChernykh | 2022-05-17T15:48:02+00:00
It shouldn't reboot with MSR mod on Intel because XMRig uses only the officially documented CPU registers on Intel systems and shutdown/reboot is not part of what's documented there. Your system is most likely unstable and can't handle RandomX mining load.

# Action History
- Created by: MCLB961 | 2021-10-06T05:22:57+00:00
