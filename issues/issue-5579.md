---
title: size in blob 6048 not have not zero modulo for sizeof(value_type) = 30
source_url: https://github.com/monero-project/monero/issues/5579
author: myaeon-ru
assignees: []
labels: []
created_at: '2019-05-28T12:48:24+00:00'
updated_at: '2020-05-16T16:27:29+00:00'
type: issue
status: closed
closed_at: '2020-05-16T16:27:29+00:00'
---

# Original Description
./monerod --version
Monero 'Boron Butterfly' (v0.14.1.0-7973fb6a)

2019-05-28 12:20:55.475	[P2P1]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1364	Synced 1844517/1844517
2019-05-28 12:20:55.475	[P2P1]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2021	SYNCHRONIZED OK
**2019-05-28 12:22:02.678	[P2P6]	ERROR	default	contrib/epee/include/serialization/keyvalue_serialization_overloads.h:164	size in blob 6048 not have not zero modulo for sizeof(value_type) = 30, type N8nodetool19peerlist_entry_baseINS_19network_address_oldEEE**

Is this error? And what actual release of monero at now moment should be used?! if last release was
Latest release
 v0.14.0.2
 6cadbdc
Boron Butterfly, Minor Point Release 0.2
@fluffypony fluffypony released this on 8 Mar · 1501 commits to master since this release





# Discussion History
## moneromooo-monero | 2019-05-28T13:45:43+00:00
This error can be ignored. You can't talk with another peer, there was a comms change which did not keep backward compat here. This will go away once all/most nodes have updated.
You are using the right version.

## moneromooo-monero | 2020-05-16T16:27:29+00:00
Innocuous.

# Action History
- Created by: myaeon-ru | 2019-05-28T12:48:24+00:00
- Closed at: 2020-05-16T16:27:29+00:00
