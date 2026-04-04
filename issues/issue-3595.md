---
title: Transaction details reveal despite pressing decline on Trezor
source_url: https://github.com/monero-project/monero-gui/issues/3595
author: maxbiddickk
assignees: []
labels: []
created_at: '2021-06-28T20:18:56+00:00'
updated_at: '2021-06-29T11:05:04+00:00'
type: issue
status: closed
closed_at: '2021-06-28T20:53:50+00:00'
---

# Original Description
Transaction details reveal despite pressing decline on Trezor

# Discussion History
## rating89us | 2021-06-28T20:51:47+00:00
It is expected behavior.

When you are on Transactions page and click on transaction details button, a export tx_key dialog will display on your Trezor. If you decline it, your trezor device will not export the tx key of this transaction to your computer.

The transaction details popup will always open and display the transaction details that are available to the wallet. If you decline exporting the tx key, only this information will not be displayed. The remaining transaction details are not imported from your hardware wallet device, and therefore are displayed.

## selsta | 2021-06-28T20:53:50+00:00
Closing as it seems working as intended.

@maxbiddickk please comment if you have more questions

## maxbiddickk | 2021-06-29T11:05:03+00:00
Very cool ! My first post on GitHub. Happy to be involved even if some what unnecessarily 🤣 sorry to waste anybody’s time !

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: selsta ***@***.***>
Sent: Monday, June 28, 2021 9:53:59 PM
To: monero-project/monero-gui ***@***.***>
Cc: maxbiddickk ***@***.***>; Mention ***@***.***>
Subject: Re: [monero-project/monero-gui] Transaction details reveal despite pressing decline on Trezor (#3595)


Closing as it seems working as intended.

@maxbiddickk<https://github.com/maxbiddickk> please comment if you have more questions

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero-gui/issues/3595#issuecomment-870033957>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AIBK3IYSCHPXH4YIRQVWL6DTVDOOPANCNFSM47OVJUVA>.


# Action History
- Created by: maxbiddickk | 2021-06-28T20:18:56+00:00
- Closed at: 2021-06-28T20:53:50+00:00
