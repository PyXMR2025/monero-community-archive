---
title: getblocktemplate sometimes returns inconsistent prev_hash and height since
  version 0.13
source_url: https://github.com/monero-project/monero/issues/5011
author: cotinco
assignees: []
labels:
- duplicate
created_at: '2018-12-24T07:53:05+00:00'
updated_at: '2018-12-24T10:49:05+00:00'
type: issue
status: closed
closed_at: '2018-12-24T10:49:05+00:00'
---

# Original Description
Since upgrade to 0.13, RPC call getblocktemplate started to behave in a very strange way (it happens about one time per week in average). After switching to a new block, it returns blockchain height after a new block, but prev_hash still contains hash of previous one. After 10-30 seconds, prev_hash also becomes consistent (without finding any blocks or any other noticeable events). I'm not sure about validity of returned templates, but mining software goes crazy because it constantly thinks that there was a reorganization of blockchain due to hash of top block changed. There are no reorganizations, alternatives, exceptions or other records in daemon logs during such moments.

# Discussion History
## moneromooo-monero | 2018-12-24T10:44:26+00:00
https://github.com/monero-project/monero/issues/4922

+duplicate

# Action History
- Created by: cotinco | 2018-12-24T07:53:05+00:00
- Closed at: 2018-12-24T10:49:05+00:00
