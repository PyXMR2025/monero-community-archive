---
title: Allow multisig txs to be created without exchanging multisig info
source_url: https://github.com/monero-project/monero/issues/8230
author: woodser
assignees: []
labels: []
created_at: '2022-03-29T15:16:43+00:00'
updated_at: '2022-03-29T15:58:05+00:00'
type: issue
status: closed
closed_at: '2022-03-29T15:58:05+00:00'
---

# Original Description
This issue requests the ability to create multisig txs without exchanging multisig info.

Currently, multisig participants must exchange multisig info before the wallet can create multisig txs. As a result, participants must complete a full round trip before a multisig tx can be signed and broadcast. This is problematic if participants go offline, as each signer must return online before the tx can be signed and broadcast.

Instead, according to @moneromooo-monero, the multisig info "could plausibly piggy back on the multisig tx itself, similarly to the output and key image info piggybacking onto cold signing data".

That would allow the multisig tx to be created without first exchanging info, and then the co-signer can update their wallet from the piggybacked info, sign, and broadcast the tx directly.

# Discussion History
## UkoeHB | 2022-03-29T15:42:51+00:00
The need for 2 round trips is an unavoidable part of multisig signing. All multisig signing algorithms have these two rounds: 1) collect nonces from all signers, 2) collect partial signatures from all signers (each signer must know the set of signer nonces), (then 3) combine partial signatures into a complete signature).

Monero's pattern is 1) each signer calls `export_multisig()` to send nonces to other signers, 2) someone who wants to make a tx calls `import_multisig()` to collect those nonces then build a tx with `transfer_selected_rct()` which is sent to other signers, 3) each signer calls `sign_multisig_tx()` to add their partial signature in a round-robin style (signing is serial - one partial signature has to use the output of another signer's `sign_multisig_tx()`), 4) the last signer completes the tx and submits it (or sends to other signers? I don't recall exactly). Step 2 requires a nearly complete tx, including all ring members, so it can't be done unless a tx is in the ledger (probably needs to be confirmed or `wallet2` will throw an error).

In Seraphis the pattern will be 1) tx proposer sends tx proposal + his own nonces to other signers, 2) other signers send their own nonces to each other, 3) each signer makes partial signatures as soon as they have enough nonces, 4) assemble final tx and submit. With Seraphis, step 1 can be done with txs that aren't even in the ledger (via tx chaining - ring sigs/membership proofs are made in step 4), and step 3 is parallel not serial.

## woodser | 2022-03-29T15:56:25+00:00
> With Seraphis, step 1 can be done with txs that aren't even in the ledger

If I understand correctly, this means the updated multisig info could be generated for 0 confirmation funds. That would solve our use case since peers are online when funds are first deposited to multisig, so a round trip isn't necessary after they potentially disconnect.

# Action History
- Created by: woodser | 2022-03-29T15:16:43+00:00
- Closed at: 2022-03-29T15:58:05+00:00
