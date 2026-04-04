---
title: 'User experience: let users spend low confirmation funds without being locked
  for 10 blocks'
source_url: https://github.com/monero-project/monero/issues/5810
author: woodser
assignees: []
labels: []
created_at: '2019-08-14T21:58:45+00:00'
updated_at: '2021-04-21T17:42:25+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This issue documents the user experience use case of being able to quickly spend funds received to their wallet with low or no confirmations if they choose to accept the added risk of being double spent.

Use case 1: Alice receives funds from her Grandmother and wants to use the funds to pay Bob.  Alice is not worried that her Grandmother will double spend her, so she is comfortable using freshly received funds to pay Bob.  Bob may then choose to accept the risk of the low confirmation funds or not.

Use case 2: Alice wants to send 2 successive payments while out shopping.  The first transaction spends all outputs in Alice's wallet and creates a change output.  The second transaction can use the change output, which is low confirmation but trusted to not be double spent, to complete a second transaction without restriction.

Technical implementation was discussed in IRC, summarized here:

It may technically be possible to remove the 10 block lock, giving users the choice to use low confirmation outputs at an increased risk of being double spent, by referencing outputs by their tx id instead of offsets, and by ordering txs within a block by their tx id.  Then transactions and their referenced outputs would remain valid across re-orgs.  This would require a consensus change and come at some space and bandwidth cost (64 bit int becomes 256 bit hash per output barring any wizardy?) in order to reference tx ids instead of offsets.

It also needs to be investigated if this could harm privacy in other ways.  For example, sarang raised "there is also a risk that ring members may not appear on both chains, leading to an intersection that could reveal the spend".  The extent of additional risk, whether the risk diminishes exponentially with each confirmation, or if the risk is deemed worthwhile by the community needs further investigation.

Comments by moneromooo:

"We discussed this. IIRC smooth was against decreasing from 10 (I assume until good evidence it's safe is found).  Relaying txes with hashes rather than indices was talked about many times, never got done. It just needs someone to do it (well).  The DB will still keep indices. Outputs are typically encoded 16 bits on average.  (maybe 24)"



# Discussion History
## woodser | 2019-08-14T22:00:31+00:00
Related: https://monero.stackexchange.com/questions/4579/is-the-10-block-lock-time-a-protocol-rule-what-rules-accompany-it

## SamsungGalaxyPlayer | 2019-08-17T16:37:25+00:00
10 indeed seems arbitrary, but I would like to see some research before changing it. There will almost certainly be a UX disappointment, since it's unlikely we can set it to require 0 blocks.

## woodser | 2019-08-17T18:20:08+00:00
I think dropping the lock time without making other changes could be dangerous because it exposes users to their transactions being invalidated even if they are not double spent (the vast majority of transactions are not double spend attempts).  That's because transactions today do not remain valid through a re-org.  But if transactions remain valid through a re-org, they are all but guaranteed to confirm unless they are double spent, which is the usual risk inherent in low confirmations.  In that case, there would be no technical reason to have any lock time at all except to enforce double spend protection if it was decided to do that or if it was found to jeopardize privacy.  That's a better long term solution IMO.

## erciccione | 2019-09-08T09:49:51+00:00
related: #5882

## Gingeropolous | 2021-04-20T13:25:35+00:00
for the record, someone suggested on IRC that we could use a hybrid approach, wherein the tx, when in the mempool, is referred to by the 32 byte hash , but once baked into the chain a while, can just be referred to by 8 byte ID. Then if the tx ends up kicked out of the chain due to a re-org, it lives again with the 32 byte hash.

or something like that.

i guess the point is that ultimately the hash can be pruned. 

edited for clarity as suggested

## hyc | 2021-04-20T13:53:40+00:00
Fwiw that sounds workable. Just, for sake of clarity: a txn has a 32 byte `hash` and in the chain it has an 8 byte `ID`. This is the terminology used throughout the codebase. Don't say "hash ID".

# Action History
- Created by: woodser | 2019-08-14T21:58:45+00:00
