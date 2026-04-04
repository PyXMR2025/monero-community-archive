---
title: Provide a more useful error message when trying to query for too many fake
  outs from a restricted RPC
source_url: https://github.com/monero-project/monero/issues/8069
author: sethforprivacy
assignees: []
labels: []
created_at: '2021-11-19T18:04:07+00:00'
updated_at: '2022-03-31T16:25:03+00:00'
type: issue
status: closed
closed_at: '2022-03-31T16:25:03+00:00'
---

# Original Description
This is a follow-up to previous issues:

- https://github.com/monero-project/monero/issues/2855
- https://github.com/monero-project/monero/issues/2028

This issue has become much more frequent and is causing quite a UX headache for those mining using p2pool as attempting to sweep/consolidate a lot of inputs is a frequently necessary task, but fails if using a remote node via restricted RPC.

The current error just says `failed to get random outs`, but gives no clue that an unrestricted RPC or a smaller input count is required to process the transaction properly.

This should likely either be changed in wallet/wallet2, or caught and expanded in the GUI at the very least. Relevant code appears to be here:

https://github.com/monero-project/monero/blob/9bba3f4767c32292cd616512cc492ca416f6adc1/src/wallet/wallet_errors.h
https://github.com/monero-project/monero/blob/19a6cc26fc679f28f104d78add701bd9da26022a/src/wallet/api/wallet.cpp

# Discussion History
## SamsungGalaxyPlayer | 2022-02-28T23:17:19+00:00
Users are seeing this error in Cake Wallet and are becoming very confused. See: https://twitter.com/NateAdamCastle/status/1498435759598145538

## SamsungGalaxyPlayer | 2022-02-28T23:30:29+00:00
The error code should ideally prompt to easily consolidate outputs down.

If the max # of inputs with restricted RPC is, say, 40, then it should make transactions for all non-dust inputs in batches of 40. These should be consolidated to 1, 2, or 16 outputs per transaction. My gut says 2 should be the default.

## CakeWallet | 2022-03-23T13:50:47+00:00
I ran into this issue today trying to spend p2pool funds. I had no idea what to do with this error message, and someone had to point me here. Please improve this error message at the minimum (with an accompanying actionable string) and ideally provide an obvious, automatic path to churn with an appropriate number of inputs. With p2pool becoming common, more people will run into this issue.

## SamsungGalaxyPlayer | 2022-03-29T16:18:38+00:00
Looks like the use-case with p2pool will be addressed when Cake Wallet moves to 0.17.3. We are currently on 0.17.2.3

https://github.com/monero-project/monero/pull/7796

~~This is still a partial fix; this error message may appear if there is a network communication error. Still,~~ someone spending many p2pool outputs should no longer run into this issue.

## SamsungGalaxyPlayer | 2022-03-31T14:00:09+00:00
@sethforprivacy you can close this I think: https://github.com/cake-tech/cake_wallet/pull/311

## sethforprivacy | 2022-03-31T16:25:03+00:00
> @sethforprivacy you can close this I think: [cake-tech/cake_wallet#311](https://github.com/cake-tech/cake_wallet/pull/311)

Perfect!

# Action History
- Created by: sethforprivacy | 2021-11-19T18:04:07+00:00
- Closed at: 2022-03-31T16:25:03+00:00
