---
title: Do not automatically start a local node when connection to remote node failed.
source_url: https://github.com/monero-project/monero-gui/issues/2456
author: tobtoht
assignees: []
labels: []
created_at: '2019-11-23T17:40:37+00:00'
updated_at: '2019-12-20T00:36:31+00:00'
type: issue
status: closed
closed_at: '2019-12-20T00:36:31+00:00'
---

# Original Description
Especially on Tails, as running a local node will not work without additional setup. 

User choice to use a remote node should be respected. The 10 second countdown is anxiety inducing. Instead, let the user know that the connection to the remote node failed.

# Discussion History
## selsta | 2019-11-23T17:46:16+00:00
Can you post steps to reproduce? This does not happen on my system.

> The 10 second countdown is anxiety inducing.

Yea this should be improved.


## tobtoht | 2019-11-23T17:51:02+00:00
Create a new wallet with advanced mode.
Select "Connect to a remote node".
Enter an offline (or nonexistent) remote node.
Go to Settings -> Node, hit Connect (with the offline node still entered)
Wait 30 seconds. The starting local node countdown will pop-up.

# Action History
- Created by: tobtoht | 2019-11-23T17:40:37+00:00
- Closed at: 2019-12-20T00:36:31+00:00
