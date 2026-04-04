---
title: Show the number of network connections in the GUI
source_url: https://github.com/monero-project/monero-gui/issues/1167
author: leafcutterant
assignees: []
labels: []
created_at: '2018-03-06T15:29:34+00:00'
updated_at: '2018-03-29T23:31:06+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I propose showing the number of inward and outward connections of a node to be displayed somewhere near the network status in the bottom left corner.

For listing connections by IP and further info, there could be a "Network" tab that is similar to what Bitcoin Core has.

# Discussion History
## SamsungGalaxyPlayer | 2018-03-06T18:34:45+00:00
The daemon log can be viewed in the settings tab, including network info. Is this information people typically care about being prominently displayed somewhere? imo it's information most people don't care about, so it's fine to be buried.

## sanderfoobar | 2018-03-29T23:22:46+00:00
@SamsungGalaxyPlayer 

In the situation that there is no internet connectivity (or otherwise not able to make connections), the daemon log will probably let you know. However, I reckon a portion of users will not actually read that and are left wondering why their GUI does not work.

So for debugging/clarity reasons I might be an advocate for such a feature, what do you think?

# Action History
- Created by: leafcutterant | 2018-03-06T15:29:34+00:00
