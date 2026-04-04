---
title: Make new address generation more user friendly
source_url: https://github.com/monero-project/monero-gui/issues/3570
author: moneromooo-monero
assignees: []
labels: []
created_at: '2021-06-17T16:53:12+00:00'
updated_at: '2021-09-05T21:44:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Filing on request from holeholehole, paraphrased:

When you have lots of addresses, it's not very convenient to scroll all the way down to get a new address. It adds an incentive to reuse an older one.

Also consider auto generating a new one every time the page is displayed, to encourage not reusing addresses between services.


# Discussion History
## MoneroArbo | 2021-06-17T17:09:54+00:00
Possible solutions:

- a toggle to hide used addresses
- a toggle to invert the sort order of addresses

Additionally, it would probably be good to visually differentiate between used and unused addresses, maybe something like an orange tinted backdrop for used addresses.

## rating89us | 2021-06-17T17:12:53+00:00
There is already a preliminary PR for this issue (#2936)

## xanoni | 2021-09-05T21:38:43+00:00
Great, I think this can be closed then?! I came here to submit a similar feature request (option to hide addresses manually).

Edit: duplicate ticket here https://github.com/monero-project/monero-gui/issues/3418

# Action History
- Created by: moneromooo-monero | 2021-06-17T16:53:12+00:00
