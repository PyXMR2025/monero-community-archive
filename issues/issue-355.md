---
title: Balance too wide for large amount, some digits hidden
source_url: https://github.com/monero-project/monero-gui/issues/355
author: peanutsformonkeys
assignees: []
labels: []
created_at: '2016-12-24T05:35:55+00:00'
updated_at: '2017-01-09T00:54:51+00:00'
type: issue
status: closed
closed_at: '2017-01-09T00:54:51+00:00'
---

# Original Description
For wallets with more than 100 (?) or 1000 XMR, the last few decimal digit(s) are not displayed. E.g. a watch-only wallet of the Monero donation address currently shows 6689.443118226450 as "Unlocked balance", but the Balance chops of the "50" at the end.

<img width="1003" alt="monero-project-donation-balance" src="https://cloud.githubusercontent.com/assets/21346321/21465397/337f0878-c9a2-11e6-926c-d8326a9014b3.png">

The larger font size for "Balance" is causing this. Maybe the font size could be somewhat dynamic, based on the number of digits to be displayed, but I think calculating that probably wouldn't be easy.

# Discussion History
## medusadigital | 2016-12-24T09:52:20+00:00
somehow related, since we have similar effects in TRX History https://github.com/monero-project/monero-core/issues/179

We had Issues with the rendering back in the days, thats why there is no dynamic font size AFAIK.
Now that the rendering issues are solved we can maybe take a 2nd try.

How the solution should look in detail needs to be discussed. 

# Action History
- Created by: peanutsformonkeys | 2016-12-24T05:35:55+00:00
- Closed at: 2017-01-09T00:54:51+00:00
