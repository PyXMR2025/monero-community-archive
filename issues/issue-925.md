---
title: Monero Research Lab Meeting - Wed 08 November 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/925
author: Rucknium
assignees: []
labels: []
created_at: '2023-11-08T16:59:52+00:00'
updated_at: '2023-11-14T17:17:29+00:00'
type: issue
status: closed
closed_at: '2023-11-14T17:17:29+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: Reducing 10 block lock: https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100). What are the bottlenecks for potential implementation?

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#915 

# Discussion History
## plowsof | 2023-11-10T16:53:02+00:00
Logs 
> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/925     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< vtnerd >__ hi     

> __< rbrunner >__ hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: I have a draft of comments and statistical simulations on jeffro256's PR 9023 to slightly change the decoy selection algorithm: https://gist.github.com/Rucknium/5562ac14e75e34ee04ed5093c660e083     

> __< j​effro256:monero.social >__ Thank you for doing that Rucknium     

> __< vtnerd >__ completed subaddresses in lws, did some bugs and other odds and ends in lws. now working on whether p2p-ssl tests are possible in monerod     

> __< r​ucknium:monero.social >__ And I think I have a way to find candidate consolidation transactions from PocketChange-like transactions using the Hungarian algorithm. I may share some draft code and results later.     

> __< rbrunner >__ Is this before OSPEAD, or later alongside OSPEAD?     

> __< hyc >__ what's up with sorting out the licensing for OSPEAD?     

> __< r​ucknium:monero.social >__ PR 9023? It can be implemented before OSPEAD. It is a small change that is probably not statistically detectable at current tx volume and ring size.     

> __< rbrunner >__ Ok. And later OSPEAD will supersede this all anyway, right?     

> __< r​ucknium:monero.social >__ hyc: The author of the library has said by email that he is OK with open source licensing (instead of no license), but hasn't push the change publicly.     

> __< hyc >__ we won't begin work on it until that's done     

> __< hyc >__ I had a summer intern lined up for it but we've lost him now that summer's over     

> __< r​ucknium:monero.social >__ rbrunner: No. PR 9023 reduces a distortion in the decoy selection algorithm that would have been there regardless of what the original probability distribution was supposed to be.     

> __< rbrunner >__ I see     

> __< r​ucknium:monero.social >__ 3) Discussion. What do we want to discuss?     

> __< j​effro256:monero.social >__ Speaking of decoy selection, is anyone against allowing duplicate membership proof members in Seraphis?     

> __< r​ucknium:monero.social >__ In a single ring?     

> __< j​effro256:monero.social >__ Yes     

> __< r​ucknium:monero.social >__ Would that be done to eliminate the distortion that PR 9023 reduces?     

> __< j​effro256:monero.social >__ Yeah it would     

> __< r​ucknium:monero.social >__ I don't think the distortion would become large enough to outweigh "sacrificing" ring member slot by having duplicates. We could try to quantify that.     

> __< rbrunner >__ Is this for some edge cases where we had a "lull", very few transactions over the last few hours, say?     

> __< r​ucknium:monero.social >__ If that's the only reason to allow duplicates.     

> __< r​ucknium:monero.social >__ rbrunner: The way that the current code works, the lull would have to last about a year. I think.     

> __< j​effro256:monero.social >__ I guess so, but people can always mis-use input slots or otherwise signal that a certain input is the true spend     

> __< r​ucknium:monero.social >__ Even in the standard wallet2 case you would sometimes have duplicates. That would waste a slot since you  cannot spend an output twice.     

> __< rbrunner >__ I am afraid I don't fully understand the issue at hand, but duplicating ring members as part of the normal algorithm, even if only rarely, sounds very strange.     

> __< j​effro256:monero.social >__ Fair enough     

> __< r​ucknium:monero.social >__ My simulations with realistic data directly from monerod's `get_output_distribution` call suggests that the distortion is minor. The KS statistic is below 0.01 in the 4 scenarios I ran.     

> __< rbrunner >__ In any case, it's pretty counter-intuitive to claim that a ring with a duplicate would be better somehow than a ring where just any random decoy gets picked to get rid of the duplicate ...     

> __< rbrunner >__ But well, maybe intuition is not a good approach here :)     

> __< j​effro256:monero.social >__ Yeah in either case the difference would be tiny     

> __< r​ucknium:monero.social >__ rbrunner: I have not done a rigorous analysis of that, but at this moment I agree.     

> __< j​effro256:monero.social >__ Yeah intuition might be correct here     

> __< r​ucknium:monero.social >__ The problem that PR 9023 fixes involves the large set of candidate decoys that are chosen to make sure there are enough spendable outputs once the outputs with custom unlock time and the longer (60 block) coinbase lock are removed from the candidate set.     

> __< r​ucknium:monero.social >__ More things to discuss? Anything about the CCS theft?     

> __< j​effro256:monero.social >__ My initial idea for a solution was to have an RPC request which collects all unusable outputs *before* picking, then it would work 100% of the time without having to pick extras, but it would be like 15x more work lol     

> __< j​effro256:monero.social >__ rbrunner7, tangentially related to the CCS theft, do you know how many people use MMS?     

> __< j​effro256:monero.social >__ Like are you aware of any groups or forums etc     

> __< rbrunner >__ Not many, I am pretty sure. It does not work with the latest version of PyBitmessage, and only a few days ago somebody told me that.     

> __< j​effro256:monero.social >__ Oh did they change the API?     

> __< rbrunner >__ I made a small PR to get it working again. With that, people can at least easily play with multisig, to get an impression     

> __< rbrunner >__ No, two more strange error messages to ignore     

> __< j​effro256:monero.social >__ I tried finding other BitMessage implementations besides PyBitMessage, do you know of any?     

> __< rbrunner >__ And well, there is no way to deny that PyBitmessage is still on Python 2, and that's end of life. Not a good starting point if you want to get more secure     

> __< j​effro256:monero.social >__ I ask b/c I tried setting up the MMS but Ubuntu 23 doesn't support pyqt4 so I can only use it as a daemon     

> __< j​effro256:monero.social >__ MMS -> PyBitMessage     

> __< rbrunner >__ I am pretty sure that PyBitmessage is the only implementation that has an API, which is crucial     

> __< rbrunner >__ The latest version is available as an appimage which solves those problems quite nicely     

> __< j​effro256:monero.social >__ Okay I'll take a look thanks     

> __< rbrunner >__ https://appimage.bitmessage.org/releases/20230116/     

> __< rbrunner >__ And the PR needed to make it work: https://github.com/monero-project/monero/pull/9059     

> __< rbrunner >__ Hopefully, as I still have a quite mysterious problem with somebody how tried that. For me it works, for them receiving messages by the MMS fails, no idea yet why     

> __< rbrunner >__ Would be interesting if you tried as well, jeffro256     

> __< j​effro256:monero.social >__ I want to see if the BitMessage PoW is prohibitively expensive for UX purposes for large setup ceremonies     

> __< rbrunner >__ Don't think so, but the messages to exchange explode into the hundreds     

> __< rbrunner >__ And well, "large" starts at 6 or 7. If you are thinking about 20 or so, don't think that's feasible at all.     

> __< rbrunner >__ But do play with it, to see firsthand, if it works for you     

> __< r​ucknium:monero.social >__ Could we explore what it would take to bring Monero's multisig theory and implementation from experimental to "known secure"?     

> __< r​ucknium:monero.social >__ Do we know what the failure modes could be with the current multisig implementation? Would a failure mode be that a single signer could pay themselves the funds? Or even someone who does not have any of the multisig keys?     

> __< rbrunner >__ Well, no idea. I think some proofs would be needed, at least in principle.     

> __< rbrunner >__ Security proofs? Does that sound right?     

> __< rbrunner >__ And about failure modes, maybe UkoeHB would know more.     

> __< r​ucknium:monero.social >__ Sounds correct to me.     

> __< r​ucknium:monero.social >__ I could place multisig as an agenda item next week. Could invite kayabaNerve and koe if they want to come.     

> __< rbrunner >__ Not a bad idea     

> __< r​ucknium:monero.social >__ I will put multisig on the agenda. We can end the meeting here.     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-11-08T16:59:52+00:00
- Closed at: 2023-11-14T17:17:29+00:00
