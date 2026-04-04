---
title: Cannot connect to peers
source_url: https://github.com/monero-project/monero/issues/2268
author: jtgrassie
assignees: []
labels: []
created_at: '2017-08-08T17:53:16+00:00'
updated_at: '2017-08-09T18:35:55+00:00'
type: issue
status: closed
closed_at: '2017-08-09T18:35:55+00:00'
---

# Original Description
With latest merged code (and also tested with #2267) I cannot connect to peers. Logs cluttered with:
```
2017-08-08 17:45:40.877	[P2P0]	ERROR	net.p2p	src/p2p/net_node.inl:808	[x.x.x.x:18080 OUT] COMMAND_HANDSHAKE Failed
2017-08-08 17:45:47.983	[P2P7]	ERROR	net.p2p	src/p2p/net_node.inl:759	[x.x.x.x:18080 OUT] COMMAND_HANDSHAKE invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)
```

# Discussion History
## moneromooo-monero | 2017-08-08T18:23:55+00:00
2267 is for the listening node. You have wait for the mining nodes to use that, which should be soon.

## jtgrassie | 2017-08-08T18:26:05+00:00
Gotcha. So basically don't run master HEAD till miners have updated? 

## moneromooo-monero | 2017-08-08T18:27:34+00:00
You can run master + 2267 now to be on v6 (long term branch). You can run v5 if you need to test things. up to you.


## jtgrassie | 2017-08-08T19:22:19+00:00
master + 2267 has the same problem though. Daemon doesn't connect to any peers / nodes and so no blocks are sync'ed and no mining occurs.

## moneromooo-monero | 2017-08-08T22:07:25+00:00
As I said, 2267 is for the *listening* node.
I'm synced to v6 testnet at the moment, so the fix is working. You might be banned by the mining node, however, if you were trying funny things to try to get to sync (I was). Try: --add-priority-node 62.210.104.109:28080

## jtgrassie | 2017-08-08T22:16:55+00:00
I simply pulled master, built and launched daemon. Nothing "funny" ;)

## jtgrassie | 2017-08-08T23:42:09+00:00
Even with:

> Try: --add-priority-node 62.210.104.109:28080

Still same problem. Same logs as above. Note this is on OSX, master (with or without 2267 applied).

## jtgrassie | 2017-08-08T23:48:57+00:00
So essentially I am stuck at block 1371359 when current height is 1372412 and no way to sync with master. It's definitely a networking issue as it cannot to peers. I know there were some networking patches and I assume it is these that have broken things on OSX at least.

## moneromooo-monero | 2017-08-09T08:52:35+00:00
Oh, with those heights, that's mainnet ? I thought you were on about testnet, where we had some trouble. That's way more concerning, I'll have a look.

## moneromooo-monero | 2017-08-09T08:59:07+00:00
I can connect to mainnet with current master, and it's syncing. I'm at about 500k height though, but I don't see what it's break at 1371359.
Can you run with --log-level 1,net\*:DEBUG and post the log please ?

## jtgrassie | 2017-08-09T11:32:43+00:00
Correct, mainnet. I reverted to the old master before all this weekends merges and it worked fine so definitely a recent merge causing the problem. Rebuilding with current master and will post the log after a run.

## moneromooo-monero | 2017-08-09T12:09:29+00:00
Uploading zip files causes github to put them on amazon, and downloading triggers some XSS protection, which I'm not disabling. Can you put the interesting part on gist.github.com, or fpaste.org, or pastebin.mozilla.org please ?

## jtgrassie | 2017-08-09T12:28:00+00:00
I'm not too sure what the most interesting bit is so here is a run (on gist).

[bitmonero.log](https://gist.github.com/jtgrassie/9c80e91b7e8af6bf8aa70e12ee36cfb7#file-bitmonero-log)

## moneromooo-monero | 2017-08-09T18:03:17+00:00
https://github.com/monero-project/monero/pull/2271

## jtgrassie | 2017-08-09T18:35:29+00:00
OK, rebuilt with #2271 and that fixes it. Well spotted @moneromooo-monero 

# Action History
- Created by: jtgrassie | 2017-08-08T17:53:16+00:00
- Closed at: 2017-08-09T18:35:55+00:00
