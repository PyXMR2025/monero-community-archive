---
title: Allow to select public nodes as daemon address in the wizard
source_url: https://github.com/monero-project/monero-gui/issues/121
author: ghost
assignees: []
labels: []
created_at: '2016-11-06T16:18:20+00:00'
updated_at: '2017-04-28T06:52:06+00:00'
type: issue
status: closed
closed_at: '2017-04-28T06:52:06+00:00'
---

# Original Description
Currently the GUI has localhost:18081 as default daemon address. I think the GUI should allow to select public nodes as daemon address. There was already a proposal on Reddit some days ago:

https://www.reddit.com/r/Monero/comments/5aq5y3/open_node_network_expansion_for_gui_release/

With an option to use one of the public nodes the GUI can be used instantly, and the users don't have to wait until the blockchain has been synced. I think this would be for non-experienced users, and for users who want to try out Monero (and the wallet GUI) a great benefit.

The GUI-integrated daemon as proposed in #39 would be still required for users who want not use a public node because of privacy issues.

What do you think about it?

# Discussion History
## moneromooo-monero | 2016-11-06T18:21:52+00:00
It is editable. AFAICT, thisalready works. If you're claiming it does not, say so specifically, and include any errors you get.
Note that using a remote daemon isn't a good idea due to changing RPC anyway. YMMV.


## ghost | 2016-11-06T20:10:07+00:00
The daemon address is already editable in the UI, but the inexperienced user may not know how to use a public node. The idea was to provide an "editable" select input field, where the user can select one of the known public nodes, or enter its own custom address.


## dEBRUYNE-1 | 2016-11-07T11:52:21+00:00
As far as I know this will be part of @Jaqueeee's daemon integration. 


## medusadigital | 2016-11-23T15:33:48+00:00
can this be closed ? or is there something that needs to be done ?

# Action History
- Created by: ghost | 2016-11-06T16:18:20+00:00
- Closed at: 2017-04-28T06:52:06+00:00
