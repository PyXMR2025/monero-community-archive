---
title: v2.99.0-beta Release Notes
source_url: https://github.com/xmrig/xmrig/issues/1066
author: xmrig
assignees:
- xmrig
labels:
- META
created_at: '2019-07-21T17:31:55+00:00'
updated_at: '2019-08-10T12:32:22+00:00'
type: issue
status: closed
closed_at: '2019-08-10T12:32:21+00:00'
---

# Original Description
v2.99.0 is first step to 3.0 release (scheduled to be done before next Monero fork in October).

### What's new:

* Fully integrated RandomX support (`rx/wow` and `rx/loki` now), thanks @SChernykh for initial integration.
* [Flexible](https://github.com/xmrig/xmrig/blob/evo/doc/CPU.md) multi algorithm configuration.
* Unlimited switching between incompatible algorithms, all mining options can be changed in runtime.
* Included all new features and fixes from from 2.15-2.16.

### Notes
* Config files from previous versions NOT compatible, `variant` option replaced to `algo`, global option `algo` removed, all CPU related settings moved to `cpu` object.
* Command line options also not compatible, `--variant` option replaced to `--algo`.
* Options `av`, `safe` and `max-cpu-usage` removed.
* Algorithm `cn/msr` renamed to `cn/fast`.
* Algorithm `cn/xtl` removed.
* API endpoint `GET /1/threads` replaced to `GET /2/backends`.

### Bonus

* http://workers.xmrig.info/

### Download

* https://github.com/xmrig/xmrig/releases/tag/v2.99.0-beta
* https://github.com/xmrig/xmrig-proxy/releases/tag/v2.16.1-beta

# Discussion History
## paolosezart | 2019-07-25T07:08:09+00:00
Good day. Why is the max-cpu-usage option deleted? It was a very convenient feature, so as not to heavily load the CPU. Return it please.

## xmrig | 2019-07-25T08:06:17+00:00
This option has too many myth and legends, most of users don't understand how this option works, CPU load can be changed by reducing threads count in config or command line.
Thank you.

## paolosezart | 2019-07-25T09:02:35+00:00
It is not always convenient to reconfigure BAT or json, since there are different numbers of cores on different computers. Therefore, the option --cpu-affinity is not very convenient. I usually put 25 or 50 percent, I have ready-made settings. Therefore, I think it is better to return the parameter "max-cpu-usage". Thank you in advance.
Today I wanted to upgrade from xmrig v2.14.1, and here such an unpleasant situation

## pboguk | 2019-07-25T18:27:57+00:00
I fully agreed with @paolosezart regaring max-cpu-usage. I have about 100 cpu miners with different number of cores/threads and deliver the same config automatically. In a case of absence max-cpu-usage I should make config for each miner.
So, if possible - please return option.

## lexansoft | 2019-08-05T04:24:04+00:00
Segmentation fault****

* ABOUT        XMRig/2.99.3-beta gcc/7.4.0
 * LIBS         libuv/1.18.0 OpenSSL/1.1.1 hwloc/1.11.9
 * CPU          AMD Ryzen Threadripper 2950X 16-Core Processor (1) x64 AES AVX2
                L2:8.0 MB L3:32.0 MB 16C/32T NUMA:2
 * DONATE       1%
 * ASSEMBLY     auto:ryzen
 * POOL #1      ca.minexmr.com:4444 algo rx/0
 * COMMANDS     hashrate, pause, resume
[2019-08-04 21:22:01.977] use pool ca.minexmr.com:4444  158.69.25.77
[2019-08-04 21:22:01.977] new job from ca.minexmr.com:4444 diff 15000 algo rx/0 height 1893892
[2019-08-04 21:22:01.977] CPU use profile  *  (32 threads) scratchpad 2048 KB
[2019-08-04 21:22:01.990] CPU READY threads 32(32) huge pages 32/32 100% memory 65536 KB (13 ms)
[2019-08-04 21:22:01.990]  rx  #1 allocate 2336 MB (2080+256) for RandomX dataset & cache
[2019-08-04 21:22:02.376]  rx  #1 allocate done huge pages 1168/1168 100% +JIT (399 ms)
[2019-08-04 21:22:02.376]  rx  #1 init dataset algo rx/0 (32 threads) seed 0000000000000000...
./start_miner-b.bash: line 4:  3970 Segmentation fault      (core dumped) ~/xmrig-b/build/xmrig -o ca.minexmr.com:4444 -t 32 -u ??? .thr0 --donate-level=1 --algo randomx

## SChernykh | 2019-08-05T05:17:25+00:00
@lexansoft You're a bit too early to try mining Monero with RandomX.

## xmrig | 2019-08-05T05:30:03+00:00
@lexansoft Yep it a bit early, but I confirm segmentation fault, it should never happen.
Thank you.

## xmrig | 2019-08-05T11:11:03+00:00
@lexansoft Fixed https://github.com/xmrig/xmrig/commit/3543abcc3cb99155b3620b53daa304daae373b2a

You should avoid use `-t` option without affinity, for complex CPUs with NUMA, better is use config file and allow miner create proper configuration, without affinity miner can't use benefit of creation RandomX datasets on each NUMA node.
Thank you.

## lexansoft | 2019-08-05T16:38:55+00:00
Yes, with config.json it does not crash.  Thank you.

But, the performance is only 3300H/s. It is too slow for such a monster
CPU.  What should I try to do?

Thank you.



Alexandre Naverniouk


On Mon, Aug 5, 2019 at 4:11 AM xmrig <notifications@github.com> wrote:

> @lexansoft <https://github.com/lexansoft> Fixed 3543abc
> <https://github.com/xmrig/xmrig/commit/3543abcc3cb99155b3620b53daa304daae373b2a>
>
> You should avoid use -t option without affinity, for complex CPUs with
> NUMA, better is use config file and allow miner create proper
> configuration, without affinity miner can't use benefit of creation RandomX
> datasets on each NUMA node.
> Thank you.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1066?email_source=notifications&email_token=AAQHPJCLGYTPHVCSMTKSMWTQDADEVA5CNFSM4IFTAWZKYY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOD3RPVXI#issuecomment-518191837>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AAQHPJFTAEIMHO3LEZSXBETQDADEVANCNFSM4IFTAWZA>
> .
>


## lexansoft | 2019-08-05T16:52:37+00:00
I ran ./xmrig --export-topology in case you need it. Please see the
attachment.

Alexandre Naverniouk


On Mon, Aug 5, 2019 at 9:38 AM Alexandre Naverniouk <lexansoft@gmail.com>
wrote:

> Yes, with config.json it does not crash.  Thank you.
>
> But, the performance is only 3300H/s. It is too slow for such a monster
> CPU.  What should I try to do?
>
> Thank you.
>
>
>
> Alexandre Naverniouk
>
>
> On Mon, Aug 5, 2019 at 4:11 AM xmrig <notifications@github.com> wrote:
>
>> @lexansoft <https://github.com/lexansoft> Fixed 3543abc
>> <https://github.com/xmrig/xmrig/commit/3543abcc3cb99155b3620b53daa304daae373b2a>
>>
>> You should avoid use -t option without affinity, for complex CPUs with
>> NUMA, better is use config file and allow miner create proper
>> configuration, without affinity miner can't use benefit of creation RandomX
>> datasets on each NUMA node.
>> Thank you.
>>
>> —
>> You are receiving this because you were mentioned.
>> Reply to this email directly, view it on GitHub
>> <https://github.com/xmrig/xmrig/issues/1066?email_source=notifications&email_token=AAQHPJCLGYTPHVCSMTKSMWTQDADEVA5CNFSM4IFTAWZKYY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOD3RPVXI#issuecomment-518191837>,
>> or mute the thread
>> <https://github.com/notifications/unsubscribe-auth/AAQHPJFTAEIMHO3LEZSXBETQDADEVANCNFSM4IFTAWZA>
>> .
>>
>


## xmrig | 2019-08-05T16:58:16+00:00
@lexansoft please open new separate issue with details:
1. Config file without wallet
2. Miner output from begin.
3. topology.xml, seems github not attach file from email.

## lexansoft | 2019-08-05T17:40:31+00:00
https://github.com/xmrig/xmrig/issues/1101

Alexandre Naverniouk


On Mon, Aug 5, 2019 at 9:58 AM xmrig <notifications@github.com> wrote:

> @lexansoft <https://github.com/lexansoft> please open new separate issue
> with details:
>
>    1. Config file without wallet
>    2. Miner output from begin.
>    3. topology.xml, seems github not attach file from email.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1066?email_source=notifications&email_token=AAQHPJGBFB3D3BZMCR6B5DLQDBL2VA5CNFSM4IFTAWZKYY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOD3SNVVY#issuecomment-518314711>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AAQHPJAVTWQKPVZ3VQXHCJTQDBL2VANCNFSM4IFTAWZA>
> .
>


## xmrig | 2019-08-10T12:32:21+00:00
#1111 

# Action History
- Created by: xmrig | 2019-07-21T17:31:55+00:00
- Closed at: 2019-08-10T12:32:21+00:00
