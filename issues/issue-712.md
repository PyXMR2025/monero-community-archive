---
title: Monero Research Lab Meeting - Wed 08 June 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/712
author: Rucknium
assignees: []
labels: []
created_at: '2022-06-06T19:01:58+00:00'
updated_at: '2022-06-13T13:06:39+00:00'
type: issue
status: closed
closed_at: '2022-06-13T13:06:39+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

5. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

7. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

8. Any other business

9. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#711 

# Discussion History
## UkoeHB | 2022-06-09T12:42:22+00:00
```
[06-09-2022 17:00:21] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/712
[06-09-2022 17:00:28] <UkoeHB> 1. greetings
[06-09-2022 17:00:28] <UkoeHB> hello
[06-09-2022 17:01:02] <rbrunner> Hello
[06-09-2022 17:01:36] <Rucknium[m]> Hi
[06-09-2022 17:01:36] <xmr-ack[m]> hi
[06-09-2022 17:01:37] <ooo123ooo1234567> hello
[06-09-2022 17:02:19] <jberman[m]> hello
[06-09-2022 17:04:36] <UkoeHB> 2. updates, what is everyone working on
[06-09-2022 17:05:25] <jberman[m]> Been working on PR 7760 exclusively
[06-09-2022 17:05:34] <jberman[m]> I see which lines of code solve the issues highlighted in the 3 tests. I'm working off this branch here to help make it clearer to others (it's still a WIP): https://github.com/j-berman/monero/commits/7760-streamlined-logic
[06-09-2022 17:05:44] <jberman[m]> I'm also working on a doc that explains what each test is doing, what issues they expose in the old code, what 7760's code is doing to solve them, etc. DM if you want to see this doc
[06-09-2022 17:05:55] <jberman[m]> The branch above and the doc is very much so still a WIP. I'm still working through my understanding of every single line. But at this point I feel confident I understand the issues exposed in the tests and the core solutions to those issues
[06-09-2022 17:07:21] <Rucknium[m]> Some BCH work (which can be re-purposed to improve https://monero.com/charts/shielded since it calculates the incoming and outgoing txs and value from CoinJoin transactions rather than just tally the number of CoinJoin UTXOs). Working with mj-xmr  to re-implement the C++ decoy selection algorithm in Python. mj is running the code to produce samples from each implementation and then we will compare them statistically with a
[06-09-2022 17:07:21] <Rucknium[m]> Kolmogorov-Smirnov test.
[06-09-2022 17:08:08] <Rucknium[m]> So hopefully soon we will have a formal specification for the default decoy selection algorithm. If we don't have one for multisig, at least we can have one for the DSA :)
[06-09-2022 17:09:10] <UkoeHB> me: working on the enote scanning workflow for seraphis. Figuring out how to handle reorgs during scanning was a little bit of work, plus deciding the most flexible interface.
[06-09-2022 17:12:04] <UkoeHB> 3. discussion, any comments/questions/topics?
[06-09-2022 17:12:14] <xmr-ack[m]> I fixed a memory leak in my script which processes the dataset i'm collecting. Also added some multiprocessing in places to speed up the undersampling process. I should have the new version of the preliminary dataset soon to start retraining models on. 
[06-09-2022 17:13:03] <Rucknium[m]> The K-S test will tell us if the two implementations produce statistically identical samples. For now we won't try to implement identical PRNGs for the C++ and Python implementations. The K-S test is sufficient for now IMHO.
[06-09-2022 17:13:35] <ooo123ooo1234567> <Rucknium[m]> "Some BCH work (which can be re-..." <- in computer science it must be done by code translation from one lang to another, not by statistical tests
[06-09-2022 17:13:59] <ooo123ooo1234567> and not with the help of docs
[06-09-2022 17:16:25] <Rucknium[m]> Just a note from last time: I said that I think Monero's weighting of the decoy selection by number of txs in each block would mitigate the issue with a spike in speculative activity shifting the real spend distribution. I didn't think it through -- in fact now I think it exacerbates it since the DSA would select more heavily from younger txs during such an incident, but was we saw with Dogecoin, the average real spend age gets
[06-09-2022 17:16:25] <Rucknium[m]> older.
[06-09-2022 17:16:41] <Rucknium[m]> So there would probably be a greater difference between the real spend distribution and the decoy distribution, which is bad.
[06-09-2022 17:18:19] <UkoeHB> makes sense
[06-09-2022 17:19:36] <UkoeHB> For the agena, I think it's ok to remove items 6 and 7
[06-09-2022 17:20:15] <Rucknium[m]> ooo123ooo1234567: Ok maybe later we will draw from identical PRNGs. In the short term what is needed is a mathematical expression for the probability density function (or probability mass function to be entirely precise) of the decoy selection algorithm.
[06-09-2022 17:20:34] <UkoeHB> could probably reorganize it into: A) things scheduled for the meeting, B) links to ongoing projects for reference
[06-09-2022 17:22:13] <Rucknium[m]> UkoeHB: Ok sounds good.
[06-09-2022 17:24:08] <Rucknium[m]> I know that there is some concern in the Monero community (vaguely defined) about additional view key options with Seraphis. UkoeHB posted a clarification on the GitHub issue. I don't know if there is anything that MRL should do about it. Sort of a tricky issue.
[06-09-2022 17:24:44] <UkoeHB> https://github.com/monero-project/research-lab/issues/92#issuecomment-1146810255
[06-09-2022 17:25:07] <UkoeHB> That comment seemed to help the redditor, so hopefully any confusion is cleared up
[06-09-2022 17:25:38] <Rucknium[m]> Tricky in that obviously there should be open debate about it, and presenting a "united front" about the additional view keys is maybe not in the Monero ethos. But also we don't want incorrect information to flourish.
[06-09-2022 17:26:39] <UkoeHB> just need to help everyone get on the same page, I don't mind criticism
[06-09-2022 17:27:20] <UkoeHB> there is no ideal solution, it's important to discuss the pros/cons that go into design decisions
[06-09-2022 17:29:15] <ArticMine> I much prefer the Jamtis approach than relying on heuristics. The latter will favor for example blockchain surveillance companies, creating a privacy in balance of power 
[06-09-2022 17:30:34] <ArticMine> Making it relatively easier for power to obtain the actual balance
[06-09-2022 17:30:53] <rbrunner> It's also a topic that's controversial for some people quite "naturally", people who don't want anybody handing over any kind of keys to anybody else
[06-09-2022 17:32:02] <UkoeHB> Speaking of design decisions, it would be helpful for people to think about different pain points with Monero. Both from a privacy attributes point of view, and user experience. I have put everything I know/remember into my seraphis implementation so far, but could always be missing something (e.g. the value of being unable to discover burnt funds, which isn't a serious security issue but still can impact users and third-party 
[06-09-2022 17:32:02] <UkoeHB> apps).
[06-09-2022 17:35:00] <cryptogrampy[m]> I think subscription services / user accounts are maybe something worth mulling.  I brought it up in dev yesterday about account creation and login verification using subaddressesbut maybe there's a better way
[06-09-2022 17:36:53] <cryptogrampy[m]> subaddress signature verification* 
[06-09-2022 17:38:12] <UkoeHB> cryptogrampy[m]: can you explain the workflow for subscription services in more detail?
[06-09-2022 17:39:08] <Rucknium[m]> cryptogrampy: If you are not already familiar, you may want to check out read.cash , noise.cash , memo.cash , and member.cash for inspiration
[06-09-2022 17:42:24] <cryptogrampy[m]> UkoeHB: No, but i'll think it through a little more for the next meeting 😛.  
[06-09-2022 17:42:50] <UkoeHB> lol ok
[06-09-2022 17:43:23] <UkoeHB> any other topics to discuss?
[06-09-2022 17:43:35] <Rucknium[m]> Just another idea to throw out there: The International Association for Cryptographic Research (IACR) has a jobs board: https://www.iacr.org/jobs/ It would be nice if we could get more visibility for MRL there, but we don't exactly have any "jobs" for anyone.
[06-09-2022 17:45:14] <Rucknium[m]> Or maybe the job is "Review multisig implementation and write a formal protocol specification for it"
[06-09-2022 17:46:06] <Rucknium[m]> (If you can raise money through the CSS, MAGIC, or other means)
[06-09-2022 17:49:20] <UkoeHB> might be better to set a large bounty for it
[06-09-2022 17:49:30] <UkoeHB> to help the socially inept
[06-09-2022 17:51:47] <ooo123ooo1234567> <Rucknium[m]> "Just another idea to throw out..." <- Any similar jobs for machine learning or statistics ?
[06-09-2022 17:53:06] <ooo123ooo1234567> and C++ devs too
[06-09-2022 17:53:28] <Rucknium[m]> Job boards for statistics? Yes. We could think about posting there too.
[06-09-2022 17:55:40] <UkoeHB> ok 
[06-09-2022 17:55:41] <Rucknium[m]> What I would like to happen is for MAGIC Monero Fund to get more funds so that we can push out a call for research grant applications to some of the big general research grant databases. Right now I don't feel like we have enough funds to be looking for lots of grant applications, since we might end up having to turn down really good proposals.
[06-09-2022 17:56:12] <Rucknium[m]> So that would include the topic areas of both cryptography and statistics.
[06-09-2022 17:56:16] <xmr-ack[m]> An idea I've had for a while, is once my MAGIC grant has finished and we have a quality dataset of transactions. We could fund a prize for a Kaggle competition which would attract high quality datascience talent from all over to look into Monero.
[06-09-2022 17:56:41] <Rucknium[m]> (I'm on the MAGIC committee)
[06-09-2022 17:57:59] <ooo123ooo1234567> Rucknium[m]: efficiency of MAGIC relatively to monero progress is small, what's the purpose to bootstrap it ?
[06-09-2022 17:58:11] <ooo123ooo1234567> Rucknium[m]: yes, conflict of interest
[06-09-2022 17:58:19] <Rucknium[m]> I think Kaggle is a good idea 👍️
[06-09-2022 18:00:03] <UkoeHB> ok it's the end of the hour, thanks for attending everyone
```

# Action History
- Created by: Rucknium | 2022-06-06T19:01:58+00:00
- Closed at: 2022-06-13T13:06:39+00:00
