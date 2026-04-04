---
title: Have node communicate network connection type to wallet
source_url: https://github.com/monero-project/monero/issues/5590
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2019-05-30T22:36:26+00:00'
updated_at: '2019-08-27T15:50:16+00:00'
type: issue
status: closed
closed_at: '2019-08-27T15:50:16+00:00'
---

# Original Description
Monero is on the verge of supporting more network connection types. I believe that a feature that allows the daemon to communicate its connection with the rest of the Monero network to the connected wallets is useful. This is a bit confusing, so I will give some examples below. Note that this would only matter for "trusted" remote or local nodes, not untrusted remote nodes.

### Example 1: I am running a wallet and node on the same device

In this case, my wallet would talk to the daemon locally. I do not need to protect this "connection." However, I want to know my node's connection with the rest of the Monero network, and I trust the feedback I receive from my own node. Thus, the node should tell my wallet if it is connected over Tor, i2p, clearnet dandelion, or clearnet no-dandelion. Other options are available of course.

### Example 2: I am running a node at home and connecting to this custom node while on vacation

In this case, I likewise do not need to protect my connection to the node at my house since I trust the node. However, I want to prevent my home IP from being associated with this transaction. The remote node should send information on the type of network connection it has to the rest of the Monero network.

### Example 3: I am connecting to a random person's node that I do not trust

Since I don't trust this node, I don't trust it to give me accurate network connection information. Likewise, I don't care if the node's IP is leaked to the rest of the Monero network. Thus, I only care about my connection to the remote node. My wallet will ignore any provided network information by an untrusted remote node.

# Requirements

- [x] Set a remote node as "trusted" (trusted daemon option)
- [ ] Have wallets ask trusted daemons for network connection type
- [ ] Have daemons report back a usable connection type (eg: i2p-zero_1.7)
- [ ] Have wallets classify the connection type for trusted daemons as low-risk (Tor, i2p), medium-risk (dandelion), high-risk (clearnet no-dandelion), or unknown (manual or not recognized)
- [ ] Have wallets warn users when sending transactions with high-risk and unknown connections from the daemon to the Monero network
- [ ] Update wallet connection page to include wallet connections to the node (local, remote_untrusted, remote_trusted) and from the node to the network (i2p-zero_1.7, low-risk)

I'm making some assumptions here, and I can clarify things a bit more. Below is the work I was doing to mock up some connection options for the GUI, and I think this feature could be useful to communicate information to the user.

![image](https://user-images.githubusercontent.com/12520755/58669234-1a3e3080-8301-11e9-83d1-c25e56c55c00.png)

# Discussion History
## moneromooo-monero | 2019-05-31T09:11:13+00:00
https://github.com/monero-project/monero/pull/5595 adds the peers' address type to RPC.

## moneromooo-monero | 2019-08-27T15:06:47+00:00
+resolved

(the GUI part can be tracked in the GUI repo)

# Action History
- Created by: SamsungGalaxyPlayer | 2019-05-30T22:36:26+00:00
- Closed at: 2019-08-27T15:50:16+00:00
