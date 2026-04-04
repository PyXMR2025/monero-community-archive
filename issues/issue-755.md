---
title: Monero Research Lab Meeting - Wed 16 November 2022
source_url: https://github.com/monero-project/meta/issues/755
author: Rucknium
assignees: []
labels: []
created_at: '2022-11-14T21:17:31+00:00'
updated_at: '2022-11-22T16:00:17+00:00'
type: issue
status: closed
closed_at: '2022-11-22T16:00:17+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2.  Discuss [Jamtis address checksums](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#64-checksum).

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

5. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#750 

# Discussion History
## UkoeHB | 2022-11-16T17:54:24+00:00
`[11-16-2022 17:00:39] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/755`
`[11-16-2022 17:00:39] <UkoeHB> 1. greetings`
`[11-16-2022 17:00:39] <UkoeHB> hello`
`[11-16-2022 17:00:42] <vtnerd> hi`
`[11-16-2022 17:00:56] <rehrar> hi`
`[11-16-2022 17:01:13] <M0xtraffikriot[m> hi!`
`[11-16-2022 17:01:14] <rbrunner> Hello`
`[11-16-2022 17:01:54] <Rucknium[m]> Hi`
`[11-16-2022 17:01:57] <UkoeHB> Rucknium[m]: https://eprint.iacr.org/2020/735`
`[11-16-2022 17:03:04] <Rucknium[m]> UkoeHB: That's the version with the error in the appendix. We can return to that later.`
`[11-16-2022 17:03:29] <UkoeHB> that's the version with an appendix lol`
`[11-16-2022 17:03:52] <UkoeHB> 2. updates, what's everyone working on?`
`[11-16-2022 17:04:36] <vtnerd> my serialization changes/branch have been _basically_ completed, including replacement of the different ZeroMQ json implementation`
`[11-16-2022 17:04:50] <vtnerd> only a few functional_rpc tests remain before issuing a pr`
`[11-16-2022 17:06:06] <UkoeHB> me: have been sick, otherwise working on finishing touches for multisig + refactoring the library into multiple directories (half done); after that is just the coinbase tx type`
`[11-16-2022 17:06:18] <vtnerd> https://github.com/vtnerd/monero/tree/replace_p2p_serialization2 is the locaiton`
`[11-16-2022 17:06:24] <Rucknium[m]> me: Familiarizing myself with previous BulletProofs+ audit process. I asked Diego Salazar from Cypherstack to be available for this meeting so we can discuss details of the BP++ audit CCS.`
`[11-16-2022 17:06:34] <rehrar> das me`
`[11-16-2022 17:07:30] <vtnerd> so it looks like someone audited the paper, and you are preparing for an audit of the yet-to-be-written bp++? or perhaps somene is writing that already`
`[11-16-2022 17:07:45] <UkoeHB> vtnerd: https://github.com/monero-project/research-lab/issues/101`
`[11-16-2022 17:08:35] <vtnerd> I ah yeah we definitely discussed that, and I forgot initially`
`[11-16-2022 17:08:58] <vtnerd> although Im a bit worried that we may need to re/write ? eh whatever it'll get done`
`[11-16-2022 17:09:09] <UkoeHB> rewrite the bp++ paper?`
`[11-16-2022 17:09:32] <vtnerd> no that mysterious implementation lol`
`[11-16-2022 17:09:35] <selsta> we will have to write the code ourselves`
`[11-16-2022 17:09:40] <UkoeHB> oh definitely`
`[11-16-2022 17:09:53] <vtnerd> yeah thats fine, there's a few people that can do it around`
`[11-16-2022 17:09:54] <UkoeHB> 3. let's move to discussion`
`[11-16-2022 17:10:24] <Rucknium[m]> We could perhaps reduce confusion by calling what CypherStack will do a "Peer review" rather than "audit".`
`[11-16-2022 17:10:38] <Rucknium[m]> Since they are not auditing any code at this point`
`[11-16-2022 17:10:48] <UkoeHB> part of the work requested from CypherStack https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/358 is a proof of concept`
`[11-16-2022 17:11:16] <Rucknium[m]> Yes but you cannot audit code you've written yourself`
`[11-16-2022 17:11:45] <rehrar> As far as I was aware, the PoC wasn't to be included, but rather was to be used more or less as a benchmarking tool since the other implementation can't be verified.`
`[11-16-2022 17:11:54] <plowsof> PoC not yet discussed/finalised/confirmed, only 1a) is covered in that ccs* `
`[11-16-2022 17:12:12] <UkoeHB> ok then take it off the ccs if it's not included...`
`[11-16-2022 17:12:13] <rehrar> So we would be doing two pieces of work. A peer review of the paper, and a PoC of the code for benchmarking purposes and comparison to BP+ so see if it's worth inclusion.`
`[11-16-2022 17:12:22] <UkoeHB> now I'm frustrated`
`[11-16-2022 17:12:43] <rbrunner> "with only (1a) being set in stone / to be achieved by this C" from the CCS`
`[11-16-2022 17:13:43] <rehrar> We're obviously happy to do the PoC as well, pending the results of the peer review.`
`[11-16-2022 17:13:56] <rbrunner> Yeah, maybe put that proposed total timeline somewhere else, so that the CCS text is single-topic without any room for doubt`
`[11-16-2022 17:14:02] <UkoeHB> rehrar: would that be an additional funding round?`
`[11-16-2022 17:14:27] <rehrar> yes`
`[11-16-2022 17:14:33] <plowsof> got it rbrunner `
`[11-16-2022 17:15:09] <plowsof> we can't raise funds for a proof of concept until the paper is audited? or am i totlaly off base here`
`[11-16-2022 17:15:45] <selsta> I'm not convinced how useful a PoC is, unless it's required as a template for the real implementation.`
`[11-16-2022 17:15:56] <UkoeHB> selsta: yes that's why I requested it`
`[11-16-2022 17:15:56] <rbrunner> Well, maybe the whole BP++ comes crashing down in that peer review, worst case`
`[11-16-2022 17:15:57] <rehrar> I mean, in theory both can be raised at once, and if something is found to be terribly wrong with the paper (unlikely), then we just don't do the PoC and the money goes to the GF.`
`[11-16-2022 17:15:57] <selsta> The author has a proof of concept on git already.`
`[11-16-2022 17:16:58] <plowsof> then we need to foamlise the scope of this PoC because there was 2 things going on - simply 'benchmarking in c++' (instead of haskell) and then creating something thats 'actually' usable for monero libraries`
`[11-16-2022 17:17:05] <plowsof> formalise*`
`[11-16-2022 17:19:04] <UkoeHB> selsta: ok if someone who can read haskell or whatever that is wants to translate it to python/c++...`
`[11-16-2022 17:19:16] <rbrunner> Why Haskell? What is now in Haskell? The author's PoC?`
`[11-16-2022 17:19:40] <UkoeHB> https://github.com/Liam-Eagen/BulletproofsPP`
`[11-16-2022 17:19:53] <vtnerd> lol I've always secretly loved haskell ... Im not sure if signing myself up for this is a good idea given other stuff Im doing`
`[11-16-2022 17:19:59] <vtnerd> but maybe this is more important`
`[11-16-2022 17:20:10] <rbrunner> Oh wow`
`[11-16-2022 17:20:16] <vtnerd> and I havent studied haskell in depth, just like what they are trying to do`
`[11-16-2022 17:21:27] <vtnerd> the tasks Im trying to do are the p2p serialization and p2p e2e encryption`
`[11-16-2022 17:21:37] <vtnerd> and few other side things, but those are the most relevant to monero`
`[11-16-2022 17:21:48] <UkoeHB> vtnerd: what timeline do you have for those p2p things?`
`[11-16-2022 17:21:51] <vtnerd> *the above is the most relevant to this discussion`
`[11-16-2022 17:21:55] <selsta> p2p serialization is the one that's almost finished?`
`[11-16-2022 17:22:17] <rbrunner> This goes over my head, but the "P" in "PoC" stands for "proof", and maybe we don't need any more proof and could directly go to the implementation in Monero codebase`
`[11-16-2022 17:22:18] <vtnerd> yes. and the p2p encryption has some code but I stopped dead in my tracks because of the tracking issue with the initial proposal`
`[11-16-2022 17:22:35] <UkoeHB> a big advantage of getting the code done in-house is we can ask cypherstack for a code audit in the future`
`[11-16-2022 17:22:46] <vtnerd> I've actually got to re-write my proposal on that, and follow closer to what bitcoin is doing (I think), but theres a few other details I've got to work through`
`[11-16-2022 17:23:20] <vtnerd> having a static-key is nice for a few reasons, but it makes the node trackable in a bunch of ways`
`[11-16-2022 17:23:37] <Rucknium[m]> AFAIK, we're not in a rush here on BP++. We can take things step by step. Probably the only downside to separating the peer review and PoC into two CCS proposals is asking the community twice to fund something.`
`[11-16-2022 17:23:52] <vtnerd> so Im still mulling over whether a --secret-p2p-key opti-in is a good idea `
`[11-16-2022 17:24:12] <vtnerd> yeah bp++ seems like it would be more on the seraphis timeline ?`
`[11-16-2022 17:24:34] <rbrunner> We estimated Seraphis 2 years out, or longer`
`[11-16-2022 17:24:47] <vtnerd> like thats going to be a major fork anyway, and bp++ in the current mlsag/ringct setup is going to be annoying`
`[11-16-2022 17:25:14] <rbrunner> More annoying than BP+ then?`
`[11-16-2022 17:25:16] <vtnerd> I mean it would enable us to bump ringct further, but then we have maintenance on a bp++ w/mslag to think about`
`[11-16-2022 17:25:23] <selsta> is it different from going from bp to bp+?`
`[11-16-2022 17:25:43] <vtnerd> no its just that bp++ with mlsag adds additional technical debt that we have to maintain in perpuitity for the project`
`[11-16-2022 17:25:51] <UkoeHB> the sooner BP++ is done, the sooner resources tied to that project can be used elsewhere`
`[11-16-2022 17:26:27] <vtnerd> hmm. well I'll let the others decide whether is higher priority then`
`[11-16-2022 17:26:29] <UkoeHB> plus the longer it takes to integrate, the less available I may end up being`
`[11-16-2022 17:26:49] <vtnerd> it sounds like bp++ is high priority then`
`[11-16-2022 17:26:56] <rbrunner> Well, otherwise we have a larger-than-would-have-been blockchain for perpetuity, no?`
`[11-16-2022 17:27:13] <UkoeHB> yes, for me it's high priority`
`[11-16-2022 17:27:17] <vtnerd> yeah theres that angle too.`
`[11-16-2022 17:27:46] <vtnerd> ok, sounds like we need bp++ immediately then, if theres a haskell implementation Ill do a straight port`
`[11-16-2022 17:27:51] <rbrunner> 2 years without a hardfork are booring anyway :)`
`[11-16-2022 17:27:53] <plowsof> the 'peer review' is promised to be completed in 'around' 12 ~ days `
`[11-16-2022 17:28:20] <UkoeHB> vtnerd: the BP++ author's proof of concept is here https://github.com/Liam-Eagen/BulletproofsPP`
`[11-16-2022 17:29:09] <vtnerd> one complication with perf comparisons is that the existing bp+ could have speed perf improvements from what I recall`
`[11-16-2022 17:29:35] <vtnerd> so if I do a port, then I'll probably simateulounyl have to improve the old two implementations to get a better compre`
`[11-16-2022 17:29:39] <UkoeHB> however I'm thinking the existing BP/BP+ files have code duplication that can be pulled into a common library and also used with BP++ (probably)`
`[11-16-2022 17:30:12] <UkoeHB> vtnerd: I don't think there are any perf improvements available, at least in terms of crypto ops`
`[11-16-2022 17:31:28] <plowsof> title changed to Bp++ Peer Review, timeline removed. 2 seperate funding rounds for Peer Review and then PoC OR attempt 2 in 1 - if 2 in 1 is voted on - then we need koe to formally right the scope of the PoC `
`[11-16-2022 17:31:38] <vtnerd> theres some small C++ stuff, like copies in a few areas, etc. Or at least that was my first impression`
`[11-16-2022 17:32:33] <selsta> plowsof: for now I think we should only fund a paper audit / peer review`
`[11-16-2022 17:34:13] <plowsof> it will take 'around' 12 days. and the other alternative for the review who got back to me are unavailable until Q2, CypherStack can start 'soon' / "next month"  `
`[11-16-2022 17:35:28] <vtnerd> Ukoehb: I'm only trying to get realistic numbers on bp++. presumably its guaranteed faster to due to algo analysis, etc., so I'll think about that as time permits`
`[11-16-2022 17:35:58] <rbrunner> Q2, as in Q2, 2023? So many things to audit ...`
`[11-16-2022 17:36:04] <Rucknium[m]> I support plowsof 's changes to the CCS. I also want to see more detail on exactly which statements and math logic will be checked. The BP++ does not have the familiar "Theorem: Proof" format, so it's not entirely clear what needs to be checked.`
`[11-16-2022 17:36:06] <plowsof> yes q2 2023`
`[11-16-2022 17:36:14] <UkoeHB> vtnerd: ok sounds great to me, glad to have your help :)`
`[11-16-2022 17:36:21] <vtnerd> Im looking at this haskell for the first time, this language is pretty wild lol. but it seems like something I should be able to pick up`
`[11-16-2022 17:36:25] <vtnerd> Ill notify immediately if I cannot`
`[11-16-2022 17:36:43] <Rucknium[m]> Thanks, vtnerd `
`[11-16-2022 17:36:53] <rbrunner> Reading is always easer than writing in a programming language :)`
`[11-16-2022 17:37:25] <vtnerd> hmmm. maybe, dunno about that`
`[11-16-2022 17:37:43] <plowsof> koe thoughts? feeling frustrated still? happy? - we still have time to play with `
`[11-16-2022 17:37:58] <rehrar> Rucknium[m] Which statements and math logic do you all want checked?`
`[11-16-2022 17:38:10] <UkoeHB> plowsof: yes this is fine, let's move forward with CCS for cypherstack to do paper audit`
`[11-16-2022 17:39:16] <rehrar> We plan to touch on the soundness, completeness, and zero knowledge portions of the paper, as touched on in the paper. We also plan to look at efficiency, aggregation, batching, and MPC compatibility.`
`[11-16-2022 17:39:20] <Rucknium[m]> rehrar: I'm hoping a cryptographer can answer that. Looks like there are certain statements about soundness, etc. under certain (standard) assumptions in the body of the paper, and then proofs in the appendix. I'm not sure what needs to be checked.`
`[11-16-2022 17:39:21] <UkoeHB> rehrar: presumably the BP++ paper should satisfy the same security requirements as BP and BP+`
`[11-16-2022 17:40:17] <Rucknium[m]> I want us to be specific in our understanding so there are no surprises down the road. I'm sure you will do a great job.`
`[11-16-2022 17:40:59] <rehrar> UkoeHB that's probably a more realistic standard. Because otherwise we'd be responsible for deciding what needs to be checked, and then checking it.`
`[11-16-2022 17:41:41] <rehrar> Which is doable...just a little weird. Us specifying our own work scope.`
`[11-16-2022 17:42:09] <rehrar> Typically it's more like the client would provide the preprint and say "please check X, Y, Z on this" and we would, if that makes sense.`
`[11-16-2022 17:42:35] <UkoeHB> yes well :)`
`[11-16-2022 17:42:44] <rehrar> But yes, we do have a good understanding of Monero, and BP/BP+, so ensuring it meets the same security requirements as those seems like a solid scope`
`[11-16-2022 17:43:42] <Rucknium[m]> "Bulletproofs++ use essentially the same model as Bulletproofs(+). The only important differences are either superficial, i.e. using additive vs multiplicative notation for the group operation or the manner in which vectors are decomposed, or in the case of the reciprocal argument a weakening from perfect completeness to statistical completeness."`
`[11-16-2022 17:43:46] <Rucknium[m]> ^ here is the claim from the paper`
`[11-16-2022 17:44:13] <UkoeHB> One thing to watch out for is novel cryptographic assumptions. Those can be hazardous`
`[11-16-2022 17:44:28] <rehrar> Right. So making sure it fits neatly and completely into the place that BP+ currently sits would be a good scope, imo. Disagreements?`
`[11-16-2022 17:45:20] <ofrnxmr[m]> +1`
`[11-16-2022 17:45:24] <UkoeHB> none from me, thanks rehrar `
`[11-16-2022 17:45:53] <rehrar> Cool. We wouldn't be able to start until early December. Would that be an issue?`
`[11-16-2022 17:46:02] <UkoeHB> that should be fine`
`[11-16-2022 17:46:18] <vtnerd> makes sense to me rehrar`
`[11-16-2022 17:47:15] <rehrar> Cool deal. If no more questions for me, then I'm off.`
`[11-16-2022 17:48:09] <Rucknium[m]> To be clear, this includes checking the correctness of proofs when "fit[ting] neatly and completely into the place that BP+ currently sits" relies on any proofs in the paper, correct?`
`[11-16-2022 17:48:33] <rehrar> yes`
`[11-16-2022 17:49:39] <Rucknium[m]> Great. Thank you`
`[11-16-2022 17:50:06] <UkoeHB> ok, any other last minute topics we should cover today?`
`[11-16-2022 17:51:05] <UkoeHB> oh btw rehrar should we use this old CCS to fund the new one? https://ccs.getmonero.org/proposals/cypherstack-sarang-triptych-research.html`
`[11-16-2022 17:51:27] <rehrar> I have zero control over how the funds on the old CCS are used.`
`[11-16-2022 17:51:33] <rehrar> That seems like it'd be a question for core.`
`[11-16-2022 17:51:41] <plowsof> they where/yet to be donated to the general fund`
`[11-16-2022 17:51:59] <UkoeHB> ah`
`[11-16-2022 17:52:05] <plowsof> seems a sensible request to go to this one , ill ask `
`[11-16-2022 17:52:07] <rehrar> Until the money is in my hands, it's core stewarded money`
`[11-16-2022 17:52:19] <rehrar> after that it's my money >:)`
`[11-16-2022 17:53:35] <UkoeHB> ok seems like we can wrap it up here, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2022-11-14T21:17:31+00:00
- Closed at: 2022-11-22T16:00:17+00:00
