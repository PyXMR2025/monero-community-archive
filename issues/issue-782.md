---
title: Monero Research Lab Meeting - Wed 18 January 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/782
author: Rucknium
assignees: []
labels: []
created_at: '2023-01-16T21:26:43+00:00'
updated_at: '2023-01-24T16:08:27+00:00'
type: issue
status: closed
closed_at: '2023-01-24T16:08:27+00:00'
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

#778 

# Discussion History
## UkoeHB | 2023-01-18T19:03:04+00:00
`[01-18-2023 17:00:08] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/782`
`[01-18-2023 17:00:08] <UkoeHB> 1. greetings`
`[01-18-2023 17:00:08] <UkoeHB> hello`
`[01-18-2023 17:00:21] <Rucknium[m]> Hi`
`[01-18-2023 17:00:26] <rbrunner> Hello`
`[01-18-2023 17:00:29] <vtnerd> hi`
`[01-18-2023 17:00:31] <one-horse-wagon[> Hello!`
`[01-18-2023 17:00:33] <UkoeHB> rbrunner: hey seraphis_essential might work :)`
`[01-18-2023 17:00:59] <rbrunner> Ok :)`
`[01-18-2023 17:01:02] <dangerousfreedom> Hi`
`[01-18-2023 17:02:45] * isthmus is partially around 👋`
`[01-18-2023 17:03:14] <UkoeHB> 2. updates, what's everyone working on?`
`[01-18-2023 17:04:13] <UkoeHB> me: continued cleanup of the seraphis library (for example yesterday I updated the legacy balance recovery stuff to support non-default hw devices)`
`[01-18-2023 17:05:43] <vtnerd> added admin-rest-api functions to monero-lws - the PR hasnt been made but the code is on my github`
`[01-18-2023 17:06:02] <vtnerd> this week is finally some bp++ hopefully`
`[01-18-2023 17:06:39] <Rucknium[m]> I did some historical analysis of the P2Pool outputs issue. Summary: The share was about 5% before the August hard fork, which is good news for privacy. It would have been bad if ring size was lower than now and p2pool output share was 15 - 20%. I will post the plots to the GitHub issue in 30 minutes (waiting on data processing).`
`[01-18-2023 17:07:31] <dangerousfreedom> still on the knowledge proofs`
`[01-18-2023 17:07:55] <isthmus> I've been doing housekeeping on some drafts that have been 95% done for months or years but still reside in private overleaf drafts... Main one is the fungibility defect labeling framework that has been shared here a few times in the past`
`[01-18-2023 17:09:38] <Rucknium[m]> isthmus:  Maybe tonz0fphun 's project could look at on-chain transaction uniformity defects.`
`[01-18-2023 17:10:07] <isthmus> Yea, based on recent chatter in this room I think that project could be a very good fit`
`[01-18-2023 17:12:10] <UkoeHB> 3. discussion`
`[01-18-2023 17:13:47] <Rucknium[m]> On OSPEAD: I am waiting for ArticMine's feedback on my draft. However, it's been 4 months so at some point I will just have to implement the plan in the document hyc and isthmus gave a green light to the general plan.`
`[01-18-2023 17:14:45] <UkoeHB> I've been thinking a little bit about data flow and when it's good or not good to use variants. Right now I have the seraphis tx implementations in separate structures, with the thought that it's much easier to reason about what a tx contains and what rules apply to it when everything is isolated. However, any marginal structural change will require an entirely new transaction type and essentially parallel `
`[01-18-2023 17:14:45] <UkoeHB> implementation of tx builders and files. Idk if this is really solvable or if it's just a tough tradeoff between spaghetti and verbosity.`
`[01-18-2023 17:16:16] <Rucknium[m]> Other members of the MAGIC Monero Committee (not me; I needed to abstain) voted to close mj's project that would help OSPEAD with things I cannot do. There was a lack of funds raised after two months. So like I have said before, OSPEAD will have some blind spots due to lack of C++ support. But the plan is mostly intact.`
`[01-18-2023 17:16:18] <UkoeHB> The alternative to separate structs is to make every tx component a variant, and then any tx handler internally branches off the variant types.`
`[01-18-2023 17:16:46] <Rucknium[m]> Unless someone else wants to work on the C++ work or mj finds funding another way.`
`[01-18-2023 17:17:14] <rbrunner> Hmmm, would that be a good topic for a new screen-sharing session, where you show what you have? I think without such an introduction it's hard to really get into this.`
`[01-18-2023 17:17:16] <UkoeHB> Which is what I'm doing for balance recovery - every enote type is piped into a variant, and enote handling involves an open-close branching pattern for type-based processing.`
`[01-18-2023 17:17:54] <rbrunner> For me right now not even the question is fully clear :)`
`[01-18-2023 17:17:59] <one-horse-wagon[> OSPEAD will have some blind spots due to lack of C++ support. But the plan is mostly intact.  Could you be more specific on the "blind spots" if possible?`
`[01-18-2023 17:19:00] <UkoeHB> Rucknium[m]: do you have an estimate of how much code is needed to get OSPEAD in shape? Like a couple files, maybe 2k lines, or a bunch of files, 5-10k lines?`
`[01-18-2023 17:19:23] <Rucknium[m]> For implementation in the Monero codebase? A few lines`
`[01-18-2023 17:20:01] <Rucknium[m]> It's just changing the probability distribution. You may have to import a new one or define it manually. Should not be hard`
`[01-18-2023 17:20:07] <UkoeHB> ah`
`[01-18-2023 17:20:21] <UkoeHB> so all the work is about studying and defining the distribution?`
`[01-18-2023 17:20:44] <Rucknium[m]> Wait. Did you mean the actual process of statistical estimation. I may have misunderstood`
`[01-18-2023 17:21:09] <UkoeHB> yeah I meant for monero implementation mainly`
`[01-18-2023 17:21:15] <rbrunner> The work for that somehwat elusive C++ dev maybe?`
`[01-18-2023 17:21:19] <Rucknium[m]> one-horse-wagon: These tasks won't get done: https://monerofund.org/projects/statistical_attack_reduction`
`[01-18-2023 17:22:11] <Rucknium[m]> Part of the selling point of OSPEAD is that it would remain parametric (the P in OSPEAD). So the actual change to the codebase would be small.`
`[01-18-2023 17:23:41] <Rucknium[m]> A very rough guess at the total number of C++ lines that would need to be written for tasks 1 - 3 there is...maybe 2k. But task 1 and 2 is mostly reading code.`
`[01-18-2023 17:24:15] <rbrunner> But I guess without 3 you are a bit in the dark how those few changed lines in the Monero codebase have to best look?`
`[01-18-2023 17:25:10] <UkoeHB> How do points 1 and 2 tie into 3, if the goal is an entirely new selection algorithm?`
`[01-18-2023 17:25:48] <UkoeHB> estimation of the real distribution via subtracting the artificial one(s)?`
`[01-18-2023 17:26:00] <Rucknium[m]> UkoeHB: The new selection algorithm is determined based on what's already on the chain, i.e. user behavior.`
`[01-18-2023 17:26:37] <Rucknium[m]> rbrunner: I don't quite understand your question`
`[01-18-2023 17:27:11] <rbrunner> 3 is "Program a fast C++ implementation of a statistical procedure that estimates Monero's real spend age distribution. "`
`[01-18-2023 17:27:13] <isthmus> @Rucknium[m] is there a reason that the analysis code needs to be in C++`
`[01-18-2023 17:27:28] <rbrunner> I guess without the result of that it's hard to adjust decoy selection in a really good way`
`[01-18-2023 17:27:31] <isthmus> Since it's not going into the Monero codebase?`
`[01-18-2023 17:27:46] <Rucknium[m]> No. It would be nice if it was in a fast language. C, Rust, even Fortran`
`[01-18-2023 17:28:20] <Rucknium[m]> I can write it in a scripting language, but that's slow. That's my plan now. Write it in R.`
`[01-18-2023 17:28:47] <hyc> Fortran might actually be most appropriate for the job...`
`[01-18-2023 17:29:32] <Rucknium[m]> It would be "nice" if it were a language that interfaces with R well like C, Fortran or C++. Maybe Rust does as well. It doesn't have to link to R though.`
`[01-18-2023 17:30:59] <Rucknium[m]> With a slow implementation, the estimate will not be as precise. And we will probably not have a good measure of how precise it is.`
`[01-18-2023 17:31:14] <isthmus> How would statistical performance depend on compute performance?`
`[01-18-2023 17:31:54] <Rucknium[m]> Statistical performance depends somewhat on items 1 - 2 in that list.`
`[01-18-2023 17:33:06] <isthmus> Oh I think we're talking about different things`
`[01-18-2023 17:33:11] <Rucknium[m]> Measurement of precision (i.e. confidence intervals or standard errors) would depend on performance since bootstrapping feasibility depends on compute performance.`
`[01-18-2023 17:34:54] <isthmus> Most of the serious "python libraries" are actually C/C++ engines with python bindings. pandas, numpy, etc. Does R have anything like that?`
`[01-18-2023 17:36:23] <Rucknium[m]> Same with R. C/Fortran/C++ under the hood. But there is a difference in getting under the hood vs being on top of it `
`[01-18-2023 17:37:11] <Rucknium[m]> If you write an explicit loop in a scripting language like R, then it's much slower than a vectorized operation that uses C under the hood.`
`[01-18-2023 17:37:17] <Rucknium[m]> I know how to write fast R code, but it definitely has limits.`
`[01-18-2023 17:39:00] <isthmus> "But there is a difference in getting under the hood vs being on top of it" hahaha yep. Going to borrow this analogy for design debates`
`[01-18-2023 17:40:08] <isthmus> I've had to explain this to people before but didn't have a good quip like this`
`[01-18-2023 17:41:10] <rbrunner> USD 48 collected on that MAGIC fundraiser, over 2 months, looks pretty bad.`
`[01-18-2023 17:42:38] <Rucknium[m]> Bootstrapping: Bootstrapping is taking a single statistical procedure and running it many times. Usually 100 at a minimum. Better if it is 1000+. It sounds like throwing things at a wall and hoping it sticks, but there is strong statistical theory for it , developed by Efron in the 1980's.`
`[01-18-2023 17:44:02] <Rucknium[m]> That's one reason why we might not get a measure of precision. I can write the code so that R can complete in reasonable time, but multiplied by 1000...that's a lot. The procedure itself is computationally expensive. Just the math.`
`[01-18-2023 17:45:33] <Rucknium[m]> Here are the only lines that probably will have to be changed in wallet2: https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L1003 ,  https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L144-L145`
`[01-18-2023 17:46:25] <Rucknium[m]> Change the distribution and define the values of the parameters of the new distribution.`
`[01-18-2023 17:47:05] <rbrunner> Maybe a somewhat pragmatic first attempt is needed, to get *something* better than now out of the door? So maybe it's 100x and some uncertaintly, but certainly better than today?`
`[01-18-2023 17:48:54] <Rucknium[m]> rbrunner: Yes. Not having fast code doesn't stop the project. It creates some blind spots. I will make it work with the resources that we have.`
`[01-18-2023 17:49:16] <rbrunner> Sounds promising.`
`[01-18-2023 17:49:35] <rbrunner> Now I understand better what you meant with "blind spots".`
`[01-18-2023 17:50:13] <isthmus> Is the process "embarrassingly parallel" ?`
`[01-18-2023 17:50:45] <rbrunner> So we could start "OSPEAD at home"? :)`
`[01-18-2023 17:52:37] <isthmus> I need a new screensaver`
`[01-18-2023 17:53:01] <Rucknium[m]> Bootstrapping is definitely embarassingly parallel. Completely independent runs.`
`[01-18-2023 17:53:47] <Rucknium[m]> And I have to split up the data anyway into weekly sets of data. And those procedures can run in parallel.`
`[01-18-2023 17:54:28] <Rucknium[m]> By "have to" I mean I need to understand what's happening over time. The estimation could take a whole year of data, but then I would just have the average.`
`[01-18-2023 17:56:41] <UkoeHB> We are approaching the end of the meeting, any last-minute questions or comments?`
`[01-18-2023 17:59:48] <UkoeHB> ok seems like we are done, thanks for attending everyone`

# Action History
- Created by: Rucknium | 2023-01-16T21:26:43+00:00
- Closed at: 2023-01-24T16:08:27+00:00
