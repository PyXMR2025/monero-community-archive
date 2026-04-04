---
title: Unable to send transactions from Beta2 GUI wallet
source_url: https://github.com/monero-project/monero-gui/issues/659
author: TheRealMadmortigan
assignees: []
labels:
- resolved
created_at: '2017-04-04T01:56:46+00:00'
updated_at: '2017-12-13T12:27:15+00:00'
type: issue
status: closed
closed_at: '2017-12-13T12:27:15+00:00'
---

# Original Description
So apparently I'm unable to send any transactions from the Beta2 GUI wallet. I just found out when I tried to contribute to a FFS project, otherwise everything seems to be working fine. The Daemon does seem to delay to start but it always starts eventually and syncs up.

I'm running Windows Server 2012 R2 and all outgoing transactions get stuck with a PENDING status. CLI will eventually show the transaction as FAILED. I already re-downloaded the wallet, deleted the cache, restored from seed, and re-synced the entire blockchain. No firewall or other changes to the server. Any ideas?

# Discussion History
## Jaqueeee | 2017-04-04T05:39:37+00:00
Hi! Could you check a block explorer after you've sent to see if the tx has been relayed? 

## TheRealMadmortigan | 2017-04-04T13:16:17+00:00
Nothing on the block explorers.  I've now deleted the entire blockchain and am almost done re-syncing from scratch.  Once this completes I'll try to send again and let you know.

## TheRealMadmortigan | 2017-04-04T14:16:24+00:00
On another look, it seems it DID eventually broadcast the transaction -- Looking into them to see when they finally sent but this is quite strange behavior.  Let me know if anyone wants to look at logs, etc.

## TheRealMadmortigan | 2017-04-04T18:49:21+00:00
Update: Blockchain is synced and up to date again. Now wallet shows me having MORE XMR than I expected, still shows one PENDING transaction, Unlocked Balance shows (Waiting for Block).
It's entirely possible that balance was incorrect prior to the re-sync and is only NOW displaying the correct balance. I don't keep that close an eye on my holdings but it's over by quite a bit...
Here's some screenshots I've gathered: http://imgur.com/a/hIakD
*The error I receive after starting the GUI
*The daemon log about 5 minutes later (the daemon connects eventually on it's own)
*The log now that the blockchain is fully synced.
Having already deleted the client, blockchain, and wallet files, I'm starting to think there's a local issue with my system. Anything else I can do to help identify the issue?

## Jaqueeee | 2017-04-04T20:10:13+00:00
hi @TheRealMadmortigan 
**1. The balance has increased.** 
It could mean the wallet or daemon wasn't fully synced last time you used it. Did you create a new transaction this time or is the PENDING transaction the same as before? In the latter case, could you provide the tx id or check on a block explorer if it's included in a block.

**2. You get the "daemon failed to start" message, but the daemon starts.** 
Others have reported this error when they had a space in the path where gui was installed. Read in your reddit post that this is not the case. However, i've done some updates in this build that fixed the issue for others. Could you please try it?
https://build.getmonero.org/downloads/monero-core-5d45967-win64.zip




## TheRealMadmortigan | 2017-04-04T20:35:29+00:00
Hi @Jaqueeee 

Thanks for the help!

It's possible it was out of sync but the wallet has been working fine both inbound and out and the balance was at the lower amount for months.  Only since the Beta 2 update did it begin to have issues sending transactions.  There is still one transaction PENDING: 

224ee438e47e16859927f5ee9b5298e0aeb8487485d5df9c0c230564cca4be2a

I'm not seeing it on any block explorers.

The wallet seems stable now but the balance is still higher than expected.  My unlocked balance also reads "waiting for Block" still but does show the same as the balance.  Is that normal, or indicative or something wrong?

The pending transaction is only 3 XMR for a FFS so worst case at this point is that it goes through and Fireice_uk gets funded an hour earlier, lol.  I would like to know that my balance is correct and help others avoid this issue as well.  Let me know if there's anything more can provide to help.  I work in IT at a high level so feel free to get technical.  Am not developer.

## TheRealMadmortigan | 2017-04-04T20:48:41+00:00
@Jaqueeee 

FYI -- I installed the new client you gave me.  Same issue with the delayed daemon start:  Here's the log if interested:

http://imgur.com/unsof0P



## Jaqueeee | 2017-04-05T05:21:42+00:00
@TheRealMadmortigan This would help me debug this:
1. Switch to log level 3 on settings page
2. Close wallet
3. delete/move monero-wallet-gui.log
4. start gui and reproduce error
5. Upload log content to https://paste.fedoraproject.org and paste link here



## TheRealMadmortigan | 2017-04-05T06:09:18+00:00
I'm performing the requested steps now.  FYI -- I'm unable to send any transactions currently with the error "was rejected by daemon with status: Failed. Reason: double spend"

Will upload the log shortly.

## TheRealMadmortigan | 2017-04-05T06:17:56+00:00
@Jaqueeee 

Output below, as requested.

https://paste.fedoraproject.org/paste/lG05hPvd8LYqgsxKcjak515M1UNdIGYhyRLivL9gydE=

## Jaqueeee | 2017-04-13T10:07:45+00:00
Hi @TheRealMadmortigan. Sorry for late reply. Have been busy last week. Are you still experiencing issues with sending? 

## golere | 2017-06-21T08:52:21+00:00
Here is a guy with a pretty similar problem: https://www.reddit.com/r/Monero/comments/6ikbof/xmr_in_limbo_after_transaction_behind_firewall/

## medusadigital | 2017-08-07T20:19:33+00:00
allright, seems to me we can close this ? 
the issue was resolved by flushing the mempool. 

doesnt seem to be a bug after all.

please pitch in if you think otherwise.



## dEBRUYNE-1 | 2017-12-13T11:09:06+00:00
This issue is resolved as follows:

https://monero.stackexchange.com/questions/6649/transaction-stuck-as-pending-in-the-gui

+resolved

# Action History
- Created by: TheRealMadmortigan | 2017-04-04T01:56:46+00:00
- Closed at: 2017-12-13T12:27:15+00:00
