---
title: Help Requested - Zero Balance after recovering via seed and blockchain/wallet
  sync - reset height to 0 same issue
source_url: https://github.com/monero-project/monero-gui/issues/3664
author: InvoluntaryYoga
assignees: []
labels: []
created_at: '2021-08-11T01:27:27+00:00'
updated_at: '2022-09-23T14:13:00+00:00'
type: issue
status: closed
closed_at: '2021-08-11T03:01:42+00:00'
---

# Original Description
Hello,

I am having an issue after needing to reinstall Monero GUI that it shows a zero balance.
Windows crashed on me, so I decided to install Linux and Windows as a dual boot. 
I have the monero GUI on both of them now, and have tried the following on both, to no avail.

First, I did a recovery via my seed/recovery phrase, and used a rounded down value for my restore height.
I ran a local node (without pruning).
I let my blockchain sync. I let my wallet sync.
I looked at my wallet, which showed a zero balance. 

Prior to my PC crashing, my wallet definitely had more than a 0 balance, and had only received into that wallet and not sent from said wallet. Unfortunately, I do not have any transaction information. I only know my restore height (around 1750000) and recovery/seed phrase.

I have tried to follow the directions here: 
https://monero.stackexchange.com/questions/6640/i-am-missing-not-seeing-a-transaction-to-in-the-gui-zero-balance

The above directions, however, did not fix the issue.
I have tried setting the restore height ~ 10k before my restore height I wrote down, and also tried setting it to 0. 
I have tried a different operating system. 
I have verified I am synced up to the latest block via looking at the block explorer (XMRchain). (I am at 2424416 right now)
I have renamed my wallet in order to initiate my wallet to rebuild/sync. 
I have tried using a remote node (node.moneroworld.com:18089). 
Nothing seems to work.

I also see 0 transactions in/out from my wallet. 
I'm not sure if that is 100% way of knowing that I somehow did not have my wallet taken from me via bad actors or what. Just some more info...It makes it seem like this is not the case.

I'm running Monero GUI version 0.17.2.2-937cb98.
Embedded monero version is 0.17.2.0-release according to the GUI.
The only other thing that I can think of that changed between now and then is using a different router, which I don't believe is any issue with any firewall rules since the blockchain still synced and I have not had issues with other wallets.

Any help would be greatly appreciated!

Here is what displays if I look at the status:
[8/10/21 9:28 PM] 2021-08-11 01:28:13.938 I Monero 'Oxygen Orion' (v0.17.2.0-release)
Height: 2424418/2424418 (100.0%) on mainnet, not mining, net hash 2.71 GH/s, v14, 12(out)+0(in) connections, uptime 0d 0h 13m 20s




# Discussion History
## selsta | 2021-08-11T01:29:53+00:00
It does not sound like that your funds are stolen, else you would see a transaction history with an outgoing transaction.

As a first step, please go to the Account page and check if you see your balance there.

## InvoluntaryYoga | 2021-08-11T01:31:10+00:00
0 Balance under the account tab as well.

## selsta | 2021-08-11T01:31:55+00:00
Do you have a transaction id from an incoming transaction?

## InvoluntaryYoga | 2021-08-11T01:32:23+00:00
Unfortunately, no. I only wrote down my recovery phrase and restore height.

## selsta | 2021-08-11T01:33:00+00:00
Do you know how to use the CLI wallet?

## InvoluntaryYoga | 2021-08-11T01:33:44+00:00
I do not. I have been on Linux for roughly 10 days or so ... limited command line knowledge, but ....gotta start sometime.

## selsta | 2021-08-11T01:35:34+00:00
You basically need these commands:

```
./monerod --detach
./monero-wallet-cli --restore-deterministic-wallet
```

Set restore height to 1.

## InvoluntaryYoga | 2021-08-11T01:37:39+00:00
Should I close the GUI and keep the daemon running before I do this? 

## selsta | 2021-08-11T01:38:09+00:00
Close the GUI, if you keep the daemon running you don't have to run ./monerod

## InvoluntaryYoga | 2021-08-11T02:06:41+00:00
I get an error "bash: ./monerod: No such file or directory".
This made me think I need to install the CLI version.

Sorry for the lack of understanding. Thank you for helping so far. 
Do I need to be in a certain directory for this?
Just verified and extracted the CLI.

## InvoluntaryYoga | 2021-08-11T02:12:56+00:00
Ah, I follow now. Needed to be in directory of the CLI I just downloaded as suspected.

## InvoluntaryYoga | 2021-08-11T02:39:13+00:00
Untagged accounts:
          Account               Balance      Unlocked balance                 Label
 *       0   xxxxxxx      0.000000000000        0.000000000000       Primary account
----------------------------------------------------------------------------------
          Total        0.000000000000        0.000000000000
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 0.000000000000, unlocked balance: 0.000000000000

[wallet xxxxxxx]: status
Refreshed 241952/241952, synced, daemon RPC v3.5, SSL
[wallet xxxxxxx]: version
Monero 'Oxygen Orion' (v0.17.2.0-release)
[wallet xxxxxxx (out of sync)]: balance
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 0.000000000000, unlocked balance: 0.000000000000
[wallet xxxxxxx (out of sync)]: show_transfers
[wallet xxxxxxx (out of sync)]: refresh
Starting refresh...
Refresh done, blocks received: 4916                             
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 0.000000000000, unlocked balance: 0.000000000000
[wallet xxxxxxx]: wallet_info
Filename: MyWallet1
Description: <Not set>
Address: xxxxxxx
Type: Normal
Network type: Mainnet
[wallet xxxxxxx]: show_transfers


This is what I have thus far.

Something I just noticed though.
The last word of my recovery phrase is a repeat of another word...When I went to write this in the CLI, I skipped one and noticed it also repeated a word. Does it repeat a word at the end of the mnemonic seed if you missed a word? 

If so...I may have made a very bad goof and wrote down an incorrect mnemonic seed.

If this is the case, I do have a backup of my wallet on a hard drive. Can I recover from this if I have the password?


## selsta | 2021-08-11T02:53:38+00:00
In general a monero seed should have 25 words. One word repeating is normal, it's a checksum.

> If this is the case, I do have a backup of my wallet on a hard drive. Can I recover from this if I have the password?

Yes.



## InvoluntaryYoga | 2021-08-11T03:00:14+00:00
Just to clarify, I did have 25 words in my recovery phrase. Just the last word was a repeat of another previously used.

Anyways, I could not get it to restore with the other methods, but sure enough super easy with the backed up wallet. 
Not sure why I hadn't thought of that days ago!

Thank you so much though! 


## selsta | 2021-08-11T03:01:42+00:00
Were you able to restore from backup? Can you confirm that the seed is the same as you wrote down? It should always be possible to restore from seed without issues and there are no known bugs around it.

Closing this for now as there doesn't seem to be any bug.

## InvoluntaryYoga | 2021-08-11T03:13:54+00:00
Confident no bug.

I can confirm that it is not what I wrote down as my XMR seed, but the seed phrase I got from the backup does seem familiar (I'd say 98+% sure of the first 5 words being used before for phrases).
I'm pretty confident now that I mix-matched recovery phrases for different cryptos. I do not have all of them here physically, but I have another copy in a safe place, but is hours away. I can confirm MAYBE this weekend with those copies if this is what happened, but not sure yet.

Sorry for your troubles. I am glad I got it sorted out though. And I also learned a teeny bit about the CLI. 
Can I throw a bit of XMR your way for your troubles?

## selsta | 2021-08-11T03:23:53+00:00
>  Can I throw a bit of XMR your way for your troubles?

Not necessary as I get community funding (ccs.getmonero.org) :) But thanks anyway!

# Action History
- Created by: InvoluntaryYoga | 2021-08-11T01:27:27+00:00
- Closed at: 2021-08-11T03:01:42+00:00
