---
title: payment_id will be not accepted via RPC
source_url: https://github.com/monero-project/monero/issues/61
author: Atrides
assignees: []
labels: []
created_at: '2014-07-15T15:34:07+00:00'
updated_at: '2014-07-17T23:55:23+00:00'
type: issue
status: closed
closed_at: '2014-07-17T23:55:23+00:00'
---

# Original Description
I'm wondering abour an error with Simplewallet, payment_id and JSON_RPC.

I tried to use it with payment_id, but TX will be sent without it:

```
{"jsonrpc":"2.0","method":"transfer","params": {"destinations":[ {"amount": 500000000000, "address": "48MTY4jFEoJefp1upERPYx2LaLDZ4TCRUYFNErH5BTuHbe4b5NAvvKV9Zx9x9Ry5Y2fwxx9uzc5snifhiHu5Cx29LTCeaQi"} ], "payment_id":"eab654f4ce4e75bba34705fa0a92d4d04e728c5fa55b937288afdd84287f08e0","fee":5000000000,"mixin":0,"unlock_time":0}
 }

{u'jsonrpc': u'2.0', u'id': 0, u'result': {u'tx_hash': u'<f79b70c8fbc56598869d57fc3229d05f0b38057b46f68fc08e7864181bd55ba7>'}}
```

If I transfer direct in console, it works fine.

```
transfer 0 48MTY4jFEoJefp1upERPYx2LaLDZ4TCRUYFNErH5BTuHbe4b5NAvvKV9Zx9x9Ry5Y2fwxx9uzc5snifhiHu5Cx29LTCeaQi 0.5 eab654f4ce4e75bba34705fa0a92d4d04e728c5fa55b937288afdd84287f08e0

Money successfully sent, transaction <9a3c98f7701064fc04118c98fb7ff37587bc6ff54cdb5afb125ad4cd3e05b6bd>
```

We can check in block explorer that the second transaction has payment_id, the first one - not


# Discussion History
## Jojatekok | 2014-07-15T16:41:52+00:00
The call you have written above looks totally correct, and it works like the same as in [my GUI wallet](https://bitcointalk.org/index.php?topic=683365).


## monero-project | 2014-07-15T17:24:50+00:00
There is a bug in RPCwallet in the one test branch
https://github.com/tewinget/bitmonero/pull/4

Is this what you're experiencing?


## tewinget | 2014-07-15T17:45:42+00:00
I just merged a change from mikezackles that I believe might fix this bug.
 Can someone verify?

On Tue, Jul 15, 2014 at 1:24 PM, monero-project notifications@github.com
wrote:

> There is a bug in RPCwallet in the one test branch
> tewinget#4 https://github.com/tewinget/bitmonero/pull/4
> 
> Is this what you're experiencing?
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/monero-project/bitmonero/issues/61#issuecomment-49064947
> .

## 

Thomas Winget
Computer Engineering
Purdue University '12


## Atrides | 2014-07-17T12:21:11+00:00
I have tested this patch and now works fine over RPC!

```
{"destinations":[ {"amount": 777000000000, "address": "48MTY4jFEoJefp1upERPYx2LaLDZ4TCRUYFNErH5BTuHbe4b5NAvvKV9Zx9x9Ry5Y2fwxx9uzc5snifhiHu5Cx29LTCeaQi"} ], "payment_id":"aaaaaaf4ce4e75bba34705fa0a92d4d04e728c5fa55b937288afdd84287f08e0","fee":5000000000,"mixin":0,"unlock_time":0}
```

TX 982a6d91e0aac71440e2c4c72169bcfe8016fe2ff48c89e5e3cc444a08180b4d


## tewinget | 2014-07-17T18:25:56+00:00
awesome!

On Thu, Jul 17, 2014 at 8:21 AM, Atrides notifications@github.com wrote:

> I have tested this patch and now works fine over RPC!
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/monero-project/bitmonero/issues/61#issuecomment-49299368
> .

## 

Thomas Winget
Computer Engineering
Purdue University '12


# Action History
- Created by: Atrides | 2014-07-15T15:34:07+00:00
- Closed at: 2014-07-17T23:55:23+00:00
