---
title: Sweep_all command not finding all inputs on v7
source_url: https://github.com/monero-project/monero/issues/2957
author: ghost
assignees: []
labels: []
created_at: '2017-12-18T18:05:38+00:00'
updated_at: '2018-05-12T00:21:13+00:00'
type: issue
status: closed
closed_at: '2017-12-19T05:22:09+00:00'
---

# Original Description
I typed `sweep_all` on the v7 testnet into my CLI with a balance of 1018 XMR. The sweep_all command only found a single input for 0.01 XMR. I typed `refresh` and my balance was still 1018 XMR. Then I tried `transfer address 1000` and that worked fine. Is sweep_all not finding all the inputs on v7 testnet?

https://paste.fedoraproject.org/paste/EonuDL7TAasOUPui17gpJw

# Discussion History
## stoffu | 2017-12-18T23:35:16+00:00
Do you have funds received in subaddresses? You can see it by `balance detail`. If this is the case, `sweep_all` command spends funds associated with just a single subaddress unless you explicitly specify spending subaddresses' indices like `index=1,2,3`.

## ghost | 2017-12-19T05:22:09+00:00
Yep that’s the issue. 

## farinspace | 2018-05-11T19:37:57+00:00
I don't quite understand "not finding all the inputs" ... but have experienced this problem twice already.

I restored a wallet with only a single inbound transaction. I then tried to move all XMR using `sweep_all [addr]`, at this point the wallet freezes. I have to `kill -9 [pid]` to stop it.

I then do `transfer [addr] [small-amount]` and it works, then I do `sweep_all [remaining-amount]` and then it works.

Not sure if this is related, but wouldn't mind understanding why this happens. thx.

## stoffu | 2018-05-12T00:21:13+00:00
@farinspace 

That behavior is likely a bug. Can you reproduce it?

# Action History
- Created by: ghost | 2017-12-18T18:05:38+00:00
- Closed at: 2017-12-19T05:22:09+00:00
