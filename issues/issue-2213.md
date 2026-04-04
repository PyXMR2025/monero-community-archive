---
title: 'Monero Seed Node discovery mechanism overhaul. '
source_url: https://github.com/monero-project/monero/issues/2213
author: medusadigital
assignees: []
labels:
- proposal
created_at: '2017-07-27T11:44:11+00:00'
updated_at: '2018-01-19T16:36:48+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
At current state, there is a script which is used to update the Seed Nodes DNS entries, but its unreliable. 

also there is no sanity check from the receiving party, resulting in eventually ending up with an empty list of seed nodes.

The effect of this is that new users are unable to connect to the network. (https://www.reddit.com/r/Monero/comments/6po28q/monero_gui_on_windows_fresh_install_stuck/)


To solve this issue once and for all, the current mechanism of discovering seed nodes should be modified in favour of a more reliable and if possible, more decentralized method

# Discussion History
## Jaqueeee | 2017-08-07T21:34:13+00:00
+proposal

## fluffypony | 2017-08-07T21:55:05+00:00
The mechanism is FINE - the issue is the specifics. Right now we use Gandi's API, which is a bit wonky. I'd like us to do the following:

1. Update the script for local DNS server (bind?) support, as well as CloudFlare's API support.
2. Determine 3 volunteers, beside myself, willing to run servers that populate the 4x default MoneroSeed addresses

## fluffypony | 2017-08-07T21:55:22+00:00
(sorry wrong button, please ignore closing)

## fluffypony | 2018-01-19T16:36:48+00:00
@mrtass we don’t provide support for forks.

# Action History
- Created by: medusadigital | 2017-07-27T11:44:11+00:00
