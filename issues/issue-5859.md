---
title: Multiple transfers to a single address in a single tx - show in the wallet
source_url: https://github.com/monero-project/monero/issues/5859
author: tmoravec
assignees: []
labels: []
created_at: '2019-08-27T07:31:05+00:00'
updated_at: '2019-08-29T09:13:12+00:00'
type: issue
status: closed
closed_at: '2019-08-29T09:13:12+00:00'
---

# Original Description
If I send multiple transfers to a single address in a single transaction, the receiving wallet shows a single transfer only. For example, this CLI command:

```
transfer 779M7jYCETTRQ2fXgcboJcYr7cGgLVEJh11ZZZDJdc4B9KwDHNQbnGX4paJhrrQbGqYDEC8F1djreV3ojURKmPQ5Tod25Jg  1 779M7jYCETTRQ2fXgcboJcYr7cGgLVEJh11ZZZDJdc4B9KwDHNQbnGX4paJhrrQbGqYDEC8F1djreV3ojURKmPQ5Tod25Jg  1 779M7jYCETTRQ2fXgcboJcYr7cGgLVEJh11ZZZDJdc4B9KwDHNQbnGX4paJhrrQbGqYDEC8F1djreV3ojURKmPQ5Tod25Jg  1
```

The transaction looks like this in `show_transfers` on the outgoing side (before `rescan_bc` - the details are apparently cached?)
```
397069    out       2019-08-27 07:21:48       3.000000000000 2fc45f6cd0a093ff9d4879d7db9293c980b55514954d62cb66842fbfd4bf54ac 0000000000000000 0.000377760000 779M7jYCETTRQ2fXgcboJcYr7cGgLVEJh11ZZZDJdc4B9KwDHNQbnGX4paJhrrQbGqYDEC8F1djreV3ojURKmPQ5Tod25Jg: 1.000000000000, 779M7jYCETTRQ2fXgcboJcYr7cGgLVEJh11ZZZDJdc4B9KwDHNQbnGX4paJhrrQbGqYDEC8F1djreV3ojURKmPQ5Tod25Jg: 1.000000000000, 779M7jYCETTRQ2fXgcboJcYr7cGgLVEJh11ZZZDJdc4B9KwDHNQbnGX4paJhrrQbGqYDEC8F1djreV3ojURKmPQ5Tod25Jg: 1.000000000000 1 - 
```

But the incoming side only shows a sum of the transfer amounts:
```
397069     in       2019-08-27 07:21:48       3.000000000000 2fc45f6cd0a093ff9d4879d7db9293c980b55514954d62cb66842fbfd4bf54ac 0000000000000000 1 - 
```


On the blockchain, the individual transfers are present, however. So I would love to access the individual transfer in the wallet on the incoming side, too. This would be useful when making/receiving multiple payments in a quick succession.

This is probably going to require changing the interface between the wallet and the daemon, and updating the RPC wallet interface as well. I can implement it but I'd love to hear your opinion, first. Thanks!


# Discussion History
## moneromooo-monero | 2019-08-27T10:52:32+00:00
incoming_transfers is the per output API. get_transfers is the per tx API.

## tmoravec | 2019-08-29T09:13:12+00:00
Drat, I'm dumb. Sorry for the confusion; closing.

# Action History
- Created by: tmoravec | 2019-08-27T07:31:05+00:00
- Closed at: 2019-08-29T09:13:12+00:00
