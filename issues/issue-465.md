---
title: CPU Affinity and AMD Threadripper Config
source_url: https://github.com/xmrig/xmrig/issues/465
author: jlaranjeiro
assignees: []
labels:
- NUMA
created_at: '2018-03-20T18:38:56+00:00'
updated_at: '2018-11-05T14:36:17+00:00'
type: issue
status: closed
closed_at: '2018-11-05T14:35:45+00:00'
---

# Original Description
After reading dozens of post i finally discover how to set affinity, please change on your instructions that to work the command must be: --cpu-affinity 0x(+HEX), i knew how to use the HexCalculator to identify them, but only after 20 post I understood i need to use the 0x before the Hexadecimal code, it was not clear for me on your help post.

Threadripper 1950x (32 Cores does not work with this version. After a few trials and errors i understood that the only possible solution is to run 2 separate  instances with different affinity on them. This most likely is a sub-optimal use of the software, so i am getting less 40H/s compared with my faithful companion of the last months XMR stak. Here I post my config commands for others who seek the same answers:

Instance 1:
xmrig.exe --print-time 15  --cpu-priority 2 --cpu-affinity 0x00005555 (or 0x0000AAAA) -t 8 -o xxxx -u xxxx -p x 

Instance 2:
xmrig.exe --print-time 15  --cpu-priority 2 --cpu-affinity 0x55550000 (or 0xAAAA0000) -t 8 -o xxxx -u xxxx -p x 

# Discussion History
## rmg8192 | 2018-03-22T01:36:20+00:00
Thats not an ideal solution...

I was getting 650+ per numa node on centos7.
I've switched to windows temporarily with my 1950x becuase i have 4x RX550s which just dont work atm with openCL on linux..

anyhow, I'm using the following to get 650H/s+ per numa block on windows..
create 2 files , eg numa0 and numa1.
start_numa0.bat 
@echo off
start /node 0 /affinity 0x00005555 xmrig.exe  -c numa0.json
pause

start /node 1 /affinity 0x5555 xmrig.exe  -c numa1.json

config files are default apart from threads : 8 and log file : numa[01].log

This locks the numa banks to the respective DIMMS. decreasing latency which gives more H/s.
on my X399 Taichi, the MOBO recommends for two dimms putting both on one side, Ive found that splitting one DIMM per "socket" for TR is better.

My TR4 with just the above is giving 1300 +- 10 on xmrig2.5

# Action History
- Created by: jlaranjeiro | 2018-03-20T18:38:56+00:00
- Closed at: 2018-11-05T14:35:45+00:00
