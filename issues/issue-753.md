---
title: 'GUI 2: Sending Monero Via Signed TX file is too abrupt.'
source_url: https://github.com/monero-project/monero-gui/issues/753
author: dontbuymonero
assignees: []
labels:
- enhancement
created_at: '2017-05-31T17:41:00+00:00'
updated_at: '2017-08-07T22:20:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
To spend Monero via offline transaction signing, the steps are as follows: On online machine: select destination address and amount of XMR to be sent, select "create tx file", save tx file, transfer tx file to offline machine. On offline machine: select "sign tx file", save the signed tx file, transfer signed tx file back to online machine. Finally, on online machine, select "submit tx file" and select the signed tx file. The issue is with the last step. Once the user selects "submit tx file", she  is asked to select a file, at which point she selects the signed tx file and clicks "ok". Once this happens, the transaction is immediately broadcast to the network. I find this too abrupt. Once the user selects the signed tx file and clicks ok, a confirmation window should pop up, asking the user if they would like to send the money now. I've used the above method twice to send money, and even after the first, I was still caught off card when the money was immediately sent. I can easily imagine circumstances where a user may submit the tx file while still being somewhat uncertain whether they want to broadcast the tx immediately (or at all, even). Instead of a confirmation window, another option could be that once the user selects the signed tx file, a button appears (or goes from being greyed out to colorful/clickable) that says something like "send your money/tx now". 

# Discussion History
## Jaqueeee | 2017-08-07T22:18:01+00:00
+enhancement

# Action History
- Created by: dontbuymonero | 2017-05-31T17:41:00+00:00
