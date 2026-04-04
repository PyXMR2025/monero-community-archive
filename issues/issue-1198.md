---
title: Display transaction size (kB) and fee rate (XMR/kB) on Send tab
source_url: https://github.com/monero-project/monero-gui/issues/1198
author: leafcutterant
assignees: []
labels:
- enhancement
created_at: '2018-03-26T16:34:32+00:00'
updated_at: '2020-04-22T21:01:37+00:00'
type: issue
status: closed
closed_at: '2020-04-22T21:01:09+00:00'
---

# Original Description
This is useful information. If it's not possible to include in the ~~fees~~ **Send** tab, at least the confirmation widow could contain them.

# Discussion History
## sanderfoobar | 2018-03-28T23:12:33+00:00
Could #1169 be closed in favor of this issue/feature-request?

## leafcutterant | 2018-03-28T23:57:44+00:00
Sure. I closed it.

Do you think it's possible to add the fee to the list of metrics to display? And could they all go on the Send tab to have a dynamically updating feedback of information?

## sanderfoobar | 2018-03-29T21:28:18+00:00
It's a good idea, but technically possibly complicated to implement. 

We could have Javascript create dummy transactions while the user is filling in the 'Send' form - will have to check the viability of that approach.

## sanderfoobar | 2018-03-29T21:38:24+00:00
+enhancement

## selsta | 2020-04-22T21:01:09+00:00
The fee itself is now displayed. Not transaction size (kB) and fee rate (XMR/kB) but should be good enough for most users.

# Action History
- Created by: leafcutterant | 2018-03-26T16:34:32+00:00
- Closed at: 2020-04-22T21:01:09+00:00
