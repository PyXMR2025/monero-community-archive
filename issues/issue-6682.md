---
title: Why are clients connected to my node not paying any rpc hashes?
source_url: https://github.com/monero-project/monero/issues/6682
author: downystreet
assignees: []
labels: []
created_at: '2020-06-22T09:51:10+00:00'
updated_at: '2022-07-20T20:02:20+00:00'
type: issue
status: closed
closed_at: '2022-07-20T20:02:20+00:00'
---

# Original Description
When running the monero daemon and using the rpc_payments command it produces a long list of 403 clients. All of these clients have paid 0 hashes except for my own wallet. I was trying to find some information on this and the only thing I found was saying that the rpc payments function was not integrated into the gui wallets yet? I just wanted to make sure that everything is functioning normally here and I'm not leaving out some command that is causing connected clients to not mine hashes.

# Discussion History
## moneromooo-monero | 2020-06-22T10:08:26+00:00
I expect most people to not want to pay anything. For now, they'll use another free node. Hopefully there will be fewer of those,and ultimately none, pushing those people to either pay or use their own. That might take time though.

AFAIK the GUI does not have this system yet.

# Action History
- Created by: downystreet | 2020-06-22T09:51:10+00:00
- Closed at: 2022-07-20T20:02:20+00:00
