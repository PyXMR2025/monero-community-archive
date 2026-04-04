---
title: Monero Research Lab Meeting - Wed 21 June 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/851
author: Rucknium
assignees: []
labels: []
created_at: '2023-06-16T22:20:17+00:00'
updated_at: '2023-07-05T00:33:41+00:00'
type: issue
status: closed
closed_at: '2023-07-05T00:33:41+00:00'
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

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#849 

# Discussion History
## plowsof | 2023-06-28T17:43:44+00:00
Logs 
```
17:00:56 <Rucknium[m]> 1) Greetings....who is here?

17:00:59 <vtnerd_> hi

17:01:10 <rbrunner> Hello

17:02:25 <Rucknium[m]> 2) Updates. What is everyone working on?

17:03:28 <Rucknium[m]> Working on OSPEAD things (something to discuss today). Dr. Borggren's research project
to analyze the EAE attack and churning has been fully funded:
https://monerofund.org/projects/eae_attack_and_churning

17:03:57 <rbrunner> Nice

17:05:09 <vtnerd_> zmq/rmq stuff for LWS, and some small work on bp++. If the paper audit doesn't provide me
with more helpful equations, I may have to try and port the C version

17:05:53 <vtnerd_> they seem to deviate from the naming schema in their one doc, so its annoying :/

17:06:58 <Rucknium[m]> 3) Discussion

17:07:29 <xmrack[m]> Hi

17:07:38 <Rucknium[m]> We have limited attendance due to MoneroKon, so this conversation can continue into
next week. To get the conversation started: I am setting up the parameters for the "validation" Monte Carlo
simulations to recover the real spend age distribution.

17:07:41 <Rucknium[m]> I argue that OSPEAD is consistent. Consistency is an asymptotic property, i.e. the
behavior of the estimator as sample size approaches infinity. Since sample size is finite, we want to make
sure that our sample size is adequate for the task.

17:08:21 <Rucknium[m]> I want to have one main "validation" set of parameters so I can test sample sizes and
adjustments. Just change those things instead of changing parameters. When the parameters change, the target
also changes, so it can get hard to compare things.

17:08:39 <Rucknium[m]> My "draft" now is:

17:08:55 <Rucknium[m]> There are three Decoy Selection Algorithms (DSAs):

17:09:09 <Rucknium[m]> 1) "wallet2". Log-gamma, shape = 19.28, rate = 1.61. 80% of rings will be constructed
with this DSA.

17:09:19 <Rucknium[m]> 2) "unknown DSA #1". Log-triangular, min = 20 minutes, max = 1 year, mode = 1 week. 15%
of rings.

17:09:32 <Rucknium[m]> 3) "unknown DSA #2". Uniform, min = 20 minutes, max = 1 year. 5% of rings.

17:09:39 <Rucknium[m]> The real spend age distribution is the empirical distribution of Litecoin, 10th week of
2022, shifted 20 minutes to match the 10 block lock.

17:10:05 <Rucknium[m]> I plot their cumulative distribution functions here:
https://github.com/Rucknium/OSPEAD/blob/main/images/draft-validation-monte-carlo.png

17:11:16 <Rucknium[m]> The objective is to get a close estimate of the "real spend", which is litecoin. If
OSPEAD gets a close estimate, then "we ship it".

17:11:59 <Rucknium[m]> Of course we don't know the true Monero real spend...that's what we are trying to
estimate in the first place.

17:12:59 <vtnerd_> so I guess litecoin was thought to be a better model than bitcoin?

17:13:04 <Rucknium[m]> Actually, I already ran OSPEAD on these parameters and it does a pretty good job with
200,000 rings as sample size, which is about a week of blockchain data

17:13:11 <xmrack[m]> I reached out to the authors of the constant time and size range proof for an update and
they said.... (full message at
<https://libera.ems.host/_matrix/media/v3/download/libera.chat/4b77afda845b8b5197d494b314e439b5945e66b7>)

17:14:41 <Rucknium[m]> vtnerd_:  Yes. Bitcoin has full blocks and higher fees. LTC matches Monero closer in
that respect. And block discovery interval time. We could try bitcoin too. Probably the outcome would not be
much different.

17:15:00 <Rucknium[m]> xmrack: Thanks!

17:16:04 <Rucknium[m]> I'm not sure what I should do about the fact that LTC outputs can be spent in the same
block they are confirmed in. That alone accounts for about 8% of spent outputs.

17:16:43 <Rucknium[m]> I shift it 20 minutes to be like Monero, but I don't think 8% of Monero outputs are
spent as soon as the 10 block lock expires.

17:17:01 <rbrunner> With "pretty good job", does that mean that your new OSPEAD algorithm comes close to that
LTC curve? Or something else altogether that I may not understand with my rudimentary knowledge about
statistics

17:17:28 <Rucknium[m]> I could just eliminate all LTC spent outputs that are spent in the sample block as
created.

17:18:17 <Rucknium[m]> rbrunner: Yes. So if it comes close to LTC, which is known, then t will come close to
XMR, which is unknown. We can measure how close it comes to LTC since we actually have the LTC real spends.

17:18:55 <Rucknium[m]> it will*

17:19:22 <rbrunner> So on a high and abstract level, it's something like "Given a curve, search for a formula
that comes close"?

17:19:46 <Rucknium[m]> Extremely high level, yes

17:19:52 <rbrunner> Yeah, thought so :)

17:20:16 <Rucknium[m]> Data is constructed just like the Monero blockchain

17:20:18 <rbrunner> But at least that gives me a hint how to think about it, in broad terms :)

17:20:19 <Rucknium[m]> For one ring:

17:21:06 <Rucknium[m]> I determine what DSA I will use. It's 80% wallet2, 15% unknown #1, 5% unknown #2. This
is to take into account  that mulitiple DSAs are in the wild.

17:22:16 <Rucknium[m]> It's it's wallet2, then I randomly and independently select 15 decoys from the log-
gamma distribution. Then I select one real spend from the LTC distribution. Those 16 random draws form a ring

17:22:51 <Rucknium[m]> Then I do that 200,000 more times to form 200,000 rings.

17:23:09 <Rucknium[m]> Then I run OSPEAD on it to recover the LTC distribution

17:24:57 <Rucknium[m]> I don't directly give it the LTC distribution since there is nothing like that on the
Monero blockchain. We don't know which ring members are real spends.

17:25:33 <rbrunner> Just curious, are your tools fast enough now for these simulations, so run times do not
drag you down too much?

17:27:19 <Rucknium[m]> It would be good to have a faster implementation. I am working on that. Now it takes
about 10 minutes on 200 CPU threads for a single iteration. You want 10-100 iterations for Monte Carlo
simulations if you are being not very rigorous. More if being rigorous.

17:28:02 <Rucknium[m]> I have to vary sample size, adjust certain things again to test how the estimator
reacts, of course.

17:28:12 <Rucknium[m]> That's with about 200,000 rings

17:28:27 <rbrunner> Interesting, thanks

17:35:37 <Rucknium[m]> If anyone has an opinion about which distribution distance metric would be best for the
distance between the LTC distribution and its OSPEAD estimate, please me know. For now I am using the
Kolmogorov-Smirnov distance since it is convenient, but I am open to using something else.

17:35:38 <Rucknium[m]> Anything else to discuss?

17:36:43 <rbrunner> Not from me, also going to pack for MoneroKon now ...

17:39:31 <Rucknium[m]> We can end the meeting here.


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-06-16T22:20:17+00:00
- Closed at: 2023-07-05T00:33:41+00:00
