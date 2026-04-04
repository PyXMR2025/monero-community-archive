---
title: Monero GUI Wallet, Sending Problem (Oxygen Orion)
source_url: https://github.com/monero-project/monero/issues/6885
author: Furiouz84
assignees: []
labels: []
created_at: '2020-10-12T19:46:21+00:00'
updated_at: '2020-10-15T22:35:53+00:00'
type: issue
status: closed
closed_at: '2020-10-15T22:35:53+00:00'
---

# Original Description
Hi guys, 

hopefully some can brighten up my dark world...

I've downloaded a second wallet.
I could send Monero to it. And I did.

But sending Monero from this Wallet says "awaiting confirmation".
And my Monero balance is untouched.
Under transactions it says sended, and To (awaiting transaction).

I've made a simple wallet.
Versions:
Gui version: 0.17.0.1-afc2e84 (Qt 5.9.9)
Monero vers: 0.17.0.1-afc2e846f

On options there is no "Node" since I tried to solve on my own. 

I've verified the hashes before downloading.

Why can I receive, but not send?

Thx in advance

# Discussion History
## selsta | 2020-10-12T19:47:44+00:00
Which wallet mode did you select? Simple mode or advanced mode? You can check inside Settings -> Info.

## Furiouz84 | 2020-10-12T19:48:37+00:00
I made a "Simple" wallet

## selsta | 2020-10-12T19:50:00+00:00
Please follow the instructions here: https://github.com/monero-project/monero-gui/issues/3140#issuecomment-706440354

It is a bug in simple mode, we are working on a fix.

## selsta | 2020-10-14T14:14:18+00:00
Resolved: https://www.getmonero.org/2020/10/14/monero-GUI-0.17.1.0-released.html

# Action History
- Created by: Furiouz84 | 2020-10-12T19:46:21+00:00
- Closed at: 2020-10-15T22:35:53+00:00
