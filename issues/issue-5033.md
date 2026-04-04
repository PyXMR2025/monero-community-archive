---
title: Ubuntu 16.04 Multiple Daemons - wallet failed to connect to daemon
source_url: https://github.com/monero-project/monero/issues/5033
author: BKdilse
assignees: []
labels: []
created_at: '2019-01-01T21:19:22+00:00'
updated_at: '2019-01-06T20:34:41+00:00'
type: issue
status: closed
closed_at: '2019-01-06T20:34:40+00:00'
---

# Original Description
Running `Monero 'Beryllium Bullet' (v0.13.0.4-ab6c17c)`

I have a Server running 11 CN Daemons, which I use to sync my various wallets.
A number of them, including Monero throw the `wallet failed to connect to daemon` error.  After several refresh attempts, I manage to sync ok.

Server has 12 Xeon Cores, and 8GB RAM, and does not appear to be overworked.
All Daemons are in sync.

Any ideas on how I can improve this?

# Discussion History
## moneromooo-monero | 2019-01-01T22:04:28+00:00
Is anything else than the wallet trying to use the monero RPC port ?


## BKdilse | 2019-01-02T08:41:15+00:00
Hi, no, nothing else is using those ports.  I've even tried shutting down all other daemons, and running monero only.

I am using a RAID10 HDD System.  I know it's not recommended, but not sure if that's causing the issue, as it syncs fine, and occasionally works?

## moneromooo-monero | 2019-01-02T10:20:19+00:00
If the daemon is synced, a HDD should be fine since there'll be just a small amount of disk access when a new block is received. It's really when syncing that a HDD hurts.
Run with --log-level 2, and see if there is any more information.

## BKdilse | 2019-01-02T10:42:10+00:00
Agreed, after sync, HDD should not be an issue.

DOH, I should have done the log bit (on the wallet I presume)?  I'll do that, and provide an update.

## BKdilse | 2019-01-02T10:52:26+00:00
Typical, monero has refreshed fine just now.

ETN is having an issue.  I'm not looking for ETN support, but as I have similar issues with XMR... does the below help at all?

```
2019-01-02 10:46:05.597	1116	INFO 	msgwriter	src/common/scoped_message_writer.h:103	Starting refresh...
2019-01-02 10:46:05.816	1116	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1254	Daemon is recent enough, asking for pruned blocks
2019-01-02 10:49:35.847	1116	DEBUG	net	contrib/epee/include/net/net_helper.h:392	Problems at read: The network connection was aborted by the local system
2019-01-02 10:49:35.863	1116	ERROR	net.http	contrib/epee/include/net/http_client.h:444	Unexpected recv fail
2019-01-02 10:49:35.863	1116	INFO 	net.http	contrib/epee/include/storages/http_abstract_invoke.h:81	Failed to invoke http request to  /getblocks.bin
2019-01-02 10:49:35.863	1116	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1268	!r. THROW EXCEPTION: error::no_connection_to_daemon
2019-01-02 10:49:35.894	1116	WARN 	net.http	src/wallet/wallet_errors.h:708	C:/BuildAgent/work/3a1e8c3d1f94e6ca/src/wallet/wallet2.cpp:1268:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getblocks.bin
2019-01-02 10:49:35.972	1116	ERROR	msgwriter	src/common/scoped_message_writer.h:103	Error: refresh failed: no connection to daemon. Please make sure daemon is running.. Blocks received: 0
2019-01-02 10:49:35.972	1116	INFO 	msgwriter	src/common/scoped_message_writer.h:103	Background refresh thread started

```

## moneromooo-monero | 2019-01-02T14:54:21+00:00
That's a timeout. Log the dameon on level 2 as well, so we can see whether it's getting the request or not. And please use master, to make sure we're not hunting something that already got fixed.

## BKdilse | 2019-01-04T20:13:06+00:00
Sorry for the delay, I'll give that a go, and get back.  Is there anything specific I should be looking for, as that level show quite a lot of information.

## moneromooo-monero | 2019-01-04T20:41:03+00:00
Best to set the log level to 2 just before you try it, set it back to 0 when done, and paste the thing to paste.debian.net or fpaste.org, and post the URL here. I'll sift through for anything interesting.

## BKdilse | 2019-01-06T20:34:40+00:00
Typical, it's still not doing it :)

I'll close this for now, and using the tips you've suggested in future, and report back.

Thanks again.

# Action History
- Created by: BKdilse | 2019-01-01T21:19:22+00:00
- Closed at: 2019-01-06T20:34:40+00:00
