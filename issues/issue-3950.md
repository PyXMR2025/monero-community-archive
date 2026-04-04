---
title: Change unlocked balance from 10 to 1 blocks via settings
source_url: https://github.com/monero-project/monero/issues/3950
author: krtschmr
assignees: []
labels:
- invalid
created_at: '2018-06-07T05:32:06+00:00'
updated_at: '2018-08-15T11:57:01+00:00'
type: issue
status: closed
closed_at: '2018-08-15T11:57:01+00:00'
---

# Original Description
especially for GUI users who can't send multiple transactions it's really time consuming to send 4x transactions for FFS funding. it takes a total of 34 blocks (>1 hour) to send 4 small donations if the user just have 1 big output.

my proposal would be to keep the **10 blocks as a default** but make it changeable with an argument 
`--blocks-confirmation 10`.

In the GUI it should be a select box in the settings tab.



# Discussion History
## italocoin-project | 2018-06-07T07:27:38+00:00
[09:18] < smooth > the reason it needs to be high is that there is no incentive to ever choose very recent outputs as fake, it can only cause you problems
[09:19] < smooth > so it needs to be high enough that the chance of any reorg is truly negligible

## moneromooo-monero | 2018-08-15T11:17:45+00:00
Changing this locally will harm your privacy.

+invalid


# Action History
- Created by: krtschmr | 2018-06-07T05:32:06+00:00
- Closed at: 2018-08-15T11:57:01+00:00
