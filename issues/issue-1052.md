---
title: Simplewallet problem with send
source_url: https://github.com/monero-project/monero/issues/1052
author: AJIekceu4
assignees: []
labels: []
created_at: '2016-09-05T08:51:21+00:00'
updated_at: '2022-04-08T11:29:12+00:00'
type: issue
status: closed
closed_at: '2022-04-08T11:29:03+00:00'
---

# Original Description
Hello all. Old wallet (which used long time for mining). Ubuntu 16.
Monero 'Hydrogen Helix' (v0.9.4.0-04906e6) simplewallet and bitmonero.

> Starting refresh...
> Refresh done, blocks received: 25
> Balance: 634.329756129527, unlocked balance: 634.329756129527
> Background refresh thread started
> [wallet 44bBla]: refresh
> Starting refresh...
> Refresh done, blocks received: 0
> Balance: 634.329756129527, unlocked balance: 634.329756129527
> [wallet 44bBla]: transfer 4 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A 10
> Error: failed to find a suitable way to split transactions
> [wallet 44bBla]: sweep_unmixable
> Error: No unmixable outputs found
> [wallet 44bBla]: sweep_all 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A
> Error: internal error: Duplicate indices though we did not ask for any
> [wallet 44bBla]: rescan_spent
> [wallet 44bBla]: transfer 4 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A 10
> Error: failed to find a suitable way to split transactions
> [wallet 44bBla]: transfer_original 4 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A 10

After last command (transfer_original) nothing happens (wait > 8 hours) and simplewallet stuck, "exit" not work, ctrl+c not work, ctrl+z not work, only kill command.

rescan_bc also did not help.

This wallet, but using old version of simplewallet and bitmonero
Monero 'Hydrogen Helix' (v0.9.4.0-unknown) (code from 06.04.2016):

> [wallet 44bBla]: refresh
> Starting refresh...
> Refresh done, blocks received: 0
> Balance: 634.329756129527, unlocked balance: 634.329756129527
> [wallet 44bBla]: transfer 4 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A 10
> Error: not enough money to transfer, available only 0.260000000000, transaction amount 10.000000000000 = 10.000000000000 + 0.000000000000 (fee)
> [wallet 44bBla]: sweep_unmixable
> Error: No unmixable outputs found
> [wallet 44bBla]: rescan_spent
> [wallet 44bBla]: transfer 4 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A 10
> Error: not enough money to transfer, available only 0.260000000000, transaction amount 10.000000000000 = 10.000000000000 + 0.000000000000 (fee)
> [wallet 44bBla]: transfer_new 4 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A 10
> Error: failed to find a suitable way to split transactions

rescan_bc also did not help.


# Discussion History
## AJIekceu4 | 2016-09-05T13:46:42+00:00
I am compile latest version from github, sync blockchain from network and problem exist:
Monero 'Hydrogen Helix' (v0.9.4.0-afe3cce)

> transfer 4 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A 10
> Error: failed to find a suitable way to split transactions

Log from monerod :
https://paste.fedoraproject.org/422289/82861147/raw/


## ghost | 2016-10-06T01:50:14+00:00
@AJIekceu4 Could you try with version 0.10 and feed back?


## AJIekceu4 | 2016-10-06T04:44:25+00:00
Version from today (wallet and monerod):
Monero 'Wolfram Warptangent' (v0.10.0.0-80c5de9)

> transfer 4 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A 10
> No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No)y
> Error: failed to find a suitable way to split transactions
> sweep_unmixable
> Sweeping 56.090000000000 for a total fee of 0.010000000000.  Is this okay?  (Y/Yes/N/No)y
> Error: transaction <5e3bc9441c2ccd6b14b974a1bae14979ef39883b88eb10b4b78c18e8e14a8a02> was rejected by daemon with status: Failed
> Error: Reason: mixin too low
> sweep_all 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A
> No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No)y
> Error: not enough outputs for specified mixin_count = 4:
> output amount = 14.110000000000, found outputs to mix = 3
> output amount = 14.010000000000, found outputs to mix = 3
> output amount = 14.020000000000, found outputs to mix = 4
> output amount = 13.950000000000, found outputs to mix = 3
> transfer_original 4 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A 10
> No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No)y

After last command (transfer_original) nothing happens  and simplewallet stuck, "exit" not work, ctrl+c not work, ctrl+z not work, only kill command.


## AJIekceu4 | 2016-10-30T09:54:11+00:00
Find the way to send this blocked amount (version from today - 30.10.2016):

> sweep_unmixable
> Error: No unmixable outputs found
> 
> sweep_all BlaBlaBlaWallet
> No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No)y
> Error: not enough outputs for specified mixin_count = 4:
> output amount = 14.010000000000, found outputs to mix = 3
> output amount = 14.110000000000, found outputs to mix = 3
> output amount = 13.950000000000, found outputs to mix = 3
> output amount = 14.020000000000, found outputs to mix = 4

But if i use mixin = 2, all ok:

> sweep_all 2 BlaBlaBlaWallet
> No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No)y

Waiting about 1 hour and after this:

> Sweeping 634.329756129527 in 280 transactions for a total fee of 27.376000000000.  Is this okay?  (Y/Yes/N/No)y
> Money successfully sent, transaction...
> ...280 blablabla


## selsta | 2022-04-08T11:29:03+00:00
Closing for inactivity. If you continue to have this issue in the latest version please comment here and I can reopen.

# Action History
- Created by: AJIekceu4 | 2016-09-05T08:51:21+00:00
- Closed at: 2022-04-08T11:29:03+00:00
