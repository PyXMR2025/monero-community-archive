---
title: Monero Configuration File for GUI wallet
source_url: https://github.com/monero-project/monero-gui/issues/3104
author: skaiaswiss
assignees: []
labels: []
created_at: '2020-09-22T19:43:05+00:00'
updated_at: '2020-10-04T22:39:29+00:00'
type: issue
status: closed
closed_at: '2020-10-04T22:39:29+00:00'
---

# Original Description
Hello Monero devs!
I am trying to send arguments to Monero GUI using .appimage file but I just figured that the GUI wallet can't receive arguments like config file as per following page https://monerodocs.org/interacting/monero-config-file/
Why it's not possible? I think it should be really a good thing if we could start the GUI sending arguments. Specially the config file one because more and more users are using Monero on a standalone USB key. In my case I use my own remote node and every time I use my USB key and Monero GUI wallet on a new computer, I lose my remote node settings because they are not stored in the USB key.
Thanks for all your hard work guys. Regards.

# Discussion History
## xiphon | 2020-09-24T00:02:22+00:00
> more and more users are using Monero on a standalone USB key

https://github.com/monero-project/monero-gui/pull/3026 - already implemented portable mode, related code needs some minor tweaks and will be merged *soon*.

# Action History
- Created by: skaiaswiss | 2020-09-22T19:43:05+00:00
- Closed at: 2020-10-04T22:39:29+00:00
