---
title: Monero Research Lab Meeting - Wed 19 January 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/651
author: Rucknium
assignees: []
labels: []
created_at: '2022-01-18T17:17:38+00:00'
updated_at: '2022-01-24T01:58:40+00:00'
type: issue
status: closed
closed_at: '2022-01-24T01:58:40+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Revisit @tevador 's idea to record account indices in the tx, to improve robustness of output recovery: https://libera.monerologs.net/monero-research-lab/20211230 . Additional reading: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#gistcomment-4025357

3. Focus on Seraphis address schemes and hopefully reach some kind of decision (or get closer, maybe narrow down the choices to 2 or 3). [Schemes](https://github.com/monero-project/research-lab/issues/92) [@tevador proposal](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)

4. Adaptive CPU regulation for improved mining performance ( maxwellsdemon )

5. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

6. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

7. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

8. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

9. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

10. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

11. Any other business

12. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#649 

# Discussion History
## UkoeHB | 2022-01-19T18:08:07+00:00
```
[01-19-2022 17:01:27] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/651
[01-19-2022 17:01:27] <UkoeHB> 1. greetings
[01-19-2022 17:01:28] <UkoeHB> hello
[01-19-2022 17:01:42] <localmonero05> Greetings.
[01-19-2022 17:01:49] <rbrunner> Hi there
[01-19-2022 17:01:52] <Rucknium[m]1> Hi
[01-19-2022 17:02:20] <mj-xmr[m]> Hi hi
[01-19-2022 17:03:37] <jberman[m]> hi hi hi
[01-19-2022 17:03:50] <mj-xmr[m]> for (int ...
[01-19-2022 17:03:56] <mj-xmr[m]> ehm.... sorry.
[01-19-2022 17:05:31] <UkoeHB> 2. Does anyone want to give updates? What has everyone been working on?
[01-19-2022 17:05:31] <UkoeHB> Myself: I haven't done much with Monero the past week. I am trying to improve at software design so when I dive into the seraphis/jamtis wallet poc I can knock it out in one go without deep revisions.
[01-19-2022 17:06:38] <mj-xmr[m]> I'm having success with my time series prediction software. Let me quickly repost:
[01-19-2022 17:06:47] * mj-xmr[m] uploaded an image: image.png
[01-19-2022 17:06:55] <mj-xmr[m]> This is how this looks before the training. The blue line is the true value and the green one is the predicted value.
[01-19-2022 17:06:55] <mj-xmr[m]> After a short training:
[01-19-2022 17:07:13] * mj-xmr[m] uploaded an image: image.png
[01-19-2022 17:07:17] <mj-xmr[m]> Almost 30% better than the baseline prediction.
[01-19-2022 17:07:23] <mj-xmr[m]> (in-sample)
[01-19-2022 17:07:29] <mj-xmr[m]> Out of sample (2 months later):
[01-19-2022 17:07:35] * mj-xmr[m] uploaded an image: image.png
[01-19-2022 17:07:41] <mj-xmr[m]> Still didn't loose much of the relative performance
[01-19-2022 17:07:47] <mj-xmr[m]> Which means, that you don't have to retrain it very often
[01-19-2022 17:07:59] <Rucknium[m]1> Me: Not much Monero-specific work from me this past week either. I hope to dive back into revising the OSPEAD technical specification for a lay audience next week. Again, if anyone would like to see the current version, just PM me and I will send it along.
[01-19-2022 17:08:18] <mj-xmr[m]> Not to take too much time right now, if somebody has questions, I can answer later.
[01-19-2022 17:08:38] <Rucknium[m]1> mj-xmr: What is the time series value you are forecasting?
[01-19-2022 17:08:40] <UkoeHB> mj-xmr[m]: can you remind us what you want to do with this software?
[01-19-2022 17:09:12] <mj-xmr[m]> The highs of the total transaction numbers for the given hourly sample
[01-19-2022 17:09:31] <mj-xmr[m]> Which means, that on average you'd expect there to be that many transactions.
[01-19-2022 17:09:57] <mj-xmr[m]> If not, you know how much you have to decoy.
[01-19-2022 17:10:07] <mj-xmr[m]> s/not/the number is below/
[01-19-2022 17:10:54] <rbrunner> I did tests with jberman[m] 's view tag PR branch; everything ran flawlessly. It's now running live as "Technet" here: https://monerotech.info/Wallet
[01-19-2022 17:11:08] <rbrunner> Code review however is still missing, despite a bounty of over 20 XMR ...
[01-19-2022 17:11:28] <mj-xmr[m]> UkoeHB: The software itself shows what model has the best chance to work. It's expected then to rather extract the model from the conglomerate and use it as a class of itself INSIDE monero.
[01-19-2022 17:11:48] <mj-xmr[m]> This will also help avoid any licensing issues.
[01-19-2022 17:11:58] <Rucknium[m]1> So basically we can pair this with the Seraphis performance tests and perhaps estimates of low-end hardware performance to get a sense of where we may be hitting a "danger zone" for computational expense.
[01-19-2022 17:12:07] <mj-xmr[m]> s/avoid/avoiding/
[01-19-2022 17:13:02] <mj-xmr[m]> This too. In fact you can plugin anything that changes across time. If there are predictable patterns in the series, it will immediately let you know.
[01-19-2022 17:14:01] <localmonero05> FYI, the images you uploaded come through as image.png, not even a clickable link on IRC side. mj-xmr[m]
[01-19-2022 17:14:23] <mj-xmr[m]> localmonero05: Thanks. Lemme correct.
[01-19-2022 17:14:42] <localmonero05> It is probably bridge's fault, not yours...
[01-19-2022 17:15:06] <localmonero05> Don't know whether you should try imgur or whatever else, individually. Seems time consuming. But if you can and want to, by all means.
[01-19-2022 17:15:10] <UkoeHB> they are visible in matrix
[01-19-2022 17:15:24] <localmonero05> Yes, precisely why I emphasize IRC side, not Matrix side.
[01-19-2022 17:17:14] <mj-xmr[m]> http://cryptog.hopto.org/monero/sim/01-untrained.png
[01-19-2022 17:17:14] <mj-xmr[m]> http://cryptog.hopto.org/monero/sim/02-in-sample.png
[01-19-2022 17:17:14] <mj-xmr[m]> http://cryptog.hopto.org/monero/sim/03-out-of-sample.png
[01-19-2022 17:17:14] <jberman[m]> thank you for that rbrunner :)
[01-19-2022 17:17:29] <rbrunner> Welcome :)
[01-19-2022 17:17:50] <localmonero05> Perfect! Thanks.
[01-19-2022 17:18:12] <UkoeHB> It seems there are a number of PRs stuck needing more review. It might be unreasonable to expect vtnerd to cover all these. If we had 1 or 2 more people able to review the big tough PRs that would help a lot.
[01-19-2022 17:18:15] <rbrunner> Can we have that as a t-shirt?
[01-19-2022 17:18:16] <Rucknium[m]1> The MAGIC Monero Fund committee plans to have its first meeting on Friday. If you have any input into how the grants process should work (or plan to submit a grant application yourself!) please let me or someone else on the committee know:
[01-19-2022 17:18:22] <Rucknium[m]1> https://www.reddit.com/r/Monero/comments/s31glu/welcome_the_new_magic_monero_fund_committee/
[01-19-2022 17:18:45] <localmonero05> Nice Rucknium[m]1.
[01-19-2022 17:18:50] <Rucknium[m]1> I am aware of at least one research grant application that is probably coming down the pipeline.
[01-19-2022 17:19:16] <rbrunner> It does start to look like the beginning of a review crisis ...
[01-19-2022 17:19:23] <localmonero05> UkoeHB: Has Rucknium[m]1's idea re: seeking talent for Monero activities bear any fruits yet? As in, any possible candidates to help vtnerd review PRs?
[01-19-2022 17:19:39] <Rucknium[m]1> Note that grant recipients must do KYC since MAGIC is a nonprofit organization registered with the U.S. tax agency.
[01-19-2022 17:20:08] <localmonero05> Damned KYC...
[01-19-2022 17:20:29] <mj-xmr[m]> rbrunner: Unfortunately I can't help with the strictly cryptography related stuff. I coop with selsta and others at GUI on more IT-related stuff.
[01-19-2022 17:20:46] <UkoeHB> I have seen wernervasquez[m] and dr_overdose[m] seem to have a grasp/interest in the deeper protocol details, however idk if they are interested and able to review PRs.
[01-19-2022 17:20:59] <rbrunner> Same problem for me. That stops me from reviewing the complete view tags PR.
[01-19-2022 17:21:20] <localmonero05> Hopefully one or both can lend a hand to vtnerd then.
[01-19-2022 17:22:29] <UkoeHB> wfaressuissia is certainly qualified, but does not seem available for PR reviewing
[01-19-2022 17:23:33] <Rucknium[m]1> localmonero05: The short answer is no. However, according to my criteria, no "active recruitment" has yet been done. The Reddit post was just a starting point. Once I get through more of my TODO list I will return to it.
[01-19-2022 17:23:49] <localmonero05> Rucknium[m]1: Sounds good. Thanks.
[01-19-2022 17:24:28] <Rucknium[m]1> I haven't been following the PRs on GitHub, but can kayabanerve  help?
[01-19-2022 17:24:43] <UkoeHB> Honestly it takes a lot of time, effort, and learning to really get into any of these PRs. A difficult problem
[01-19-2022 17:25:03] <rbrunner> Definitely.
[01-19-2022 17:26:01] <Rucknium[m]1> UkoeHB: Yes exactly. We need a long pipeline to bring in talent. As in, investing in recruitment now will pay off in several months or even a year.
[01-19-2022 17:26:45] <rbrunner> Especially when *tons* of new code will get written for the switch to Seraphis, all needing review.
[01-19-2022 17:26:49] <localmonero05> Pressing issue is, hard to find mathematicians, cryptographers, or coders who are actually interested in learning the ropes of XMR, no?
[01-19-2022 17:27:22] <localmonero05> Besides allocating funds for recruitment of experts, it should also have some monies for the right person to shill the project, to entice them. Ha.
[01-19-2022 17:27:58] <mj-xmr[m]> Yes, it does require a lot of skills in one go. I myself have proposed an ambitious friend but she gave it up.
[01-19-2022 17:28:01] <Rucknium[m]1> localmonero05: Yes. I think they are out there, but they don't know about Monero, or they know about Monero vaguely but don't know that their skills could be of use. Or they need better funding options.
[01-19-2022 17:28:02] <localmonero05> Many infosec, et. al. people look down on cryptocurrencies, generally speaking.
[01-19-2022 17:28:47] <localmonero05> Correct. MAGIC might aid that situation, since some may be looking for just fiat retribution for their work, and not be concerned re: KYC procedures. Agreed.
[01-19-2022 17:30:57] <Rucknium[m]1> And don't forget that there are researchers writing about Monero right now and publishing papers, but they are not within the Monero Project infrastructure. So we could go to them first.
[01-19-2022 17:31:30] <rbrunner> By the way, there was an idea from last September or so to make a code freeze for the next hardfork on ... drum roll ... January 16 :)
[01-19-2022 17:31:30] <localmonero05> Such as? Any examples? Just curious.
[01-19-2022 17:32:22] <localmonero05> rbrunner: this one? https://github.com/monero-project/meta/issues/630
[01-19-2022 17:32:51] <localmonero05> https://github.com/monero-project/meta/issues/630#issuecomment-1013027880
[01-19-2022 17:33:04] <rbrunner> Right.
[01-19-2022 17:33:18] <localmonero05> Should we hold a -dev meeting, or something? Cc. luigi1112, selsta, binaryFate.
[01-19-2022 17:33:41] <rbrunner> May be in order, yes.
[01-19-2022 17:33:54] <UkoeHB> In any case, if there is anyone out there lurking who is enthusiastic about the protocol details and wants to make sure it is implemented correctly, we need you :). We don't urgently need code writers so much as people who can make sure the code is solid (and help improve code proposals).
[01-19-2022 17:34:12] <localmonero05> Aye, PR reviewers.
[01-19-2022 17:34:24] <selsta> everything for the multisig fixes is PRed now, just need a final approval
[01-19-2022 17:34:31] <ArticMine[m]> Yes We need some follow up on the HF
[01-19-2022 17:34:57] <Rucknium[m]1> localmonero05: I really hate to use Google, but this is easiest. Here are Monero papers with publication dates of this year:
[01-19-2022 17:34:59] <Rucknium[m]1> https://scholar.google.com/scholar?as_ylo=2022&q=Monero
[01-19-2022 17:35:11] <localmonero05> Copy that. Thanks for sharing.
[01-19-2022 17:35:31] <localmonero05> ArticMine[m]: Do you suggest a dev meeting to discuss HF topics?
[01-19-2022 17:35:57] <localmonero05> selsta: Do we need reviewers for such PRs, or should luigi just merge?
[01-19-2022 17:36:01] <Rucknium[m]1> Obviously, not all those papers are super relevant, but many of them are.
[01-19-2022 17:36:10] <ArticMine[m]> Yes
[01-19-2022 17:36:31] <selsta> localmonero05: they are reviewed for the large part, just final approval is missing
[01-19-2022 17:36:36] <localmonero05> Roger that. I'll follow up in -dev later today, to see what date and time is most convenient for everyone. Thanks ArticMine[m].
[01-19-2022 17:36:38] <selsta> ideally they final approval comes from the reviewer
[01-19-2022 17:36:51] <localmonero05> Got it.
[01-19-2022 17:38:03] <jberman[m]> UkoeHB: FWIW I don't have the deep math expertise yet (view tags were pretty simple), but I'm working on building it and am very enthusiastic about protocol details and want to see them implemented correctly. The time and effort for me to train to get to a point of being able to offer a very high quality review to spot issues in the math of the deeper crypto changes (like with multisg + BP+) is fairly large for where I am right
[01-19-2022 17:38:03] <jberman[m]> now, but I'm working on it
[01-19-2022 17:38:46] <UkoeHB> jberman[m]: great :) I am looking forward to it
[01-19-2022 17:39:10] <rbrunner> That's the spirit.
[01-19-2022 17:39:23] <mj-xmr[m]> That's the spirit!
[01-19-2022 17:40:37] <ArticMine[m]> Excellent
[01-19-2022 17:43:33] <UkoeHB> Moving on. I think tevador's jamtis is in a ~final state (maybe only some semantic changes left). Now would be a great time for people to read it over and leave your thoughts. Especially those who already gave feedback, like rbrunner and localmonero05 and jberman[m] .
[01-19-2022 17:43:58] <UkoeHB> link: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024
[01-19-2022 17:46:00] <Rucknium[m]1> hermestris from #monero-recruitment:monero.social  said that they have work experience managing commercial payment processing, so hopefully they could offer their opinions as well, with respect to merchant-side issues.
[01-19-2022 17:48:29] <tevador> Sorry for being late. I'm not expecting major changes to Jamtis anymore. The only thing that might take some effort is finding a suitable BCH polynomial for the checksum, but that's a rather minor thing for the specs. 
[01-19-2022 17:50:23] <rbrunner> If we really can pull this off we will miles ahead of other coins ...
[01-19-2022 17:50:43] <rbrunner> As in: Implement it as working code and hardfork
[01-19-2022 17:51:48] <mj-xmr[m]> Sorry to intervene once more, but for the completeness sake: The prediction model can also make it easier to detect spam. Look at the right hand of this time window. You can clearly and objectively (= automatically) say, that there was a spam effort.
[01-19-2022 17:51:48] <mj-xmr[m]> http://cryptog.hopto.org/monero/sim/03-out-of-sample.png
[01-19-2022 17:51:59] <UkoeHB> Idk about miles ahead, afaik Firo's upgrade will have similar features.
[01-19-2022 17:53:01] <UkoeHB> Is it a spam effort or just someone who wants to make a bunch of txs?
[01-19-2022 17:53:01] <rbrunner> Interesting. Competition can bring motivation.
[01-19-2022 17:54:04] <UkoeHB> (distinction without a difference?)
[01-19-2022 17:54:06] <mj-xmr[m]> UkoeHB: Essentially the same. Even if for legit purposes, if overloads the network.
[01-19-2022 17:54:50] <Rucknium[m]1> mj-xmr: We'd want to combine this with a monitoring system based on the "Fingerprinting a Flood" research, which has many metrics to examine.
[01-19-2022 17:54:59] <ArticMine[m]> What about scaling in Firo?
[01-19-2022 17:55:28] <UkoeHB> Scaling?
[01-19-2022 17:56:14] <ArticMine[m]> I believe we're well ahead
[01-19-2022 17:56:41] <UkoeHB> What are you referring to exactly?
[01-19-2022 17:57:28] <ArticMine[m]> Ability to scale on chain
[01-19-2022 17:57:44] <ArticMine[m]> As technology improves
[01-19-2022 17:57:54] <UkoeHB> Oh
[01-19-2022 17:58:51] <UkoeHB> Well, we are at the end of the hour so I'll call the meeting here. Thanks for attending everyone
[01-19-2022 17:59:05] <mj-xmr[m]> TY everybody.
[01-19-2022 17:59:18] <ArticMine[m]> Thanks
[01-19-2022 17:59:19] <localmonero05> Thanks, all.
[01-19-2022 17:59:25] <w[m]> Thanks 
[01-19-2022 17:59:27] <localmonero05> UkoeHB: Same day, same hour next week?
[01-19-2022 17:59:41] <localmonero05> s/hour/time
[01-19-2022 18:00:29] <UkoeHB> yes
```

# Action History
- Created by: Rucknium | 2022-01-18T17:17:38+00:00
- Closed at: 2022-01-24T01:58:40+00:00
