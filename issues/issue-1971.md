---
title: WARN ge_frombytes_vartime failed at 266 ???
source_url: https://github.com/monero-project/monero/issues/1971
author: bart886
assignees: []
labels: []
created_at: '2017-04-13T22:29:05+00:00'
updated_at: '2017-04-14T13:26:43+00:00'
type: issue
status: closed
closed_at: '2017-04-14T13:26:43+00:00'
---

# Original Description
What is that warn in monerod? All blockchain is synchronized.
[P2P5]  WARN    ringct  src/ringct/rctOps.cpp:266       ge_frombytes_vartime failed at 266

# Discussion History
## moneromooo-monero | 2017-04-14T07:06:18+00:00
It tells you some part of the transaction's ringct signatures is invalid.


## bart886 | 2017-04-14T10:53:14+00:00
Ist`s not a bug or problem on my site?

## moneromooo-monero | 2017-04-14T13:22:50+00:00
No, this is normal if you're getting a bad tx. Some older monero version code can send those (though this was before rct was enabled), so I'm assuming someone is using that. But given it still happens nowadays, something may be off. Still, there's nothing wrong with your setup based on this.

## bart886 | 2017-04-14T13:26:11+00:00
ok thanks

# Action History
- Created by: bart886 | 2017-04-13T22:29:05+00:00
- Closed at: 2017-04-14T13:26:43+00:00
