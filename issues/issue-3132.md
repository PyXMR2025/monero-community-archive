---
title: 'Bug report: Application icon does not display properly on Ubuntu'
source_url: https://github.com/monero-project/monero-gui/issues/3132
author: viperperidot
assignees: []
labels: []
created_at: '2020-10-06T21:11:02+00:00'
updated_at: '2023-01-18T16:06:25+00:00'
type: issue
status: closed
closed_at: '2023-01-18T16:06:25+00:00'
---

# Original Description
I have installed the latest version of the Monero GUI v0.17.0.1 on Ubuntu version 20.04.1. In the application tray the Monero icon does not display properly. Here is a screenshot of what it looks like: https://imgur.com/PTroRVp

The application does appear correctly on the dock once Monero GUI is launched and running.

I checked the .desktop file and under icon it just says 'monero'. I tried replacing this field with a file path to the Monero logo and that fixed the problem, however once you launch the application any changes made to the .desktop file get overwritten and the application icon does not display properly once again.

Any suggestions on how to fix this would be appreciated, thanks.

# Discussion History
## haluzpav | 2021-11-20T19:30:38+00:00
Yea, I see there were several attempts, starting from #2292, none of them got merged. :disappointed: 

## selsta | 2021-11-21T04:18:57+00:00
@haluzpav https://github.com/monero-project/monero-gui/pull/3251

On first startup it should ask you if you want to install desktop file.

## haluzpav | 2021-11-21T11:59:19+00:00
@selsta Yes, it does, but it shows only a generic icon, as in OP's screenshot. There's no Monero icon under `.local/share/icons/` where the most of other apps put their icons. I have Fedora with Gnome, so maybe it's somehow related to Gnome or its themes, if you believe there should be the icon? However I don't see where could it take the icon from.

## selsta | 2023-01-18T16:06:25+00:00
Continuing in #4006

# Action History
- Created by: viperperidot | 2020-10-06T21:11:02+00:00
- Closed at: 2023-01-18T16:06:25+00:00
