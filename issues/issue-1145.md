---
title: Monero Research Lab Meeting - Wed 22 January 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1145
author: Rucknium
assignees: []
labels: []
created_at: '2025-01-21T20:23:17+00:00'
updated_at: '2025-01-30T19:43:02+00:00'
type: issue
status: closed
closed_at: '2025-01-30T19:43:02+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Prize contest to optimize some FCMP cryptography code.

4. Some preliminary results from [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) research into improved decoy selection algorithm.

5. Research on [Autonomous System (AS) peer connection rules](https://github.com/monero-project/monero/pull/7935) to reduce spy node risk.

6. Any other business

7. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1142 

# Discussion History
## chaserene | 2025-01-22T02:41:07+00:00
date-agnostic alternative time zone calculator (works regardless of daylight saving time shifts):
https://www.timeanddate.com/worldclock/meeting.html?p1=1440

## Rucknium | 2025-01-23T19:09:30+00:00
Logs

> __< r​ucknium:monero.social >__ MRL meeting in this room in two hours.     

> __< s​yntheticbird:monero.social >__ The legend once said that it was meeting time...     

> __< rbrunner >__ Indeed     

> __< s​yntheticbird:monero.social >__ 1. Greetings (unofficial)     

> __< j​berman:monero.social >__ *waves*     

> __< rbrunner >__ Here :)     

> __< s​yntheticbird:monero.social >__ hello     

> __< a​rticmine:monero.social >__ Hello     

> __< c​haser:monero.social >__ hello     

> __< s​yntheticbird:monero.social >__ 2. Updates. What is everyone working on?     

> __< b​oog900:monero.social >__ ping Rucknium     

> __< s​yntheticbird:monero.social >__ Rucknium:     

> __< j​effro256:monero.social >__ Howdu     

> __< s​yntheticbird:monero.social >__ I propose if rucknium isn't there at :10 we run a wheel to decide who is moderator     

> __< 0​xfffc:monero.social >__ Hi everyone. I am off. But I will be reading the meeting silently.     

> __< j​effro256:monero.social >__ Me: PR reviews and improving the Carrot library flow     

> __< c​haser:monero.social >__ SyntheticBird: you've already assumed that role :)     

> __< s​yntheticbird:monero.social >__ alright if you insist chaser \* proceed to act shy \*     

> __< a​rticmine:monero.social >__ I have been working on scaling algorithm  for FCMP. The consensus part is done. I am working on the fee part     

> __< a​rticmine:monero.social >__ Reviewing the BCH scaling algorithm.     

> __< a​rticmine:monero.social >__ I am also reading Highjacking  Bitcoin. Many assumptions there on both sides     

> __< j​berman:monero.social >__ me: updated the FCMP++ WIP PR with the latest (includes wallet sync, improved tree build time, and a demo of calling prove/verify over the FFI. latest builds passing with tobtoht's help): https://github.com/monero-project/monero/pull/9436     

> __< s​yntheticbird:monero.social >__ 3. Prize contest to optimize some FCMP cryptography code.     

> __< s​yntheticbird:monero.social >__ jberman:     

> __< s​yntheticbird:monero.social >__ (tell me if im switching too quickly)     

> __< j​berman:monero.social >__ good pace to me :)     

> __< j​berman:monero.social >__ A list of tasks todo for the contest:     

> __< j​berman:monero.social >__ 1) Write a test suite for the competition     

> __< j​berman:monero.social >__ 2) Finalize contest specs/details     

> __< j​berman:monero.social >__ 3) Decision on where to host the competition     

> __< j​berman:monero.social >__ 4) How to accept submissions? (private or public)     

> __< j​berman:monero.social >__ 5) Decision on how to raise funds     

> __< j​berman:monero.social >__ 6) Who to get involved to judge the final submissions      

> __< j​berman:monero.social >__ 7) Decide on timeline/dates     

> __< j​berman:monero.social >__ 8) Plan to attract talent     

> __< j​berman:monero.social >__ Starting with 1, I'm happy to take a stab at this and will try to have a test suite ready by next MRL meeting (unless any takers want to give it a go)     

> __< j​berman:monero.social >__ I figure we can discuss some of these details today, like 3/4/5     

> __< j​berman:monero.social >__ On where to host the contest, could be as simple as a github repo, or create a new website. The latter would take more effort but would be nice to have in attracting talent. Here was a comparable contest site kayaba linked in a past meeting: https://www.zprize.io/     

> __< rbrunner >__ Regarding 3): Maybe it's not glorious at all, but for exchanging info, progress reports, a simple GitHub issue could do     

> __< rbrunner >__ Why a whole repo? So people can submit their code there?     

> __< j​berman:monero.social >__ Ya, the repo could host the test suite as well, it would be clear how to submit code to win the contest by cloning the repo     

> __< rbrunner >__ Alright     

> __< j​berman:monero.social >__ ah I should also link kayabanerve 's exisitng draft repo for the contest: https://github.com/kayabaNerve/fcmp-plus-plus-optimization-competition/tree/main     

> __< j​berman:monero.social >__ Can start from there     

> __< j​effro256:monero.social >__ As for 4, if we're using something like a Github repo, we need to make sure that as the contestants are pushing code, that they can't see the others' code, so we prevent plagiarism     

> __< s​yntheticbird:monero.social >__ Re 3): a website would only possible if people are available to make it (i'm not sorry), would need to ask at monero-website.     

> __< s​yntheticbird:monero.social >__ Re 4): Allowing anonymous submission is always preferable.     

> __< plowsof >__ having the code private - but confirmed test results public would prevent someone from running the attempt through an LLM and submitting a slightly different variation under an alias to claim any runner up prizes      

> __< s​yntheticbird:monero.social >__ Re 5): CCS as always?     

> __< plowsof >__ although the people who submit attempts could still do that :)      

> __< j​berman:monero.social >__ ya, the runner up part seems tricky since it leaves room for gaming     

> __< j​berman:monero.social >__ private submissions could be a patch to the repo submitted privately to an email     

> __< rbrunner >__ A website for 3) would be cool, but well, we can't even move our "New GetMonero.org" forward, so ...     

> __< j​berman:monero.social >__ anon submissions definitely should be allowed imo too     

> __< j​berman:monero.social >__ repo sounds fine to me     

> __< Rucknium >__ Hi! Sorry. Had unexpected problems.     

> __< rbrunner >__ I think "making noise" in the right circles for the contest could be much more important than some nice website     

> __< s​yntheticbird:monero.social >__ Hi Rucknium, we were at 3.     

> __< j​berman:monero.social >__ anyone against a repo?     

> __< a​rticmine:monero.social >__ Sounds to me like a reasonable approach     

> __< s​yntheticbird:monero.social >__ same     

> __< j​berman:monero.social >__ great     

> __< j​berman:monero.social >__ anyone against private submissions via patch via email, feel free to speak up :)     

> __< rbrunner >__ GitHub doesn't offer something there? Private repos that you can open for select persons?     

> __< rbrunner >__ Maybe even if, too complicated     

> __< j​berman:monero.social >__ so contestants fork the repo, keep their fork private and share with judge(s)     

> __< j​berman:monero.social >__ seems reasonable. either would work     

> __< j​berman:monero.social >__ on the decision to raise funds, there is also the general fund which ofrnxmr has voiced reasoning to utilize in the past. figure it's worth discussion compared to a CCS     

> __< rbrunner >__ Hmm, maybe a CCS could already be a part of "making noise"     

> __< s​yntheticbird:monero.social >__ If Core is willing to give GF should be better.     

> __< s​yntheticbird:monero.social >__ rbrunner not sure, people external to monero may not care about CCS.     

> __< rbrunner >__ Do we already have an idea of the sum that we might offer?     

> __< s​yntheticbird:monero.social >__ it will just be a "Look we're crowdfunding our super context"     

> __< s​yntheticbird:monero.social >__ contest*     

> __< s​yntheticbird:monero.social >__ From the repo:      

> __< s​yntheticbird:monero.social >__ > The best submission for an optimized helioselene will be awarded 50 XMR. The second best submissions will be awarded 25 XMR.     

> __< s​yntheticbird:monero.social >__ > The best solution for an optimized ec-divisors will be awarded 150 XMR. The second best submission will be awarded 75 XMR.     

> __< rbrunner >__ That's a bit at the low end if you ask me ... If I compare how much we paid for specialist time for reviews and audits     

> __< j​effro256:monero.social >__ Agreed     

> __< rbrunner >__ Although it's always sooo easy to spend other peoples' money :)     

> __< s​yntheticbird:monero.social >__ i'm sure general fund will do just fine     

> __< j​berman:monero.social >__ How about 500 XMR for ec divisors 1st place (close to $100k), 200 XMR for helioselene 1st place? kayaba likely has greatest context into amount of work it might take for participants, so this is a bit stabbing in the dark. But it's also a fairly important element we very much so want to see optimized     

> __< j​berman:monero.social >__ also, 2nd place getting half is definitely a lot when 2nd place could potentially be gamed by 1 participant with anon submissions     

> __< rbrunner >__ If the GF can fund that, why not.     

> __< c​haser:monero.social >__ if needed, I'm sure a CCS could fill in a funding gap. last year's CCS's proved that the community is more than willing to fund efforts to make FCMP++ succeed. we even had a private actor step up and fund research outside the CCS.     

> __< j​berman:monero.social >__ it seems there is some rough support to request the GF to fund (or help fund) the contest as well. we can let that marinate until next week     

> __< s​yntheticbird:monero.social >__ Perfect     

> __< j​effro256:monero.social >__ How much XMR is estimated to be left over from the FCMP++  research fund?     

> __< s​yntheticbird:monero.social >__ 4. Some preliminary results from [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) research into improved decoy selection algorithm.     

> __< s​yntheticbird:monero.social >__ Rucknium     

> __< Rucknium >__ Attack success = correctly guessing the real spend in the ring.     

> __< Rucknium >__ Recall that the theoretical minimum attack success through completely random guessing would be 1/16 = 6.25%     

> __< Rucknium >__ According to my estimates, an adversary could take advantage of the divergence between the real spend age distribution and the status quo decoy distribution to achieve an attack success probability of 23.5%, on average, since the August 2022 hard fork. This corresponds to an effective ring size of 4.2     

> __< Rucknium >__ With a new improved, fitted decoy distribution, we can get that probability down to 7.6 percent, corresponding to an effective ring size of 13.2     

> __< Rucknium >__ What is the relevance of this after FCMP activation? There will be a _backup_ method to construct FCMP txs that requests the FCMP Merkle tree paths as a set of decoys from a (potentially spying) remote node. So this distribution can be used for that.     

> __< Rucknium >__ I will probably publicly release all OSPEAD-related documents and code around February 20.     

> __< Rucknium >__ At least one thing that I could use wider feedback on is how quickly do we think the ecosystem implemented the off-by-one patch. I tried to measure it statistically, but I got unsatisfactory results because the difference between the patched and unpatched distributions is so small.     

> __< Rucknium >__ However, it is important to get it right since it affects the real spend estimate of the youngest spendable block, which is probably the most common block to spend from.     

> __< Rucknium >__ Right now I just assume a linear trend from the date of release of the patch to the end of the dataset (now October 2024), assuming 75% adoption by the end.     

> __< c​haser:monero.social >__ 4.2? damn. is that attack viable today? and what does such an attack take to execute?     

> __< Rucknium >__ Yes, continues to be viable. Some weeks it would be even more efefctive, some weeks less. Depends on what the real spend age distribution is each week.     

> __< Rucknium >__ To execute the attack you need an estimate of the real spend age distribution     

> __< a​rticmine:monero.social >__ There is also the possibility of combining this with clustering algorithms     

> __< c​haser:monero.social >__ alright, but how does an adversary arrive at a good estimate of the real spend age distribution?     

> __< Rucknium >__ The larger the divergence between the real spend age distribution and the decoy distribution, the higher the attack success probability.     

> __< s​yntheticbird:monero.social >__ jeffro256: according to CCS repo there is 1537 XMR left     

> __< s​yntheticbird:monero.social >__ (continue on ospead)     

> __< Rucknium >__ Through the techniques I developed in the OSPEAD research     

> __< c​haser:monero.social >__ Artic: feel free to expand on clustering algorithms     

> __< a​rticmine:monero.social >__ The best example is the leaked Chainalysis video     

> __< Rucknium >__ This is why the estimate of the real spenddistribution is a double-edged sword. It would allow you to set a better decoy distribution, but it also allows an adversary to attack user privacy.     

> __< Rucknium >__ The attack sucess estimate I quoted is about single-ring attack effectiveness. When a tx has multiple rings, the correlations between them can be leveraged.     

> __< c​haser:monero.social >__ Rucknium: I see. and this potential attack will become publicly viable, retroactively, when OSPEAD is published, right?     

> __< j​berman:monero.social >__ "according to CCS repo there is 1537 XMR left" -> working on an estimate for how much we expect to be leftover after all tasks completed     

> __< Rucknium >__ There's a paper on MoneroResearch.info by Borggren about the inter-ring correlations.     

> __< Rucknium >__ chaser: yes     

> __< a​rticmine:monero.social >__ The co spend heuristic was used to overcome ring signatures of 16. The cluster has to be larger than the effective ring size. If one lowers the effective ring size to say 5 then the cluster size needed is much lower     

> __< Rucknium >__ In fact it would not be difficult for me to write a bit of code to try to guess the real spend in all rings since August 2022     

> __< rbrunner >__ What's the importance of the August 2022 hardfork? Just the start date of your investigation? Or something "wrong" since only that?     

> __< Rucknium >__ Just the start date     

> __< Rucknium >__ that jberman implemented     

> __< Rucknium >__ No good reason to go back further than that, but you could     

> __< Rucknium >__ It took about two weeks of computation time to do the two years of data     

> __< Rucknium >__ On a 64 thread machine     

> __< rbrunner >__ Hmm, wouldn't several decoy selection algorithms in use make things *more* difficult for an adversary?     

> __< Rucknium >__ And that's after I sped up one of the main steps by 240x compared to the original implementation :D     

> __< j​effro256:monero.social >__ Perhaps going back further, when ring size was small, would help the more recent results, since one could eliminate very old decoys from new rings when the spend is known-ish?     

> __< Rucknium >__ rbrunner: exactly. 70% of my R&D was spend on solving the problem with multiple decoy selection algorithms being used in the wild.     

> __< a​rticmine:monero.social >__ It has to be ideally statistically indistinguishable from the actual spend distribution     

> __< Rucknium >__ Spending very old outputs is very rare, though     

> __< j​effro256:monero.social >__ Fair     

> __< a​rticmine:monero.social >__ The output selection algorithm.     

> __< c​haser:monero.social >__ 4.2 is very bad, IMHO. a severe reduction in the effective privacy of ringCT transactions. this could be way less for the 2024 March suspected spam period.     

> __< s​yntheticbird:monero.social >__ have more than 2 outputs and you are screwed     

> __< a​rticmine:monero.social >__ I have to leave for another meeting. Will review the discussion late.     

> __< Rucknium >__ Sorry it took this long, but MRL decided that a new decoy selection algorithm probably could not safely be deployed without a hard fork, so other near-term priorities were put ahead of the research frequently     

> __< s​yntheticbird:monero.social >__ waves     

> __< s​yntheticbird:monero.social >__ Rucknium: ack.     

> __< rbrunner >__ I think we got it pretty right with priorities. E.g. looking at the spam wave more or less in real time was indeed important.     

> __< s​yntheticbird:monero.social >__ We're near over the hour, last topic     

> __< s​yntheticbird:monero.social >__ 5. Research on [Autonomous System (AS) peer connection rules](https://github.com/monero-project/monero/pull/7935) to reduce spy node risk.     

> __< Rucknium >__ Like I said in the previous meeting, any devs or resaerchers that want to see the report before Feb 20 can DM me for a copy.     

> __< Rucknium >__ I read four papers on Tor's resistance to traffic correlations at the AS level     

> __< Rucknium >__ Since we're at the hour, I'll discuss them next meeting I think     

> __< c​haser:monero.social >__ rbrunner: I agree.     

> __< rbrunner >__ Sounds reasonable.     

> __< Rucknium >__ My plan now is to figure out the cost structure that an adversary would encounter if they wanted to defeat an AS diversity rule by leasing IP addresses.     

> __< rbrunner >__ Also something like a double-edged sword :) You do the budgeting for the adversaries :)     

> __< Rucknium >__ Basically, is there a big discount from leasing many IP addresses from a single AS, compared to leasing many IPs from many ASes     

> __< b​oog900:monero.social >__ FWIW I have been running my tool to find proxies and they are still running nodes on the banned IPs     

> __< s​yntheticbird:monero.social >__ Probably because many don't have the ban list     

> __< Rucknium >__ Thanks for the update, boog     

> __< b​oog900:monero.social >__ "running nodes"     

> __< s​yntheticbird:monero.social >__ """make it so that we can communicate with a node""" \* wink \* \* wink \*     

> __< s​yntheticbird:monero.social >__ Alright is there anything someone wish to add ?     

> __< Rucknium >__ Recently I emailed Fanti, the lead author of the Dandelion++ paper, asking her option on the Clover paper (D++ alternative) and countermeasures to node proxies. I'll share info when I have it.     

> __< s​yntheticbird:monero.social >__ ack. thx for the efforts Rucknium     

> __< s​yntheticbird:monero.social >__ We can end meeting there. Thanks everyone.     

> __< Rucknium >__ Thanks for stepping in, syntheticbird :)     

> __< s​yntheticbird:monero.social >__ np it boost my ego     

> __< s​needlewoods:monero.social >__ you did a good job SyntheticBird, thanks everyone     

> __< j​berman:monero.social >__ thanks all     

> __< j​berman:monero.social >__ a comment Rucknium : the DSA would also be useful for the jamtis-RCT light wallet tier (so light wallets wouldn't need to download all elems necessary to re-build the tree), which imo should still be on the roadmap     

> __< Rucknium >__ Good point :)     

> __< j​berman:monero.social >__ Estimating 200 XMR for remaining EC divisors work, 50-200 XMR for gadgets formal verification (hand wave guess from other tasks), and 6 audits of varying complexity hand-waved at 50-200 XMR each also (perhaps more if we want multiple rounds). That's a pretty large range that could feasibly use the remaining fund of 1537 XMR. Seems unlikely that would occur and we'll likely end up <clipped message>     

> __< j​berman:monero.social >__ with funds leftover, but I figure it makes sense to keep the XMR from the research fund reserved for the work drafted out in the CCS and not re-purpose it     

> __< r​ottenwheel:unredacted.org >__ Rucknium: but this is not happening anymore because of forthcoming FCMP++ and CARROT network upgrade, correct?     

> __< 3​21bob321:monero.social >__ ^     


# Action History
- Created by: Rucknium | 2025-01-21T20:23:17+00:00
- Closed at: 2025-01-30T19:43:02+00:00
