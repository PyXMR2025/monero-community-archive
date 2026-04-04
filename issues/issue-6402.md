---
title: Help please! Failed transaction stuck! How to cancel??
source_url: https://github.com/monero-project/monero/issues/6402
author: dimyself
assignees: []
labels: []
created_at: '2020-03-25T02:43:43+00:00'
updated_at: '2020-11-05T18:12:33+00:00'
type: issue
status: closed
closed_at: '2020-10-15T22:46:22+00:00'
---

# Original Description
Hi there, I've read / tried everything I can think of. This is the current status of the "send" transaction I'm trying to release is "failed" "out". I've tried recreating the wallet using the seed/key words. I was using 15.0.2 gui wallet on linux. I had done a few send/receive transactions previously, but for some reason this transaction didn't go through.

So, after downloading the latest gui 15.0.4 and restoring my wallet using key words, it never restored the fund.

So, I'm trying to run "flush_txpool" like this: ./monerod flush_txpool and also ./monerod flush_txpool <tran_id> .... and I just keep getting this error:

"Error: Unsuccessful -- json_rpc_request:"

Is there not an easier way to cancel a transaction??? Like maybe IDK, right-click cancel? Or to run flush_txpool from the gui or something? There's no options in the gui whatsoever that I can see. I also see no options using ./monero-wallet-cli.

So, I have to run monerod and build a 77gb DB just to cancel a transaction?? Also, how come theres not auto timeout on transactions? It's been a full day and its still locked up. Obviously this is abnormal for a transaction, no?

What am I missing here?? I see hardly any information in the documentation either on how to fix this. And the little bit I do see, is unclear on what to do.

Sorry if this is coming across impatient, I'm just tired of dealing with this. I've been troubleshooting this for hours now and see nothing helpful on how to fix. It seems this should be greatly improved process, unless I'm just missing something

Thanks

# Discussion History
## sumogr | 2020-03-25T05:23:21+00:00
run monerod and type flush_txpool from daemon. then run your cli wallet and type rescan_spent

## dimyself | 2020-03-25T06:35:19+00:00
Thanks for reply.

I do that, and after rescan_spent it says "out of sync"

Then if I run balance it shows the same incorrect balance. If I run show_transfers, I still see the "failed" "out" transaction.

I then exit the cli wallet and log back in. But the balance is the same, and still missing the failed transaction (which still shows up using the show_transfers command

What else can I try?

## dimyself | 2020-03-25T06:55:27+00:00
One thing I noticed is, on the cli it shows "failed" status, but in the gui, it shows Blockheight: Pending, Address Sent to: "Waiting on address to leave txpool"; Confirmations: 0/10

Did I lose my money??? I don't know what is going on here?! If I flush_txpool, it's trying to remove the transaction from my history/transactions page, but it's not adding the XMR back into my balance

Is there possibly someone I can talk to? Like a discord chat or somewhere else? I'm afraid the money's gone, and I need to get this taken care of. It's been a full day I've been working on this.

Thank you!

## sumogr | 2020-03-25T07:08:51+00:00
keep your daemon synced and type rescan_bc on cli

## dimyself | 2020-03-25T07:19:37+00:00
So, I ran it from cli. Before I ran it , I could see the failed transaction in show_transfers.

After I ran it, it asked for wallet password which I put in. But it still just shows the same balance. Show_transfers doesn't list the failed transaction anymore either.



## moneromooo-monero | 2020-05-16T17:41:06+00:00
I assume you either got your money back or the tx was mined by now, right ?

## HelmesPaul | 2020-11-05T18:12:33+00:00
Thank you sumogr!! "rescan_bc" command in cli wallet was the solution! Yes moneromooo the money is back on the account.

# Action History
- Created by: dimyself | 2020-03-25T02:43:43+00:00
- Closed at: 2020-10-15T22:46:22+00:00
