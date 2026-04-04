---
title: Consider a different messaging backend for the MMS
source_url: https://github.com/monero-project/monero/issues/8762
author: tobtoht
assignees: []
labels:
- enhancement
- proposal
created_at: '2023-03-04T18:04:26+00:00'
updated_at: '2025-04-28T22:40:16+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The [Multisig Messaging System](https://www.getmonero.org/resources/user-guides/multisig-messaging-system.html) (MMS) depends on [PyBitmessage](https://wiki.bitmessage.org/). 

PyBitmessage saw its latest stable release in [Feb 2018](https://github.com/Bitmessage/PyBitmessage/releases/tag/v0.6.3), 5 years ago. It [depends](https://github.com/Bitmessage/PyBitmessage/blob/v0.6/src/depends.py#L15) on Python 2, which has been EOL since [Jan 2020](https://www.python.org/doc/sunset-python-2/).

Most Linux distributions, including [Debian](https://wiki.debian.org/Python), [Arch Linux](https://security.archlinux.org/package/python2) and [Fedora](https://fedoraproject.org/wiki/Changes/RetirePython2) no longer ship Python 2.

Efforts to port PyBitmessage to Python 3 have [not gained much traction](https://github.com/Bitmessage/PyBitmessage/issues/1712). It is unclear if this is still being worked, but given the lack of activity in the repo and of the core maintainer I think it firmly falls into the vaporware category.

It should go without saying that running unmaintained networking software is a security concern and it is in my opinion inadvisable to continue to support it. I can't leave unmentioned that PyBitmessage once before had a  [RCE vulnerability](https://github.com/Bitmessage/PyBitmessage/commit/8ce72d8d2d25973b7064b1cf76a6b0b3d62f0ba0#diff-54d55baf8967b2416bd9fc199d3cc22dcf68d95aeeb45f447bf8b0b0bf662b8fR9) that was [used to steal cryptocurrency](https://thehackernews.com/2018/02/bitmessage-bitcoin-hackers.html).

Ping @rbrunner7 

Open questions:

- Does the MMS still work with Monero's current experimental multisig implementation?
- What would be a suitable replacement for PyBitmessage?

# Discussion History
## rbrunner7 | 2023-03-05T07:09:07+00:00
Regarding your first question: Yes, the MMS works with the latest changes to Monero multisig, especially the added key data exchange rounds that were added to increase the security of the whole system. In fact, I used the MMS to test these changes as they were developed, because after all those years, and with all its reliance on a quite questionable transport mechanism, there is simply no faster and easier way to do Monero multisig in various ways, for different values of M and N.

Regarding a possible replacement for PyBitmessage, a bit of background info:

When I started working on the MMS I quickly discovered that messaging tools are numerous almost like pebbles on a beach, and still new ones continue to pop up. But when I checked which ones could be used by Monero in a fully automatic way to deliver messages between Monero wallets I found exactly one that had an API to do so: PyBitmessage.

Various people proposed alternatives already during the MMS development, and my question was always the same: Does it offer an API for fully automatic sending and receiving of messages? As explained, they never did as far as I could see.

Maybe I did not search enough, and maybe in the meantime new such tools with an API came to be, but in any case that was my starting point.

I think any serious search for a PyBitmessage replacement should start with the Monero daemons themselves. Because, ask yourself: Is there already a good, battle-tested and well-maintained system that allows to send data between Monero wallets? Stupid question - of course there is: the network of Monero daemons. Just one problem: So far, they only "transport" transactions between wallets, so to say.

Unfortunately you run into difficult design problems if you want to expand the data transport duties of Monero daemons to multisig related data between wallets. Most serious are spam and DoS problems.

But as far as I know I am the only one who ever seriously investigated here, and maybe a second attempt would be successful where I gave up after some time.

I documented this attempt of building a "Monero daemon messaging system" here: https://taiga.getmonero.org/project/rbrunner7-really-simple-multisig-transactions/wiki/monero-daemon-messaging-system

## vtnerd | 2023-03-07T21:23:48+00:00
https://github.com/torproject/torspec/blob/main/control-spec.txt

It should be possible to create a temporary hidden service using the `ADD_ONION` control command. The wallet listens for RPC connections that get forwarded from Tor. Tor does the client authentication and encryption. The downside is that both peers must both be online for this to work. The work-around is to have the sender try X number of times (it's no different than BitMessage in a sense when you break it down).

I think everything will work with just a single ed25519 key (per user) - the pubkey is used for client authentication in one direction, and is used for server identification in the other. This key would be separate from any Monero related stuff, just like a Bitmessage key is different. We could have a `xmrmms.....` prefix or something to identify the messaging keys. Once everything is setup, the keys are disposed.

If we got this working, configuration with tor will be even easier. The user just specifies the control port (typical 9051) and then `monerod` auto-determines and configures everything else (so that `--anonymous-inbound` becomes optional for correctly setting up tor in/out p2p messaging).

--------------

Do many people use the MMS system? The funky part is that you have to relay an address to each other, just to initiate the messaging. Alternatively, you could just email each other the parts directly from the CLI window. I suppose there is additional privacy with this MMS technique.

## rbrunner7 | 2023-03-08T19:11:38+00:00
> The downside is that both peers must both be online for this to work. 

Yeah, that's a very nice feature of the Bitmessage network that I forgot to mention so far: that sender and recepient of a message do not have to be online at the same time because messages "will wait for you". If it was only for me I wouldn't accept a replacement for current MMS that has a hard "must be online at the same time" requirement, that would just not fly for me.

> Do many people use the MMS system? 

I suspect that the MMS has only very few users. It has some functionality that is missing that would get noticed and reported if many people used it. It also has some issues if you use the most recent PyBitmessage version that is distributed as appimage, but I know about exactly zero questions and complaints regarding these. That's one of the reasons my motivation to invest further time into the system is low.

> The funky part is that you have to relay an address to each other, just to initiate the messaging.

Well, if you see wallets to be fully on their own, because you can't count on any help from the daemons, I don't see how it could work otherwise with any reasonable privacy.

> I suppose there is additional privacy with this MMS technique.

Privacy is excellent. The MMS encrypts messages per recipient. And Bitmessage must be one of damned few systems that produce almost zero usable metadata about the message traffic. It even uses Dandelion.

It's a real pity that we have to fear that PyBitmessage is experiencing a slow death by lack of contributors and interest.


## vtnerd | 2023-03-08T19:28:09+00:00
> Yeah, that's a very nice feature of the Bitmessage network that I forgot to mention so far: that sender and recepient of a message do not have to be online at the same time because messages "will wait for you". If it was only for me I wouldn't accept a replacement for current MMS that has a hard "must be online at the same time" requirement, that would just not fly for me.

BitMessage just tries repeatedly to send until the recipient comes online. There isn't much difference if we write this code ourselves within the the Monero project.


## rbrunner7 | 2023-03-08T19:58:23+00:00
I guess it makes a difference how many wallets are online to span up a "wallet network" that can store and forward for everybody. If people act too selfishly and only let their wallets run for the MMS when they themselves have a need for the MMS it might not reach critical mass to offer "connectivity" 24/7.

## vtnerd | 2023-03-08T23:24:01+00:00
I don't see many other options, unless BitMessage development picks up.

## plowsof | 2023-06-07T09:42:12+00:00
for visibility: https://bounties.monero.social/posts/83/8-999m-bitmessage-rival-or-re-write 

>Below is a proof of concept of a p2p messenger that runs over i2p. It uses libgpgme for encrypt/decrypt messages and JWP (json web proof) for contacts to authenticate between each other. Contacts just need to mutually add each other by exchanging .b32.i2p address.
> https://github.com/creating2morrow/nevmes
>This isn't currently a viable replacement [..]

## rbrunner7 | 2023-06-07T16:38:45+00:00
Thanks, @plowsof , that Neveko project looks promising if the dev(s) do pull through, bring it to production quality and really add the API they hint at in the ReadMe.

## kayabaNerve | 2023-07-04T17:27:07+00:00
Hot take. If Monero doesn't have the bandwidth to build a P2P messenger for multisig, we shouldn't integrate one just to offer it as a 'feature'. I'd vote to deprecate MMS if there's not a clear path forward. We shouldn't leave it neglected and discuss potential options for years, just to choose something else to be just as neglected.

PyBitmessage, while dead simple, hasn't worked out. Unless we have a project we believe will work out, for years to come, maintaining security *and meeting all design criteria necessary for something as security critical and adversarial as multisig*, we shouldn't just shim in whatever we get running.

## tobtoht | 2023-07-04T23:56:30+00:00
I'm waiting for something promising to come out of that bounty, but as it stands I'm for the removal of the MMS in the next hard fork if nothing changes. In my opinion, it is sadly inadvisable to continue to use the MMS in its current form due to the lack of maintenance of its transport mechanism and its dependencies. I have a nuclear option available [here](https://github.com/tobtoht/monero/commit/ab0e367593a5854232a774edfdff1299b99512bf) should we reach broad consensus to go that route.

I think any solution that ties multisig messaging to a specific anonymity network is not really a good way forward, considering how flaky these networks are at times and how users tend to favor one over the other. From recent memory: I2P [downtime](https://old.reddit.com/r/i2p/comments/10wln04/news_and_weather_updates/), Tor [downtime](https://old.reddit.com/r/TOR/comments/ktv8bw/the_entire_tor_v3_consensus_is_down/) or the [DoS attacks](https://blog.torproject.org/tor-network-ddos-attack/) that lasted months and at some points "impacted the network severely enough that users could not load pages or access onion services". Multisig applications require better availability than these networks can provide, so they shouldn't be the _only_ option available. In fact, tying the MMS to any specific transport mechanism is likely doomed to end in a repeat of the current state of affairs.

We could revisit the idea of using the daemon to pass messages around. It seems great at first glance, every wallet is already connected to a daemon that is part of a P2P network, so why not? As far as I'm aware there are still no good solutions to the problems rbrunner laid out [here](https://taiga.getmonero.org/project/rbrunner7-really-simple-multisig-transactions/wiki/fighting-spam-by-pow). Given that a static PoW difficulty can't work, how do nodes reach consensus on the amount of PoW required to add a message to the pool? And would it not still be trivial to DoS the network to a point where the PoW requirement makes is unusable for legitimate participants?

Alternatively, the MMS could be made to be transport mechanism agnostic. For example, it could just communicate with a service hosted on the local machine (similar to a Tor daemon - a bridge, if you will) according to some well-defined API and let the bridge figure out how to route messages to other participants. In practice, this will probably lead to competing bridge implementations that aren't necessarily compatible with each other. One exclusively works over I2P, one over Tor, different wallets may bundle different bridges and you end up having trouble getting all participants to use the same bridge. However, for some applications it might be perfectly acceptable to push all encrypted messages to a centralized clearnet host, eliminating all the inherent problems of P2P and anonymity networks, and this approach would easily allow such an implementation.

Finally, we could abandon the idea of an integrated interoperable solution for multisig messaging. The two prime use-cases for multisig are escrowed marketplaces, for which an [efficient implementation](https://www.youtube.com/watch?v=qrjKDuyFv0Y)  is being worked on (message transport doable without MMS) and multi-factor wallets like Rino, which can have their own centralized messaging solution. As far as I know multisig with more than 3 cosigners isn't really used outside of enterprise environments, which will favor custom solutions anyway.

## rbrunner7 | 2023-07-05T16:36:10+00:00
Thanks for the many interesting thoughts, @tobtoht . I currently think along very similar lines, and agree with most you say.

Maybe somebody clever should really take another attempt at a daemon-based wallet-to-wallet messaging mechanism. With the right twists it may be be doable with quite reasonable effort, and has the potential to solve the problem once-and-for-all.

## kayabaNerve | 2023-07-05T20:12:09+00:00
> As far as I know multisig with more than 3 cosigners isn't really used outside of enterprise environments, which will favor custom solutions anyway.

With very large multisigs, you really need identifiable abort. Not only does Monero not offer that, any transport layer would have to verifiable. For Serai, which obviously has its own impl of multisig with identifiable abort, I actually wrote my own micro-blockchain I'll underpin with Tendermint to order multisig messages and achieve consensus. So that's the "custom solution" favored on this end...

At the very least, yes, transport agnostic/daemon backed as @tobtoht said is solid.

## jeffro256 | 2023-11-10T18:04:32+00:00
> Hot take. If Monero doesn't have the bandwidth to build a P2P messenger for multisig, we shouldn't integrate one just to offer it as a 'feature'. I'd vote to deprecate MMS if there's not a clear path forward. We shouldn't leave it neglected and discuss potential options for years, just to choose something else to be just as neglected.
> 
> PyBitmessage, while dead simple, hasn't worked out. Unless we have a project we believe will work out, for years to come, maintaining security _and meeting all design criteria necessary for something as security critical and adversarial as multisig_, we shouldn't just shim in whatever we get running.

If we use the existing Monero p2p network, if that transport method fails, then there's no point to the MMS anymore ;), which solves that problem: they die together. I'm in favor of making a temporary application-agnostic messaging layer on Monero, since we already have all of the pieces we need: An ASIC-resistant PoW algo, EC cryptography, Unfakable timestamps to mitigate pre-loaded spam attacks (block hashes), an existing thriving p2p network, dandelion++, and nodes who are used to storing large quantities of data. This messaging layer wouldn't just be useful for multisig, it would allow wallets to trade recipients, refund addresses, transaction memos, and other things we don't forsee yet. AND that would *actually* disincentivize `tx_extra` and other forms of stenography, instead of forcing devs to create more and more clever ways of encoding arbitrary data in plain sight.  

For each application suite that needs messages to persist for longer periods of time (months, years), those nodes can subscribe to their daemons and store those messages for longer, then find each other using e.g. libp2p. So the nodes themselves can be less burdened with on-chain data, while those who wish to store extra data out of the goodness of their hearts, or for a fee, can choose to do so. 









## rbrunner7 | 2023-11-10T18:19:07+00:00
@jeffro256 : You may read [my comment here](https://github.com/monero-project/monero/issues/8762#issuecomment-1455009880) higher up from March, especially towards the end, about my attempts to design exactly such a daemon based communication layer for the MMS.

What I remember: It looks like a no-brainer first, and you would think that there are only some details to work out, but then, as you look at the details ...

But well, I repeat this my statement, to emphasize:

> But as far as I know I am the only one who ever seriously investigated here, and maybe a second attempt would be successful where I gave up after some time.

## kayabaNerve | 2023-11-10T18:26:43+00:00
I'd like to explicitly comment that messaging layers have a variety of design criteria depending on their use-case. The above messaging layer would presumably be ephemeral, a valid design use-case, yet in the process become invalid for anything needing an effectively permanent solution for data availability. Accordingly, they don't disincentive TX-extra/stenography for such use cases.

I'm also unsure an effective solution on the scale of months/years can be designed due to a variety of comments, though I won't begin that commentary here and now.

Monero's P2P network for a short-term message delivery system likely will work fine in environments like multisig though. There is a variety of academic commentary available on the requirements of broadcast layers, yet any P2P network can have enough protocols overlaid to meet academic requirements.

## fullmetalScience | 2024-03-12T11:06:58+00:00
[Tox](https://github.com/TokTok/c-toxcore) may be an interesting candidate. Refer to the minimal implementation called [MiniTox](https://github.com/hqwrong/minitox) to get an idea.

As a true P2P messaging network, it relates to Monero principles. It uses Ed25519 key-pairs to identify participants, which, in theory, should allow for sending messages *"to"* Monero addresses - a feature that would pave the way for very interesting use cases like in-person trade. (In contrast, the current MMS requires participants to manually enter a separate PyBitmessage transport address.

Tox is mature and active enough to be considered a viable option and there already are "nodes". The protocol could need a formal audit, which the Monero community may be interested to fund. Technically, the two projects make for a perfect match. We could get in touch with their community to see what they think about a closer cooperation.


As for *"sending messages to Monero addresses"*, I'm still investigating. These are the main points I've identified so far:

* Reusing keys across different applications is considered cryptographically questionable. Monero however has several keys of varying criticality to chose from, so I suspect there to be a viable solution to this concern.
* Tox, using the official X25519 specification, differs from Monero's where clamping is omitted. This effectively makes keys incompatible. Seraphis may impact this too (Poodle?). If necessary, maybe Tox would be inclined to update the protocol under the outlook of a vast boost in adoption.

## haveno-user | 2024-06-09T01:51:10+00:00
As somebody who's currently having to test multisig without the benefit of MMS, due to the dependency-hell situation that bitmessage is in, I have a suggestion.

First add the simplest possible alternate backend to MMS that requires the wallets to be in the same directory.  That would already make testing much less tedious.

Then expand it to if the wallets are on the same machine.

Then add a tiny daemon that has to be manually configured on each machine that hosts one share of a multisig wallet, but allows for MMS automation after it's installed.

Start simple so it can actually be done.

## jermanuts | 2024-09-10T12:43:19+00:00
Are there any alternatives to BitMessage protocol? Because it is not [very secure](https://zolagonano.github.io/blog/posts/a-very-technical-look-at-bitmessage#bitmessages-encryption).

Tox isn't secure either @fullmetalScience , https://blog.tox.chat/2023/03/redesign-of-toxs-cryptographic-handshake/. However, there's a PR to fix it https://github.com/TokTok/c-toxcore/pull/2450.

## goldroom | 2024-09-24T14:42:28+00:00
@fullmetalScience not sure if it's relevant, but for clarification: Tox also uses X25519 key-pairs as identities (and _not_ Ed25519).
@jermanuts KCI is a post-compromise issue if a private X25519 identity key of a Tox entity is stolen. This enables to reverse-impersonate _others_ to the entity who's private key was stolen (with limitations). Not sure if this threat is relevant to your use-case.

# Action History
- Created by: tobtoht | 2023-03-04T18:04:26+00:00
