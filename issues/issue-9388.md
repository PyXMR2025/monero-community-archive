---
title: Daemons processing big blocks may bump against serializer sanity checks and
  fail to sync
source_url: https://github.com/monero-project/monero/issues/9388
author: rbrunner7
assignees: []
labels:
- bug
- important
- discussion
created_at: '2024-06-28T15:41:11+00:00'
updated_at: '2024-09-08T08:07:05+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
As discussed in this week's MRL meeting there is an interesting and potentially dangerous problem detected on stressnet: If you leave the default of syncing in chuncks of 20 blocks the Monero daemon can't sync beyond blockchain regions with very big blocks, with "very big" being around 1.5 MB in the case of the stressnet blockchain around height 2521675. You have to use a startup switch of `--block-sync-size 1` to make sure you can sync.

The problem is that sooner or later the daemon, while syncing, bans all peers, which of course is a problem.

With a bit of luck I found the problem: So the daemon requests 20 blocks from peers. This results in over 30 MB of data that in some parts bumps against limits in the serializer that were put in place a few years ago to fight against attacks using "doctored" data that deserializes to hundreds of megabytes and crashes Monero daemons.

The limits in question are here: https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/contrib/epee/include/storages/levin_abstract_invoke2.h#L48

While debugging I saw the daemon wanting to go over the limit of 16384 strings. I found deserialization code hard to debug because of all the templating in the C++ code, but I suspect it could be one particularly large vector of strings that brings things over the limit.

I made a "band aid" style / "not fit for production" PR against the stressnet repository master branch that helps the daemon to sync: https://github.com/spackle-xmr/monero/pull/12

But I think a dev with experience in such things, which is not me, should take a good look at this and decide whether simply rising those limits is a reasonable way to go. We may need a new automatism that watches block sizes and automatically goes lower with "block sync size" instead, for example.

# Discussion History
## Rucknium | 2024-06-28T16:22:11+00:00
Here is my investigation of the `--block-sync-size` thresholds to sync sets of large blocks:

I synced a stressnet node from the genesis block using the latest version 250.18.3.3.2, but I set `--block-sync-size` to 20 to match the mainet default.

The node got stuck at height 2521517 with repeated message like `Sync data returned a new top block candidate: 2521517 -> 2524276 [Your node is 2759 blocks (3.8 days) behind]`. Block sizes at this height were about 1.5MB. Then it banned some peers. The bans expired after 2 minutes because we set a new ban duration in the code.

I decreased `--block-sync-size` by 1, then I let it try to sync for 10 or more minutes. I did this many times to see the maximum value of `--block-sync-size` that the node could use to get over the large block "hill". Eventually, it started syncing at `--block-sync-size 14`. It looks like the node can sync a chunk of blocks about 24MB in size.

The node encountered some alt chains between heights 2521576 and 2521702.

While my node was syncing, there was another syncing node on the network probably with the new `--block-sync-size 1` default. Its height passed my node, but it may have helped lift my node's height as it passed because the blocks chunk it could send my node was less than what my node specified as it passed. (If the other node was only 5 blocks ahead of my node, it could send me a block chunk of just 5 blocks.) By the time my node got to height 2521570, the other node was more than 20 blocks ahead of mine, so it could not lift my node.

The table below shows the block heights and sizes around the time that the node syncing was stuck. `block_weight.10.block.rolling.mean` is the mean of the block weight of the next 10 blocks. For example, height = 2521300 and block_weight.10.block.rolling.mean = 0.72 means that the mean block weight of blocks 2521300 - 2521309 was 0.72 MB.

```txt
     height block_weight.10.block.rolling.mean
 1: 2521300                               0.72
 2: 2521310                               0.72
 3: 2521320                               0.72
 4: 2521330                               0.74
 5: 2521340                               0.74
 6: 2521350                               0.73
 7: 2521360                               0.74
 8: 2521370                               0.74
 9: 2521380                               0.74
10: 2521390                               0.74
11: 2521400                               0.74
12: 2521410                               0.89
13: 2521420                               1.01 <- 100-block median block size increases. Block size is over 1MB
14: 2521430                               1.26
15: 2521440                               1.26
16: 2521450                               1.12
17: 2521460                               1.20
18: 2521470                               0.90
19: 2521480                               1.19
20: 2521490                               1.28
21: 2521500                               1.53
22: 2521510                               1.65 <- `--block-sync-size 20` does not sync past 2521517
23: 2521520                               1.51
24: 2521530                               1.52
25: 2521540                               1.53
26: 2521550                               1.55
27: 2521560                               1.55
28: 2521570                               1.57 <- `--block-sync-size 19-16` does not sync past 2521576
29: 2521580                               1.58
30: 2521590                               1.59
31: 2521600                               1.59
32: 2521610                               1.60
33: 2521620                               1.61
34: 2521630                               1.62
35: 2521640                               1.63
36: 2521650                               1.64
37: 2521660                               1.64
38: 2521670                               1.65
39: 2521680                               1.66
40: 2521690                               1.68
41: 2521700                               1.68 <- `--block-sync-size 15` does not sync past 2521702
42: 2521710                               1.68
43: 2521720                               1.69
44: 2521730                               1.70
45: 2521740                               1.72
46: 2521750                               1.73
47: 2521760                               1.73
48: 2521770                               1.74
49: 2521780                               1.75
50: 2521790                               0.69
51: 2521800                               0.04 <- txpool backlog consumed. Back to small blocks
52: 2521810                               0.00
53: 2521820                               0.00
54: 2521830                               0.10
55: 2521840                               0.00
56: 2521850                               0.01
57: 2521860                               0.21
58: 2521870                               0.00
59: 2521880                               0.00
60: 2521890                               0.00
61: 2521900                               0.00
62: 2521910                               0.00
63: 2521920                               0.00
64: 2521930                               0.00
65: 2521940                               0.15
66: 2521950                               0.02
67: 2521960                               0.01
68: 2521970                               0.00
69: 2521980                               0.00
70: 2521990                               0.00
```


The 10 block rolling mean of number of transactions per block is:

```txt
     height num_txes.10.block.rolling.mean
 1: 2521300                          471.0
 2: 2521310                          471.8
 3: 2521320                          473.2
 4: 2521330                          290.8
 5: 2521340                          195.0
 6: 2521350                          284.2
 7: 2521360                          227.4
 8: 2521370                          297.4
 9: 2521380                          481.8
10: 2521390                          482.9
11: 2521400                          483.1
12: 2521410                          454.1
13: 2521420                          532.7 <- 100-block median block size increases. Block size is over 1MB
14: 2521430                          613.6
15: 2521440                          601.2
16: 2521450                          578.2
17: 2521460                          592.2
18: 2521470                          477.6
19: 2521480                          557.4
20: 2521490                          589.7
21: 2521500                          734.4
22: 2521510                          821.4 <- `--block-sync-size 20` does not sync past 2521517
23: 2521520                          989.3
24: 2521530                          995.0
25: 2521540                         1002.3
26: 2521550                         1013.6
27: 2521560                         1015.9
28: 2521570                         1023.3 <- `--block-sync-size 19-16` does not sync past 2521576
29: 2521580                         1030.2
30: 2521590                         1040.1
31: 2521600                         1041.2
32: 2521610                         1042.8
33: 2521620                         1049.5
34: 2521630                         1056.7
35: 2521640                         1067.8
36: 2521650                         1069.1
37: 2521660                         1070.6
38: 2521670                         1077.3
39: 2521680                         1084.4
40: 2521690                         1096.7
41: 2521700                         1098.1 <- `--block-sync-size 15` does not sync past 2521702
42: 2521710                         1099.6
43: 2521720                         1106.5
44: 2521730                         1113.9
45: 2521740                         1127.2
46: 2521750                         1128.8
47: 2521760                         1130.5
48: 2521770                         1137.1
49: 2521780                         1144.8
50: 2521790                          448.8
51: 2521800                           23.6 <- txpool backlog consumed. Back to small blocks
52: 2521810                            0.2
53: 2521820                            0.0
54: 2521830                           67.6
55: 2521840                            0.0
56: 2521850                            6.6
57: 2521860                           93.5
58: 2521870                            0.0
59: 2521880                            0.0
60: 2521890                            0.0
61: 2521900                            0.0
62: 2521910                            0.0
63: 2521920                            2.2
64: 2521930                            0.0
65: 2521940                           98.3
66: 2521950                           13.3
67: 2521960                            4.7
68: 2521970                            2.7
69: 2521980                            0.0
70: 2521990                            0.0
```



## ronohara | 2024-09-08T08:04:57+00:00
I started spinning up a new node yesterday and hit the same sort of problem but on the mainnet. I didn't record the blockheight where it occurred, but I am sure it is not triggered by the content of blocks. 

 I get repeated message like Sync data returned a new top block candidate: 2521517 -> 2524276 [Your node is 2508897 blocks (6.8 years) behind]... then SYNC starts again.

I tried restarting the node multiple times but it always went back into that repeating message.

BUT when I resumed the node in the early hours of the day this morning it happily went past that and has continued nicely (still syncing now - 87% done).

In the afternoon here, the internet is pretty congested, but in the early AM it is not. To me that indicates that the issue was that my system was getting a new genuine top block (number increasing each time), before it had received and processed the current 20 block chunk. Probably blocks not received (internet congestion) rather than CPU limits (lightly loaded 8 way CPU) 

Because it recovered when I restarted in the morning - with no changes to the setup - it seems to be timing related and triggered by network congestion.  I didn't need to try your suggestion of  --block-sync-size 1



# Action History
- Created by: rbrunner7 | 2024-06-28T15:41:11+00:00
