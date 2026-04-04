---
title: sweep_all shows 0 as amount but works.
source_url: https://github.com/monero-project/monero/issues/1135
author: Onefox
assignees: []
labels: []
created_at: '2016-09-25T21:19:43+00:00'
updated_at: '2016-12-15T17:11:51+00:00'
type: issue
status: closed
closed_at: '2016-12-15T17:11:51+00:00'
---

# Original Description
I just used a VM with monero.linux.x86.v0-10-0-0.tar.bz2 on testnet [(iso)](https://www.reddit.com/r/Monero/comments/53ucza/monero_testnet_live/).

And the sweep_all command doesn't show the correct amount that is transferred but its working as it should except of the displayed amount.

See:
![sweep_all](https://cloud.githubusercontent.com/assets/1709259/18818318/70a16c04-8376-11e6-807b-ba11ab349441.PNG)


# Discussion History
## moneromooo-monero | 2016-09-26T10:28:17+00:00
Can you try with set_log 2, and look for "Transaction X/Y:" lines. Do these show non-zero amounts after "sending" ? I think you can post the lines from "Made an attempt at a final", that should not dislcose much private info.
If it does show 0, do you have several lines with "amount=0.002000000000, real_output=2, real_output_in_tx_index=7, indexes:" immediately before those lines, with non zero amounts ?


## moneromooo-monero | 2016-10-15T18:21:04+00:00
https://github.com/monero-project/monero/pull/1224


# Action History
- Created by: Onefox | 2016-09-25T21:19:43+00:00
- Closed at: 2016-12-15T17:11:51+00:00
