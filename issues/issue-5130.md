---
title: Multisig tx signing aborts with "Transaction prefix does not match data"
source_url: https://github.com/monero-project/monero/issues/5130
author: rbrunner7
assignees: []
labels: []
created_at: '2019-02-07T19:33:03+00:00'
updated_at: '2019-03-19T14:41:46+00:00'
type: issue
status: closed
closed_at: '2019-03-19T14:41:46+00:00'
---

# Original Description
Signing of multisig transactions (current master HEAD) aborts in `wallet2::sign_multisig_tx` with an error message of "Transaction prefix does not match data", currently output at line 6412.

Reproduce as follows:

* Configure multisig wallets. 2/2 multisig suffices
* Fund the wallet, sync, wait for unlock
* Start a tx in one wallet
* Try to sign it in the other wallet using the CLI wallet command `sign_multisig` -> Error

I and some other fellow MMS tester tried 2/2, 2/3 and 3/3 multisig, on Stagenet and on Testnet: It seems it's always the *second* signature that fails (the first of course happening together with the `transfer` command).

With a litte trial-and-error I found out that with the code at [this commit from January 18](https://github.com/monero-project/monero/commit/b7441c4a328f32cdf33f8e07816bcb080483d4cb) signing still works, but with one more commit included, the [pruning commit from January 22](https://github.com/monero-project/monero/commit/b750fb27b0f20e9443827732b69a504a76036430), it does not work anymore.

Wallet construction seems to be ok: Even with the wallet constructed with latest HEAD code signing works with the pruning PR left out, and stops to work with that included.

# Discussion History
## tmoravec | 2019-02-11T15:16:20+00:00
Can reproduce with 2/2 wallets.

## tmoravec | 2019-02-11T15:55:47+00:00
Logs from the CLI wallet (stagenet): https://paste.debian.net/1066986/

## tmoravec | 2019-02-11T19:42:33+00:00
The tx hash of the transaction obtained from `cryptonote::construct_tx_with_tx_key` is different from what's in `exported_txs`. In both cases, the hash is valid, at least according to `is_hash_valid`.

`tx blob_size: 140734459372256, ptx.tx blob_size: 0` <- Neither of these numbers make sense.

All of prefix hash, blob hash, and prunable hash are different. Blob hash different => inputs/outputs are different.

## naughtyfox | 2019-03-07T12:28:59+00:00
We faced this issue as well. The problem was in dummy encrypted payment id and was already fixed.

## moneromooo-monero | 2019-03-13T17:27:18+00:00
So it's fixed ?

## rbrunner7 | 2019-03-13T21:05:11+00:00
I just tried with latest HEAD: Still does not work for me.

@naughtyfox 's statement also somehow contradicts my own earlier result that it works with the pruning PR left out, but does not work with that PR included. Anyway, as I said, current HEAD (unmodified, with all PRs in) still gives me that `Transaction prefix does not match data` error.

## rbrunner7 | 2019-03-13T21:23:18+00:00
Ah, maybe, @naughtyfox sees a connection between this issue and the issue solved in
PR #5270. Well, wouldn't that be strange, as that PR is about Wallet API?

## moneromooo-monero | 2019-03-13T22:22:43+00:00
OK, I'll test/fix this soonish then.

## naughtyfox | 2019-03-13T22:35:27+00:00
The problem I solved in referenced PR is not about mismatched transaction prefix. This one happens when you use wallet api for non-N/N multisig transactions.

The quickest way to check if it's transaction extra / encrypted payment id problem is to make multisig tx with non-default payment id. If transaction goes well than the problem still persists.

## moneromooo-monero | 2019-03-14T15:47:44+00:00
After all this debugging, I found the bug. And then I realized... I'd seen that change somewhere.

https://github.com/monero-project/monero/pull/5168/files

## rbrunner7 | 2019-03-14T17:03:48+00:00
So ... cherry-pick that to make multisig work again if I want to test, or is there more to it?

## moneromooo-monero | 2019-03-14T17:33:14+00:00
Just that.

## rbrunner7 | 2019-03-14T19:58:59+00:00
Verified: Works.

## moneromooo-monero | 2019-03-19T14:16:37+00:00
+resolved

# Action History
- Created by: rbrunner7 | 2019-02-07T19:33:03+00:00
- Closed at: 2019-03-19T14:41:46+00:00
