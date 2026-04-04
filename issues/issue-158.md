---
title: Ringsize slider giving different values
source_url: https://github.com/monero-project/monero-gui/issues/158
author: ghost
assignees: []
labels:
- duplicate
created_at: '2016-11-13T04:02:40+00:00'
updated_at: '2017-12-13T13:09:15+00:00'
type: issue
status: closed
closed_at: '2017-12-13T13:09:15+00:00'
---

# Original Description
See this video (11:29) https://youtu.be/-n5azwzhwiA?t=11m29s

At the start of the video the Medium setting gives a mixin of 8. Then at 12m11s (about 40 seconds later) I use the same Medium privacy setting yet the confirmation popup shows a mixin of 7.

# Discussion History
## moneromooo-monero | 2016-11-13T10:00:14+00:00
AFAICT, you just moved the slider just before. So.. it works ?


## medusadigital | 2016-11-13T14:53:05+00:00
it works basically as designed, but it can "snap" everywhere. 

so its porssible to basically produce something like this: 

![sliderpixel](https://cloud.githubusercontent.com/assets/17108301/20246541/019303cc-a9b9-11e6-877f-5fe30497ea1f.png)

the issue seems that it can snap at the start of a zone, and also at its end, the difference being one pixel.

we should only allow snapping at the end of each zone


## moneromooo-monero | 2016-11-18T19:21:05+00:00
or in the middle :D


## medusadigital | 2017-08-07T20:06:03+00:00
so what would be the prefered behaviour ? 

to me personally it seems good enough. 

## dEBRUYNE-1 | 2017-12-13T10:56:30+00:00
Closing this in favor of #863.

+duplicate

# Action History
- Created by: ghost | 2016-11-13T04:02:40+00:00
- Closed at: 2017-12-13T13:09:15+00:00
