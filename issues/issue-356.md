---
title: Improving the GUI simple mode UX at time of v19 release
source_url: https://github.com/seraphis-migration/monero/issues/356
author: j-berman
assignees: []
labels:
- upstream
created_at: '2026-05-07T02:19:55+00:00'
updated_at: '2026-05-07T02:19:55+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Last hard fork we received a massive number of support issues around the time of the fork. Even GUI users who updated reported that their wallets were stuck syncing. https://github.com/monero-project/monero/pull/8544 was introduced to improve the problem, but it isn't a perfect solution for GUI simple mode users as described in https://github.com/seraphis-migration/monero/pull/355.

I've spent quite a bit of time digging further into this general problem. I'm commenting on my investigation and thoughts thus far.

_____

When `--bootstrap-daemon-address "auto"` is used to start `monerod` (which the GUI simple modes do in the background), the `monerod` instance will connect to one of the nodes [from its local peerlist with an RPC port advertised](https://github.com/monero-project/monero/blob/cabeafa01a4c4881351259b9e391a92f680eb22d/src/rpc/bootstrap_node_selector.cpp#L91-L96) (via `on_get_public_nodes`) to serve as the "bootstrap" daemon. The bootstrap selector uses some logic to bias [first toward the whitelist peers](https://github.com/monero-project/monero/blob/cabeafa01a4c4881351259b9e391a92f680eb22d/src/rpc/bootstrap_node_selector.cpp#L95), and [second towards peers with fewest connection failures](https://github.com/monero-project/monero/blob/cabeafa01a4c4881351259b9e391a92f680eb22d/src/rpc/bootstrap_node_selector.cpp#L75-L76).

**If I'm a GUI simple mode user and my local node has very few *upgraded* whitelisted peers with RPC ports exposed, then my local node is going to have trouble finding a suitable bootstrap daemon to use, and my GUI is going to have trouble functioning.**

One solution I've been experimenting with on stressnet in addition to https://github.com/seraphis-migration/monero/pull/355 (using my own local `monerod` connected to stressnet): if `monerod` started with `--bootstrap-daemon-address "auto"`, *only* connect to nodes with top supported version == ours. And save a peer's top supported version in the peerlist, then only consider peers with top supported version == ours as a bootstrap candidate in the bootstrap selector logic. Thus, any whitelisted peers with top supported version saved in our peerlist (and RPC port exposed) will immediately be suitable as a bootstrap daemon candidate.

In practice, it's not really performing that much better than this solution is, because there are so few nodes on the stressnet network. It can still end up taking a while to successfully connect to a bootstrap daemon.

The UX is far from ideal still, even with that PR and with the above experimental solution both implemented.

I've mentioned to @selsta that it could make sense to release `monerod` **before** releasing the GUI binaries when the binaries are ultimately released. Then we can give infra operators / the ecosystem time to update in order to increase chances that GUI simple mode users will connect to the upgraded nodes when we release the GUI.

I can also spend more time trying to rework some peer selection logic higher up the stack to make a stronger effort at connecting to nodes with the same highest supported version, and have at least 1 connection with RPC exposed when using bootstrap mode. E.g. peers share peerlists with each peer's top supported version, and `--bootstrap-daemon-address "auto"` daemons can first try to connect to those with top supported version set (and RPC port set).

Alas, I'm pretty confident we're going to see GUI user complaints when v19 releases no matter what. At this point in time, I don't see a perfect way around it. It's a chicken and egg problem: we'll need tons of nodes to update first before releasing the GUI.

_____

Deprecating bootsrapping in favor of the GUI just using a default set of trusted community run nodes to choose from has been floated in the past. With the "spy node" problem (and high fee problem, and just not great reliability), I think there is probably solid reason to do so to protect users. But this bootstrap feature *is* theoretically a nice idea, and I do feel a solid interest in wanting to keep it and try to improve it because it's a more decentralized approach. It's a neat idea in principle.



# Discussion History
# Action History
- Created by: j-berman | 2026-05-07T02:19:55+00:00
