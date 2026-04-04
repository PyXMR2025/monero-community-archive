---
title: 'Balance on GUI Walle not updating '
source_url: https://github.com/monero-project/monero-gui/issues/4202
author: orte9011
assignees: []
labels: []
created_at: '2023-07-30T02:07:21+00:00'
updated_at: '2023-07-30T13:34:42+00:00'
type: issue
status: closed
closed_at: '2023-07-30T13:34:42+00:00'
---

# Original Description
Transaction ID 
2a65feb14b1c99da0b1caab67210a70e460deef565a1e3c7c52d1706dc3f5baf

GUI
0.18.2.2-unknown (Qt 5.15.8

Wallet mode: Simpled mode 
Wallet Height 2500000

I have tried changing height , renaming wallet name 

Nothing works 

To update the balance with the last transactions , first transaction on this wallet 

Network status shows connected

Please help 

# Discussion History
## selsta | 2023-07-30T02:12:59+00:00
Try to use advanced mode and set a custom remote node. You can go to the main menu by clicking on the exit symbol in the top left corner.

Then click on "Change wallet mode" and select "Advanced mode". Afterwards open your wallet again, go to Settings -> Node, select "Remote node" and enter the following node:

address: `selsta2.featherwallet.net`
port: `18081`

This should resolve your issue for now. No extra hard disk space required and no issues with monerod not starting.

----------

Other remote node in case the above has issues:

address: `selsta1.featherwallet.net `
port: `18081`

address: `node.community.rino.io`
port: `18081`

More nodes: nodes.monero.com

After that try to change the height again and do a full rescan. If you still have issues afterwards I will give you further steps.

## orte9011 | 2023-07-30T05:08:19+00:00
Hi Selsta :

Thanks for your prompt reply. I have tried two different nodes and restarted the wallet changing the size but did not work.
Can you please send me further steps 

![image](https://github.com/monero-project/monero-gui/assets/140928545/48ec57c0-183e-4dd3-8def-af415da7eaa5)



## orte9011 | 2023-07-30T07:48:37+00:00
Thanks my balance finally updated 

## orte9011 | 2023-07-30T09:10:46+00:00
Hi I scan the transactions and I can see the balance but I can't send funds, Are you able to give me a hand? please 

## selsta | 2023-07-30T11:56:34+00:00
What happens when you try to send the funds?

## orte9011 | 2023-07-30T12:42:09+00:00
I was getting failed , not sure why . But finally I transferred funds successfully.Thanks for your help Sent from my iPhoneOn 30 Jul 2023, at 21:56, selsta ***@***.***> wrote:﻿
What happens when you try to send the funds?

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you modified the open/close state.Message ID: ***@***.***>

## selsta | 2023-07-30T13:34:42+00:00
Glad to hear that you were able to send your funds. If you continue to have issues please open a new issue.

# Action History
- Created by: orte9011 | 2023-07-30T02:07:21+00:00
- Closed at: 2023-07-30T13:34:42+00:00
