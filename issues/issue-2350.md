---
title: 'Unknown Recipient '
source_url: https://github.com/monero-project/monero-gui/issues/2350
author: marianoquilmes
assignees: []
labels:
- invalid
created_at: '2019-08-14T00:13:33+00:00'
updated_at: '2020-02-13T09:27:08+00:00'
type: issue
status: closed
closed_at: '2020-02-13T01:27:44+00:00'
---

# Original Description
Hello I have used an address saved in the address book section to send some funds like I always did and in the address part it says Unknown Recipient even though it was the address saved that I have always used.

Is there a way to claim those funds? 

I do not understand why when I wrote down my password the address went blank.

I have all this info:
tx ID, Address, Payment ID, Tx Key, Tx Note, Rings but no Destinations.

Also de Payment proof is bigger than normal and starts with "Spendproofv19..." instead of "OutProof"

Regards.

Mariano.



# Discussion History
## dEBRUYNE-1 | 2019-08-14T08:05:33+00:00
Which version of the GUI are you using? 

## marianoquilmes | 2019-08-14T13:27:50+00:00
Hello, here is the info:

GUI version: v0.14.0.0 (Qt 5.7.0)
Embedded Monero version: v0.14.0.2
Wallet creation height: 1847322
Wallet mode: Advanced mode

## selsta | 2019-08-14T18:18:09+00:00
Please update to v0.14.1.0 and try again.

## marianoquilmes | 2019-08-14T18:41:44+00:00
Do I have to uninstall the current GUI Version and then install the new one or it can be performed by installing it directly?

## dEBRUYNE-1 | 2019-08-14T19:32:01+00:00
You can find upgrade instructions in this thread:

https://www.reddit.com/r/Monero/comments/c8eg6k/gui_v01410_boron_butterfly_with_ledger_nano_x_and/

## dEBRUYNE-1 | 2019-11-25T08:58:16+00:00
@marianoquilmes - Are you still seeing issues with GUI v0.15.0.1? 

## selsta | 2020-02-13T01:26:09+00:00
Closing due to inactivity and no reply.

+invalid

## rating89us | 2020-02-13T09:27:08+00:00
I guess this is a duplicate of #2008, and it's still an issue. History tab shows "Unknown recipient" in transactions that are still pending, and sometimes the first confirmation takes a lot (>10 min.). This issue will be fixed in the new transaction flow that I'll PR soon.

# Action History
- Created by: marianoquilmes | 2019-08-14T00:13:33+00:00
- Closed at: 2020-02-13T01:27:44+00:00
