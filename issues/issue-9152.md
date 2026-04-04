---
title: 'monero-cli: non-interactive wallet generation'
source_url: https://github.com/monero-project/monero/issues/9152
author: kkarhan
assignees: []
labels:
- wontfix
- low priority
- proposal
- wallet
created_at: '2024-02-04T16:20:27+00:00'
updated_at: '2024-02-06T04:12:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi,

I've been testing around with monero-cli a bit and I do really like Monero as Project and concept, tho one feature I'm missing is the ability to *non-interactively* generate wallets.

When running ```./monero-wallet-cli --create-address-file --password [REDACTED] --mnemonic-language English --generate-new-wallet ./new.wallet ``` I get not just some output in the form ```new.wallet```, ```new.wallet.keys``` and ```new.wallet.address.txt``` but also have to deal with the whole interactivity, which I don't want to.

````
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Fluorine Fermi' (v0.18.3.1-release)
Logging to ./monero-wallet-cli.log
Generated new wallet: 
[REDACTED]
View key: [REDACTED]
**********************************************************************
Your wallet has been generated!
To start synchronizing with the daemon, use the "refresh" command.
Use the "help" command to see a simplified list of available commands.
Use "help all" command to see the list of all available commands.
Use "help <command>" to see a command's documentation.
Always use the "exit" command when closing monero-wallet-cli to save 
your current session's state. Otherwise, you might need to synchronize 
your wallet again (your wallet keys are NOT at risk in any case).


NOTE: the following 25 words can be used to recover access to your wallet. Write them down and store them somewhere safe and secure. Please do not store them in your email or on file storage services outside of your immediate control.

[REDACTED] [REDACTED] [REDACTED] [REDACTED] [REDACTED] [REDACTED] [REDACTED] [REDACTED]
[REDACTED] [REDACTED] [REDACTED] [REDACTED] [REDACTED] [REDACTED] [REDACTED] [REDACTED]
[REDACTED] [REDACTED] [REDACTED] [REDACTED] [REDACTED] [REDACTED] [REDACTED] [REDACTED] [REDACTED]
**********************************************************************
The daemon is not set up to background mine.
With background mining enabled, the daemon will mine when idle and not on battery.
Enabling this supports the network you are using, and makes you eligible for receiving new monero
Do you want to do it now? (Y/Yes/N/No): : N
Background mining not enabled. Set setup-background-mining to 1 to change.
If you are new to Monero, type "welcome" for a brief overview.
Error: wallet failed to connect to daemon: http://localhost:18081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or change the daemon address using the 'set_daemon' command.
Background refresh thread started
[wallet [REDACTED] (no daemon)]: exit
[REDACTED]@[REDACTED]:$ 
````

Not only is it ```interactive```but it doesn't really scale well and whilst one could [workaround some of these by using ```pipe```](https://monero.stackexchange.com/questions/10385/creating-a-wallet-in-non-interactive-mode-using-monero-wallet-cli/10395#10395), this doesn't scale well nor does it save the *mnemonic recovery phrase* at all.

Personally, a lot of my tools like [```mkp224o```](https://github.com/cathugger/mkp224o) and [```enc```](https://github.com/life4/enc) allow [scripting entire workflows](https://github.com/life4/enc?tab=readme-ov-file#armordearmor-the-message) making it easy to [alias recurring actions](https://github.com/kkarhan/misc-scripts/blob/master/bash/.bash_aliases#L55).

---

Proposed solution:

Add a ```---batched``` and/or ```---non-interactive``` flag to ```monero-wallet-cli```, parsing i.e. a ```batch.conf``` or ```non-interactive.conf``` file where one could define the parameters like language for the *mnemonic recovery seed* anlong side other parameters, allowing to automate wallet generation and potentially even transfers to said wallets.

For example ```monero-wallet-cli --non-interactive``` would generate a new folder named ```wallet```, automatically choose a secure password [i.e. running ```< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-128};echo;``` for a 128 digit, [secure password](https://www.howtogeek.com/howto/30184/10-ways-to-generate-a-random-password-from-the-command-line/)]. and write all the info into it, resulting in the following structure:

````
├── wallet 	
    ├── wallet.address.txt
    ├── wallet.mnemonic.txt
    ├── wallet.view.key.txt
    ├── wallet.wallet
    └── wallet.keys
````

Basically acting like a CLI version of [Monero Wallet](https://github.com/xmraddress/xmraddress.org) [Generators](https://monero-wallet-generator.com/) like the [one orphaned  who's code I keep online](https://github.com/kkarhan/paperwallet)... 

---

Use-Cases:

This would enable the design of *Monero Voucher Generators* that similar to  [Prepaid Cards](https://en.wikipedia.org/wiki/Stored-value_card) like [Paysafecard](https://en.wikipedia.org/wiki/Paysafecard#Functionality) could generate wallets on the fly and even load them with balance if desireable.

These could then print-out the ```wallet.address.txt```, ```wallet.mnemonic.txt``` and ```wallet.view.key.txt``` on thermal paper [or even generate [QR Codes](https://en.wikipedia.org/wiki/QR_code) for these as well] making it trivial to use these on the go - both offline and online.



Furthermore it makes integration of Monero simpler for 3rd party applications like online payment.

---

Looking into existing solutions:

As of writing, I've [not](https://monero.stackexchange.com/questions/7464/how-to-communicate-programmatically-with-the-monero-cli-wallet-using-php/7465#7465) [really](https://monero.stackexchange.com/questions/11043/how-to-generate-a-monero-wallet-programatically/11046#11046) found a good solution to this problem.

# Discussion History
## kkarhan | 2024-02-05T10:15:04+00:00
@0xFFFC0000 I'd Propose marking this as [feature](https://github.com/monero-project/monero/labels/feature) -[request](https://github.com/monero-project/monero/labels/request).

---

If I can be of any assistance in making #9152 happen, please let me know. 

## selsta | 2024-02-05T14:47:28+00:00
Is there a reason you don't use monero-wallet-rpc? It seems better suited for what you want to do, the CLI was never built for this. Though maybe I'm missing something.

## plowsof | 2024-02-05T14:49:03+00:00
This is possible with monero-wallet-rpc combined with a scripting language e.g. shell/python. We also have monero-javascript which is being used in this gift wallet generator https://xmr.gift/generator.

Redeeming these gift cards can be done instantly with the combination of scan_txid + the wallets seed. This area of UX is being worked on / has some proof of concepts already. I can share links later. 

## nahuhh | 2024-02-05T15:50:57+00:00
Left you a thumbs down to balance out your upvoting of yourself 

## kkarhan | 2024-02-05T18:56:47+00:00
> Is there a reason you don't use monero-wallet-rpc? It seems better suited for what you want to do, the CLI was never built for this. Though maybe I'm missing something.

@selsta sadly not as it doesn't do offline bulk generation of wallets.

The use-case is that of a basically airgapped wallet generator where one then takes the generated wallet and then uses the generated QR code for the primary address to top it up, and then gets a confirmation on a second loading terminal with the ```tx_id``` and ```restore height``` of the block -1 containing said transaction.

Basically turning it into one of those prepaid cards that have no balance until loaded after paying at the cashier...


Also being able to just generate wallets automatically and airgapped would allow preproducing said wallets in a physical card form - We've seen this with [Bitcoin being done](https://store.ballet.com/pages/real) and that really boosted adoption.

## kkarhan | 2024-02-05T19:03:03+00:00

> This is possible with monero-wallet-rpc combined with a scripting language e.g. shell/python. We also have monero-javascript which is being used in this gift wallet generator https://xmr.gift/generator.
> 
> Redeeming these gift cards can be done instantly with the combination of scan_txid + the wallets seed. This area of UX is being worked on / has some proof of concepts already. I can share links later.

@plowsof as I mentioned I am aware of these solutions but sadly they don't fit the use case of a "Monero Wallet Generator" in that they don't simply spit out said parameters in a way that lends itself for automation. 

Firing up a ```headless``` Firefox with Selenium seems very bloated espechally when [the desired parameters are already spit out in the ```cli-wallet```](https://github.com/monero-project/monero/issues/9152#issue-2117173887).

It's just inconvenient at scale to not have a ```--non-interactive``` flag that allows to automate the wallet generation process similar to how i.e. [```enc``` offers to just generate a key without user interaction](https://github.com/life4/enc?tab=readme-ov-file#generate-a-key).

## plowsof | 2024-02-05T19:16:39+00:00
i dont recall you mentioning the gift wallet generator i linked (which can be used offline) https://github.com/xmrdotgift/generator , but more over, the monero-wallet-rpc can do all of the things you require in probably less time that it has taken to draft up this issue / comment 

## nahuhh | 2024-02-05T23:07:51+00:00
>plowsof as I mentioned I am aware of these solutions but sadly they don't fit the use case of a "Monero Wallet Generator" in that they don't simply spit out said parameters in a way that lends itself for automation.

https://github.com/nahuhh/redeem_gift_poc/blob/generate_test/generate_gift_test

lol
MIT btw

is there _anything_ you need that ISNT already implemented?
this even writes the seed to an nfc card in encrypted form

# Action History
- Created by: kkarhan | 2024-02-04T16:20:27+00:00
