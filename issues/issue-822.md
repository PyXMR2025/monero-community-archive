---
title: Monero Research Lab Meeting - Wed 05 April 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/822
author: Rucknium
assignees: []
labels: []
created_at: '2023-04-04T16:29:58+00:00'
updated_at: '2023-04-11T16:07:03+00:00'
type: issue
status: closed
closed_at: '2023-04-11T16:07:02+00:00'
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

#818 

# Discussion History
## UkoeHB | 2023-04-05T18:01:15+00:00
`[04-05-2023 16:59:58] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/822`
`[04-05-2023 16:59:58] <UkoeHB> 1. greetings`
`[04-05-2023 16:59:58] <UkoeHB> hello`
`[04-05-2023 17:00:12] <ArticMine[m]> Hello `
`[04-05-2023 17:00:31] <compdec[m]> Hello`
`[04-05-2023 17:00:33] <rbrunner> Hello`
`[04-05-2023 17:00:36] <Rucknium[m]> Hi`
`[04-05-2023 17:00:39] <tevador> Hi`
`[04-05-2023 17:00:43] <hbs[m]> Hello`
`[04-05-2023 17:00:43] <jeffro256[m]> Howdy`
`[04-05-2023 17:01:00] <vtnerd__> hi`
`[04-05-2023 17:02:01] <UkoeHB> 2. updates, what's everyone working on?`
`[04-05-2023 17:02:42] <jeffro256[m]> I implemented the solution for research lab issue 109 in this PR: https://github.com/monero-project/monero/pull/8815`
`[04-05-2023 17:03:04] <UkoeHB> me: new CCS https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/384 , updated the seraphis draft https://github.com/UkoeHB/Seraphis , next need to write the jamtis-instantiation companion paper`
`[04-05-2023 17:03:06] <Rucknium[m]> Monitoring Mordinals. In the last 3 days Mordinal minting has essentially ceased: https://gist.github.com/Rucknium/67cc9efdf7e43a40c52417611b322d43`
`[04-05-2023 17:03:51] <vtnerd__> LWS stuff, and reviewed jberman patch for decoy selection off by one`
`[04-05-2023 17:04:14] <Rucknium[m]> I also started reviewing jeffro256 's code ^ to avoid selecting coinbase outputs when spending non-coinbase outputs.`
`[04-05-2023 17:04:16] <UkoeHB> vtnerd__: how's it going with BP++?`
`[04-05-2023 17:04:54] <Rucknium[m]> I will probably do a write-up next week on the empirical privacy effects of Mordinals (+ coinbase outputs).`
`[04-05-2023 17:05:14] <jeffro256[m]> Nice `
`[04-05-2023 17:05:36] <vtnerd__> haven't had the time, busy with personal it stuff and taxes, etc.`
`[04-05-2023 17:05:55] <jeffro256[m]> UkoeHB: If you had to summarize the seraphis doc updates in one sentence, what would it be?`
`[04-05-2023 17:06:02] <vtnerd__> I'll ping you privately about it later, as there simply isn't enough to report here`
`[04-05-2023 17:06:12] <UkoeHB> vtnerd__: ok thanks`
`[04-05-2023 17:07:08] <UkoeHB> seraphis paper updates: minor cleanup, cut out implementation recommendations, simplified composition proof writeup, added grootle proof construction + security proof (mostly copied from lelantus-spark paper)`
`[04-05-2023 17:09:32] <Rucknium[m]> I wonder if compdec has something they want to bring up.`
`[04-05-2023 17:09:40] <UkoeHB> I decided not to do anything beyond that with the main seraphis paper, since security proofing and whatnot is not my area of enthusiasm or expertise. It is in a good spot to get help upgrading the security model.`
`[04-05-2023 17:10:58] <Rucknium[m]> Sounds like a good plan to me.`
`[04-05-2023 17:11:00] <narodnik> greets`
`[04-05-2023 17:11:10] <narodnik> will i get kicked now for saying hello`
`[04-05-2023 17:11:35] <UkoeHB> narodnik: no`
`[04-05-2023 17:11:48] <UkoeHB> 3. discussion; today we must return to the tx_extra issue`
`[04-05-2023 17:12:24] <narodnik> about the ECIP proof, we are in the middle of some stuff and it takes all my time, but i started writing the benchmarks on the side`
`[04-05-2023 17:12:24] <UkoeHB> I summarized my position here: https://github.com/monero-project/monero/issues/6668#issuecomment-1476531556`
`[04-05-2023 17:13:09] <narodnik> now im doing the normal pedersen commit, have the scheme written in sage, then will begin constructing circuits with modified ECIP proof to benchmark against normal pedersen commit`
`[04-05-2023 17:14:34] <UkoeHB> thanks narodnik `
`[04-05-2023 17:16:37] <UkoeHB> Does anyone have anything new to add on the subject of tx_extra?`
`[04-05-2023 17:17:06] <rbrunner> I didn't see any discussion about tx_extra anywhere for quite some time now, seems the subject has exhausted itself a bit lately`
`[04-05-2023 17:17:30] <tevador> there has been some activity here: https://github.com/monero-project/monero/issues/6668`
`[04-05-2023 17:17:38] <Rucknium[m]> IMHO, the "encrypted by default" phrase is a little misleading to most readers. By default, wallet2 would not be able to put arbitrary data into tx_extra, encrypted or not AFAIK. And if the encryption "rule" has no enforcement mechanism whatsoever, then "by default" is misleading.`
`[04-05-2023 17:18:09] <jeffro256[m]> <UkoeHB> "I summarized my position here..." <- I mostly agree with this with one difference: I don't think we should trivialize that one bit of information of "is this field present or not?" This one bit of likability is different from other bits in say, input selection, in that the "cost" of this bit is very high compared to other entropy. It is represents whether or not a user uses some functionality. In can be reasonable`
`[04-05-2023 17:18:09] <jeffro256[m]> expected that a user who uses that field is more likely to use it in the future, and one who doesn't is less likely. Same for the users that a user interacts with. Long story short, tx_extra, if kept, should be mandatory because even giving transaction constructors the option of having it be present is a bigger privacy issue than initially assumed IMO`
`[04-05-2023 17:19:49] <vtnerd___> I think the phrasing is close enough, the information that goes into tx extra from wallet2 doesn't leak user info`
`[04-05-2023 17:20:19] <UkoeHB> Rucknium[m]: the current trajectory is changing tx_extra for seraphis, in which case there would not be wallet2. The core library would encrypt/decrypt tx extra contents by default. Whether anything above that adds tx_extra data to txs or uses recovered tx_extra data isn't pertinent.`
`[04-05-2023 17:20:22] <vtnerd___> but if accuracy is that important it can be reworked to say that`
`[04-05-2023 17:20:54] <vtnerd___> ah yes, seraphis won't use tx extra for the ecdh pub, right?`
`[04-05-2023 17:21:22] <jeffro256[m]> Intuitively, tx_extra is used for applications. Users who use an application interact with other users who use an application. Thus, whether tx_extra is present or not I think is a stronger heuristic for linkability than one might initially assume.`
`[04-05-2023 17:21:28] <UkoeHB> vtnerd___: right, currently there are no standard uses of tx_extra`
`[04-05-2023 17:22:08] <tevador> the new tx_extra should also be prunable`
`[04-05-2023 17:22:27] <UkoeHB> tevador: yes I was thinking more about that today, it should be doable fairly easily`
`[04-05-2023 17:22:32] <jeffro256[m]> Agreed, it isn't used for consensus anyways `
`[04-05-2023 17:23:21] <blankpage[m]> I agree near enough 99% with Ukoe's linked comment. The heuristic of "user uses app which needs tx_extra" will get weaker once there are more "apps" using this feature.`
`[04-05-2023 17:23:41] <UkoeHB> jeffro256[m]: the point of having 1 bit distinction is the two 'puddles' will be very large`
`[04-05-2023 17:25:47] <jeffro256[m]> If the two puddles are of equal size, we are halving the effective ring size. If one of the pools is much larger than the other, then one of the puddles gets screwed over incredibly hard`
`[04-05-2023 17:26:37] <rbrunner> Halving the ring size? The two puddles won't only transact within themselves, one would think`
`[04-05-2023 17:26:49] <UkoeHB> > If the two puddles are of equal size, we are halving the effective ring size.`
`[04-05-2023 17:26:49] <UkoeHB> it's not that dramatic, there is only an analytical bias that may be stronger/weaker depending how much information you have`
`[04-05-2023 17:27:27] <Rucknium[m]> I think the effective ring size would only be halved if the recipient of the tx knew what kind of "user" they were dealing with, always. O if an external observer somehow knew.`
`[04-05-2023 17:27:54] <jeffro256[m]> Yes,  but if you make the assumption that users with tx_extra interact with those who do, and vice versa, the effective ring size is half unles you do decoy selection for only outputs in transaction which matching tx_extra`
`[04-05-2023 17:28:48] <rbrunner> And there, with that assumption, I have my doubts whether it's realistic`
`[04-05-2023 17:28:52] <UkoeHB> I don't think that's a reasonable assumption`
`[04-05-2023 17:29:21] <ofrnxmr[m]> regukar spends wouldnt use it`
`[04-05-2023 17:29:23] <jeffro256[m]> IRL the huerustic probably won’t be that strong , but we’re opening ourselves up to that possibility if we allow the field to be optional`
`[04-05-2023 17:29:28] <tevador> I we think the portion of transactions using tx_extra will be significant, we should make it mandatory instead. The space savings argument becomes much weaker then.`
`[04-05-2023 17:29:44] <ofrnxmr[m]> only apps etc would`
`[04-05-2023 17:29:55] <Rucknium[m]> If a user gets their XMR from a DEX that uses tx_extra and then spends it like normal to a merchant (not using tx_extra), then the assumption would be incorrect`
`[04-05-2023 17:30:24] <UkoeHB> tevador: it would be easy enough to switch to mandatory`
`[04-05-2023 17:30:48] <ofrnxmr[m]> a merchant recieving the funds knows to exckude txextra (sorry for bad typing)`
`[04-05-2023 17:31:14] <UkoeHB> and unconstrained -> optional -> mandatory (-> removed) would be the conservative development path`
`[04-05-2023 17:31:31] <ofrnxmr[m]> id skip optional`
`[04-05-2023 17:31:37] <rbrunner> That's also not the "faultline" of the community, it's question about a detail. The main question still is "remove" versus "keep in some form". We are stuck there.`
`[04-05-2023 17:32:08] <jeffro256[m]> Rucknium[m]: Right it wouldn’t be so cut and dry in real life but why allow it ?`
`[04-05-2023 17:32:09] <ofrnxmr[m]> (i mean, if were talking abot hard forks. optional right now isnt ideal either)`
`[04-05-2023 17:33:37] <jeffro256[m]> jeffro256[m]: It’s just simply worse for privacy by a large margin which is why we’re discussing tx_extra in the first place `
`[04-05-2023 17:35:00] <tevador> It seems that nobody is arguing strongly for removal today.`
`[04-05-2023 17:35:11] <Alex|LocalMonero> I am`
`[04-05-2023 17:35:20] <Alex|LocalMonero> Ofrn is`
`[04-05-2023 17:35:26] <ofrnxmr[m]> rbrunner - remove is just an extension of 255 limit. need to start with relocating stuff furst`
`[04-05-2023 17:35:29] <ofrnxmr[m]> i sm as well`
`[04-05-2023 17:35:30] <Alex|LocalMonero> Oh, sorry, you meant like today today.`
`[04-05-2023 17:35:55] <Alex|LocalMonero> No yeah, post-Seraphis removal is what I mean`
`[04-05-2023 17:36:17] <rbrunner> Yes, of course. I claim that we are (almost) all talking post seraphis hardfork anyway`
`[04-05-2023 17:36:29] <tevador> I meant today as in in this meeting.`
`[04-05-2023 17:36:35] <ofrnxmr[m]> i dont mind sooner :)`
`[04-05-2023 17:36:54] <Lyza> post seraphis hardfork, or simply don't include it in seraphis?`
`[04-05-2023 17:37:01] <ofrnxmr[m]> yes sir tevador. technical difgiculties or id say more`
`[04-05-2023 17:37:03] <plowsof11> v0.18.2.2 is tagged / to be released when binaryFate does the 'things'`
`[04-05-2023 17:37:29] <rbrunner> Yes, and people who want to keep even want to keep tx_extra with everything else relocated, just to avoid misunderstandings`
`[04-05-2023 17:38:46] <rbrunner> For what it's worth, I was once reading when sech1 seemed to explain that they changed their opinion, from "remove" to "keep" ...`
`[04-05-2023 17:39:35] <ofrnxmr[m]> tevador, are you in the party of standarizing outputs? any thiughts on inputs?`
`[04-05-2023 17:39:39] <rbrunner> Of course the proposal that is on the table, keep with a quite small size limit and a strong push toward encryption`
`[04-05-2023 17:40:13] <ofrnxmr[m]> id just add the return address fuekd, encryot it with destination address, maje it a dummy if not enabked`
`[04-05-2023 17:40:56] <rbrunner> You mean something like allowing only strictly 2 outputs?`
`[04-05-2023 17:41:07] <ofrnxmr[m]> yes sir`
`[04-05-2023 17:41:22] <ofrnxmr[m]> or 2 and 16`
`[04-05-2023 17:41:27] <rbrunner> That's ... something else :)`
`[04-05-2023 17:41:46] <ofrnxmr[m]> largeky the sane topic of bad decits`
`[04-05-2023 17:41:54] <ofrnxmr[m]> decoys`
`[04-05-2023 17:42:27] <rbrunner> Yes, but adding this to the already difficult and mostly stuck tx_extra keep versus remove discussion probably does not make things easier, no?`
`[04-05-2023 17:42:34] <Alex|LocalMonero> I believe that keeping tx_extra is signaling that arbitrary data injection has a stable standardized place on the Monero blockchain that is open and efficient. I believe that this is counter-productive towards Monero's goals. I believe that if arbitrary data is to be stored on the chain it should look just like any other tx data, meaning that only if a party chooses to reveal their keys may privacy be harmed, just like`
`[04-05-2023 17:42:34] <Alex|LocalMonero> with normal txs.`
`[04-05-2023 17:42:43] <ofrnxmr[m]> it does imo`
`[04-05-2023 17:43:09] <rbrunner> That may bloom into some new argument?`
`[04-05-2023 17:43:14] <Alex|LocalMonero> I also believe that arbitrary data storage on the XMR chain should be disincentivized to the greatest practical extent.`
`[04-05-2023 17:43:57] <sech1> arbitrary data can be stored in outputs, ~30 bytes per output and it's impossible to stop it`
`[04-05-2023 17:44:11] <rbrunner> Because, after all, that's an important point: What is *new*?`
`[04-05-2023 17:44:26] <ofrnxmr[m]> but steg doesnt stand out `
`[04-05-2023 17:44:31] <Alex|LocalMonero> sech1: I understand, but it's better if it blends in with the crowd`
`[04-05-2023 17:44:34] <sech1> which is why fixed small tx_extra is better than forcing arbitrary data into outputs`
`[04-05-2023 17:44:51] <Alex|LocalMonero> Nobody is forcing anyone to use outputs, people can use CLSAG too`
`[04-05-2023 17:44:51] <ofrnxmr[m]> and return address field + small msg is what thirchain or serai need`
`[04-05-2023 17:45:12] <ofrnxmr[m]> so.. they just beed anothey dummy change address`
`[04-05-2023 17:45:18] <rbrunner> CLSAG after Seraphis?`
`[04-05-2023 17:45:28] <ofrnxmr[m]> afaict`
`[04-05-2023 17:45:28] <Alex|LocalMonero> And keep in mind, sech1 , that there is little business case to develop applications around an unstable API.`
`[04-05-2023 17:45:53] <politicalweasel[> would the return address be one per tx or one per output?`
`[04-05-2023 17:45:56] <Alex|LocalMonero> If you want to make a stable arbitrary data API you are signalling that aribitrary data is welcome on the chain.`
`[04-05-2023 17:46:29] <Alex|LocalMonero> developers are now welcome to write arbitrary data and create an application layer and soft forks.`
`[04-05-2023 17:46:41] <Alex|LocalMonero> This will harm fungibility and privacy.`
`[04-05-2023 17:46:47] <ofrnxmr[m]> politicalweasel[: standarize to 2 out and question is answered`
`[04-05-2023 17:46:48] <sech1> If it stays uniform (fixed size and encrypted), it doesn't hurt privacy`
`[04-05-2023 17:47:48] <Rucknium[m]> AFAIK, putting data in output public keys does not blend in. You can put plaintext data there that is easy to detect....with your eyes, for example.`
`[04-05-2023 17:48:48] <Alex|LocalMonero> sech1: 1. there's no way to ensure encryption `
`[04-05-2023 17:48:48] <Alex|LocalMonero> 2. there's no way to prevent people from softforking that way `
`[04-05-2023 17:48:49] <Alex|LocalMonero> 3. you are imposing a storage and tx fee burden on the most users for the benefit of the application layer and soft forkers; you're practically disincentivizing people from *not* utilizing tx_extra since they pay the fee anyway`
`[04-05-2023 17:48:57] <UkoeHB> I am going to implement tx_extra pruning + optional encrypted field in the seraphis library as a temporary solution. These changes can be considered incremental improvement over the current library. Future incremental changes are still on the table.`
`[04-05-2023 17:49:54] <Rucknium[m]> For example, the first output public keys of this tx is all zeros: https://xmrchain.net/search?value=35ccad6e5f36a4320d1296ecb02ee34ce1591096658f236915943d2e55e43007`
`[04-05-2023 17:50:09] <sech1> Alex|LocalMonero There are statistical randomness tests. We can tune them to be very sensitive to non-random data. Even if they give false positives on 10% of true random data, wallet can regenerate it until the test passes.`
`[04-05-2023 17:50:09] <ofrnxmr[m]> what does txextra in seraphis cyrrebtky look like?`
`[04-05-2023 17:50:21] <UkoeHB> ofrnxmr[m]: same as today except TLV is enforced`
`[04-05-2023 17:50:30] <ofrnxmr[m]> ok`
`[04-05-2023 17:50:46] <rbrunner> And all standard stuff moved out, of course`
`[04-05-2023 17:50:58] <rbrunner> So empty as default, I guess`
`[04-05-2023 17:51:02] <hbs[m]> Has a study on uniqueness of output public keys been done before?`
`[04-05-2023 17:51:54] <tevador> AFAIK yes. There are many duplicates.`
`[04-05-2023 17:52:12] <Rucknium[m]> hbs: AFAIK, you generally will not have a collision unless it is deliberate.`
`[04-05-2023 17:52:20] <Alex|LocalMonero> sech1: Why are we bending over backwards to accomodate arbitrary data injectors? Why do they get a pass unlike ASIC manufactureres who used to be just as inevitable? Make arbtrary data unstable, inefficient, costly, and ideally indistinguishable from other data. Wouldn't you agree that this is the best solution`
`[04-05-2023 17:52:34] <ofrnxmr[m]> cuz its easier`
`[04-05-2023 17:52:36] <sech1> Because outputs`
`[04-05-2023 17:52:37] <politicalweasel[> Return addresses + stealth address + encrypted amounts field + ecdh key would likely be enough for at least 128 bytes of arbitrary data`
`[04-05-2023 17:52:39] <politicalweasel[> jsut saying`
`[04-05-2023 17:52:45] <UkoeHB> sech1 with seraphis it would be 30 + 18 + 8 + 32 bytes per output (Ko, encrypted addr tag, encoded amount, enote ephemeral pubkey)`
`[04-05-2023 17:52:51] <sech1> Tell me how to prevent stuffing arbitrary data into outputs and I'll change my opinion`
`[04-05-2023 17:53:04] <ofrnxmr[m]> politicalweasel[: which is fine if its akso a user feature`
`[04-05-2023 17:53:10] <Rucknium[m]> Deliberate cases could be an attempt to exploit the "burning bug" against a naive victim and victim's naive software`
`[04-05-2023 17:54:11] <rbrunner> "Why are we bending over backwards" That's a funny description of what we do.`
`[04-05-2023 17:55:04] <UkoeHB> we are approaching the hour, are there any last-minute questions or comments on other topics?`
`[04-05-2023 17:55:12] <Alex|LocalMonero> sech1: 1. outputs are not going away just cuz we add tx_extra. Malicious actors can still exploit it, even non-malicious ones might prefer to use outputs if you put a low enough limit on the size of tx_extra. You would have a case if tx_extra closed the outputs exploit, but it doesn't, it just adds another risk to fungibility`
`[04-05-2023 17:55:12] <Alex|LocalMonero> 2. well-intentioned devs can steg into CLSAG for now; as for post-seraphis, we'll have to see what other steg methods might be available`
`[04-05-2023 17:55:12] <Alex|LocalMonero> 3. the honest subset of arbitrary data injectors are a marginal minority and do not at the moment pose a risk for the chain. if/when they do the question can be revisited, not the other way around`
`[04-05-2023 17:56:25] <ofrnxmr[m]> koe, just that i thinj standarizing in/out might be wirth more duscussion alongside coinbase and txextra `
`[04-05-2023 17:56:28] <ofrnxmr[m]> ty`
`[04-05-2023 17:57:05] <Alex|LocalMonero> there is a snowball effect: if you create a stable arbitrary data API you attract more people to rely on arbitrary data injection which will create more risk for output exploitation by honest actors. By disincentivizing arbitrary data injection, refusing to signal a stable API, you also minimize honest actor output exploit risks as well`
`[04-05-2023 17:58:21] <UkoeHB> protocol instability is the opposite of what want to aim for`
`[04-05-2023 17:58:39] <Alex|LocalMonero> For arbitrary data injectors? It should be, I believe.`
`[04-05-2023 17:59:16] <rbrunner> We could abbreviate that to "ADIs" :)`
`[04-05-2023 17:59:24] <Alex|LocalMonero> good idea`
`[04-05-2023 18:00:29] <UkoeHB> that's the end of the hour, thanks for attending everyone; it may be a while before I implement those tx_extra changes, I'll keep the channel updated as usual`

# Action History
- Created by: Rucknium | 2023-04-04T16:29:58+00:00
- Closed at: 2023-04-11T16:07:02+00:00
