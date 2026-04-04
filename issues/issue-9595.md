---
title: 'Multisig 2/3 does not work. Failed to perform multisig keys exchange: Failed
  to derive public key'
source_url: https://github.com/monero-project/monero/issues/9595
author: ghost
assignees: []
labels:
- wallet
created_at: '2024-11-28T15:11:36+00:00'
updated_at: '2025-03-18T01:03:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
// EDIT
If you want to recreate issue, try creating 2/3 multisig wallet via cli, you will not be able to complete second key exchange for all users. Bug is difficult.
// EDIT

This happen every time I do second round of exchange_multisig_keys for 2/3. Every time i do it perfectly like documentation, passing in correct order.

I do prepare_multisig.
I do  make_multisig [info1, info2], make_multisig [info1, info3] etc like they do in docs.
i do "exchange_multisig_keys info1 info2" etc with info from last command.

then i do "exchange_multisig_keys info1 info3" etc with info from last command.

 It works with first wallet that does the command, so long as wallet hasnt been closed after first exchange, else it fails like the others. All respond with : Failed to perform multisig keys exchange: Failed to derive public key

# Discussion History
## ghost | 2024-11-28T22:03:46+00:00
Could this be because im doing these back-to-back-to-back?? I perform the make_multisig for the 3rd wallet, then immediately proceed to exchange_multisig_keys, without closing the wallet or refreshing it. Is a timeout required? I will keep testing. 2/2 work fine.

## ghost | 2024-12-03T09:51:48+00:00
Big progress in indentifying bug, but still no solution.

Outline:
Funcitonal tests pass I assume, or monero would not release.
Therefore, creating 2/3 multisig work as per tests.
These tests are RPC, not CLI.

Issue:
Impossible to create 2/3 multisig wallet using CLI, even when matching logic of passing test perfectly, or following the recommend procedure in the documentation.
Always result in "Failed to derive public key" for exchange_multisig_keys

Possible solution:
2/3 Multisig creation only work in RPC. will test and confirm.


## ghost | 2024-12-03T11:10:32+00:00
Im wondering if bug is from using the same RPC, where in testing using a different RPC for each wallet. 

As it is multisig 2/3 does not work start to finish using single RPC, or CLI using single RPC. Very unfortunate.

## nahuhh | 2025-03-18T01:03:58+00:00
resolved on irc

# Action History
- Created by: ghost | 2024-11-28T15:11:36+00:00
