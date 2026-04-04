---
title: 0.16.0.0 monerod possible fd leak or resource exhaustion?
source_url: https://github.com/monero-project/monero/issues/6623
author: ghost
assignees: []
labels: []
created_at: '2020-06-02T21:07:19+00:00'
updated_at: '2020-06-10T14:34:44+00:00'
type: issue
status: closed
closed_at: '2020-06-10T14:34:44+00:00'
---

# Original Description
no special config - start cli monerod to sync up, progress is made but eventually stops with the

"There were 0 blocks in the last 90 minutes....."

stopping monerod and restarting it is a workaround.

i guess that there may be a file descriptor leak or some other resource exhaustion.  Next time it happens I will take a look at lsof and check some other things.

Monitoring your monerod state if you are running 0.16.0.0 is a good idea.

I wonder if there is a system resource we should increase that may not have been mentioned.




# Discussion History
## moneromooo-monero | 2020-06-02T22:49:57+00:00
Can you include the evidence you found for this being due to fd/resource exhaustion ?

## trasherdk | 2020-06-03T03:32:39+00:00
Looks to me like, just another day on the Monero network.

Build from master about 2 days ago, claiming to be `v015.0.0`
```
2020-06-02 10:33:53.560 W There were 22 blocks in the last 90 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack, or your computer's time is off. Or it could be just sheer bad luck.
2020-06-02 10:35:23.638 W There were 22 blocks in the last 90 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack, or your computer's time is off. Or it could be just sheer bad luck.
2020-06-02 11:52:42.986 I Synced 2111788/2111788
2020-06-02 11:52:42.987 I SYNCHRONIZED OK
2020-06-02 12:36:53.729 I Synced 2111821/2111821
2020-06-02 12:36:53.729 I SYNCHRONIZED OK
2020-06-02 12:36:56.119 I SYNCHRONIZED OK
2020-06-02 12:37:01.800 I SYNCHRONIZED OK
2020-06-02 17:19:27.399 I Version 0.15.0.1 of monero for source is available: https://downloads.getmonero.org/source/monero-source-v0.15.0.1.tar.bz2, SHA256 hash 083a3862f554a2e5157686d7a8075557dfd6f07de08069cac91017c17739750b
2020-06-02 20:56:09.024 W There were 0 blocks in the last 20 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack, or your computer's time is off. Or it could be just sheer bad luck.
2020-06-02 20:57:39.064 W There were 0 blocks in the last 20 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack, or your computer's time is off. Or it could be just sheer bad luck.
2020-06-02 20:59:09.313 W There were 0 blocks in the last 20 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack, or your computer's time is off. Or it could be just sheer bad luck.
2020-06-02 23:20:41.441 I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 2112097
2020-06-02 23:20:41.442 I id:     <7e36fa2a68b4dd136d0620ebf067728f02a9ec438190a7f8360b13153cbe0794>
2020-06-02 23:20:41.442 I PoW:    <5f7558b75ed299d4439ad09221978540f2f0622b1f03d1bc6222d50400000000>
2020-06-02 23:20:41.442 I difficulty:     158911723882

version 
0.15.0.0-992b7ce30

status 
Height: 2112220/2112220 (100.0%) on mainnet, not mining, net hash 1.30 GH/s, v12, update needed, 4(out)+4(in) connections, uptime 1d 9h 30m 56s
```

Plenty of resources left:
```
  1  [|                                   0.7%]   Tasks: 74, 264 thr; 1 running
  2  [|                                   0.7%]   Load average: 0.03 0.10 0.15 
  3  [|                                   1.4%]   Uptime: 64 days, 21:58:21
  4  [                                    0.0%]
  Mem[|||||||||||||||||||||||||||||3.46G/7.78G]
  Swp[||||                          155M/1.90G]
```

While running 9 monero screen sessions:
```
monerod-stagenet     (Detached)
monerod-testnet      (Detached)
poolwallet-stagenet  (Detached)
userwallet-testnet   (Detached)
feewallet-stagenet   (Detached)
userwallet-mainnet   (Detached)
userwallet-stagenet  (Detached)
monerod-mainnet      (Detached)
minerwallet-stagenet (Detached)
```


## ghost | 2020-06-10T14:34:28+00:00
its happened a few more times and i have verified with lsof that it is not an fd leak

it appears the monerod gets confused about the chain height and gets stuck on an orphan chain - i've seen that with smaller coins - but have not seen it with monero for - what - 2 to 3 years.

i have been running monerod --out-peers=32 and have not seen the problem since.

closing since i have a workaround


# Action History
- Created by: ghost | 2020-06-02T21:07:19+00:00
- Closed at: 2020-06-10T14:34:44+00:00
