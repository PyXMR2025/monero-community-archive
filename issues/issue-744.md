---
title: 'Minor: add a button to start the daemon immediately '
source_url: https://github.com/monero-project/monero-gui/issues/744
author: fresheneesz
assignees: []
labels: []
created_at: '2017-05-25T18:26:11+00:00'
updated_at: '2017-08-08T00:53:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
At the start, there's a countdown timer that waits to see if you want to use a non-local or non-default daemon. I assume this is there to allow a user maximum privacy in case they don't want to directly connect to the network even for a few seconds. But there should be a button to immediately go in for all those of us who just want to get in and use it in the usual default way.

# Discussion History
## medusadigital | 2017-08-08T00:23:52+00:00
so you mean, next to the, "use custom settings" button, we do a button "start now", so peaople dont need to wait 5 secounds ? 

the "use custom settings" button is there so users can abort the launch, and add more settings afaik.

not sure thats worth it to be honest.

more opinions appreciated

## fresheneesz | 2017-08-08T00:53:49+00:00
I'd say the ideal thing is probably to not connect to the network the first time until the user has a chance to create custom settings. The the rest of the time, just use whatever settings they've used before and automatically connect. 

# Action History
- Created by: fresheneesz | 2017-05-25T18:26:11+00:00
