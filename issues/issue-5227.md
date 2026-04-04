---
title: Stagenet node syncing bad chain
source_url: https://github.com/monero-project/monero/issues/5227
author: du2zy
assignees: []
labels: []
created_at: '2019-03-04T13:34:55+00:00'
updated_at: '2019-04-23T15:41:59+00:00'
type: issue
status: closed
closed_at: '2019-04-23T15:41:59+00:00'
---

# Original Description
Hello!

My stagenet node stops syncing at 276916 block. It has not updates about last 6 hours. But I see only 273336 blocks in explorer.

It strange situation. Can anybody explain, what it means?


# Discussion History
## du2zy | 2019-03-04T16:02:21+00:00
I was cleaned up monero folder and was restarted syncing. I found a line in the log:
```
2019-03-04 15:27:36.957	[P2P7]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[46.101.93.177:37020 INC] Sync data returned a new top block candidate: 128431 -> 276916 [Your node is 148485 blocks (103 days) behind] 
```
I was DROP this IP with iptables. After it seems synchronization has returned to normal (Last block in https://community.xmr.to/explorer/stagenet/ explorer and last block in my log are equals). 

```
2019-03-04 15:56:44.318	[P2P3]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1179	[***]  Synced 137631/273421 (50% 135790 blocks remaining)
```

What it means? I was connected to bad node with fake blockchain? It is possible to protect my test node in future?

## moneromooo-monero | 2019-03-04T18:54:20+00:00
There is nothing suggesting a fake blockchain here.
Try with #5225

## moneromooo-monero | 2019-03-04T18:55:09+00:00
Or with current release-v0.13 branch (this is what will be the future 0.14.0.2), whch already has that patch.

## du2zy | 2019-03-04T19:11:18+00:00
I had similar problem with v0.13.0.4 a few days ago.
Do you have an updated precompiled binaries with this fix (any branch)? I don't want to compile it.
What plans about 0.14.0.2 release? Will it be distributed as binary files? What is the timeline?
Thanks for answers.

## du2zy | 2019-03-04T19:15:11+00:00
Does this problem only occur in stagenet?
Does this need to be fixed for Mainnet too?


## moneromooo-monero | 2019-03-04T20:16:33+00:00
There will be prebuilt binaries soon. Probably within a day or two. The problem is that once you've gone on a particular version past a consensus fork, you can't reorg back past the block where the consensus rules change. The patch fixes this. Once you have the patch, it works for stagenet as well as mainnet and testnet.

## moneromooo-monero | 2019-03-08T00:54:56+00:00
There are 0.14.0.2 binaries now on https://ww.getmonero.org/downloads/

## moneromooo-monero | 2019-03-16T22:19:15+00:00
Can you sync to the correct chain now with 0.14.0.2 ?

## moneromooo-monero | 2019-03-31T19:01:44+00:00
ping

## moneromooo-monero | 2019-04-17T12:06:44+00:00
I'll close as fixed in a few days if there's no more comment.

## moneromooo-monero | 2019-04-23T15:34:34+00:00
+resolved

# Action History
- Created by: du2zy | 2019-03-04T13:34:55+00:00
- Closed at: 2019-04-23T15:41:59+00:00
