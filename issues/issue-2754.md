---
title: 'Fails to start mining RTM '
source_url: https://github.com/xmrig/xmrig/issues/2754
author: tommyprevatt
assignees: []
labels: []
created_at: '2021-11-29T19:02:32+00:00'
updated_at: '2021-11-29T19:20:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
When mining RTM with 12600K it stops right after saying "register values for "intel" preset have been set successfully." Same issue occurs using the command line/cmd file or the config file. 
6.16.0 ran fine using the same command. Likewise, 6.16.1 seems to work fine with Monero/RandomX.

**To Reproduce**
run command "xmrig.exe -a gr -o stratum.us-la1.suprnova.cc:6273 -u wallet_id -p x" with i5-12600k. 

**Expected behavior**
It should run and start mining

**Required data**
Windows
i5-12600K Alder Lake CPU

Output:
D:\Miners\xmrig-6.16.1>xmrig.exe -a gr -o stratum.us-la1.suprnova.cc:6273 -u WALLET_ID -p x
 * ABOUT        XMRig/6.16.1 gcc/10.1.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          12th Gen Intel(R) Core(TM) i5-12600K (1) 64-bit AES
                L2:9.5 MB L3:20.0 MB 10C/16T NUMA:1
 * MEMORY       5.0/15.8 GB (32%)
                Controller0-ChannelA-DIMM0: <empty>
                Controller0-ChannelA-DIMM1: 8 GB DDR4 @ 3600 MHz F4-3600C16-8GVKC
                Controller1-ChannelA-DIMM0: <empty>
                Controller1-ChannelA-DIMM1: 8 GB DDR4 @ 3600 MHz F4-3600C16-8GVKC
 * MOTHERBOARD  Micro-Star International Co., Ltd. - PRO Z690-A WIFI DDR4(MS-7D25)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      stratum.us-la1.suprnova.cc:6273 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-11-29 13:50:44.229]  net      use pool stratum.us-la1.suprnova.cc:6273  66.165.237.58
[2021-11-29 13:50:44.229]  net      new job from stratum.us-la1.suprnova.cc:6273 diff 3277 algo ghostrider height 195057
[2021-11-29 13:50:44.517]  msr      register values for "intel" preset have been set successfully (288 ms)

D:\Miners\xmrig-6.16.1>pause
Press any key to continue . . .


# Discussion History
## tommyprevatt | 2021-11-29T19:13:38+00:00
I realized I grabbed the GCC build. I just downloaded the MSVC build and it runs perfectly fine. I'll leave it to you to determine if that's expected behavior and this issue should be closed. 

## SChernykh | 2021-11-29T19:20:12+00:00
I confirm the GCC build crashes, we'll look into it.

# Action History
- Created by: tommyprevatt | 2021-11-29T19:02:32+00:00
