---
title: Overflow in amount of show_transfers for outgoing tx
source_url: https://github.com/monero-project/monero/issues/6667
author: arnuschky
assignees: []
labels: []
created_at: '2020-06-19T20:26:23+00:00'
updated_at: '2022-05-25T10:12:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I scanned an older operational wallet and I see a lot of overflows for the `amount` field for *some* outgoing transactions. Example:

```
 1816434,       in,unlocked,      2019-04-19 11:52:27,      0.006828880000,    349.352851863904,xxx,xxxxxxxxxxxxxxxx,0.000000000000,     4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,      0.006828880000,"xxx",
 1816434,      out,       -,      2019-04-19 11:52:27,18446743.92970955161,    349.496600933904,xxx,0000000000000000,0.000250930000,                                                                                                   -,                    ,"xxx",
 1816434,      out,       -,      2019-04-19 11:52:27,18446743.89844358242,    349.671615203100,xxx,0000000000000000,0.000251700000,                                                                                                   -,                    ,"xxx",
 1816434,       in,unlocked,      2019-04-19 11:52:27,      0.129829170000,    349.801444373100,xxx,xxxxxxxxxxxxxxxx,0.000000000000,     4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,      0.129829170000,"xxx",
 1816434,      out,       -,      2019-04-19 11:52:27,18446743.89570955161,    349.979193543100,xxx,0000000000000000,0.000250830000,                                                                                                   -,                    ,"xxx",              
 1816434,      out,       -,      2019-04-19 11:52:27,18446743.89570955161,    350.156942223100,xxx,0000000000000000,0.000251320000,                                                                                                   -,                    ,"xxx",
 1816434,       in,unlocked,      2019-04-19 11:52:27,      0.004828880000,    350.161771103100,xxx,xxxxxxxxxxxxxxxx,0.000000000000,     4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,      0.004828880000,"xxx",
 1816436,      out,       -,      2019-04-19 11:53:37,      0.110000000000,    350.051600183100,xxx,0000000000000000,0.000170920000,                                                                                                   -,                    ,"xxx",
 1816438,       in,unlocked,      2019-04-19 11:54:46,     10.000000000000,    360.051600183100,xxx,0000000000000000,0.000000000000,     8xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,     10.000000000000,"xxx",
 1816438,       in,unlocked,      2019-04-19 11:54:46,     10.000000000000,    370.051600183100,xxx,0000000000000000,0.000000000000,     8xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,     10.000000000000,"xxx",
```

Some pointers:
 - I only see this in approx the first half of 2019, none later in the year, nothing in 2020
 - Seems to be a pure display bug as the running balance is ok
 - Only outgoing tx are affected
 - Amount is clearly an overflow, some fixed value minus the real amount
 - Affects `show_transfers` as well as `export_transfers`
 - Confirmed with 0.15 and 0.16 CLI

# Discussion History
## moneromooo-monero | 2020-06-19T20:37:52+00:00
Did you restore your wallet from seed or keys at the cutoff point ?

## arnuschky | 2020-06-19T20:40:11+00:00
Both

## arnuschky | 2020-06-19T20:40:58+00:00
seed with 0.15 and keys with 0.16 to be exact

# Action History
- Created by: arnuschky | 2020-06-19T20:26:23+00:00
