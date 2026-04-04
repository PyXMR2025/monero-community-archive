---
title: 'MRL recommendation: Ban spy node IP addresses from connecting to your node'
source_url: https://github.com/monero-project/meta/issues/1124
author: Rucknium
assignees: []
labels: []
created_at: '2024-12-11T19:02:44+00:00'
updated_at: '2026-01-29T11:51:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**UPDATE 14 January 2026**: MRL ban list version 2 released. It is available at the same URL as before: [https://raw.githubusercontent.com/Boog900/monero-ban-list/refs/heads/main/ban_list.txt](https://raw.githubusercontent.com/Boog900/monero-ban-list/refs/heads/main/ban_list.txt). It is recommended to update to the latest ban list. The vast majority of spy nodes in the old ban list have switched to different IP addresses.

**UPDATE 19 June 2025**: Code and explanation for how the spy nodes were detected is [here](https://github.com/Boog900/p2p-proxy-checker). [Relevant MRL meeting log](https://github.com/monero-project/meta/issues/1223).

The Monero Research Lab (MRL) [has decided](https://github.com/monero-project/meta/issues/1119) to recommend that all Monero node operators enable a ban list of suspected spy node IP addresses. The spy nodes can reduce the privacy of Monero users.

`cuprate` developer Boog900 discovered these spy nodes and created an IP address ban list. Developers and researchers associated with MRL (list names) have indicated their approval of this list by signing it with their PGP keys.

## How do I enable the ban list?

Download the ban list from `https://raw.githubusercontent.com/Boog900/monero-ban-list/refs/heads/main/ban_list.txt` and remember the directory on your computer where you saved it so you can replace `--ban-list <file-path-to-ban-list>` below with it. For example, if you saved the file in `/home/user/Downloads`, they you would replace `<file-path-to-ban-list>` with `/home/user/Downloads/ban_list.txt`. **WINDOWS USERS**: Download the ban list file directly and save it. Do not copy-paste it into a new file. There is a Windows problem with the copy-paste method that [will be fixed in the next Monero software release version](https://github.com/monero-project/monero/pull/9610).

### Running `monerod` from the terminal

If you run the node from the terminal, add `--ban-list <file-path-to-ban-list>` when you start up `monerod`, i.e.

`./monerod --ban-list <file-path-to-ban-list>`

If you use a config file instead of command line flags, add this line to the config file:

`ban-list=<file-path-to-ban-list>`

### Monero GUI wallet

If you use a remote node, whoever operates the remote node will decide if the ban list is enabled. If your run your own local node through the GUI wallet, go to Settings. In the "Daemon startup flags" box, input "`--ban-list <file-path-to-ban-list>`". Then click the orange "Stop daemon" button. It will take a few seconds for the daemon to shut down. Then click the orange "Start daemon" button.

### Docker

If you use SethForPrivacy's `monerod` Docker file, update to the latest version, which has the ban list: https://github.com/sethforprivacy/simple-monerod-docker

If you run the Docker Monero node with any custom flags or custom config file, [you need to add to `--ban-list=/home/monero/ban_list.txt` to the set of flags or `ban-list=/home/monero/ban_list.txt` to the config file](https://libera.monerologs.net/monero/20241205#c468982).

## FAQs

**1) What is the evidence that spy nodes run at these IP addresses?**

The numerous spy node IP addresses are pretending to be distinct nodes, but the spying adversary is proxying a few nodes through a large number of IP addresses. That way, the spying adversary can spy on the node network, but does not have to pay the full cost of running one node per IP address.

Unfortunately, the exact fingerprint of the spy nodes is not being released because the spying adversary might be able to fix the fingerprint and set up new spy IP addresses. However, a large number of the suspected spy IP addresses are the same IP addresses implicated in ["LinkingLion" spying on the BTC node network as far back as 2020](https://b10c.me/observations/06-linkinglion/). The spying adversary is likely using the same IP addresses to spy on BTC and Monero.

Furthermore, most of the spying IP addresses are in a few "subnets", which are basically consecutive IP address numbers that can be purchased at a bulk price rate from IP address providers. Almost every IP address in the subnets have a suspected spy node, a status MRL is calling "subnet saturation". More details are in the [MRL GitHub issue](https://github.com/monero-project/research-lab/issues/126).

**2) Can I tell how many spy nodes my node is connected to?**

Yes. You can run the `peers.ip.collect()` function in the `xmrpeers` R package. See the "Examples" in the documentation [here](https://rucknium.github.io/xmrpeers/reference/peers.ip.collect.html#ref-examples). The function will also start to show the subnet saturation after running for about 24 hours.

**3) What is the privacy issue?**

Monero uses Dandelion++ for privacy of transactions relayed on its peer-to-peer node network. Dandelion++ provides strong privacy, but even its privacy can be weakened if there are too many spy nodes on the network. An adversary who controls a lot of spy nodes may be able to guess which user's IP address was the original sender of a Monero transaction.

**4) Won't the spying adversary just change its IP addresses?**

This is possible, but it's costly for the adversary. The LinkingLion BTC spying adversary is still using these IP addresses even though the spying has been publicly revealed for at least 21 months, which suggests that the adversary cannot easily change their IP addresses.

**5) Are more universal fixes possible so that a specific ban list doesn't have to be used?**

MRL will analyze the possible benefit of implementing an algorithm that chooses node peers to maximize diversity of Autonomous System Networks (ASNs), which are groups of IP addresses managed by the same entity. This algorithm could reduce the probability of connecting to too many potential spy nodes.

In the long term, there may be ways for nodes to verify that their peers are truly running a node instead of just proxying one node through many IP addresses.

**6) Why not block these IP addresses by default in the Monero node software?**

Blocking the IP addresses by default is technically possible, but it would set a precedent of blocking IP addresses by a decision making process that is semi-centralized. MRL has decided to ask node operators to block these IP addresses voluntarily instead of by default. 

# Discussion History
## sethforprivacy | 2024-12-12T18:54:39+00:00
I can confirm this has been deployed on my public node and all of Cake's Monero nodes.

## Rucknium | 2024-12-12T19:50:14+00:00
@sethforprivacy Wonderful. Thank you!

## rblaine95 | 2024-12-14T09:33:12+00:00
Would a viable long term solution be to block IPs that share node fingerprints?

e.g: If the same fingerprint is detected across >1 IP automatically ban the IPs?

## selsta | 2024-12-14T14:00:15+00:00
@rblaine95 I don't think this is possible, whatever fingerprint detection we use can simply be fixed by the spy node operators before we even put out a release.

## kkarhan | 2024-12-14T19:22:57+00:00
As per [recent commit](https://github.com/greyhat-academy/lists.d/commit/f036e9b094ef0cba99bada1beae97aa64df0fdbd) said [banlist](https://github.com/Boog900/monero-ban-list) has been added to [lists.d](https://github.com/greyhat-academy/lists.d) [```blocklists.list.tsv```](https://github.com/greyhat-academy/lists.d/blob/a16de0856fccf13553c2a33f4d4abcefb68ba209/blocklists.list.tsv#L23).

In [my comment](https://gist.github.com/Rucknium/76edd249c363b9ecf2517db4fab42e88?permalink_comment_id=5335513#gistcomment-5335513) under @Rucknium 's [gist](https://gist.github.com/Rucknium/76edd249c363b9ecf2517db4fab42e88) I considered such cyberespionage attempts a matter of security, which is in line with [known state-sponsored attacks against Monero](https://www.youtube.com/watch?v=WkphgF6Hn4w&t=26s).

- Simply because [malicious nodes](https://www.youtube.com/watch?v=WkphgF6Hn4w&t=76s) like [```node.moneroworld.com```](https://youtu.be/WkphgF6Hn4w?feature=shared&t=216) are easy to spin up and U$D 1,25M is a lot of money to burn, tho with IPv4 shortages it'll be hard for said attackers to keep doing so if we literally blocklist entire /24's.

Needless to say the optimal strategy would be if everyone were to [host their own node over Tor](https://www.youtube.com/watch?v=nDBHhz00vjI) but that's sadly not a viable option for everyone.

To address @rblaine95 's [question](https://github.com/monero-project/meta/issues/1124#issuecomment-2543024030): *It's not that easy*, given that someone may have a shitty ISP with changing IPv4's or using mobile networks or even using [Multipath TCP](https://en.wikipedia.org/wiki/Multipath_TCP) or some [applicanced](https://www.viprinet.com/en) / commercial VPN for redundancy...

- That being said such malicious nodes are a general problem and it'll be only a matter of time till the operators of said network either learn how to properly deploy stuff without wasting entire /24's with non-unique Fingerprints.

- I'd suggest to look at how [Tor Project](https://www.torproject.org/) dealt with that. I remember [ioerror](https://github.com/ioerror) having dealt with such things in the past when the *"P.R."* China and Russia tried to deanonymize local Tor users but I don't have much details on that...

So besides the existing IPv4 banlist I'd also suggest IPv6 banlists and to look into [integrating Tor natively](https://guide.onionmobile.dev/tor-on-ios/tormanager) into Monero wallets and nodes where feasible.

- [Feather Wallet](https://github.com/feather-wallet/feather) and [monerujo](https://github.com/m2049r/xmrwallet) already have Tor integration, may it be [built in as in Feather Wallet](https://docs.featherwallet.org/guides/tor-support) or simple proxy support.

## kkarhan | 2024-12-14T19:24:43+00:00
> @rblaine95 I don't think this is possible, whatever fingerprint detection we use can simply be fixed by the spy node operators before we even put out a release.

Yeah, they'd just learn how to use ansible (or whatever tools they use to deploy that) properly instead of rolling out clones...

- simply because the suspected attackers [have a lot of money to burn through](https://github.com/monero-project/meta/issues/1124#issuecomment-2543318835)...

## kkarhan | 2024-12-14T19:30:13+00:00

> **6) Why not block these IP addresses by default in the Monero node software?**
> 
> Blocking the IP addresses by default is technically possible, but it would set a precedent of blocking IP addresses by a decision making process that is semi-centralized. MRL has decided to ask node operators to block these IP addresses voluntarily instead of by default.

**THIS** is crucial. Otherwise it would be trivial to strong-arm MRL into imploding Monero!

## HCNOP | 2025-01-31T15:08:38+00:00
I am syncing a local node on MacOS, but will soon set up a full node on VPS. 
Regarding the local node on Monero GUI that is currently syncing, is there a chance that some nodes on the ban list will be queried during the sync?

## Rucknium | 2025-02-03T20:03:32+00:00
@HCNOP 
> Regarding the local node on Monero GUI that is currently syncing, is there a chance that some nodes on the ban list will be queried during the sync?

No, if you have the ban list enabled.

## runatyr1 | 2025-02-17T04:11:27+00:00
Isn't an alternative solution, to upgrade Monero to only accept connections via Tor, and force all wallets to implement it? This way even if it is a spy node it can't collect anything useful

## runatyr1 | 2025-02-17T04:13:21+00:00
Another question, in monerohash.com there is a Monero node map that shows like 50% of all nodes on the network being in the same spot in the USA. Is this accurate? If so it could be a huge privacy issue.

![Image](https://github.com/user-attachments/assets/47cfc294-bc92-4218-b35b-7d3f4ed33ce0) 


## runatyr1 | 2025-02-18T01:10:22+00:00
> * What would be the benefit of choosing TOR over I2P, I was under the impression I2P was specifically built to handle this kind of of P2P traffic over its network?

My understanding is the underlying concern in this GH issue is that spy nodes can log user IPs potentially compromising privacy.  While I2P is used for node peering, and the initial solution offered here is banning spy nodes from becoming peers; I'm referring to another possible solution: enforcing TOR on wallet to node connection, which I believe happen using ZMQ and it already has good TOR support. 

Making TOR mandatory for wallet to node connections, in my understanding, would eliminate the need of maintaining spy node blocklists, as IP logging would become useless. For now, the only fault-proof solution is running your own node, but for the average user is not easy enough. And banning spy nodes is only a mitigation as not all node operators will do it, and governments with their big budgets could spin up thousands of spy nodes if they wanted (and maybe they already do).

> * Integrate it directly into monerod daemon, wallets will all automatically inherit it then

Yes I think this would require changes in monerod, and wallet providers would require to add TOR support. It also needs considerations on the performance impact of establishing TOR circuit which I believe takes 5-10 seconds and would need to be re-done in mobile devices when changing networks. This is above my development knowledge, so I'm only sharing the idea in case someone else wants to pick it up to further consider/implement.

## jeffro256 | 2025-04-30T17:41:35+00:00
> Another question, in monerohash.com there is a Monero node map that shows like 50% of all nodes on the network being in the same spot in the USA. Is this accurate? If so it could be a huge privacy issue.

IIRC, all the the IPs in the USA without precise geographical data, as according to the database monerohash.com uses, get placed in Ashburn, Virginia. So no, probably not accurate. 

## Rucknium | 2025-07-16T16:59:54+00:00
It has come to my attention that some node operators can make a mistake when trying to enable the ban list, especially when performing all tasks on the command line. The mistake can prevent the ban list from taking effect.

The link for the ban list originally appeared as `https://github.com/Boog900/monero-ban-list/blob/main/ban_list.txt` This is an HTML web page on GitHub. If the web page is downloaded directly through a `wget` request or similar, all the extra HTML code will be downloaded in the file. Then, the Monero node software will fail to properly parse the ban list file when there is all the extra HTML content.

If node operators directly download the file, they should use the link to the raw text file: `https://raw.githubusercontent.com/Boog900/monero-ban-list/refs/heads/main/ban_list.txt`

Node operators and users can check if a specific node (with IP address) has the MRL ban list enabled by scrolling to the bottom of this experimental web app and searching for the node: https://moneronet.info/

## nahuhh | 2025-07-16T18:15:27+00:00
https://github.com/Boog900/monero-ban-list/raw/main/ban_list.txt

this works too (redirects)

## Rucknium | 2026-01-14T15:57:20+00:00
Version 2 of the ban list has been released. It is available at the same URL as before: [https://raw.githubusercontent.com/Boog900/monero-ban-list/refs/heads/main/ban_list.txt](https://raw.githubusercontent.com/Boog900/monero-ban-list/refs/heads/main/ban_list.txt). It is recommended to update to the latest ban list. The vast majority of spy nodes in the old ban list have switched to different IP addresses.

Timeline since the first ban list was released:

- In June 2025, the method used to detect the spy nodes was published: https://github.com/Boog900/p2p-proxy-checker

- July: A daily network scanner and webapp data visualizer was deployed: [MoneroNet.info](https://moneronet.info/) . Network scans suggest that about 8 percent of honest nodes were using the MRL ban list.

- Early October: New version of the Monero node software included the "[subnet deduplication](https://github.com/monero-project/monero/pull/9939)" countermeasure. Spy node adversaries rent contiguous ranges of IP addresses called "subnets" in bulk to minimize their costs. Subnet deduplication is a peer choice rule that lowers the probability of connecting to a node in a densely-populated IP address subnet. According to simulations, subnet deduplication reduces the number of connections to spy nodes by 70 percent for node operators who do not use the MRL ban list. (Operators who do use the MRL ban list would not try to connect to the spy nodes in the first place.) The subnet deduplication code was written by rbrunner7 and reviewed by vtnerd, jeffro256, and Rucknium.

- Late October: Spy nodes using IP addresses belonging to the Digital Ocean and Hetzner server rental companies begin hiding their spy node "fingerprint". These spy nodes are still operating but no longer respond to ping requests with the telltale spy node behavior.

- Early December: Almost all spy nodes on the LionLink Autonomous System (AS) shut down. The LionLink spy nodes were the most numerous spy nodes on the Monero network. A few days later, a roughly equal number of spy nodes appear on IP addresses within the Spruce Creek AS. The Spruce Creek AS was registered in November 2024 by an unknown party. The migration of these spy nodes to new IP addresses triggered the release of this new MRL ban list.

- Mid-January: The DNS-disseminated ban list, managed by Monero contributors, is updated to include the MRL version 2 ban list. The DNS ban list can be enabled by adding the `--enable-dns-blocklist` startup flag to the Monero node. According to network scans, about 50 percent of honest reachable nodes do enable the DNS ban list.

## gueperide | 2026-01-16T09:49:32+00:00
on Ditatompel, i can see MRL and DNS banlist HTTP enabled nodes but no one TOR or I2P nodes...why ? tks

## Rucknium | 2026-01-17T13:55:47+00:00
@gueperide

The ban list enabled status of an onion-ized Monero node RPC cannot be queried directly.

A node is detected as having a ban list enabled by initiating (a "handshake") a normal peer-to-peer connection with a node. One of the sets of information that nodes exchange when they initiate a connection is a list of up to 250 IP addresses and ports of other nodes. The purpose of the information exchange is to give new nodes more potential peers to try to connect with to keep the network strong and interconnected.

If a node shares zero IP addresses that are on a ban list during its handshake, it is very likely that the node has the ban list enabled. The node won't share a banlisted IP address because it would already have been removed the the node's internal peer list.

Connecting with peers and sending data to wallets are two separate node functions that require separate ports. These are known as the p2p and RPC ports, respectively. Usually, the ports are on the same IP address. My network scanner at https://moneronet.info/ assumes that if the p2p handshake suggests that a node has enabled the ban list, then the RPC port on the same IP addresses has the ban list enabled. @ditatompel 's website https://xmr.ditatompel.com/ pulls data from my network scanner.

The whole point of an onion hidden service is to unlink a service's real IP address from its onion address. The onion hidden service connects wallets to a node's RPC port, which is different from the p2p port that I use to infer whether the node has the ban list enabled. I cannot determine the ban list status of the node that is providing RPC connections through an onion hidden service.

I agree it's confusing when @ditatompel 's website says that no onion or I2P remote nodes have the ban list enabled. Maybe I can work with @ditatompel to write some brief explanation text about it. We could also indicate the ban list enabled status on the few onion and I2P remote nodes that have known clearnet IP addresses, e.g. https://github.com/feather-wallet/feather-nodes/blob/master/nodes.yaml


## gueperide | 2026-01-17T19:29:36+00:00
many thanks for this explanation, 
I hope I've understood the main points.

But we do agree that it's still necessary to enable the ban list for TOR and IP2 nodes, right?

Thanks

## ditatompel | 2026-01-29T11:51:37+00:00
> I agree it's confusing when [@ditatompel](https://github.com/ditatompel) 's website says that no onion or I2P remote nodes have the ban list enabled. Maybe I can work with [@ditatompel](https://github.com/ditatompel) to write some brief explanation text about it.

Thanks @Rucknium, I appreciate it! For now, I've [added a short explanation](https://github.com/ditatompel/xmr-remote-nodes/pull/219) and a link to my site explaining why there are no Tor or I2P nodes listed as having enabled the MRL and DNS ban lists. 

# Action History
- Created by: Rucknium | 2024-12-11T19:02:44+00:00
