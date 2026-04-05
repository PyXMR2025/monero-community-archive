---
title: XMrig-4.3.1-beta shows garbage characters on Windows 7
source_url: https://github.com/xmrig/xmrig/issues/1241
author: kio3i0j9024vkoenio
assignees: []
labels:
- bug
created_at: '2019-10-13T21:24:10+00:00'
updated_at: '2019-10-24T22:32:20+00:00'
type: issue
status: closed
closed_at: '2019-10-24T22:32:20+00:00'
---

# Original Description
![XMrig-4 3 1-beta Garbage Screen](https://user-images.githubusercontent.com/35711866/66727156-ee7c9c80-ee02-11e9-8ff9-647e6379fb2d.JPG)
I have tried both the GCC and the MSVC version and both display garbage characters.


# Discussion History
## kio3i0j9024vkoenio | 2019-10-14T04:02:21+00:00
![xmrig-4 2 1-beta](https://user-images.githubusercontent.com/35711866/66728939-8089a280-ee0d-11e9-9317-ed2355f0a0d5.JPG)

This is version 4.2.1-beta that shows the correct characters so something is broken in 4.3.1-beta.

## 2010phenix | 2019-10-20T12:54:57+00:00
confirm
Test now 4.3.1 and same wrong charset color label
@kio3i0j9024vkoenio quick fix: use       --no-color or in json     "colors": false,

PS @xmrig exist another more big problem (first time see this in 3.x version), if need make new issue..
reproduce:
1. config Win 7 x64 \ Kaspersky Internet Security 18.0 \ xmrig 431
2. start xmrig (with param for example: xmrig -o rx.minexmr.com:4444 -u Wallet)
3. in first start miner activate KIS system security window about xmrig try read\make in registry HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\services\Tcpip\Parameters
4. add xmrig to make trusted (by hand - not auto)
5. miner start correct and do job
6. close miner (cmd window not close just hung) and you can't kill them even over task kill by PID only REBOOT windows system
 


## xmrig | 2019-10-20T17:05:02+00:00
Fixed.

6. How exactly you close the miner? it likely hugepages issue, why it happen is unknown might be some compatibility issues with KIS, disabling hugepages should help.
Thank you.

## 2010phenix | 2019-10-20T22:15:57+00:00
@xmrig just close on Х mouse сlick cmd window....
ok am test without hugepages... and write....

## 2010phenix | 2019-10-21T13:44:22+00:00
@xmrig, if disable hugepages miner close normal... Your guess correct, HugePage at miner close not clean or ....

-- cut --
E:\xmrig-4.3.1-beta>xmrig --no-color --no-huge-pages -o rx.minexmr.com:4444 -u xmr431
 * ABOUT        XMRig/4.3.1-beta gcc/9.2.0
 * LIBS         libuv/1.31.0 OpenSSL/1.1.1c hwloc/2.0.4
 * HUGE PAGES   permission granted
 * CPU          Intel(R) Core(TM) i5-2500 CPU @ 3.30GHz (1) x64 AES
                L2:1.0 MB L3:6.0 MB 4C/4T NUMA:1
 * DONATE       5%
 * ASSEMBLY     auto:intel
 * POOL #1      rx.minexmr.com:4444 algo auto
 * COMMANDS     'h' hashrate, 'p' pause, 'r' resume
 * OPENCL       disabled
[2019-10-21 16:26:36.665] use pool rx.minexmr.com:4444  138.201.21.239
[2019-10-21 16:26:36.665] new job from rx.minexmr.com:4444 diff 50000 algo rx/0
height 1325946
[2019-10-21 16:26:36.665]  rx   init dataset algo rx/0 (4 threads) seed 5e0d7664
cbeee71b...
[2019-10-21 16:26:36.665]  rx   allocated 2336 MB (2080+256) huge pages 0% 0/116
8 +JIT (0 ms)
[2019-10-21 16:26:45.186]  rx   dataset ready (8518 ms)
[2019-10-21 16:26:45.186]  cpu  use profile  rx  (3 threads) scratchpad 2048 KB
[2019-10-21 16:26:45.186]  cpu  READY threads 3/3 (3) huge pages 0% 0/3 memory 6
144 KB (2 ms)
[2019-10-21 16:27:54.878] new job from rx.minexmr.com:4444 diff 33333 algo rx/0
height 1325949
[2019-10-21 16:27:56.508] accepted (1/0) diff 33333 (42 ms)
[2019-10-21 16:28:50.822] speed 10s/60s/15m 918.7 921.9 n/a H/s max 926.4 H/s
[2019-10-21 16:28:58.752] new job from rx.minexmr.com:4444 diff 22222 algo rx/0
height 1325950
-- cut --

Inthis case maybe add for more informative...
 * HUGE PAGES   permission granted **but disable over config**

## xmrig | 2019-10-22T07:43:07+00:00
v4.4.0-beta with the fix released.

@2010phenix now miner will show `HUGE PAGES disabled` if it disabled by user.

# Action History
- Created by: kio3i0j9024vkoenio | 2019-10-13T21:24:10+00:00
- Closed at: 2019-10-24T22:32:20+00:00
