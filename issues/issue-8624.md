---
title: 'Discussion: Community Nodes and Request For Volunteers'
source_url: https://github.com/monero-project/monero/issues/8624
author: jeffro256
assignees: []
labels:
- proposal
created_at: '2022-10-25T03:53:41+00:00'
updated_at: '2022-12-16T08:22:02+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Who this affects

People who use Monero GUI wallet in Simple Mode and Simple Bootstrap Mode.

## How Monero GUI Simple Mode works Now


![Monero Community Nodes](https://user-images.githubusercontent.com/10839482/197677792-6f155ef3-efb1-41cf-a70f-0c334a7817d7.jpg)

On the wallet mode selection screen, if the user chooses Simple Mode, Simple Bootstrap Mode, or Advanced mode, the value of `persistentSettings.walletMode` [is](https://github.com/monero-project/monero-gui/blob/aef4a982dc644b3e971a89c8b65dd57d21d5e085/wizard/WizardModeSelection.qml#L99) [set](https://github.com/monero-project/monero-gui/blob/aef4a982dc644b3e971a89c8b65dd57d21d5e085/wizard/WizardModeSelection.qml#L53) [to](https://github.com/monero-project/monero-gui/blob/aef4a982dc644b3e971a89c8b65dd57d21d5e085/main.qml#L2271) 0, 1, or 2, respectively. This value is used to [set the flags of the `monerod` process](https://github.com/monero-project/monero-gui/blob/aef4a982dc644b3e971a89c8b65dd57d21d5e085/main.qml#L706-L708) that Monero GUI spins up in the background. For Simple Mode and Simple Bootstrap Mode (0 and 1), the `--bootstrap-daemon-address` option is set to `auto`. In Simple Mode (0), the `--no-sync` flag is also set.

The `--bootstrap-daemon-address` option is a feature of the core RPC server. When a core RPC server with a bootstrap daemon receives an RPC request, in which block data it does not have is requested for, it will pass that request though to the bootstrap daemon. In this manner, you can seamlessly interact with an unsynced `monerod` process as if it was fully synced with the network. When a `monerod` process is in `--no-sync` mode, this means that virtually all data requests will be passed off its bootstrap node, since it has no block data synced.

When the daemon has the bootstrap daemon address set to `auto`, as it does in Simple Mode and Simple Bootstrap Mode (0 and 1), `monerod` will search the p2p network list, filtering out remote nodes with an open RPC port. These remote nodes are ranked by the local `monerod` process based on how responsive they are plus a handful of sanity checks (e.g. whether the remote node's block head is higher than ours). Then a random node is picked to be the bootstrap node, unless it gets punished in the rankings.

To put it all together, Simple Mode and Simple Bootstrap Mode (0 and 1) start a local `monerod --bootstrap-daemon-address auto ...` process, and interact with it like a normal fully synced `monerod` process. In the background, the local `monerod` process is passing off RPC requests to other random public nodes on the network.

## How Monero GUI Simple Mode Would Work With Community Nodes
When opening a Monero GUI wallet with Simple Mode, we would skip starting a `monerod` process and connect directly to a random community node from the `wallet2` code, secured by an SSL context with a list of hard coded certificate fingerprints. These hardcoded list of nodes would act sort of as a root DNS server, for which we would ask for a list of nodes which it trusts/operates, probably by way of a JSON RPC endpoint. The wallet would maintain a cached list of remote nodes to connect to, which it would randomly switch between, all secured either by SSL or happen over an anonymity network. This is the main reason why this post is in the `monero` repo and not the `monero-gui` repo: the `wallet2` code should be refactored to streamline all the RPC requests through an interface which allows us to seamlessly switch our remote node underneath. For more details, see the discussion at #8605.

## Pros of Community Nodes
1. Security - We can manually control who we connect to which limits the attack surface of [receiving bad information](https://github.com/monero-project/monero/issues/8298) from public nodes or men-in-the-middle.
2. Privacy - Since we know the identities of servers we want to connect to ahead of time, we can use SSL to encrypt our traffic to these nodes which prevents passive surveillance and prevents bad actor public nodes logging RPC requests.
3. Startup Speed - When we skip spawning a `monerod` process, we can save 5-10 seconds of waiting around doing nothing, vastly improving the UX.
4. Scanning Latency - Each RPC request from the wallet to a `monerod` process in "simple mode" must take 2 "hops" there and back: `wallet -> local node -> public node -> local node -> wallet`, as opposed to connecting directly to a community node.
5. Reliability - We can pour resources into a smaller number of high functioning community nodes instead of thrashing around looking for a public node with a decent connection.
6. Antivirus Compatibility - `monerod` contains mining software which sometimes causes antivirus programs to falsely quarantine `monerod`, which causes Simple Mode to fail without warning.

## Cons of Community Nodes
1. Centralization - Who gets to decide who runs the community nodes? Why Person X and not Person Y? Etc. And if one of the node operators becomes compromised, a larger portion of the network is affected.
2. Load balancing - Since all previous GUI Simple Mode RPC requests will be routed through a smaller number of nodes, each community node must be able to handle a larger number of requests.

## Volunteer Operator Requests
Right now, if you would like to be a volunteer community node operator (we can filter out later), please post a maximum of 1 network address per network (IPv4, IPv6, Tor, or I2P) that would be available. For each IPv4 or IPv6 address, also post an SSL certificate generated by `monero-gen-ssl-cert`. If you have a PGP key in the repo, and you would like to sign with that, that would be appreciated.



# Discussion History
## poiuty | 2022-10-27T13:50:12+00:00
Generate SSL certificate.
```
# su monero
# cd /home/monero/.bitmonero
# monero-gen-ssl-cert --certificate-filename node.crt --private-key-filename node.key

Empty passphrase, the private key will be saved to disk unencrypted, use --passphrase to set a passphrase or --prompt-for-passphrase to prompt for one
New certificate created:
Certificate: node.crt
SHA-256 Fingerprint: 6B:AD:46:14:7A:45:AF:52:55:7C:06:AF:19:D2:4D:E3:0B:39:2B:F6:2B:AA:84:E3:C7:DC:4B:0D:79:C1:B9:22
Private key: node.key (unencrypted)
```

Edit config.
```
# nano /etc/monerod.conf

rpc-ssl-certificate=/home/monero/.bitmonero/node.crt
rpc-ssl-private-key=/home/monero/.bitmonero/node.key
```

Restart monerod.
```
systemctl stop monerod.service
systemctl start monerod.service
```

Node info.
```
Germany, Hetzner, AX101.
https://www.hetzner.com/dedicated-rootserver/ax101

176.9.63.51
2a01:4f8:150:812f::2

p2p-bind-port=18080
rpc-bind-port=18081

-----BEGIN CERTIFICATE-----
MIIEdDCCAlwCAQEwDQYJKoZIhvcNAQELBQAwADAeFw0yMjEwMjcxMzM2NDVaFw0y
MzA0MjcxMzM2NDVaMAAwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQCu
+lLnYVlc5ezF4eh6bQ3g3ke0q5ZjfvhUNaRbKJgvCioPDHvb19jdZ9M5mLJMArSg
5wrxD7X2g7bNwB5eUyB/IBTkUqBb0nleUgpaTzFPOAA9ZIp3ZF8JXlHXu/Dy6Dkq
wGV6mIbBSs6NeAf228elFQk47thIHM3IXH2MmLdYjHJD4o28FgZI/jC6EDCvz7Vm
RtdlW4iwgpCKfX/Awh0w/5Ttruyx0hYo9Wu4NMA8A0W/yiZYBpzGo19q/ZIqrrW2
wX0A9vCgSiQ6FTn77pC5CaUYdxg9pA9UW92eC4VPaiC5yKReiVh18BImIrreIuSS
5zZK3Gk0H43xD6UzyBpLZ/7w+UwxUER6IgwGAOwREa/3xdGwzy7Ru9sCvEjr0uV/
8Dic103Egk8udh8rJazRWLsu3hF+QIDLYlp7lGFkoL2dm+mW3qOm3jsEyuT5ABeG
5Dobny4ZzvC/v0MaW3gqh9z0RI3LW2r7t13t1ioTu/4JmgvZXzTLNmH6znmhaUmF
qT6qq5KkOteZpNuSummsmKYMxZr7BQWZQe15wIXoRYBR/fTVN8L+cnhaxFrnGcHt
3faU/TLN58kF0bMTYGe63nt7Mm5acu1Ni0fOPKwDx0H+qkvVBgWsXH5ENQHTLPeH
oQz/QpD5Bw6nvKI6PO1OOgxIPxoMgv73FOT4fmEVLwIDAQABMA0GCSqGSIb3DQEB
CwUAA4ICAQBRk/5EH5LzJ/fIEIKZ6yVPFWzwcUd0Vjl1oVkTOya0iBhNhE0vDQ89
aZK2KdSufjpIJHlu9ki8blRUTgxW50UyHHTD77vWZDdsm4zOY63nx+Y9ybY0QX8Q
W3LIXbDIvbjMlgcXw6uR4G9BArGOCRt7vL4XWQ/KzuaYN1MP44XvSvhsbJSzAWx3
b5soIlyQJJO7o+A0cGXq/RRN5jYPST366TqjdCribQpfGbQrs2IpDjzc/Iddexzi
qYMzLaZ9pn7R5BaCwxV/smDdFItTXwkdlPry+gre4rbHkrv9KAhArx4QXQf+fkc6
xmZMNFkb489S+41GLsOxVmZThfA77oagkJ6gH9smdSX8UMcfBNmdE2XEVtmoJHs5
IatkbZC7lORRFkfaZTG7mB+7D7rTqvkGnGrp9aRKXXskH0eLgkQoC7S/u9kwgXbu
b/RxwxklORsDGd4555bzXqzAEuQkYUZ1QDUmT5rqqun+HiIMfwBeAi7VyKFkJl0l
mH6KmEQtea4pEW3Zrf21w+0YJlZ3tjLVSxUtSTLruag5bZ+IJfZTTnlP1vZZoRFX
463NngUuadiAhLXwbb/tGpggnJl153tGs1Pjc1+/6IdDlvzQaLMp7bo2V/ay22UQ
/VaorSM0AA3xGAqOsVdn8LDGLBqpGRExWdH7bApLWeDAfKPi6lmvhA==
-----END CERTIFICATE-----
```

## SamsungGalaxyPlayer | 2022-10-27T13:56:04+00:00
I will speak with Vik, but Cake Wallet is interested in providing at least 6 nodes on IPV4, and 1 node on Tor. We can also set up 1 node on i2p. Can you point to a domain like `xmr-node.cakewallet.com`, or just IPV4?

## jeffro256 | 2022-10-27T17:07:32+00:00
@SamsungGalaxyPlayer I'd say that, yeah, DNS names should be allowed since we're going to be securing them with hardcoded SSL certificates so DNS poisoning shouldn't be too much of an issue (please correct me if I'm wrong). Also y'all can definitely run 6 nodes on IPV4, I'm just asking for 1 _"root"_ community node per network per IRL entity at the moment.

## hinto-janai | 2022-10-27T18:39:41+00:00
I'm also interested in this since I'll be relying on community nodes in a project of mine. I have a list of community nodes [here](https://github.com/hinto-janaiyo/gupax/blob/bf81b2c57cfe50cd93ac54e03a2d507f58e4aa5c/src/node.rs#L27) that are all unencrypted. Hopefully most of the owners wouldn't mind upgrading or even creating a 2nd server if poked hard enough :D

>Centralization - Who gets to decide who runs the community nodes?

I think this will be the only big issue. Having some type of large consensus is necessary here. A standardized node list voted on by the community would be really nice. Not sure how this would be implemented in practice though.

If community nodes were implemented as the first choice, for fallback sake, would the `--bootstrap-daemon-address` monerod code still be available? Or would holding on to it make things difficult? The RPC passthrough + ranking code seem too wasteful to remove. It could maybe save the day in the (unlikely) scenario where all community nodes are down.

## selsta | 2022-10-27T20:03:32+00:00
> If community nodes were implemented as the first choice, for fallback sake, would the --bootstrap-daemon-address monerod code still be available?

We wouldn't remove bootstrap functionality, just not use it in monero-gui.

## MajesticBank | 2022-11-01T10:20:06+00:00
Great idea and really good improvement over previous model, however very challenging task.

Is there some dead-line on this ?

Would be cool that DNS should be supported also beside IPs so that in case of IP change node still can be functional ( SSL cert stays the same )

Will be for sure able to provide wide range of remote node servers, based on number of users and load. 


The design wallet -> local node -> public node -> local node -> wallet still involves monerod?

Thinking out loud maybe would be cool to have "node families" 

Any possibilities of multi-hop system? wallet -> node family 1 -> node family 2 -> network








## endorxmr | 2022-11-04T12:38:13+00:00
@poiuty careful, I have seen some recent reports that Hetzner has become quite anti-crypto in general, and has caused trouble/blocked accounts of users doing anything crypto-related (not just mining, but also running a node and/or other crypto-related related activities).

It's not in their ToS, more of an "unofficial internal policy" at this point.

## monerobull | 2022-11-07T09:23:35+00:00
What's the estimated cost for running one of these beefed up nodes on a hosting provider?
I'd love to apply for community node but am not sure what costs this would entail.

## poiuty | 2022-11-07T21:01:46+00:00
@endorxmr, after Chia (plotting), Hetzner changed the ToS.
> Operating applications that are used to mine cryptocurrencies
> https://www.hetzner.com/legal/dedicated-server/

Monero node is not a miner. But even if Hetzner is anti-crypto. 
No problem. It won't stop me. I will set up nodes in another data center.

@monerobull, dedicated server costs $40~100 per month.
A good choice AMD Ryzen 3600, 64GB RAM, NVMe disks in raid1, 1 Gbit/s.


## endorxmr | 2022-11-07T21:48:16+00:00
@poiuty yeah I knew about the mining policy, but I was specifically referring to them being anti-crypto in general (even running a node). There should be a post about it on r/Monero from 1-2 months ago, I think.

## jeffro256 | 2022-11-14T23:02:58+00:00
> Is there some dead-line on this ?

@MajesticBank  No, not currently. I'm working on it whenever I can. I'm currently reviewing/ waiting on others to approve @j-berman's `scan_tx` fix so I can start pushing ahead with the RPC refactorings.

> Will be for sure able to provide wide range of remote node servers, based on number of users and load.

Great! :)

> The design wallet -> local node -> public node -> local node -> wallet still involves monerod?

I'm not sure if I understand the question,

> Thinking out loud maybe would be cool to have "node families"
> 
> Any possibilities of multi-hop system? wallet -> node family 1 -> node family 2 -> network

Currently the way I have it designed is that there is one "root" node per IRL identity. All this root "node" has to do is provide a JSON endpoint which contains a list of their recommended servers. When the wallet starts up, it picks a random root node, asks for servers from that root node, then randomly selects one of those. This should allow the system to scale and balance loads without having to update wallet software. 

Or are you asking for more of an onion-routed system like Tor? 

## jeffro256 | 2022-11-14T23:06:37+00:00
> What's the estimated cost for running one of these beefed up nodes on a hosting provider? I'd love to apply for community node but am not sure what costs this would entail.

I have no idea what the traffic will be like for each node since that depends on the number of users (I don't know Monero GUI usage stats), the number of root identities, and the number of community servers you run. What is nice though is that if the community network does get overloaded, we can just throw more servers at the problem since it's all distributed public information. 

## Gingeropolous | 2022-12-05T12:21:16+00:00
well you could guess I'm not a huge fan of the centralized aspect of this, but the current scenario does warrant some kind of solution. 

however, the bitcoin ecosystem (granted, they don't do everything ideally as well), has avoided a centralized approach regarding the electrum light wallet system. ... and of course it uses some kind of headers sync to validate providers or something. 

i dunno. I feel there's a better solution than centralization, but like always, decentralized solutions are harder. 

## jeffro256 | 2022-12-11T20:46:10+00:00
Yeah the centralization thing does bug me a little, but Electrum light wallet have issues as well. For one, the wallet "subscribes" to notifications to their addresses by telling the servers which addresses to scan transaction for. This is pretty bad for traceability (think MyMonero light wallet) and is an issue which this community node scheme does not have.

What would be nice is to have some variation of [Simple Payment Verification](https://electrum.readthedocs.io/en/latest/spv.html#spv), but again, this has the issue of the servers lying by omission. 

It's all tradeoffs, but the fact that this only applies to wallets which 1) don't want to run a node and 2) know they're relying on a higher degree of trust makes the move from relying on a random untrusted public node with an open RPC port worth it in my eyes.

## Gingeropolous | 2022-12-13T12:34:22+00:00
> but Electrum light wallet have issues as well. For one, the wallet "subscribes" to notifications to their addresses by telling the servers which addresses to scan transaction for. This is pretty bad for traceability (think MyMonero light wallet) and is an issue which this community node scheme does not have.

I wasn't referring to that component of Electrum light wallets, more to the components of the protocol that build the electrum network. As far as I know (but I can't find the exact documentation on this), an electrum wallet (similar to the GUI in remote-node mode) connects to multiple servers (in monero, remote nodes)

> By default, Electrum tries to maintain connections to ~10 servers. The client subscribes to block header notifications to all of these, and also periodically polls each for dynamic fee estimates. For all connected servers except one, that is all they are used for. Getting block headers from multiple sources is useful to detect lagging servers, chain splits, and forks.

https://electrum.readthedocs.io/en/latest/faq.html

Of course, in monero, even if a wallet connected to 10 nodes, a malicious node could serve up fake (or synthetic) information to become part of the 10 servers a wallet connects to. Then, if the electrum protocol was followed, the wallet could use the fake one to actually push the transaction. This could allow an attacker to blackhole the transaction (simply not relay it), but I think this can be countered by just pushing the transaction to all of the connected nodes. Each node could start its own dandelion stem per protocol, preventing the remote node blackhole attack. 

Currently a monero wallet just connects to one remote node. 

Basically, I think a lot of the problems encountered when using remote nodes could be remedied by connecting to multiple remote nodes. (except for the problem of IP exposure, but that is an inherent problem when using a remote node). 

## MajesticBank | 2022-12-16T08:22:02+00:00
I don't agree with broadcast to all narrative. That would allow one node to observer whole Monero GUI tx activity.

In my opinion we need to lean more towards tor onion layered model.

In broadcast to all scenario while comparing to Tor, , imagine you are connecting to all entry nodes at once, your connection wouldn't not be private at all.




# Action History
- Created by: jeffro256 | 2022-10-25T03:53:41+00:00
