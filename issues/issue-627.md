---
title: Monero Research Lab Meeting - Wed 17 November 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/627
author: Rucknium
assignees: []
labels: []
created_at: '2021-11-16T06:21:36+00:00'
updated_at: '2021-11-23T06:02:56+00:00'
type: issue
status: closed
closed_at: '2021-11-23T06:02:56+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. A list of open research questions, their priority, and anticipated difficulty. Similar to [what Grin has](https://grin.mw/open-research-problems).

3. "Seeing a bug in Aeon transactions where multiple inputs in one transaction use the same output. " https://github.com/monero-project/monero/pull/8047

4. Cryptographic performance benchmarks https://github.com/Rucknium/misc-research/tree/main/Monero-Cryptography-Benchmarks

5. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

6. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88)) @j-berman @Rucknium

7. [The Science of Blockchain Conference 2022 Jan 24-26](https://cbr.stanford.edu/sbc22/#cfp). Submission deadline: November 23, 2021 11:59pm PST

8. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

9. Rucknium's OSPEAD discussion ([CCS proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/255) , Reddit discussion [1](https://www.reddit.com/r/Monero/comments/py8ub3/ccs_proposal_ospead_fortifying_monero_against/) & [2](https://www.reddit.com/r/Monero/comments/pyopq0/the_mathematical_nonsense_of_a_possible/)

10. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

11. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

12. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

13. Any other business

14. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#626 

# Discussion History
## UkoeHB | 2021-11-17T19:46:25+00:00
```
[11-17-2021 17:00:51] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/627
[11-17-2021 17:00:51] <UkoeHB> 1. greetings
[11-17-2021 17:00:51] <UkoeHB> hello
[11-17-2021 17:01:07] <one-horse-wagon[> Hello.
[11-17-2021 17:01:11] <rbrunner> Hi there
[11-17-2021 17:01:17] <Rucknium[m]> disclosure-bot-x: Please define conflict of interest in this context
[11-17-2021 17:01:31] <carrington[m]> Hi hi hi
[11-17-2021 17:01:33] <Rucknium[m]> Hi
[11-17-2021 17:01:52] <UkoeHB> It's a bot
[11-17-2021 17:02:16] <one-horse-wagon[> Rucknium.  Did you ever post Document A anywhere so I could read it?
[11-17-2021 17:02:37] <Rucknium[m]> I can send you the working draft
[11-17-2021 17:02:49] <Rucknium[m]> Do you want it now?
[11-17-2021 17:03:29] <jberman[m]> hello :)
[11-17-2021 17:03:49] <UkoeHB> Let's do updates briefly, then get into the agenda
[11-17-2021 17:03:49] <UkoeHB> 2. updates - what has everyone been working on lately?
[11-17-2021 17:04:08] <one-horse-wagon[> Rucknium[m]: Sure
[11-17-2021 17:05:43] <jberman[m]> Finishing up requested changes to the view tag PR (ty to UkoeHB for the review), then will be getting back to decoy selection work
[11-17-2021 17:06:02] <Rucknium[m]> My OSPEAD CCS proposal was funded (Thank you everyone!). I ran some analysis on the blockchain data for PR#8047. Working on Document A and incorporating feedback.
[11-17-2021 17:07:16] <UkoeHB> me: I made two MRL issues to discuss the design of a potential seraphis implementation. 1) PoC performance results ( https://github.com/monero-project/research-lab/issues/91 ), 2) Seraphis address schemes ( https://github.com/monero-project/research-lab/issues/92 ). Last week I found and fixed a rare crypto bug ( https://github.com/monero-project/monero/pull/8052 ). My next steps are integrating performance results into the 
[11-17-2021 17:07:16] <UkoeHB> Seraphis paper, then integrating coinstudent2048['s security modeling work into the Seraphis paper.
[11-17-2021 17:09:16] <Rucknium[m]> one-horse-wagon: Sent. If anyone else wants the draft of Document A, let me know. I'm just not posting it publicly since it's not good to have old versions floating around publicly.
[11-17-2021 17:10:55] <carrington[m]> I'm happy to wait unless you need feedback before pub. No shortage of other things here for me to catch up on!
[11-17-2021 17:12:08] <Rucknium[m]> carrington: I mean, it could be nice to have feedback. Mainly, it needs to be more accessible to laypeople. It sort of needs an introduction. 
[11-17-2021 17:12:27] <Rucknium[m]> You are not obligated to give feedback just because you receive it.
[11-17-2021 17:13:04] <carrington[m]> Well in that case sling it over and hopefully I'll be able to give some meaningful feedback in a few days
[11-17-2021 17:13:35] <UkoeHB> wfaressuissia: are you available to give an update on your multisig PR? It is a blocker for people planning to use multisig, so knowing what timeline to expect can be very helpful.
[11-17-2021 17:14:18] <rbrunner> Wait, is there a second multisig PR on the way, beside yours, UkoeHB?
[11-17-2021 17:14:45] <Rucknium[m]> carrington: Sent
[11-17-2021 17:16:03] <UkoeHB> rbrunner: yes, multisig is unusable until then. Maybe luigi1111 will make a statement ?
[11-17-2021 17:16:28] <rbrunner> You mean in the sense of "too risky", right?
[11-17-2021 17:16:33] <wfaressuissia> " It is a blocker for people planning to use multisig ..." soon
[11-17-2021 17:17:24] <rbrunner> I was asking myself whether it makes sense to test again your updated multisig code. So much changed that I would say my previous results are kind of invalid now.
[11-17-2021 17:17:40] <rbrunner> But maybe wait, and test with the second one on top?
[11-17-2021 17:17:49] <UkoeHB> Yeah, might as well wait.
[11-17-2021 17:19:30] <UkoeHB> wfaressuissia: ok well, sounds like it's closer than last time I asked lol
[11-17-2021 17:19:55] <UkoeHB> let's move on to agenda items; looks like a new one was added Rucknium[m] 
[11-17-2021 17:20:51] <Rucknium[m]> Yes. I think it would be great to put together a list of open research questions. Grin has this: https://grin.mw/open-research-problems
[11-17-2021 17:21:08] <wfaressuissia> " It is a blocker for people planning to use multisig, ..." what's the right place to discuss deeply how it will be used in practice ?
[11-17-2021 17:21:54] <Rucknium[m]> This would help us in a number of ways. First, it would help us determine priorities and maybe uncover low hanging fruit. The view tag idea comes to mind here.
[11-17-2021 17:22:35] <Rucknium[m]> It would help attract researchers, in general, since they would then know what the questions they could work on.
[11-17-2021 17:22:48] <carrington[m]> It seems like a good format for collecting what is presently scattered across github issues, papers, reddit posts and various websites.
[11-17-2021 17:22:55] <coinstudent2048[> Hi! Regarding open problems listing, I have some, but more "theoretical". What's the status of moneroresearch.wtf?
[11-17-2021 17:22:58] <Rucknium[m]> And if we have a more formal funding structure for MRL, they could serve as the basis for Requests For Propsals
[11-17-2021 17:22:59] <UkoeHB> wfaressuissia: I don't think there is a place right now (other than this channel). You could open an MRL github issue for longer-term discussions https://github.com/monero-project/research-lab/issues
[11-17-2021 17:23:13] <wfaressuissia> What's the performance difference (theoretical maximum, practical maximum, actual diff for wallet2 scanning) of view tag in practice ?
[11-17-2021 17:23:57] <wfaressuissia> That code is so "beautiful", there is non-zero chance that it's far from theoretical maximum of ~50% (?)
[11-17-2021 17:24:47] <Rucknium[m]> coinstudent2048[: Theoretical question are great to add. Status of moneroresearch.wtf is carrington was reaching out to spirobel  to work on it I think.
[11-17-2021 17:24:49] <wfaressuissia> "I don't think there is a place right now (other than this channel). " It makes sense to make usable for any market, not only haveno or something similar
[11-17-2021 17:25:05] <UkoeHB> I think the theoretical maximum is closer to 25%, since scalar mult key is so expensive compared to the operations you get to skip.
[11-17-2021 17:25:42] <wfaressuissia> "I think the theoretical maximum is closer to 25%" is it for asm from external/supercop or without ?
[11-17-2021 17:26:16] <UkoeHB> iirc it is the same with or without
[11-17-2021 17:27:18] <carrington[m]> I've had a pretty whacky IRL week so haven't made much progress on those ideas sadly. In the meantime I'm rereading ZtM2 and making notes
[11-17-2021 17:28:06] <UkoeHB> Ok, I don't think I did a direct comparison with 'unoptimized'. It is 25% using supercop.
[11-17-2021 17:29:32] <Rucknium[m]> Anyway, so it looks like coinstudent2048 has a small list of questions to contribute. I will make a MRL GitHub issue about it. I suppose I can host the working list on https://cryptpad.sethforprivacy.com/
[11-17-2021 17:30:47] <Rucknium[m]> Or maybe coinstudent2048 can make the MRL issue and start the CryptPad doc
[11-17-2021 17:30:49] <UkoeHB> > It makes sense to make usable for any market, not only haveno or something similar
[11-17-2021 17:30:49] <UkoeHB> Multisig has always been generic, although there is an address-generation optimization that really benefits uses of 2-of-3.
[11-17-2021 17:32:06] <wfaressuissia> I'm about end user API, current multisig related functions are crap and 1 instance of monero-wallet-rpc per 1 multisig wallet is a crap idea too
[11-17-2021 17:32:25] <carrington[m]> I was thinking that if we consider ZtM2 to be the protocol specification, it might make sense to organise  research/problems on the basis of the chapters of ZtM2 
[11-17-2021 17:32:29] <wfaressuissia> it's too heavy, there is a need for something more efficient
[11-17-2021 17:33:34] <UkoeHB> I think the issue is multisig tx builder code is heavily integrated with wallet2.
[11-17-2021 17:34:08] <UkoeHB> Along with all the labor of tracking outputs and recording state.
[11-17-2021 17:34:40] <wfaressuissia> The distance between ZtM2 and actual code isn't small and getting increased with time
[11-17-2021 17:35:37] <UkoeHB> carrington[m]: I wouldn't call ZtM2 a spec... but the organization might be useful. I'd also look at the Seraphis paper introduction for a sense of protocol structure.
[11-17-2021 17:37:23] <carrington[m]> Yes I should have said "nearest thing we have to a protocol spec". Points taken. Are any parts of ZtM2 badly outdated already? Or only after the next fork?
[11-17-2021 17:37:24] <Rucknium[m]> Oh, another thing that the list of open questions could be useful for is to tag articles on moneroresearch.wtf according to which questions they may address
[11-17-2021 17:38:43] <wfaressuissia> "I think the issue is multisig tx builder code is heavily integrated with wallet2." Everything is wallet2 is deeply integrated (due to short term ugly changes without any refactoring or redesign)
[11-17-2021 17:39:16] <wfaressuissia> * Everything in wallet2 ...
[11-17-2021 17:39:17] <UkoeHB> outdated: CLSAG is being used, fee/dynamic-block changes for next fork (https://github.com/monero-project/monero/pull/7819), BP+ for next fork, multisig chapter needs an update, a few minor details I can't remember
[11-17-2021 17:40:04] <rbrunner> Well, that's just progress. Of course ZtM2 is only a snapshot at a certain point in time. I fail to see anyhting special here.
[11-17-2021 17:40:14] <carrington[m]> Ah yes CLSAG. Thanks for the summary
[11-17-2021 17:42:27] <Rucknium[m]> Agenda item 7 is: The Science of Blockchain Conference 2022 Jan 24-26. Submission deadline: November 23, 2021 11:59pm PST
[11-17-2021 17:42:45] <Rucknium[m]> If we want to submit something to this, which I think we should, we need to do it very soon
[11-17-2021 17:43:08] <Rucknium[m]> Fingerprinting a Flood would be the obvious choice, as a work in progress
[11-17-2021 17:43:25] <UkoeHB> > Everything is wallet2 is deeply integrated (due to short term ugly changes without any refactoring or redesign)
[11-17-2021 17:43:26] <UkoeHB> With my Seraphis PoC I am trying to encapsulate as much tx protocol logic as possible, so wallet-level code just has to plug into component library APIs. Hopefully that gets us one step in the right direction.
[11-17-2021 17:44:49] <UkoeHB> Similarly, the multisig address PR pulled a lot of logic into the `multisig` component library.
[11-17-2021 17:44:56] <Rucknium[m]> What happened to wallet1? Was it lost in a boating accident?
[11-17-2021 17:45:19] <UkoeHB> Rucknium[m]: I suppose the authors of that paper would have to submit it.
[11-17-2021 17:46:08] <Rucknium[m]> I'm an author, so in theory I can submit. isthmus would be the best person to spearhead it, though.
[11-17-2021 17:48:54] <UkoeHB> Does anyone have any last-minute questions or things they want to discuss?
[11-17-2021 17:49:10] <Rucknium[m]> Should we discuss the Seraphis performance tests? I suppose my main comment is if there isn't a huge tradeoff, keeping the flavors that allow collaborative funding would be great.
[11-17-2021 17:49:50] <gingeropolous> which flavors? concise vs. whatever the other was?
[11-17-2021 17:49:51] <jberman[m]> <wfaressuissia[m]> ""I think the issue is multisig..." <- I was thinking of refactoring a bit of wallet2 during view tag stuff. It seems like we're continuously just going to add booleans for new features based on fork version (e.g. `use_rct`, `bulletproof`, `use_view_tags`), and pass the booleans from function to function
[11-17-2021 17:50:04] <luigi1111> UkoeHB: couldn't it be 50% if you tag the first pubkey instead of the correct one? 
[11-17-2021 17:50:04] <UkoeHB> The cost of collaborative funding is `32 + 96*(num_inputs - 1) bytes`.
[11-17-2021 17:50:12] <luigi1111> (or more) 
[11-17-2021 17:50:45] <UkoeHB> luigi1111: yeah it's 25% if you have 1:1 matching with outputs and txo pubkeys, there can be more if all outputs share a txo pubkey.
[11-17-2021 17:51:22] <luigi1111> hmm I don't get it
[11-17-2021 17:52:01] <luigi1111> not sharing pubkeys should make it faster in my version
[11-17-2021 17:52:02] <Rucknium[m]> UkoeHB: UkoeHB: Roughly, what's that in percentage terms? I know we haven't yet settled on a tx size yet.
[11-17-2021 17:52:27] <luigi1111> (same speed, faster as a % increase) 
[11-17-2021 17:53:45] <UkoeHB> The 25% comes from skipping `Ko - H(derivation,t)*G`. The remaining 75% is from computing `derivation = kv * R`. If a tx has one txo pubkey, then you only need to compute one `derivation` for the entire tx. The `Ko - H(derivation,t)*G` steps can be replaced with view-tag checks for all outputs. If you have one txo pubkey per output, then you have to compute `derivation_t` for each output - quite expensive.
[11-17-2021 17:55:46] <UkoeHB> Rucknium[m]: ~ 1-10% scaling with the number of inputs.
[11-17-2021 17:56:46] <Rucknium[m]> So a single input would be close to 1% larger tx size?
[11-17-2021 17:56:58] <UkoeHB> Yes
[11-17-2021 17:58:26] <UkoeHB> ~ 5% for a 2-in/2-out tx
[11-17-2021 17:58:26] <Rucknium[m]> Worth it, in my eyes. It is important that we have a breakdown of the tx characteristics of txs in the last year or so, in order to get a better sense of how your performance tests would play out in "production".
[11-17-2021 17:59:11] <Rucknium[m]> I can work on this with neptune 
[11-17-2021 17:59:26] <gingeropolous> what are we adding for 5%?
[11-17-2021 18:00:52] <UkoeHB> gingeropolous: the ability for multiple people to fund the same tx (provide inputs)
[11-17-2021 18:04:29] <Rucknium[m]> Noncustodial crowdfunding where donors can recover their XMR if the funding goal is not met.
[11-17-2021 18:06:12] <luigi1111> ukoe I get that, 25% seems the minimum increase
[11-17-2021 18:08:20] <luigi1111> <UkoeHB> gingeropolous: the ability for multiple people to fund the same tx (provide inputs) <= can't they do this now? 
[11-17-2021 18:09:41] <UkoeHB> not without interacting, collaborative funding allows 'independent' funding
[11-17-2021 18:09:45] <wfaressuissia> tx prefix hash is needed to derive signature challenge, that means set of signers should be known in advance
[11-17-2021 18:10:35] <UkoeHB> right ^
[11-17-2021 18:10:46] <wfaressuissia> key images for all inputs should be known in advance
[11-17-2021 18:10:53] <wfaressuissia> "... You could open an MRL github issue for longer-term discussions https://github.com/monero-project/research-lab/issues" I need at least 1 human who can dive deeply into problem. I don't see any value in comments from people with shallow knowledge of the problem.
[11-17-2021 18:10:54] <UkoeHB> Anyway, we are past the hour so I will call the meeting here. Thanks for attending everyone.
```

## UkoeHB | 2021-11-20T19:05:38+00:00
For the next agenda, can you add 'discuss requirements to get [the multisig PR](https://github.com/monero-project/monero/pull/7877) merged'?

## carrington1859 | 2021-11-20T21:58:28+00:00
@Rucknium  it might be good idea to include the following link in future meeting posts so that new users can easily join the Matrix channel.

https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web

# Action History
- Created by: Rucknium | 2021-11-16T06:21:36+00:00
- Closed at: 2021-11-23T06:02:56+00:00
