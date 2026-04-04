---
title: 'Ledger nano S: Wrong device status SW=6930'
source_url: https://github.com/monero-project/monero-gui/issues/2480
author: ghost
assignees: []
labels: []
created_at: '2019-11-24T11:53:22+00:00'
updated_at: '2019-11-25T18:59:14+00:00'
type: issue
status: closed
closed_at: '2019-11-24T13:41:23+00:00'
---

# Original Description
I'm a trying to open my wallet using my ledger nano S on a Windows 10 1903 machine but the wallets gives the error
```2019-11-24 11:49:48.299 9044 ERROR device.ledger src/device/device_ledger.cpp:414 Wrong Device Status : SW=6930 (EXPECT=9000, MASK=ffff)``` in the logs (and on the gui).

I am using a Ledger Nano S with the latest firmware version and the Monero app 1.4.1 (I tried with the 1.3.3 but same result).
I also tried to open the Monero wallet (gui) with administrator permissions but also, same result.

Any clue of why is this happening?
Logs attached.
[monero-wallet-gui.log](https://github.com/monero-project/monero-gui/files/3883490/monero-wallet-gui.log)


# Discussion History
## patrickdessalle | 2019-11-24T12:50:13+00:00
For what I understood on Reddit, the Monero app on Ledger is linked to a specific version of the Monero GUI app on your computer.
In order to use 0.15.0.1, Ledger (the company) needs to make a new Monero app (1.4.2 I suppose) as the 1.4.1 is linked to 0.15.0 and cannot accept 0.15.0.1

They said they'll work on it on Monday

## dEBRUYNE-1 | 2019-11-24T13:12:06+00:00
@patrickdessalle - Correct. Please see:

https://www.reddit.com/r/Monero/comments/e0lspk/gui_v01501_carbon_chamaeleon_ledger_nano_s/

## ghost | 2019-11-24T13:26:21+00:00
Oh, ok sorry about the dumb issue then.
One last question: do you know where I can download the monero gui version `0.15.0`?

## dEBRUYNE-1 | 2019-11-24T13:29:32+00:00
You mean v0.15.0.0? Because the only release with release binaries is v0.15.0.1. 

## ghost | 2019-11-24T13:39:45+00:00
Yes, or at least, the last version working with the Ledger app.

## ghost | 2019-11-24T13:41:22+00:00
Nevermind, I found a zip of the right version.

I'm sorry for wasting the time of everyone, next time, I'll search myself.

## cslashm | 2019-11-25T10:50:16+00:00
 v0.15.0.1 => app 1.4.2

## selsta | 2019-11-25T18:59:14+00:00
v1.4.2 is now out: https://www.reddit.com/r/Monero/comments/e1k7dg/ledger_monero_app_142_is_out/

# Action History
- Created by: ghost | 2019-11-24T11:53:22+00:00
- Closed at: 2019-11-24T13:41:23+00:00
