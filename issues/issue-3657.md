---
title: 'Post-upgrade issue: blockheight stuck despite doing blockchain rollback'
source_url: https://github.com/monero-project/monero/issues/3657
author: khelle
assignees: []
labels: []
created_at: '2018-04-18T11:52:32+00:00'
updated_at: '2018-04-19T11:35:44+00:00'
type: issue
status: closed
closed_at: '2018-04-19T11:35:44+00:00'
---

# Original Description
I was not aware that any fork is being made in XMR, so I did not update my node in time. I tried to do it today (18 April), but have problems with synchronization. I did following steps:

1. My node previously reached height of around ~1554000 on alt chain split so according to #3578 I needed to rollback the blockchain. Using node v0.11 I did:

```
monero-blockchain-import --pop-blocks 10000
```

After doing that my node reported being at ~1544000, so before the fork happened.

2. I updated the node to v0.12, and started it.

3. It updated from ~1544000 to 1546040, and after that it stuck with following log output:

```
2018-04-18 10:37:30.596	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[193.70.42.105:18080 OUT] Sync data returned a new top block candidate: 1546040 -> 1553833 [Your node is 7793 blocks (10 days) behind] 
SYNCHRONIZATION started
2018-04-18 10:39:35.790	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[220.145.106.236:52121 INC] Sync data returned a new top block candidate: 1546040 -> 1553835 [Your node is 7795 blocks (10 days) behind] 
SYNCHRONIZATION started
2018-04-18 10:42:32.332	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[76.232.45.157:64659 INC] Sync data returned a new top block candidate: 1546040 -> 1554191 [Your node is 8151 blocks (11 days) behind] 
SYNCHRONIZATION started
2018-04-18 10:43:08.077	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[81.4.104.14:18080 OUT] Sync data returned a new top block candidate: 1546040 -> 1553836 [Your node is 7796 blocks (10 days) behind] 
SYNCHRONIZATION started
2018-04-18 10:49:22.063	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[76.232.45.157:50045 INC] Sync data returned a new top block candidate: 1546040 -> 1554191 [Your node is 8151 blocks (11 days) behind] 
SYNCHRONIZATION started
2018-04-18 10:51:52.313	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[84.47.80.18:55652 INC] Sync data returned a new top block candidate: 1546040 -> 1553842 [Your node is 7802 blocks (10 days) behind] 
SYNCHRONIZATION started
2018-04-18 11:01:05.249	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[62.210.55.52:18080 OUT] Sync data returned a new top block candidate: 1546040 -> 1553847 [Your node is 7807 blocks (10 days) behind] 
SYNCHRONIZATION started
2018-04-18 11:01:53.346	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[37.230.160.42:18080 OUT] Sync data returned a new top block candidate: 1546040 -> 1553848 [Your node is 7808 blocks (10 days) behind] 
SYNCHRONIZATION started
2018-04-18 11:07:17.449	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[5.8.195.146:1189 INC] Sync data returned a new top block candidate: 1546040 -> 1553850 [Your node is 7810 blocks (10 days) behind] 
SYNCHRONIZATION started
2018-04-18 11:18:44.522	[P2P4]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[76.21.40.137:60988 INC] Sync data returned a new top block candidate: 1546040 -> 1553853 [Your node is 7813 blocks (10 days) behind] 
SYNCHRONIZATION started
2018-04-18 11:19:32.772	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[24.21.89.11:18080 OUT] Sync data returned a new top block candidate: 1546040 -> 1553855 [Your node is 7815 blocks (10 days) behind] 
SYNCHRONIZATION started
2018-04-18 11:29:54.185	[P2P8]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[193.112.183.206:47046 INC] Sync data returned a new top block candidate: 1546040 -> 1553861 [Your node is 7821 blocks (10 days) behind] 
SYNCHRONIZATION started
2018-04-18 11:30:27.275	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[66.70.218.224:18080 OUT] Sync data returned a new top block candidate: 1546040 -> 1553861 [Your node is 7821 blocks (10 days) behind] 
SYNCHRONIZATION started
2018-04-18 11:31:49.750	[P2P1]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[106.14.3.84:52484 INC] Sync data returned a new top block candidate: 1546040 -> 1553862 [Your node is 7822 blocks (10 days) behind] 
SYNCHRONIZATION started
2018-04-18 11:35:34.955	[P2P5]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[65.31.165.228:11242 INC] Sync data returned a new top block candidate: 1546040 -> 1553864 [Your node is 7824 blocks (10 days) behind] 
SYNCHRONIZATION started
```

What did I do wrong?

# Discussion History
## moneromooo-monero | 2018-04-18T15:33:19+00:00
Restart monerod with --log-level 1 to get more info on why blocks fail to add.

## khelle | 2018-04-19T11:35:44+00:00
Ok, after adding --log-level=1 for some reason it started to sync again. I am not sure what the problem was, because I was restarting it previously few times and restart by itself did not help. I believe it is not possible for me to reproduce this.

# Action History
- Created by: khelle | 2018-04-18T11:52:32+00:00
- Closed at: 2018-04-19T11:35:44+00:00
