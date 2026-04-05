---
title: Classic numactl settings works faster than 2.9.4 built in numa support
source_url: https://github.com/xmrig/xmrig/issues/1103
author: vegaman64
assignees: []
labels:
- bug
- NUMA
created_at: '2019-08-06T19:12:48+00:00'
updated_at: '2019-08-09T09:45:51+00:00'
type: issue
status: closed
closed_at: '2019-08-09T09:45:50+00:00'
---

# Original Description
#!/bin/bash
/sbin/sysctl -w vm.nr_hugepages=2500
STRATUM_SERVER="loki.miner.rocks"
STRATUM_PORT="5005"
RIG_ID=""
POOL_WORKER="L8GxxxxxxxxxxxxxxxxxxxxxYe8W"
POOL_PASS="w=RigServer46"
THREADS="8"
XMPATH="/home/miner/xmrig"
CMD_OPTS="--rig-id ${RIG_ID} --asm intel --donate-level 2 -k -t ${THREADS}"
echo 'Starting xmrig CPU in a detached screen, use "screen -r" to resume...'

killall -TERM xmrig >/dev/null 2>&1
sleep 1
seq 0 1 | xargs -P 0 -I node numactl -N node /usr/bin/screen -d -m ${XMPATH}/xmrig -a rx/loki -o stratum+tcp://${STRATUM_SERVER}:${STRATUM_PORT} -u ${POOL_WORKER} -p ${POOL_PASS} ${CMD_OPTS}
exit 0

Gives 2x2540hs = 5080hs

#!/bin/bash
/sbin/sysctl -w vm.nr_hugepages=2500
STRATUM_SERVER="loki.miner.rocks"
STRATUM_PORT="5005"
RIG_ID=""
POOL_WORKER="L8GxxxxxxxxxxxxxxxxxxxxxYe8W"
POOL_PASS="w=RigServer46"
THREADS="16"
XMPATH="/home/miner/xmrig"
CMD_OPTS="--rig-id ${RIG_ID} --asm intel --randomx-init --donate-level 2 -k -t ${THREADS}"
echo 'Starting xmrig CPU in a detached screen, use "screen -r" to resume...'

killall -TERM xmrig >/dev/null 2>&1
sleep 1
/usr/bin/screen -d -m ${XMPATH}/xmrig -a rx/loki -o stratum+tcp://${STRATUM_SERVER}:${STRATUM_PORT} -u ${POOL_WORKER} -p ${POOL_PASS} ${CMD_OPTS}
exit 0

Gives 4940hs

2x Xeon e5 2650 v1

Am I doing something wrong?

# Discussion History
## xmrig | 2019-08-07T04:07:44+00:00
You CPU has 20 MB L3 cache, so 10 threads per CPU should be better option or you found 8 threads is give more hashrate?

NUMA support in miner not work properly if threads not use CPU affinity, because miner don't know what NUMA node should use for this thread, single `-t` option create threads without affinity.

You have 3 options:
- Remove `-t` option, miner will use 20 threads with proper affinity.
- Use config file, then remove 4 threads, `lscpu` helps understand what numbers should be removed.
- If you still prefer command line, use `--cpu-affinity` option, it most complicated way.

## vegaman64 | 2019-08-07T07:17:57+00:00
Thanks a lot! Shown config is just a part of the context - we really need cli only to keep it universal. 
On my previous (RX Benchmark and XMRig) tests 16 threads (or 8 threads per numa) gave optimal results (I believed it's L2 limitation) however with -t removed I'm now getting 5100Hs which is already better than before. Jet to try with hyper threading enabled. 
Can you please point me to a "read thing" about --cpu-affinity? ..it's interesting as there is still a room for playing.
Thanks for XMRig, guys! 

## xmrig | 2019-08-07T09:06:11+00:00
In case if HT disabled miner use only 16 threads, bеcause cores ended before L3 cache.
CPU affinity it just mapping between miner threads and CPUs cores/threads, you can saw it in config or if press `h`. also this used to find NUMA node for thread.

If affinity no set it fine for simple cases, one CPU with unified L3 cache, or external binding (numactl).

In recent version 2 major things reproduced:
1. New multi algorithm config format https://github.com/xmrig/xmrig/blob/evo/doc/CPU.md (2.99.0+)
2. NUMA support #1077 (2.99.2+)

`--cpu-affinity` is just one number representation for CPU affinity, it not human friendly, hard to explain and because `-t` option can't define multiple profiles, I don't recommend use it. Example https://i.imgur.com/4Udaagg.png for simple case 16 threads `--cpu-affinity=0xFFFF`

## vegaman64 | 2019-08-07T09:26:41+00:00
Thanks again! It means I can live without diving any deeper this time  as HT settings gives me both options - 16 threads with correct affinity and 20 threads with correct affinity. 

## vegaman64 | 2019-08-07T11:50:43+00:00
Why aren’t you looking at l2 cache when auto setting threads count?  At least in my tests I found  it is as important to have 256kb of l2 as 2MB L3 per thread on RandomX .

## xmrig | 2019-08-07T12:08:05+00:00
Can you give examples of CPUs with less than 256 kB of L2 cache per core, and better configuration for them?
Thank you.

## vegaman64 | 2019-08-07T13:40:32+00:00
E5 v1 Xeons for example. Most of 8 core ones has 20Mb L3 and 8x256kb L2. If HT enabled auto config sets 10 threads as technically 20Mb L3 allows it, but L2 is enough only for 8 threads so running 10 gives much less in overall. On CN L2 doesn’t  matter that much so we were able to count on L3 only I guess. Now I know we can use HT settings to switch between RandomX and CN to use auto threads config, but from my understanding it could be done automatically by looking at l2 if it’s set to RandomX.

## xmrig | 2019-08-07T13:51:38+00:00
Sounds right, I need time to check it.
Thank you.

## vegaman64 | 2019-08-07T13:51:58+00:00
I think it relates to almost any Xeon

## xmrig | 2019-08-08T14:03:58+00:00
Done.

## xmrig | 2019-08-09T09:45:50+00:00
v2.99.5-beta released https://github.com/xmrig/xmrig/releases/tag/v2.99.5-beta

# Action History
- Created by: vegaman64 | 2019-08-06T19:12:48+00:00
- Closed at: 2019-08-09T09:45:50+00:00
