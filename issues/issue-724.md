---
title: Monero Research Lab Meeting - Wed 03 August 2022
source_url: https://github.com/monero-project/meta/issues/724
author: Rucknium
assignees: []
labels: []
created_at: '2022-08-01T17:01:42+00:00'
updated_at: '2022-08-10T06:07:52+00:00'
type: issue
status: closed
closed_at: '2022-08-10T06:07:52+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

3. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

4. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

5. Any other business

6. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#722 

# Discussion History
## UkoeHB | 2022-08-03T18:15:31+00:00
`[08-03-2022 17:00:02] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/724`
`[08-03-2022 17:00:02] <UkoeHB> 1. greetings`
`[08-03-2022 17:00:02] <UkoeHB> hello`
`[08-03-2022 17:00:28] <dangerousfreedom> Hi!`
`[08-03-2022 17:00:45] <xmrack[m]> hey`
`[08-03-2022 17:01:53] <Rucknium[m]> Hi`
`[08-03-2022 17:02:11] <jberman[m]> hello`
`[08-03-2022 17:02:30] <tevador> hi`
`[08-03-2022 17:04:13] <UkoeHB> 2. updates, what has everyone been working on?`
`[08-03-2022 17:05:04] <dangerousfreedom> This week I implemented bulletproofs in Rust and I will start scanning the blockchain for the bp transactions this weekend. Although my Python code works, it is tooo slow. So I thought that making another implementation in Rust would be more efficient and serai (kayabaNerve) can also profit from that.`
`[08-03-2022 17:05:41] <dangerousfreedom> Also, I finished my first reading about Seraphis and have some questions about it. But I will let them for the end of the meeting.`
`[08-03-2022 17:05:58] <Rucknium[m]> OSPEAD, with a focus on forecasting and evaluating out-of-sample risk.`
`[08-03-2022 17:06:15] <jberman[m]> reviewing trezor's hf PR, then planning to move over to reviewing the serialization overhaul (7999/vtnerd's alternative)`
`[08-03-2022 17:07:25] <UkoeHB> me: still working on legacy balance recovery for my seraphis lib (will probably be doing less hours this month, on vacation)`
`[08-03-2022 17:08:18] <xmrack[m]> I've been working on the MAGIC grant, I've finished processing all the datasets and now hyperparameter tuning the models. If anyone has free time over the next few weeks I'd love for some constructive feedback on the paper. `
`[08-03-2022 17:10:18] <UkoeHB> 3. discussion, anybody have comments/questions?`
`[08-03-2022 17:10:29] <dangerousfreedom> xmrack[m]: Nice! I will try to in the next 2-3 weeks.`
`[08-03-2022 17:10:56] <Rucknium[m]> xmrack: Are you ready to share some preliminary results here?`
`[08-03-2022 17:11:44] <xmrack[m]> Yea, one second`
`[08-03-2022 17:12:19] <tevador> I have a 100% assembly implementation of the X25519 key exchange using mulx/adcx/adox instructions. Will post some benchmarks later this week. That's probably as fast as output scanning can get with current CPUs.`
`[08-03-2022 17:12:31] <kayabanerve[m]> Hello :)`
`[08-03-2022 17:12:39] <UkoeHB> tevador: very cool, thanks for taking that up`
`[08-03-2022 17:12:54] <selsta> tevador: what's the difference to the supercop lib we use?`
`[08-03-2022 17:12:59] <kayabanerve[m]> I implemented BP+ verification in Rust as well, sorry for being a bit late to comment`
`[08-03-2022 17:13:35] <tevador> selsta: supercop doesn't use mulx, only legacy mul. And this is X25519, which only works on the X coordinate.`
`[08-03-2022 17:14:37] <Rucknium[m]> tevador: Fantastic. Would the code apply to Seraphis outputs (enotes) too?`
`[08-03-2022 17:14:56] <tevador> I estimate ~30% speed-up for x86 and up to 3x speed-up for ARM64, which also has a full assembly implementation (not by me).`
`[08-03-2022 17:15:25] <xmrack[m]> It appears that the AdaBoost random forrest is performing the best when tested on mainnet transactions, with a 19% accuray. The gradient boosted classifier also achieves similar accuracies but with very difffernt feature importances. The results may vary as my mainnet validation dataset only includes ~72 ring... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/61a172d1a3baf69a251633477a118328deeb21f1)`
`[08-03-2022 17:15:27] <tevador> Rucknium[m]: the plan is to use X25519 with Seraphis`
`[08-03-2022 17:17:43] <jberman[m]> tevador: 🎉`
`[08-03-2022 17:17:55] <UkoeHB> dangerousfreedom: what are your questions about seraphis?`
`[08-03-2022 17:18:17] <Rucknium[m]> xmrack: In the machine learning field, is there a typical explanation for why two ML algorithms would have quite different feature importance rankings?`
`[08-03-2022 17:19:00] <dangerousfreedom> UkoeHB: 1) To make sure I understood, if you could boil down Seraphis to two concepts, what would them be? No ring signatures anymore (usage of linking-tags instead) and separation of this part (membership) from the rest of the transaction? `
`[08-03-2022 17:19:00] <dangerousfreedom> 2) What is state of the implementation? Do we have a minimum wallet or minimum node?`
`[08-03-2022 17:19:00] <dangerousfreedom> 3) Is there already a template of a transaction with all the inputs and outputs like we would see at the json representation of a tx?`
`[08-03-2022 17:20:01] <kayabanerve[m]> The membership proof is still for a specified subset. It's key images which are replaced by linking tags.`
`[08-03-2022 17:20:30] <UkoeHB> 1) separation of 'membership proof' and `
`[08-03-2022 17:20:33] <UkoeHB> whoops`
`[08-03-2022 17:20:52] <tevador> "key image" is a colloquial term for a linking tag; it's the same thing`
`[08-03-2022 17:21:11] <dangerousfreedom> Yeah`
`[08-03-2022 17:21:47] <UkoeHB> 1) separation of 'membership proof' and 'ownership proof' into two pieces; more powerful user key structures are possible with the new key image construction`
`[08-03-2022 17:21:57] <kayabanerve[m]> While that is true in purpose, and it's a bit awkward to be changing terminology, I do appreciate highlighting their vastly different implementation.`
`[08-03-2022 17:21:58] <dangerousfreedom> Actually, the linking tag would be the stealth_address, right?`
`[08-03-2022 17:21:59] <xmrack[m]> Rucknium[m]: Yes, each model uses different algorithms which separate the features to the best of their ability and correlate patterns for each of the ring positions. The way they go about doing this could easily cause a difference in feature importance across multiple models. This is mainly why I'm training a few different ones along with a neural network. `
`[08-03-2022 17:22:02] <dangerousfreedom> These would be the members?`
`[08-03-2022 17:22:09] <UkoeHB> I basically gave up on the linking tag terminology lol`
`[08-03-2022 17:22:58] <dangerousfreedom> Haha`
`[08-03-2022 17:23:06] <kayabanerve[m]> Eh. We should encourage it`
`[08-03-2022 17:23:13] <kayabanerve[m]> But yes, does take more time to do so :p`
`[08-03-2022 17:25:59] <UkoeHB> the kind of linking tag we have is a key image, so I think it's fine`
`[08-03-2022 17:26:10] <Rucknium[m]> xmrack: I think medium-term it would be good to estimate confidence intervals for the F1-score on the mainnet transactions since the sample size is small. The typical approach would be bootstrapping as long as the F1-score satisfies the technical regularity condition of being a _pivotal statistic_.`
`[08-03-2022 17:26:40] <kayabanerve[m]> I do have a side comment on Seraphis dev/impl, further inspired by a recent thing I noticed from BP+. BP+ implemented new generators and a new transcript. While I have no idea why (as under batch verification, there should be no benefit to new generators of the same quantity/method, especially since these aren't even batched together). The new transcript is... negative however. It's the same methodology as the previous one`
`[08-03-2022 17:26:40] <kayabanerve[m]> (with all the idiocy it brought), yet with a DST. While I don't mind the DST, it broke type safety because Monero keys aren't type safe :/`
`[08-03-2022 17:26:55] <UkoeHB> 2) the core library is mostly done, I just need to finish integrating legacy enotes and add a coinbase tx type; the core library should be well-featured enough to build a wallet from`
`[08-03-2022 17:26:59] <Rucknium[m]> Hopefully there is a standard and mathematically-proven way to do that with ML. If there is not, I will be Very Upset with the machine learning field :P`
`[08-03-2022 17:27:26] <kayabanerve[m]> It also performed unnecessary operations in its initial parameters, which I can't explain. While yes, I know the BP+ code is settled, and this is -dev commentary, I do believe there is the discussion with Seraphis about ensuring we don't continue such oddities.`
`[08-03-2022 17:27:53] <xmrack[m]> Rucknium[m]: Off the top of my head I’m not sure. But I’ll look into this`
`[08-03-2022 17:28:23] <kayabanerve[m]> While UkoeHB is a great developer, and I know they have fixed a lot of issues like this in their work on a new library and new wallet I want to highlight the value of independent implementation for full review, both of theory and practice.`
`[08-03-2022 17:28:26] <UkoeHB> 3) there is no serialization finalized - that kind of thing is up to future developers, but the main tx type is here https://github.com/UkoeHB/monero/blob/seraphis_lib/src/seraphis/txtype_squashed_v1.h`
`[08-03-2022 17:29:27] <UkoeHB> there are several areas where serialization can be optimized compared to the C++ representation, I'll probably have to write some things down for that`
`[08-03-2022 17:29:56] <rbrunner> I think this will bring much fun because it does not derive from the CryptoNote tx type that now permeates the code from bottom to top`
`[08-03-2022 17:31:38] <dangerousfreedom> Ok, nice! Thank you for the answers!`
`[08-03-2022 17:31:54] <vtnerd> UkoeHB as a quick remninder (which you probably know), the cryptonote serialization is separate from the work that jberman[m] is referencing, and is a bit more compact in binary size`
`[08-03-2022 17:32:00] <UkoeHB> kayabanerve[m]: I already forked the BP+ code to use the seraphis transcript system + generator factory https://github.com/UkoeHB/monero/blob/seraphis_lib/src/seraphis/bulletproofs_plus2.h`
`[08-03-2022 17:32:18] <UkoeHB> vtnerd: I mean serialization in general (of any kind)`
`[08-03-2022 17:32:25] <UkoeHB> all I have is a C++ struct`
`[08-03-2022 17:33:05] <UkoeHB> kayabanerve[m]: I believe switching to seraphis transcripts actually sped things up a bit since blake2b is a bit faster than keccak`
`[08-03-2022 17:33:13] <vtnerd> for seraphis? a brand new one? probably makes sense to start new but man`
`[08-03-2022 17:33:23] <UkoeHB> yes`
`[08-03-2022 17:33:32] <dangerousfreedom> I have another point too. Maybe in resonance with what kayabaNerve said.`
`[08-03-2022 17:34:13] <dangerousfreedom> I'm not happy with the non-canonical points and scalars stored in the blockchain. Although I didn't find any bug that could definitely lead to inflation, these points and scalars can lead to wrong signatures and fungibility issues that will cause trouble for different nodes and wallets implementations, which are inevitable as the project grows. Moreover, I believe we should change the mindset that we have now which is`
`[08-03-2022 17:34:13] <dangerousfreedom> 'trust in the code' to something like 'trust in the math' which is a more robust argument as math proofs are usually less prone to errors than implementations of these math proofs.`
`[08-03-2022 17:34:19] <kayabanerve[m]> I know :p I'm very happy you covered both of these. I'm discussing items of this level of eccentricity in general though. While you're also working hard against it, I'm highlighting how we're individuals in our own ecosystems, and how certainty there...`
`[08-03-2022 17:34:41] <vtnerd> its probably a great chance to break away from cruft, and finally get some "librarization" going for downstream projects, but hopefully it won't turn into too big of a project`
`[08-03-2022 17:34:52] <UkoeHB> I refuse to write this kind of disgusting mess in my library lmao https://github.com/UkoeHB/monero/blob/24ef2d6d8742abddf8e090faaba518aa42a04ba7/src/ringct/rctTypes.h#L335`
`[08-03-2022 17:35:11] <kayabanerve[m]> The hero we need`
`[08-03-2022 17:35:16] <vtnerd> yeah and `/src/ringct` is one of the better folders`
`[08-03-2022 17:35:40] <vtnerd> well kaya the problem has been doing librization meant total pain with compatiability`
`[08-03-2022 17:35:44] <kayabanerve[m]> Iirc you also made it so we don't need to write commitments into the bp to do verification which is great`
`[08-03-2022 17:36:05] <vtnerd> but since thats being blown up it does make it easier in one sense, but the older code still needs to be present for blockchain verificaiton :/`
`[08-03-2022 17:36:41] <vtnerd> anyway I;ll stop hijacking this, ukoehb if you need seralization suggestions thats one of my few specialities`
`[08-03-2022 17:36:58] <vtnerd> the interface I developed could also do tagless (like cryptonote)`
`[08-03-2022 17:37:06] <kayabanerve[m]> vtnerd: This is about librarization. It's about implementation preferences of developers or decisions relevant to an ecosystem which make it hard to move out. I'm commenting independent implementation is one of the highest forms of review and enables commenting on the portability of decisions as well`
`[08-03-2022 17:37:06] <vtnerd> so most compact`
`[08-03-2022 17:37:10] <UkoeHB> vtnerd: you may want to spearhead that effort, since I don't plan to do anything with serialization`
`[08-03-2022 17:37:35] <UkoeHB> once legacy stuff and the coinbase tx type is ready, I am moving on (after finishing the paper)`
`[08-03-2022 17:37:41] <rbrunner> I am a bit confused. Why should existing serialization be unfit for sure?`
`[08-03-2022 17:37:54] <vtnerd> ah - you'll have enough with trying to get seraphis integrated, etc. ?`
`[08-03-2022 17:37:59] <kayabanerve[m]> While portability largely isn't an issue, I'd highlight the rct::key type ambiguity and custom hash to point as examples. I'm mainly concerned about the eccentric preferences which have pervaded monero's history though`
`[08-03-2022 17:37:59] <vtnerd> it is a massive effort already`
`[08-03-2022 17:38:12] <rbrunner> After all we serialize all kinds of things already, no?`
`[08-03-2022 17:38:24] <vtnerd> the existing serialziation for cryptonote is decent actually`
`[08-03-2022 17:38:54] <vtnerd> its just that the interface I wrote could handle epee/json/(most) cryptonote/msgpack`
`[08-03-2022 17:39:01] <vtnerd> whereas now there are multiple in the codebase`
`[08-03-2022 17:39:50] <vtnerd> there are several "tricks" in the existing tx that can't be duplicated easily with a generic library, since it reuses array length values across fields, etc., that is extremely custom`
`[08-03-2022 17:40:11] <dangerousfreedom> I think it is impossible to go from rct::key -> point with certainty. The other way round is possible. I dont know if it happens in the code.`
`[08-03-2022 17:40:14] <vtnerd> and as ukoehb will point out, that code is a bit gross and hard to follow due to the custom nature`
`[08-03-2022 17:40:17] <Rucknium[m]> Making the protocol itself more strict can improve development decentralization. Hopefully there could be less reliance on the actual wallet2 code and more reliance on a protocol specification. (This goes for decoy selection and other forms of defects in tx uniformity IMHO too.)`
`[08-03-2022 17:41:18] <rbrunner> With every additional wish here right now we cooly add one more person year of work :)`
`[08-03-2022 17:44:11] <dangerousfreedom> I will finish my CCS by the end of this month and I would like to continue working for the betterment of Monero as I have built in the past 6 months my tools and knowledge about Monero to do so. Specially regarding the security and cryptography behind, as I said, we should really make sure to have only canonical scalars and points stored in the bc. I will propose a new CCS this month and would like to know how I can help.`
`[08-03-2022 17:44:11] <dangerousfreedom> :)`
`[08-03-2022 17:44:33] <vtnerd> if ukoehb does rewrites similar to multisig it will help out big time, regardless of any strict spec being written`
`[08-03-2022 17:44:57] <dangerousfreedom> From my side, I would like to continue working on my monero-inflation-checker (as I still have BP+ to check and also I believe I can improve the content and make more implementations in Rust) and help to implement the necessary functions for Seraphis/Jamtis. Do you think I could help you, jberman, tevador and someone else to implement the necessary stuff for Seraphis/Jamtis? How is the work structured so far? Where is the`
`[08-03-2022 17:44:57] <dangerousfreedom> TODO list of the project ? :p`
`[08-03-2022 17:45:20] <vtnerd> fluffy had one somewhere a long time ago`
`[08-03-2022 17:45:35] <vtnerd> doing what ukoehb is finally doing with txes was on that list`
`[08-03-2022 17:47:13] <rbrunner> As I mentioned, hightlight every place in the code that now references cryptonote::transaction and mark it for possible rewrite.`
`[08-03-2022 17:47:16] <vtnerd> I don't think an updated one exists`
`[08-03-2022 17:47:28] <rbrunner> Then sit back and marvel at about half of all code marked ... :)`
`[08-03-2022 17:47:52] <UkoeHB> yeah idk anything about how tx serialization is handled`
`[08-03-2022 17:48:10] <vtnerd> yeah thats the one concern I have with the seraphis proposals, its going to be a beast to integrate and will likely take longer than expected`
`[08-03-2022 17:48:23] <UkoeHB> figuring out the core library already takes up my entire attention`
`[08-03-2022 17:48:36] <vtnerd> which isn't to say that Im against it, just that it will likely be a slog`
`[08-03-2022 17:48:49] <rbrunner> I don't say UkoeHB did not do good work, maybe there really is no way around this hard brake, but boy will this bring work with it.`
`[08-03-2022 17:48:57] <rbrunner> *break`
`[08-03-2022 17:49:01] <vtnerd> oh no trying to get seraphis shoehorned into all parts is already a huge task`
`[08-03-2022 17:49:16] <vtnerd> yeah billable hours for all!`
`[08-03-2022 17:49:31] <rbrunner> For all our dozens of devs? Hurray!`
`[08-03-2022 17:49:42] <UkoeHB> vtnerd: it should be possible to completely deprecate wallet2 aside from wallet file migration, so hopefully that helps`
`[08-03-2022 17:49:49] <vtnerd> yeah it always sounds good until you realize it just means you become overworked`
`[08-03-2022 17:49:57] <rbrunner> :)`
`[08-03-2022 17:50:15] <vtnerd> yes, we can move stuff to the side but it always have to be around somewhere sadly`
`[08-03-2022 17:50:33] <rbrunner> But well, maybe the introductin of RingCT looked similar at start, and we could do it after all`
`[08-03-2022 17:50:47] <vtnerd> or maybe we just make wallet2 forcibly sweep all coins, and then start fresh`
`[08-03-2022 17:51:04] <Rucknium[m]> Hiring freezes and layoffs have started in the tech sector. Could be a good time to do some talent scouting.`
`[08-03-2022 17:51:15] <UkoeHB> vtnerd: it won't be necessary, the new library can do full legacy balance recovery + spend legacy coins`
`[08-03-2022 17:51:18] <rbrunner> That's the spirit.`
`[08-03-2022 17:51:39] <UkoeHB> or will, when I'm done working`
`[08-03-2022 17:52:06] <vtnerd> ok you are ambitious. clear out your calendar lol`
`[08-03-2022 17:52:09] <rbrunner> I think that alone will be a very big plus. Thank you for that.`
`[08-03-2022 17:52:29] <dangerousfreedom>  Is there any discussion about changing the crypto libraries (and therefore the serialization)? What if we took a LibSodium or OpenSSL libraries?`
`[08-03-2022 17:55:30] <UkoeHB> dangerousfreedom: no the monero crypto library is too deeply embedded`
`[08-03-2022 17:55:56] <rbrunner> Maybe that would also be quite risky and would need very, very good testing.`
`[08-03-2022 17:56:05] <UkoeHB> we need the raw crypto library for optimized implementations anyway`
`[08-03-2022 17:57:16] <dangerousfreedom> I believe we should consider enforcing some encodings at least to be compatible canonical points and scalars for Seraphis. As in my opinion this presents a far bigger risk than quantum computing. `
`[08-03-2022 17:58:12] <dangerousfreedom> (If we are only planning to change the library for post-quantum cryptography schemes someday)`
`[08-03-2022 17:58:53] <UkoeHB> vtnerd: I think it would be even more work if legacy stuff wasn't fully integrated, because there are balance recovery overlap problems around the transition. `
`[08-03-2022 17:59:19] <UkoeHB> you'd end up in a situation where wallets need an instantiation of both wallet2 and spwallet`
`[08-03-2022 17:59:48] <UkoeHB> dangerousfreedom: yes everything is already enforced to some degree`
`[08-03-2022 18:00:32] <UkoeHB> prime subgroup isn't enforced except where necessary for efficiency reasons, but crypto point/scalar serialization should be enforced everywhere`
`[08-03-2022 18:01:40] <UkoeHB> ok that's the end of the hour, so I'll call it here; thanks for attending everyone; I'm happy to answer any further questions about seraphis in this channel (as usual)`
`[08-03-2022 18:02:08] <dangerousfreedom> Thank you :)`
`[08-03-2022 18:04:47] <vtnerd> dangerousfreedom the serialization for crypto points just uses ed25519 standard form. every ed25519 library uses that same format afaik, and it works just fine (albeit somewhat slow to unpack the x-coord)`
`[08-03-2022 18:05:09] <vtnerd> the serialization we have to is tracking multiple public_keys, integers, etc`
`[08-03-2022 18:06:16] <vtnerd> monero has used a custom implementation that is strictly ordered, such that no "tag" or "value" information is serialization - all fields must be in a specific order`
`[08-03-2022 18:07:06] <vtnerd> so ASN.1, msgpack, and all kinds of binary formats are "less acceptable" because they bloat the binary size a bit more with field type/name information`
`[08-03-2022 18:09:17] <vtnerd> Im not sure of a comparable standard serialization format off the top of my head, although I will search for one to help with seraphis/ukoehb`
`[08-03-2022 18:09:35] <vtnerd> but we'll probaly just continue with custom, because a strictly ordered format breaks golang, javascript, and a whole bunch of other languages that assume unordered fields in their framework`
`[08-03-2022 18:10:19] <dangerousfreedom> vtnerd: Oh, thank you for the detailed explanation.`
`[08-03-2022 18:12:51] <UkoeHB> vtnerd: by crypto serialization I mean whether a point can be decoded from 32 bytes or if a scalar is in reduced form (sc_check())`

# Action History
- Created by: Rucknium | 2022-08-01T17:01:42+00:00
- Closed at: 2022-08-10T06:07:52+00:00
