---
title: Wallet claims transactions uses an encrypted payment ID
source_url: https://github.com/seraphis-migration/monero/issues/136
author: Greb-i2p
assignees: []
labels: []
created_at: '2025-10-05T16:30:05+00:00'
updated_at: '2025-11-05T00:00:31+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In monero-wallet-cli v0.19.0.0-alpha.1.1-release on the stressnet.
When using sweep_all, the receiver gets the message
`NOTE: this transaction uses an encrypted payment ID: consider using subaddresses instead`

To reproduce use sweep_all, with the target address in another wallet

I also saw this on a output received from the faucet, so probably it can happen from other commands.

# Discussion History
## rbrunner7 | 2025-10-05T16:44:40+00:00
That's a totally harmless info message that has nothing to do with FCMP++, stressnet or similar. We have that in the codebase for years already. I am not even sure it's appropriate; maybe that encrypted payment ID it complains about is just the dummy random value used instead of a true payment ID to make it impossible to see whether a transaction actually uses one.

## jeffro256 | 2025-11-05T00:00:02+00:00
This issue is caused by `simplewallet` trying to decrypt new Carrot encrypted payment IDs in the same manner as pre-Carrot encrpted payment IDs, resulting in a psuedo-random "decrypted" payment ID as if the receiver used an integrated address. This triggers a false positive of the aforementioned warning message. I can come up with a fix soon. 

# Action History
- Created by: Greb-i2p | 2025-10-05T16:30:05+00:00
