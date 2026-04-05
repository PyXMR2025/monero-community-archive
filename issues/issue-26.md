---
title: 'Project Licensing '
source_url: https://github.com/Cuprate/cuprate/issues/26
author: Boog900
assignees: []
labels:
- C-discussion
created_at: '2023-08-29T20:33:42+00:00'
updated_at: '2024-05-27T00:58:23+00:00'
type: issue
status: closed
closed_at: '2024-02-02T23:19:49+00:00'
---

# Original Description
This issue is for discussion around the licensing of Cuprate. Currently Cuprate is licensed under AGPL-3 with some of the crates that make up Cuprate licensed under the MIT license.

As I see it we have 3 options:

1. Full MIT
2. Full (A)GPL-3
3. Split MIT/ AGPL-3 (keep it how it is now)

Doing 2 and changing to full AGPL-3 will be going against what I said I would do in my CCS (so isn't possible?) but I have left the option there. Plus going full AGPL would be too restrictive IMHO.

reasons given for AGPL-3:
hyc: [`permissive license allows proprietary companies to build "monero-compatible" apps that no outsider has the ability to review or verify`](https://libera.monerologs.net/monero-community/20230829#c275505)
silverpill: [`The license protects the project from hostile forks and generally serves as a deterrent against privatization of public goods` & (with MIT) `any company can safely use Cuprate as part of their infrastructure because it has business-friendly license, create a closed-source fork and hire developers who were previously working on open-source version.`](https://monero.town/comment/1310875)

reasons given for MIT:
spirobel: [`It gives too much power to the people who have the copyright of the code. It is also hard to switch away from this later on if there was no contributor license agreement signed by every single contributor. `](https://matrix.to/#/!WzzKmkfUkXPHFERgvm:matrix.org/$XHdBynnDNwJJihkx2YjjcmSz7K6MVw52RGUmJd-J3UY?via=matrix.org&via=monero.social&via=libera.chat)

There are way more reasons given for each than I stated there I just grabbed a few.

I do not have a strong opinion either way between 1 & 3, I think doing 2 would be too restrictive.

Edit: To clarify "too restrictive", it would force people who use the crates to use the GPL license. This is an issue if people want to use the crate in code under licensed MIT for example, they would be forced to go for another option/ create another version licensed under, for example, MIT. Though this, admittedly, would allow people to use these crates in proprietary code.


# Discussion History
## plowsof | 2023-08-29T21:05:33+00:00
Original developer wanted MIT and you convinced them to move toward 3 correct? Could you clarify your own reasons for this (e.g. there have been comments along the lines of (i will exaggerate here) ' why trust devs that where looking to cash in on this at a later date.. what if they sneak in a money printer') could you speak to that line of thinking? 

## Boog900 | 2023-08-29T21:21:57+00:00
> Original developer wanted MIT and you convinced them to move toward 3 correct

Originally Cuprate was licensed under MIT when synthetic announced Cuprate a few people asked/ convinced us to move to (A)GPL we discussed this and I thought it was a good compromise to do split (A)GPL/ MIT like Serai. We are both not licensing experts.

> why trust devs that where looking to cash in on this at a later date.. what if they sneak in a money printer

I am not sure if I understand this, are they talking about taking CCS money?? 

I would say an building an alternative implementation of a node would be the worst way to exploit people for money (or for anything). Any exploit I put into Cuprate will get caught by monerod denying me my money as monerod would just deny the bad blocks. It would be way better to hide an exploit like this in a wallet/ DEX.

Eventually **if** Cuprate becomes recommend for production use I would expect a lot of people will have gone through the code, especially consensus code, so any exploit should be found.

## silverpill | 2023-08-29T22:54:38+00:00
@plowsof I was one of those who asked @SyntheticBird45 about GPL after announcement. Here's a link to discussion: https://matrix.to/#/!ZdVDBBouJUyQVsewKn:monero.social/$7gP8NyoUdAq_PGFTQycQsezDSlCX3i-iZtTOVgsX1I8?via=libera.chat&via=matrix.org&via=monero.social

@Boog900 

>Split MIT/ AGPL-3 (keep it how it is now)

I'm in favor of this option. As far as I know, you're collaborating with Serai developers, who might want to use your code in their project. If some Serai crate is MIT-licensed, it can't depend on AGPLv3 crates, so licensing everything under AGPLv3 would hurt a collaboration.
In general, it is considered a good practice to use permissive licenses for libraries / re-usable modules (to facilitate collaboration between various projects) and use copyleft licenses for project-specific stuff. Full (A)GPL-3 makes sense if you're building an user-facing application (like a website or a mobile app), or if you're not interested in collaborating with projects using permissive licenses.

## k4r4b3y | 2023-09-03T10:45:40+00:00
I find hyc and silverpill's reasons for being in-favor of GPL reasonable.

## dan-da | 2023-09-05T05:53:28+00:00
I agree with hyc.  gpl requires that companies that use this code in their products publish their changes.  If one benefits, one should give back.  simple.

## vorot93 | 2023-09-05T15:00:33+00:00
Speaking as the maintainer of Rust MDBX bindings and the original ORM code that `cuprate-database` descends from, I'd strongly recommend going AGPL-3.0 with CLA to prevent actors like Paradigm from exploiting your work. See Akula/reth debacle as an example of this.

## silverpill | 2023-09-05T16:50:06+00:00
@vorot93 Interesting, somehow I missed it: https://thedefiant.io/paradigm-accused-copying-code. VC-funded fork competing with a volunteer-driven project is one the scenarios I had in mind when I advocated for AGPL-3.0.

Akula was licensed under AGPL-3.0. That didn't prevent a malicious fork, but made it more costly. According to the article, Paradigm had to re-write AGPL-3.0 licensed parts of the code, but they did it nevertheless.

I don't like the CLA idea though. Do you think that CLA would have changed the outcome of Akula/Reth case?

## vorot93 | 2023-09-05T16:54:23+00:00
@silverpill Paradigm exploited the fact that Akula changed license from Apache instead of starting with AGPL. This way they claimed no copyright infringement (despite plagiarism).

CLA is required to properly manage copyright 'just in case', so that drive-by contributors don't handcuff authors to AGPL.

## vorot93 | 2023-09-05T17:07:59+00:00
Despite bad rep, AGPL+CLA is the gold standard for reaffirming ownership over your projects. It allows the author to explore licensing deals and contract work later on (subject to CLA terms) instead of perpetually depending on community handouts. It also gives the authors an edge over hostile forks who don't get to enjoy no-strings-attached code without compensating authors for their time and efforts.

## vorot93 | 2023-09-05T17:15:01+00:00
In the case of Cuprate I can almost guarantee that this work WILL attract unwanted attention from those seeking to decrypt Monero, as a clean view into Monero's inner workings, in a much easier language.

For this project to not be a net negative it must be legally toxic for closed-source crypto analytics services (e.g. Chainalysis).

## spirobel | 2023-09-05T19:10:33+00:00
> It also gives the authors an edge over hostile forks who don't get to enjoy no-strings-attached code without compensating authors for their time and efforts.

So who gets to be the author? This means Monero devs are in a competition about who gets to make the commit. The winning strategy is to share as little information as possible. Let others go down wrong paths. Don't document anything and make everything as complicated as possible. Then do posturing to be seen as the guru that has the secret talents to understand the giant messy code base.

So we end up with a giant, convoluted, undocumented, code base that is essentially a turf war. We need to avoid (re?-)creating this culture at all costs.

We need to come to the understanding that we share the same values and goals. So we can just cooperate and share information and it does not matter who commits the code in the end.

The argument that hyc gives is weak. Closed source unaudited "apps" have no chance of success in the Monero community. And we don't need the government and lawyers to keep it that way.

At the same time there is no talk about the cost that this kind of license introduces. But you have to consider this. There is no free lunch. Introducing legal restrictions on how code can be used has real effects and those are not just positive and an easy win for "the developers".

## vorot93 | 2023-09-06T04:03:45+00:00
> So who gets to be the author? This means Monero devs are in a competition about who gets to make the commit. The winning strategy is to share as little information as possible. Let others go down wrong paths. Don't document anything and make everything as complicated as possible.

I'm not talking about _Monero devs_ (monerod, I assume). I'm speaking specifically about Cuprate.

@Boog900 is the author, public face and main contributor of this project. Cuprate is his brainchild. It's only natural that he gets to be the custodian of copyright to the code.

> Then do posturing to be seen as the guru that has the secret talents to understand the giant messy code base.
> So we end up with a giant, convoluted, undocumented, code base that is essentially a turf war. We need to avoid (re?-)creating this culture at all costs.

Isn't that the way with monerod (or any other node implementation not written by an enterprise) anyway?

> We need to come to the understanding that we share the same values and goals. So we can just cooperate and share information and it does not matter who commits the code in the end.

There will always be entrepreneuring individuals who do a lot more than others, either through code, design or organization. They should also bear a lot more fruit for their efforts.

_We can just cooperate and share information_ is such a naive view of the world that it doesn't work EVEN in open source.
 
> The argument that hyc gives is weak. Closed source unaudited "apps" have no chance of success in the Monero community. And we don't need the government and lawyers to keep it that way.

But they have every chance with criminals, cyberpolice and everyone else seeking to break Monero by giving an easy entry into node's internals. Pretty sure *their* work isn't going to be an open source one if we let them.

> At the same time there is no talk about the cost that this kind of license introduces. But you have to consider this. There is no free lunch. Introducing legal restrictions on how code can be used has real effects and those are not just positive and an easy win for "the developers".

Poor, poor FAANGs and VCs who don't get to do their usual routine of fork (or copypaste) and sell. What a bad real effect of copyleft on the society.

And as I said, CLA is the gold standard for keeping modern copyleft projects from being handcuffed by their own license. I have yet to see what could outweigh this. I know there are drama queens who make a public scandal out of every CLA, but I'm not sure if their presence is a net win for any software project anyway.

## spirobel | 2023-09-06T07:03:28+00:00
>@Boog900 is the author, public face and main contributor of this project. Cuprate is his brainchild. It's only natural that he gets to be the custodian of copyright to the code.

>And as I said, CLA is the gold standard for keeping modern copyleft projects from being handcuffed by their own license. I have yet to see what could outweigh this. I know there are drama queens who make a public scandal out of every CLA, but I'm not sure if their presence is a net win for any software project anyway.

so you are suggesting:

  1. we pay boog900 through the CCS

 2. on top of that every other contributor has to sign his copyright over to him so he can be **"the custodian of the copyright of the code"**?
 
I will bite my tongue now and not make any suggestions. I just hope you are well taken care of by your legal custodians.



## kayabaNerve | 2023-09-07T03:41:57+00:00
I believe MIT, LGPL, GPL, and AGPL all have places.

MIT: You want to contribute your code to the public, without practical restriction.
LGPL: You want to contribute your code to the public, without practical restriction on use, yet ensure external contributions are also FOSS.
GPL: You want to contribute your code to the public, with all contributions and apps built on top also made FOSS licensed.
AGPL: GPL, yet aware networking exists.

This is my *not legal advice* simplification of licenses.

Serai was cited here as an example of split licensing, inappropriately so IMO. I made all of Serai's libraries intended for external use MIT as I do not want to practically restrict any usage of said libraries. The Serai-proper stack is AGPL as it lives in an market environment rife with:

1) Forks
2) Closed-source, trusted projects

And my goal was to prevent the Serai stack from being re-purposed into a closed-source bridge/DEX without attribution and source-availability.

For Serai to be used as an example, Cuprate would have to so argue itself. I do not believe Cuprate can. While the Monero node has been frequently forked, those forks have always (almost always?) been for FOSS projects. I'm unaware of any closed-source forks with any notability.

Even if someone did want to fork Cuprate and offer a 'high-performance Monero alternative', closed source for market protection, I have faith the people interested in technology such as Monero would reject it as being unverifiable and so centralized. Accordingly, I don't believe AGPL offers benefit here for Cuprate.

To discuss practicality:

Recently, RandomX was used in a proprietary miner (a collection of RISC-V chips). An AGPL license on Cuprate's binaries would not have helped in the circumstance as the underlying libs would still be MIT, under a split-licensing scheme. If the libs, such as RandomX, were (L/A)GPL, then any edits would have to be made available *to customers*. This assumes the company behind the miner used the existing RandomX code, and wouldn't write their own, despite:

1) The existing codebase not having a RISC-V JIT backend, showing a significant amount of software development was done
2) RandomX being a documented protocol with alternative implementations (providing proof the protocol can be replicated/another basis)

While RandomX being (L/A)GPL would've caused this company, if they did in fact add a RISC-V JIT backend to the existing code, to be obligated to make it available (something I'd very much appreciate), (A)GPL would force any integrators to also be so bound which could be very limiting. Accordingly, the most I'd advocate is for LGPL.

For the second example, Chainalysis:

1) LGPL would be insufficient here, as their apps likely build on top of the libs, requiring the libs to be GPL/AGPL
2) GPL likely wouldn't prevent them from using any of this code

You'd have to be a customer, prove they use GPL code, and then argue that you being a customer of Chainalysis's data feeds makes you a customer of their proprietary software used to create said data feeds. I'm unsure what the legal precedence is on this, and how much of a fight it may be, yet I'd assume its not practical.

I'd propose making:

1) The libs MIT or LGPL, which would handle the miner situation (yet not the IMO, as a non-lawyer, infeasible to handle Chainalysis situation)
2) The final binary MIT or GPL (AGPL can be a headache to review/manage)

I don't personally see any value to splitting MIT/GPL, and would note LGPL libraries should be widely usable. Accordingly, I don't personally care if the project goes MIT, or if it goes LGPL/GPL. I would find value being able to directly read from the Cuprate DB though, which would require its schema being considered a lib (LGPL at worse). Same for the P2P protocol, and about everything except the final sum binary which hooks it all together.

As one final discussion, this would let someone else fork Cuprate, reusing most of its libs, to build their own node. If LGPL, the libs remain intact, so I wouldn't see the issue there. While the Akula/reth drama was brought up, and hits on this note, that's a mess with many sides. From my understanding, reth has no actual code from Akula (or perhaps a minimal amount, which I won't say allows any transgressions, solely to note that the vast majority was self-written and it accordingly can't be argued as a fork of the Akula codebase) and accordingly should simply be dropped from this discussion. With any system, anyone can look at the design and algorithms and replicate it. Cuprate is itself a replication of Monero.

## Boog900 | 2023-09-07T11:07:49+00:00
Appreciate everyone writing out their thoughts!

I don't want to go with a CLA, the decision made from this issue will be final.

After reading though the discussion, I think there is a lot more support for keeping the binary (A)GPL and putting a less restrictive license on the libraries that make up Cuprate.

I do agree with @kayabaNerve that there isn't much point in doing an MIT/(A)GPL split. Although alright for the libs not specific to Cuprate, licensing the Cuprate specific libs under MIT would reduce the benefits of making the binary (A)GPL in the first place as it would be "easy" to just re-write the binary and then you would have a whole Rust node under MIT. Licensing the Cuprate specific libs under (A)GPL with the binary would *potentially* be harming valid use cases, although you could argue that if someone wants to use a Cuprate specific section they probably should be open sourcing their work but I don't want to force that restriction on people till the end of time.

That leaves us with 2 options: 

1. Full MIT
2. ~LGPL for the libs, (A)GPL for the binary.~

2 might not be possible though due to what I put in my CCS so maybe 3 licenses:

2. MIT: concensus code - everything I make for my current CCS
  LGPL: every other lib that makes up Cuprate
  (A)GPL: the final binary 


## kayabaNerve | 2023-09-07T13:18:09+00:00
I don't think it's extremely easy to write a service successfully handling P2P connections, managing a mempool, ordering a blockchain, performing most-work evaluations calling all the verify functions + properly managing the DB...

Which all would be in the scope of the binary. Though sure, it's much easier when the P2P protocol is a library (especially if a basic message handler exists there), along with the DB schema.

MIT + LGPL sounds like a mess.

## Boog900 | 2023-09-07T13:43:26+00:00
Yeah it wouldn't be extremely easy but it certainly wouldn't be the challenge that starting from scratch is.

> MIT + LGPL sounds like a mess.

I agree.

## Boog900 | 2024-02-02T23:19:49+00:00
Ok I want to make a decision on this. I think the best choice, that will make the most people happy, is split MIT/AGPL with the libs making up Cuprate being MIT and the final binary being AGPL. 

Although I think I would've preferred LGPL + AGPL we can't because of my CCS.

So split MIT/AGPL is what Cuprate will be going with.

## SyntheticBird45 | 2024-02-02T23:38:45+00:00
Sounds fair enough

# Action History
- Created by: Boog900 | 2023-08-29T20:33:42+00:00
- Closed at: 2024-02-02T23:19:49+00:00
