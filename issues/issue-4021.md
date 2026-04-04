---
title: transaction using GUI taking more than 48 hours
source_url: https://github.com/monero-project/monero-gui/issues/4021
author: cnxnhcv
assignees: []
labels: []
created_at: '2022-09-03T21:42:53+00:00'
updated_at: '2022-09-04T17:12:19+00:00'
type: issue
status: closed
closed_at: '2022-09-04T17:12:19+00:00'
---

# Original Description
I am moving some of my XMR into another wallet to exchange it, however, it is still going through confirmations for two days,
is this normal? and how to fix it.
many thanks

# Discussion History
## cnxnhcv | 2022-09-03T22:54:22+00:00
I am using version (0.18.1.0)
hight (2287055)
mode: advanced (Remote node), I tried changing the remote node too, but still the same issue,

## selsta | 2022-09-04T00:26:07+00:00
- Do you have a transaction id?
- Which remote node do you have set?

Transactions in monero take seconds, with 2 minutes to confirm. So if the exchange has sent the coins then they should be in your wallet.

## cnxnhcv | 2022-09-04T10:16:15+00:00
yea :6a53317b847d46cad508a4df27e5c0a0d9bfb4bcca5febc47976878edb5585e7

and I use the remote nodes from:https://nodes.monero.com/
I tried their main one, changed two times but no difference.

## selsta | 2022-09-04T10:30:10+00:00
You can go to Settings -> Wallet, press "Scan transaction" and then enter the transaction id. Please check if the transaction shows up and do this only once per transaction id.

## cnxnhcv | 2022-09-04T10:52:47+00:00
it does show up, its on 1957 confirmations and still going since more than 48 hours, and block height of 2702534

## selsta | 2022-09-04T10:53:30+00:00
And previously it did not show up?

## selsta | 2022-09-04T10:57:17+00:00
You have to explain in more detail what you are doing and what the exact issue is.

## cnxnhcv | 2022-09-04T10:57:17+00:00
it was showing up all the time, since the start, but I never got it on my exchange wallet, and my other wallet says they will notify me when an xmr is coming, however, they didn't detect anything coming for 2 days, and when I check the GUI transaction is still increasing in confirmations.

## selsta | 2022-09-04T10:58:22+00:00
Which exchange are you using? What is this wallet that "notifies" you? The transaction is confirmed and the issue is purely on the receiving side.

## cnxnhcv | 2022-09-04T11:04:34+00:00
I will contact them, however, I used their website to change from xmr into btc and the opposite, and never had an issue, probably as you said I have to contact them, their website always tells me there is xmr waiting to confirm.
jus asking if is it normal the confirmation is increasing after two days. or it is the receiving side issue?

## selsta | 2022-09-04T11:05:43+00:00
It takes ~2 minutes for a transaction to confirm. The issue is definitely on the receiving side, assuming you sent the funds to the correct address.

Also which wallet is this wallet that "notifies" you?

## cnxnhcv | 2022-09-04T11:15:58+00:00
I might use the word (notify) wrong here, my apologies.

when they receive the xmr they tell me it arrived and going through an exchange process, it's changenow.io website.
I'll contact them and update everything here.

many thanks.


## selsta | 2022-09-04T11:16:52+00:00
I just wanted to make sure you aren't using freewallet which is a scam.

## cnxnhcv | 2022-09-04T11:21:28+00:00
wish I knew about this before, coz I already got scammed a few years ago with a free online wallet, but moved a few xmr that is less than 50 dollars as a test, 

probably should start adding my GUI wallet to my USB wallet, since it has the option to do so.


## selsta | 2022-09-04T11:25:27+00:00
Make sure to only use wallets recommended here: https://www.getmonero.org/downloads/

Don't use Google and search for "monero wallet".

# Action History
- Created by: cnxnhcv | 2022-09-03T21:42:53+00:00
- Closed at: 2022-09-04T17:12:19+00:00
