---
title: The 'promo' video needs to be updated
source_url: https://github.com/monero-project/monero-site/issues/951
author: erciccione
assignees: []
labels:
- community
- ⛑️ contributor needed
created_at: '2020-04-26T09:59:05+00:00'
updated_at: '2024-03-24T08:19:11+00:00'
type: issue
status: closed
closed_at: '2024-03-24T08:19:11+00:00'
---

# Original Description
https://web.getmonero.org/media/Monero_Promo.m4v

It's outdated and needs to be updated. Opening this issue for discussion and progress tracking.

# Discussion History
## SamsungGalaxyPlayer | 2020-05-06T14:09:28+00:00
@ajs-xmr is working on this.

## Sunray-Nucleon | 2020-05-18T17:54:15+00:00
.3 XMR per minute is still correct because its .6 in two minutes - thats how i see it. But the term "will never drop below" is maybe not good, because who knows what will be in more far future. It could be said "is fixed at 0.6 per two minutes" or so

## erciccione | 2020-11-25T16:11:26+00:00
@ajs-xmr any news about the video?

## erciccione | 2021-05-17T09:56:01+00:00
ping @ajs-xmr 

## jakubkrnac | 2021-09-26T17:02:48+00:00
I could do the job but I need some type of script. Is anybody willing to write a script with updated informations?

## SamsungGalaxyPlayer | 2021-09-28T20:46:26+00:00
Rough draft: https://cryptpad.fr/pad/#/2/pad/edit/TJ+lw+iQ7NUJZLXmz0eeyzeW/

## erciccione | 2021-09-29T07:42:53+00:00
> Rough draft: https://cryptpad.fr/pad/#/2/pad/edit/TJ+lw+iQ7NUJZLXmz0eeyzeW/

This is a complete redo of the video tho, not an update. It should definitely be discussed with the community before implementing it.

## erciccione | 2021-09-29T08:12:57+00:00
About the proposed script:

In general i think it gives too many technical information the user don't need at this stage. I think we should see this video as the first point of contact for a user that doesn't know anything about cryptocurrencies but it's attracted by the possibility of transacting privately. I think the original video was doing a good job from that point of view, but the proposed script gives too many technical info that are not needed at this stage and could confuse the user. Like scaling strategies, adaptive blocksize, the possibility of sharing private keys of wallets, etc. I think we should also keep the different categories in the video ("Monero si decentralized" -> why; or "Monero is private"-> why).

The old script was doing a very good job in speaking to somebody who hear about crypto and Monero for the first time. I think that should be the priority to keep in mind when working on this script.

> Show triptych

We shouldn't mention triptych when we are not sure we are going to implement it. Right now looks like other alternatives might be preferred. In general, it's a technical detail that a first time user doesn't need to know.

> Monero is a proud privacy coin.

As far as i understood there is part of the community that would like to stir away from the "privacy coin" label, because you cannot be a currency without being private. Personally i think we should avoid the term, especially because there will probably be regulations directed to "privacy coins".

> Monero has more private transactions than all other cryptocurrencies combined, even Bitcoin and Ethereum.

This could mislead people in thinking that it's possible to make private transaction with Bitcoin or Ethereum, but it's not. To achieve privacy people have to use external tools (mixers, specific wallets, etc)

> Instead, volunteers like you(!)

We shouldn't assume every visitor wish to contribute to the project.

> Take back control of your finances with the gold standard in digital payments.

This will not mean anything to the layman. I would drop it entirely.

The most important thing that is missing is why Monero is important in practical terms. Who would want to use it? Why is Monero useful in real life? The old video mention examples of who could benefit from using Monero. We should keep something like that in the new script as well:

> This means businesses can keep their suppliers in secret, 
> as well as citizens escape government repressions, and nosy neighbors or crooks 

## SamsungGalaxyPlayer | 2021-09-29T17:47:41+00:00
> Show triptych

I was referring to a 3 pane thing there as in the dictionary definition of triptych, not Triptych^TM. Sorry for the confusion :)

I specifically took the approach of discussing limited blockchain specific things. I used quite a bit of general language more akin to typical payments. And most importantly, I went for IMPACT. This video is to capture the watcher's interest more than it is to simply run through facts. Most notably, I want the watcher to takeaway that Monero is trustworthy/safe, is exciting, and is prestigious.

Things I avoided on purpose:

- Stealth addresses
- Ring signatures
- RingCT
- Using "blockchain"

Things I kept limited on purpose, because I believe these arguments do not drive much impact:
- Decentralization. The benefits of decentralization are simply too complicated to convey in a ~1 minute intro video

Things I want to incorporate more:
- Fungibility. It's currently not mentioned at all. One hit in our Defcon materials was the heading "NFTs are 

Things I am considering removing:
- Mining. This is a tough one, since mining is a powerful part of Monero's identity. However, it may simply not be impactful enough, and it's hard to make the impact argument here we should make in just a second.
- Adaptive block size. Scalability is important, and it's important that someone gets an association that "Monero = scalable." But- it's not very impactful.

Specific impact I pulled in
- Monero being the gold standard
- Monero being proud of its identity
- Monero having a super supportive community

I'm not a a marketing expert, and we should make sure we weight their opinions the most. Else, we're going to end up with an intro dev guide :p

## erciccione | 2021-10-18T10:44:36+00:00
> Things I kept limited on purpose, because I believe these arguments do not drive much impact:
Decentralization. The benefits of decentralization are simply too complicated to convey in a ~1 minute intro video

The most revolutionary aspect of cryptocurrencies like Monero is that they are decentralized money. Something that never happened in history before and the main reason for cryptocurrencies to exist. That's something that should definitely be emphasized, not removed.

> Things I want to incorporate more:
Fungibility. It's currently not mentioned at all. One hit in our Defcon materials was the heading "NFTs are

Maybe could be mentioned, but IMO *this* is something too complicated to convey in a ~1 minute video.

> Mining. This is a tough one, since mining is a powerful part of Monero's identity. However, it may simply not be impactful enough, and it's hard to make the impact argument here we should make in just a second.

Monero asic-resistance is one of the pillars of Monero and one of the most interesting factors for people who look for a non-scammy project that is more egalitarian than Bitcoin and most of the cryptocurrency in existence. If we find a way to point this out in a meaningful way, we should add it.

> Adaptive block size. Scalability is important, and it's important that someone gets an association that "Monero = scalable." But- it's not very impactful.

Agree.

> Monero being the gold standard

I still think this is not useful or meaningful.

> I'm not a a marketing expert, and we should make sure we weight their opinions the most

I disagree. We should try to stir away from the traditional way of marketing, which is based on gimmicks and psychological tricks to try to sell a product to as many people as possible. What we need is a video that makes clear to a newcomer what Monero is and how it can be useful to them and the world.

## johnr365 | 2021-10-18T13:55:40+00:00
If the video is going to be short, there's going to have to be a lot of assumptions.

Perhaps the easiest assumption is that the audience has some idea of what Bitcoin is.

So then, one approach (and it doesn't have to be for this specific video necessarily) is to leverage everything off Bitcoin.

So for example:
- Similar to Bitcoin, Monero is open source, decentralised software, where miners mine a supply of coins that is fixed in software, rather than arbitrarily inflated by central banks and governments. 

- Whereas with Bitcoin you have a transparent ledger that anyone can observe and track, Monero uses a set of technologies to prevent this kind of snooping. This privacy also gives Monero a property called fungibility, that Bitcoin does not have. On Bitcoin, if someone sends you coins that were previously linked to nefarious activity, others can see that - and might start asking questions. In Monero, the history of the coins does not matter, because it can't be openly read on the blockchain.

- With Bitcoin, transparency is the default. With Monero, transparency is optional. If you *want* to share with someone the details of your wallet, you can provide them your built-in private view-key which lets them take a look.

- Monero aims to improve on Bitcoin's decentralization, such that the mining algorithm is setup so that you don't need expensive, custom hardware. You can effectively mine using your CPU, which is a commodity that everyone with computers and smartphones has access to.

- Bitcoin has taken an approach that makes it expensive to use for smaller amounts. If it costs $5 to buy a $4 coffee with Bitcoin, it doesn't make sense to do. Longer term, the idea is that people will buy coffee with Bitcoin via side-chains like the Lightning Network. Monero has taken a different approach that will allow for larger amounts of transactions to take place at lower cost. This keeps the network usable and affordable for smaller transactions, such as buying coffee.

## erciccione | 2021-10-18T16:09:52+00:00
> Perhaps the easiest assumption is that the audience has some idea of what Bitcoin is.

This is an approach we decided to stir away from some time ago, when getmonero and especially the homepage, gave for assumed that the user knew what Bitcoin is, even roughly. We decided to change that in favour of a more neutral and Monero-specific approach and i still think that should be the case. Users might come to getmonero because they look for a way to transact privately, which is unrelated to Bitcoin.

Also, Monero doesn't aim to improve Bitcoin, Monero is a separated project that has merits on its own. We are mature and solid enough to not need to compare ourselves to Bitcoin.

## johnr365 | 2021-10-19T12:09:38+00:00
@erciccione - Thanks for the reply. 

Totally understand if you don't want to take the approach of building on assumptions in this video. It was just a suggestion on the basis that some assumptions will need to be made (if the video is to be short), and assuming some awareness of the coin that brought cryptocurrency mainstream, is one option.

Regarding this comment:

> Also, Monero doesn't aim to improve Bitcoin, Monero is a separated project that has merits on its own.

Whilst I agree with the sentiment, it's also worth remembering that Monero was built on top of the cryptonote protocol, of which the third paragraph of the whitepaper literally says:

> In this paper, we study and propose solutions to the main deficiencies of Bitcoin.

Anyhow - let's keep moving things forward with this video.

# Action History
- Created by: erciccione | 2020-04-26T09:59:05+00:00
- Closed at: 2024-03-24T08:19:11+00:00
