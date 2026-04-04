---
title: Change developer donation from percentage of fee to absolute amount
source_url: https://github.com/monero-project/monero-gui/issues/656
author: ghost
assignees: []
labels:
- invalid
created_at: '2017-04-01T23:51:36+00:00'
updated_at: '2018-12-17T12:27:26+00:00'
type: issue
status: closed
closed_at: '2018-12-17T12:27:26+00:00'
---

# Original Description
I see problems ahead when someone sends a high priority (x166) transaction, yet keeps developer donations on at say 50%, thereby actually sending x166 + x83 = x249 of the original transaction.

If instead an absolute value was used for the donation (e.g. 0.005XMR), with a pre-set maximum donation (e.g. 0.1XMR) to visibly demonstrate the developers aren't just rent-seeking, I believe we would end up with a safer UX.

# Discussion History
## leafcutterant | 2018-03-06T15:52:09+00:00
@NanoAkron, excuse me, but what is "developer donation"? Do you say that this wallet has a built-in donation tap like MultiBit HD that sends an extra amount to developers after every transaction?

## mmbyday | 2018-12-17T09:12:40+00:00
+invalid
This % based donation behavior doesn't exist. afaik.

## dEBRUYNE-1 | 2018-12-17T11:50:52+00:00
I am going to close this as adding an additional output to the transaction (that would go to the donation fund) is detrimental to privacy. More information can be found here:

https://weuse.cash/2018/01/18/you-shouldnt-use-xwallet-if-you-care-about-your-privacy/

Note that Xwallet has since then fixed this particular behavior in their wallet. 

## dEBRUYNE-1 | 2018-12-17T11:50:57+00:00
+invalid

# Action History
- Created by: ghost | 2017-04-01T23:51:36+00:00
- Closed at: 2018-12-17T12:27:26+00:00
