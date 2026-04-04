---
title: Monero blocks indefinitely when sweeping unmixable outputs
source_url: https://github.com/monero-project/monero/issues/3409
author: lomacks
assignees: []
labels: []
created_at: '2018-03-15T04:27:11+00:00'
updated_at: '2022-03-16T15:37:49+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:37:49+00:00'
---

# Original Description
If I have a non-zero locked balance, and attempt to sweep unmixable outputs, the client blocks indefinitely - or at least until the connection to monerod times out, and the client has to be restarted. Presumably it is blocking until all outputs are unlocked in order to finish constructing the transaction.

I have only tested this using the GUI client, but I believe the issue is within common monero wallet code. I am using the 0.11.1.0 release.

Intended behaviour should be to either not block (if possible); or otherwise disable the "sweep unmixable" function (and GUI button) until all outputs are unlocked.

I have included a partial stack trace below. Thanks.

```
2018-03-15 00:27:13.820   0x70000ffe6000        INFO    wallet.wallet2  src/wallet/wallet2.cpp:1793     Refresh done, blocks received: 0, balance: [REDACTED], unlocked: [REDACTED, but lower than total balance]
2018-03-15 00:27:17.159   0x7fffa0916340        DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:4863     Using v2 rules
2018-03-15 00:27:17.199   0x7fffa0916340        DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:4863     Using v4 rules
2018-03-15 00:27:17.279   0x7fffa0916340        DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:4863     Using v6 rules
```
... the client locks up, time passes, and eventually the connection to the daemon times out...
```
2018-03-15 00:28:18.820   0x70000ffe6000        DEBUG   net     contrib/epee/include/net/net_helper.h:392       Problems at read: Operation canceled
2018-03-15 00:28:18.826   0x70000ffe6000        ERROR   net.http        contrib/epee/include/net/http_client.h:444      Unexpected recv fail
2018-03-15 00:28:18.826   0x70000ffe6000        INFO    net.http        contrib/epee/include/storages/http_abstract_invoke.h:50 Failed to invoke http request to  /json_rpc
```


# Discussion History
## moneromooo-monero | 2018-09-14T11:08:21+00:00
Current master now has several improvements to do with RPC speed and timeouts.
Does this still happen for you now ?

## moneromooo-monero | 2018-10-12T20:30:51+00:00
That's now on a released binary. Still happening ?

## moneromooo-monero | 2018-11-04T12:48:29+00:00
ping

## moneromooo-monero | 2019-06-15T10:54:54+00:00
ping, 0.14.1.0 released now, and it should not do this anymore. If no reply soon, I'll close as fixed.

# Action History
- Created by: lomacks | 2018-03-15T04:27:11+00:00
- Closed at: 2022-03-16T15:37:49+00:00
