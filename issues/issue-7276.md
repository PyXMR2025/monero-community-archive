---
title: Reduce reliance on Ledger for Ledger wallets
source_url: https://github.com/monero-project/monero/issues/7276
author: skorokithakis
assignees: []
labels: []
created_at: '2021-01-04T01:20:15+00:00'
updated_at: '2022-03-04T14:58:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It would be great if Monero could optionally store the view key on the device. My wallet is already protected by a passphrase, and I consider storing the encrypted view key on my computer an acceptable risk. This would make syncing and viewing balances much easier, since it would turn my wallet into basically a read-only softwallet, but still require the Ledger when sending funds.

I think this would be great for usability, since people usually view transactions more than they send funds. Another benefit is that you wouldn't have to have your Ledger open and connected for hours while the client syncs the blockchain, you could instead just connect the Ledger for the few seconds you need to sign a sending transaction and turn it off it afterwards.

# Discussion History
## SamsungGalaxyPlayer | 2021-01-04T16:38:39+00:00
Relevant background reading https://monero.stackexchange.com/questions/10500/why-do-i-have-to-export-the-private-view-key-every-time-i-use-my-ledger

## skorokithakis | 2021-01-04T16:52:12+00:00
@SamsungGalaxyPlayer thanks for that! It would appear that the Ledger is required for more than the key, as I had exported the key and removed the Ledger so the blockchain could download.

However, it turned out that the Ledger was still required (for block verification? I'm not sure, it never asked me for the key again).

Also, related issue: https://github.com/LedgerHQ/app-monero/issues/27

## jonathancross | 2022-03-04T14:58:04+00:00
I agree that caching the private view key in the wallet would be a great option for most users.

Assuming a strong password is used for the wallet, I see no significant downside as compared to having the user _manually_ export the view key every session -- both can be intercepted and stolen by malware on the desktop machine.  If the user has a weak password and malware on the system, then there would be some risk of the wallet file being brute-forced, but for very little gain.

Users who are concerned about these sort of attacks should instead be filtering blocks through the Ledger device itself.

> for block verification? 

No, exporting the private view key allows your computer to "scan blocks looking for transactions".
If the key is not exported, then the Ledger device itself will need to scan blocks.  This is dramatically slower (tiny processor with almost no RAM), but protects the view key from any potential malware running on your computer (a privacy consideration for some Monero users).

This is in contrast to Bitcoin where transactions are already public, so there is no significant loss of privacy if malware steals the view key (aka `xpub`).

# Action History
- Created by: skorokithakis | 2021-01-04T01:20:15+00:00
