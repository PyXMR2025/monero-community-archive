---
title: Monero Research Lab Meeting - Wed 06 March 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/976
author: Rucknium
assignees: []
labels: []
created_at: '2024-03-05T21:03:24+00:00'
updated_at: '2024-03-14T12:43:29+00:00'
type: issue
status: closed
closed_at: '2024-03-14T12:43:28+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [CypherStack have requested 50% ($16,000) of the Bulletproofs++ Peer Review CCS to be paid out.](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/358#note_23485)

4. @jeffro256 [ I think we can improve how the nodes handle alternative blocks in a way that might naturally reduce the number of reorgs on the network.](https://github.com/monero-project/meta/issues/966#issuecomment-1936243293)

5. [Transaction volume increase this week](https://bitinfocharts.com/comparison/monero-transactions.html#3m)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#973 

# Discussion History
## Rucknium | 2024-03-14T12:43:28+00:00
> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/976     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< vtnerd >__ hi     

> __< rbrunner >__ Hello     

> __< a​aron:cypherstack.com >__ Hello!     

> __< p​lowsof:matrix.org >__ hi     

> __< d​iego:cypherstack.com >__ hello hello!     

> __< 0​xfffc:matrix.org >__ Hi everyone.     

> __< h​into.janaiyo:matrix.org >__ hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: OSPEAD. I think I will make my self-imposed deadline of next week for milestone 2.     

> __< vtnerd >__ me: working on getting LWS new accounts "pushed" to scan threads intead of resetting the scan state on new accounts     

> __< vtnerd >__ also was tracking a LWS bug someone reported privately via telegram, but was unable to duplicate (segfault)     

> __< 0​xfffc:matrix.org >__ Me: worked on second version of reader_writer lock 9181 which addresses writer starvation issue. It is finished, and in a good shape. I believe with few reviews and a little bit more testing we will be able to get it merged. I am running it on my private node too.     

> __< r​ucknium:monero.social >__ 3) Discuss: CypherStack have requested 50% ($16,000) of the Bulletproofs++ Peer Review CCS to be paid out. https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/358#note_23485     

> __< d​iego:cypherstack.com >__ Hiya. I brought this up at the community meeting too.     

> __< r​ucknium:monero.social >__ Aaron Feickert: Could you say something brief about the review progress. I heard that you found some flaws in the security proofs, but you were able to repair some(?) of them     

> __< d​iego:cypherstack.com >__ Basically we're more than halfway through and the singular milestone is kind of set up to only pay out at the end. Given the length of the project, it'd be very helpful to us to be able to have a mid payout to keep some cash flowing.     

> __< d​iego:cypherstack.com >__ Aaron can answer specific questions, but our progress report is basically the following:     

> __< d​iego:cypherstack.com >__ We've made significant progress. Lots of math. Lots of digging. Found some errors so far. Talked to the authors who responded. Still more to work through. Got like 11-12 pages of math so far.     

> __< d​iego:cypherstack.com >__ We DO have a VERY incomplete draft of the paper for viewing if people want proof of work. Just what we've done up to this point.     

> __< d​iego:cypherstack.com >__ Aaron Feickert: if you wanted to give a very brief statement about security proofs and authors as Rucknium asked?     

> __< a​aron:cypherstack.com >__ Yeah, we've identified a number of issues so far. There's a fair amount of notation that's incomplete or incorrect, several points in the proofs that we needed to expand on significantly for correctness, one proof that was incorrect (and even had an incorrect statement) that we rewrote, and another whose validity we're still attempting to verify     

> __< a​aron:cypherstack.com >__ I've been in contact with the preprint authors as well to discuss some of the issues     

> __< r​ucknium:monero.social >__ "incorrect statement" == theorem is wrong? Do you have a counterexample? Is it an important THM for the paper?     

> __< r​ucknium:monero.social >__ To me it sounds like we will need another party to do another review of your work because the changes are large. That's fine. It affects hard fork planning.     

> __< a​aron:cypherstack.com >__ The particular lemma is at the heart of higher-level emulation claims. The statement of the lemma was incorrect: it couldn't possibly have held, didn't match the proof (which had other errors), and wouldn't have made sense for the emulation     

> __< a​aron:cypherstack.com >__ The authors agreed, provided the actual statement, and we rewrote the proof to assert it could be fixed (it can)     

> __< a​aron:cypherstack.com >__ A lot of the preprint is written fairly informally, unfortunately, in terms of things like notation and claims. This makes it challenging.     

> __< rbrunner >__ How does that compare with earlier Bulletproofs and Bulletproofs+?     

> __< rbrunner >__ I mean, do you happen to know whether the papers were better?     

> __< a​aron:cypherstack.com >__ That's an excellent question     

> __< a​aron:cypherstack.com >__ Roughly speaking, I'd say that BP and BP+ share a lot of the same underlying structure, and the way the range proving protocols are built makes analysis reasonably straightforward     

> __< r​ucknium:monero.social >__ Thanks so much for your work on this. I don't like to set precedent for splitting milestone payments, but your CCS proposal only had one milestone. Most proposals have multiple. I think it would be OK to pay half the milestone if we get your current draft.     

> __< a​aron:cypherstack.com >__ The extra "+" in BP++ carries a lot weight; the structure of its range proving protocols is _very_ different and _much_ more complex     

> __< a​aron:cypherstack.com >__ *a lot of weight     

> __< r​ucknium:monero.social >__ FWIW, BP+ had a flaw in one of its math proofs. It was caught and corrected in one of Monero's reviews.     

> __< a​aron:cypherstack.com >__ Yep     

> __< rbrunner >__ I think the precedent would not be a big problem if we try to find points for mid-way payout in future such CCSs to avoid the issue in the first place     

> __< rbrunner >__ For big reviews, that is     

> __< a​aron:cypherstack.com >__ Anyway, as Diego Salazar mentioned, we have an in-progress report (around 11-12 pages)     

> __< a​aron:cypherstack.com >__ I would caution against making it widely available, lest readers assume more from it than they ought     

> __< r​ucknium:monero.social >__ My gut says that the benefit of BP++ might not be worth the risk. We "only" get smaller tx sizes and faster verification. But if we're wrong then a malicious actor can create counterfeit XMR. Too early to say for sure now while the review is ongoing of course.     

> __< rbrunner >__ Just curious: Will BP++ continue to be used in a FCMP version of Monero, if it comes to that?     

> __< r​ucknium:monero.social >__ If you don't want the draft widely available, then maybe write a summary of initial findings? That wouldn't take much time, right?     

> __< a​aron:cypherstack.com >__ Rucknium: how detailed would you like such a summary to be?     

> __< d​iego:cypherstack.com >__ No. The draft is ready to go and the work has been done on it already.     

> __< r​ucknium:monero.social >__ I am not a cryptographer, so ask one :)     

> __< a​aron:cypherstack.com >__ @rbrunner: I am not certain how much work would be needed to modify the BP++ protocols to support that     

> __< r​ucknium:monero.social >__ 1 - 2 pages summary I assume would cover things     

> __< a​aron:cypherstack.com >__ Rucknium: the risk assessment is tricky, to be sure, given the complexity     

> __< a​aron:cypherstack.com >__ There are a lot of new moving parts to BP++     

> __< d​iego:cypherstack.com >__ I'm sorry to be a choosing beggar here, but I'd rather not spend a few hours of unpaid work on a summary.     

> __< r​ucknium:monero.social >__ I was skeptical of this paper from the beginning. Take my skepticism with a grain of salt :)     

> __< a​aron:cypherstack.com >__ Rucknium: all math should be subject to healthy skepticism :D     

> __< d​iego:cypherstack.com >__ Happy to share the draft we prepared yesterday as proof of our work. If a summary is needed for release of half the funds then we'll push forward without it until completion.     

> __< d​iego:cypherstack.com >__ Not trying to be hostile or antagonistic. Hope my words don't come off that way.     

> __< a​aron:cypherstack.com >__ The draft does contain a warning right up front about its incomplete status, and is thoroughly watermarked as a draft!     

> __< a​aron:cypherstack.com >__ (This is common for Cypher Stack reviews, so there's no doubt about the draft status of initial reports)     

> __< r​ucknium:monero.social >__ If there are not vulnerability disclosure concerns with the draft, then we have to give something public to the community IMHO. It can be a summary or the current rough draft     

> __< a​aron:cypherstack.com >__ Again, I would just caution any readers against assuming final conclusions from such a draft     

> __< rbrunner >__ We have a comment on GitLab from UkoeHB: "A short progress report may be appropriate, to justify adding a milestone" I guess he could do with a more detailed interim report as well     

> __< d​iego:cypherstack.com >__ Showing the community isn't a problem, I don't think. I think the big issue is spreading it widely on social media.     

> __< a​aron:cypherstack.com >__ Rucknium: I know of only one implementation, and I don't think it's deployed anywhere (or even assumed to be ready for deployment)     

> __< rbrunner >__ Yeah, I don't think social media will be a real problem :)     

> __< rbrunner >__ In this particular case     

> __< a​aron:cypherstack.com >__ Readers should just be cautioned that the findings could change over time as the review continues, and as we continue discussions with the preprint authors     

> __< d​iego:cypherstack.com >__ Where would be appropriate/sufficient for community? IRC channels? Telegram? Reddit?     

> __< r​ucknium:monero.social >__ Post on the CCS proposal as a comment IMHO. Any community members closely following the proposal will see it     

> __< d​iego:cypherstack.com >__ Perhaps the gitlab discussion itself     

> __< rbrunner >__ Yup, had the same thought     

> __< r​ucknium:monero.social >__ Anyone else in the meeting here have opinions about this?     

> __< r​ucknium:monero.social >__ Diego Salazar: "I'm sorry to be a choosing beggar here, but I'd rather not spend a few hours of unpaid work on a summary." That's totally understandable :)     

> __< d​iego:cypherstack.com >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/358#note_23499     

> __< a​aron:cypherstack.com >__ Also note that the preprint authors haven't been sent the draft     

> __< rbrunner >__ Yeah, I suppose the work turned out to be bigger than anticipated anyway     

> __< a​aron:cypherstack.com >__ We've been discussing specific issues via email     

> __< r​ucknium:monero.social >__ You are aware that the paper was accepted at EUROCRYPT 24 right?     

> __< a​aron:cypherstack.com >__ I was not!     

> __< d​iego:cypherstack.com >__ By a lot. The proposal was first made when draft 1 was a thing and I didn't think much of the timeline. Then draft 2 dropped and it more than doubled the workload.     

> __< a​aron:cypherstack.com >__ The authors didn't mention it, but I also didn't ask /shrug     

> __< midipoet >__ Just clearly state it's a draft and summarise the content into bullet points with [draft] after each one?     

> __< r​ucknium:monero.social >__ https://eurocrypt.iacr.org/2024/acceptedpapers.php     

> __< p​lowsof:matrix.org >__ sounds ideal. jberman / UkoeHB where the first to request. if they can give it a lgtm     

> __< a​aron:cypherstack.com >__ Rucknium: interesting! How did you come across it?     

> __< r​ucknium:monero.social >__ Revise it and get coauthor credit ;)     

> __< r​ucknium:monero.social >__ kayabanerve saw it first     

> __< a​aron:cypherstack.com >__ I'm intrigued as to what the EUROCRYPT reviewers thought     

> __< r​ucknium:monero.social >__ And then we discussed here the quality of peer review standards in cryptography     

> __< a​aron:cypherstack.com >__ I will note that conference/journal reviews can be all over the place     

> __< r​ucknium:monero.social >__ *rubber stamp*     

> __< a​aron:cypherstack.com >__ I've seen some that are really excellent, and others where I questioned if the reviewer read the whole paper =p     

> __< a​aron:cypherstack.com >__ That's not to say their specific reviews were thorough or not thorough (I have no idea)     

> __< a​aron:cypherstack.com >__ I can only speak for our review     

> __< d​iego:cypherstack.com >__ Yeah if you all can go to the PR and give an emoji or something, that'd be great. :D     

> __< a​aron:cypherstack.com >__ (Terrifyingly, I've seen situations where reviewers were not required to read security proofs)     

> __< a​aron:cypherstack.com >__ Anyway, sorry to derail!     

> __< r​ucknium:monero.social >__ Yeah I quoted our conversation about that here in this channel. I hope that was OK.     

> __< a​aron:cypherstack.com >__ (Side note: the EUROCRYPT program looks excellent)     

> __< rbrunner >__ That "accepted paper" list is fascinating for a crypto-noob like me: How much I have absolutely no clue about :)     

> __< p​lowsof:matrix.org >__ pending emojis/lgtm from jberman/UkoeHB. it would seem that binaryFate should then go ahead and send out the payment when possible yes?     

> __< rbrunner >__ Sounds reasonable to me     

> __< d​iego:cypherstack.com >__ Weee! Thanks all.     

> __< rbrunner >__ Well, depending on the emoji used of course     

> __< d​iego:cypherstack.com >__ We do hope to have this completed this month, I believe.     

> __< a​aron:cypherstack.com >__ Hopefully the giant DRAFT watermark is large and annoying enough :)     

> __< r​ucknium:monero.social >__ Thank you Diego Salazar  and Aaron Feickert . Incredible work.     

> __< d​iego:cypherstack.com >__ Given we are actually much farther than half way     

> __< a​aron:cypherstack.com >__ Rucknium: thanks! I admit it's been a challenging review     

> __< a​aron:cypherstack.com >__ But as always, I hope it's useful to the community and broader ecosystem     

> __< d​iego:cypherstack.com >__ jberman: UkoeHB ^     

> __< d​iego:cypherstack.com >__ either way. Nothing else from us.     

> __< r​ucknium:monero.social >__ We had a couple more items of the agenda. jeffro256  isn't here now to continue the +1 alternative block tiebreaking idea.     

> __< r​ucknium:monero.social >__ We have had a x2 increase in Monero tx volume the last two days: https://bitinfocharts.com/comparison/monero-transactions.html#3m     

> __< a​aron:cypherstack.com >__ 2x increase in two days??     

> __< hyc >__ the surge seems to have already subsided     

> __< rbrunner >__ Yes. Just checked, it's ongoing. They pushed blocksize up to 310 KB at one time     

> __< a​aron:cypherstack.com >__ Some kind of obvious spam attack?     

> __< a​aron:cypherstack.com >__ Anything stand out about the tx structures?     

> __< rbrunner >__ In the morning UTC it was a bit less. Now we have again 1039 txs waiting.     

> __< hyc >__ my node says there are ~880txs in pool now, 5 block backlog     

> __< a​aron:cypherstack.com >__ geez     

> __< rbrunner >__ Mostly 1 in / 2 out as far as I can see, nothing extraordinary: https://xmrchain.net/     

> __< r​ucknium:monero.social >__ lots of 1in/2out txs. We could try to run the same analysis that we did in 2021. But that's a lot of work. https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60     

> __< hyc >__ could be a very naive exchange or pool doing payouts to 1 user per tx     

> __< hyc >__ when they should have been doing N destinations per tx...     

> __< p​lowsof:matrix.org >__ txpool for convenience: https://xmrchain.net/txpool     

> __< a​aron:cypherstack.com >__ holy mempool batman     

> __< r​ucknium:monero.social >__ plowsof and I are storing txpool data. This will help with fee prediction algorithms later.     

> __< hyc >__ I just check print_pool_stats on monerod ...     

> __< r​ucknium:monero.social >__ And other research questions we don't know about yet     

> __< a​aron:cypherstack.com >__ If it is an attack, wonder if it's the same entity/entities as the earlier Zcash spam attack     

> __< a​aron:cypherstack.com >__ That went on for quite some time     

> __< r​ucknium:monero.social >__ Anyone think I should divert effort to analyze this? I prefer "no"...     

> __< rbrunner >__ My first thought is "Depends on how long this continues" ...     

> __< r​ucknium:monero.social >__ I don't know what action could be taken. The dynamic block size is supposed to work its magic.     

> __< r​ucknium:monero.social >__ It's it's not magical, then it should be made more magical...but that has to wait for a hard fork     

> __< r​ucknium:monero.social >__ If it's*     

> __< p​lowsof:matrix.org >__ monerod print_pool_state for convenience* web url so i look busy hyc** lol     

> __< p​lowsof:matrix.org >__ stats*     

> __< r​ucknium:monero.social >__ Anything else? If not we can end the meeting.     

> __< r​ucknium:monero.social >__ --- end meeting ---     

> __< p​lowsof:matrix.org >__ thanks for chairing Rucknium!     

> __< UkoeHB >__ Thanks for the update Aaron, good to see the progress :)     

> __< a​aron:cypherstack.com >__ @UkoeHB thanks!    

# Action History
- Created by: Rucknium | 2024-03-05T21:03:24+00:00
- Closed at: 2024-03-14T12:43:28+00:00
