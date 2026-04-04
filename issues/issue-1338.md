---
title: Limit P2P system to just 2-3 connections to the same IPv4 address
source_url: https://github.com/monero-project/monero/issues/1338
author: ghost
assignees: []
labels: []
created_at: '2016-11-13T15:56:10+00:00'
updated_at: '2017-02-24T06:06:54+00:00'
type: issue
status: closed
closed_at: '2017-02-24T06:06:54+00:00'
---

# Original Description
Is this possible to at least make it a little more difficult to drown out the network by spawning endless spoof nodes requiring sync data?

# Discussion History
## moneromooo-monero | 2016-11-13T21:05:50+00:00
No. Feel free to add it. Also a lesser anti-preference for hosts on the same subnet would be useful.


## ghost | 2016-11-14T07:49:56+00:00
That would require a dynamic peer risk stratification/scoring system, which would be nice but sadly beyond my experience. 


## moneromooo-monero | 2016-11-14T11:12:28+00:00
Doesn't need to be super complex to start with.

New peers we connect to: see make_new_connection_from_peerlist
This picks a random peer: get_random_index_with_fixed_probability
Then a few tests for suitability: is_peer_used, is_remote_ip_allowed, is_addr_recently_failed
Then connects: try_to_connect_and_handshake_with_new_peer
All that is in src/p2p_net_node.inl

A simple way would be to add another suitability test: check the randomly selected IP is not in the same subnet has another one. Or the randonm selection could first partition known IPs in "same subnet as an current connection" and "others", and always pick from others unless it's empty.


## anonimal | 2017-01-14T15:25:59+00:00
As noted in #1572, will this effect Tor users (more than 3 connections from 1 exit node)?

# Action History
- Created by: ghost | 2016-11-13T15:56:10+00:00
- Closed at: 2017-02-24T06:06:54+00:00
