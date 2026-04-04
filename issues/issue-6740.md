---
title: My Ledger wallet seems to always crash. I get the following error
source_url: https://github.com/monero-project/monero/issues/6740
author: drinkyd
assignees: []
labels: []
created_at: '2020-08-03T18:32:06+00:00'
updated_at: '2022-02-19T04:22:28+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:22:28+00:00'
---

# Original Description
Hi, 

With the GUI it never finishes syncing and crashes. 

With the CLI, I get to "Starting refresh..." and get this error:

terminate called after throwing an instance of 'std""runtime_error'
 what(); wrong Device Status: 0x6f42 (UNKNOWN), EXPECTED 0x9000 (SW_OK), MASK 0xffff

Does anyone know what is causing this and how I can sync my wallet to the local chain I downloaded without crashing? I'm running the latest version of Monero on window 10 with SSD drive. 

Thanks. 

# Discussion History
## selsta | 2020-08-03T20:29:36+00:00
Are you running the latest Ledger firmware and Ledger monero app and monero software?

Can you try to recreate your wallet?

## drinkyd | 2020-08-04T05:37:13+00:00
Yes latest version of everything. When you say recreate wallet? Do you mean to reset my ledger? My wallet worked before but it took forever. Now it just gives me the error described in the original post.

## selsta | 2020-08-07T09:54:28+00:00
> Do you mean to reset my ledger? 

No, just create a new monero wallet with your Ledger.

Also can you try to use a different computer?

## drinkyd | 2020-08-12T05:17:38+00:00
If I create a new wallet, how do I transfer my funds to this new wallet if I can't access the funds due to the crashing? 

## selsta | 2020-08-12T05:19:52+00:00
If you restore your Ledger wallet on a different computer your funds will be there, no transfer necessary.

## drinkyd | 2020-08-15T06:51:02+00:00
Yes I tried it on another computer. And now the GUI just closes automatically during syncing. *sigh* I think I'm going to give up. It shouldn't be that difficult accessing funds.  Any more ideas what I can do? I've been dealing with this for months. 

## selsta | 2020-08-15T11:00:11+00:00
So both CLI and GUI also have issues on a different computer?

You can follow this tutorial to convert your Ledger seed into a Monero seed: 
https://monero.stackexchange.com/questions/11979/how-to-convert-ledger-seed-to-monero-compatible-seed-on-windows

This should only be done as a last step if everything else fails as it exposes your Ledger seed to your computer.

# Action History
- Created by: drinkyd | 2020-08-03T18:32:06+00:00
- Closed at: 2022-02-19T04:22:28+00:00
