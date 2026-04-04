---
title: I2P and Tor Seed Nodes + Other Weird Stuff
source_url: https://github.com/monero-project/monero/issues/6380
author: vtnerd
assignees: []
labels: []
created_at: '2020-03-11T00:59:13+00:00'
updated_at: '2020-11-11T05:03:43+00:00'
type: issue
status: closed
closed_at: '2020-11-11T05:03:43+00:00'
---

# Original Description
My original proposal included hard-coded I2P and Tor seed nodes, similar to IP seed nodes in the  codebase. @moneromooo-monero asked questions about sharing I2P/Tor addresses over IP, so that _additional_ seed nodes for these networks are not needed. Apologies for the length, but there is no other way to describe potential issues but with detail. See section at end for summary.

After "red-teaming" things a bit:

### P2P `peer_id` Problems
The `peer_id` field in the p2p protocol has been used to identify when a node unintentionally connects to itself. This can occur due to NATing - the node may not "know" its real external IP to the internet, and therefore a randomized 64-bit value is used as a quick technique to determine if the node is trying to connect to itself. For privacy purposes, each network type (ipv4/6, i2p and tor) all use different randomly generated `peer_id` values so there aren't clear associations to link an IP address to an I2P/Tor connection (see some recent PRs too).

Unfortunately, this identifier is persistent _within_ a single run of `monerod`, so it can be used to identify outbound connections from the same source. In other words, all outbound Tor connections from a node will have a unique identifier, and all outbound I2P connections will have a separate unique identifier. This will allow a spy to link associated transactions, even as the daemon is "rotating" its use of outbound connections to send transactions.

Either the `peer_id` needs to be permanently cleared over I2P/Tor OR a uniquely generate value per connection attempt needs to be created. The former is susceptible to self-connections if the user misconfigures the daemon with an incorrect inbound I2P/Tor address.

### I2P/Tor -> IP attack
Uniquely generated I2P/Tor addresses are shared over a specific outbound I2P/Tor connection (the victims inbound connection), then IP p2p traffic is watched to spot these unique addresses similar to how a botnet would watch for tx broadcasts. The attack may not work because the remote I2P/Tor node could share these unique addresses over I2P/Tor before sharing them over IP. However, an attacker can send a unique address over I2P/Tor, then immediately request peerlists over IP to help with the search. 

One suggested mitigation is an "opt-in" for sharing received I2P/Tor addresses over the IP network. This way, only publicly known Monero nodes could have their true IP address "leaked" to an I2P/Tor address (which isn't really a leak).

Combining this technique with the above attack (`peer_id`), allows an attacker to link the unique `peer_id` for I2P/Tor to an IP address. The attacker would have to get lucky (the public node would have to choose them as an outbound I2P/Tor connection), but while the attack was active, all transactions sent from that node over I2P/Tor can be immediately sourced to an IP address. Since its a public relay, this is less terrible than other situations but not awesome since its definitely not expected. So fixing the above is useful to prevent this attack.

This entire attack can also be mitigated with unique I2P/Tor seed nodes.

### IP -> I2P/Tor Attack
The opposite attack is also possible, where a node generates unique I2P/Tor addresses and shares them with a specific IP address. Similar to the reverse attack, the victim node is going to share these addresses creating complications, but an attacker can increase their chances by requesting peerlists for suspected connections. This would leak an I2P/Tor connections to an IP address. This attack requires the victim unlucky to connect outbound to the attacker.

EDIT: I forgot to mention, the attacker cannot control the selected outbound connections. So this isn't guaranteed to be possible in all cases, but sybiling increases chances.

Altering the behavior of p2p peerlist sharing will need to be done to fully mitigate this risk. Some randomized delay usage of peerlist information and altering the `TIME_SYNC` p2p command entirely so that the peerlist is not sent by request. The latter is arguably more important.

This entire attack can also be mitigated with unique I2P/Tor seed nodes.

### I2P/Tor -> I2P/Tor Attack
Same as IP -> I2P/Tor except attempting to determine the related active connections of a node. This never leaks IP address, only related connections on the same network (related I2P connections and related Tor connections). This could potentially leak related transactions.

The mitigations are randomized peerlist sharing, p2p protocol changes, and connection rotating (occasional disconnects and selecting another peer). I think rotating connections should make this difficult enough.

### Summary
The easiest/safest technique for I2P/Tor seeding is separate hard-coded addresses for each network type. An opt-in strategy where a node takes I2P/Tor addresses to the IP network is _mostly_ workable, but could use additional work to "shore-up" some weird privacy edge cases.

My recommendation is unique seed nodes or immediately commit to working on additional mitigations (randomized peerlist sharing and p2p `TIMED_SYNC` changes). And FYI, I'm not thrilled about another CCS for these mitigations because they aren't easy, might be overkill, and might not work - this isn't a secret plea for whole bunch more billable hours. That said, altering peerlist behavior might be useful for I2P/Tor->I2P/Tor sharing too.

### Additional Recommendations (resulting from all of this probing and not yet planned):
Random `peer_id` per connection attempt over I2P/Tor seems basically mandatory for privacy. Or clearing the value depending on the difficulty of the change (haven't spec'ed it yet).

Rotating (disconnecting/reconnecting) outbound I2P/Tor connections is also desirable to reduce multiple transactions from being sent during a single connection (which links the two transactions as being related IF the node is not a public relay). However, this creates more opportunities for a node to connect to a sybil attacker. At this point, even my head is spinning. Still, rotating connections is probably desireable.

# Discussion History
## ghost | 2020-03-11T09:51:01+00:00
# P2P peer_id Problems

Just allow a node to connect to itself, and get rid of this fingerprint.

# I2P/Tor -> IP attack

The proper way to run a hidden service is to avoid IP traffic all together. The part "then IP p2p traffic is watched to spot these ..." won't be possible.

# IP -> I2P/Tor Attack

Same above, so "shares them with a specific IP address" could not be pull off.

# I2P/Tor -> I2P/Tor Attack

I don't see how this is possible since the service is completely hidden.


## sumogr | 2020-03-11T11:36:43+00:00
in my very very humble opinion and with way less knowledge compared to yours
regarding peer id there are three options.
1. allow loopbacks altogether like winnie the pooh suggested above and remove peer ids
2. regenerate the peer id in random short intervals and remove logging of it on peerlists peer info (you ll have to solve how to allow loopbacks when asked for though. At the moment its done by searching for the peer id on local peerlists )
3. get your local public ip (for example ask it back from the first remote you connect to) and ban it unless explicitly allowed
For the rest first prove and replicate the theoretical attack and then strain your head trying to patch it (peerlists system though ingenious is leaking and is vulnerable from many sides that is a proven fact)

## hyc | 2020-03-11T18:35:09+00:00
I see no problem with generating a new peer ID on each connection attempt and detecting it again on the incoming side. This seems to be a trivially fixable issue.

## vtnerd | 2020-03-11T20:49:56+00:00
> ### P2P peer_id Problems
>
> Just allow a node to connect to itself, and get rid of this fingerprint.

Yes, that was one of two suggestions.

> ### I2P/Tor -> IP attack
>
> The proper way to run a hidden service is to avoid IP traffic all together. The part "then IP p2p traffic is watched to spot these ..." won't be possible.

I'm not sure what you mean. My suggestion above was to not share information across network types, which is what you might be saying. But this comes with the downsides of requiring seed nodes for each network type.

If you meant to never use IP in the daemon when using I2P/Tor, this isn't realistic currently. Surrounding node attacks and DoS are bit nasty over I2P/Tor.

> ### I2P/Tor -> I2P/Tor Attack
>
> I don't see how this is possible since the service is completely hidden.

Any state information used across I2P/Tor connections can potentially leak (to an attacker) which of its inbound connections are from the same source. The peerlists are part of the daemons state that can be changed by peers and that information is shared with yet other peers. So peerlists can (potentially) be leveraged to track related connections.

The spy sends unique Tor addresses via the p2p peerlist protocol to the victim connection, and then requests the peerlists of all inbound Tor connections. Inbound connections from the same source will typically return the unique addresses before other nodes are notified of these addresses. And sybil/aliases are cheap.

This isn't a suggestion to drop I2P/Tor usage in the daemon. The attack isn't guaranteed because the victim must do `receive_peer_list -> grey_list -> grey_list_housekeeping -> whitelist -> to_attacker`. And the attacker cannot control when housekeeping occurs, the addresses it selects for housekeeping or the addresses it returns to the attacker. _However_, the attacker: (1) knows exactly when housekeeping occurs (just after the attacker receives the `TIMED_SYNC` request from the victim), (2) can inject multiple cheap sybil/aliases into the peerlist gray table, and (3) can send multiple `TIMED_SYNC` requests below the spam threshold to probe the whitelist table. 

As I tried to make clear, I am uncertain whether the attack is practical. But the attacker has lots of control over state and response in the current protocol design, which is not ideal. My current thoughts are that anyone wanting all connections over I2P/Tor should have an entirely separate "zone" inside of the daemon to isolate information even further (yes, seriously). Also, some protocol/peerlist changes would be useful.

> 1. allow loopbacks altogether like winnie the pooh suggested above and remove peer ids

Yes, that was one of my suggestions. The other was a per-connect attempt id.

> 2. regenerate the peer id in random short intervals and remove logging of it on peerlists peer info (you ll have to solve how to allow loopbacks when asked for though. At the moment its done by searching for the peer id on local peerlists )

Its  preferable to create one per connection attempt, but this suggestion would be another fallback option.

> 3. get your local public ip (for example ask it back from the first remote you connect to) and ban it unless explicitly allowed

This isn't possible. The problem is not within IP networks, the problem is strictly within the I2P or Tor network. The node can avoid connecting to itself if the user specifies the `--anonymous-inbound ...` flag properly, but fails if the user specifies this incorrectly (a new address was generated, etc.)

> For the rest first prove and replicate the theoretical attack and then strain your head trying to patch it (peerlists system though ingenious is leaking and is vulnerable from many sides that is a proven fact)

The question was whether sharing peerlists between network types was privacy safe. This type of state sharing increases the attack surface, which was the point of the issue. The attacks aren't "dead simple", so accepting the risk and avoiding the additional hard-coded seeds might be worth it. 

I think at a minimum, yet-another runtime option to filter addresses received from other network types should be provided. The most cautious users can enable that flag.

> I see no problem with generating a new peer ID on each connection attempt and detecting it again on the incoming side. This seems to be a trivially fixable issue.

Agreed. It might be funky due to the current implementation, but we've got far more complicated code this in Monero.

## ghost | 2020-03-11T21:18:56+00:00
> > ### I2P/Tor -> IP attack
> > The proper way to run a hidden service is to avoid IP traffic all together. The part "then IP p2p traffic is watched to spot these ..." won't be possible.

> If you meant to never use IP in the daemon when using I2P/Tor, this isn't realistic currently. Surrounding node attacks and DoS are bit nasty over I2P/Tor.

Yes that's what I meant. Either block clear net at the firewall level, or add some flag in monerod to prevent ipv4. This is currently _not_ unrealistic, are you suggesting tor hidden services are generally broken?

> 
> > ### I2P/Tor -> I2P/Tor Attack
> > I don't see how this is possible since the service is completely hidden.
> 
> ... So peerlists can (potentially) be leveraged to track related connections.

It's just a table of hidden service addresses and unused ip addresses, assuming clear net is blocked. What can an adversary get from looking at these? If the problem is DDoS, then we are back at the validity of the previous assumption, that is tor hidden services are generally vulnerable, but are they?


## vtnerd | 2020-03-11T22:09:29+00:00
> Yes that's what I meant. Either block clear net at the firewall level, or add some flag in monerod to prevent ipv4. This is currently not unrealistic, are you suggesting tor hidden services are generally broken?

Blocking clearnet entirely is not recommended without additional work/research. A new Tor address can be made cheaply, to facilitate [eclipse attacks](https://www.usenix.org/node/190891). Two possible mitigations are (1) requiring PoW for connections and (2) some kind of prefix matching for addresses (prefer addresses with the same prefix). This isn't necessarily an issue within Tor, but is a limitation of how information is provided for PoW blockchains.

Inbound Tor connections are also currently difficult to deal with for DoS purposes.

> It's just a table of hidden service addresses and unused ip addresses, assuming clear net is blocked. What can an adversary get from looking at these? If the problem is DDoS, then we are back at the validity of the previous assumption, that is tor hidden services are generally vulnerable, but are they?

This isn't a bug/attack at the I2P/Tor layer, this is a potential issue within the Monero P2P protocol. Even with the extremely limited commands, the daemon carries state between Tor connections. Once the `peer_id` is corrected, linking two different connections/txes to the same source through peerlist data is not trivial, but not implausible.

And DoS type attacks are terrible for privacy. Available CPU and bandwidth is part of the node state, and is impossible to _not_ leak when the limits are reached. There is lots of research showing that Tor is susceptible to this kind of stuff (researchers have actually attempted it). Luckily this type of attack is targeted and more noisy. "Fixing" this (kind of practical) attack is definitely outside of the bounds of what Monero can offer anytime soon.

## ghost | 2020-03-11T22:37:12+00:00
> > Yes that's what I meant. Either block clear net at the firewall level, or add some flag in monerod to prevent ipv4. This is currently not unrealistic, are you suggesting tor hidden services are generally broken?
> 
>  A new Tor address can be made cheaply, to facilitate [eclipse attacks](https://www.usenix.org/node/190891). 

It also applies to ipv6, therefore it's already an accepted risk.

> Inbound Tor connections are also currently difficult to deal with for DoS purposes.
> 
> > It's just a table of hidden service addresses and unused ip addresses, assuming clear net is blocked. What can an adversary get from looking at these? If the problem is DDoS, then we are back at the validity of the previous assumption, that is tor hidden services are generally vulnerable, but are they?

> And DoS type attacks are terrible for privacy. Available CPU and bandwidth is part of the node state, and is impossible to _not_ leak when the limits are reached.

What can possibly be leaked to an observer when a server's response time is a bit slow? Is it really relevant here?



## vtnerd | 2020-03-11T23:29:04+00:00
> It also applies to ipv6, therefore it's already an accepted risk.

Enabling IPv6 isn't the same as disabling IP. There are less IPv6 addresses, and they are harder  to obtain than an ed25519 pubkey. The rules for IPv4 and IPv6 are more similar than for pubkey overlays. We arguably should do /32 or /64 biases for IPv6 like current /16 for IPv4. Monero might need to find some research paper for recommendations first.

EDIT: There are mitigation strategies, just pointing out that its far easier to obtain many ed25519 keys. The address space is also significantly larger.

> What can possibly be leaked to an observer when a server's response time is a bit slow? Is it really relevant here?

The delayed response is the leak. Available resources are part of the state of any system, and most systems don't randomize response times slower. And yes its relevant because it can be used to identify connections from the same source.

For instance, [Bandwidth Attacks against Tor](https://www.usenix.org/system/files/sec19-jansen.pdf). The primary author is at the US Naval Research Lab, which is interesting because Tor started at that same lab. That paper and similar ones are at least worth a read.

Its also important to remember that Tor has undergone far more research into mitigation strategies than Monero's P2P protocol now being shoved over Tor.

## moneromooo-monero | 2020-03-12T01:11:17+00:00
I agree with the one off peer id (essentially a challenge on connection).
For seed nodes, anonimal mentioned that (at least in i2p) it's possible to have a key/address with many hosts "serving" it. We could therefore have one hardcoded i2p node address with a public private key, and any node using an i2p connection would be one of many replying. I have no idea whether that'd be trivially DoSable (ie, since the private key is public, Eve sets a computer to serve either sybils or bad addresses). Bearing in mind that if Eve broadasts plenty of sybils to the network, they'll end up in the honest seed nodes' peer lists too.

## ghost | 2020-03-12T10:24:45+00:00
> And yes its relevant because it can be used to identify connections from the same source.

Can you explain what "connections from the same source" mean? And how by introducing a controlled delay of a hidden service by active probing, in this case a DoS, can give an attacker this information?



## xiphon | 2020-03-12T13:20:19+00:00
> I see no problem with generating a new peer ID on each connection attempt and detecting it again on the incoming side. This seems to be a trivially fixable issue.

And seems then we can drop peer ID on the server side (server -> client handshake), i.e. always pass a dummy/random one. There is no use for it, cause we only interested in outgoing connections' peer IDs.


## sumogr | 2020-03-12T14:18:42+00:00
i think its overanalysed. occam's razor just regenerate it upon each new connection. its sole purpose of existence (identifying loopbacks) is still valid this way,


## vtnerd | 2020-03-12T15:26:01+00:00
> i think its overanalysed. occam's razor just regenerate it upon each new connection. its sole purpose of existence (identifying loopbacks) is still valid this way,

Which is literally what multiple people have said already, including myself in the original post.

## ghost | 2020-03-14T01:35:21+00:00
Since this thread is already this deep, why not just allow users to tunnel clear net through sock5 / tor? It will fix your second and third problem, and will prevent eclipse attacks.

## vtnerd | 2020-03-14T02:52:41+00:00
> Since this thread is already this deep, why not just allow users to tunnel clear net through sock5 / tor? It will fix your second and third problem, and will prevent eclipse attacks.

This [increases the risk of eclipse attacks](https://arxiv.org/pdf/1410.6079.pdf). The attacker can get exit nodes banned, restricting the supply of exit nodes that are allowed to communicate to the p2p network. The authors of the paper actually attempted this in-the-wild with Bitcoin.

## ghost | 2020-03-14T08:25:18+00:00
This paper only presented that nodes behind tor might be easily fingerprint able on bitcoin network. Stretching it to "This increases the risk of eclipse attacks" is your inference, and I assume clearly not demonstrated. Is this why clear net is not using socks5?

Edit: OK, it seems I missed the point on the part of Exit node. But this is just a theoretical attack, and I think it's not the developer's call to decide if a user should always access the clear net or not.

Edit2: As a side note, if you enable socks5 support for clear net. You can also help those who do not have proper access to internet. They might not be using tor, but probably they already have some sort of socks5 servers around, and you won't be needing some expensive CDN to give them access to the network, they already have their own tools, which might be in the form of a proxy server.

## vtnerd | 2020-03-15T13:57:41+00:00
> Edit: OK, it seems I missed the point on the part of Exit node. But this is just a theoretical attack, and I think it's not the developer's call to decide if a user should always access the clear net or not.

They authors did run some tests against the Bitcoin network:

> We validated this part of the attack by forcing about 7500 running  Bitcoin peers to ban our Exit node. To do this we implemented a rudimentary Bitcoin client which is capable of sending different custom-built Bitcoin messages.

Monero has [~1312 nodes](https://monerohash.com/nodes-distribution.html) and similar properties - there are messages you can send to get an [IP instantly banned](https://github.com/monero-project/monero/blob/19ce033299e213e04d3fb4cda29d2e74f0f04cad/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L479). One of the suggested countermeasures was using hidden services.

Two weaknesses of the paper: (1) they only tried to get their exit node banned _not every other_ exit node (is this what you meant by theoretical?), and (2) the attack is "noisy". In practice, getting a specific `exit node -> monero p2p` route banned is so quick that the real issue is the "noise"  this generates. And as for (2) - Monero RPC can report current bans, but I don't know of any systematic way this is being processed to determine that an attack is in progress. It would probably need to be a part of the P2P protocol since RPC isn't always available. The issue is that it would need to be decentralized, and somehow calculated+reported to the local node.

This isn't argument for preventing users from doing all Monero connections over I2P/Tor, just that sending only transactions over I2P/Tor is the more cautionary approach.

------------------------

> Edit2: As a side note, if you enable socks5 support for clear net. You can also help those who do not have proper access to internet. They might not be using tor, but probably they already have some sort of socks5 servers around, and you won't be needing some expensive CDN to give them access to the network, they already have their own tools, which might be in the form of a proxy server.

Yes it may be useful to some people, but this is unlikely to be the suggested mode of operation and is not relevant to the topic (of safely spreading I2P/Tor hidden service addresses to participants). I never intended to suggest that this mode should never be implemented or used.

## ghost | 2020-03-15T15:40:25+00:00
Fair enough.

The key argument here is that users should decide if they want to tunnel clearnet with socks5/tor, socks5/custom proxy or socks5/i2p, not the developer. I'm not invalidating your concerns, or any possible attacks.

I have no more questions.


## knaccc | 2020-06-14T05:05:35+00:00
@vtnerd 
> The easiest/safest technique for I2P/Tor seeding is separate hard-coded addresses for each network type

Great, I agree. We already have a few volunteers that are running mipseeds (see https://github.com/i2p-zero/i2p-zero/blob/master/mipseed.md). Even better, if they ever cease to be able to volunteer, it's easy for them to provide their server tunnel private key to someone else, so that someone else can seamlessly take over the running of the mipseed.

@moneromooo-monero 
> For seed nodes, anonimal mentioned that (at least in i2p) it's possible to have a key/address with many hosts "serving" it. We could therefore have one hardcoded i2p node address with a public private key, and any node using an i2p connection would be one of many replying.

I asked the I2P devs about this, and it's a planned feature. It does not currently exist. Right now, only one I2P node can listen on a particular I2P b32 address.


# Action History
- Created by: vtnerd | 2020-03-11T00:59:13+00:00
- Closed at: 2020-11-11T05:03:43+00:00
