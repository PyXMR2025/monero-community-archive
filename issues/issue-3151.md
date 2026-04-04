---
title: Cannot open view-only hardware wallet
source_url: https://github.com/monero-project/monero-gui/issues/3151
author: viperperidot
assignees: []
labels: []
created_at: '2020-10-12T05:10:23+00:00'
updated_at: '2022-02-07T07:19:50+00:00'
type: issue
status: closed
closed_at: '2020-10-31T23:51:52+00:00'
---

# Original Description
I created a view-only wallet by clicking the button in the Settings GUI interface. The wallet created successfully yet when I try to open it I get the message: 'Couldn't open wallet: file [view-only wallet file path] does not correspond to [view-only.keys path]'

I am using a Ledger Nano X. Not sure what went wrong but I have tried deleting the view-only wallet and keys and creating again with the same issue happening. 

# Discussion History
## xiphon | 2020-10-12T20:48:17+00:00
Ledger doesn't support creating view-only wallets (yet?).

## viperperidot | 2020-10-12T21:33:21+00:00
Oh really? Ok I didn't know that, because you can make watch-only wallets in Bitcoin using Ledger so they must have not implemented it yet for XMR. I could put a feature request on the Ledger GitHub I suppose but I am pretty sure it's probably already on their list. 

Edit: I was suggested to post this on the Ledger Monero app GitHub so I have made an issue there.

## xiphon | 2020-10-31T23:51:52+00:00
Closed via https://github.com/monero-project/monero-gui/pull/3160

## ksdhans | 2022-02-07T07:19:50+00:00
As posted elsewhere, it looks like extracting the data needed from Ledger is possible:
https://shawnhogan.com/2021/07/how-to-get-monero-private-view-key-from-ledger.html

It would be great if exporting view only wallets for Ledger were added (with appropriate warnings). I know people argue that you shouldn't do it. However, there are situations where it's needed. For example, if you have a payment server (like BTCPay), then it needs the view keys in order to operate. It isn't practical to have the Ledger device permanently plugged in with the Monero app active.

# Action History
- Created by: viperperidot | 2020-10-12T05:10:23+00:00
- Closed at: 2020-10-31T23:51:52+00:00
