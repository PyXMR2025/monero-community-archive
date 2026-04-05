---
title: epyc 7502
source_url: https://github.com/xmrig/xmrig/issues/2190
author: Aspalatos
assignees: []
labels: []
created_at: '2021-03-17T17:44:05+00:00'
updated_at: '2021-04-12T13:55:11+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:55:11+00:00'
---

# Original Description
Is there a way to run randomx booster on epyc cpu?
my 7502 shows unsupported CPU.
Thanks

# Discussion History
## Lonnegan | 2021-03-17T22:27:12+00:00
Can you post a screenshot please and give A LITTLE BIT more information what you mean? ;)

## Aspalatos | 2021-03-18T11:17:32+00:00
When I'm mining monero with ryzen or intel cpu randomx booster gives me 20% performance boost in hashrate but when I try to install same randomx booster on epyc cpu its not working. at the end it states not supported cpu. This is what happens when i run randomx booster scrypt.

-----------------------------------------------------------------------------------------------

tool 'msr-tools  numactl' not found, r.sh is trying to install the dependency
execute: apt-get --no-install-recommends --yes install msr-tools  numactl
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  msr-tools numactl
0 upgraded, 2 newly installed, 0 to remove and 34 not upgraded.
Need to get 48.5 kB of archives.
After this operation, 195 kB of additional disk space will be used.
Get:1 http://de.archive.ubuntu.com/ubuntu focal/main amd64 msr-tools amd64 1.3-3 [10.0 kB]
Get:2 http://de.archive.ubuntu.com/ubuntu focal/main amd64 numactl amd64 2.0.12-1 [38.5 kB]
Fetched 48.5 kB in 0s (222 kB/s)   
Selecting previously unselected package msr-tools.
(Reading database ... 207806 files and directories currently installed.)
Preparing to unpack .../msr-tools_1.3-3_amd64.deb ...
Unpacking msr-tools (1.3-3) ...
Selecting previously unselected package numactl.
Preparing to unpack .../numactl_2.0.12-1_amd64.deb ...
Unpacking numactl (2.0.12-1) ...
Setting up numactl (2.0.12-1) ...
Setting up msr-tools (1.3-3) ...
Processing triggers for man-db (2.9.1-1) ...

No supported CPU detected

active 2 MiB pages
execute: sysctl -w vm.nr_hugepages=1280
vm.nr_hugepages = 1280
Error: not enough 2 MiB pages 48/1280

activate 1 GiB pages
execute: echo 3 > /sys/kernel/mm/hugepages/hugepages-1048576kB/nr_hugepages

------------------------------------------------------------------------------------------------------------------------------

And this is my CPU

Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
Address sizes:                   43 bits physical, 48 bits virtual
CPU(s):                          64
On-line CPU(s) list:             0-63
Thread(s) per core:              2
Core(s) per socket:              32
Socket(s):                       1
NUMA node(s):                    1
Vendor ID:                       AuthenticAMD
CPU family:                      23
Model:                           49
Model name:                      AMD EPYC 7502P 32-Core Processor
Stepping:                        0
Frequency boost:                 enabled
CPU MHz:                         2896.509
CPU max MHz:                     2500.0000
CPU min MHz:                     1500.0000
BogoMIPS:                        4990.81
Virtualization:                  AMD-V
L1d cache:                       1 MiB
L1i cache:                       1 MiB
L2 cache:                        16 MiB
L3 cache:                        128 MiB
NUMA node0 CPU(s):               0-63

## SChernykh | 2021-03-18T11:25:57+00:00
You can just run xmrig as root, no need to use randomx_boost.sh. But if you really want to, you can change `AMD Ryzen` to `AMD EPYC` in the script to make it work.

## Aspalatos | 2021-03-18T11:38:20+00:00
I tried but anyway it says not supported CPU for randomx booster. Im getting 22kh for epyc 32 core and 28kh for 24 core ryzen lol

## Lonnegan | 2021-03-18T14:12:37+00:00
Don't use randomx booster! xmrig has integrated MSR mod function. You just have to....
- run xmrig unmodified or the official binary
- run xmrig as admin
- not run xmrig in a VM
- set MSR mod to true in the config.json

I have 14 kH/s with a Zen 2 12 core at stock w/o OC, so your 28 kH/s with a Zen 2 24 core is exactly what the hashrate should be. But you won't get 37 H/s with a Zen 2 Epyc 32 core  even with MSR mod, because clock speed of the Epyc is much lower than Ryzen and Ryzen Threadripper. But you are right, it should be more than 22 kH/s. When you use the integrated MSR function of xmrig, you will get it. ~29 kH/s should be realistic.

## Aspalatos | 2021-03-18T14:28:38+00:00
 "rdmsr": true,
 "wrmsr": true,

This is the only msr text I could find in config.json
Its already true.
Im root user
maybe this is how this CPU performs and thats about it

## Lonnegan | 2021-03-18T14:30:11+00:00
Can you please post a screenshot of the start of xmrig till the first hashrate display?

## Aspalatos | 2021-03-18T14:34:53+00:00
![epyc](https://user-images.githubusercontent.com/56341710/111643613-61abee80-87ff-11eb-9f02-3d1df55da6e0.png)


## Aspalatos | 2021-03-18T14:36:04+00:00
hmm now shows 26kH/s

## Lonnegan | 2021-03-18T14:44:16+00:00
Ok, it looks alright:

HUGE PAGES support = ok
ASSEMBLY ryzen = ok
msr register values for ryzen 17h successfully = ok (THAT's THE RANDOMX BOOSTER)
allocated huge pages 100% +JIT = ok
huge pages memory 100% = ok
64 threads using 131072 KB of cache = ok

The configuration of the miner is fine.

Your EPYC can boost up to 3.3 GHz turbo. The question is, if it does or if the frequency is much lower due to TDP limits. If it can run with 3.3 GHz, your hashrate should be about 29 kH/s. If it has to drop to its base frequency of 2.5 GHz, hashrate will be just 23 kH/s. Everything between 23-29 kH/s is possible depending of the clock frequency under full load.

Besides you have to check with top or htop, if any other process in the background eats up compute power.

## Aspalatos | 2021-03-18T15:02:09+00:00
Thanks guys !!

# Action History
- Created by: Aspalatos | 2021-03-17T17:44:05+00:00
- Closed at: 2021-04-12T13:55:11+00:00
