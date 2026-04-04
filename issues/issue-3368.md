---
title: 'Gui wallet crashing while sending transaction '
source_url: https://github.com/monero-project/monero-gui/issues/3368
author: hopi369
assignees: []
labels: []
created_at: '2021-03-26T09:13:33+00:00'
updated_at: '2021-03-27T19:35:41+00:00'
type: issue
status: closed
closed_at: '2021-03-27T19:35:41+00:00'
---

# Original Description
Hey guys,

I hope you are doing good.  When trying to send transactions from my Gui wallet the app crashes.  I've tried to change public node and it still does not work.  Could anyone help me with this?  Also tried to restore my wallet from Trezor hardware device and for some reason that is not working either.

Looking forward to hearing from you

# Discussion History
## selsta | 2021-03-26T11:44:38+00:00
Are you using the latest Trezor firmware and latest version of Trezor bridge?

Do you have any other (non Monero) Trezor wallets open?

## hopi369 | 2021-03-26T14:03:55+00:00
 did have a different wallet up  as well, thanks a lot it worked!

## selsta | 2021-03-27T19:35:41+00:00
Ok, this will be fixed in the next release so that having a different wallet open should not result in a crash anymore.

# Action History
- Created by: hopi369 | 2021-03-26T09:13:33+00:00
- Closed at: 2021-03-27T19:35:41+00:00
