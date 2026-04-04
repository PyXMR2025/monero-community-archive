---
title: monero snap not published in the Ubuntu Store
source_url: https://github.com/monero-project/monero/issues/1532
author: come-maiz
assignees: []
labels:
- proposal
created_at: '2017-01-06T20:14:47+00:00'
updated_at: '2021-10-06T03:24:43+00:00'
type: issue
status: closed
closed_at: '2021-10-06T03:24:42+00:00'
---

# Original Description
I see that you already have everything ready to build a snap package:
https://github.com/monero-project/monero/blob/master/snapcraft.yaml

However, it is not yet published to the Ubuntu store. It would be great to push it to the edge channel, so early adopters can start testing it. It will also be nice to expose monero to all the Ubuntu users.

The first step is to register the name:
https://myapps.developer.ubuntu.com/dev/click-apps/register-name/

Then you can build the snap in Ubuntu 16.04 with:

    $ sudo apt install git snapcraft
    $ git clone https://github.com/monero-project/monero
    $ cd monero
    $ snapcraft

And you can push the snap to the edge channel with:

    $ snapcraft push monero_0_amd64.snap --release edge

I'd be happy to help you getting it tested. If you have any questions about snaps, please let me know.

# Discussion History
## dEBRUYNE-1 | 2018-01-08T12:36:32+00:00
+proposal

## selsta | 2021-10-06T03:24:42+00:00
We removed the snap package again as it wasn't actively maintained. Closing this.

# Action History
- Created by: come-maiz | 2017-01-06T20:14:47+00:00
- Closed at: 2021-10-06T03:24:42+00:00
