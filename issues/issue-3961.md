---
title: Monero GUI showing zero balance issue
source_url: https://github.com/monero-project/monero-gui/issues/3961
author: purpleskie5
assignees: []
labels: []
created_at: '2022-07-06T06:56:33+00:00'
updated_at: '2024-04-02T22:25:17+00:00'
type: issue
status: closed
closed_at: '2022-07-06T20:30:39+00:00'
---

# Original Description
Would appreciate any help here:

I made a withdraw yesterday from the exchange to my MoneroGUI, I first had an issue with connecting to a node but that was solved after connecting to a remote one.

But the issue is it's not showing any transactions and the balance is zero.
I double checked the address before and after I made the withdrawal and it's the same.

I recently changed the wallet block to 1940000 as someone suggested but that still didn't work, I tried previous blocks as well but it's still not showing.

I also went to the tool where you can check if the transaction succeeded and entered the Tx Id, Private view key and Primary address. I then got an error saying "View Key doesn't match your address".
So I tried searching the MoneroBlocks and entered the Tx ID and it showed me a transaction but neither the inputs or outputs belong to me.

I'm also not using Trezor or a Ledger wallet,  The only thing I could think would be out of the box is that at the beginning I forgot my wallet's password and had to restore it using the seeds and noticed a new wallet was added (or the same one) with different seeds and with the new name I entered.

Soon after, I remembered the password for the first one so I thought why keep the new one and proceeded in deleting it.
I don't think it had something to do with this but again I'm new to this and could be wrong.


# Discussion History
## selsta | 2022-07-06T19:20:25+00:00
As a first step, please go to Settings -> Info and post

- Version
- Wallet restore height
- Wallet mode

Also please post the transaction id of the missing transaction.

## purpleskie5 | 2022-07-06T19:33:00+00:00
It's resolved right now, The issue was with the address.
I don't know if I'm the only one who faced this but there is an obvious glitch in the GUI address based on what I've experienced.

For some reason when you click on copy the primary address and paste it, a totally different address appears, even when you double click and paste it.

I checked this before making the transaction and thought that Monero or Kraken decodes your address into another one since it is a stealth address crypto and proceeded with the withdraw.

It is not until I made another wallet and tried to register the address to make a withdraw that an error message appeared and said it was already registered.
Turns out you have to manually copy the address with the cursor and leave the last character out then adding it later, to give the same address that is showing in the GUI.

The fault also lies with me for not probably researching more about this, Is there a way you can retrieve funds sent to another address (maybe not even registered?)

## selsta | 2022-07-06T19:34:22+00:00
Which operating system are you using? Could it be that you have malware on your system? The address should never change after pasting.

## purpleskie5 | 2022-07-06T19:45:11+00:00
I'm using windows 11, I'm not running any anti-virus only windows security.
Even though I'm copying the correct one right now it's showing me a different one, it could be a malware.
What do you recommend to do?


## selsta | 2022-07-06T19:46:38+00:00
What you describe sounds like typical malware behavior, they replace your address with theirs.

Can you post your address here and also the address it replaces to?

## purpleskie5 | 2022-07-06T19:49:39+00:00
My address:
4AHWy89S4fzjG6n9JX4PUD34YwgJVV4XREG4qnRh1EdxbfhDHHzskguZHyvuAx2qhTeT3MG4C6EbAVhDbf8WNNaLTGhwsvW
It changes to:
47vcMwEwosJRc4bCAcRRw7WwezTRn8dCHBjTnYXsZG3UR3Eya88PN3rZKexzwJojRMGVexryHmy47NXmNuDyZirWSexaEYv

## purpleskie5 | 2022-07-06T19:55:12+00:00
I searched it, It is a malware, Other people have reported it.

## selsta | 2022-07-06T19:55:28+00:00
Does the same happen when you copy a Bitcoin or Ethereum address?

In any way, the best thing you can do is reinstall your operating system and consider all wallets and accounts you logged into compromised.

It's possible that you only have the clipboard swapper installed but if you want to be on the safe side change your passwords and generate new wallets once you have reinstalled your operating system.

## purpleskie5 | 2022-07-06T20:05:09+00:00
I'm not using any other cryptos or wallets.
I tried to locate the path and found a folder with these commands:

Retrying to obtain clipboard.
Detected recursive rearrange. Aborting after two iterations.
Retrying to obtain clipboard.
Retrying to obtain clipboard.
Unable to obtain clipboard.

That's the one right?


## plowsof | 2022-07-06T20:17:06+00:00
The address appears in this thread: https://www.reddit.com/r/Monero/comments/mcvuxc/beware_crypto_stealing_malware/

Your system is 'compromised' and there could be more evil things other than just a clipboard swapper. i would backup any important files to external storage as soon as possible, and follow selstas advice. the monero wallets you have now , should never be used again and a clean operating system install.

## purpleskie5 | 2022-07-06T20:28:33+00:00
Will do, Thanks for the advice and everything.
I will figure out how to download Ubuntu and install a new operating system as soon as I can.
At least I won't lose the lesson
Thanks again.

## selsta | 2022-07-06T20:30:38+00:00
I'll close this here as there isn't anything we can do on our side, but you can still write comments if you have remaining questions.

## Tribe78 | 2023-12-14T23:28:42+00:00
Hi, I have a similar issue.
I copy and pasted the address I wanted to send funds to. I didn't check it properly and sent funds. I assumed it changed the address for security.
The funds are gone and never arrived.
There is a red circle next to the transaction and says sent to "unknown recipient".
Any advice if its gone, or can recover?


## selsta | 2023-12-15T05:08:32+00:00
@Tribe78 what do you mean with "it changed the address"? Can you elaborate? Do you have a transaction id?

## Tribe78 | 2023-12-15T06:46:35+00:00
I copied the address from where I wanted to send the funds, and pasted the address into Monero and sent the funds.
The funds never arrived at destination. I have rescanned, changed to larger block height. Opened new wallets and used keys and seed to restored. I cant seem to get them back. So paranoid I have lost them. 
There is a red dot next to the sent transaction. So Im hoping it didnt arrive and its recoverable.
Here is the transaction ID.
b0bdf05fe733fcc16fcc077de562e8de48ff8db44c0c78ce2206996217c1d1e7

## selsta | 2023-12-15T16:11:58+00:00
Just to clarify, do you own the wallet that should have received it?

## Tribe78 | 2023-12-15T19:25:12+00:00
No I don’t own the wallet it went to.


## selsta | 2023-12-15T19:26:25+00:00
How can you be sure that the issue isn't on the receiving side?

Also which operating system are you using? Is it possible that there is address changing malware installed, e.g. Windows?

## Tribe78 | 2023-12-15T19:31:24+00:00
I don’t know if problem is on other side.
I am on a Mac. I have scanned my computer for malware. Monero always shows up as effected. But no malware. 

I was wondering if it was malware as well.



## selsta | 2023-12-15T19:32:09+00:00
Did you try to reach out to the receiver with the transaction id?

## Tribe78 | 2023-12-15T19:48:36+00:00
How do I do that?
The transaction ID is different to the address for the address I tried to send to?
Is there a way to contact the owner of the ID? 

## selsta | 2023-12-16T02:23:08+00:00
I don't know who you sent it to. If it was an exchange contact their support, if it was a website try to send an email.

> The transaction ID is different to the address for the address I tried to send to?

Yes. The transaction ID is the identification of the transaction itself, the address is where the transaction ID is getting sent to.

> Is there a way to contact the owner of the ID?

Not in monero directly. You have to manually reach out to the person, e.g. by email, support chat or whatever.

# Action History
- Created by: purpleskie5 | 2022-07-06T06:56:33+00:00
- Closed at: 2022-07-06T20:30:39+00:00
