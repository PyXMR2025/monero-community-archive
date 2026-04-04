---
title: 'Multisig: N-of-N Fast Setup'
source_url: https://github.com/monero-project/monero/issues/8757
author: LocalMonero
assignees: []
labels:
- feature
- proposal
created_at: '2023-03-03T02:00:22+00:00'
updated_at: '2023-12-07T21:22:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently, N/N multisig wallets are required to complete the post-KEx round just as M/N wallets are (at least in the CLI wallet).

As per @UkoeHB, under M/N without the post-KEx round the most that can happen is there isn't a full set of N honest participants with completed multisig accounts, so funds sent to your local completed account are effectively inaccessible.

with N-of-N it's less of a concern since there is no 'subset of honest users'.  All @UkoeHB could think of was the post-KEx round could act as a heartbeat test on the other party in a 2-of-2 if you obtained a potentially very old pubkey from them.

Allow N/N Multisig wallets to be finalized without the post-KEx round.

# Discussion History
## UkoeHB | 2023-03-03T02:12:18+00:00
The best way to implement this would be a wallet2 method `multisig_nofn_fast_noninteractive_setup()` that internally force-updates the post-kex round after the initial kex round.

The multisig implementation itself should not change, because all default account setup ceremonies should have the same security properties. One property relevant to N-of-N that the post-kex round provides is ensuring that ceremonies are *interactive*. This way you cannot go through an entire setup ceremony without interacting with the other group members, which could lead to unintended consequences if other group members are dead/unavailable.

# Action History
- Created by: LocalMonero | 2023-03-03T02:00:22+00:00
