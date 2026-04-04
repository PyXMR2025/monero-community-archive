---
title: failed to get random outs
source_url: https://github.com/monero-project/monero/issues/2028
author: AJIekceu4
assignees: []
labels: []
created_at: '2017-05-15T01:58:10+00:00'
updated_at: '2017-05-15T20:08:18+00:00'
type: issue
status: closed
closed_at: '2017-05-15T20:07:54+00:00'
---

# Original Description
Hello ALL.
Wallet: Monero 'Wolfram Warptangent' (v0.10.3.1-9ed496b)
Remote node: Monero 'Wolfram Warptangent' (v0.10.3.1-9a9fb04)

Trying to send some monero from **mining** wallet to another:

> No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y
> Error: failed to get random outputs to mix: failed to get random outs

> sweep_unmixable
> Wallet password: ********
> Error: No unmixable outputs found

> sweep_all 48xxx
> Wallet password: ********
> No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): y
> Error: failed to get random outputs to mix: failed to get random outs

But i can successfully transfer not big amount, like 1/25 of total wallet balance. 


# Discussion History
## moneromooo-monero | 2017-05-15T15:06:01+00:00
Is your daemon slow ? The wallet might be hitting a timeout. If the daemon isn't on 127.0.0.1 (but is on the local network), you may want to add --trusted-daemon, which makes that call a lot faster (at the cost of leaking some private info from the wallet to the daemon).


## AJIekceu4 | 2017-05-15T15:51:40+00:00
> Is your daemon slow ?

Maybe, it running on 2 cores cpu. 

> The wallet might be hitting a timeout. If the daemon isn't on 127.0.0.1 (but is on the local network), you may want to add --trusted-daemon, which makes that call a lot faster (at the cost of leaking some private info from the wallet to the daemon).

But "Error: failed to get random outputs to mix: failed to get random outs" appears after 2-3 second after transfer command. I think timeout time is much bigger than few seconds.

Anyway, i add --trusted-daemon, but nothing change. Command "sweep_unmixable" has same output, but much faster, about 2 second. But i still can not use transfer or sweep_all  because get "Error: failed to get random outputs to mix: failed to get random outs" after few seconds. 


## moneromooo-monero | 2017-05-15T15:59:34+00:00
Then level 2 log in both daemon and wallet, please.

## AJIekceu4 | 2017-05-15T20:07:54+00:00
Thanks to moneromooo ;)
My problem was related with "--restricted-rpc" option in daemon start parameters. Without this - all OK.

# Action History
- Created by: AJIekceu4 | 2017-05-15T01:58:10+00:00
- Closed at: 2017-05-15T20:07:54+00:00
