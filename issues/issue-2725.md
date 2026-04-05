---
title: Ghostrider fail when number of threads is passed
source_url: https://github.com/xmrig/xmrig/issues/2725
author: marcusfpereira
assignees: []
labels:
- bug
created_at: '2021-11-26T22:01:30+00:00'
updated_at: '2021-12-19T15:28:49+00:00'
type: issue
status: closed
closed_at: '2021-12-19T15:28:49+00:00'
---

# Original Description
When a "gr" or "ghostrider" profile is defined or when the option --threads=X is passed xmrig 6.16.0 fails to start the threads:

*** No Theads (OK):
$sudo ./xmrig -a gr -o raptoreumemporium.com:3008 -u XXXXXXXXXXXXXXXXXXXXXXXX.Test
 * ABOUT        XMRig/6.16.0 gcc/5.4.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i5-4440 CPU @ 3.10GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/4T NUMA:1
 * MEMORY       3.8/15.5 GB (24%)
                DIMM_A0: 4 GB DDR3 @ 1600 MHz TEAMGROUP-UD3-1600
                DIMM_A1: 4 GB DDR3 @ 1600 MHz Team-Elite-1600   
                DIMM_B0: 4 GB DDR3 @ 1600 MHz TEAMGROUP-UD3-1600
                DIMM_B1: 4 GB DDR3 @ 1600 MHz Team-Elite-1600   
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - B85M-E/BR
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      raptoreumemporium.com:3008 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-11-26 18:53:14.891]  net      use pool raptoreumemporium.com:3008  172.14.53.224
[2021-11-26 18:53:14.891]  net      new job from raptoreumemporium.com:3008 diff 6554 algo ghostrider height 193031
[2021-11-26 18:53:14.891]  msr      register values for "intel" preset have been set successfully (0 ms)
[2021-11-26 18:53:15.972]  cpu      use profile  ghostrider  (3 threads) scratchpad 2048 KB
[2021-11-26 18:53:15.976]  cpu      GhostRider algo 1: cn/lite (1 MB)
[2021-11-26 18:53:15.976]  cpu      GhostRider algo 2: cn/turtle-lite (128 KB)
[2021-11-26 18:53:15.976]  cpu      GhostRider algo 3: cn/turtle (256 KB)
[2021-11-26 18:53:15.984]  cpu      READY threads 3/3 (24) huge pages 100% 24/24 memory 49152 KB (13 ms)

*** with treads (Fail):
$ sudo ./xmrig -a gr -o raptoreumemporium.com:3008 -u XXXXXXXXXXXXXXXXXXXXXXXX.Test -t 4
 * ABOUT        XMRig/6.16.0 gcc/5.4.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i5-4440 CPU @ 3.10GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/4T NUMA:1
 * MEMORY       3.8/15.5 GB (24%)
                DIMM_A0: 4 GB DDR3 @ 1600 MHz TEAMGROUP-UD3-1600
                DIMM_A1: 4 GB DDR3 @ 1600 MHz Team-Elite-1600   
                DIMM_B0: 4 GB DDR3 @ 1600 MHz TEAMGROUP-UD3-1600
                DIMM_B1: 4 GB DDR3 @ 1600 MHz Team-Elite-1600   
 * MOTHERBOARD  ASUSTeK COMPUTER INC. - B85M-E/BR
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      raptoreumemporium.com:3008 algo ghostrider
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-11-26 18:53:28.758]  net      use pool raptoreumemporium.com:3008  172.14.53.224
[2021-11-26 18:53:28.758]  net      new job from raptoreumemporium.com:3008 diff 6554 algo ghostrider height 193031
[2021-11-26 18:53:28.759]  msr      register values for "intel" preset have been set successfully (0 ms)
[2021-11-26 18:53:29.832]  cpu      use profile  *  (4 threads) scratchpad 2048 KB
[2021-11-26 18:53:29.833]  cpu      thread #0 self-test failed
[2021-11-26 18:53:29.833]  cpu      thread #1 self-test failed
[2021-11-26 18:53:29.833]  cpu      thread #2 self-test failed
[2021-11-26 18:53:29.833]  cpu      thread #3 self-test failed
[2021-11-26 18:53:29.833]  cpu      disabled (failed to start threads)


# Discussion History
## dapovoa | 2021-11-26T22:40:10+00:00
Yup, this release is a joke! Not working here too.
Also the MSR is block in system if not run in admin in first time.

## mo35 | 2021-11-26T23:00:05+00:00
ryzen 5900 set on 10 treads , self test failed on all treads. anyways it works without set treads , but as soon as -t is introduced , it fails

## SChernykh | 2021-11-26T23:16:23+00:00
This bug will be fixed in the next version. In the meantime, you can switch to using config.json and change the number of threads there.

## SChernykh | 2021-11-27T11:33:49+00:00
Fixed in #2729 which will be included in the next release.

## Spudz76 | 2021-11-27T13:00:56+00:00
`--threads` is the caveman way of forcing thread counts.  It rarely works right especially with algo-hopping, and GR is an algo built around algo-hopping...

Stop using --threads and edit the number of threads by hand in the config.json instead, after they are properly autoconfigured.

# Action History
- Created by: marcusfpereira | 2021-11-26T22:01:30+00:00
- Closed at: 2021-12-19T15:28:49+00:00
