---
title: Sweep_all command in CLI wallet only sweeps half of balance.
source_url: https://github.com/monero-project/monero/issues/7990
author: downystreet
assignees: []
labels: []
created_at: '2021-10-04T02:11:42+00:00'
updated_at: '2021-10-07T17:28:13+00:00'
type: issue
status: closed
closed_at: '2021-10-04T02:15:11+00:00'
---

# Original Description
Wallet Version: CLI Monero 'Oxygen Orion' (v0.17.2.3-release)

The sweep_all command only sent half of my full balance to the address. A second sweep_all command sent the rest of it. My wallet balance was empty previously and I received monero from two different addreses in different amounts. The sweep_all command sent the exact amount of the individual amounts received previously. I wasn't paying attention to the first transaction when the y/n authorization came up and I went ahead with it only sending the amount of a previously received amount. I thought sweep_all was supposed to send the entire balance? 
![sweep_all1](https://user-images.githubusercontent.com/63488055/135783700-49bcbfc9-52b8-45fb-ad31-2ae14ae5f217.png)


# Discussion History
## selsta | 2021-10-04T02:15:11+00:00
```
[wallet]: help sweep_all
Command usage: 
  sweep_all [index=<N1>[,<N2>,...] | index=all] [<priority>] [<ring_size>] [outputs=<N>] <address> [<payment_id (obsolete)>]

Command description: 
  Send all unlocked balance to an address. If the parameter "index=<N1>[,<N2>,...]" or "index=all" is specified, the wallet sweeps outputs received by those or all address indices, respectively. If omitted, the wallet randomly chooses an address index to be used. If the parameter "outputs=<N>" is specified and  N > 0, wallet splits the transaction into N even outputs.
```

You have to use `sweep_all index=all` if you want to sweep from all subaddress indices in one transaction.

## downystreet | 2021-10-04T02:19:21+00:00
Good to know. 

## trasherdk | 2021-10-07T16:17:28+00:00
It says `[<payment_id (obsolete)>]` Okay.
What about `[<ring_size>]` Is that still an option?

## selsta | 2021-10-07T17:28:13+00:00
> What about [<ring_size>] Is that still an option?

No, it should fail with different ring sizes. I guess the help text should update.

# Action History
- Created by: downystreet | 2021-10-04T02:11:42+00:00
- Closed at: 2021-10-04T02:15:11+00:00
