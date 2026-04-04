---
title: Monero asks for enabling background mining even when `set setup-background-mining
  0` is given on the command line
source_url: https://github.com/monero-project/monero/issues/5695
author: hokkjoy
assignees: []
labels: []
created_at: '2019-06-25T20:28:42+00:00'
updated_at: '2019-06-25T20:38:32+00:00'
type: issue
status: closed
closed_at: '2019-06-25T20:38:32+00:00'
---

# Original Description
This is how this goes down:

1. Run `monero-wallet-cli set setup-background-mining 0`
2. Be asked what to do about bg mining
3. Answer `Y` for "enable"
4. Type `set` and find that it is disabled

So, the command does seem to run and have effect (4), but the client should probably not ask (3) in the first place in such a scenario.

# Discussion History
## hokkjoy | 2019-06-25T20:38:32+00:00
issue superseded by #5685

# Action History
- Created by: hokkjoy | 2019-06-25T20:28:42+00:00
- Closed at: 2019-06-25T20:38:32+00:00
