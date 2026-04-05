---
title: Possible bug with Conceal pools?
source_url: https://github.com/xmrig/xmrig/issues/2669
author: agentpatience
assignees: []
labels: []
created_at: '2021-11-03T02:09:48+00:00'
updated_at: '2021-11-04T00:26:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the [bug**]([url](url))

I get rejected shares when trying to mine conceal on fastpool or soapyfresh pools and using -a cn/ccx ??


# Discussion History
## agentpatience | 2021-11-03T02:23:16+00:00
vertex4~/xmrig/build (master) $ sudo ./conceal.sh
 * ABOUT        XMRig/6.15.3 gcc/11.2.1
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz (2) 64-bit AES
                L2:7.0 MB L3:70.0 MB 28C/28T NUMA:4
 * MEMORY       0.9/15.5 GB (6%)
                A1: 4 GB DDR4 @ 2400 MHz 9ASF51272PZ-2G6E1
                A3: 4 GB DDR4 @ 2400 MHz 9ASF51272PZ-2G6E1
                B1: 4 GB DDR4 @ 2400 MHz 9ASF51272PZ-2G6E1
                B3: 4 GB DDR4 @ 2400 MHz 9ASF51272PZ-2G6E1
 * MOTHERBOARD  Dell Inc. - Dell Inc.
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      us.fastpool.xyz:10166 algo cn/ccx
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-11-03 02:22:18.423]  net      use pool us.fastpool.xyz:10166  207.244.240.82
[2021-11-03 02:22:18.423]  net      new job from us.fastpool.xyz:10166 diff 5000 algo cn/ccx height 0 (1 tx)
[2021-11-03 02:22:18.423]  cpu      use profile  cn  (28 threads) scratchpad 2048 KB
[2021-11-03 02:22:18.891]  cpu      READY threads 28/28 (28) huge pages 100% 28/28 memory 57344 KB (468 ms)
[2021-11-03 02:22:25.145]  cpu      rejected (0/1) diff 5000 "Rejected share: invalid result" (274 ms)
[2021-11-03 02:22:26.514]  cpu      rejected (0/2) diff 5000 "Rejected share: invalid result" (242 ms)
[2021-11-03 02:22:29.358]  cpu      rejected (0/3) diff 5000 "Rejected share: invalid result" (315 ms)
[2021-11-03 02:22:29.479]  cpu      rejected (0/4) diff 5000 "Rejected share: invalid result" (268 ms)
[2021-11-03 02:22:33.612]  cpu      rejected (0/5) diff 5000 "Rejected share: invalid result" (366 ms)
[2021-11-03 02:22:37.233]  cpu      rejected (0/6) diff 5000 "Rejected share: invalid result" (506 ms)
[2021-11-03 02:22:37.422]  cpu      rejected (0/7) diff 5000 "Rejected share: invalid result" (386 ms)
[2021-11-03 02:22:39.762]  cpu      rejected (0/8) diff 5000 "Rejected share: invalid result" (460 ms)
[2021-11-03 02:22:40.766]  cpu      rejected (0/9) diff 5000 "Rejected share: invalid result" (459 ms)
[2021-11-03 02:22:44.431]  cpu      rejected (0/10) diff 5000 "Rejected share: invalid result" (501 ms)
[2021-11-03 02:22:44.847]  cpu      rejected (0/11) diff 5000 "Rejected share: invalid result" (432 ms)
[2021-11-03 02:22:47.321]  cpu      rejected (0/12) diff 5000 "Rejected share: invalid result" (430 ms)
[2021-11-03 02:22:48.165]  cpu      rejected (0/13) diff 5000 "Rejected share: invalid result" (480 ms)
[2021-11-03 02:22:49.445]  cpu      rejected (0/14) diff 5000 "Rejected share: invalid result" (473 ms)
[2021-11-03 02:22:51.147]  net      new job from us.fastpool.xyz:10166 diff 5000 algo cn/ccx height 0 (1 tx)
[2021-11-03 02:22:51.741]  cpu      rejected (0/15) diff 5000 "Rejected share: invalid result" (597 ms)
[2021-11-03 02:22:51.897]  cpu      rejected (0/16) diff 5000 "Rejected share: invalid result" (513 ms)
[2021-11-03 02:22:53.668]  cpu      rejected (0/17) diff 5000 "Rejected share: invalid result" (644 ms)
[2021-11-03 02:22:53.981]  cpu      rejected (0/18) diff 5000 "Rejected share: invalid result" (625 ms)
[2021-11-03 02:22:57.243]  cpu      rejected (0/19) diff 5000 "Rejected share: invalid result" (595 ms)
[2021-11-03 02:22:57.390]  cpu      rejected (0/20) diff 5000 "Rejected share: invalid result" (610 ms)
[2021-11-03 02:23:01.633]  cpu      rejected (0/21) diff 5000 "Rejected share: invalid result" (616 ms)
[2021-11-03 02:23:02.409]  cpu      rejected (0/22) diff 5000 "Rejected share: invalid result" (628 ms)


## Kevzmasterz | 2021-11-03T02:27:55+00:00
Please chose nvidia

On Wed, Nov 3, 2021, 10:23 AM Jeffrey ***@***.***> wrote:

> vertex4~/xmrig/build (master) $ sudo ./conceal.sh
>
>    - ABOUT XMRig/6.15.3 gcc/11.2.1
>    - LIBS libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.1.0
>    - HUGE PAGES supported
>    - 1GB PAGES disabled
>    - CPU Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz (2) 64-bit AES
>    L2:7.0 MB L3:70.0 MB 28C/28T NUMA:4
>    - MEMORY 0.9/15.5 GB (6%)
>    A1: 4 GB DDR4 @ 2400 MHz 9ASF51272PZ-2G6E1
>    A3: 4 GB DDR4 @ 2400 MHz 9ASF51272PZ-2G6E1
>    B1: 4 GB DDR4 @ 2400 MHz 9ASF51272PZ-2G6E1
>    B3: 4 GB DDR4 @ 2400 MHz 9ASF51272PZ-2G6E1
>    - MOTHERBOARD Dell Inc. - Dell Inc.
>    - DONATE 1%
>    - ASSEMBLY auto:intel
>    - POOL #1 <https://github.com/xmrig/xmrig/issues/1>
>    us.fastpool.xyz:10166 algo cn/ccx
>    - COMMANDS hashrate, pause, resume, results, connection
>    - OPENCL disabled
>    - CUDA disabled
>    [2021-11-03 02:22:18.423] net use pool us.fastpool.xyz:10166
>    207.244.240.82
>    [2021-11-03 02:22:18.423] net new job from us.fastpool.xyz:10166 diff
>    5000 algo cn/ccx height 0 (1 tx)
>    [2021-11-03 02:22:18.423] cpu use profile cn (28 threads) scratchpad
>    2048 KB
>    [2021-11-03 02:22:18.891] cpu READY threads 28/28 (28) huge pages 100%
>    28/28 memory 57344 KB (468 ms)
>    [2021-11-03 02:22:25.145] cpu rejected (0/1) diff 5000 "Rejected
>    share: invalid result" (274 ms)
>    [2021-11-03 02:22:26.514] cpu rejected (0/2) diff 5000 "Rejected
>    share: invalid result" (242 ms)
>    [2021-11-03 02:22:29.358] cpu rejected (0/3) diff 5000 "Rejected
>    share: invalid result" (315 ms)
>    [2021-11-03 02:22:29.479] cpu rejected (0/4) diff 5000 "Rejected
>    share: invalid result" (268 ms)
>    [2021-11-03 02:22:33.612] cpu rejected (0/5) diff 5000 "Rejected
>    share: invalid result" (366 ms)
>    [2021-11-03 02:22:37.233] cpu rejected (0/6) diff 5000 "Rejected
>    share: invalid result" (506 ms)
>    [2021-11-03 02:22:37.422] cpu rejected (0/7) diff 5000 "Rejected
>    share: invalid result" (386 ms)
>    [2021-11-03 02:22:39.762] cpu rejected (0/8) diff 5000 "Rejected
>    share: invalid result" (460 ms)
>    [2021-11-03 02:22:40.766] cpu rejected (0/9) diff 5000 "Rejected
>    share: invalid result" (459 ms)
>    [2021-11-03 02:22:44.431] cpu rejected (0/10) diff 5000 "Rejected
>    share: invalid result" (501 ms)
>    [2021-11-03 02:22:44.847] cpu rejected (0/11) diff 5000 "Rejected
>    share: invalid result" (432 ms)
>    [2021-11-03 02:22:47.321] cpu rejected (0/12) diff 5000 "Rejected
>    share: invalid result" (430 ms)
>    [2021-11-03 02:22:48.165] cpu rejected (0/13) diff 5000 "Rejected
>    share: invalid result" (480 ms)
>    [2021-11-03 02:22:49.445] cpu rejected (0/14) diff 5000 "Rejected
>    share: invalid result" (473 ms)
>    [2021-11-03 02:22:51.147] net new job from us.fastpool.xyz:10166 diff
>    5000 algo cn/ccx height 0 (1 tx)
>    [2021-11-03 02:22:51.741] cpu rejected (0/15) diff 5000 "Rejected
>    share: invalid result" (597 ms)
>    [2021-11-03 02:22:51.897] cpu rejected (0/16) diff 5000 "Rejected
>    share: invalid result" (513 ms)
>    [2021-11-03 02:22:53.668] cpu rejected (0/17) diff 5000 "Rejected
>    share: invalid result" (644 ms)
>    [2021-11-03 02:22:53.981] cpu rejected (0/18) diff 5000 "Rejected
>    share: invalid result" (625 ms)
>    [2021-11-03 02:22:57.243] cpu rejected (0/19) diff 5000 "Rejected
>    share: invalid result" (595 ms)
>    [2021-11-03 02:22:57.390] cpu rejected (0/20) diff 5000 "Rejected
>    share: invalid result" (610 ms)
>    [2021-11-03 02:23:01.633] cpu rejected (0/21) diff 5000 "Rejected
>    share: invalid result" (616 ms)
>    [2021-11-03 02:23:02.409] cpu rejected (0/22) diff 5000 "Rejected
>    share: invalid result" (628 ms)
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2669#issuecomment-958603984>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AVNETRWWNBPK5KEIUQETG63UKCTMPANCNFSM5HH2YQQA>
> .
>


## Kevzmasterz | 2021-11-03T02:45:20+00:00
I activated my outlook now, can do it again?

On Wed, Nov 3, 2021, 10:27 AM john kevin quilaton <
***@***.***> wrote:

> Please chose nvidia
>
> On Wed, Nov 3, 2021, 10:23 AM Jeffrey ***@***.***> wrote:
>
>> vertex4~/xmrig/build (master) $ sudo ./conceal.sh
>>
>>    - ABOUT XMRig/6.15.3 gcc/11.2.1
>>    - LIBS libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.1.0
>>    - HUGE PAGES supported
>>    - 1GB PAGES disabled
>>    - CPU Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz (2) 64-bit AES
>>    L2:7.0 MB L3:70.0 MB 28C/28T NUMA:4
>>    - MEMORY 0.9/15.5 GB (6%)
>>    A1: 4 GB DDR4 @ 2400 MHz 9ASF51272PZ-2G6E1
>>    A3: 4 GB DDR4 @ 2400 MHz 9ASF51272PZ-2G6E1
>>    B1: 4 GB DDR4 @ 2400 MHz 9ASF51272PZ-2G6E1
>>    B3: 4 GB DDR4 @ 2400 MHz 9ASF51272PZ-2G6E1
>>    - MOTHERBOARD Dell Inc. - Dell Inc.
>>    - DONATE 1%
>>    - ASSEMBLY auto:intel
>>    - POOL #1 <https://github.com/xmrig/xmrig/issues/1>
>>    us.fastpool.xyz:10166 algo cn/ccx
>>    - COMMANDS hashrate, pause, resume, results, connection
>>    - OPENCL disabled
>>    - CUDA disabled
>>    [2021-11-03 02:22:18.423] net use pool us.fastpool.xyz:10166
>>    207.244.240.82
>>    [2021-11-03 02:22:18.423] net new job from us.fastpool.xyz:10166 diff
>>    5000 algo cn/ccx height 0 (1 tx)
>>    [2021-11-03 02:22:18.423] cpu use profile cn (28 threads) scratchpad
>>    2048 KB
>>    [2021-11-03 02:22:18.891] cpu READY threads 28/28 (28) huge pages
>>    100% 28/28 memory 57344 KB (468 ms)
>>    [2021-11-03 02:22:25.145] cpu rejected (0/1) diff 5000 "Rejected
>>    share: invalid result" (274 ms)
>>    [2021-11-03 02:22:26.514] cpu rejected (0/2) diff 5000 "Rejected
>>    share: invalid result" (242 ms)
>>    [2021-11-03 02:22:29.358] cpu rejected (0/3) diff 5000 "Rejected
>>    share: invalid result" (315 ms)
>>    [2021-11-03 02:22:29.479] cpu rejected (0/4) diff 5000 "Rejected
>>    share: invalid result" (268 ms)
>>    [2021-11-03 02:22:33.612] cpu rejected (0/5) diff 5000 "Rejected
>>    share: invalid result" (366 ms)
>>    [2021-11-03 02:22:37.233] cpu rejected (0/6) diff 5000 "Rejected
>>    share: invalid result" (506 ms)
>>    [2021-11-03 02:22:37.422] cpu rejected (0/7) diff 5000 "Rejected
>>    share: invalid result" (386 ms)
>>    [2021-11-03 02:22:39.762] cpu rejected (0/8) diff 5000 "Rejected
>>    share: invalid result" (460 ms)
>>    [2021-11-03 02:22:40.766] cpu rejected (0/9) diff 5000 "Rejected
>>    share: invalid result" (459 ms)
>>    [2021-11-03 02:22:44.431] cpu rejected (0/10) diff 5000 "Rejected
>>    share: invalid result" (501 ms)
>>    [2021-11-03 02:22:44.847] cpu rejected (0/11) diff 5000 "Rejected
>>    share: invalid result" (432 ms)
>>    [2021-11-03 02:22:47.321] cpu rejected (0/12) diff 5000 "Rejected
>>    share: invalid result" (430 ms)
>>    [2021-11-03 02:22:48.165] cpu rejected (0/13) diff 5000 "Rejected
>>    share: invalid result" (480 ms)
>>    [2021-11-03 02:22:49.445] cpu rejected (0/14) diff 5000 "Rejected
>>    share: invalid result" (473 ms)
>>    [2021-11-03 02:22:51.147] net new job from us.fastpool.xyz:10166 diff
>>    5000 algo cn/ccx height 0 (1 tx)
>>    [2021-11-03 02:22:51.741] cpu rejected (0/15) diff 5000 "Rejected
>>    share: invalid result" (597 ms)
>>    [2021-11-03 02:22:51.897] cpu rejected (0/16) diff 5000 "Rejected
>>    share: invalid result" (513 ms)
>>    [2021-11-03 02:22:53.668] cpu rejected (0/17) diff 5000 "Rejected
>>    share: invalid result" (644 ms)
>>    [2021-11-03 02:22:53.981] cpu rejected (0/18) diff 5000 "Rejected
>>    share: invalid result" (625 ms)
>>    [2021-11-03 02:22:57.243] cpu rejected (0/19) diff 5000 "Rejected
>>    share: invalid result" (595 ms)
>>    [2021-11-03 02:22:57.390] cpu rejected (0/20) diff 5000 "Rejected
>>    share: invalid result" (610 ms)
>>    [2021-11-03 02:23:01.633] cpu rejected (0/21) diff 5000 "Rejected
>>    share: invalid result" (616 ms)
>>    [2021-11-03 02:23:02.409] cpu rejected (0/22) diff 5000 "Rejected
>>    share: invalid result" (628 ms)
>>
>> —
>> You are receiving this because you are subscribed to this thread.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/xmrig/xmrig/issues/2669#issuecomment-958603984>, or
>> unsubscribe
>> <https://github.com/notifications/unsubscribe-auth/AVNETRWWNBPK5KEIUQETG63UKCTMPANCNFSM5HH2YQQA>
>> .
>>
>


## Spudz76 | 2021-11-03T02:54:40+00:00
`[2021-11-03 02:22:18.423] net new job from us.fastpool.xyz:10166 diff 5000 algo cn/ccx height 0 (1 tx)`

Well, height zero is definitely wrong.  We'd need to see a packet debug dump of what the pool(s) are sending as a job, it's clearly corrupt or using some new encoding.


## SChernykh | 2021-11-03T09:00:03+00:00
Conceal switched to Cryptonight-GPU, it's not a cn/ccx anymore

## agentpatience | 2021-11-03T09:46:52+00:00
> 
> 
> Conceal switched to Cryptonight-GPU, it's not a cn/ccx anymore

I tried passing -a cn/gpu but algo stays set to auto?

## agentpatience | 2021-11-03T10:01:12+00:00
./xmrig -o us.fastpool.xyz:10166 -u solo:ccx7FJcdhqqHZg1grJSezcFgXnTfiYnmnDYw9NYc8n4fe8NPKwbhxroXtznxBsofFP8JB32YYBmtwLdoEirjAbYo4DBZeX2tJb -p drillBIT -k -a cn/gpu
 * ABOUT        XMRig/6.15.3 gcc/11.2.1
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.1.0
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz (2) 64-bit AES
                L2:7.0 MB L3:70.0 MB 28C/28T NUMA:4
 * MEMORY       0.9/15.5 GB (6%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      us.fastpool.xyz:10166 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-11-03 09:53:48.666]  net      us.fastpool.xyz:10166 unknown algorithm, make sure you set "algo" or "coin" option
[2021-11-03 09:53:48.666]  net      us.fastpool.xyz:10166 login error code: 6
[2021-11-03 09:53:54.007]  net      us.fastpool.xyz:10166 unknown algorithm, make sure you set "algo" or "coin" option
[2021-11-03 09:53:54.007]  net      us.fastpool.xyz:10166 login error code: 6
[2021-11-03 09:53:59.968]  net      us.fastpool.xyz:10166 unknown algorithm, make sure you set "algo" or "coin" option
[2021-11-03 09:53:59.968]  net      us.fastpool.xyz:10166 login error code: 6
[2021-11-03 09:54:05.976]  net      us.fastpool.xyz:10166 unknown algorithm, make sure you set "algo" or "coin" option
[2021-11-03 09:54:05.976]  net      us.fastpool.xyz:10166 login error code: 6
[2021-11-03 09:54:11.981]  net      us.fastpool.xyz:10166 unknown algorithm, make sure you set "algo" or "coin" option
[2021-11-03 09:54:11.981]  net      us.fastpool.xyz:10166 login error code: 6

## Spudz76 | 2021-11-03T11:20:41+00:00
CN-GPU is not in mainline.  You must use MoneroOcean fork, or my [master-restoreCNGPU](https://github.com/Spudz76/xmrig/tree/master-restoreCNGPU) or [dev-restoreCNGPU](https://github.com/Spudz76/xmrig/tree/dev-restoreCNGPU) which are simply mainstream current master/dev with CN-GPU put back in (no other MoneroOcean mods).

## agentpatience | 2021-11-03T11:41:18+00:00
Ok, you mean I use this version? https://github.com/MoneroOcean/xmrig

## Spudz76 | 2021-11-04T00:26:45+00:00
Yes if you require pre-compiled.

# Action History
- Created by: agentpatience | 2021-11-03T02:09:48+00:00
