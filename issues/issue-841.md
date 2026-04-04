---
title: Monero Research Lab Meeting - Wed 24 May 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/841
author: Rucknium
assignees: []
labels: []
created_at: '2023-05-23T19:45:51+00:00'
updated_at: '2023-06-05T19:27:36+00:00'
type: issue
status: closed
closed_at: '2023-06-05T19:27:36+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: [Consider removing the tx_extra field](https://github.com/monero-project/monero/issues/6668).

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100).

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#839 

# Discussion History
## plowsof | 2023-05-31T18:53:09+00:00
Logs 
```
17:01:09 <UkoeHB> meeting time https://github.com/monero-project/meta/issues/841

17:01:09 <UkoeHB> 1. greetings

17:01:09 <UkoeHB> hello

17:01:12 <vtnerd> hi

17:01:20 <rbrunner> Hello

17:02:09 <Rucknium[m]> Hi

17:03:35 <UkoeHB> 2. updates, what's everyone working on?

17:03:51 <xmrack[m]> Hi

17:04:07 <UkoeHB> me: slowly working on escrowed multisig design for monerokon.

17:05:12 <vtnerd> I like that - I'm slowly working on bulletproof++ -
https://github.com/ElementsProject/secp256k1-zkp/files/10130246/BP_PP_proofs.pdf

17:05:30 <Rucknium[m]> Experimented with cluster computing software on Monero Research Computing server and
settled on an R native solution for now. Developing and testing some R code at scale on the cluster to make
sure there is no RAM blowup.

17:05:46 <vtnerd> I previously thought the linked pdf was just a copy of the eprint, but its actually just the
math equations for the protocol

17:06:35 <vtnerd> I have no idea how to do a batched proof like we had previously, so I will focus on just
getting the single case

17:06:54 <vtnerd> I also got the new serialization pushed out, but that is less of a MRL task

17:07:25 <UkoeHB> batching should be possible wherever generators can be shared

17:08:18 <vtnerd> ah ok, yeah that makes sense, but I feel like i will still botch it lol

17:08:47 <vtnerd> we previously only batched per tx ?

17:08:58 <vtnerd> nvm, I can find that in the code easily enough

17:09:24 <ghostway[m]> Sorry for my ignorance about bulletproofs, but how does batching work there? Is it
clever maths and/or not recomputing stuff or using simd instructions (or all together because the first part
can be precomputed before the parallel part)?

17:09:24 <ghostway[m]> Anyway, probably tomorrow I'll start to do some wallet work

17:10:01 <UkoeHB> ah there's batched verification and aggregated proving which are different; batched
verification is easy but idk how the aggregated proving works

17:14:53 <ghostway[m]> Did I stump the meeting?...

17:15:12 <UkoeHB> ghostway[m]: batched verification is possible because proofs are verified by summing EC
points and checking they equal identity. You can combine multiple proof verifications in one large
multiexponentiation (adding all proofs together at the same time) by multiplying the elements of each proof
with a random verifier-selected number (ensuring no proof cross-talk is possible). You get perf gains from the

17:15:12 <UkoeHB> multiexponentiation algorithm and from sharing generators between proofs.

17:15:12 <ghostway[m]> s/stump/disrupt/

17:16:38 <Rucknium[m]> Matrix<>IRC bridge is having problems again.

17:17:05 <UkoeHB> I think it's working fine

17:17:47 <Rucknium[m]> Matrix users can see all IRC messages here: https://libera.monerologs.net/monero-
research-lab/20230524

17:18:30 <Rucknium[m]> "ah there's batched verification and aggregated proving which are different; batched
verification is easy but idk how the aggregated proving works" This message didnt come through to Matrix AFAIK

17:18:34 <k4r4b3y[m]1> I am using matrix. Liberalogs are no different so far.

17:19:01 <ghostway[m]> It is for me, thanks!

17:20:40 <Alex|LocalMonero> https://github.com/monero-project/monero/issues/8757

17:20:40 <Alex|LocalMonero> Any chance we can allow fast N-of-N multisig setup?

17:21:00 <ghostway[m]> I think I should just come to irc. I have to find my tor config lol

17:21:43 <Alex|LocalMonero> The post-kex round is unnecessary because all keys are involved in the signing.

17:22:47 <Alex|LocalMonero> This will make the 2/2 multisig setup a single round-trip long, simplifying it
greatly in a stateless API context.

17:24:05 <UkoeHB> Alex|LocalMonero: that's kind of a dev question

17:24:17 <Alex|LocalMonero> Got it, apologies.

17:24:41 <Alex|LocalMonero> I thought it was relevant to research in case there are security risks related to
bypassing the post-kex round.

17:24:59 <Alex|LocalMonero> Just wanted to make sure it's clear.

17:27:16 <Rucknium[m]> On this recent off-by-one error in decoy selection: IMHO, treating Monero's statistics
like its cryptography is treated would be a good idea. For cryptography, formal specifications are written.
Then code is independently audited to make sure that the specification is executed properly.

17:27:56 <Rucknium[m]> This would apply at least to the decoy selection algorithm and Dandelion++
implementation.

17:30:32 <Rucknium[m]> I have heard people, e.g. kayabaNerve, say that wallet2's decoy selection algorithm is
difficult to port to another language or implementation. If there was a formal specification, maybe it would
be less so.

17:31:37 <rbrunner> Hmm, but then, if you implement a spec, code in other languages would maybe audits as
well, at least in principle

17:31:48 <rbrunner> *maybe need audits

17:31:53 <UkoeHB> writing a spec does imply some cost

17:32:20 <UkoeHB> not a bad thing to have though, of course

17:32:27 <Rucknium[m]> That would be a good thing IMHO.

17:33:07 <Rucknium[m]> We could start by reverse-engineering a spec from the current code.

17:33:52 <rbrunner> Or, we look forward, and start a spec based approach with Seraphis.

17:34:14 <ghostway[m]> I'd agree, I don't think it would require audits, it would only lessen the impact of
bad coding

17:36:17 <Rucknium[m]> A crude simple test is to take some alternative code and generate thousands or millions
of (unused) rings against the mainnet blockchain and test statistical equivalence.

17:37:39 <Rucknium[m]> That's what I did (except no actual blockchain, just the output indices) to validate
the Python and R ports of parts of wallet2's decoy selection algorithm here: https://github.com/mj-xmr/monero-
mrl-mj/tree/master/decoy

17:38:47 <rbrunner> Maybe stupid question, but why didn't this unearth some hints about the recent one-off
bug?

17:39:08 <rbrunner> I guess you didn't have that in your alternative implementations?

17:39:31 <UkoeHB> it's a small hard-to-see edge condition

17:39:50 <Rucknium[m]> (the statistical test code isn't in the repo, but the implementations are there)

17:40:01 <rbrunner> Not enough cases randomly generated that hit it, then?

17:40:19 <rbrunner> So no difference sticks out

17:40:28 <Rucknium[m]> Not a stupid question. I think this piece of the code was isolated from the part that
decided which outputs werwe eligible for decoy selection

17:41:42 <Rucknium[m]> There are two more things: a KS test, which is what I did has "low power". That means
that it can be hard for it to detect very small differences. A KS test is very general, which is why it's
used. And:

17:43:16 <Rucknium[m]> R is indexed from 1. C++ is indexed from zero. Like I said, I think this code that I
worked on was isolated from the main problem, so I would not have caught it anyway. But even if I saw it, I
may have assumed it was an off-by-one error in my own code because of the R port. Or maybe I would hav
erealized it.

17:44:10 <rbrunner> Interesting, thanks

17:44:34 <Rucknium[m]> This is why with an audit or more complete test you would want to test using the actual
mainnet blockchain to make sure there is "100% code coverage" of the test

17:46:43 <UkoeHB> A good place to start would be writing an MRL research issue outlining the algorithm that we
have.

17:47:06 <UkoeHB> If someone writes that issue: Rucknium[m] jberman[m] jeffro256[m] then I will review it.

17:48:25 <Rucknium[m]> Reverse-engineering a spec is on my to-do list. But it's much easier to work with
someone who can read the original C++, e.g. jeffro256

17:49:04 <Rucknium[m]> UkoeHB: Thanks.

17:50:32 <UkoeHB> Are there any other topics we should touch on before the end of the meeting?

17:54:07 <UkoeHB> ok I think that wraps it up, thanks for attending everyone


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-05-23T19:45:51+00:00
- Closed at: 2023-06-05T19:27:36+00:00
