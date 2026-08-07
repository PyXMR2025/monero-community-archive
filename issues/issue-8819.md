---
title: Improve transaction proof documentation
source_url: https://github.com/monero-project/monero/issues/8819
author: UkoeHB
assignees: []
labels:
- enhancement
- documentation
created_at: '2023-04-05T21:01:35+00:00'
updated_at: '2026-08-04T19:13:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Credit for this issue goes to the Cremers, Loss, Wagner team behind [this paper](https://eprint.iacr.org/2023/321).

Transaction proofs (`check_tx_key()`, `InProofs/OutProofs`) do not guarantee that funds associated with a proof are spendable. They could be permanently time locked, already spent, or burnt due to duplication of onetime addresses. The documentation around those proofs should be clarified:

- in the CLI commands
- in the CLI [documentation](https://www.getmonero.org/resources/user-guides/monero-wallet-cli.html)
- in the [Monero.how](https://www.monero.how/tutorial-how-to-prove-payment) website
- wherever else they are documented...

It is also worth noting that a user who receives burnt funds may not be adequately notified/aware of it, since the wallet currently hides that information to a large extent.

Other recommendations:
 - Add clearer UI in the (commandline/giu)wallet for these transactions. In our tests, this case looked extremely hidden. The amount magically is reduced, but the transaction(s) exists. Errors are logged but a normal user will have no clue as to what happened and why there might be a discrepancy between the amount in the proof and the amount visible in their wallet.
 - Add documentation on how to better check proof-of-payments for spendability, or suggest (or enforce!) to only use them on subaddresses.


# Discussion History
## HardenedSteel | 2026-08-04T19:05:27+00:00
1. Do we mean time locked for very long time are burnt coins?
2. Already spent; double spending attempt or spent after receiving the coins? Because why a transaction proof would prove the coins are spendable. As the name suggests its proof of transaction.
3. ~~burnt due to duplication of onetime addresses; how this is possible? do we mean an address with lost private keys?~~

# Action History
- Created by: UkoeHB | 2023-04-05T21:01:35+00:00
