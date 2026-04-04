---
title: Transaction not appearing - I've followed all instructions!
source_url: https://github.com/monero-project/monero-gui/issues/1328
author: rodoebri
assignees: []
labels:
- resolved
created_at: '2018-04-18T14:48:02+00:00'
updated_at: '2018-04-19T20:54:21+00:00'
type: issue
status: closed
closed_at: '2018-04-19T20:54:21+00:00'
---

# Original Description
Hi all.  I sent 8 Monero from my Binance account to my wallet about 12 hours ago.  It was the old wallet so since then I have upgraded to the new wallet, renamed my wallet so that it re-downloaded the wallet file and it is still not appearing.  I also tried verifying the transaction at https://xmr.llcoins.net/checktx.html and it is saying that my private key is invalid!

Here is the transaction provided by Binance:  https://moneroblocks.info/tx/38609776fddb5bf5fae9fefcc8999bd22e9707bcaa7be84c15f36f325415bfa5

The transaction appears to have gone through from Binance but at this point I am at a loss.  I am hoping it has not disappeared but am losing a bit of that hope. 

Any help would be appreciated!

# Discussion History
## rodoebri | 2018-04-18T14:48:48+00:00
P.S. I am using the GUI wallet monero-gui-win-x64-v0.12.0.0 

## dEBRUYNE-1 | 2018-04-18T17:56:59+00:00
>and it is saying that my private key is invalid!

Are you sure you followed this guide correctly?

https://monero.stackexchange.com/questions/6137/how-do-i-as-a-recipient-verify-that-my-transaction-actually-arrived

Also, are you using a local node or a remote node?

## rodoebri | 2018-04-18T19:23:34+00:00
Yes.  I filled in the information exactly to the linked tool and it told me that the private key was invalid.  

I just tried again and now it of course is saying the following but it still is not appearing in my wallet:

This address owns output        0 with pubkey: 0e904a636d60cdf3f83b02f5c000e37c7a39ca108489b561d9964a27349884d1 for amount: 7.84310901
This address doesn't own output 1 with pubkey: d4258851534dabc2f8c8c8636020bf378102ced4bb6e7527a5be325a5d332b6d for amount: Confidential

Total received: 7.84310901
Found payment ID:  xxxxxxx (do you need this?).

I am using a local node and it says that both the wallet and daemon are up to date.  However this added balance is not appearing.

Thanks!

## dEBRUYNE-1 | 2018-04-18T20:06:03+00:00
>I am using a local node and it says that both the wallet and daemon are up to date. 

Could you post the full output of `Show status` (on the `Settings` page of the GUI)?

## rodoebri | 2018-04-18T20:50:44+00:00
Here you go:
Height: 1554457/1554457 (100.0%) on mainnet, not mining, net hash 549.96 MH/s, v7, up to date, 8(out)+2(in) connections, uptime 0d 0h 52m 58s

Height: 1554457/1554457 (100.0%) on mainnet, not mining, net hash 549.96 MH/s, v7, up to date, 8(out)+2(in) connections, uptime 0d 0h 55m 50s

Height: 1554457/1554457 (100.0%) on mainnet, not mining, net hash 549.96 MH/s, v7, up to date, 5(out)+0(in) connections, uptime 0d 5h 22m 17s

Height: 1554457/1554457 (100.0%) on mainnet, not mining, net hash 549.96 MH/s, v7, up to date, 5(out)+0(in) connections, uptime 0d 5h 22m 22s

Height: 1554457/1554457 (100.0%) on mainnet, not mining, net hash 549.96 MH/s, v7, up to date, 1(out)+1(in) connections, uptime 0d 7h 12m 0s

Height: 1554457/1554457 (100.0%) on mainnet, not mining, net hash 549.96 MH/s, v7, up to date, 1(out)+1(in) connections, uptime 0d 7h 12m 9s


## rodoebri | 2018-04-19T14:13:46+00:00
Should I be worried?

## dEBRUYNE-1 | 2018-04-19T15:45:14+00:00
Your `Show status` output indicates that you're on the wrong (alternative) chain. Therefore, you should be able to resolve your issue with this guide:

https://monero.stackexchange.com/questions/7989/i-forgot-to-upgrade-from-cli-or-gui-v0-11-to-cli-or-gui-v0-12-and-as-a-result

Please note:

>As a general rule of thumb, for each day you synced after the fork height (1546000 or April 6) you have to pop 800 blocks. Thus, let's say you synced 10 days on the wrong (alternative) chain, you should use --pop-blocks 8000

Since we're 13 days after the scheduled network upgrade, you ought to use `--pop-blocks 10400`

P.S. I reckon aforementioned guide might be a bit convoluted. Therefore, if you need any assistance, feel free to shoot me a PM on Reddit:

https://www.reddit.com/user/dEBRUYNE_1/

## rodoebri | 2018-04-19T20:37:38+00:00
Thanks!  Finally fixed it.  I had a few errors, realized Windows Firewall was still blocking a couple of Monero executables, but it's all in there.

Thank you again for your help! 

## dEBRUYNE-1 | 2018-04-19T20:48:02+00:00
Good to hear and you're welcome :) 

+resolved

# Action History
- Created by: rodoebri | 2018-04-18T14:48:02+00:00
- Closed at: 2018-04-19T20:54:21+00:00
