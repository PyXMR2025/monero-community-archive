---
title: Wallet crash on OSX when switching to a different and invalid remote node while
  syncing
source_url: https://github.com/monero-project/monero-gui/issues/804
author: jedigras
assignees: []
labels:
- invalid
created_at: '2017-07-30T05:02:21+00:00'
updated_at: '2018-11-18T16:00:37+00:00'
type: issue
status: closed
closed_at: '2018-11-18T16:00:37+00:00'
---

# Original Description
The GUI wallet crashed when I was syncing using one of my remote nodes.  I decided to try to spin up a windows remote node too and connect to that from the GUI while it was still syncing using the first linux remote node.  It just hung and crashed.  I later realized that the windows node wasn't even accessible remotely as the port was firewalled off.  I guess some more robust error checking or something to disconnect the connected remote node would be nice.

# Discussion History
## medusadigital | 2017-08-08T00:16:51+00:00
i agree on the more robust error checking when connecting, would be a good idea to make that more solid.

what i fear is that this might be the wrong repo, since this is probably something affecting the wallet APi directly, which is part of monero itself.

@Jaqueeee knows the code well, what do you think? 

or any chances its a monero-core related thing ? 

## erciccione | 2018-11-18T13:49:11+00:00
Can be reopened if valid

+invalid

# Action History
- Created by: jedigras | 2017-07-30T05:02:21+00:00
- Closed at: 2018-11-18T16:00:37+00:00
