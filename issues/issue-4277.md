---
title: monerod in testnet says it needs upgrading ?
source_url: https://github.com/monero-project/monero/issues/4277
author: gituser
assignees: []
labels:
- invalid
created_at: '2018-08-17T18:12:05+00:00'
updated_at: '2018-08-17T20:19:48+00:00'
type: issue
status: closed
closed_at: '2018-08-17T20:16:50+00:00'
---

# Original Description
Hi.

I've just build latest `master` branch and monerod status gives me that there is an update needed (for some reason):

```
 monero-testnet-dev:~$ ./monerod --testnet status
Height: 1166281/1166281 (100.0%) on testnet, not mining, net hash 339 H/s, v8, update needed, 14(out)+0(in) connections, uptime 0d 0h 0m 41s
```

Any idea how to fix this?

# Discussion History
## moneromooo-monero | 2018-08-17T20:08:07+00:00
You can either ignore it, or comment out the message in the source. I'll go away when a new fork is set up, within about a month.

+invalid


## gituser | 2018-08-17T20:19:48+00:00
I've just implemented some check to shut down monerod if it says that it has been forked, that's why I've asked about testnet update issue.

OK, thanks for the clarification.

# Action History
- Created by: gituser | 2018-08-17T18:12:05+00:00
- Closed at: 2018-08-17T20:16:50+00:00
