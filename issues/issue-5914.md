---
title: Setting up a wallet with a full node and tor should be easier
source_url: https://github.com/monero-project/monero/issues/5914
author: kpcyrd
assignees: []
labels: []
created_at: '2019-09-15T17:56:11+00:00'
updated_at: '2023-06-17T15:07:50+00:00'
type: issue
status: closed
closed_at: '2022-04-08T16:37:26+00:00'
---

# Original Description
After some discussion in #monero-dev I would like to highlight the following things that could be improved.

The usecase I'm looking at is the one that I assume is the most common one:
- a single laptop running a full node, the gui wallet and tor
- all connections should be through tor, so the external ip address doesn't leak to other monero nodes and the isp can't see that monero is used
- no incoming connections to keep everything as simple as possible

The rationale is that the current ANONYMITY_NETWORKS.md is rather difficult to follow, which causes wrong assumptions and misconfiguration that allows monero to work, but doesn't actually fulfil the objectives we've defined above.

This list has been written in a somewhat short time and I likely contains mistakes, I'm happy to edit the original post with feedback.

## Two conflicting guides

There are two [(1)] [(2)] guides describing how to setup monero with tor, giving very different advice.

[(1)]: https://github.com/monero-project/monero/#using-tor
[(2)]: https://github.com/monero-project/monero/blob/master/ANONYMITY_NETWORKS.md

## torsocks example doesn't work with the gui client

The gui wallet needs to connect to a port in localhost. This is forbidden by torsocks to prevent leaks by local dns resolvers and the example doesn't disable this restriction, so the gui wallet fails to start the daemon.

## `--proxy` currently doesn't support ipv4/ipv6:
Assuming I'm reading this correctly there's a `--proxy` flag, but no way to use it for all traffic. This is because you have to prefix it with a zone like this:
```
--proxy tor,127.0.0.1:9050
```
This means the proxy is only used for nodes matching the zone. For my example this would be for `.onion` only. Zones supported are currently only tor and i2p. Everything else is going through clearnet with no proxy.

https://github.com/monero-project/monero/blob/2c171a9b02f8f23cc36db0465a4b587b60e629d5/src/p2p/net_node.cpp#L207-L218

There is in fact a `--proxy` option at the wallet that accepts `127.0.0.1:9050` with no zone restriction. This is for `wallet -tor-> remote daemon -> clearnet`, but this isn't what we want to do and adds to the confusion.

## Section about Outbound connections has issues

This section: https://github.com/monero-project/monero/blob/2c171a9b02f8f23cc36db0465a4b587b60e629d5/ANONYMITY_NETWORKS.md#outbound-connections

Suggests `--add-exclusive-node`, but doesn't mention that this is going to disable peer discovery, so you're only connected through that one node. This would _theoretically_ be a problem because you would unknowingly put this node into a position to perform an eclipse attack.

The section above this claims that you can't actually sync block through anonymous networks, which mitigates the eclipse attack problem mentioned above, but also means we can't implement the setup we've described in the beginning using this guide.

I can see why a onion only mode is problematic regarding sybil attacks, but it doesn't mention why I can't just use tor to connect to the bootstrap node and then use tor to connect to clearnet nodes while using the ip address scarcity as sybil attack defense.

# Discussion History
## jtgrassie | 2019-09-15T19:08:56+00:00
> Two conflicting guides

Not really. The guide in the README clearly points out there is a "new, still experimental, integration with Tor", which is the second link you reference.

> --proxy currently doesn't support ipv4/ipv6

Correct. What does this have to do with this issue? This option is for connecting to a local tor/i2p socks proxy.

> There is in fact a --proxy option at the wallet that accepts 127.0.0.1:9050 with no zone restriction.

I think this is just a documentation lapse. It should still have the zone IIRC.

> This is for wallet -tor-> remote daemon -> clearnet, but this isn't what we want to do and adds to the confusion.

Perhaps describe exactly what you do want?

> Section about Outbound connections has issues
> ...Suggests --add-exclusive-node, but doesn't mention that this is going to disable peer discovery...

Adding an exclusive node does not disable peer discovery. It just means you will only be communicating with the specified peer, and if that is a tor/i2p peer, means not syncing the blockchain. This is [documented](https://github.com/monero-project/monero/blob/master/ANONYMITY_NETWORKS.md#p2p-commands) in the doc and explains you would also need to add an exclusive clearnet peer to enable block syncing.

The primary goal of the experimental tor/i2p integration right now is as documented: "The design is intended to maximize privacy of the source of a transaction by broadcasting it over an anonymity network, while relying on IPv4 for the remainder of messages to make surrounding node attacks (via sybil) more difficult.".







## kpcyrd | 2019-09-15T19:51:10+00:00
> > --proxy currently doesn't support ipv4/ipv6
> 
> Correct. What does this have to do with this issue? This option is for connecting to a local tor/i2p socks proxy.

"This option is for connecting to a local tor" doesn't mean anything. Does it use tor to connect to hidden services or does it route everything through tor? I can assure you that people are going to assume the later, while it only does the former.

---

> > There is in fact a --proxy option at the wallet that accepts 127.0.0.1:9050 with no zone restriction.
> 
> I think this is just a documentation lapse. It should still have the zone IIRC.

This was just a sidenote because there was some brief confusion in #monero-dev where all of this was discussed beforehand.

---

> > This is for wallet -tor-> remote daemon -> clearnet, but this isn't what we want to do and adds to the confusion.
> 
> Perhaps describe exactly what you do want?

I did, at the very beginning:

> The usecase I'm looking at is the one that I assume is the most common one:
> 
>     * a single laptop running a full node, the gui wallet and tor
> 
>     * all connections should be through tor, so the external ip address doesn't leak to other monero nodes and the isp can't see that monero is used
> 
>     * no incoming connections to keep everything as simple as possible

---

> Adding an exclusive node does not disable peer discovery. It just means you will only be communicating with the specified peer, and if that is a tor/i2p peer, means not syncing the blockchain. This is [documented](https://github.com/monero-project/monero/blob/master/ANONYMITY_NETWORKS.md#p2p-commands) in the doc and explains you would also need to add an exclusive clearnet peer to enable block syncing.

The fact that I had to seek back and forth in the docs and read multiple paragraphs to figure out answers to some basic questions was the reason I'm filing this issue, it's too easy to miss some detail somewhere and I don't think we can the blame the user if they do.

> [...] while relying on IPv4 for the remainder of messages to make surrounding node attacks (via sybil) more difficult.".

Re-read what I've suggested, connecting to ipv4 addresses through tor doesn't make you more prone to a sybil attack. The white/grey peerlist protection doesn't care how you connect to an address.

## jtgrassie | 2019-09-15T20:09:28+00:00
>> Correct. What does this have to do with this issue? This option is for connecting to a local tor/i2p socks proxy.

> "This option is for connecting to a local tor" doesn't mean anything. 

As I said, it's for connecting to a local **tor/i2p socks proxy**

> Does it use tor to connect to hidden services or does it route everything through tor? I can assure you that people are going to assume the later, while it only does the former.

Traffic that is routed through the socks proxy (and in this case tx broadcasts only) would get sent over tor/i2p to the specified tor/i2p peer.

> I did, at the very beginning...

> * all connections should be through tor, so the external ip address doesn't leak to other monero nodes and the isp can't see that monero is used

This is not what is being addressed in the experimental tor/i2p integration, as documented. If you want to route *all* traffic over tor, you need to use torsocks.

> * no incoming connections to keep everything as simple as possible

If you don't want incoming connections, don't add the options to listen (e.g. don't add `--anonymous-inbound ...`).

> The fact that I had to seek back and forth in the docs and read multiple paragraphs to figure out answers to some basic questions was the reason I'm filing this issue

You are more than welcome to rewrite the guides if you feel they are inaccurate or misleading. 

## jtgrassie | 2019-09-15T20:37:43+00:00
>> There is in fact a --proxy option at the wallet that accepts 127.0.0.1:9050 with no zone restriction.

> I think this is just a documentation lapse. It should still have the zone IIRC.

I've just double checked and it's not a documentation lapse. The ***wallet*** proxy option is a standard socks proxy option, no zone needs specifying. The documentation is accurate.

## selsta | 2022-04-08T16:37:26+00:00
The daemon now supports `--proxy` for all traffic.

## k4r4b3y | 2023-06-17T14:03:02+00:00
>The daemon now supports --proxy for all traffic.

@selsta does that mean that by adding `proxy=tor,127:0.0.1:9050` line to my monerod.conf file, I will be hiding my node's connections to the clearnet peers under the tor network? And that a network observer will not be seeing my machine connecting to a bunch of random IP addresses with 18081 ports, but instead will only see that my machine is connecting to the tor network? Am I understanding this `--proxy` flag's use correctly?

## selsta | 2023-06-17T15:07:50+00:00
`--proxy` does not have a `tor` option, the correct syntax would be `proxy=127.0.0.1:9050`

Regarding your question, yes the traffic would be routed through the Tor network. I can't say exactly what a network observer would see, I think even with Tor it would be possible to detect someone running a monero node because of specific traffic and timing patterns.

See also https://github.com/monero-project/monero/issues/7078

# Action History
- Created by: kpcyrd | 2019-09-15T17:56:11+00:00
- Closed at: 2022-04-08T16:37:26+00:00
