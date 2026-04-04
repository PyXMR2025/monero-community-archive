---
title: CLI not connecting to Daemon - macOS 10.13.5 - GUI does connect
source_url: https://github.com/monero-project/monero/issues/4053
author: apxs94
assignees: []
labels: []
created_at: '2018-06-25T20:44:02+00:00'
updated_at: '2018-10-08T12:32:58+00:00'
type: issue
status: closed
closed_at: '2018-10-08T12:32:58+00:00'
---

# Original Description
Hi,

- macOS 10.13.5 on 2017 Macbook Pro

- Tested using 0.12.0.0 and 0.12.2.0

Error message I'm getting is:
```
Starting refresh...
Error: refresh failed: no connection to daemon. Please make sure daemon is running.. Blocks received: 0
Background refresh thread started
[wallet 494sdi (out of sync)]: 
```
- No antivirus or software firewall running.
- Blockchain is running from extermal USB
- GUI does sync from the daemon (oddly), just not CLI

Looking at the CLI log, this is the main error I get:

```
2018-06-25 19:26:42.620   0x7fff98967380        ERROR   net.http        contrib/epee/include/net/http_client.h:456      Unexpected recv fail
2018-06-25 19:26:42.622   0x7fff98967380        ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1706     !r. THROW EXCEPTION: error::no_connection_to_daemon
2018-06-25 19:26:42.623   0x7fff98967380        WARN    net.http        src/wallet/wallet_errors.h:794  /DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:1706:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = gethashes.bin
2018-06-25 19:26:42.627   0x7fff98967380        ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: refresh failed: no connection to daemon. Please make sure daemon is running.. Blocks received: 0
```

Unsure how to further debug, help much appreciated.

# Discussion History
## apxs94 | 2018-06-26T12:20:56+00:00
@stoffu 
Can you recommend any further debugging I could do for this?

## stoffu | 2018-06-27T02:01:00+00:00
Probably it's because of the timeout being too low, which was fixed in #3962.

## apxs94 | 2018-06-27T12:01:25+00:00
@stoffu 
Thanks for the reply! Appreciate it.
Ok, will cross my fingers #3962 fixes it.
If I want to test, I can either compile latest master, or, wait until it's released?
Just checking if they're my two options? As I'm not v familiar with github/builds etc.

## stoffu | 2018-06-27T13:26:37+00:00
If you can, please try building the latest master and report if your problem is indeed fixed. Otherwise, you'd have to wait for the next release binary.

## moneromooo-monero | 2018-10-06T18:43:56+00:00
Fixed with current master/0.13 branch ?

## apxs94 | 2018-10-08T04:21:59+00:00
> Fixed with current master/0.13 branch ?

Yes, thank you.

## moneromooo-monero | 2018-10-08T12:27:27+00:00
Thanks for checking.

+resolved

# Action History
- Created by: apxs94 | 2018-06-25T20:44:02+00:00
- Closed at: 2018-10-08T12:32:58+00:00
