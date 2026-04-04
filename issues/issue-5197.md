---
title: ' Can not forwarding 18080 port  '
source_url: https://github.com/monero-project/monero/issues/5197
author: maogo
assignees: []
labels: []
created_at: '2019-02-25T09:24:20+00:00'
updated_at: '2019-07-24T03:15:17+00:00'
type: issue
status: closed
closed_at: '2019-03-21T14:41:52+00:00'
---

# Original Description
No description

# Discussion History
## jindouyunz | 2019-02-25T09:28:40+00:00
Anyone helps? it's a common issue in China, preventing people to run full node here, appreciate much.

## moneromooo-monero | 2019-02-25T10:49:20+00:00
If I understand correctly, the issue is that connections from the outside to your home network are impossible due to your home network not being addressable from the outside. Is that correct ?

If so, then a mitigation could be to have part of the outgoing connections jump from host to host till they find some which are not synced yet. This will ensure the "hidden" node is as useful as possible to the network in terms of serving blockchain data.



## moneromooo-monero | 2019-02-25T13:11:15+00:00
If you want to connect to it from the outside (ie, from a wallet), then you'd need some ssh magic.

If you want your node to contribute to the network by supplying historical blockchain, then currently it will kind of work on and off, if you're connecting to syncing nodes, but the change I suggested above (which requires code changes) would work for this.


## moneromooo-monero | 2019-02-26T12:49:23+00:00
https://github.com/monero-project/monero/pull/5199 adds those code changes I mentioned above.

## moneromooo-monero | 2019-03-21T14:36:31+00:00
#5199 is now merged.

For external wallet access (eg, phone wallet to home node), you can either use the Tor proxy that was added recently (see ANONYMITY_NETWORKS.md for details). Otherwise, some ssh reverse setup.

So I'll call it fixed.

+resolved


# Action History
- Created by: maogo | 2019-02-25T09:24:20+00:00
- Closed at: 2019-03-21T14:41:52+00:00
