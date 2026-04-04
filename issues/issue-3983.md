---
title: '`show_transfers out` reports incorrect values'
source_url: https://github.com/monero-project/monero/issues/3983
author: moneroexamples
assignees: []
labels: []
created_at: '2018-06-11T06:04:05+00:00'
updated_at: '2018-06-11T23:02:22+00:00'
type: issue
status: closed
closed_at: '2018-06-11T23:02:22+00:00'
---

# Original Description
I'm using stagenet now and monero version `commit 25e7a7d96f2e46821d6613e6d2012b367dd70f38`.

seed for the stagenet wallet.

```
gels lair teeming cease nanny utility inexact leisure
civilian emerge zippers skew gasp enjoy fugitive nanny
candy nuance muppet scrub uneven yard ulcers unquoted yard
```

This corresponds to default wallet of open monero at stagenet (http://172.104.45.209:81/) and am pretty sure that outgoing values shown there are correct. But `monero-wallet-cli` shows very strange numbers of outgoing transfers (notice values of about 18446685.05933599319) for the same wallet.

```
[wallet 57Hx8Q]: show_transfers out
   91167    out       2018-06-06 18446657.97436341319 a783198e169e0fb8eee990cf41f40145497d0cee21abcaa0367c0dae5bc8279b 0000000000000000 0.063408800000  0 - 
   93138    out       2018-06-09      67.917661481583 bcc39dbc076818ee6e61252b7baeb83ed150678ba3eb93f020095ac0de368d2d 0000000000000000 0.017007620000  0 - 
   93643    out       2018-06-09 18446685.05933599319 1640236fe817f83b0bd2082c655d152be390e4f78e41db5b935bb8a53249fe8c 0000000000000000 0.067964960000  0 - 
   94433    out      07:49:44 PM 18445744.17672471161 87617d03aeab903262dacf764eb845b13a3775860acec23f2af595af43b8c295 0000000000000000 0.063015160000  0 - 
```

But the wallet balance is ok, so it seems that the values are incorrectly reported only for outgoing txs. These outgoing txs were not made using `monero-wallet-cli`.


# Discussion History
## stoffu | 2018-06-11T08:15:24+00:00
Yes, this seems like a bug.

## moneromooo-monero | 2018-06-11T11:07:22+00:00
https://github.com/monero-project/monero/pull/3985

Whatever code is doing this is adding the pubkey twice, fingerprinting it in the process.

## stoffu | 2018-06-11T11:41:40+00:00
@moneroexamples Oh, I noticed just now that some of these txes have additional tx keys, which I find strange because those txes have only two outputs (destination & change), so additional tx keys shouldn't be necessary. What exactly did you do to create these txes?

## moneromooo-monero | 2018-06-11T12:29:51+00:00
#3985 was off, fixed now. <s>Building on master now to double check as I tested on my work branch where the wallet code has a lot of changes in that area.</s> checked.

## moneroexamples | 2018-06-11T22:38:04+00:00
@moneromooo-monero 

Oh, havn't noticed extra tx keys. thanks. So this must be bug in open monero then. 

edit. Just found it. It was open monero adding second key. Already fixed.

Thanks again.

# Action History
- Created by: moneroexamples | 2018-06-11T06:04:05+00:00
- Closed at: 2018-06-11T23:02:22+00:00
