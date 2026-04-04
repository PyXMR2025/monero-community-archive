---
title: Stop using MoneroPulse checkpointing and making unnecessary DNS queries unless
  explicitly enabled in wallet2
source_url: https://github.com/monero-project/monero/issues/8407
author: sethforprivacy
assignees: []
labels: []
created_at: '2022-06-27T17:14:43+00:00'
updated_at: '2022-07-06T14:04:06+00:00'
type: issue
status: closed
closed_at: '2022-07-06T14:04:05+00:00'
---

# Original Description
In finding a major (but rare) UX issue (transaction generation taking 20s+) was related to DNS, I also was pointed to the core problem being that wallet2 makes many DNS queries before it processes a transaction. These queries seem to go to many `moneropulse.*` domains (related to old checkpointing logic, more [here](https://monerodocs.org/infrastructure/monero-pulse/) and to a set of hard-coded DNS servers (found [here](https://github.com/monero-project/monero/blob/9a124f681119855949f6406ecd69c2ad91da9770/src/common/dns_utils.cpp#L46-L53)).

These queries happen even if using IP address for the selected node, and even if not sending to an OpenAlias address. Not only are these causing major UX issues for people who have strict capture/handling of DNS traffic (like DoH users, VPN users, and others), but it also allows trivial fingerprinting of Monero users along with pin-point accuracy to determine when a specific IP address generates (and likely sends) a transaction by a given DNS server along with all MoneroPulse operators (whoever they are).

This behavior should be moved to a manual flag (for those who still want MoneroPulse checkpointing for some reason) and disabled by default except for two specific use-cases:

1. A user is using a DNS address for their selected node
  - This should be handled by the devices DNS anyways, not by wallet2
2. A user enters an OpenAlias address in the address box of a given wallet
  - This also should be handled by the device itself and not wallet2

Here are some of the places these DNS addresses and servers are in the code:

- https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp
- https://github.com/monero-project/monero/blob/master/src/checkpoints/checkpoints.cpp
- https://github.com/monero-project/monero/blob/master/src/common/dns_utils.cpp

# Discussion History
## sethforprivacy | 2022-07-06T14:04:05+00:00
Resolved via https://github.com/monero-project/monero/pull/8408.

# Action History
- Created by: sethforprivacy | 2022-06-27T17:14:43+00:00
- Closed at: 2022-07-06T14:04:05+00:00
