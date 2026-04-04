---
title: Proposal for Carrot Transaction Format Changes
source_url: https://github.com/monero-project/monero/issues/9566
author: jeffro256
assignees: []
labels:
- important
- proposal
- discussion
created_at: '2024-11-12T06:26:07+00:00'
updated_at: '2024-12-08T23:48:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Carrot will require either a change to the hard format of `cryptonote::transaction_prefix` or a change to `extra` field handling.

### What transaction data Carrot needs

#### Per transaction output

| Name | Symbol | Byte Size |  Same storage as v16 |
|---------|------------|--------------|-------------------------------|
| Output pubkey | <code>K<sub>o</sub></code> | 32 | Yes |
| Amount commitment | <code>C<sub>a</sub></code> | 32 | Yes |
| Encrypted amount | <code>a<sub>enc</sub></code> | 8 |  Yes |
| Encrypted Janus anchor | <code>anchor<sub>enc</sub></code> | 16 | No |
| View tag                | `vt` | 3 | No |

Note that Carrot expands the per-output size of enotes by 18 bytes from 73 to 91. 

#### Enote ephemeral pubkeys

Carrot transactions, like the previous addressing protocol, needs "enote ephemeral pubkeys" AKA "additional transaction pubkeys" to act as bases for the ECDH sender-receiver secret. There is one enote ephemeral pubkey <code>D<sub>e</sub></code> per transaction output, except in non-coinbase 2-output transactions, where there is only one total. This is more or less the same as before, as the wallet construction/scanning code already did the 1-transfer-1-change transaction pubkey optimization. 

### How we could store this data 

The most straight-forward way to store the per-output data would be to add the non-amount stuff to a struct like so:
```
struct txout_to_carrot_key
{
    crypto::public_key key;
    carrot::janus_anchor_t janus_anchor;
    carrot::view_tag_t view_tag;
};
```

And then add it to the `txout_target_v` variant, just like how the v15 view tag update did it. We would keep the amount commitments in `outPk` and encrypted amounts in `ecdhInfo`, just like they currently are. That way, both coinbase and non-coinbase transactions' output targets would be `txout_to_carrot_key`, just like how it is now with `txout_to_tagged_key`. 

As for the enote ephemeral pubkeys, there's two main possible pathways we could take: A) put it in `extra` like how transaction pubkeys are done now, or B) hardcode it into the transaction format. Option A has much easier integration. Option B will be able to save one byte per transaction by skipping the size, since the number of enote ephemeral pubkeys is a direct function of the number of outputs and whether or not the transaction is coinbase. I vote option A since FCMP++/Carrot will add a lot of changes to the format already without new premature optimizations. 

# Discussion History
## rbrunner7 | 2024-12-08T15:38:12+00:00
Maybe I am late because you already coded most of this anyway, but never mind:

I don't understand the last sentence:

> I vote option A since FCMP++/Carrot will add a lot of changes to the format already without new premature optimizations.

What do you mean here with "premature optimizations"?

Your vote for A), i.e. continue with using `tx_extra`, surprises me a bit. For me, using `tx_extra` for totally normal, fundamental transaction data always looked like kind of a hack. If the transaction needs it, can't work without it, it's not "extra". Thus unless I overlook something, maybe something you allude to in the sentence I don't understand, I would probably vote B).

## jeffro256 | 2024-12-08T23:48:07+00:00
> If the transaction needs it, can't work without it, it's not "extra".

It depends on how you define "can't work without it". The consensus code only cares about output pubkeys and amount commitments, so that input, balance, and range proofs can be satisfied. It doesn't care about view tags, anchors, ephemeral pubkeys, encrypted amounts, etc being in the transaction. All of the other stuff necessary to Carrot is just as "extra" as ordinals to the consensus code. The view tags, encrypted amounts, etc could be transmitted off-chain, and transaction sending would work exactly the same. The only reason we put it in the transaction is for data availability.

# Action History
- Created by: jeffro256 | 2024-11-12T06:26:07+00:00
