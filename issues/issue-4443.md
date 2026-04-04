---
title: 'Discussion: Multiple transactions for FCMP++ "sweep all" transfers'
source_url: https://github.com/monero-project/monero-gui/issues/4443
author: jeffro256
assignees: []
labels: []
created_at: '2025-05-06T20:40:18+00:00'
updated_at: '2025-05-11T14:19:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The FCMP++ upgrade is likely to put a hard limit on the number of inputs at 8: https://gist.github.com/kayabaNerve/dbbadf1f2b0f4e04732fc5ac559745b7 and https://gist.github.com/Rucknium/784b243d75184333144a92b3258788f6. Because of this, one issue will likely crop up pretty often: sweep all transactions will run out of inputs. If the user owns more than 8 unspent enotes, then attempting to send a transaction with amount=all will cause an exception.

There's a few potential solutions:
    A) Break up the sweep all transaction into multiple transactions automatically
    B) Break up the sweep all transaction into multiple transactions with user confirmation
    C) Tell the user to consolidate funds manually first


Which one should the GUI go with for this scenario?

# Discussion History
## nahuhh | 2025-05-09T15:32:28+00:00

D) Increase limit to tx size limit 


this isnt only an issue for sweeps, but for everyday usage.

> A) Break up the sweep all transaction into multiple transactions automatically

This results in 
1. multiple received tx on the other end
2. seemingly 0 net computational benefit vs sending them all in a single tx
3. Larger blockchain storage

> B) Break up the sweep all transaction into multiple transactions with user confirmation

same as A but with worse UX

> C) Tell the user to consolidate funds manually first

1. lol.
2. User with 2000 outputs needs to (manually) make multiple transactions
3. services need to be psychic to know how many outputs they need, or wait 20+minutes to create more.

..
all 3 of these options would appear to (frequently) break atomic swaps, employer payouts, spend proofs, bill payments, casual shopping ... lol


under (D), you'd still have to deal with the tx limit (100kb).
transfer vs transfer_split. Most wallets use transfer_split for sweep_all transactions. Feather explicitly uses transfer (will not split into multiple transactions).

For 64 input vs 8*8 input, is there
a) a computational pro or con
b) a storage / bandwidth pro or con

## ComputeryPony | 2025-05-11T01:37:51+00:00
nahuhh may be right about increasing the tx limit (and I don't know anything about the right number it should be so I'll stay out of it)

However, even with 64 inputs possible, eventually a user will encounter a situation where they will hit the tx input/size limit even for non-sweep all transactions.
I would vote for a variation of C but have the wallet it do it automatically with user confirmation when the user tries to send a tx that hits the limit.
It's possible that it could take several consolidations if the user has lots of tiny outputs (thinking of p2pool) and it would be painful to try to explain to someone they need to go and do consolidations with precise numbers of inputs to make things work again.

How about having the wallet inform the user that consolidation will be needed to send this transaction and it will take an estimated X number of transactions to consolidate, user confirms and enters their password once, then the wallet repeatedly preforms consolidations and waits for outputs to unlock until it has the needed amount for the transfer, then re-prompt the user that the transfer is ready and have a separate yes/no for this final send decision.

This does require that the spend key be decrypted and kept available the whole time the consolidating process is running but it prevents the user from being nagged about having send a bunch of txs with ~20 minutes in-between each.

As for the final confirmation not being automatic it feels more natural to have this feel like separate steps to the user. A consolidation step they agreed to, and then a transfer they agree to, on top of that fees could have changed for the final sending tx which wouldn't be possible to know until the wallet is done consolidating.

There is an annoying issue when having this done automatically in that tx fees might change between consolidating txs (or a malicious node tricks the wallet into thinking they are) and the wallet would need to stop the consolidation if the fee became "too high". A reasonable default for "too high" would need to be decided upon.

There are other corner cases that would need to be ironed out as well:
&emsp;&emsp;If the user is trying to "send all" to a different wallet and consolidation is needed then the final amount possible to send isn't known until the end.
&emsp;&emsp;If the user is trying to send an amount just below their total balance then tx fees during consolidation might eat up enough of the balance to make the original transaction impossible. How do we explain that to the user and do we warn them ahead of time if the numbers are close enough?
&emsp;&emsp;Anything else I'm not thinking of?


On the up side:
&emsp;&emsp;The user has this situation handled for them. A situation they didn't do anything to create, all they did was receive so they aren't "at fault" for causing this, so making them jump through hoops to fix it feels wrong.
&emsp;&emsp;The final tx still stays "atomic" and either sends the amount or doesn't
&emsp;&emsp; If the consolidation process is stopped in the middle (crash, user closes wallet, etc...) then all they did was self-sends and the wallet would recover naturally when re-opened without any special handling.
&emsp;&emsp;Having this be in the wallet code rather than just the GUI means CLI users also benefit and have it "just work" for them too.


I'm actually unaware of what the wallet does currently when it hits the limit. Does it just fail the transaction? Does it tell the user to do consolidations themselves?

EDIT: To be clear, I'm talking about interactive wallets like the CLI, GUI, and Feather. I know this wouldn't work well for non-interactive wallets like nahuhh mentioned.

## nahuhh | 2025-05-11T14:12:45+00:00
Also need to think about 
"i'm at the store and i'm spending $500. Most of my inputs are $20 or less"

or

"i sell hot dogs and charge $3 per hot dog. My rent is $3000/month. I have to consolidate 1000 inputs. What exactly is the benefit of spamming 125 8input txs instead of 15 64input txs?"

all of these proposed solutions assume that everyone spends from their desktop and can wait 20+ minutes for an unexpected consolidation. 

8 inputs is freakishly low. Outputs can be low, because, realistically, when does a buyer ever send a transfer to multiple recipients at once?
exchanges, employers, mining pools etc would benefit from multi-output, but spending monero does not.

multiple input is not even close to the same argument as outout. Input limits put huge hurdles on your ability to use monero.
unless there is an actual, notable, computational benefit to prefer 8 8in txs over 1 64in, i dont see any reason to limit this aside from a, imo, poor or misguided design preference 

# Action History
- Created by: jeffro256 | 2025-05-06T20:40:18+00:00
