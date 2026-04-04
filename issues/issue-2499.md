---
title: DNSSEC validation causing very slow startup
source_url: https://github.com/monero-project/monero/issues/2499
author: jtgrassie
assignees: []
labels: []
created_at: '2017-09-20T21:07:12+00:00'
updated_at: '2017-09-30T16:15:04+00:00'
type: issue
status: closed
closed_at: '2017-09-30T16:15:04+00:00'
---

# Original Description
```
2017-09-20 21:02:43.934	  0x7fff73d47000	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:419	Loading checkpoints
2017-09-20 21:02:43.934	  0x7fff73d47000	INFO 	checkpoints	src/cryptonote_basic/checkpoints.cpp:182	Blockchain checkpoints file not found
2017-09-20 21:03:24.296	  0x7fff73d47000	DEBUG	net.dns	src/common/dns_utils.cpp:460	DNSSEC not available for checkpoint update at URL: checkpoints.moneropulse.co, skipping.
2017-09-20 21:03:24.296	  0x7fff73d47000	DEBUG	net.dns	src/common/dns_utils.cpp:465	DNSSEC validation failed for checkpoint update at URL: checkpoints.moneropulse.co, skipping.
2017-09-20 21:04:55.529	  0x7fff73d47000	DEBUG	net.dns	src/common/dns_utils.cpp:460	DNSSEC not available for checkpoint update at URL: checkpoints.moneropulse.se, skipping.
2017-09-20 21:04:55.529	  0x7fff73d47000	DEBUG	net.dns	src/common/dns_utils.cpp:465	DNSSEC validation failed for checkpoint update at URL: checkpoints.moneropulse.se, skipping.
```

# Discussion History
## jtgrassie | 2017-09-20T21:15:10+00:00
Looks related to [#2172 (comment)](https://github.com/monero-project/monero/issues/2172#issuecomment-315324536)

DNSSEC validation seems incorrectly implemented at present but also the timeouts look to be unnecessarily long IMHO, causing slow startup.

## moneromooo-monero | 2017-09-21T08:24:25+00:00
https://github.com/monero-project/monero/pull/2504 should help. Same timeouts, but all will run concurrently.

# Action History
- Created by: jtgrassie | 2017-09-20T21:07:12+00:00
- Closed at: 2017-09-30T16:15:04+00:00
