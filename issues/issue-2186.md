---
title: '[TREZOR] No plausible deniability with passphrase on Monero GUI'
source_url: https://github.com/monero-project/monero-gui/issues/2186
author: rating89us
assignees: []
labels:
- invalid
created_at: '2019-05-30T14:58:39+00:00'
updated_at: '2019-09-01T01:27:31+00:00'
type: issue
status: closed
closed_at: '2019-09-01T01:27:31+00:00'
---

# Original Description
In Trezor's web wallet (not Monero wallet), you enter a passphrase (empty, "b", or "c", and then the corresponding wallet is displayed (Wallet "A", Wallet "B", Wallet "C"). So if you are in a situation where you are physically threatened by a criminal, you can now safely give up your PIN number (which can be changed anyway). If the criminal demand a passphrase, you can give out the one with the lesser amount.

According to Trezor's [blog](https://blog.trezor.io/passphrase-the-ultimate-protection-for-your-accounts-3a311990925b): 
> The second and arguably even more important addition brought to the table [by passphrase] is plausible deniability. There is no such thing as an “incorrect passphrase” and you can create an unlimited number of wallets. This can be quickly turned to your benefit when you decide to redistribute your balances to give you a “cover”.

In Monero GUI, it is different, instead of asking for any passphrase (with passphrases a, b, c,... opening Wallets A, B, C, ...), it first opens Wallet A, and then requests the specific passphrase for wallet A. This happens because when I open my Monero GUI, it will automatically open a previously created monero wallet (.dat file) that contains the exported private view key that was exported from Trezor. This private view key corresponds to a single wallet (for instance, Wallet "A").

The problem is that when I type a "false" passphrase in Monero GUI, it displays: 
```
Couldn't open wallet: Device wallet does not match wallet address.
Device address: 4....
Wallet address: 4...
```
I'm not sure what is the best solution here. But I believe there should be a way for user to enter a second passphrase, without the wallet displaying an error message. Maybe instead of displaying this error message, it could create a new wallet from device, using this "false" passphrase.

@ph4r05 

# Discussion History
## selsta | 2019-05-30T15:04:10+00:00
I think this feature won’t be possible.

## rating89us | 2019-05-30T15:13:38+00:00
I didn't try it yet, but I believe that one way to have plausible deniability is to create multiple Monero wallets with different passphrases, transfer some funds to these wallets, and then disable passphrase function on Trezor device, and delete the .dat files of wallets using passphrases. 

## selsta | 2019-05-30T15:15:40+00:00
If I’m not missing something, deleting the wallet file is enough for plausible deniability.

## ph4r05 | 2019-05-30T15:19:31+00:00
Workaround for plausible deniability is to delete all wallet files after usage. Just restore the wallet from the device next time you need it.

However, in this case you lose tx private keys (for tx proofs). So it might be beneficial to backup those after you submit a transaction.

Another workaround: store wallet files on an encrypted hidden disk. When forced, unlock decoy disk (plausible deniability) and use decoy wallet files and decoy passphrase. Or recover wallet with fake passphrase. 

If you have wallet files on your disk I cannot think of any cryptographically secure mechanism to work with the passphrase plausible deniability right now. GUI/CLI implementation would be just superficial. IMO It would be a ton of work in order to make wallet work properly in the fake passphrase scenario.


## rating89us | 2019-05-30T15:25:00+00:00
Monero GUI could save all tx private keys in a separate file and delete all .dat files every time it is closed.
So every time you want to use your Trezor on GUI, it would be as if it was the first time (create wallet from device).

## ph4r05 | 2019-05-30T15:33:05+00:00
It would need a bit more thinking. I think a lot of users prefer usability and practicality instead of plausible deniability (which can be achieved either way by proposed workarounds). 

Recovering a wallet with each GUI opening is a pain as you have to scan the blockchain for incoming payments. IMO this cannot be a default setting.  

> Monero GUI could save all tx private keys in a separate file and delete all .dat files every time it is closed.

We could add tx info import/export as it could be a generaly-usable feature. In the CLI there might be an extra command, GUI could do it on demand (button) or automatically after each transaction (if the checkbox is enabled). 

There are still a lot of UX questions and use-cases to be thought of... (not an easy thing to implement, may be difficult to maintain -> high cost.)

## selsta | 2019-09-01T01:27:01+00:00
This would be better suited for the monero repo. (https://github.com/monero-project/monero/issues/). Also this feature would require large changes that I think are unlikely to get implemented.

+invalid

# Action History
- Created by: rating89us | 2019-05-30T14:58:39+00:00
- Closed at: 2019-09-01T01:27:31+00:00
