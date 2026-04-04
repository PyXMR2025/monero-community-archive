---
title: The Public Remote Node Problem
source_url: https://github.com/monero-project/meta/issues/1079
author: Gingeropolous
assignees: []
labels: []
created_at: '2024-09-19T13:49:00+00:00'
updated_at: '2025-01-05T21:07:06+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Monero’s remote node problem

As we’re all aware, the cryptosphere is abuzz with the recent leaked chainalysis video, in which they claim the ability to track monero transactions. One of their approaches is the _incredibly sophisticated_ method of running a remote node and tracking the users that connect to it and the txs pushed by it. 

As the one semi-responsible for the proliferation of the use of remote nodes, I feel I should take it upon myself to try and stir up our approach to this infrastructure hack that is the remote node network. 

It was, and still is, a hack to allow users to hold their own keys and transact on the monero network without downloading the blockchain. This is obviously useful for those using wallets on their phones or other low-storage, not-always-on devices. However, there are clear downsides as demonstrated by the chainalysis intrusion – anyone can operate a remote node, including spies. 

### The Rationale for the remote node network
In my mind, the counterpoint has always been that with the availability of the “instant-on” nature of a new user using the Monero-GUI with a remote node, the user is more likely to keep using the Monero GUI instead of becoming impatient with the initial-blockchain download and abandoning the Monero GUI for some third party solution that has a high probability of being a scam wallet such as Freewallet or any number of wallets you’ve never heard of (but somehow users on r/monerosupport have found.)

Furthermore, once the GUI is installed, there’s a higher probability that the user will actually sync their own blockchain.

(However, one could argue that most new users are on mobile, so the behavior of the GUI is relatively moot). 

### The existing landscape
In order for everyone to be on the same page, the current state of the remote node network is as follows, as far as I’m aware. Node operators can open their RPC port to allow users to connect to their node to obtain blockchain data and to push transactions. This can either be done manually, using a combination of –rpc-restricted-bind-port and –rpc-bind-ip  and (I think) –restricted-rpc. Or, one can use an “automatic” configuration, using the  --public-node, which “Allow other users to use the node as a remote (restricted RPC mode, view-only commands) and advertise it over P2P.” In the manual configuration, the node operator then needs to advertise their node via a directory service like monero.fail , or have their node IP in a domain name DNS entry, like node.moneroworld.com. Additionally, there are some directory providers that scan the monero p2p network for open RPC ports (18089 as opposed to 18081) and then serve those IP addresses via DNS in a geolocated manner to end users that connect, like opennode.xmr-tw.org. In the automatic configuration, the node now indicates to the monero p2p network that its RPC port is open. The automatic configuration and its p2p listing are used by the monero GUI in simple mode, such that a simple mode GUI user is connected to a random monero node that has the –public-node flag active. As far as I’m aware, most mobile wallets do not use the monero p2p network listing, but instead offer defaults, usually hosted by the wallet provider (like xmr-node.cakewallet.com). 

## Anyway, lets list our options.

I won’t list this as one of the options because it makes a hierarchy weird, but this is our base state: Do nothing. Things are fine, and remote node operators and directory providers just need to do a better job keeping their resources trustworthy, and users should understand the risk and accept the risks of using another persons node. 
Pros: Easy.
Cons: Trustful, doesn’t really address the problem. Puts high expectations on users to be knowledgeable of the risks, and expects remote node operators and directory providers to be super l33t. 

### Option 1: Attempt to shut down the remote node network. Disable the simple and bootstrap option in the monero GUI.
Pros: Easy to disable in GUI
Cons: Unknown whether the entire community will shut down their remote node operations. Users that use remote nodes will seek other solutions, and some percentage of them may be worse than the current situation. Remote nodes that remain will probably be spy nodes. 

### Option 2: Flood the monero network with remote nodes. Design the daemon software so that the RPC port is open by default, even for GUI users. 
Pros: Relatively easy to implement, code-wise.
Cons: Unknown how effective this could be, considering some % of users will be behind a firewall that they don’t know how to open. Spy nodes still exist, but its less likely users connect to them. Honestly not really a great option. 

### Option 3: i2pify / torify all the things. Get i2p and/or tor baked into the monero software so that remote nodes can only offer hidden services, and remote-node users can only connect via i2p and/or tor. 
Pros: really takes care of the whole thing, at least regarding IP association. 
Cons: heavy, heavy code work (relative to other options), and some of it falls on 3rd party developers for mobile wallets. Unless its bisq-like (where things just happen using tor, no user initiative needed), it probably won’t be used. 

### Option 4: modify remote node network behavior to make it better. For instance, can the RPC enabled nodes perform their own kind of dandelion? 
Pros: probably easier than baking in i2p
Cons: depends on numerous RPC nodes existing, might require 2 to be most effective. Ends up being just another shell game, in which a high penetration of spy nodes renders this countermeasure useless. 

### Option 5: find a way to make the blockchain size constant relative to time, and ideally constant relative to output count.
(added by @preland )
Pros: everyone and their dog will eventually (or maybe even immediately depending on how small it can be made) be able to trivially run their own node, even on smartphones. This will not only fix the spy node issue, but will also make the network much more secure.
Cons: This may be impossible to do, and is at the very least very difficult. This would likely be bottlenecked by FCMP, as the changes made by FCMP would almost definitely influence the implementation.

So far, options 2-4 really address only the IP tracing. None of these options address the fact that malicious remote nodes can offer poisoned data. I think there are aspects of seraphis / jamtis that function as countermeasures for poison data delivery. 

Any other options people can think of? 

# Discussion History
## preland | 2024-09-19T15:27:00+00:00
Another option would be fixing the root problem: most mainstream users don’t want to/can’t download and maintain the entire blockchain in its current state. This issue will only get worse over time, as blockchain size increases et infinitum. This aspect of the blockchain size will also effect option 3, to the extent that i2p would be the only realistic (and let’s face it: moral) option due to bandwidth constraints on “exit” nodes, and this would only get worse as time goes on.

### Option 5: find a way to make the blockchain size constant relative to time, and ideally constant relative to output count.
Pros: everyone and their dog will eventually (or maybe even immediately depending on how small it can be made) be able to trivially run their own node, even on smartphones. This will not only fix the spy node issue, but will also make the network much more secure.
Cons: This may be impossible to do, and is at the very least very difficult. This would likely be bottlenecked by FCMP, as the changes made by FCMP would almost definitely influence the implementation. 

## nahuhh | 2024-09-20T11:31:17+00:00
> Monero’s remote node problem
> 
> As we’re all aware, the cryptosphere is abuzz with the recent leaked chainalysis video, in which they claim the ability to track monero transactions. 

They don't claim the ability to track monero transactions.

> One of their approaches is the _incredibly sophisticated_ method of running a remote node and tracking the users that connect to it and the txs pushed by it. 

method of using @Gingeropolous's proxy 

> As the one semi-responsible for the proliferation of the use of remote nodes, I feel I should take it upon myself to try and stir up our approach to this infrastructure hack that is the remote node network. 

Even though you run a, or multiple, nides yourself, youre also directly responsible for forwarding users traffic directly to chainalysis / feds.

> It was, and still is, a hack to allow users to hold their own keys and transact on the monero network without downloading the blockchain.

No it isnt. It's literally by design.
Electrum is a "hack".
Monero wallets are a separate piece of software (not a part of monerod). They are (by design) intended to connect to an external node. Whether the node is on localhost, LAN or across the ocean is just a matter of an ip address change.

> This is obviously useful for those using wallets on their phones or other low-storage, not-always-on devices. However, there are clear downsides as demonstrated by the chainalysis intrusion – anyone can operate a remote node, including spies. 

All nodes are "remote nodes" in relation to the walet software. Again, monerod does not contain a wallet.

You sound like youre writing about bitcoin and electrum...

> ### The Rationale for the remote node network
> In my mind, the counterpoint has always been that with the availability of the “instant-on” nature of a new user using the Monero-GUI with a remote node, the user is more likely to keep using the Monero GUI instead of becoming impatient with the initial-blockchain download and abandoning the Monero GUI for some third party solution that has a high probability of being a scam wallet such as Freewallet or any number of wallets you’ve never heard of (but somehow users on r/monerosupport have found.)

You must be referring to simple/bootstrap mode. Monero GUI also includes monerod ajd the ability to run a full node.

Bootstrap mode being bad has nothing to do with the ability to use remote nodes. It's bad because the nodes that it chooses are nodes which had to opt in to --public-node, and are very likely to be honeypot nodes.

> Furthermore, once the GUI is installed, there’s a higher probability that the user will actually sync their own blockchain.
> 
> (However, one could argue that most new users are on mobile, so the behavior of the GUI is relatively moot). 

I'm not at all understanding what youre getting at. monerujo is the only wallet that randomly chooses a node from a list. None of the mobile wallets use simple/bootstrap mode, as that requires monerod.

> ### The existing landscape
> In order for everyone to be on the same page, the current state of the remote node network is as follows, as far as I’m aware. Node operators can open their RPC port to allow users to connect to their node to obtain blockchain data and to push transactions. 

> This can either be done manually, using a combination of –rpc-restricted-bind-port and –rpc-bind-ip  and (I think) –restricted-rpc.

--rpc-restricted-bind-ip
--rpc-restricted-bind-port

> Or, one can use an “automatic” configuration, using the  --public-node, which “Allow other users to use the node as a remote (restricted RPC mode, view-only commands) and advertise it over P2P.” 

> In the manual configuration, the node operator then needs to advertise their node via a directory service like monero.fail , or have their node IP in a domain name DNS entry, like node.moneroworld.com. Additionally, there are some directory providers that scan the monero p2p network for open RPC ports (18089 as opposed to 18081) and then serve those IP addresses via DNS in a geolocated manner to end users that connect, like opennode.xmr-tw.org.

the crazy thing is that you proxied node.moneroworld.com to spy nodes AND to another proxy.

> In the automatic configuration, the node now indicates to the monero p2p network that its RPC port is open. The automatic configuration and its p2p listing are used by the monero GUI in simple mode, such that a simple mode GUI user is connected to a random monero node that has the –public-node flag active. As far as I’m aware, most mobile wallets do not use the monero p2p network listing, but instead offer defaults, usually hosted by the wallet provider (like xmr-node.cakewallet.com). 

you can connect a mobile wallet to a node that uses bootstrap mode and use the nkde as a proxy...

> ## Anyway, lets list our options.
> 
> I won’t list this as one of the options because it makes a hierarchy weird, but this is our base state: Do nothing. Things are fine, and remote node operators and directory providers just need to do a better job keeping their resources trustworthy, and users should understand the risk and accept the risks of using another persons node. 
> Pros: Easy.
> Cons: Trustful, doesn’t really address the problem. Puts high expectations on users to be knowledgeable of the risks, and expects remote node operators and directory providers to be super l33t. 

the problem is always trust.
The only knowledge it expects of users is for them to understand that, if using clearnet, the receiving node can correlate your IP to the TX that your submitting directly to the nodes RPC port. Your ISP can as well.

> ### Option 1: Attempt to shut down the remote node network. Disable the simple and bootstrap option in the monero GUI.
> Pros: Easy to disable in GUI
> Cons: Unknown whether the entire community will shut down their remote node operations. Users that use remote nodes will seek other solutions, and some percentage of them may be worse than the current situation. Remote nodes that remain will probably be spy nodes. 

Kill --public-node = good
Kill bootsstraps "auto" mode = good

Shut down remote node network? What are you even talking about. All nodes are remote in relation to wallets. 

killing bootstrap mode isnt necessary. I can specify whatever node i feel like, whether i run it locally or not.

killing remote nodes isnt even possible without forcing monero to behave like btc, which is worse for privacy (everyone usinf electrum).

> ### Option 2: Flood the monero network with remote nodes. Design the daemon software so that the RPC port is open by default, even for GUI users. 
> Pros: Relatively easy to implement, code-wise.
> Cons: Unknown how effective this could be, considering some % of users will be behind a firewall that they don’t know how to open. Spy nodes still exist, but its less likely users connect to them. Honestly not really a great option. 

retarded.

> ### Option 3: i2pify / torify all the things. Get i2p and/or tor baked into the monero software so that remote nodes can only offer hidden services, and remote-node users can only connect via i2p and/or tor. 
> Pros: really takes care of the whole thing, at least regarding IP association. 
> Cons: heavy, heavy code work (relative to other options), and some of it falls on 3rd party developers for mobile wallets. Unless its bisq-like (where things just happen using tor, no user initiative needed), it probably won’t be used. 

the code work for this isnt heavy heavy, what r u talking about?? still a stupid idea.
Do you even know how tor/i2p work?? They are essentially port forwarding .... if i can port forward to onion, i can port forward to clearnet. Theres nothing stopping me from serving my "onion-only" rpc to a clearnet bind via iptables, ssh port forwarding or many other solutions. 

> ### Option 4: modify remote node network behavior to make it better. For instance, can the RPC enabled nodes perform their own kind of dandelion? 
> Pros: probably easier than baking in i2p
> Cons: depends on numerous RPC nodes existing, might require 2 to be most effective. Ends up being just another shell game, in which a high penetration of spy nodes renders this countermeasure useless. 

😑😑😑 are you trolling

> ### Option 5: find a way to make the blockchain size constant relative to time, and ideally constant relative to output count.
> (added by @preland )
> Pros: everyone and their dog will eventually (or maybe even immediately depending on how small it can be made) be able to trivially run their own node, even on smartphones. This will not only fix the spy node issue, but will also make the network much more secure.
> Cons: This may be impossible to do, and is at the very least very difficult. This would likely be bottlenecked by FCMP, as the changes made by FCMP would almost definitely influence the implementation.

If everyone runs a node, its the same as broadcasting your tx yourself. Its not good for privacy. 
It literally does NOTHING to address privacy concerns.

## preland | 2024-09-20T12:41:59+00:00
Doesn't Dandelion++ mitigate linking IP addresses with transactions? (As long as you are running your own node and not using an untrusted node) If so, I don't see how everyone running a node would harm privacy.

## nahuhh | 2024-09-20T13:29:35+00:00
> Doesn't Dandelion++ mitigate linking IP addresses with transactions? (As long as you are running your own node and not using an untrusted node) If so, I don't see how everyone running a node would harm privacy.

I don't want to get into details, but the tldr is:

you cant trust dandelion, due to design choices / flaws. 

The majority of nodes allow me to know that they are the origin

--tx-proxy using tor + i2p isnt a perfect solution, but is much better for both propagation times and privacy.

the problem is that we haven't seen anonymous-inbound or hidden services get attacked / sybilled yet, and its very attackable. Its not a panacea either. disable_noise on tx-proxy helps, as it acts similar to feathers multibroadcast. 
Relying on external networks is never a good idea though. Tor onion services were attacked brutally a few months ago and a lot of onions were completely unreachable. I2p has had its own ddos issues in the past as well. 

## Gingeropolous | 2024-09-20T19:02:24+00:00
> > Monero’s remote node problem
> > As we’re all aware, the cryptosphere is abuzz with the recent leaked chainalysis video, in which they claim the ability to track monero transactions.
> 
> They don't claim the ability to track monero transactions.
> 
> > One of their approaches is the _incredibly sophisticated_ method of running a remote node and tracking the users that connect to it and the txs pushed by it.
> 
> method of using @Gingeropolous's proxy
> 
> > As the one semi-responsible for the proliferation of the use of remote nodes, I feel I should take it upon myself to try and stir up our approach to this infrastructure hack that is the remote node network.
> 
> Even though you run a, or multiple, nides yourself, youre also directly responsible for forwarding users traffic directly to chainalysis / feds.
> 
> > It was, and still is, a hack to allow users to hold their own keys and transact on the monero network without downloading the blockchain.
> 
> No it isnt. It's literally by design. Electrum is a "hack". Monero wallets are a separate piece of software (not a part of monerod). They are (by design) intended to connect to an external node. Whether the node is on localhost, LAN or across the ocean is just a matter of an ip address change.
> 

What I mean is that it seems the software was not really designed for 1 monerod to be serving 50+ or 100+ RPC connections. To me, the fact that the old software would allow any RPC connected wallet to initiate mining on the daemon suggests that the original design of the software didn't consider that the wallet user would be different than the daemon user. 

> > This is obviously useful for those using wallets on their phones or other low-storage, not-always-on devices. However, there are clear downsides as demonstrated by the chainalysis intrusion – anyone can operate a remote node, including spies.
> 
> All nodes are "remote nodes" in relation to the walet software. Again, monerod does not contain a wallet.
> 
> You sound like youre writing about bitcoin and electrum...
> 
> > ### The Rationale for the remote node network
> > In my mind, the counterpoint has always been that with the availability of the “instant-on” nature of a new user using the Monero-GUI with a remote node, the user is more likely to keep using the Monero GUI instead of becoming impatient with the initial-blockchain download and abandoning the Monero GUI for some third party solution that has a high probability of being a scam wallet such as Freewallet or any number of wallets you’ve never heard of (but somehow users on r/monerosupport have found.)
> 
> You must be referring to simple/bootstrap mode. Monero GUI also includes monerod ajd the ability to run a full node.
> 
> Bootstrap mode being bad has nothing to do with the ability to use remote nodes. It's bad because the nodes that it chooses are nodes which had to opt in to --public-node, and are very likely to be honeypot nodes.
> 
> > Furthermore, once the GUI is installed, there’s a higher probability that the user will actually sync their own blockchain.
> > (However, one could argue that most new users are on mobile, so the behavior of the GUI is relatively moot).
> 
> I'm not at all understanding what youre getting at. monerujo is the only wallet that randomly chooses a node from a list. None of the mobile wallets use simple/bootstrap mode, as that requires monerod.

What I was getting at is that a reason for a network of available remote nodes to exist is that a new user will have an instant-on user experience, and be more likely to continue running the monero software. However, this is somewhat irrelevant because most new users these days probably are using a mobile wallet. So there's no incentive to provide GUI users with an instant on experience, at least from the perspective of getting them to run their own monerod, eventually.  

> 
> > ### The existing landscape
> > In order for everyone to be on the same page, the current state of the remote node network is as follows, as far as I’m aware. Node operators can open their RPC port to allow users to connect to their node to obtain blockchain data and to push transactions.
> 
> > This can either be done manually, using a combination of –rpc-restricted-bind-port and –rpc-bind-ip  and (I think) –restricted-rpc.
> 
> --rpc-restricted-bind-ip --rpc-restricted-bind-port
> 
> > Or, one can use an “automatic” configuration, using the  --public-node, which “Allow other users to use the node as a remote (restricted RPC mode, view-only commands) and advertise it over P2P.”
> 
> > In the manual configuration, the node operator then needs to advertise their node via a directory service like monero.fail , or have their node IP in a domain name DNS entry, like node.moneroworld.com. Additionally, there are some directory providers that scan the monero p2p network for open RPC ports (18089 as opposed to 18081) and then serve those IP addresses via DNS in a geolocated manner to end users that connect, like opennode.xmr-tw.org.
> 
> the crazy thing is that you proxied node.moneroworld.com to spy nodes AND to another proxy.

I think at one point it was pointing to opennode.xmr-tw.org , and then I switched it to like 5 nodes from members of the community once I became aware that the remote node network  was being infiltrated. afraid.org DNS doesn't allow mixing CNAMES and A records for the same subdomain. 

> 
> > In the automatic configuration, the node now indicates to the monero p2p network that its RPC port is open. The automatic configuration and its p2p listing are used by the monero GUI in simple mode, such that a simple mode GUI user is connected to a random monero node that has the –public-node flag active. As far as I’m aware, most mobile wallets do not use the monero p2p network listing, but instead offer defaults, usually hosted by the wallet provider (like xmr-node.cakewallet.com).
> 
> you can connect a mobile wallet to a node that uses bootstrap mode and use the nkde as a proxy...
> 
> > ## Anyway, lets list our options.
> > I won’t list this as one of the options because it makes a hierarchy weird, but this is our base state: Do nothing. Things are fine, and remote node operators and directory providers just need to do a better job keeping their resources trustworthy, and users should understand the risk and accept the risks of using another persons node.
> > Pros: Easy.
> > Cons: Trustful, doesn’t really address the problem. Puts high expectations on users to be knowledgeable of the risks, and expects remote node operators and directory providers to be super l33t.
> 
> the problem is always trust. The only knowledge it expects of users is for them to understand that, if using clearnet, the receiving node can correlate your IP to the TX that your submitting directly to the nodes RPC port. Your ISP can as well.
> 
> > ### Option 1: Attempt to shut down the remote node network. Disable the simple and bootstrap option in the monero GUI.
> > Pros: Easy to disable in GUI
> > Cons: Unknown whether the entire community will shut down their remote node operations. Users that use remote nodes will seek other solutions, and some percentage of them may be worse than the current situation. Remote nodes that remain will probably be spy nodes.
> 
> Kill --public-node = good Kill bootsstraps "auto" mode = good
> 
> Shut down remote node network? What are you even talking about. All nodes are remote in relation to wallets.

I mean shutting down directory providers or proxies, like monero.fail, opennode.xmr-tw.org, or node.moneroworld, etc. 

> 
> killing bootstrap mode isnt necessary. I can specify whatever node i feel like, whether i run it locally or not.
> 
> killing remote nodes isnt even possible without forcing monero to behave like btc, which is worse for privacy (everyone usinf electrum).

> > ### Option 2: Flood the monero network with remote nodes. Design the daemon software so that the RPC port is open by default, even for GUI users.
> > Pros: Relatively easy to implement, code-wise.
> > Cons: Unknown how effective this could be, considering some % of users will be behind a firewall that they don’t know how to open. Spy nodes still exist, but its less likely users connect to them. Honestly not really a great option.
> 
> retarded.
> 
> > ### Option 3: i2pify / torify all the things. Get i2p and/or tor baked into the monero software so that remote nodes can only offer hidden services, and remote-node users can only connect via i2p and/or tor.
> > Pros: really takes care of the whole thing, at least regarding IP association.
> > Cons: heavy, heavy code work (relative to other options), and some of it falls on 3rd party developers for mobile wallets. Unless its bisq-like (where things just happen using tor, no user initiative needed), it probably won’t be used.
> 
> the code work for this isnt heavy heavy, what r u talking about?? still a stupid idea. Do you even know how tor/i2p work?? They are essentially port forwarding .... if i can port forward to onion, i can port forward to clearnet. Theres nothing stopping me from serving my "onion-only" rpc to a clearnet bind via iptables, ssh port forwarding or many other solutions.
>

Yes, I'm aware. What I'm talking about is providing a user experience like how bisq operates. head to https://bisq.network/ , download their software, and watch it magically connect to the bisq and bitcoin networks using tor, all without the user doing anything. Your average user is not going to be knowledgable or comfortable doing the things you described. 
 
> > ### Option 4: modify remote node network behavior to make it better. For instance, can the RPC enabled nodes perform their own kind of dandelion?
> > Pros: probably easier than baking in i2p
> > Cons: depends on numerous RPC nodes existing, might require 2 to be most effective. Ends up being just another shell game, in which a high penetration of spy nodes renders this countermeasure useless.
> 
> 😑😑😑 are you trolling
> 
> > ### Option 5: find a way to make the blockchain size constant relative to time, and ideally constant relative to output count.
> > (added by @preland )
> > Pros: everyone and their dog will eventually (or maybe even immediately depending on how small it can be made) be able to trivially run their own node, even on smartphones. This will not only fix the spy node issue, but will also make the network much more secure.
> > Cons: This may be impossible to do, and is at the very least very difficult. This would likely be bottlenecked by FCMP, as the changes made by FCMP would almost definitely influence the implementation.
> 
> If everyone runs a node, its the same as broadcasting your tx yourself. Its not good for privacy. It literally does NOTHING to address privacy concerns.

I appreciate your response, but I'm having a hard time gleaning anything that moves us forward. You seem to propose that we do nothing, and continue to expect users to figure out i2p or tor on their own. 

## nahuhh | 2024-09-20T20:09:28+00:00
People like you, pushed for and told ppl to use remote nodes. You, as a "trusted" member of our community, irresponsibly and negligently forwarded users traffic to federal agents. This was against long running advice of "ONLY use nodes where you trust the operator". 

youre still running this proxy smfh. and was still pointed to the TW proxy as of a few days ago.
point it to your own node or fkoff. Youre the problem. Trust is the problem. Trusting people who mishandle your data is the problem.

wallet cli even has a flag for --this-is-probably-a-spy-node

1.
monero doesnt support i2p-sam
monero doesnt support tor control

It should support both, should auto-configure  tx-proxies and anonymous inbounds.

2. monero doesnt even support blockchain sync over tor/i2p.

3. Monero doesnt encrypt p2p network traffic, and uses self signed certs for rpc traffic (which are easy to MITM). peerlist store ip address, not domain names. You can specify certs to use for your node, but only cli has cert pinning. 

4. the root solution to decoy tracking is fcmp.
so sit back and wait.

5. the solution to ip obfuscation for ANY service, is to use a privacy preserving protocol. Whether that be personal vpn using an anon vps, tor, onion or i2p.
you cant use ANY service over clearnet HTTP and expect privacy. Its not monero's job to fix clearnet. 

monero network traffic is easily monitored and intercepted. 
Using a vpn is putting lipstick on a pig.
using tor exit nodes w/o encryption is pointless.
using centrally issued certs requires a domain name.

tldr: solution?
- i2p-sam
- tor control 
- kill the "auto" bootstrap parameter
- onion/i2p remote nodes to be _recommended_ but nothing should prevent anyone from use whatever rpc they manually decide to.

the following wallet all support privacy
  - cake (socks, includes onion node)
  - stack (tor included, default node has a cert but no cert pinning, doesnt include onion node)
  - mysu (socks + tor included + onion and i2p nodes included)
  - anonero (socks + tor enforced)
  - feather  (socks + tor included + onion nodes included)

> expect users to figure out i2p or tor on their own.

GUI is the only major wallet that has terrible defaults and hard to enable privacy protections.
other wallets offer good privacy to their users.

where other wallets slipped up, was trusting node.moneroworld.com. 

stack ONLY ships their own node.
I've advised cake to remove all clearnet nodes that they do not control
speaking to monerujo is a waste of time
feather uses an included tor binary by default, and has onion nodes.

Its _trusted_ node operators + wallet makers jobs to ensure that they are handling your transactions in a private and secure manner.

the problem is simple: people like you who run honeypots like node.moneroworld.com and push(ed) public-node and simple mode, despite well known privacy issues with offering such convenience without any network level protections 

## preland | 2024-09-20T20:37:02+00:00
I am the one who is working on I2P sam integration for monero btw; it’s been a rly tough job for me this past year (plus with me balancing a metric ton of irl stuff while doing it), but I think it should be finished by year’s end (same with neroshop’s I2P integration, though that could take longer since it needs UDP data gram support, which is tougher and currently less documented than TCP). Not sure how long it’ll take to get merged after that point.

## nahuhh | 2024-09-20T20:48:54+00:00
> I am the one who is working on I2P sam integration for monero btw; it’s been a rly tough job for me this past year (plus with me balancing a metric ton of irl stuff while doing it), but I think it should be finished by year’s end (same with neroshop’s I2P integration, though that could take longer since it needs UDP data gram support, which is tougher and currently less documented than TCP). Not sure how long it’ll take to get merged after that point.


also this

https://github.com/monero-project/monero-gui/pull/4337


## preland | 2024-09-20T21:10:22+00:00
> > I am the one who is working on I2P sam integration for monero btw; it’s been a rly tough job for me this past year (plus with me balancing a metric ton of irl stuff while doing it), but I think it should be finished by year’s end (same with neroshop’s I2P integration, though that could take longer since it needs UDP data gram support, which is tougher and currently less documented than TCP). Not sure how long it’ll take to get merged after that point.
> 
> 
> also this
> 
> https://github.com/monero-project/monero-gui/pull/4337
> 

Huh, I wasn't aware that someone had resumed work on the GUI

Tbh that PR was abandoned, so if they can get it working then I'll be happy

## Gingeropolous | 2024-09-21T12:26:25+00:00
again, i wasn't "pointed to the TW proxy as of a few days ago", again because I can't mix cnames and A records. I think that changed that in 2020, like I stated. And in the video the tracing was from 2020. 

I think I'll just point people to monero.fail now, where there is no warning about using a remote node at all, and users should just figure it out. 

>  you cant use ANY service over clearnet HTTP and expect privacy. Its not monero's job to fix clearnet.

I agree. 

> other wallets offer good privacy to their users.

What wallets? As far as I know, people use cake, monerujo, stack, and feather. 

Anyway, it seems your general comment is for option 1, to shut down the public remote node offerings, and for option 3, to get i2p or tor more user friendly.  

## nahuhh | 2024-09-21T13:14:23+00:00
> again, i wasn't "pointed to the TW proxy as of a few days ago", again because I can't mix cnames and A records. I think that changed that in 2020, like I stated. And in the video the tracing was from 2020. 

youre right. My mistake.

> I think I'll just point people to monero.fail now, where there is no warning about using a remote node at all, and users should just figure it out. 

better: you should stop offering any advice.

responsible ppl:
1. Recommend against untrusted nodes
2. Warn about clearnet nodes
3. Advise that onion/i2p rpc are best practice if you must use a remote node, 
4 cont. And tx-proxy / anon inbound especially if its your own node


> > other wallets offer good privacy to their users.
> 
> What wallets? As far as I know, people use cake, monerujo, stack, and feather. 

Feather, stack, and mysu include tor daemons by default
feather, mysu, cake support i2p via socks
monerujo supports tor via orbot, but implementation is terrible
cake supports tor via socks

feather enables tor by default
anonero forces tor by default

feather includes onion nodes
cake includes onion nodes
mysu includes onion and i2p nodes

etc.

> Anyway, it seems your general comment is for option 1, to shut down the public remote node offerings, and for option 3, to get i2p or tor more user friendly.  

I literally said
Dev:
kill "auto" bootstrap
kill --public-node

users:
emphasize that "trust" = real trust
clearnet is not friendly, even if you trust the node op. Use onion/i2p for sending tx¹

wallets:
enable cert pinning
¹prefer onion/i2p for sending transactions

node runners:
setup tx-proxy and anon inbound


## jeffro256 | 2024-09-21T15:13:37+00:00
Option 6: 

Write a new type of wallet that crawls the p2p network, verifies PoW, and downloads block data from peers. All calculations (fee calc, decoy selection, FCMP tree building) are performed by pulling against data which is verified to be part of the blockchain. Then broadcast transactions *only* over an anonymity network to random peers. This type of wallet would be a lot more expensive to run than today's full wallet, but much less expensive than a full wallet + local node, and without the storage requirements. This would have a "leeching" effect on the p2p protocol, which might negatively effect node-to-node traffic. 

## monero-love | 2024-09-21T17:27:44+00:00
Something I think should be taken into consideration is that in parts of the world where monero and privacy are paramount for decedents activists, journalists and the like, think Venezuela, Iran, and the United States, downloading the whole blockchain on spotty connections with a netbook from 2009 all the while keeping it synced is a big ask. 

Sure, you can get a VPS at a non-KYC host and run a node independently, but some folks don't have the means, skills, or time to do so. How will you fire up Tails and connect to a node without a public node? The barrier to entry for the casual user is still high. That isn't just a Monero-specific problem. Gupax is incredible and, for the most part, point-and-click, yet casual users still have issues.

[TOR](https://nusenu.medium.com/the-growing-problem-of-malicious-relays-on-the-tor-network-2f14198af548) had/has a similar issue with rouge relays.

Public nodes are necessary, and the community's smart folks will figure out a solution. 

chime in smart folks.

## boldsuck | 2024-09-21T18:04:53+00:00
>     3. Monero doesnt encrypt p2p network traffic, and uses self signed certs for rpc traffic (which are easy to MITM).

I created CAcert.org certificates for all my nodes. Is it useful to create DANE DNS record?
I saw @vtnerd is working on it: [ccs vtnerd 2024-q3](https://ccs.getmonero.org/proposals/vtnerd-2024-q3.html)

> Using a vpn is putting lipstick on a pig.

ROFL

>  kill --public-node

Should we disable/comment out this on the remote nodes as well?

> node runners:
> setup tx-proxy and anon inbound

I have, and anyone who trusts me/my nodes is welcome to use the onion addresses.
There is plenty of bandwidth available.

## preland | 2024-09-21T19:23:14+00:00
> Something I think should be taken into consideration is that in parts of the world where monero and privacy are paramount for decedents activists, journalists and the like, think Venezuela, Iran, and the United States, downloading the whole blockchain on spotty connections with a netbook from 2009 all the while keeping it synced is a big ask.
> 
> Sure, you can get a VPS at a non-KYC host and run a node independently, but some folks don't have the means, skills, or time to do so. How will you fire up Tails and connect to a node without a public node? The barrier to entry for the casual user is still high. That isn't just a Monero-specific problem. Gupax is incredible and, for the most part, point-and-click, yet casual users still have issues.
> 
> [TOR](https://nusenu.medium.com/the-growing-problem-of-malicious-relays-on-the-tor-network-2f14198af548) had/has a similar issue with rouge relays.
> 
> Public nodes are necessary, and the community's smart folks will figure out a solution.
> 
> chime in smart folks.

See option 5 above; this is one of  the reasons why I think the nature of the blockchain itself shouldn’t be overlooked, especially since the issue only grows worse with every passing day, and gets more difficult to retroactively implement and address (ie when it becomes too big a problem, it will already be too late)

## SorenEricMent | 2024-09-22T09:43:26+00:00
There are one more option that is hovering on my mind for several days and I think it is worth to consider it.
Currently there are two ways for an user to initiate a transaction: they either add the tx to their own node's tx pool by RPC, or to use a remote node's public RPC.
Can we modify the client code to populate the tx to the network as they are a running independent node? Or in other words, run a tiny, pseudo Monero node that is only for tx populate use? this doesn't seems to be computational extensive and is practicable for lower end devices.

## Gingeropolous | 2024-09-22T11:03:49+00:00
@SorenEricMent , yeah I think this gets at one of the underlying issues. A remote node user (client) has to download blockchain data from the remote node, craft the transaction, and then the client pushes the transaction to the remote node, which then propagates the tx via dandelion++. 

So the client could "appear" like a normal node when they push the transaction, but the manner in which the client connects and downloads the data (via RPC) makes them different than a normal node. 

So its that connection between "this client downloaded the blockchain data via RPC" and "this same client is pushing this transaction" that can allow the remote node user to associate a given tx with an IP address. 

So yeah, we could do something like a client downloads the needed data from a remote node A, and then disconnects and pushes the tx using remote node B (which could just be a standard node, as you say). But then we get a sybil situation where an attacker could just flood the network with nodes and then be able to make associations because "oh, this client just downloaded this data from node A, but I also own node B and it connected to B to send a tx". 

## thisIsNotTheFoxUrLookingFor | 2024-09-22T13:58:26+00:00
I like option 3.

As for the concerns r.e. syncing the chain initially through Tor yes I agree, we should not entertain it. But, getmonero.org hosts an old blockchain.raw that is the entire blockchain synced to a few years ago, why don’t we kick off a thing that creates a new blockchain.raw every 24hrs and we can seed it as a torrent amd/or host on getmonero.org for initial offline sync, then they connect via Tor and sunc the remaining 24hrs of blocks?

The GUI could fetch the torrent or pull from getmonero.org to build the chain

## nahuhh | 2024-09-22T14:06:22+00:00
It takes just as long to verify the raw as it takes to sync normally (and 2x as much space).. and is a central point of failure.

on the contrary, we should stop providing the raw.

## thisIsNotTheFoxUrLookingFor | 2024-09-22T14:09:46+00:00
> So yeah, we could do something like a client downloads the needed data from a remote node A, and then disconnects and pushes the tx using remote node B (which could just be a standard node, as you say). But then we get a sybil situation where an attacker could just flood the network with nodes and then be able to make associations because "oh, this client just downloaded this data from node A, but I also own node B and it connected to B to send a tx".

Mmhmm this is why Tor pins to guard relays on entry and shifts the remaining relays in the circuit frequently to try and stop someone owning both entry and exit (A and B in your case).

Given RPC over Tor is a thing already, I reckon probably forcing the GUI to use remote nodes over Tor/i2p is ideal, like literally don’t let them input anything other than an onion in the GUI. This is obviously just for running a light wallet connecting to a remote nodes over Tor and not syncing the chain.

Bootstrap the chain over clearnet, but ensure ANYTHING involving a TX is done over Tor



## selsta | 2024-09-22T14:11:55+00:00
>  I reckon probably forcing the GUI to use remote nodes over Tor/i2p is ideal, like literally don’t let them input anything other than an onion in the GUI.

If I run my own node, why should I be not allowed to connect to it over clearnet?

## thisIsNotTheFoxUrLookingFor | 2024-09-22T14:12:03+00:00
> It takes just as long to verify the raw as it takes to sync normally (and 2x as much space).. and is a central point of failure.
> 
> on the contrary, we should stop providing the raw.

The idea is to avoid the burden of dl 200GB over Tor. So basically option 3 Tor all the things but still sync chain over clearnet. But now I think about it why not just pull blocks over clearnet RPC and then enforce everything else through Tor.

## thisIsNotTheFoxUrLookingFor | 2024-09-22T14:17:04+00:00
> > I reckon probably forcing the GUI to use remote nodes over Tor/i2p is ideal, like literally don’t let them input anything other than an onion in the GUI.
> 
> If I run my own node, why should I be not allowed to connect to it over clearnet?

Well if the wallets and everything are all geared up to enable you to automatically and easily do it through Tor, why would you want to use clearnet? Like when would anyone refuse to use a privacy preserving network and regress to clearnet? This is privacy coin right?

## selsta | 2024-09-22T14:28:05+00:00
> Well if the wallets and everything are all geared up to enable you to automatically and easily do it through Tor, why would you want to use clearnet? Like when would anyone refuse to use a privacy preserving network and regress to clearnet? This is privacy coin right?

Tor slows down wallet sync significantly, and the privacy benefit is small in this case which would mostly help with ISP-level spying. There is also the issue with Tor being easily DDoSed, which would mean you can't submit transactions anymore.

## thisIsNotTheFoxUrLookingFor | 2024-09-22T14:41:28+00:00
It also stops remote RPC correlating a supplied TX to an IP as all it sees is IP of the Tor/i2p relay, which is actually a huge privacy bump.

I thought enabling hash/PoW anti DoS on Hidden Services is reducing DDoS over Tor, isn’t this what Haveno implemented to stop their nodes getting DDoSed?

## selsta | 2024-09-22T14:44:23+00:00
> It also stops remote RPC correlating a supplied TX to an IP as all it sees is IP of the Tor/i2p relay, which is actually a huge privacy bump.

But that is irrelevant if I control both the node and the wallet.

> I thought enabling hash/PoW anti DoS on Hidden Services is reducing DDoS over Tor, isn’t this what Haveno implemented to stop their nodes getting DDoSed?

I just know that over the recent years there were multiple occasions where Tor was unsuably slow to the point where you couldn't even sync a wallet.

## thisIsNotTheFoxUrLookingFor | 2024-09-22T14:52:45+00:00
Possible Tor/i2p can have outage but probably not both Tor/i2p both at same time.

My monerod is only Tor, as in I allow Tor P2P incoming via .onion, I have —proxy=127.0.0.1:9050 so any outgoing P2P going to clearnet addresses is done through Tor and I am getting blocks quickly no issue. Of course that doesn’t mean an issue won’t occur but it’s on my todo to add in i2p as well

I also have bitcoin node 100% Tor, literally everything is Tor with it and it also works really well

## nahuhh | 2024-09-22T15:01:52+00:00
 
> My monerod is only Tor, as in I allow Tor P2P incoming via .onion, I have —proxy=127.0.0.1:9050 so any outgoing P2P going to clearnet addresses is done through Tor and I am getting blocks quickly no issue.

NO nodes can connect to you. You can ONLY connect to nodes that have incoming connections open.

## nahuhh | 2024-09-22T15:03:40+00:00
> I also have bitcoin node 100% Tor, literally everything is Tor with it and it also works really well

AFAIK. BTC does NOT allow you to run in an onion-only mode. It -proxy requires clearnet nodes on the other side of the exit node



## thisIsNotTheFoxUrLookingFor | 2024-09-22T15:05:43+00:00
> > My monerod is only Tor, as in I allow Tor P2P incoming via .onion, I have —proxy=127.0.0.1:9050 so any outgoing P2P going to clearnet addresses is done through Tor and I am getting blocks quickly no issue.
> 
> NO nodes can connect to you. You can ONLY connect to nodes that have incoming connections open.

Not true, I have tons of nodes connecting to my .onion address over P2P however blocks are not propagated over Tor currently so I’m pulling blocks from the peers I am connecting out to through —proxy and I’m not sharing blocks that’s correct. Let me fetch my exact node connection stats

## nahuhh | 2024-09-22T15:09:31+00:00
> Not true, I have tons of nodes connecting to my .onion address over P2P however blocks are not propagated over Tor currently so I’m pulling blocks from the peers I am connecting out to through —proxy and I’m not sharing blocks that’s correct. Let me fetch my exact node connection stats

as i said, you can ONLY connect to nodes that have incoming connections. 

Incoming onion peers are not syncing blocks. Anonymous-inbound an entirely different service than p2p-bind

and yes you are sharing blocks, but only with the subset of nodes that have clearnet incoming connections

## thisIsNotTheFoxUrLookingFor | 2024-09-22T15:09:39+00:00
> > I also have bitcoin node 100% Tor, literally everything is Tor with it and it also works really well
> 
> AFAIK. BTC does NOT allow you to run in an onion-only mode. It -proxy requires clearnet nodes on the other side of the exit node

100% my Bitcoin node is Tor only, here is my current peer list, out to .onions, incoming over 127.0.0.1 coming in to me by my onion (bitcoin6twde6mauc5flogkenljfxk3bemqobjse73bf2bnfjaxnfgyd.onion:8333)

![image](https://github.com/user-attachments/assets/a7990aa8-dfd0-46f4-b269-40b292824bea)

See only Tor is ticked, IPv4 and IPv6 are not allowed, not advertised and totally firewalled. I am synced totally fine and I do not seem to have any real delay getting blocks etc.

![image](https://github.com/user-attachments/assets/c0cc73c3-f8aa-459c-884c-7cb8fb8012b3)



## thisIsNotTheFoxUrLookingFor | 2024-09-22T15:15:36+00:00
> and yes you are sharing blocks, but only with the subset of nodes that have clearnet incoming connections

Yes I am not sharing blocks this is what I said, because I have no incoming clearnet connections only Tor. I used to allow clearnet in, but decided against it, really everyone should be using Tor/i2p.

So my node does this:

monerod <- onion <- peer connects incoming to share TX only
monerod -> proxy (Tor) -> I connect to peer and I receive blocks and TX through  proxy (Tor)
monerod -> onion -> I connect to peer onion and share TX only

But yes unfortunately as devs do not allow sharing of blocks over Tor I no longer relay/propagate blocks to the swarm with this setup.

## nahuhh | 2024-09-22T15:30:54+00:00


> So my node does this:
> 
> monerod <- onion <- peer connects incoming to share TX only
> monerod -> proxy (Tor) -> I connect to peer and I **send and** receive blocks and TX through  proxy (Tor)
> monerod -> onion -> I connect to peer onion and share TX only

correction

## thisIsNotTheFoxUrLookingFor | 2024-09-22T15:33:05+00:00
> > monerod -> proxy (Tor) -> I connect to peer and I **send and** receive blocks and TX through  proxy (Tor)

Are you sure? My understanding is we pull information from peers we connect out to and relay it to peers who connect in to us, is this false?


## thisIsNotTheFoxUrLookingFor | 2024-09-22T15:47:38+00:00
> Doesn't Dandelion++ mitigate linking IP addresses with transactions?

It does but Dandelion++ is only used for relaying TX to other peers via P2P. When you connect to a node via RPC, you are not using Dandelion you are telling the node you wish to give it your transaction and the node can correlate it to you, this is what Chainalysis did.

## nahuhh | 2024-09-22T15:55:30+00:00
> > > monerod -> proxy (Tor) -> I connect to peer and I **send and** receive blocks and TX through  proxy (Tor)
> 
> Are you sure? My understanding is we pull information from peers we connect out to and relay it to peers who connect in to us, is this false?
> 

Yes im sure

## nahuhh | 2024-09-22T15:56:44+00:00
> > Doesn't Dandelion++ mitigate linking IP addresses with transactions?
> 
> It does but Dandelion++ is only used for relaying TX to other peers via P2P. 

as i said in my first reply - dandelion is defeatable. 

## thisIsNotTheFoxUrLookingFor | 2024-09-22T16:02:54+00:00
> > > > monerod -> proxy (Tor) -> I connect to peer and I **send and** receive blocks and TX through  proxy (Tor)
> > 
> > 
> > Are you sure? My understanding is we pull information from peers we connect out to and relay it to peers who connect in to us, is this false?
> 
> Yes im sure

Can you show me where you get this? Because I could have sworn we receive data from the peers we connect to and then we relay it to the peers that connect to us, admittedly I could be wrong as I could be thinking of Bitcoin or something else I am using, but it does seem most logical to pull and push data in this manner in a P2P swarm.

## nahuhh | 2024-09-22T16:08:47+00:00
> Can you show me where you get this? Because I could have sworn we receive data from the peers we connect to and then we relay it to the peers that connect to us, admittedly I could be wrong as I could be thinking of Bitcoin or something else I am using, but it does seem most logical to pull and push data in this manner in a P2P swarm.

incoming vs outgoing only decides the direction that initial connection is made, after which data flows in both direction.

example. If an outgoing peer mines a block.. or send a tx, you receive it and broadcast it to your outgoing (and incoming peers). You dont just leech off the network. Data flows in both directions. (though its stil centralized since you can only connect to nodes that have incoming connections)

## thisIsNotTheFoxUrLookingFor | 2024-09-22T16:21:38+00:00
> > Can you show me where you get this? Because I could have sworn we receive data from the peers we connect to and then we relay it to the peers that connect to us, admittedly I could be wrong as I could be thinking of Bitcoin or something else I am using, but it does seem most logical to pull and push data in this manner in a P2P swarm.
> 
> incoming vs outgoing only decides the direction that initial connection is made, after which data flows in both direction.
> 
> example. If an outgoing peer mines a block.. or send a tx, you receive it and broadcast it to your outgoing (and incoming peers). You dont just leech off the network. Data flows in both directions. (though its stil centralized since you can only connect to nodes that have incoming connections)

I don't know this person on the Monero Support reddit, but they seem to be suggesting that outgoing connections pull blocks and then we relay to incoming connections as I suspected. Because I could connect to a out peer that is not fully synced as well, in that case I would be sending all data from block 0 to the out peer but this person suggests it is only in peers that place such a burden, out peers do not, which suggests that we pull from out peers and push to in peers. But alas I do not know if this person is right for sure obviously.

![image](https://github.com/user-attachments/assets/adadaacc-c421-4a42-a543-efc96ee7ee66)


## preland | 2024-09-22T18:07:12+00:00
To make sure we are on the same page here: if you use your own trusted node, can your transaction be traced to that node without the node itself being compromised?

If it can (ie dandelion doesn’t do enough), then that will need to be mitigated.

Alternatively, if it can’t, then significantly reducing the barriers for users to run their own nodes (reducing blockchain size) will address it. “Light” wallets are the safety concern in this case.

## thisIsNotTheFoxUrLookingFor | 2024-09-22T18:11:14+00:00
> To make sure we are on the same page here: if you use your own trusted node, can your transaction be traced to that node without the node itself being compromised?
> 
> If it can (ie dandelion doesn’t do enough), then that will need to be mitigated.
> 
> Alternatively, if it can’t, then significantly reducing the barriers for users to run their own nodes (reducing blockchain size) will address it. “Light” wallets are the safety concern in this case.

Well Dandelion++ is a plausible deniability protection like ring signatures. if I get a stem TX from you, maybe you are the original sender but also maybe you are not. If you want to change it so that I cannot even suspect it was you, make sure your node is using Tor only, and then all another node will ever see is the Tor exit relay IP.

So, to answer your question directly from my understanding, if you do it correctly nobody can trace a TX you send to your own node as coming from you or your node.

## scramblr | 2024-09-22T18:36:53+00:00
Addressing the massive blockchain issue is the right approach, and only approach that is forward-thinking.

**I believe it'd be in the best interest for mobile clients to immediately start bootstrapping/populating the blockchain by:**
- **Start Blockchain Download From $TODAY_BLOCK and work backwards towards block Zero (0)**

_[ Instead of Using Current Methodology Which Is ]_

- Start at block 0, and download for days until you reach 3.2 Million blocks for full node client (and then presumably prune..).
--OR--
- Use Untrusted Remote Node And _YOLO Privacy!_

Of course the dynamics change of the blockchain distributions/download would start to potentially cause some chaos, but limiting it to a few mobile clients and beginning testing what impacts it will have could be the best way to get the most bang for the buck without making core changes that affect _EVERYONE_- It'd be a way of eliciting any problems the new method would introduce while maintaining a relatively easy rollback plan...

EDITS: Lots of formatting and stuff

## Gingeropolous | 2024-09-23T01:45:25+00:00
@scramblr , the issue with the approach of working backward is that the chain is verified starting from the beginning. I.e., each transaction references a prior transaction, and in order for a new transaction to be valid, you need to check the validity of an older transaction. 

now, there is the idea of header sync, or PoW sync (i think the 2 are interchangeable), in which the header information of the chain is verified. However, this still doesn't allow you to form transactions because you have a bunch of block headers. Of course, the client could request random blocks from a bunch of peers and check the headers to make sure they match, but for whatever reason no one has really wanted to implement headers-first sync in the monero software. I think because its something the reference implementation probably shouldn't have in it, because the job of the reference implementation is to provide a robust blockchain.. and a headers chain is not that. 

## boldsuck | 2024-09-23T09:20:31+00:00
> I thought enabling hash/PoW anti DoS on Hidden Services is reducing DDoS over Tor, isn’t this what Haveno implemented to stop their nodes getting DDoSed?

Connections to Hidden Services can be attacked at various points before Rendezvous Circuits are even established.
- Proof of Work (PoW) is only before establishing Rendezvous Circuits. After the attacker has established a connection to a seednode, he is able to establish hundreds of more and the seednode disconnects all older peers. And can flood the seednodes with ‘gliberish’ stuff.
- In addition, DDoS attacks against HsDir relays are possible through OOM killers. HsDir flag will then be gone for at least 4 days. [A case study on DDoS attacks against Tor relays](https://www.petsymposium.org/foci/2024/foci-2024-0014.pdf)
- You can enable DoS defense at the intropoint level. However, intropoint and guard relays can be attacked with DOS.

[Onion service DoS guidelines](https://community.torproject.org/onion-services/advanced/dos/)

## jeffro256 | 2024-09-26T06:24:00+00:00
> the issue with the approach of working backward is that the chain is verified starting from the beginning. I.e., each transaction references a prior transaction, and in order for a new transaction to be valid, you need to check the validity of an older transaction.

This is the correct reason for nodes, which need to verify crypto proofs, but the reason why we have to scan forward with wallets is that the wallet cannot determine whether or not any given ring signature spends one of their owned enote without scanning each ring member first. So scanning backwards would result in missed key images stored, making the balance recovery process incomplete. 

Shameless plug: [Carrot](https://github.com/jeffro256/carrot/blob/master/carrot.md) improves upon this by requiring all transactions where one's enote is spent to contain a scannable output, even if for a 0 amount. Carrot wallets should thus persistently store all key images for transactions which contain one or more outputs that are scannable. If this is done, balance recovery stays complete even if performed in any arbitrary on-chain order. This small requirement should make multi-threaded scanning logic more performant and less error-prone. If one chooses to write the code for this, Carrot could enable backwards scanning to find and spend unspent transaction outputs very quickly for improved UX in the scenario where funds were sent to the wallet recently, but the last scan was a long time ago and performing forward scanning would be slow. 



## porkchopbeauties | 2025-01-05T21:07:05+00:00
I am just a layman so if this is wrong or I misunderstand something then forgive me.

The problem is two-fold in my opinion:

### Nodes sending junk data to attack users (e.g. arbitrary high fees)

- The vulnerability reported in January 2023 by hackerone
- monero-project/monero issue #8298

There would need to be some way to verify the data from other sources to make sure it's correct, either the blockchain itself or other nodes. Or limits hardcoded into wallets to warn if the fee is above say 0.01 Monero.

### Nodes spying on transactions and who is sending the transactions

What if there was a built-in p2p similar to Tor's Snowflake where any client connecting will also act as a relay for other people's transactions? So no one transaction can truly be attributed to a specific IP, it could very well be another transaction from some random user in the network that has simply been forwarded to the node. Obviously there would need to be some controls to prevent spamming like rate limiting so no one client gets overwhelmed with incoming transactions, nor can they spam the node with transactions. It would be X transactions every N minutes, or whatever is acceptable.
From the thread it seems that Dandelion only works on the node level rather than the user level, so this would be like a user level Dandelion.

To further intensify things, what if there was some way to break down a transaction into fragments, let's say ten different fragments. Then the user will send each fragment to ten random peers, who will forward the fragments to different nodes. And they'll be organized by number "Transaction 12345 Fragment Number 1" ... "Transaction 12345 Fragment Number 10". Maybe there could be some way to encrypt the transaction ID just in the beginning, and then at the end after receiving the message from a random peer then the public node can decrypt it.

But as usual if a malicious actor has multiple nodes or clients then they might be able to make out which IP is sending what.

Also if an observer in the network can see the transaction ID or anything that distinguishes it, and monitor the flow of transaction IDs coming and going from different peers, then further thought should be considered on if there's some way to disguise or distort the origin of the transaction, maybe by mixing in decoy transactions or some way of making it impossible to tell where a transaction really started from. Like multiple peers all making the same amount of "noise" (sending the same data at the same time) for Transaction 12345. Or a peer listening for N minutes then releasing a big batch of their own and other peer's transactions all at once, or smaller bursts over some period of time.

Again as a layman I have no idea if this is doable or if the network can handle these extra steps. Maybe it could just be an extra option for people who want added privacy.
Thank you for your time.


# Action History
- Created by: Gingeropolous | 2024-09-19T13:49:00+00:00
