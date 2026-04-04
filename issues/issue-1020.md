---
title: bitmonerod example for start_miner is incorrect
source_url: https://github.com/monero-project/monero/issues/1020
author: quanah
assignees: []
labels: []
created_at: '2016-08-30T21:30:48+00:00'
updated_at: '2016-12-15T17:44:12+00:00'
type: issue
status: closed
closed_at: '2016-12-15T17:33:25+00:00'
---

# Original Description
Output of help is:

  start_mining         Start mining for specified address, start_mining <addr> [threads=1]

However, the format is actually
  start_mining         Start mining for specified address, start_mining <addr> [<threads>]


# Discussion History
## JamesCullum | 2016-09-02T20:05:04+00:00
Fixed it yourself https://github.com/monero-project/bitmonero/commit/1d5ba65f3dfc498fbbfac7e00b6e434022816eaf, didnt you? Consider closing the issue then.


## quanah | 2016-12-15T17:44:12+00:00
Yep!

# Action History
- Created by: quanah | 2016-08-30T21:30:48+00:00
- Closed at: 2016-12-15T17:33:25+00:00
