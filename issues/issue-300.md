---
title: 'Kovri Discussion: 21 January 2019 20:00 UTC'
source_url: https://github.com/monero-project/meta/issues/300
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2019-01-20T17:42:43+00:00'
updated_at: '2019-01-22T15:04:16+00:00'
type: issue
status: closed
closed_at: '2019-01-22T15:04:16+00:00'
---

# Original Description
**Location**

[Freenode](https://kiwiirc.com/nextclient/#irc://irc.freenode.net/#kovri) | [Mattermost](https://mattermost.getmonero.org/monero/channels/kovri) | [Slack](https://monero.slack.com/) | Irc2P

Please test the relays shortly before using. If there are any issues, please use Freenode IRC directly.

Please PM [SGP on Reddit](https://www.reddit.com/message/compose/?to=SamsungGalaxyPlayer&subject=Monero%20Slack%20invite%20(from%20GitHub)&message=Hello%20please%20send%20a%20Monero%20Slack%20invite%20to%20the%20following%20email:) with your email for a Slack invite if desired.

 - `#kovri`

**Time**

20:00 UTC
3:00p ET
4:00p CT
noon PT

[Use this timezone calculator to convert UTC to your time zone](https://www.timeanddate.com/worldclock/converter.html?iso=20190119T200000&p1=tz_et&p2=28&p3=111&p4=49&p5=179&p6=70&p7=224&p8=48&p9=136).

**Proposed Meeting Items**

This is a discussion on Kovri and the proposed processes by which Monero can limit leaked network metadata and increase network resilience.

Relevant recent discussions and materials:
https://github.com/monero-project/monero/issues/5070
https://github.com/monero-project/monero/pull/4988
https://github.com/knaccc/i2p-zero
https://gist.github.com/coneiric/a26ea711ed7abc7279416a7fb38a283e#file-tini2p-design.md
https://gitlab.com/sekreta/sekreta/blob/master/README.md#the-sekreta-plan

# Discussion History
## SamsungGalaxyPlayer | 2019-01-20T21:46:17+00:00
# Introduction

The recent Kovri drama has prompted the Monero community to rethink the process by which it hopes to provide network-layer privacy and resilience. I have divided this into sections where I discuss several important topics.

I'm going to refer to `nodes` and `wallets` in different methods of interactions, so make sure to pay attention. It's the best way I know how to communicate this for clarity. Monero has a number of circumstances where wallets are independent from nodes.

Even though this comment is long, it still serves as a high-level summary of the situation.

# Network Goals

It's important to outline the goals of the solution we are trying to provide.

**1. Node transaction broadcast hide IP**: perhaps on the most basic level, nodes should be able to broadcast transactions in a way that hides their IP. Even in situations when a user attempts actions 4, 5, 6, or 7, there is no leak to these services if the same user is running them.

**2. Node transaction broadcast without censorship**: nodes should be able to send messages with some resistance to sybil attacks, with a special focus on the incremental attack surface added when using privacy networks.

**3. Node hidden entirely in anonymizing layer**: this is a "reach goal:" users should have the option to run Monero nodes that are connected to other Monero nodes entirely through the anonymizing layer. While one's ISP could tell a user is connected to the anonymizing layer, they would not be able to explicitly tell what traffic is being sent through it. This in part requires that a number of applications other than Monero use this service to provide additional traffic to hide among.

**4. Wallet to remote node transaction broadcast**: users often rely on remote nodes to connect to the network, deciding they would not like to run a full node themselves. An ideal solution would protect the IP of the user who connects to these remote nodes.

**5. Wallet to remote node full synchronization**: an extension of 4, users could ideally synchronize with remote nodes entirely through the anonymizing layer. Unfortunately, this has severe performance limitations, since it requires a lot of data, and the data often needs to pass through several hops. It's likely such an approach will cause congestion for the anonymizing network, extra stress on the remote nodes, and significantly longer synchronization times, hurting UX.

**6. Wallet to lightweight server transaction brodcast**: the same as 4 except with a MyMonero / openmonero / moenro-fastsync -style server.

**7. Wallet to lightweight server full synchronization**: the same goals as 5, but this would be possible with far less performance drawbacks. Users and the server can communicate entirely over an anonymizing layer without significant overhead. Most of the overhead is on the server's end.

# Proposed Solutions

## The "Kovri" Solution

Kovri *nearly* works to some extent with Monero right now. Some would could be done to get Kovri ready for production. However, the majority of the Kovri team, including oneiric_, Sean, and anonimal, are dissatisfied with Kovri's code.

It is difficult for an outsider to tell how polished Kovri is, but the main developers say that continuing work on Kovri would take several months of effort. Furthermore, other i2p routers include new functionality that has not yet been built for Kovri, including NTCP2.

It's likely that even if Kovri was made to "work" in the simplest sense, it would be unreliable, unsafe, and cumbersome to integrate with a substantial portion of the Monero network.

As a plus, Kovri is built in C++, which should make ports to iOS relatively easier than Java applications. This could eventually help goals 4-7, but afaict, no work has been done on this yet.

## The "Kovri Lite" Solution

oneiric_ and others proposed rebuilding Kovri from the ground up, only supporting the bare minimum and best features that are relevant to Monero. You can read the initial outline for the proposal [here](https://gist.github.com/coneiric/a26ea711ed7abc7279416a7fb38a283e#file-tini2p-design.md).

This may be the "ideal" solution if it always worked as we hope, but there are a number of limitations that get in the way. It isn't built out at all yet, and would require 1+ years of full-time effort to get it into any meaningful shape. And beyond that, it would require security audits and ongoing maintenance and support.

Furthermore, there are project management limitations, since someone would need to spearhead the project. We haven't had a great track record in this area. While it could change, I'm doubtful, and I recommend a full series of management documentation before this gets going.

On the plus side, C++ would be easier to port to iOS. But ports would extend the timeline even further.

## The "i2pd" Solution

i2pd is an existing i2p router built in C++ that works right now. Monero could find a way to integrate with the router to get a relatively easy win. Porting would still be necessary for iOS to permit goals 4-7.

Unfortunately, there is past and existing conflict between members of the Monero community and i2pd developers. fluffypony and anonimal expressed disappointment working with the development i2pd development team, and orignal feels like Kovri was a project "stolen" from them. Furthermore, orignal threatened to explicitly disallow Monero from using future i2pd updates in its license. It's not best to build out critical Monero infrastructure that will likely not be supported.

Furthermore, i2p-java and Kovri developers complain about the general construction of i2pd's code.

## The "i2p-zero / i2p-java" Solution

knaccc re-introduced the idea of an i2p-java-based system. In its early history, Monero decided not to use i2p-java for the required Java installations, which were bulky and burdensome to UX. However, it is now possible to package all dependencies within the application so a user doesn't need to install anything else. knaccc built [i2p-zero](https://github.com/knaccc/i2p-zero): a zero-dependency i2p-java router. Adding this router would only take a few dozen extra MB.

i2p-java is perhaps the easiest to build basic support for to support goals 1-3. Goals 4-7 could be made possible on android, but iOS would be difficult.

i2p-java developers have been generally positive to the idea, even offering to support the [libsam3](https://github.com/i2p/libsam3) C library. Monero would need to build support to use this library, but once built, desktop clients could easily interact with i2p-java.

i2p-java is the most-supported and oldest i2p router, and it is liberally-licensed. If the Monero community is able to work well with them, I think we should strongly consider this option.

## The "Tor" Solution

vtnerd spent a lot of time working a partial Tor solution. This allows users to trivially connect to Tor to broadcast transactions, fulfilling goals 1 and 2. It could be extended to support other goals, but ultimately, Tor is not as effective for a network-wide implementation, since Monero users will "leech" off Tor's infrastructure without contributing.

While Monero should consider supporting Tor, there are a number of benefits that Monero can get out of other systems that Tor cannot reliably provide to thousands of users.

## The "Dandelion" Solution

Dandelion is a mechanism of using Monero nodes to create an i2p-like system. Users choose "outbound" Monero nodes that they relay the transaction broadcast through before it is sent to the rest of the network. This helps create a layer of network separation.

This generally fulfills goal 1, but it probably doesn't meet the other goals. However, it can be implemented in Monero node software directly, and users can have better network privacy if they are able to use Monero but not i2p, for instance.

Dandelion should be considered as a supplementary option to others. Nodes can support Dandelion and non-Dandelion clearnet connections AND i2p connections. Other cryptocurrencies have adopted Dandelion.

## The "Sekreta" Solution

anonimal introduced [Sekreta](https://gitlab.com/sekreta/sekreta/blob/master/README.md#the-sekreta-plan), which is purported to be a universal API that can be used with any number of anonymizing networks. It plans to incorporate a high level of network success; data cannot easily be decrypted if certain networks are compromised. This could potentially help with goal 2.

However, I believe it fundamentally fails all the other goals compared to other solutions.  The focus is built around not trusting any individual anonymizing network. However, in doing so, you leak metadata across however many systems you decide to use. For goal 1, for instance, your transaction broadcast is protected only by the weakest of the networks. Furthermore, circumstantial evidence from 2 or more networks that would not be meaningful independently could make for powerful heuristics when information is compared across networks.

I believe Sekreta is a solution to problems that Monero doesn't really have right now, and that it works counter to the goals that made Kovri appealing in the first place. I do not believe that, even if built, it would fulfill any of the goals Monero is looking for.

Furthermore, work on Sekreta has not yet begun. It would take significant effort to get it into a useful state. And of course once it got there, it wouldn't really be usable for any purpose.

Sekreta seems to have been introduced out of a deep distrust of other anonymity solutions. While it's important to have these qualities in mind when assessing different solutions, Sekreta does so in a way that removes their entire purpose. [It's nonsensical to me](https://www.reddit.com/r/Monero/comments/aeizzp/never_bring_a_knife_to_a_gun_fight_bring_popcorn/edpyn4x/).

## Other Solutions

There are a number of other possible solutions, including other misc. i2p routers, anonymization networks, etc. These include Loki, different language libraries for SAMv3, and i2p routers in Rust, for instance. While it is important to consider these options, I personally believe I have outlined the most important ones above.

## jtgrassie | 2019-01-21T00:30:26+00:00
A couple of extra comments...

### i2p-zero

I think it's worth pointing out that using i2p-java/i2p-zero, there are a few different ways this could be implemented and probably needs more discussion.

The simplest is likely making use of vtnerd's Tor PR because this makes use of SOCKS code (for connecting to a torsocks daemon) and would be the lowest effort code changes in Monero. i2p-zero would starts a SOCKS server that forwards requests through the i2p network to an i2p destination, which would be exposing a proxy to the nodes listening localhost p2p port. i2p-zero provides a way to bundle the core parts of i2p (router, SAM, i2ptunnel) which could be shipped with the Monero releases for a zero-conf setup for end users. The Tor PR also has  a very nice separation of what goes over an anonymous network and what goes over clearnet.

An alternative would be to use i2p-zero and libsam3 as the bridge between Monero and i2p-zero. This would require a fair bit of coding on the Monero side to integrate, because whilst libsam3 itself is pretty simple, Monero's net code is less so. There are benefits though, such as shared tunnel for in/outbound connections and lower resource usage.

Another alternative discussed today was the possibility of the i2p SOCKS code implementing BIND, which would allow both inbound and outbound tunneling. This is not yet implemented but the i2p-java crew have expressed they would help implement (this and ongoing libsam3 support above - in fact, I must say, they have been really welcoming and offering up support for whichever route we feel is most appropriate for Monero).

### i2pd

Aside from the negative attitudes coming from certain i2pd developers, there is nothing stopping us bundling up i2pd with Monero or basing new work off of it. It's open source and so long as we abide by it's license at the time (which is currently BSD 3-clause), theres nothing stopping us doing that. However, the hostility is concerning and incorporating future upstream changes may become problematic if they changed the license. Whilst I would prefer a pure c/c++ i2p setup, and i2pd looks pretty clean now, for the stated reasons and the fact the i2p-java team are being so helpful and welcoming, I would suggest that the i2p-java/zero route is preferable.

### tini2p

I welcome the thinking here, but IMHO, it looks like a much longer term ambition. We have been holding out on Kovri for such a long time and I feel we need some nearer-term solution.

### Sekreta

This doesn't exist, why would we even want to discuss this at this stage? This is surely a much longer way out and we just have no idea right now if this will ever see the light of day or even if it's ever a desirable solution.

### Kovri

I would love to hear from anyone who has been working on this (other than anonimal) on precisely how viable this actually is right now and how it could be bundled and integrated.


## neuroscr | 2019-01-21T04:14:08+00:00
# Lokinet
	
## Introduction

I’m Ryan from the Lokinet team, and while I wasn't able to make your community meeting, I'd like to at least give a little information about how Lokinet may reach most of your goals in the span of 4 weeks (maybe longer if you have some unsaid requirements here).

[Lokinet](https://github.com/loki-project/loki-network)'s API is a layer 4 virtual network interface, this means any TCP, UDP or ICMP application can use Lokinet today, no need for a libsam, socks or anything like that. By simply changing the hostname you’re addressing, you can access hidden services which, based on a cursory glance of the [Tor support vtnerd has written](https://github.com/monero-project/monero/pull/4988), should be very straightforward to add a fake TLD (like .monero) to send transactions over.

Lokinet has hidden services as well as exits working now, meaning it supports wallets and nodes today. We utilize DNS for additional addressing needs of a mixnet. This allows us to address nodes over clearnet, encrypted and anonymously.

Since [Loki](https://github.com/loki-project/loki) is a Monero fork, our codebases, goals, and problems are very similar. We are a well organized and fully funded team, that with Jeff/majestrate/psi’s vision has built an I2P replacement in under a year with much better UX and interfaces. Using the experience Jeff has from the years of his I2P development, we’ve managed to take the best pieces from existing protocols and made it versioned and modular where I2P is not, see [LLARP High Level Description](https://github.com/loki-project/loki-network/blob/master/docs/high-level.txt). 

Given that Loki is essentially already working on this exact problem, we see no reason why we shouldn’t collaborate on this with Monero. If this community chooses to adopt LLARP/Lokinet, this new protocol gets more eyes and contributors which we wouldn’t otherwise have, and Monero gets a solution that meets all of the requirements laid out within a fairly minimal timeframe, and whilst maintaining a C/C++ codebase. We’re open to several options including a shared global mixnet using Lokinet (having a ton of traffic to hide in) or helping you form your own using the underlying [LLARP](https://loki-project.github.io/loki-docs/Lokinet/LLARP/) protocol (so you’re not “leeching” off others). 

## Moneros Network Goals

I have written an analysis comparing the project goals to Lokinet’s capability below:

```
1. Node transaction broadcast hide IP
```
**Achievable soon**: We just need to modify the Monero code to post the transaction to a different hostname, so we can be directed off the clearnet onto an anonymous path to another node. As said above, with vtnerd’s recent Tor support, this should be very straightforward.

```
2. Node transaction broadcast without censorship
```
**Achievable soon?**: You can broadcast today but what's missing is your “sybil resistance”. I’m not quite sure what you mean by that, as to me none of these options address it and yet there are claims that they do. Lokinet has a “relay firewall” API that will work with the Loki cryptoc that will provide serious sybil resistance when combined with our economics but I’m guessing you don’t want to copy that model exactly. However, Monero could use pieces of that API to develop their own solution using the LLARP protocol.

```
3. Node entirely hidden in anonymizing layer
```
**Complete**: We have run `lokid` completely behind a lokinet client and it has successfully interacted with the `lokid` through Lokinet's exit functionality, with no modification to the daemon.

```
4. Wallet to remote node transaction broadcast
```
**Complete**: Lokinet is already separated into clients and routers. So you don't have to run a "full node" (just a client) to get onto the network or run a SNapp (aka hidden service). Lokinet is designed to be small, mobile-friendly and efficient whether it’s a client or a router. However, Routers are designed to be trusted and audited by each other to ensure this layer of trust.

```
5. Wallet to remote node full synchronization
```
**Complete**: We've done this but why would you want to? As you pointed out it just makes everyone's lives worse. This could be an opt-in feature, but I wouldn’t recommend this be the default.

```
6. Wallet to lightweight server transaction broadcast
```
**Complete**: Any current internet (tcp/udp/icmp) application can be used over Lokinet.

```
7. Wallet to lightweight server full synchronization
```
**Complete**: See 6. We also have an inter-network addressing scheme, where you can drop the anonymity and keep the encryption for trusted node-to-node communication (Service Nodes in the Loki cryptoc use-case) on Lokinet. This could easily be changed.

---

**Mobile**: Lokinet is made as a C++ library that should be easily dropped into other projects. We are also interested in native iOS / Android support.


---

**Footprint**: We can run on a raspi1, very little memory and cpu footprint. Also, it would not add extra size to any distribution and would not inherit any security vulnerabilities from any JDK.

---

**License**: We use a [zlib-style license](https://github.com/loki-project/loki-network/blob/master/LICENSE) which is very liberal.

---

On paper, LLARP/Lokinet seem to fit the bill quite well, but there are drawbacks, namely with project maturity and security auditing. Lokinet is still a work in progress, we’re currently integrating with several loki cryptoc services and improving its UX and code However, we have a pretty solid MVP working today with [user facing documentation](https://loki-project.github.io/loki-docs/Lokinet/LokinetOverview/), and [the start of our developer documentation](https://github.com/loki-project/loki-network/tree/master/docs) for which we will be engaging security auditors in the medium term. 

Let us know if you have any questions or need any clarifications. [Majestrate (Jeff/psi)](https://github.com/majestrate), [michael-loki](https://github.com/michael-loki), [KeeJef](https://github.com/keejef/), [tewinget](https://github.com/tewinget), and I will be available to contribute. We’re readily available at #llarp on freenode or [https://discord.gg/eB8k6xQ](https://discord.gg/eB8k6xQ). Or for even more fun, join us on the [secret Lokinet IRC…](https://loki-project.github.io/loki-docs/Lokinet/Guides/LokinetIRC/)


## jtgrassie | 2019-01-21T05:18:19+00:00
@neuroscr thanks for your detailed overview of LLARP/LokiNET. It's certainly worth discussion at some point, but just in my opinion, I don't think right now is that time, simply because of:

> but there are drawbacks, namely with project maturity and security auditing

Tor and i2p are far ahead in terms of maturity, network size and auditing. And whilst there maybe better alternatives in the pipeline so to speak, I think for a currency the size of Monero, we can't be too hasty implementing something without these aspects. This is not to say there couldn't be a parallel path of development adding LLARP/LokiNET as another privacy network option, but right now the focus, again IMO, needs to stay on Tor & i2p integration. The latter of which being bundled with Monero with a zero-conf use-case so novice users get a layer of network privacy by default.

## MoroccanMalinois | 2019-01-21T12:22:53+00:00
@SamsungGalaxyPlayer 

> It is difficult for an outsider to tell how polished Kovri is

It is _marginally_ polished, so marginally that i2pd is in much better state

@jtgrassie 

> I would love to hear from anyone who has been working on this (other than anonimal) on precisely how viable this actually is right now and how it could be bundled and integrated.

I would not trust it for anything barely critical. It's in a very bad shape. fwiw, i'd be strongly against any kind of integration with monero in the current situation. 

## vtnerd | 2019-01-21T21:48:58+00:00
Tor meets all of the listed goals. Whether its better at protecting privacy and better suited for hidden services, etc., is another discussion. As an example I have a patch where `monero-wallet-cli` is synchronizing with a `monerod` over a Tor hidden service. The patch should be compatible with the various i2p solutions too. The user does have to manually setup the hidden service forwarding to `monerod`.

## SamsungGalaxyPlayer | 2019-01-21T22:40:45+00:00
This meeting was divided among two channels for various reasons. Here are the logs:

**#kovri**: https://www.irccloud.com/pastebin/UqEpxgYe/Kovri%20meeting%202019.01.21

**#monero-community**: https://www.irccloud.com/pastebin/R7wfEZA0/Monero%20meeting%202019.01.21

# Action History
- Created by: SamsungGalaxyPlayer | 2019-01-20T17:42:43+00:00
- Closed at: 2019-01-22T15:04:16+00:00
