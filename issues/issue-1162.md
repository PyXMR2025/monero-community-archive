---
title: Monero Research Lab Meeting - Wed 26 February 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1162
author: Rucknium
assignees: []
labels: []
created_at: '2025-02-25T21:48:06+00:00'
updated_at: '2025-03-08T17:30:50+00:00'
type: issue
status: closed
closed_at: '2025-03-08T17:30:50+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Prize contest to optimize some FCMP cryptography code](https://github.com/j-berman/fcmp-plus-plus-optimization-competition).

4. [Release of OSPEAD HackerOne and CCS milestone submissions](https://github.com/Rucknium/OSPEAD).

5. Research on [subnet deduplication for peer selection](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf) to reduce spy node risk.

6. Any other business

7. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1159 

# Discussion History
## j-berman | 2025-02-26T16:24:27+00:00
I unfortunately have to miss the meeting today.

For my latest, see my CCS update (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/527#note_28861). I also finished my re-review of PR 9135.

_____

On the FCMP++ optimization competition: we need to settle on a machine to use for benchmarks, and the repo could use a review: https://github.com/j-berman/fcmp-plus-plus-optimization-competition

_____

On research tasks, there were a few questions last week:

- Status of Veridise ec-divisors proof / review continuation: Veridise has completed their work on ec-divisors review, we are now just waiting on them to release it publicly.

- Status of Cypher Stack ec-divisors review: ongoing.

- Gadgets formal verification: next TODO is to discuss with Veridise.

- On moving forward with implementation audits:

  - GBP impl audit: CS audited this work on their own prerogative (awesome :) ). From the audit report: "Overall, we find that the implementation is well written and appears suitable for its intended purpose". @kayabaNerve intends to address the audit. After addressing, there is a question of whether or not we want additional audit(s). Personally I think it makes sense to get multiple rounds of audits from independent parties.

  - EC divisors impl audit: since ec divisors is in the FCMP++ optimization competition scope, it makes sense to hold off until that is complete.

  - Tower cycle impl audit: same as above.

  - Gadgets impl audit: we should do this after gadgets formal verification.

  - Circuit impl audit: this is slated for discussion on how best to proceed with Veridise. We may want to audit the spec first. Perhaps it makes sense to bring in additional independent parties to work on this as well. 

  - GSP impl audit: @kayabaNerve says this is good to go and is advocating for Cypher Stack to take this on given their existing work on CLSAG for [monero-{serai,wallet}](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/518).

## Rucknium | 2025-02-27T17:47:38+00:00
Logs

> __< r​ucknium:monero.social >__ MRL meeting in this room in two hours     

> __< j​berman:monero.social >__ Unfortunately I won't be able to make today's meeting, I shared my latest, an update regarding FCMP++ optimization competition, and FCMP++ research here: https://github.com/monero-project/meta/issues/1162#issuecomment-2685563055     

> __< j​berman:monero.social >__ gingeropolous: wondering if you have a suggestion for one of your machines you think we could/should use for the FCMP++ optimization competition? Imo the main requirement really is that it will be around several months from now (when the competition ends)     

> __< r​ucknium:monero.social >__ I wrote a FAQ for the OSPEAD repo: https://github.com/Rucknium/OSPEAD/tree/main?tab=readme-ov-file#frequently-asked-questions-faqs     

> __< r​ucknium:monero.social >__ Based of the FAQ, there is a 4-out-of-7 probability that the answer to your question is "No" :P     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1162     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< s​yntheticbird:monero.social >__ Hello there     

> __< a​rticmine:monero.social >__ Hello     

> __< rbrunner >__ Hello     

> __< c​haser:monero.social >__ hello     

> __< j​effro256:monero.social >__ Howdy     

> __< b​oog900:monero.social >__ hi     

> __< v​tnerd:monero.social >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Prepared and posted the OSPEAD Hackerone and CCS Milestone 1-2 documents and code: https://github.com/Rucknium/OSPEAD . Worked on game theory of subnet deduplication as a spy node countermeasure.     

> __< s​gp_:monero.social >__ Hello     

> __< v​tnerd:monero.social >__ updated socks5 review, and trying to figure out the bug reports from my recently merged PRs     

> __< j​effro256:monero.social >__ Responding to reviews for #9135, trying to reproduce bugs on release branch, and improving FCMP++/Carrot transaction construction code.     

> __< r​ucknium:monero.social >__ 3) Prize contest to optimize some FCMP cryptography code. https://github.com/j-berman/fcmp-plus-plus-optimization-competition     

> __< r​ucknium:monero.social >__ jberman had to miss this meeting, but said in his comment ( https://github.com/monero-project/meta/issues/1162#issuecomment-2685563055 ) "On the FCMP++ optimization competition: we need to settle on a machine to use for benchmarks, and the repo could use a review"     

> __< r​ucknium:monero.social >__ Maybe this issue was already discussed, but I didn't see it in the repo: One-sided execution of licensing. Say that someone wins the competition, but wants to negotiate for more XMR before assigning the appropriate open source license to their code. How to avoid?     

> __< r​ucknium:monero.social >__ I think this can be avoided by requiring that contestants submit a Monero address with their code submission. When someone is chosen, the XMR gets sent to them and the code is given the open source license. Therefore, there is no waiting on action by a contestant.     

> __< c​haser:monero.social >__ can't they still use their own choice of license?     

> __< r​ucknium:monero.social >__ Yes, but it would be dual-licensed in that case     

> __< r​ucknium:monero.social >__ When they submit, the terms of the submission are that it gets the open source license if it is the winner (and they get the prize XMR)     

> __< j​effro256:monero.social >__ Why don't we say put the Monero BSD license on your code to begin with, otherwise the submission is invalid? I'm assuming that the submissions are private to the judges until the winner is picked. We can return the code back to the losers with all rights reserved before, yeah? (IDK I'm not a lawyer)     

> __< r​ucknium:monero.social >__ They contestants may fear that they won't get the prize XMR if they already give the open source rights in the beginning     

> __< c​haser:monero.social >__ I'm not an expert at licenses, but what you outlined still sound like they could "show" us an attractive submission that's licensed under their own terms and essentially blackmail us to pay     

> __< v​tnerd:monero.social >__ Wouldn't they have to disclose the code so that it can be compiled into the benchmark utility? Seems odd that we would even accept an unknown binary     

> __< j​effro256:monero.social >__ If they fear that we will steal their code ..... why would they ever believe that we would pay them in the first place? IDK, if they don't trust us to blatantly use/license their code correctly, they probably wouldn't be sacrificing their man hours for the possibility of payment in the first place.     

> __< v​tnerd:monero.social >__ jeffro256: weve had 1-2 people try to hold code hostage in the past, under fear of non-payment     

> __< r​ucknium:monero.social >__ jeffro256: Because that action would be a violation of open source licensing rules     

> __< rbrunner >__ Sounds somehow like an "unsolvable" problem to, not possible to do "trustless". We and the contestant may *have* to trust each other     

> __< rbrunner >__ *problem to me     

> __< r​ucknium:monero.social >__ AFAIK, under my suggestion, the contestants just have to trust that the Monero Project won't violate open source rules. If the contestants have to assign the license before submission, then they would also have to trust that the Monero Project won't renege on its word. If this isn't considered a possible issue, that's fine, We can keep it as it is.     

> __< rbrunner >__ They have to trust us to pay also?     

> __< rbrunner >__ Ah, you mean pay first, license afterwards     

> __< NorrinRadd >__ "if they don't trust us to blatantly use/license their code correctly, " -- agreed     

> __< NorrinRadd >__ ignore that      

> __< NorrinRadd >__ "why would they ever believe that we would pay them in the first place?" -- agreed     

> __< NorrinRadd >__ if trust is an issue, they won't participate in the first place     

> __< s​agewilder:unredacted.org >__ In agreement with Rucknium's approach, a clear definition of the license should be explicitly stated in the reward agreement to prevent any potential loopholes that could allow one party to misappropriate the submission. Even if unlikely.     

> __< s​agewilder:unredacted.org >__ Regarding the issue of trust, as this is my first collaboration with Monero, I consider the most solid basis possible for any work I submit.     

> __< r​ucknium:monero.social >__ Ok. If they submit code with the open source license already attached, then that eliminates the issue of having code held hostage from the Monero Project     

> __< r​ucknium:monero.social >__ Reminder: sagewilder is a likely contestant FWIW.     

> __< rbrunner >__ "Pay first, delivery afterwards" does make some sense.     

> __< a​rticmine:monero.social >__ We must have consistent licencing for the project as a whole. Right now this is BSD. If we choose to change the license this is a totally separate discussion from this competition     

> __< rbrunner >__ They trust us to pay, we trust them to license after payments. It's mutual.     

> __< j​effro256:monero.social >__ A license that is sort of unambiguous in a code-like manner, but may or may not hold up in court is: "this file is copyrighted by participant X, all rights reserved, unless a Monero payment proof to address A for prize amount P can be provided, in which case this file is copyright of the Monero Project"     

> __< rbrunner >__ Clever     

> __< NorrinRadd >__ rbrunner: that requires 2 trust instances.  if the license is present upon submission, only 1 trust instance is required      

> __< r​ucknium:monero.social >__ A semi-smart contract :)     

> __< rbrunner >__ You invented a new license     

> __< a​rticmine:monero.social >__ We need to specify our license as it is now as a condition of participation in the contest     

> __< rbrunner >__ NorrinRadd: Yes. As a power shift away from the contestant, towards the Monero project     

> __< NorrinRadd >__ yes clever Re: Jeffro256     

> __< s​agewilder:unredacted.org >__ This text and its formulation are satisfactory to me.     

> __< a​rticmine:monero.social >__ The last thing we need is new "creative" licences     

> __< rbrunner >__ Surely we would re-license afterwards? Or would that be problematic?     

> __< a​rticmine:monero.social >__ So the current Monero license is a condition of participation     

> __< a​rticmine:monero.social >__ We cannot relicense afterwards.     

> __< r​ucknium:monero.social >__ I don't know if the "conditional license" needs to be assigned to the code submission itself. You can add it as a stipulation in the contest rules.     

> __< s​yntheticbird:monero.social >__ what? we can't relicense BSD ?     

> __< a​rticmine:monero.social >__ We can relicense the current BSD but not the other way     

> __< a​rticmine:monero.social >__ For example turn GPL v3 into BSD     

> __< s​yntheticbird:monero.social >__ the joy of GPL     

> __< NorrinRadd >__ it's not a relicense imo. "unless x, in which case this file's license is "abc"" -- it's self contained; all present uplon original submission == not a re-license      

> __< rbrunner >__ We hope for several submissions, right? And the chance of reneg / code taken hostage is there, but probably on the smaller side? So in that unlikely case we take the runner up, problem solved.     

> __< a​rticmine:monero.social >__ There are many arguments in favor and against for example regarding a strong copyleft such as GPL v 3.     

> __< s​yntheticbird:monero.social >__ imo it should be MIT     

> __< s​yntheticbird:monero.social >__ just for the ease of mind of the ecosystem     

> __< j​effro256:monero.social >__ I think Rucknium is saying that that might discourage participants b/c we can legally use their code without awarding them the prize money, even if we pinky promise before-hand that we won't     

> __< a​rticmine:monero.social >__ This competition is not the place to discuss changing the Monero license     

> __< b​oog900:monero.social >__ You can relicense GPL if all authors agree, with jeffro256's idea they are giving permission to relicense if they receive payment     

> __< s​yntheticbird:monero.social >__ oh maybe i misunderstood, i thought you were discussing the license of the submission     

> __< r​ucknium:monero.social >__ jeffro256: Yes, that is what I am saying.     

> __< NorrinRadd >__ they are welcome to not participate      

> __< j​effro256:monero.social >__ It wouldn't be changing the license of all of the Monero, just that submission     

> __< a​rticmine:monero.social >__ If they are chosen they agree to the current Monero license.     

> __< NorrinRadd >__ if conditional are allowed in legal agreements I believe. it's just a license with an if condition. It's not a license change.     

> __< j​effro256:monero.social >__ AFAIK, in a codebase, not every single line of code has to have the same license. Some files in the repo might have an MIT license, some might have BSD, the main LICENSE file provided in a git repo is just a "default" license, but it doesn't/can't override existing licenses     

> __< a​rticmine:monero.social >__ As long as the licenses are compatible     

> __< r​ucknium:monero.social >__ We have a couple more items to get to. We can discuss licensing issues with the contest next meeting, too. jberman isn't in attendance right now. And I'm sure kayabanerve  would like to give input too since he like to give input about licensing.     

> __< c​haser:monero.social >__ there is a big differential. an established free software project with long-term contributors is much less likely to renege on their word than a pseudonymous contestant who can just assume a new identity without any costs.     

> __< a​rticmine:monero.social >__ Typically it is one way compatibility. Mixing GPL and BSD for example leads to GPL the whole code     

> __< r​ucknium:monero.social >__ On which hardware to perform the benchmarks, the MRL computing cluster has some powerful machines:     

> __< s​yntheticbird:monero.social >__ New achievement unlocked: KayabaNerve, the lawyer 🖊     

> __< r​ucknium:monero.social >__ 3700x     

> __< r​ucknium:monero.social >__ 3900x     

> __< r​ucknium:monero.social >__ 5900x     

> __< r​ucknium:monero.social >__ 64 thread AMD Ryzen Threadripper 3970x     

> __< r​ucknium:monero.social >__ 256 thread 2x 7h12 server     

> __< r​ucknium:monero.social >__ Epyc server     

> __< r​ucknium:monero.social >__ And some low-power machines:     

> __< r​ucknium:monero.social >__ AMD C-50 Processor     

> __< r​ucknium:monero.social >__ Intel(R) Core(TM)2 Duo CPU T8100   2.10GHz     

> __< j​effro256:monero.social >__ So you're saying to specify the terms of the contest that "paid/winning submissions became copyright of the Monero project" and to have participants submit their code with no license attached (default is always copyright of the author)?     

> __< a​rticmine:monero.social >__ I believe we have to distinguish here between the license for the submission and the license the winner agrees for their code ahead of time if they win     

> __< a​rticmine:monero.social >__ The latter has to be BSD.     

> __< b​oog900:monero.social >__ that was jeffro's idea AFAIK     

> __< s​yntheticbird:monero.social >__ jeffro should license his idea in the chat next time     

> __< s​yntheticbird:monero.social >__ wrong reply     

> __< a​rticmine:monero.social >__ The submission license should be GPL v3 compatible     

> __< j​effro256:monero.social >__ My opinion is that we should benchmark and what we believe will be the "median" user hardware in the short term future. So new, but mid-range price range for new hardware     

> __< j​effro256:monero.social >__ *for what we     

> __< j​effro256:monero.social >__ new *consumer-grade* hardware     

> __< j​effro256:monero.social >__ So probably not AMD EPYCs     

> __< rbrunner >__ Good idea. A server machine may have large first-level caches that make things fast, which might not happen on a "normal" machine     

> __< r​ucknium:monero.social >__ AFAIK, there is no mid-range consumer hardware in the MRL computing cluster. So we may have to go somewhere else for the bechmark machine.. gingeropolous , any comments?     

> __< s​yntheticbird:monero.social >__ 3700X is mid range imo     

> __< r​ucknium:monero.social >__ 4) Release of OSPEAD HackerOne and CCS milestone submissions. https://github.com/Rucknium/OSPEAD     

> __< r​ucknium:monero.social >__ Comments or questions on this ^?     

> __< c​haser:monero.social >__ what do you all think about publishing a public-facing post on how these findings practically affect user privacy? IMHO this would be due as responsibility to users who rely on Monero's privacy. Some parts of Rucknium's FAQ looks like a good starting point.     

> __< rbrunner >__ Sounds good. There have been some insecurities, e.g. about that "ring size eduction to 4.2" or so, i.e. how to actually interpret that     

> __< r​ucknium:monero.social >__ It's possible, but a little difficult because it affects different threat models differently.     

> __< rbrunner >__ On Reddit     

> __< s​yntheticbird:monero.social >__ guys i swear one day we will have a getmonero.org blog that is working. 2 more weeks before new post     

> __< r​ucknium:monero.social >__ I hope my horse race betting metaphor helps people understand. AFAIK, Monero users are gamblers anyway 😉     

> __< rbrunner >__ Horse race betting? I have probably overlooked that.     

> __< c​haser:monero.social >__ true, it's difficult to put the outcomes into exact pigeonholes. however, we can distinguish (as you already have).     

> __< r​ucknium:monero.social >__ rbrunner: In the FAQ: https://github.com/Rucknium/OSPEAD?tab=readme-ov-file#frequently-asked-questions-faqs     

> __< r​ucknium:monero.social >__ "Q: Does the MAP Decoder attack work by eliminating decoys?"     

> __< c​haser:monero.social >__ if we are proper, it should go to the official blog.     

> __< rbrunner >__ Thanks!     

> __< rbrunner >__ Yeah, nothing against a getmonero.org blog post. With pointer to it on Reddit, monero.town and maybe elsewhere     

> __< r​ucknium:monero.social >__ IMHO, it may be a good idea for someone besides myself to reproduce the results from the small validation simulation: https://rucknium.github.io/OSPEAD/CCS-milestone-2/OSPEAD-docs/_book/successful-simulation.html#sec-successful-simulation-code     

> __< c​haser:monero.social >__ rbrunner: sounds great     

> __< r​ucknium:monero.social >__ Reproducing the whole Monero estimate isn't possible right now on consumer-grade hardware, but it could be possible with improvements to the code.     

> __< c​haser:monero.social >__ inb4 OSPEAD optimization contest     

> __< r​ucknium:monero.social >__ The reproducer would have to install the right packages first:     

> __< r​ucknium:monero.social >__ https://rucknium.github.io/OSPEAD/CCS-milestone-2/OSPEAD-docs/_book/requirements.html     

> __< r​ucknium:monero.social >__ https://github.com/Rucknium/OSPEAD?tab=readme-ov-file#installing-the-decoyanalysis-r-package     

> __< r​ucknium:monero.social >__ chaser: We actually had two proposal already to do that, but circumstances prevented it. So for now I am on my own     

> __< c​haser:monero.social >__ you mean people volunteering? or an actual contest? I didn't know that!     

> __< r​ucknium:monero.social >__ These two functions are the specific speedup targets (and I already wrote instructions for someone unfamiliar with the R code to re-implement):     

> __< r​ucknium:monero.social >__ https://github.com/Rucknium/OSPEAD/blob/main/CCS-milestone-2/decoyanalysis/R/bjr.R#L534-L587     

> __< r​ucknium:monero.social >__ https://github.com/Rucknium/OSPEAD/blob/main/CCS-milestone-2/decoyanalysis/R/bjr.R#L719-L894     

> __< plowsof >__ chaser Rucknium is this one of the two proposals? https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/375     

> __< r​ucknium:monero.social >__ First, isthmus was going to task one of his employees with re-implementing major parts in C++      

> __< r​ucknium:monero.social >__ Yes, that one plowsof. Thanks     

> __< plowsof >__ mj xmr the other for MAGIC?     

> __< r​ucknium:monero.social >__ Then later, after I re-factored, hyc was going to ask someone to implement those ^ small parts in C. But it was my fault it was delayed (since I was investigating an inconsistency issue in Monte Carlo simulations that turned out to be rooted in the intra-ring dependence issues)     

> __< plowsof >__ https://github.com/MAGICGrants/Monero-Fund/issues/21      

> __< j​effro256:monero.social >__ This is purely optional, but it would be nice to have these four plots on the same graph: A) empirical distribution of all ring members in Monero B) gamma distribution we currently use C) Estimated real spend distribution as demixing of A and B and other analysis from your work, and D) the distribution you recommend in Milestone II to approximate C     

> __< j​effro256:monero.social >__ The beta distribution recommended was interesting     

> __< r​ucknium:monero.social >__ jeffro256: Except for (A), those are plotted here in Figure 3.1: https://rucknium.github.io/OSPEAD/CCS-milestone-2/OSPEAD-docs/_book/performance-evaluation.html#fig-decoy-distributions-top-1-3-not-log     

> __< r​ucknium:monero.social >__ I meant 13.1     

> __< r​ucknium:monero.social >__ Vertical log scale here in Figure 13.3: https://rucknium.github.io/OSPEAD/CCS-milestone-2/OSPEAD-docs/_book/performance-evaluation.html#fig-decoy-distributions-top-1-3-log     

> __< r​ucknium:monero.social >__ I'll work on getting (A) in the same plot with the others     

> __< j​effro256:monero.social >__ Are the output ages since creation or since spendability     

> __< r​ucknium:monero.social >__ IMHO, the generalized beta distribution of the second kind (GB2) won because it is flexible. It might not be the best to actually implement because the code to make those draws might not be widely available in relevant programming languages, but those details can be discussed down the road. The difference between the top 4 choices wasn't very much (0.2 percentage points attack suc<clipped message     

> __< r​ucknium:monero.social >__ cess probability).     

> __< r​ucknium:monero.social >__ Table 13.1 has the comparison of the fitted proposed decoy distributions: https://rucknium.github.io/OSPEAD/CCS-milestone-2/OSPEAD-docs/_book/performance-evaluation.html#tbl-main-attack-success     

> __< r​ucknium:monero.social >__ Spendability.     

> __< r​ucknium:monero.social >__ So the edits to the decoy selection algorithm that jberman made in 2021 would be reverted. Those edits moved the Moser-based gamma from beginning at the 10 block lock to the chain tip. and then re-distributed the "unspendable" part of the gamma distribution t the recent spend window     

> __< r​ucknium:monero.social >__ The Moser paper estimated their distribution on historical data when the 10 block lock wasn't a consensus rule and some wallet implementations violated it.     

> __< k​ayabanerve:matrix.org >__ Rule #1 requires an approved license Rucknium     

> __< k​ayabanerve:matrix.org >__ The approved licenses is a file in-repo which doesn't exist. I'd recommend public domain (CC0, unlicense), MIT, BSD-1, BSD-2, BSD-3, and maybe some LGPLs.     

> __< r​ucknium:monero.social >__ So, the license had to be applied before submission, under the draft rules?     

> __< a​rticmine:monero.social >__ I oppose LGPLs. We should not be changing the license of the Monero project by this competition     

> __< a​rticmine:monero.social >__ I propose the only approved license is the current Monero license     

> __< s​gp_:monero.social >__ I see that as the only option that makes sense     

> __< s​gp_:monero.social >__ you're paying for it, you get to pick the license, so pick the same one     

> __< s​yntheticbird:monero.social >__ I'm against and i've no argument to explain it therefore i'm all for it     

> __< s​yntheticbird:monero.social >__ checkmates myself     

> __< plowsof >__ BSD-3      

> __< r​ucknium:monero.social >__ I will draft a public-facing post about the OSPEAD results. (Just because I write a draft doesn't mean it has to go on getmonero.org). In the meantime, feel free to continue giving feedback about interpretations and especially the FAQ: https://github.com/Rucknium/OSPEAD?tab=readme-ov-file#frequently-asked-questions-faqs     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone!     

> __< a​rticmine:monero.social >__ Thanks     

> __< s​yntheticbird:monero.social >__ thx Rucknium     

> __< s​yntheticbird:monero.social >__ thx everyone     

> __< s​yntheticbird:monero.social >__ thx myself     

> __< j​effro256:monero.social >__ Thanks everyone !     

> __< c​haser:monero.social >__ thank you Rucknium! and thank you all.     

> __< k​ayabanerve:matrix.org >__ ArticMine: A LGPL lib does not propagate to Monero. It only requires the copy-left terms be applied to derivatives of the lib itself.     

> __< k​ayabanerve:matrix.org >__ Only approving Monero's BSD-3 is silly as we have non-BSD-3 libs *and* the existing libs are MIT. Anyone who forks them so their submission is an improvement can't unilaterally relicense to BSD-3.     

> __< k​ayabanerve:matrix.org >__ It'd force complete rewrites of the existing libs.     

> __< k​ayabanerve:matrix.org >__ If we're already at MIT and BSD-3, why not allow public domain dedications which impose no terms at all? What's the issue with LGPL when it wouldn't propagate to Monero?     

> __< j​berman:monero.social >__ The way the contest is currently set up, contestants would submit a PR that modifies the existing code *that is already licensed under MIT*     

> __< j​berman:monero.social >__ I structured the contest like that to make it easier on contestants to get started coding, see the README's for ec-divisors-contest and helioselene-contest: https://github.com/j-berman/fcmp-plus-plus-optimization-competition     

> __< j​berman:monero.social >__ As such, wouldn't their submissions fall under MIT by default? And I wouldn't see a problem with that. We are fine to use the code in Monero as a git submodule     

> __< j​berman:monero.social >__ 3700x seems like a solid machine to run the contest on. Maybe if gingeropolous has something available in between that and the low power machines, would be optimal. But I don't see an issue going with a 3700x     

> __< k​ayabanerve:matrix.org >__ They could introduce API-compatible libs under their own license or individually license files. Again, the entire poly.rs file is ripe for a rewrite.     

> __< k​ayabanerve:matrix.org >__ I'm fine with kneecapping to MIT alone though.     

> __< j​berman:monero.social >__ Simplest path here seems MIT to me     



## hinto-janai | 2025-02-28T14:10:14+00:00
@j-berman Will you need full access to the benchmarking machine(s) for the competition? I may not be able to provide access but I can run benchmarks on the machines listed here [1](https://github.com/Cuprate/benches?tab=readme-ov-file#machines) [2](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/543#note_28614), I'll be buying a few more mid-range ones soon to cover Windows and macOS as well, if that matters.

> and the repo could use a review

Is there anything specific I could help with? It seems I can review everything barring the reference implementation code.

## j-berman | 2025-02-28T18:03:32+00:00
From the latest in MRL, it seems we should be good going with one of @Gingeropolous 's machines (personally I think it would be nice that multiple people can remote into his cluster and verify results).

A few things that would be sweet to have reviewed:

- The weights for the helioselene benchmark (can assess my logic for those weights by checking the flamegraphs): https://github.com/j-berman/fcmp-plus-plus-optimization-competition/tree/main/helioselene-contest#how-your-helioselene-score-is-calculated

- The code for the benchmarks and tests in `helioselene-contest` and `ec-divisors-contest` (benches/, src/, and tests/)

- The 3 README's: [main](https://github.com/j-berman/fcmp-plus-plus-optimization-competition/blob/main/README.md), [`ec-divisors-contest`](https://github.com/j-berman/fcmp-plus-plus-optimization-competition/tree/main/ec-divisors-contest), [`helioselene-contest`](https://github.com/j-berman/fcmp-plus-plus-optimization-competition/tree/main/helioselene-contest)

# Action History
- Created by: Rucknium | 2025-02-25T21:48:06+00:00
- Closed at: 2025-03-08T17:30:50+00:00
