---
title: Unspendable dust outputs (> 0.00000582 XMR~)
source_url: https://github.com/monero-project/monero/issues/8405
author: hinto-janai
assignees: []
labels: []
created_at: '2022-06-24T20:08:53+00:00'
updated_at: '2022-10-11T17:03:46+00:00'
type: issue
status: closed
closed_at: '2022-07-09T12:56:09+00:00'
---

# Original Description
I've naturally accumulated a few dust outputs/change that are worth less than current fees (currently around 0.00000582 XMR), and due to the mandatory fees, they've essentially become unspendable.

I assumed if I had a single output that could cover fees like:
```
10 outputs worth 0.000005 XMR
1 output worth 1 XMR
```
`sweep_all` would pay for fees using the 1 XMR output, however it just skips over the dust outputs and sweeps the single 1 XMR output. I'm under the impression network consensus rejects transactions without any fees, so modifying wallet software is a no-go.

I'm aware that sweeping these outputs would actually lose me money (probably why sweeps don't include dust), but having a bunch of unspendable outputs does feel weird. For now, is this the only solution https://github.com/monero-project/monero/issues/1525#issuecomment-270388425?

# Discussion History
## plowsof | 2022-06-29T13:45:22+00:00
I'm a bit confused myself because:
```
sweep_unmixable - only relevant for very old wallets (<= 2016); send all unmixable outputs to yourself with ring_size 10
```
but `sweep_dust` appears in the monero rpc wallet hm

## moneromooo-monero | 2022-07-06T08:06:01+00:00
Outputs that do not pay for themselves increased fee are ignored. You can turn this off with "set ignore-fractional-outputs 0".
Consensus allows 0 fee txes, though nobody will mine them for you, you'd have to mine it yourself.

## Commodore6416 | 2022-07-06T08:29:33+00:00
Thank you man, I was just filling out an application and have no idea about GitHub. Fuck knows what I was doing on there.,.,,,sorry 

Sent from my iPhone

> On 6 Jul 2022, at 6:06 pm, moneromooo-monero ***@***.***> wrote:
> 
> ﻿
> Outputs that do not pay for themselves increased fee are ignored. You can turn this off with "set ignore-fractional-outputs 0".
> Consensus allows 0 fee txes, though nobody will mine them for you, you'd have to mine it yourself.
> 
> —
> Reply to this email directly, view it on GitHub, or unsubscribe.
> You are receiving this because you are subscribed to this thread.


## hinto-janai | 2022-07-09T12:56:09+00:00
> set ignore-fractional-outputs 0

I didn't think to look at the set commands. It works perfect, thanks. 

# Action History
- Created by: hinto-janai | 2022-06-24T20:08:53+00:00
- Closed at: 2022-07-09T12:56:09+00:00
