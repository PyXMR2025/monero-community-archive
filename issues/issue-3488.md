---
title: 'Feature request: integrate security key/YubiKey support'
source_url: https://github.com/monero-project/monero-gui/issues/3488
author: rating89us
assignees: []
labels: []
created_at: '2021-05-19T02:38:28+00:00'
updated_at: '2021-06-16T10:07:41+00:00'
type: issue
status: closed
closed_at: '2021-06-16T10:07:41+00:00'
---

# Original Description
Currently Monero GUI funds are only protected by the wallet password. If the desktop computer holds a hot wallet and it is compromised by a remote attacker, all balance can easily be stolen.

After linking the wallet file with a stronger authentication device, Monero GUI could ask the user to physically touch or insert a security key USB device when doing critical actions, like sending funds or displaying the mnemonic seed.

# Discussion History
## t-anon | 2021-05-22T00:26:22+00:00
Monero GUI already supports hardware wallets.

You really should avoid using a YubiKey as opposed to a hardware wallet. Namely because:

- PIN entry would be insecure on a YubiKey as it would go need to go through the OS
- If you generate the seed on the YubiKey, it can never leave the YubiKey
- If you don't generate the seed on the YubiKey, you can't really safely load it onto the YubiKey

Hardware wallets (namely the Ledger, due to a secure element) have a much better security model than a YubiKey because they have their own airgapped input methods for PIN and seed entry.

So you are effectively asking for something less secure than a hardware wallet but more secure than a software wallet, which, well... kind of niche. Just buy a hardware wallet.

## rating89us | 2021-05-23T19:09:30+00:00
- A wallet file linked to the YubiKey means that every time you copy this wallet file into any monero wallet, this wallet must require authentication on YubiKey in order to confirm risky actions: confirm sending transactions and displaying its seed.
- The YubiKey will not store the seed, it will be stored in the wallet file. User will still have to write down the seed on a paper backup.
- Supporting YubiKey would enable users to carry higher amounts on their hot (connected on the internet) Monero GUI wallets on desktop (or mobile, when available).
- For example, you could generate a wallet file linked to YubiKey on a air gapped computer and then copy your wallet file into your Monero GUI on desktop. Now you have a wallet file in Monero GUI that will never send transactions and displays its seed, unless you authenticate with YubiKey.
- Also, YubiKey is cheaper than a hardware wallet, is multipurpose (more privacy), and is easier to carry.

## selsta | 2021-05-24T03:38:38+00:00
> this wallet must require authentication on YubiKey in order to confirm risky actions: confirm sending transactions and displaying its seed.

This would only be a visual action, a custom GUI could patch these confirmations out. This isn't possible with a real hardware wallet.

Malware on your computer could still steal your seed once you open a wallet with a YubiKey, it would barely improve your security compared to a regular password.

## rating89us | 2021-05-24T10:12:26+00:00
> This would only be a visual action, a custom GUI could patch these confirmations out. This isn't possible with a real hardware wallet.

My idea would require a special type of Monero wallet file. The wallet file itself should require the YubiKey to unlock it, just like a password works today. Therefore it doesn't matter in which wallet software you import this wallet file, you will not be able to open this wallet file without its "physical password". 

> Malware on your computer could still steal your seed once you open a wallet with a YubiKey, it would barely improve your security compared to a regular password.

When a wallet software has opened and unlocked a YubiKey wallet file, it should not have the "display seed" options enabled. I'm not sure if the seed can be stolen by analyzing memory, etc.

## t-anon | 2021-06-09T01:55:37+00:00
The point is that for the use case that must be solved (a compromised client - malware on your computer), YubiKeys fail miserably.

It doesn't matter if the wallet software can't access your seed. Malware will just re-write the address you intend to send money to "behind the scenes."  As soon as you try to use the wallet to send money to someone, the malware will hook into the Monero client and change the recipient address while letting the "correct" address stay displayed on the GUI. Then, when you touch your YubiKey, you'll be signing a transaction for the wrong address, while thinking you signed a transaction for the correct one.

This is known as a "confused deputy attack" and it is the main issue with YubiKeys today. YubiKeys cannot really mitigate a compromised client - at which point you may as well just use a software wallet. It is why hardware wallets have displays, and it's why the wallet display shows the recipient address. 

## rating89us | 2021-06-16T10:07:41+00:00
Thanks for your explanations, it seems that YubiKey is not really useful for Monero GUI.

# Action History
- Created by: rating89us | 2021-05-19T02:38:28+00:00
- Closed at: 2021-06-16T10:07:41+00:00
