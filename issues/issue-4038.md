---
title: How to restore tx key in cli from mymonero ? cmds needed
source_url: https://github.com/monero-project/monero/issues/4038
author: Gyng3r
assignees: []
labels:
- invalid
created_at: '2018-06-22T13:23:47+00:00'
updated_at: '2018-06-22T14:52:48+00:00'
type: issue
status: closed
closed_at: '2018-06-22T13:57:04+00:00'
---

# Original Description
Hello, 
i need the tx key from a transaction which i sent from mymonero.com. Currently I have the cli version  0.12.2.0 downloaded and synchronized with the blockchain. What are the commands for the cli to restore the cache where the TX Key is located ? When i use this tutorial https://www.monero.how/tutorial-how-to-prove-payment , i become a error no tx found.

# Discussion History
## stoffu | 2018-06-22T13:52:26+00:00
That functionality is nonexistent AFAIK. You can tag this issue as “feature request”.

## moneromooo-monero | 2018-06-22T13:52:34+00:00
If you sent it with mymonero, mymonero would have it (and AFAIK it doesn't keep them). They're not on the blockchain. Pleae keep this bug tracker for bug reports. You can get help on reddit, or #monero on Freenode.

+invalid


## stoffu | 2018-06-22T14:52:48+00:00
I think I misunderstood the intent of the question. No, it's not possible to recover tx secret keys when you restore your wallet from seed, as @moneromooo-monero explained.

I thought about the ability to import tx keys from outside services like MyMonero to wallets restored using the CLI/GUI useful, which would then enable generating tx proofs. But this use case may be fairly niche, I suppose.


# Action History
- Created by: Gyng3r | 2018-06-22T13:23:47+00:00
- Closed at: 2018-06-22T13:57:04+00:00
