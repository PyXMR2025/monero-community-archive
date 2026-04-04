---
title: 'Discussion: preventing P2P proxy nodes.'
source_url: https://github.com/monero-project/research-lab/issues/126
author: Boog900
assignees: []
labels: []
created_at: '2024-10-31T18:58:07+00:00'
updated_at: '2025-08-11T22:20:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Background

While investigating this issue: https://github.com/monero-project/monero/issues/9496 I noticed in one of the log snippets posted that a peer sent a message that wouldn't normally be sent if both nodes were running default `monerod` https://github.com/monero-project/monero/issues/9496#issuecomment-2394738955:

```
2024-10-04 22:14:12.000 I [162.218.65.219:11095 INC] 227 bytes received for category command-1001 initiated by peer
2024-10-04 22:14:12.001 I [162.218.65.219:11095 INC] 10 bytes sent for category command-1007 initiated by us
2024-10-04 22:14:12.002 I [162.218.65.219:11095 INC] 15520 bytes sent for category command-1001 initiated by us
```

Command `1001` is a handshake request & response. Command `1007` is a [support flag request & response](https://github.com/monero-project/monero/blob/master/docs/LEVIN_PROTOCOL.md#1007-request-support-flags). Support flags are contained in the handshake message, currently the only flag is for fluffy blocks, `monerod` will always activate this flag, even if you enable the `no_fluffy_blocks` arg (it will only disable _sending_ fluffy blocks).  

Support flag requests are only sent if you leave the support flags in the handshake empty, so `162.218.65.219` either compiled their own `monerod` unsetting the fluffy blocks support flag or, more likely, they are running completely custom software.

I tried to find all the nodes displaying this behavior but sadly when I connected to this node it had the fluffy blocks support flag set. Knowing that they are probably running custom software I decided to try find another difference in behavior from `monerod`, and luckily I managed to find one. I am going to keep the exact method private to prevent them fixing it. The method will not give false positives, `monerod` would never do what these nodes do. I am certain these nodes are proxies to real nodes.

Scanning the network for this behavior I found 1900 IP addresses running these bad nodes: https://github.com/Boog900/monero-ban-list/blob/main/ban_list.txt, the majority were from these 6 subnets:

```
91.198.115.0/24
100.42.27.0/24
162.218.65.0/24
193.142.4.0/24
199.116.84.0/24
209.222.252.0/24
``` 

Which overlaps with LinkingLions: https://b10c.me/observations/06-linkinglion/. 

In total while scanning the network I found around 4900 active IP addresses, which is less than half the count of nodes on https://monero.fail/map (currently 12941). I decided to run monero.fail's tool myself, with a slight modification to check nodes are reachable before adding them to the list. With this tool I got 10175 "Recent Peers". monero.fail counts the same IP running nodes on different ports as different peers, which is fine, but it explains the difference in the count.

The spy nodes run multiple proxies behind the same IP, in the list of 10175 IP:Port combinations the amount of nodes with an IP in the 6 main subnets + some `23.92.36.*` that the proxies use is 7584.

This means from the data I have it looks like ~40% of the IPs running Monero nodes are not real nodes and ~75% of the "Recent Peers" from my scan using monero.fails tool were from an IP in the 6 main subnets + some 23.92.36.* that the proxy nodes were using.

Having such a large chunk of the network, each tx sent over clearnet is highly likely to be rooted through one of their nodes at least once in the stem stage. Allowing them to hold onto it and use one of the few information leaks from `monerod` to try and find the peers in the stem path before it, example: https://github.com/monero-project/monero/issues/9496#issuecomment-2395469805. Even if a node does not accept incoming connections they are still highly likely to be connected to at least one node ran by this entity which can be used to exploit an information leak.

With the amount of nodes ran by this entity IMO network security is also an issue. 

## Ideas 

### Banning these IP addresses

Banning the IP addresses is a good solution for individual nodes, however not all nodes will do it and they could just switch IPs.

### Hardening the addressbook

Although currently `monerod` prefers to connect to peers in different /16 subnets, the addressbook does not limit the amount of peers stored per subnets, it will even store the same IP with different ports also it could store IPv6 mapped IPv4 addresses, and the canonical IPv4 address at the same time in different entries.

We could limit the amount of address stored per subnet, like bitcoin, and prevent the same IP from being stored multiple times.
Although these nodes could still be active they would be less likely to be connected to.

### Proof of Storage

There are schemes for proving that a node is storing the blockchain: https://ieeexplore.ieee.org/document/10174897 although this would require "encrypting" the blockchain, which isn't ideal.


# Discussion History
## SyntheticBird45 | 2024-10-31T19:15:51+00:00
At the same time, I've been investigating these IPs on auxiliary channels and I'm able to attest these are all exhibiting signs of running the exact same software. I've (with also the contribution of plowsof) been able to identify other methods to detect them, which are going to stay private but can be shared to other trusted MRL members.

## RB90909 | 2024-10-31T21:33:28+00:00
Can this help ? https://github.com/monero-project/monero/pull/7935 ; we need to add this to have more diverse peer connectivity 

## Rucknium | 2024-11-06T16:37:08+00:00
**TL;DR: An analysis of node log data provides further supporting evidence that the IP addresses on the banlist are controlled by an eavesdropping adversary. At any given time, an average of 15 percent of outbound connections of the honest logging nodes were made to IP addresses on the banlist, which reduced the effectiveness of the Dandelion++ privacy protocol.**

I used fluff-phase transaction relay log data to analyze peer-to-peer connections from honest nodes to IP addresses on the banlist: https://github.com/Boog900/monero-ban-list/blob/main/ban_list.txt

The log data was collected from about ten nodes between April 14, 2024 and May 23, 2024. The data is described in Section 9 of my ["March 2024 Suspected Black Marble Flooding Against Monero: Privacy, User Experience, and Countermeasures"](https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-flood.pdf). 

## IPs on banlist do not initiate connections (consistent with optimal attack strategy against Dandelion++)

IP addresses in the banlist make up about 11 percent of all 13,600 unique node IP addresses in the dataset. For outbound connections only, IP addresses in the banlist make up about 25 percent of all 6,200 unique node IP addresses. For outbound connections only and counting each port as a distinct node, IP addresses in the banlist make up about 50 percent of all 9,400 distinct nodes.

The banlist IP addresses almost never initiate connections. They only wait for honest nodes to establish outbound connections to them. Only a single IP address on the banlist appeared as an inbound connection to the logging nodes.

Outbound connections are the privacy-sensitive connection type. Dandelion++ relays stem-phase transactions to outbound connections only. The Dandelion++ threat model in Fanti et al. (2018) assumes that

> Spies can generate as many outbound edges as they want, to whichever nodes they choose; however, they cannot force honest nodes to create outbound edges to spies.

and

> Dandelion is naturally robust to nodes that create a disproportionate number of edges, because spies can only create outbound edges to honest nodes. This matters because in the stem phase, honest nodes only forward messages on outbound edges.

The operator of the banlist IP addresses is encouraging honest nodes to establish outbound connections to the malicious proxy nodes. When honest nodes have many outbound connections to spy nodes, the privacy protections of Dandelion++ do not work very well. Outbound connections are the only type of connections that a node with closed ports can have, so closed-port nodes are at higher risk of eclipse attacks in this circumstance.

## Banlist IP addresses within the`/24` subnet ranges "saturate" their subnets

The banlist includes six IP address ranges. These IP address ranges include 254 unique IP addresses in their ranges, from `xxx.xxx.xxx.1` to `xxx.xxx.xxx.254`. For each of the six subnets, between 240 and 254 unique IP addressees appear in my dataset. This subnet saturation suggests that a single entity controls every IP address in the subnet and the entity uses the IP addresses to accept connections from honest peer nodes.

Besides the IP addresses on the banlist, the greatest subset saturation in the dataset was `49.12.239.0/24` with about 30 unique IP addresses. This subnet is associated with a Hetzner Autonomous System Network (ASN), which leases servers to companies and individuals. The banlist IP address ranges are probably malicious, given that similar saturation behavior is not observed for any other IP address ranges.

## Empirical privacy impact

The share, $p$, of an honest node's outbound connections that are made to spy nodes determines the honest node's privacy risk at any given time. Higher $p$ means greater privacy risk.

The dataset contains data on the duration of each logging node's connection to peers. (The data is actually a log of fluff-phase transactions received from peer nodes, but the first and last time receiving transactions from a node is roughly the same as the duration of the connection.)

Some of the logging node operators apparently already manually enabled a banlist that prevented connections to most of the IP addresses on @Boog900 's banlist. Data from these logging nodes was excluded from the following analysis. The share of malicious nodes in the logging nodes' outbound connections at any given time can be weighted by the duration of each connection to produce a $p$ for an average period of time.

The weighted average $p$ of the logging nodes was about 0.15, much less than the 25 percent share of distinct IP addresses on the banlist (if using the unique IP address metric) and the 50 percent share of distinct nodes (if using the distinct IP/port combination metric). Possible reasons for the discrepancy are discussed in the next section.

How much of a threat to privacy do these suspected spy proxy nodes pose to users? The Dandelion++ paper (Fanti et al. 2018) choose recall and precision to measure the privacy of the protocol:

> As discussed in [Venkatakrishnan, Fanti & Viswanath (2017)], precision and recall are a superset of the metrics typically studied in this space; in particular, recall is equivalent (in expectation) to probability of detection. On the other hand, _precision_ can be interpreted as a measure of a node’s plausible deniability; the more transactions get mapped to a single node, the lower the adversary’s precision.

Recall and precision have these definitions in terms of true positives, false positives, and false negatives:

`recall = true_positives / (true_positives + false_negative)`

`precision = true_positives / (true_positives + false_positives)`

Venkatakrishnan, Fanti & Viswanath (2017) prove that the lowest recall and precision that any clearnet transaction relay protocol can achieve is $p$ and $p^2$, respectively. Fanti et al. (2018) prove that the Dandelion++ protocol can achieve the $p$ lower bound on recall and nearly achieve the $p^2$ lower bound on precision in realistic circumstances.

Assuming the IP addresses on the banlist are malicious spy nodes controlled by a single adversary, the mean recall and precision that the adversary achieved would be approximately the empirical mean of $p$ and $p^2$, respectively. The weighted average $p$ was already estimated to be 0.15 above. Due to [Jensen's inequality](https://en.wikipedia.org/wiki/Jensen's_inequality) the mean of $p^2$ is _not_ $0.15^2 = 0.023$, but a [Riemann–Stieltjes integral](https://en.wikipedia.org/wiki/Riemann%E2%80%93Stieltjes_integral) of the weighted empirical cumulative distribution function (WECDF) of $p$ can be used instead. Integrating $f(x) = x^2$ with respect to the WECDF gives an estimated mean precision of 0.035.

## Share of outbound connections to malicious nodes is lower than the share of malicious nodes on the network

In the previous section I noted that the share of outbound connections that logging nodes made to the banlist IP address is lower than the share of banlist IP address on the network. At least two factors could explain the discrepancy.

First, connections to banlist IP addresses are about 25 percent shorter in time duration than connections to IP addresses that are not on the banlist. The shorter connection durations would mean less weight is given to banlist IP addresses in the weighted mean of $p$.

Second, [Monero nodes prefer to connect to nodes that are not within the same `/16` IP address ranges](https://libera.monerologs.net/monero/20241020#c448210). Since most of the banlist IP addresses are in just six `/24` ranges (which are a strict subset of `/16` ranges), a Monero node that is already connected to an IP address on the banlist would likely skip many of the banlist IP addresses when it chooses its next outbound peer connection.

## Suggestion

An honest node that does not establish outbound connections to IP addresses on the banlist would provide better privacy to users who use the node as a local or remote node to construct and broadcast transactions. Future versions of the Monero node software could hard-code some or all of the banlist IP addresses to avoid establishing outbound connections (which are the most privacy-sensitive type of connection), but still allow inbound connections from those IP addresses. The software modification would _not_ exclude those IP addresses from the network. Instead, nodes from those IP addresses would just have to establish their own outbound connections to nodes on the network. The hard-coded behavior could remain in effect until a more universal solution presents itself.

**Special thanks to @Boog900 for feedback on this analysis.**

_Analysis code is forthcoming._

## References

Venkatakrishnan, S. B., Fanti, G., & Viswanath, P. (2017). Dandelion: Redesigning the Bitcoin Network for Anonymity, Proc. ACM Meas. Anal. Comput. Syst. 1(1).

Fanti, G., Venkatakrishnan, S. B., Bakshi, S., Denby, B., Bhargava, S., & Miller, A., et al. (2018). "Dandelion++: Lightweight Cryptocurrency Networking with Formal Anonymity Guarantees," Proc. ACM Meas. Anal. Comput. Syst. 2(2).  

## yanmaani | 2025-08-11T18:46:59+00:00
Could injection of latency help here?

If I have an encrypted connection to another node with some shared secret, it would be possible to do something like:
- `k` = `shared secret % 60`
- I will only send own messages when `k` < `time() % 60` < `k + 2`
- I will only respond to messages when `k + 5` < `time() % 60` < `k + 7`

If we are two nodes communicating directly, this would add a latency that's known by us both. But if there is a third party in the middle, unless it can grind the value of the shared secret, it would add a minute of unexplained latency.

Some messages, I guess, are too urgent to be subjectable to this.

(Maybe nodes could send out random requests to calculate something like hash(old txn || shared secret) and see if they get a response in this minute or the next? Of course this then opens the possibility of the MITM attacker responding to those early.)

## Boog900 | 2025-08-11T22:20:04+00:00
This could potentially fix class A proxies mentioned here: https://github.com/Boog900/p2p-proxy-checker but sadly that is the easiest type to kill. Class B is a lot more tricky as they do run a node but have multiple addresses pointing to it, it would be easy to overcome your scheme if all addresses share a single blockchain and each have access to all the data in it. 

# Action History
- Created by: Boog900 | 2024-10-31T18:58:07+00:00
