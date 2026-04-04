---
title: Monero Research Lab Meeting - Wed 12 March 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1171
author: Rucknium
assignees: []
labels: []
created_at: '2025-03-11T23:22:08+00:00'
updated_at: '2025-03-23T14:01:13+00:00'
type: issue
status: closed
closed_at: '2025-03-23T14:01:12+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Prize contest to optimize some FCMP cryptography code](https://github.com/j-berman/fcmp-plus-plus-optimization-competition).

4. [Release of OSPEAD HackerOne and CCS milestone submissions](https://github.com/Rucknium/OSPEAD). Analysis of risk of new decoy selection algorithm without a hard fork.

5. Possible intermediate hard fork before FCMP hard fork. @nahuhh , @xenumonero , `elongated`.

6. Research on [subnet deduplication for peer selection](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf) to reduce spy node risk.

7. Any other business

8. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1167 

# Discussion History
## Rucknium | 2025-03-15T16:38:28+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1171     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< s​yntheticbird:monero.social >__ Hello there     

> __< rbrunner >__ Hello     

> __< j​berman:monero.social >__ *waves*     

> __< j​effro256:monero.social >__ Howdy     

> __< v​tnerd:monero.social >__ Hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< v​tnerd:monero.social >__ working on the haveno unit tests to determine source of failure with recent release builds     

> __< v​tnerd:monero.social >__ Im still getting an unrelated error, working on this privately with woodser     

> __< j​berman:monero.social >__ me: CLI FCMP++ transfers are working (ironing out kinks), batch verification is working in my local, pushing soon     

> __< r​ucknium:monero.social >__ me: Researching the safety of deploying a change to the decoy selection algorithm without a hard fork. Re-writing another part of the BJR estimator in Rust for a speedup. First I was fighting Rust's type system, then its borrow checker.     

> __< r​ucknium:monero.social >__ 3) Prize contest to optimize some FCMP cryptography code. https://github.com/j-berman/fcmp-plus-plus-optimization-competition     

> __< r​ucknium:monero.social >__ Oh, wait, I have some announcements     

> __< r​ucknium:monero.social >__ MoneroKon has a call for proposals for talks. Tentative deadline is March 24: https://cfp.twed.org/mk5/cfp     

> __< j​effro256:monero.social >__ me: wallet2 tx construction for Carrot/FCMP++     

> __< r​ucknium:monero.social >__ I will probably submit at least one proposal     

> __< r​ucknium:monero.social >__ cuprate version 0.0.1 has been released: https://www.reddit.com/r/Monero/comments/1j9k1n8/cuprate_v001_released     

> __< r​ucknium:monero.social >__ It has a protocol book that can help researchers figure out what the code does without reading the source: https://monero-book.cuprate.org/     

> __< r​ucknium:monero.social >__ cuprate is an alternative implementation of the Monero node software     

> __< r​ucknium:monero.social >__ Thanks to help from plowsof, you can now link papers in moneroresearch.info without such a long URL     

> __< r​ucknium:monero.social >__ https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=1     

> __< r​ucknium:monero.social >__ can be reduced to     

> __< r​ucknium:monero.social >__ https://moneroresearch.info/1     

> __< r​ucknium:monero.social >__ We can get back to agenda item 3, the FCMP optimization competition. How much more is there to discuss on this?     

> __< j​berman:monero.social >__ On the contest, I made some changes from last week's meeting as per kayabanerve 's suggestions:     

> __< j​berman:monero.social >__ - ec-divisors benches both the instantiation of the ScalarDecomposition as well as scalar_mul_divisor     

> __< j​berman:monero.social >__ - the ec-divisors-contest README now includes a section explaining why a submission that shifts majority weight into ScalarDecomposition::new may beat a submission that keeps majority weight in scalar_mul_divisor if both submissions have the same overall speedup     

> __< k​ayabanerve:matrix.org >__ Veridise is working on a quote to formally verify the gadgets and audit the circuit.     

> __< j​berman:monero.social >__ gingeropolous has also purchased a 5600g that I think is suitable for the contest (I can add a clause that makes it clear there should be no benefit from the gpu), also taking into account that wasm cycles is not CPU dependent and the score is a combo of wasm cycles improvement + time to execute     

> __< j​berman:monero.social >__ Next for the contest is just sign-off on the details. Then we can settle on timeline and commence the marketing blitz     

> __< r​ucknium:monero.social >__ The people that definitely need to approve the details are jberman , jeffro256 , and kayabanerve . Is that correct? Others can approve, too, of course     

> __< j​berman:monero.social >__ Ideally yes     

> __< k​ayabanerve:matrix.org >__ FWIW, the circuit is quite small and the gadgets quite simple. One is literally equality. After the discrete logarithm gadget, currently proven, there may not be too much meaningful to work with. Part of Veridise's quote, exclusive to the specification and not the implementation, will be about what supporting evidence makes sense (formal verification, additional security proofs) a<clipped message     

> __< k​ayabanerve:matrix.org >__ s part of auditing the circuit.     

> __< k​ayabanerve:matrix.org >__ I don't need to, I stepped back Rucknium.     

> __< r​ucknium:monero.social >__ IMHO, rule 2 should change from "Submissions must be written by the submitter and licensed under MIT." to "Submissions must be written by the submitter and licensed under MIT _at the time of submission_." To make it very clear.     

> __< r​ucknium:monero.social >__ IIRC, you have the MIT license in there with the repo template, but the rule mention helps clarify too, I think.     

> __< j​berman:monero.social >__ ok     

> __< r​ucknium:monero.social >__ kayabanerve: You have been suggesting changes. That's why I included you. But, I acknowledge.     

> __< k​ayabanerve:matrix.org >__ *The contest doesn't need me to sign off.     

> __< k​ayabanerve:matrix.org >__ So have you, and it doesn't require your sign off ;)     

> __< k​ayabanerve:matrix.org >__ My distinction wasn't to proclaim disinterest, it was to say I'm not officially managing this.     

> __< r​ucknium:monero.social >__ IMHO, the timeline details and publicity plan can be decided before the next MRL meeting if that makes the most sense. Don't want to unnecessarily delay things.     

> __< j​berman:monero.social >__ Ok proposal: once we get sign-off, the contest opens for submissions 1 month after that, will be open for submissions for 2 months, and we can commence marketing immediately upon sign-off     

> __< r​ucknium:monero.social >__ That timeline sounds great to me     

> __< j​berman:monero.social >__ xmrack: we can work together on a blog post / whatever announcements you want to make on other platforms     

> __< j​berman:monero.social >__ (I ping xmrack since he volunteered to handle marketing :) )     

> __< j​berman:monero.social >__ Also, binaryFate has expressed positive sentiment toward the GF funding the prize payouts, and I requested confirmation the GF would be willing to cover the prizes 100% in full     

> __< j​berman:monero.social >__ (I just requested confirmation 2 minutes ago to be clear)     

> __< j​berman:monero.social >__ that's all I got     

> __< r​ucknium:monero.social >__ Thanks, jberman     

> __< r​ucknium:monero.social >__ 4) Release of OSPEAD HackerOne and CCS milestone submissions. Analysis of risk of new decoy selection algorithm without a hard fork. https://github.com/Rucknium/OSPEAD     

> __< r​ucknium:monero.social >__ I made a blog post PR to the getmonero.org blog: https://github.com/monero-project/monero-site/pull/2448     

> __< r​ucknium:monero.social >__ Here a preview of how it looks: https://deploy-preview-2448--barolo-time-757cf9.netlify.app/2025/03/10/ospead-optimal-ring-signature-research     

> __< r​ucknium:monero.social >__ Any suggestions welcome. I don't know when it will go live, but probably soon.     

> __< r​ucknium:monero.social >__ I have been looking into spackle 's suggestion of a gradual rollout of a new decoy selection algorithm (DSA) without a hard fork, where a new release version of wallet2 would gradually transition to the new DSA over a period of weeks or months, to prevent anonymity puddles when some users don't update immediately.     

> __< r​ucknium:monero.social >__ This is a complicated statistical question because it involves several steps. IMHO, it's best to investigate this with Monte Carlo simulations instead of trying to figure out a closed-form expression. I developed a closed-form expression when the fungibility defect is known with certainty, like a nonstandard fee, here: https://github.com/Rucknium/misc-research/blob/main/Monero-Fun<clipped message     

> __< r​ucknium:monero.social >__ gibility-Defect-Classifier/pdf/classify-real-spend-with-fungibility-defects.pdf     

> __< r​ucknium:monero.social >__ But with a different DSA, the adversary needs to classify txs as old-version or new-version first, which creates some uncertainty at that step.     

> __< r​ucknium:monero.social >__ If people here think it's not worth it to investigate, I can drop it, too     

> __< j​berman:monero.social >__ I have a q, does the OSPEAD research use the exact algorithm from the Monero code, or does it strictly use the same gamma shape and rate?     

> __< r​ucknium:monero.social >__ jberman: Use it for what?     

> __< r​ucknium:monero.social >__ To estimate the real spend distribution, it uses the exact Monero code, even changing by the block height of the tx construction. It has flat steps at each block     

> __< j​effro256:monero.social >__ I read the post and it seems like a good high level introduction to include on the maim site     

> __< r​ucknium:monero.social >__ I used jeffro256's python code in his DSA documentation PR as the basis for the wallet2 DSA     

> __< r​ucknium:monero.social >__ I had to convert the random draw into a closed-form of the CDF. It is semi-closed-form since there are many "steps" in the procedure, one for each block height at least.     

> __< s​packle:monero.social >__ Rucknium: Is it a fair guess to say that the DSA a transaction used could be classified with high confidence even with a relatively low number of decoys selected from a new distribution?     

> __< s​packle:monero.social >__ Having had additional time to reflect, my guess is that with OSPEAD being as effective as it is operating off 1/16 ring members, even ~2/15 decoys will stand out like a sore thumb.     

> __< s​packle:monero.social >__ If this seems correct; it leads me to thinking that the goal of a gradual rollout would be most simply and best achieved by delaying the DSA switch to a higher block height so people have time to upgrade, then performing the switch all at once.     

> __< r​ucknium:monero.social >__ To do the first-step classification into different DSAs, the adversary would usually want an estimate about what share of txs use the old-version and new-version DSA. That's the mixing proportion. To get that, the adversary could use the BJR technique (refer to the OSPEAD repo about BJR) or the simpler Hall (1981). "On the non-parametric estimation of mixture proportions."     

> __< r​ucknium:monero.social >__ spackle: I have been doing some very preliminary test classifications. I am getting a higher classification error rate than I expected, actually. This is with ideas from Bagui & Vaughn  (1998) that I will discuss later. The rate of misclassification is about 20% when ring size is 16 (very preliminary).     

> __< r​ucknium:monero.social >__ That's a comparison of the wallet2 DSA and an OSPEAD-derived one     

> __< r​ucknium:monero.social >__ Adding in a rule to avoid coinbases is more complicated.     

> __< r​ucknium:monero.social >__ Rings are repeated measurements. The literature on nonparametric classification with repeated measurements is small, at least as far as I have found.     

> __< r​ucknium:monero.social >__ This paper uses a Mann-Whitney statistic to do the classification: Hudimoto, H. (1964). "On a distribution-free two-way classification."     

> __< r​ucknium:monero.social >__ This paper, and related papers by Bagui, use a majority-vote rule that classifies each ring member through standard nonparametric discriminant analysis (or nearest neighbor in this case), and then classifies based on which distribution gets the most votes: Bagui & Vaughn  (1998). "Statistical Classification Based on A-Rank Nearest Neighbor Rule"     

> __< a​ntilt:we2.ee >__ so a first guess: would reduce 4.2 -> 3.8     

> __< r​ucknium:monero.social >__ Another Bagui paper: Bagui & Mehra (1999) "Classification of multiple observations using multi-stage rank nearest neighbor rule"     

> __< a​ntilt:we2.ee >__ @ 50:50     

> __< r​ucknium:monero.social >__ Disappointingly, this big review paper only had a paragraph or two on nonparametric techniques. It focused on assuming a normal distribution: Lix & Sajobi (2010) "Discriminant analysis for repeated measures data: a review"     

> __< r​ucknium:monero.social >__ Repeated measurements appear a lot in medicine. I guess normal distributions make sense in medicine if the source of the distribution is just measurement error.     

> __< r​ucknium:monero.social >__ I will probably be able to set up a Monte Carlo simulation with at least one of these techniques by next MRL meeting.     

> __< j​effro256:monero.social >__ Are you aware of the coinbase decoy selection PR?     

> __< r​ucknium:monero.social >__ Note that this issue with analyzing the risk of a DSA change without a hard fork was out of scope of my original OSPEAD CCS, so labor time on this is coming from my general statistical research CCS.     

> __< r​ucknium:monero.social >__ Yes     

> __< r​ucknium:monero.social >__ IIRC, it requires a node change, but I'm not sure     

> __< j​effro256:monero.social >__ Are you saying *modeling* how that affects determine the real spends in a distribution is harder ?     

> __< r​ucknium:monero.social >__ Yes, modeling is harder     

> __< j​effro256:monero.social >__ Yeah for the performant version     

> __< r​ucknium:monero.social >__ Because I'm not sure if I should treat coinbases as a separate variable, which would make it multivariate instead of univariate discriminant analysis.     

> __< j​effro256:monero.social >__ You *can* do it without a node update , but its worse IMO     

> __< r​ucknium:monero.social >__ I think with Hudimoto (1964) and similar techniques, it would give inaccurate results if coinbases were considered the same "variable" as non-coinbases, for classification purposes.     

> __< r​ucknium:monero.social >__ I think Bagui would be OK though.     

> __< j​effro256:monero.social >__ Because theres probably a real difference in spend behaviors of coinbase outputs vs regular outputs     

> __< r​ucknium:monero.social >__ There's also the question of if it is worth it because excluding coinbases could increase the classification accuracy (by the adversary) much more than the gain in ring member slots. Without a hard fork, that is     

> __< j​effro256:monero.social >__ I think that that was the main concern and why the coinbase DSA change wasn't merged initially     

> __< r​ucknium:monero.social >__ According to my recent data, coinbase outputs make up 6% of recent outputs. If I'm drawing 15 decoys with the status quo DSA, then the probability of not getting any coinbase ring members is about 40%     

> __< j​effro256:monero.social >__ Although a soft fork instead of a hard fork could be implemented to enforce that rings consist of only coinbase members or only non-coinbase members     

> __< r​ucknium:monero.social >__ But on average, a coinbase occupies just one ring member slot now (15 * 0.06 = 0.9)     

> __< r​ucknium:monero.social >__ ^ Assuming the user is not spending a coinbase output in the ring     

> __< r​ucknium:monero.social >__ Let's combine this discussion with the next item. I know at the last meeting there wasn't much support for this, but there was some discussion after the meeting:     

> __< r​ucknium:monero.social >__ 5) Possible intermediate hard fork before FCMP hard fork. ofrnxmr  , xenu  , elongated     

> __< r​ucknium:monero.social >__ jeffro256: Could you speak more about this soft fork idea? That would require a new release, and what kind of actions by miners and users?     

> __< k​ayabanerve:matrix.org >__ I maintain my strong advocacy for no     

> __< l​ordx3nu:matrix.org >__ the timeline is the key here. i can't speak on the development of fcmps but if it is more than a year out then we should do a hard fork.     

> __< a​rticmine:monero.social >__ My question here is what is a realistic timeline for FCMP++ on the main chain.?     

> __< k​ayabanerve:matrix.org >__ We should be at testnet with academia and audits ~halfway done and moving forward, right jberman?     

> __< k​ayabanerve:matrix.org >__ Not at at testnet but about the first testnet given the work on integration?     

> __< j​effro256:monero.social >__ There's a ton of details to work out, but I would be very sad if FCMP++ wasn't live on mainnet within 2025     

> __< k​ayabanerve:matrix.org >__ If so, we can start syncing with integrators (unless FCMP++ is there but CARROT isn't).     

> __< e​longated:matrix.org >__ What would be worst case timeframe scenario for fcmp++ ?     

> __< rbrunner >__ That's easy. Never. Because some audit finds a catastrophic flaw in the crypto.     

> __< e​longated:matrix.org >__ So we should plan for a intermediate hf     

> __< l​ordx3nu:matrix.org >__ i think a hard fork to ospead is actually quite logical. it gives fcmps some more breathing room for audits and it helps ring sigs in the interim     

> __< j​effro256:monero.social >__ Worst case? Kayaba, j-berman, I, and anyone else capable of working on FCMP++ in the immediate future get Ebola and die and then quantum computers start working and obsolete FCMP++ before its testnet     

> __< l​ordx3nu:matrix.org >__ also it "wakes up" the network     

> __< j​berman:monero.social >__ Agree with this     

> __< k​ayabanerve:matrix.org >__ That's why I stated we're simply hashing y coordinates in NWLB.     

> __< k​ayabanerve:matrix.org >__ Else we would be delayed a month.     

> __< a​ntilt:we2.ee >__ for the record: a series of soft forks would "punish" those who do not upgrade with a continuous decrease in privacy - and "reward" those who do upgrade.     

> __< rbrunner >__ "Logical" is, for me, a question of opinion, not something mathematical. I find it "logical" to put each and every available dev hour into FCMP++     

> __< rbrunner >__ Down with rings as fast as possible.     

> __< rbrunner >__ No more bandaids with "intermediate hardforks"     

> __< j​effro256:monero.social >__ Worst case that is somewhat plausible and forseeable in my opinion ? The contest and the audits of that code get dragged out and push the mainnet back a few months . Or the broader ecosystem is slow to update and there is a lot of pressure to wait to activate the HF until everyone is ready     

> __< k​ayabanerve:matrix.org >__ We don't need the contest     

> __< a​rticmine:monero.social >__ With a timeline for FCMP++ within 2025 l cannot support an interim HF     

> __< e​longated:matrix.org >__ So eoy 2026 would be realistic time line     

> __< k​ayabanerve:matrix.org >__ I already said if that becomes a holdup, we should audit existing and move forward with contest libs being a post deployment upgrade     

> __< a​rticmine:monero.social >__ The contest libs are not a HF     

> __< rbrunner >__ I think some people here quite underestimate how much work goes into a well and responsibly done Monero hardfork.     

> __< k​ayabanerve:matrix.org >__ We also can update the eco as soon as we're at the final testnet. We don't  have to update the eco during the ahF lead time     

> __< k​ayabanerve:matrix.org >__ *HF, not "ahF"     

> __< rbrunner >__ "So eoy 2026 would be realistic time line" That escalated quickly to that year end as realistic, oh boy :)     

> __< e​longated:matrix.org >__ If we can push out fcmp++ q1 2026, intermediate hf can be avoided; if there is a chance of anything longer than that we should start planning for hf     

> __< l​ordx3nu:matrix.org >__ yeah i agree. q2 2026 is pushing it     

> __< l​ordx3nu:matrix.org >__ i think waking up the network is being undervalued here as well     

> __< rbrunner >__ Also don't underestimate psychology. Any intermediate hardfork could do everybody a disservice because it takes wind out of the sails of FCMP++     

> __< k​ayabanerve:matrix.org >__ I'm not trying to underestimate it. I'm saying 3 months should be enough to finish the protocol , 3 months enough to start integration and the testnet, and 3 months for HF lead and finish integration for EO this Y     

> __< rbrunner >__ People think it will be comfy to put up with rings a while longer without a problem.     

> __< rbrunner >__ kayabanerve: I think people underestimate the *intermediate* hardfork, to be clear     

> __< k​ayabanerve:matrix.org >__ I'd hope for mid-Q4 given how things have been going.     

> __< rbrunner >__ No such thing as "let us slip in a cute, little intermediate hardfork, it won't hurt" :)     

> __< l​ordx3nu:matrix.org >__ q4 sounds awesome. but if things aren't going that way then we should pivot. I think being flexible is a good idea here because we do have a hf fix for ring sigs.     

> __< k​ayabanerve:matrix.org >__ Yes, FCMP++     

> __< k​ayabanerve:matrix.org >__ :p     

> __< s​packle:monero.social >__ Noting the immense emphasis on not disrupting FCMP++ development, I would like to hear more opinions on an OSPEAD focused soft fork. My perception is that a good effort can be made to minimize development requirements for a soft fork DSA change, and that this represents a decent compromise position to give most people what they mostly want.     

> __< r​ucknium:monero.social >__ This was the hard fork planning checklist from last hard fork: https://github.com/monero-project/meta/issues/630     

> __< rbrunner >__ spackle: If it's indeed "what they mostly want", yeah, why not.     

> __< r​ucknium:monero.social >__ Doesn't a soft fork mostly affect node software? Using the soft fork definition from bitcoin and its cousins.     

> __< rbrunner >__ Maybe the terminology is a bit fuzzy here, maybe we should name it a "not-hardfork" to avoid confusion ...     

> __< r​ucknium:monero.social >__ With BTC soft forks, you could have wallets do segwit txs (and other types), but no one was required to upgrade     

> __< a​ntilt:we2.ee >__ wallet-upgrade     

> __< a​rticmine:monero.social >__ In 2013 a soft fork became a hard fork https://blog.citp.princeton.edu/2015/07/28/analyzing-the-2013-bitcoin-fork-centralized-decision-making-saved-the-day/     

> __< j​effro256:monero.social >__ Usually it affects both, but old nodes don't have to update to stay up-to-date in consensus     

> __< a​rticmine:monero.social >__ So no to an interim fork, with a less than a year timeline for FCMP     

> __< r​ucknium:monero.social >__ By the way, the first version of this issue said "However, the tentative plan would be an early Spring hard-fork, i.e. February or March of 2022." The hard fork finally happened in August 2022.     

> __< rbrunner >__ Which issue?     

> __< rbrunner >__ Ah, the 630     

> __< r​ucknium:monero.social >__ > This was the hard fork planning checklist from last hard fork: https://github.com/monero-project/meta/issues/630     

> __< r​ucknium:monero.social >__ GitHub keeps version history of issues.     

> __< r​ucknium:monero.social >__ We are 30 minutes past the hour. We'll end the meeting here, but feel free to continue discussing. Thanks everyone.     

> __< a​rticmine:monero.social >__ Thanks     

> __< l​ordx3nu:matrix.org >__ thanks ruck!     



# Action History
- Created by: Rucknium | 2025-03-11T23:22:08+00:00
- Closed at: 2025-03-23T14:01:12+00:00
