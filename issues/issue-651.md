---
title: User guide still refers to "mixin" (deprecated, right?)
source_url: https://github.com/monero-project/monero-site/issues/651
author: ordtrogen
assignees: []
labels: []
created_at: '2018-03-16T11:26:27+00:00'
updated_at: '2018-04-09T21:10:32+00:00'
type: issue
status: closed
closed_at: '2018-04-09T21:10:32+00:00'
---

# Original Description
On

https://getmonero.org/resources/user-guides/monero-wallet-cli.html

the transfer command is described as 
"transfer MIXIN ADDRESS AMOUNT"
but as I understand "mixin" is now called "ring size" since 0.11?

I don't know if it's enough to just s/mixin/ring size on the page.


# Discussion History
## erciccione | 2018-03-16T13:48:50+00:00
ring size = mixin + 1
So yeah, it definitely needs to be corrected. Thanks for spotting it, i guess all user guides need to be reviewed, we got some massive updates lately

## erciccione | 2018-04-09T16:30:53+00:00
Will be fixed with #678 

+in progress

# Action History
- Created by: ordtrogen | 2018-03-16T11:26:27+00:00
- Closed at: 2018-04-09T21:10:32+00:00
