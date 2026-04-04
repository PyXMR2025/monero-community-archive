---
title: Double spend even after re-sync following a failed 'pending' tx
source_url: https://github.com/monero-project/monero-gui/issues/3930
author: okuh196
assignees: []
labels: []
created_at: '2022-05-25T16:01:11+00:00'
updated_at: '2025-01-06T16:23:24+00:00'
type: issue
status: closed
closed_at: '2022-11-03T21:17:17+00:00'
---

# Original Description
Greetings all.

After an unsuccessful attempt to send money (the transaction received a failed status after several hours of pending status)
I received on the same purse one more transaction and decided to spend money thinking that there could be no problem, but now I receive error 
"Couldn't send the money: transaction <abcd> was rejected by daemon with status: Failed. Reason: double spend"

I saved the old wallet file without the extension and imported the keys after reloading the wallet to have the network scanned from scratch. But the problem remained.

# Discussion History
## selsta | 2022-05-25T20:50:58+00:00
Can you go to Settings -> Info and post:

- Version
- Wallet mode

## selsta | 2022-11-03T21:17:17+00:00
Closing due to lack of reply.

## alecov | 2024-04-22T18:23:40+00:00
Reopen this. Happened twice to me during the last few weeks.

GUI version: 0.18.3.3-release (Qt 5.15.13)
Embedded Monero version: 0.18.3.3-release
Wallet mode: Advanced mode (Remote node)

Running on Tor over a relatively unstable connection. 

This pops in the log occasionally: `Unable to send transaction(s) to tor - no available outbound connections`.

The first time it happened, the transaction eventually went through and got mined. This _definitely_ proves that "Transaction Failed" is a UX bug: a transaction can _never_ absolutely fail if at least some other node around got hold of it, since nothing guarantees the transaction will not be mined eventually (short of a double-spend transaction).

EDIT: The second one has also eventually confirmed. This is beyond terrible -- I was messing around with `flush_txpool` without success nor an indication of what was wrong.

## CocolinoFan | 2025-01-06T16:23:23+00:00
God bless you @alecov !
Yes! Running `flush_txpool` in the local monerod fixed the issue for me too. 
Wow I was stuck with this for a whole day!

# Action History
- Created by: okuh196 | 2022-05-25T16:01:11+00:00
- Closed at: 2022-11-03T21:17:17+00:00
