---
title: Monero Research Lab Meeting - Wed 01 March 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/803
author: Rucknium
assignees: []
labels: []
created_at: '2023-02-28T16:10:44+00:00'
updated_at: '2023-03-04T18:50:25+00:00'
type: issue
status: closed
closed_at: '2023-03-04T18:50:25+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2.  Discuss: [Consider removing the tx_extra field](https://github.com/monero-project/monero/issues/6668).

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

5. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#801 

# Discussion History
## UkoeHB | 2023-03-01T19:37:11+00:00
`[03-01-2023 16:00:34] <dangerousfreedom> I cant make it to today's meeting but from my side I started working in a transaction history component (drafted some basic ideas and started implementing it) and opened a [CCS](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/377). The plan is to build this component and integrate the knowledge proofs into the wallet using half of the time of the proposed CCS. The other half I would be working on`
`[03-01-2023 16:00:34] <dangerousfreedom> building necessary functions that needs to be done after discussing it in the #no-wallet-left-behind channel. I thank you for your comments.`
`[03-01-2023 16:17:17] <UkoeHB> Meeting .75hr`
`[03-01-2023 16:54:54] <isthmus> Shoot, I’m getting pulled into another meeting at the top of the hour. I may be able to drop into the MRL meeting later. Only two quick notes from my end:`
`[03-01-2023 16:54:58] <isthmus> (1) Geometry Labs produced a small workflow demo codebase showing how to connect R to C++, as part of gearing up to potentially contribute to OSPEAD computations. I will be chatting with Ruck about iterating the workflow and planned roadmap. We can skip talking about CCS today, as these discussions are ongoing and I’ll be updating the proposal.`
`[03-01-2023 16:55:15] <isthmus> (2) If tx_extra comes up, just want to reiterate my stance concisely: In the long run I will support any solution where the consensus rules / protocol / format results in a single anonymity pool of uniformly indistinguishable transaction. This includes, but is not limited to: `
`[03-01-2023 16:55:15] <isthmus> - removing tx_extra (in which case Monero’s scope is narrowed to store and transfer of value, i.e.making xmr just be a currency with no bells and whistles)`
`[03-01-2023 16:55:15] <isthmus> - a fixed-length encrypted field with consensus enforcement`
`[03-01-2023 16:55:15] <isthmus> (of course when I say “tx_extra” what I mean is not the literal field, but rather having a field designed for arbitrary data blobs)`
`[03-01-2023 16:55:15] <isthmus> Also, I am OK with relay rules as short-term measures, but never as a long-term replacement for consensus rules.`
`[03-01-2023 17:00:44] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/803`
`[03-01-2023 17:00:45] <UkoeHB> 1. greetings`
`[03-01-2023 17:00:45] <UkoeHB> hello`
`[03-01-2023 17:00:48] <tevador> Hi`
`[03-01-2023 17:00:53] <rbrunner> Hello`
`[03-01-2023 17:01:04] <one-horse-wagon[> Hello.`
`[03-01-2023 17:02:10] <Rucknium[m]> Hi`
`[03-01-2023 17:04:04] <UkoeHB> 2. updates, what's everyone working on?`
`[03-01-2023 17:06:43] <tevador> I posted a few updates about the new curve cycles, there are a few options available: https://github.com/monero-project/research-lab/issues/100`
`[03-01-2023 17:07:09] <ArticMine[m]> Hi`
`[03-01-2023 17:07:57] <Rucknium[m]> Sent C++ test for R wrappers to isthmus. The returned code passed the tests. Exceeded expectations, in fact. Writing R code to gather ring data by RPC. Spent my allocated 8 hours on researching possible statistical tests of encrypted tx_extra  contents. Made some progress on that, but not as much as I would have liked.`
`[03-01-2023 17:08:45] <UkoeHB> me: I merged dangerousfreedom's draft of seraphis knowledge proofs to seraphis_lib and updated it to production quality. Now I'm working on refactoring enote scanning into a state machine that will be more flexible/reusable in the long run. After this and further refactoring to use block checkpoints, I will work on the seraphis paper.`
`[03-01-2023 17:11:29] <UkoeHB> 3. discussion, we are slated to discuss tx_extra some more today`
`[03-01-2023 17:12:39] <rbrunner> Did any discussions happen between last meeting and this one? I didn't see any`
`[03-01-2023 17:12:41] <ArticMine[m]> Can we narrow down tx extra to A or B3?`
`[03-01-2023 17:12:56] <rbrunner> Well, discussions went on right after the meeting`
`[03-01-2023 17:13:28] <UkoeHB> as a reminder, here is the choice matrix:`
`[03-01-2023 17:13:28] <UkoeHB> A) [remove tx extra]: tx utility flexibility tied to hardfork (or steganography)`
`[03-01-2023 17:13:28] <UkoeHB> B) [keep tx extra in some optimized form]: uniformity and scaling trade-offs depending on the solution`
`[03-01-2023 17:13:29] <UkoeHB>     1) leave as unlimited-size TLV field`
`[03-01-2023 17:13:29] <UkoeHB>     2) mandate maximum tx extra size (e.g. anything in 0 - 1000 bytes) (option: encrypted by default)`
`[03-01-2023 17:13:29] <UkoeHB>     3) mandate optional fixed-length tx extra size + encrypt by default`
`[03-01-2023 17:13:29] <UkoeHB>     4) mandate fixed-length tx extra for all txs + encrypt by default`
`[03-01-2023 17:13:30] <UkoeHB>     5) other`
`[03-01-2023 17:14:16] <one-horse-wagon[> Can we just go ahead and vote.  I vote for A.  Get rid of it.`
`[03-01-2023 17:15:06] <ArticMine[m]> I prefer a vote to narrow down to A or B3 first `
`[03-01-2023 17:15:06] <tevador> B3 sounds like a good compromise`
`[03-01-2023 17:15:10] <rbrunner> With the few people here? That's a bit optimistic. We could vote, but the vote would probably get ignored ...`
`[03-01-2023 17:15:17] <sech1> A means removing it for regular transactions, not for coinbase?`
`[03-01-2023 17:15:18] <UkoeHB> I see this problem as being a conflict between three of Monero's core design goals: privacy, scalability, and longevity.`
`[03-01-2023 17:15:29] <tevador> sech1: yes, coinbase would keep it`
`[03-01-2023 17:15:35] <sech1> A in the long term, B3 short term`
`[03-01-2023 17:15:53] <sech1> B3 gives only 2 anonymity puddles`
`[03-01-2023 17:16:08] <rbrunner> What is "long term" for you, sech1?`
`[03-01-2023 17:16:15] <sech1> Seraphis fork`
`[03-01-2023 17:16:27] <tevador> This decision is for the Seraphis fork.`
`[03-01-2023 17:16:33] <sech1> then A`
`[03-01-2023 17:16:47] <sech1> but if A, we need to gather all current uses of tx_extra`
`[03-01-2023 17:16:50] <sech1> from all parties`
`[03-01-2023 17:17:08] <tevador> Pre-Seraphis, we have this: https://github.com/monero-project/monero/pull/8733`
`[03-01-2023 17:17:25] <hbs[m]> B3 would also probably need to gather all uses of tx_extra as some may exceed the fixed-length that B3 would install`
`[03-01-2023 17:17:51] <Rucknium[m]> UkoeHB: Isn't it Security, Privacy, and Decentralization? https://www.getmonero.org/resources/about/`
`[03-01-2023 17:17:53] <ArticMine[m]> B3 256 bytes `
`[03-01-2023 17:17:58] <rbrunner> We had 256 bytes on the table. Is something important known that would not fit?`
`[03-01-2023 17:18:40] <rbrunner> Because I would, so far, gladly agree to narrow down to A versus B3 256 bytes for a vote`
`[03-01-2023 17:18:42] <UkoeHB> A means a permanent increase in the chance of future hardforks - increased power of the core team.`
`[03-01-2023 17:19:09] <UkoeHB> Rucknium[m]: decentralization isn't really a property`
`[03-01-2023 17:19:17] <UkoeHB> it's just a fancy word that sounds good`
`[03-01-2023 17:19:37] <UkoeHB> the goal of 'decentralization' is longevity`
`[03-01-2023 17:19:37] <ArticMine[m]> We can vote for A or B3 256 Now Then announce the final vote between A  and B3 256`
`[03-01-2023 17:19:41] <moneromooo> B3 would also remove the ability for public data fwiw, which ew have now. Like "add this hash of some timestamped data".`
`[03-01-2023 17:20:18] <rbrunner> Well, any such "public" service could publish their fixed key?`
`[03-01-2023 17:20:24] <sech1> Does it affect atomic swaps in any way? Or Seraphis will fix it in another way?`
`[03-01-2023 17:20:35] <moneromooo> No. You can have longevity with a totally centralized system. They're orthogonal.`
`[03-01-2023 17:21:05] <tevador> AFAIK none of the atomic swap protocols for Monero need tx_extra.`
`[03-01-2023 17:21:14] <sech1> good`
`[03-01-2023 17:21:20] <hbs[m]> rbrunner: may be hard to say, but for example this is a tx coming out of a CEX, where tx_extra has 323 bytes: https://localmonero.co/blocks/search/06b4837aaebf9c9dc011cf4ad8c51463d0f6715337f01fef9b4833bf12bedca2`
`[03-01-2023 17:21:38] <rbrunner> By the way, I was brainstorming about a vote not in a particular meeting, but in a GitHub issue during one week, say`
`[03-01-2023 17:22:18] <tevador> hbs[m]: this is due to the tx public keys, there are no extra data in that tx.`
`[03-01-2023 17:22:22] <rbrunner> Because meetings tend to have attendance problems`
`[03-01-2023 17:22:22] <ArticMine[m]> We have to narrow this down first `
`[03-01-2023 17:22:39] <rbrunner> Of course`
`[03-01-2023 17:22:52] <sech1> "where tx_extra has 323 bytes" <- I think it's because of additional pubkeys (one per output)`
`[03-01-2023 17:23:01] <sech1> they can be moved to a dedicated tx field`
`[03-01-2023 17:23:12] <rbrunner> They are, in Seraphis, no?`
`[03-01-2023 17:23:19] <hbs[m]> tevador: Ok then, thanks for clarifying, I had not checkd the actual content, just checked the size.`
`[03-01-2023 17:23:44] <tevador> Yes, Seraphis already separates tx pubkeys. tx_extra would be only for "extra" data then.`
`[03-01-2023 17:24:17] <rbrunner> So we can maybe vote today what exactly we put up for a vote?`
`[03-01-2023 17:24:19] <sech1> #define TX_EXTRA_MYSTERIOUS_MINERGATE_TAG   0xDE`
`[03-01-2023 17:24:25] <sech1> the only thing I found about actual usage :D`
`[03-01-2023 17:24:34] <sech1> coming from scam pool minergate`
`[03-01-2023 17:24:35] <ArticMine[m]> rbrunner: Yes `
`[03-01-2023 17:25:11] <rbrunner> Something like a first derivative :)`
`[03-01-2023 17:25:32] <tevador> Maybe we can agree that the options are A or B3. If we advertise the next meeting on reddit, hopefully more people will come.`
`[03-01-2023 17:25:32] <UkoeHB> I like B3 because it is an incremental improvement in privacy and longevity, and only a minor regression for scalability. The other options are more significant regressions in at least one property (other than 'do nothing').`
`[03-01-2023 17:25:39] <ArticMine[m]> I propose A or B3 256`
`[03-01-2023 17:25:44] <moneromooo> Good lord, reddit...`
`[03-01-2023 17:26:02] <Rucknium[m]> Do we have a clear plan for implementation of B3 256? Has monerod ever changed the criteria for relaying transactions outside of a hard fork?`
`[03-01-2023 17:26:09] <ofrnxmr[m]> Im solidly in group A`
`[03-01-2023 17:26:09] <ofrnxmr[m]> Perhaps should be noted that wownero HF's to 1kb limit soon`
`[03-01-2023 17:26:27] <rbrunner> You can only vote today what we put up for a vote, seems to me`
`[03-01-2023 17:26:51] <moneromooo> Well, we haven't yet voted whether there should be a vote.`
`[03-01-2023 17:27:02] <rbrunner> I second ArticMine's A or B3 256 as the only two options to vote on`
`[03-01-2023 17:27:09] <moneromooo> I do too.`
`[03-01-2023 17:27:10] <ghostway[m]> B3 is my choice as well`
`[03-01-2023 17:27:10] <ghostway[m]> For the update, I'm trying to make more tests to reveal more bugs in my code. I think it is ok. Will commit and push in the coming days for another round of reviews from koe`
`[03-01-2023 17:27:25] <tevador> Rucknium[m]: we have PR #8733`
`[03-01-2023 17:27:27] <Rucknium[m]> I would expect that we would have a leaky sieve: many old version nodes would allow those tx. If the tx gets to a miner who is running an old version node, then the relay rules are ineffective`
`[03-01-2023 17:28:05] <rbrunner> Voting whether having a vote is a bit circular ...`
`[03-01-2023 17:28:16] <UkoeHB> Rucknium[m]: there is not a concrete design for B3 yet, it would require some discussion.`
`[03-01-2023 17:28:24] <tevador> A or B3 will be implemented with Seraphis, which is a mnadatory hard fork.`
`[03-01-2023 17:29:01] <ghostway[m]> rbrunner: Being like the US system lol`
`[03-01-2023 17:29:02] <ArticMine[m]> It narrows down the debate `
`[03-01-2023 17:29:20] <rbrunner> If we have, by any chance, an earlier hardfork still, we could introduce even earlier, if somebody goes the extra mile to modify the old tx format`
`[03-01-2023 17:29:27] <UkoeHB> It would be nice to see less discussion about voting and more focus on design goals/philosophy.`
`[03-01-2023 17:29:43] <ofrnxmr[m]> +1 koe`
`[03-01-2023 17:30:34] <rbrunner> I am pretty sure that an analysis would show we have pretty much the same goals, but weight them differently, hence the long standstill`
`[03-01-2023 17:30:56] <rbrunner> Because goals conflict in this case as I understand them`
`[03-01-2023 17:31:04] <UkoeHB> can't analyze comments that don't exist`
`[03-01-2023 17:31:26] <ArticMine[m]> I just do not see  consensus possible for any other options `
`[03-01-2023 17:32:02] <ArticMine[m]> So we can narrow the field `
`[03-01-2023 17:32:52] <ofrnxmr[m]> A/B3 , can we agree that these are the goals? And progress from there`
`[03-01-2023 17:33:03] <UkoeHB> I'd rather have a consensus on the reasons for making a choice, than force a decision to be made.`
`[03-01-2023 17:34:11] <tevador> Does anyone favor any other B apart from B3?`
`[03-01-2023 17:35:22] <UkoeHB> the people in favor of other options are not in this meeting`
`[03-01-2023 17:36:12] <UkoeHB> https://libera.monerologs.net/monero-research-lab/20230215#c205874`
`[03-01-2023 17:37:11] <rbrunner> Hmm, looks like it`
`[03-01-2023 17:38:11] <ofrnxmr[m]> Rene appears to be the only one who did not have a vote for a or b3`
`[03-01-2023 17:38:21] <tevador> I see 3 people there who did not specify either A or B3.`
`[03-01-2023 17:38:49] <rbrunner> Yes, back then. I can easily compromise on B3 256, and would agree to vote on that.`
`[03-01-2023 17:38:49] <tevador> + "unwanted" and "blank"`
`[03-01-2023 17:38:58] <ArticMine[m]> Out of how many?`
`[03-01-2023 17:39:43] <tevador> At least 20`
`[03-01-2023 17:39:46] <ofrnxmr[m]> tevador:  thanks, I missed those 👍`
`[03-01-2023 17:40:08] <rbrunner> So really like American politics? First round of voting with *all* options, open for 1 week, second round with the two top voted from the first round?`
`[03-01-2023 17:40:37] <rbrunner> If we declare this meeting as not complete enough to decide what to vote on ...`
`[03-01-2023 17:41:12] <tevador> I think the support for anything other than A or B3 is not there. We can narrow it down to A or B=B3.`
`[03-01-2023 17:41:43] <ArticMine[m]> tevador: That is my point `
`[03-01-2023 17:44:44] <rbrunner> Now, the resident Core Team member could throw in his authority and announce a vote A versus B3 ... ?`
`[03-01-2023 17:45:41] <rbrunner> In some way to discuss further`
`[03-01-2023 17:46:51] <tevador> We can open a MRL issue with these two choices and schedule the final decision for the next meeting.`
`[03-01-2023 17:47:16] <UkoeHB> I think this whole thing is good evidence that being unable to operate without core is not healthy for the project in the long run.`
`[03-01-2023 17:48:18] <ArticMine[m]> This is not a core team issue `
`[03-01-2023 17:48:54] <rbrunner> Maybe, but I think we still compare quite favorably with other projects. We don't routinely bumb into such difficult decisions like this one`
`[03-01-2023 17:49:03] <rbrunner> *bump`
`[03-01-2023 17:49:12] <ArticMine[m]> We should be able as a group to narrow this down `
`[03-01-2023 17:49:49] <rbrunner> Well, we don't miss much right now. Still nobody explicitely spoke out against putting up that vote.`
`[03-01-2023 17:50:00] <UkoeHB> being able to operate without centralized decision making * there`
`[03-01-2023 17:50:23] <tevador> We could roll a d20.`
`[03-01-2023 17:50:56] <rbrunner> The last digit of the hash of the next XMR block decides.`
`[03-01-2023 17:54:05] <rbrunner> Come on, give yourself a jolt, if enough people agree on that vote, we have at least something :)`
`[03-01-2023 17:55:15] <UkoeHB> I remain more interested in design philosophy than voting.`
`[03-01-2023 17:55:36] <moneromooo> I agree that A and B3 seem to be the best ones to choose from. Whether a vote is the best idea though, not sure.`
`[03-01-2023 17:56:10] <rbrunner> The least bad idea? To break out of a 2 year checkmate situation?`
`[03-01-2023 17:56:13] <ArticMine[m]> UkoeHB: I see that question as flexibility without a hard fork`
`[03-01-2023 17:56:26] <UkoeHB> ArticMine[m]: yes`
`[03-01-2023 17:56:33] <tevador> So let's open an issue for it, narrowed down to A or B(3). Some arguments for each choice will be gathered for the next meeting.`
`[03-01-2023 17:57:36] <Rucknium[m]> I support tevador 's plan`
`[03-01-2023 17:57:44] <rbrunner> I understand UkoeHB interest in design philosophy, but frankly, I am afraid such discussion would be even more difficult`
`[03-01-2023 17:58:16] <tevador> Btw, we can still have a soft fork with option A. It has been discussed before.`
`[03-01-2023 17:58:18] <UkoeHB> that just sounds lazy, we should not make decisions out of laziness`
`[03-01-2023 17:58:40] <ArticMine[m]> How does narrowing down the vote preclude the philosophy question `
`[03-01-2023 17:59:22] <UkoeHB> it's mostly a distraction, since philosophy logically precedes choice`
`[03-01-2023 17:59:34] <UkoeHB> notice how we wasted 40 minutes 'narrowing it down'`
`[03-01-2023 17:59:38] <rbrunner> I guess UkoeHB thinks that the "right" philosophy would naturally decide the tx_extra question`
`[03-01-2023 18:00:56] <UkoeHB> We are at the end of the hour, so I'll call it here. We can tentatively narrow the choices to A/B3 pending further direction changes.`
`[03-01-2023 18:01:02] <rbrunner> Well, I think this meeting was more than just a waste of time. If we really put up that issue, that is.`
`[03-01-2023 18:01:10] <UkoeHB> next meeting let's try to have more concrete arguments`
`[03-01-2023 18:01:13] <UkoeHB> thanks everyone`

# Action History
- Created by: Rucknium | 2023-02-28T16:10:44+00:00
- Closed at: 2023-03-04T18:50:25+00:00
