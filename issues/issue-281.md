---
title: Adding Tor to hosted wallet server API standard
source_url: https://github.com/monero-project/meta/issues/281
author: paulshapiro
assignees: []
labels: []
created_at: '2018-10-01T17:37:07+00:00'
updated_at: '2018-10-02T06:06:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Over time we've gotten lots of requests to expose a Tor hidden service address on MyMonero.

After thinking about it more, we propose adding Tor to the lightweight wallet server API standard, and adding built-in support to the server implementation in the Monero src. 

We've begun adding it recently since it's something that needs to happen anyway. We think it should be part of the standard though because it confers a number of benefits for users (it can be enabled in lightwallet apps as a best practice), as well as server operators who, e.g. won't have to worry about opening ports on firewalls.

# Discussion History
## paulshapiro | 2018-10-01T17:46:31+00:00
Just wanted to mention it probably makes the most sense to begin support at prop 224 (long) addresses.

## anonimal | 2018-10-01T23:26:23+00:00
1. API? This is literally as simple as running the request through loopback. Wallet implementations should be network agnostic.
2. Why is this going to the meta repo? This is a monero code request.

## paulshapiro | 2018-10-01T23:33:11+00:00
1. No, this is for the standard for the lightwallet servers. It means light wallet implementations should expect for this feature to be available and try to support it. So obviously the wallet implementation will be "network agnostic", since users won't be *required* to use it. 

2. We didn't announce it to huge fanfare or anything but a number of the lightwallet server implementors have agreed to establish an implementation standard and place it on this repo for community ownership. 

## paulshapiro | 2018-10-01T23:33:33+00:00
Of course another ticket will be opened on the Monero src repo unless someone gets to the PR first. I just decided not to state the obvious when originally posting.

## anonimal | 2018-10-01T23:37:15+00:00
>So obviously the wallet implementation will be "network agnostic", since users won't be required to use it.

I don't think you understand... You've not proven any technical reason to support Tor over any other socket based overlay network. Network agnostic means literally the wallet will only be dealing with an IP address, even if it's loopback. What is Tor-specific here?

## paulshapiro | 2018-10-01T23:38:19+00:00
What is Tor-specific... is the fact that lightwallet server implementations will support Tor in a particular manner that can benefit from being documented…?

## anonimal | 2018-10-01T23:40:01+00:00
I don't think you understand the basic networking aspect yet... You can replace Tor with X anonymity system. What Tor-specific functions do you need?

## paulshapiro | 2018-10-01T23:42:22+00:00
No, I'm pretty sure I understand it, thanks. This isn't a document where we "prove technical reasons to support Tor over other networks". It's a document that says what the servers try to support and how they do so.

## anonimal | 2018-10-01T23:45:42+00:00
>No, I'm pretty sure I understand it, thanks.

I have yet to see proof of that. If you did, you would realize you can use kovri in an identical manner through its http and socks proxy - and could have since it's inception. You don't need a kovri API to do that.

>It's a document that says what the servers try to support and how they do so.

But you haven't even proven the need to support anything... You literally don't understand how Tor works but you want to use it specifically in a standard?

## anonimal | 2018-10-01T23:46:26+00:00
Servers say "I want this" but what you don't realize is that "this" is generic enough to not need to specify Tor - at least until this is proven otherwise.

## paulshapiro | 2018-10-01T23:49:31+00:00
> But you haven't even proven the need to support anything

I haven't proven the need to support JSON and msgpack either but I think it's a pretty good idea to document how the servers can best use them.

> If you did, you would realize you can use kovri in an identical manner 

Yes, I think we all agree that when Kovri is mature enough we will integrate it as well.

## anonimal | 2018-10-01T23:59:26+00:00
>Yes, I think we all agree that when Kovri is mature enough we will integrate it as well.

So this is actually an integration proposal and not a standard proposal? You should pick a lie and stick with it.

>I haven't proven the need to support JSON and msgpack either but I think it's a pretty good idea to document how the servers can best use them.

Again, until do a modicum of research, you'll see that the standard you're proposing - given the information you've provided - would be identical for *any* socks proxy usage. This is network agnostic and *not specific to Tor*.

## paulshapiro | 2018-10-02T00:13:44+00:00
I already understand everything you said, and maintain that you ignore that this is a repository for collecting information about best practices and standards and agreeing on what we want to support. You're not even a participant in this standard, so what's your deal? Am I not allowed to use the word Tor? I already showed one clear example of possible implementation standardization, not that it's easily visible after all of this nonsense! But aside from that, I'm having a hard time stomaching your behavior and suggest you take a hard look at why you are commenting on this thread. 

## SRCoughlin | 2018-10-02T01:49:28+00:00
A good example of a Tor-specific implementation is the Onion Service layer (previously called Hidden Services). We would need to implement a form of network database to track onion service descriptors on the Monero network, similar to the current master node list of IP addresses. It would also be necessary for numerous nodes to interface both such networks to prevent a network fork.

There's a lot of work necessary for this to happen, but it might be worth the effort given a large demand by the community.

(Note that I2P and Kovri also have similar requirements but have many advantages over the Onion  Service layer.) 

## paulshapiro | 2018-10-02T01:58:01+00:00
>  We would need to implement a form of network database to track onion service descriptors

Our plan is to have a singular prop 224 address which is embedded in our client apps - users would be able to specify their own address in Preferences (or our hidden service address). One neat solution is if the address they enter starts with a prefix (i.e. "mymonero") like ours then we would be able to throw a warning (given how extremely unlikely such an address would be if not exactly the same).

In the absence of that and given that the general use case for a lightwallet server is as operated by a trusted party (basically friends and family) I had initially assumed that typical communication of the address (like posting it on a website or sending it over email) would be sufficient. It's definitely a neat idea though and it's something I've tried to put a little bit of thought into.

## SRCoughlin | 2018-10-02T02:16:08+00:00
> users would be able to specify their own address in Preferences (or our hidden service address)

While a good idea, my worry with this is that there has to be _a lot_ of nodes that subscribe to both TCP/IP and Onion Service layers or else the miners on the separate/forked networks will constantly be stuck in long and unproductive re-org battles. If the Onion Service denies mining then much of its power is lost. And since Tor is no longer state-of-the-art for privacy preservation I don't see how we can make this a default setting.

The theory behind Kovri is that since I2P is state-of-the-art we would have that as a default layer along with TCP/IP, making isolated nodes optional. So all nodes would share both networks and privacy would be preserved.

This plan is up for debate, of course, and could easily be modified.

## paulshapiro | 2018-10-02T02:19:10+00:00
Ok, but this isn't for the Monero daemon, this is for the lightweight wallet server

## SRCoughlin | 2018-10-02T02:22:32+00:00
> this is for the lightweight wallet server

Doh! :smile: 

With no mining there's no issue at all. Onion Services would work quite well in this case. 

(The only caveat is that the node that connects to the monero network could be analyzed for new TXNs and then assumed to be part of the service. Then again this is true regardless of communication between the node and the client.)

## fluffypony | 2018-10-02T06:06:20+00:00
Just to clarify, this is specifically to add Tor support to the standard so that all lightwallet implementations support Tor. When Kovri is ready then that would be an additional hidden service that is supported, not a replacement.

# Action History
- Created by: paulshapiro | 2018-10-01T17:37:07+00:00
