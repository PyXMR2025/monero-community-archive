---
title: Gui becomes non-responsive when remote node disconnects during synchronization
source_url: https://github.com/monero-project/monero-gui/issues/2000
author: Engelberg
assignees: []
labels:
- resolved
created_at: '2019-03-10T02:24:02+00:00'
updated_at: '2019-07-12T16:18:44+00:00'
type: issue
status: closed
closed_at: '2019-07-12T16:18:44+00:00'
---

# Original Description
I'm using Windows 64-bit gui build 0.14.0.0.

I'm synchronizing a view wallet from scratch from the .keys file, using a remote node that has a tendency to drop out intermittently but comes back within a minute.

When the connection to the remote node is temporarily lost, the gui freezes up.  Even after the remote node is operational again, the gui stays frozen and completely non-responsive..



# Discussion History
## dEBRUYNE-1 | 2019-07-03T17:33:46+00:00
Can you check whether this is still an issue with GUI v0.14.1.0? 

## dEBRUYNE-1 | 2019-07-12T16:05:54+00:00
I am going to close this as (i) the author did not respond and (ii) xiphon addressed a lot of potential freezing issues in GUI v0.14.1.0. 

## dEBRUYNE-1 | 2019-07-12T16:05:58+00:00
+resolved

# Action History
- Created by: Engelberg | 2019-03-10T02:24:02+00:00
- Closed at: 2019-07-12T16:18:44+00:00
