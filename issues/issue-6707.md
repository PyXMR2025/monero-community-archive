---
title: 'E Error forking: Cannot allocate memory'
source_url: https://github.com/monero-project/monero/issues/6707
author: trasherdk
assignees: []
labels: []
created_at: '2020-07-14T16:40:31+00:00'
updated_at: '2020-07-14T16:40:31+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Got a new error just now. Haven't noticed this one before.
I switched from mining with xmrig, against monero-pool, to mining on monero-cli/monerod (2 of 4 threads).

While using xmrig and monero-pool, I haven't seen this error.
```
2020-07-14 16:01:26.865        W There were 11 blocks in the last 90 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack, or your computer's time is off. Or it could be just sheer bad luck.
2020-07-14 16:01:29.125        I Found block <45934d72f24e4baeb296c9abd4f7b638e935ea6d852cccf80857a72a45325746> at height 622804 for difficulty: 225024
2020-07-14 16:01:29.975        E Error forking: Cannot allocate memory
2020-07-14 16:01:30.090        E   failed to find tx meta
2020-07-14 16:01:30.090        E   failed to find tx meta
2020-07-14 16:01:30.090        E   failed to find tx meta
2020-07-14 16:01:30.090        E   failed to find tx meta
**A little later**
2020-07-14 16:25:39.478        E   failed to find tx meta
2020-07-14 16:25:39.478        E   failed to find tx meta
2020-07-14 16:25:58.465        E Error forking: Cannot allocate memory
2020-07-14 16:25:58.465        E   failed to find tx meta
2020-07-14 16:25:58.465        E   failed to find tx meta
**A little later**
2020-07-14 16:27:13.112        E   failed to find tx meta
2020-07-14 16:28:22.851        I Found block <46d668e39bc17e94184b432a3e817cacec57839bf6da6f23b254afdd7bf6d83b> at height 622816 for difficulty: 223220
2020-07-14 16:28:22.907        E Error forking: Cannot allocate memory
2020-07-14 16:28:22.950        E   failed to find tx meta
```
Slackware64 14.2
I have 8 GB RAM, running a mainnet node, stagenet node, wallet-rpc, 2 x wallet-cli, monero-pool.
There's roughly 1 GB free most of the time.

```
$ free -k
              total        used        free      shared  buff/cache   available
Mem:        8157228     7074800      825308           0      257120      827540
Swap:       1993704      839920     1153784

$ ulimit
unlimited

$ ulimit -l
4096

$ cat /proc/meminfo 
MemTotal:        8157228 kB
MemFree:          823524 kB
MemAvailable:     827256 kB
Buffers:           24380 kB
Cached:           163312 kB
SwapCached:        52248 kB
Active:          6572732 kB
Inactive:         523172 kB
Active(anon):    6475652 kB
Inactive(anon):   432592 kB
Active(file):      97080 kB
Inactive(file):    90580 kB
Unevictable:        3180 kB
Mlocked:            3180 kB
SwapTotal:       1993704 kB
SwapFree:        1153784 kB
Dirty:                20 kB
Writeback:             0 kB
AnonPages:       6860160 kB
Mapped:            87016 kB
Shmem:                 0 kB
Slab:              92812 kB
SReclaimable:      70956 kB
SUnreclaim:        21856 kB
KernelStack:        3920 kB
PageTables:        69216 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:     6064124 kB
Committed_AS:    8186096 kB
VmallocTotal:   34359738367 kB
VmallocUsed:           0 kB
VmallocChunk:          0 kB
AnonHugePages:   5492736 kB
HugePages_Total:       8
HugePages_Free:        2
HugePages_Rsvd:        1
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:       13740 kB
DirectMap2M:     8374272 kB
```

And the receiving wallet is not looking healthy either.

All good:
```
[wallet 58yYoy]: status                       
Refreshed 622821/622821, synced, daemon RPC v3.1, SSL

[wallet 58yYoy]: refresh        
Starting refresh...
Refresh done, blocks received: 0                                
Balance: 35453.452342163543, unlocked balance: 35431.755687875717 (9 block(s) to unlock)
```
Next few refresh, not so good:
```
Balance: 35551.308221399990, unlocked balance: 35442.604025365411 (59 block(s) to unlock)
Balance: 35595.140739421430, unlocked balance: 35442.604025365411 (59 block(s) to unlock)
Balance: 35671.957402267495, unlocked balance: 35561.934764937268 (59 block(s) to unlock)
Balance: 35726.417373906426, unlocked balance: 35561.934764937268 (59 block(s) to unlock)
Balance: 35737.485248175131, unlocked balance: 35594.479082498146 (59 block(s) to unlock)
```


# Discussion History
# Action History
- Created by: trasherdk | 2020-07-14T16:40:31+00:00
