---
title: Proving maximum outbound connection count to allow selecting inbound peers
  as a dandelion++ stem
source_url: https://github.com/monero-project/research-lab/issues/160
author: Boog900
assignees: []
labels: []
created_at: '2026-05-23T14:08:12+00:00'
updated_at: '2026-05-24T23:52:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Introduction

Monero's network currently has a significant number of "proxy nodes", nodes that do not store their own blockchain and instead forward requests to other nodes [1]. These nodes are assumed to be trying to spy on transaction IP origins. This problem has been known about for over a year. Although some countermeasures have been introduced (ban lists and subnet de-duplication [2]), the spy is still around and has reacted by changing IPs and diversifying across subnets [3].

Proposed solutions so far have either been questionably effective or expensive (or both) [4],[5]. This proposal does not attempt to prevent proxy or spy nodes in any way. The goal is to allow inbound connections to be used for stemming transactions.

A documented issue with dandelion++ is that it only routes stem transactions to outbound connections. This means if you get a stem tx from an inbound node that you can't reach, they most likely created the tx (assuming they are not running a node over Tor). This is an intentional design choice, as it is harder for an adversary to get you to connect to them rather than for them to connect to you, especially as multiple connections are needed to be in with a good chance of getting picked as a stem.

If there was a way to tap into all the unreachable nodes (nodes that only make outbound connections) we would simultaneously fix this privacy leak _and_ increase the size of the stem graph.

We cannot just blindly allow selecting stem nodes from inbound peers. The problems noted in the dandelion paper would make the current network situation a lot worse as now every IP the spy has can make an inbound connection to every reachable node. We need a way to make sure nodes are not making too many connections.

We also should aim to keep the network graph private. The D++ paper discusses the impact of learning the stem graph on privacy, although the network graph is not the stem graph making it public may help the adversary to trace txs.

## Overview

To give a simple explanation of the protocol, it can be broken down into 3 stages. This is not meant to be a complete spec, it's supposed to give a rough idea.

### Identity generation

Firstly, nodes must generate a public and private key to sign messages. Nodes then complete a small PoW puzzle with this public key and their IP. Once the node has completed the PoW it will send the joint PoW solution and the public key to the network. All nodes will verify, propagate and store the public key, PoW and IP.

If 2 different public keys claim the same IP then the PoW should be invalidated, requiring the node at the IP to do it again.

### Proving max connections

To prove maximum connections nodes will generate a Merkle tree over outbound addresses they are currently connected to. The Merkle tree will be restricted to 5 layers allowing 16 outbound connections. Each address is salted with random data before being hashed to prevent nodes from just trying all nodes addresses to find a hash.

The root of this Merkle tree is then signed with the public key and sent to every node in the network.

For the up to 16 nodes the node is currently connected to it will send the salt and tree path for that node's address so that it can reconstruct the root. If the root does not match or the peer does not get a proof it is in the tree then the peer fails and should not be allowed to be stemmed to.

When sending the Merkle tree root to the network a counter will be included. This counter will be incremented on every update, nodes should make sure their address is included in the most recent seen hash. If nodes send 2 Merkle tree roots with the same counter value then their PoW should be invalidated.

### Stem changes

Now when selecting stems we include inbound peers that complete the protocol for 1 of the stem slots but keep 1 as only outbound. So 1 outbound, 1 inbound + outbound. When we receive stem txs we behave the same as we do now, selecting 1 of the 2 for each connection to route all stem txs from them. For local txs only outbound stems should be used, this is to prevent targeted attacks on nodes.

Nodes should not use this protocol for outbound connections, every outbound connection should be in stem selection.

---

## What happens to nodes that fail part of the protocol

Any node which fails part of the protocol should not face any punishment beyond just not being included in the peers to stem to.

## What if an adversary lies about owning an IP they do not

An adversary doing PoW on another node's IP they do not own is an attack pretty impossible to prevent so we try to minimise the impact. By not punishing peers for breaking the protocol beyond not including them for stem, we get a worse case scenario similar to the current situation where nodes with no incoming connections do not get stemmed to.

Nodes under attack in this way should keep doing PoW until the adversary hopefully gives up.

## What are the exact PoW details?

I want to leave this open for now, it could be randomX. We could get nodes to mine blocks for PoW, although the node must mine to an address they don't own, so there is maximum cost for adversaries. It could be 2 minutes of PoW, or it could be an hour.

We could also require that PoW be updated after a certain amount of time and use some sort of cumulative difficulty to make it harder for an adversary to fake being a real node to invalidate PoW.

## What if people don't want their IP to be sent round the network?

The IP you use to connect to nodes in the P2P network is not kept private already. Other nodes can see your address when you connect to them.

We could make the protocol opt-out though.

---

[1]: https://github.com/monero-project/meta/issues/1124
[2]: https://github.com/monero-project/monero/pull/9939
[3]: https://xmrnetscan.redteam.cash/
[4]: https://github.com/monero-project/research-lab/issues/126
[5]: https://vimeo.com/1095371245


# Discussion History
## tevador | 2026-05-23T20:34:21+00:00
> By not punishing peers for breaking the protocol beyond not including them for stem, we get a worse case scenario similar to the current situation where nodes with no incoming connections do not get stemmed to.

I think this is a weakness. The whole network knows when a particular IP has had its identity/PoW invalidated, so any stem transactions coming from that IP during that time can be deduced to originate from that IP.

Another weakness is that unreachable nodes are often behind NAT with a shared external IP, so multiple honest nodes might appear to originate from the same IP, invalidating each other's PoW constantly (although I'm not sure how common it is for honest nodes).

Instead, we could make nodes actively request that their outgoing connection be used for stemming. Such connections will need to provide a PoW equivalent to X solutions per second as long as that connection is marked to be stemmed to. Honest nodes will request 1-2 outgoing connections for stemming. Spy nodes won't have enough CPU power to select all of their outgoing connections for stemming. Honest nodes unable to provide PoW for stemmable connections will still get some plausible deniability for submitted transactions because nobody could be certain that the node doesn't have a stemmable outgoing connection.

## Boog900 | 2026-05-24T11:05:31+00:00
> I think this is a weakness. The whole network knows when a particular IP has had its identity/PoW invalidated, so any stem transactions coming from that IP during that time can be deduced to originate from that IP.

Yeah its not ideal, but this is the current situation now, at least an adversary would have to keep up PoW with this proposal. 

> Another weakness is that unreachable nodes are often behind NAT with a shared external IP, so multiple honest nodes might appear to originate from the same IP, invalidating each other's PoW constantly (although I'm not sure how common it is for honest nodes).

Yeah this is something that would need to be worked out, we could attempt to detect this by connecting to the other node and verifying it is on our IP. We could also print warnings when PoW is invalidated to alert operators.

Both these problems could be completely solved if we used proof of storage to tie a public key to a nodes blockchain. That way 1 blockchain gives you 1 public key, even if behind the same IP.

> Instead, we could make nodes actively request that their outgoing connection be used for stemming. Such connections will need to provide a PoW equivalent to X solutions per second as long as that connection is marked to be stemmed to. Honest nodes will request 1-2 outgoing connections for stemming. Spy nodes won't have enough CPU power to select all of their outgoing connections for stemming. 

This would completely remove the IP requirement, meaning an adversary would just need 1 IP and a mining rig to connect to a lot more nodes than normal peers. PoW per connection would mean that the difficulty would have to be low as otherwise weaker nodes will be excluded, making it easy for an adversary to get an advantage.

> Honest nodes unable to provide PoW for stemmable connections will still get some plausible deniability for submitted transactions because nobody could be certain that the node doesn't have a stemmable outgoing connection.

Although you can't be certain, I think the current network spy could make a good guess by if a node has ever sent a PoW solution to them. If a node has been active for weeks, it would be very unlikely to not see a PoW solution from them. 


## tevador | 2026-05-24T22:41:31+00:00
> Both these problems could be completely solved if we used proof of storage to tie a public key to a nodes blockchain. That way 1 blockchain gives you 1 public key, even if behind the same IP.

Can you cite a proof of storage protocol that can prove one public key per copy of blockchain? The protocol must not allow multiple nodes to generate a valid proof using the same physical copy of the blockchain.

> This would completely remove the IP requirement, meaning an adversary would just need 1 IP and a mining rig to connect to a lot more nodes than normal peers.

Assuming the above mentioned proof of storage protocol exists, wouldn't it have the same issue? Meaning the attacker would need only 1 IP and a few 20 TB hard drives.

> PoW per connection would mean that the difficulty would have to be low as otherwise weaker nodes will be excluded, making it easy for an adversary to get an advantage.

Currently, we use IP addresses as a resource to limit spy node activity. IPv4 addresses cost about $0.5/month.

For PoW, let's take [HashWX](https://github.com/tevador/hashwx), which was designed for client puzzles and can verify a solution much faster than RandomX. It also has an interesting property that old CPUs perform nearly as well as new ones.

I estimate that a last gen AMD Ryzen CPU can do about 25 MH/s at 70 W with undervolting. At $0.03/kWh, that amounts to about $1.5/month, or the equivalent of 3 IP addresses, which would get the attacker 48 stemmable connections. So if we set the hashrate requirement per stemmable connection at 0.5 MH/s, it will roughly match the cost of obtaining an equivalent number of IPv4 addresses.

I'm running a Monero node on a 14 year old dual core Intel CPU that can still do about 1.1 MH/s of HashWX per core, so it should be able to support 1-2 stemmable outgoing connections.


## vtnerd | 2026-05-24T23:52:35+00:00
The alternative proposed by @tevador seems like it would be easier to implement as well. At least at a quick high-level glance - the node only has to keep state per connection instead of some global thing.

# Action History
- Created by: Boog900 | 2026-05-23T14:08:12+00:00
