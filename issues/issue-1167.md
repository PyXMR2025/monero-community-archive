---
title: Monero Research Lab Meeting - Wed 05 March 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1167
author: Rucknium
assignees: []
labels: []
created_at: '2025-03-04T21:25:13+00:00'
updated_at: '2025-03-15T16:38:46+00:00'
type: issue
status: closed
closed_at: '2025-03-15T16:38:46+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Prize contest to optimize some FCMP cryptography code](https://github.com/j-berman/fcmp-plus-plus-optimization-competition).

4. [Release of OSPEAD HackerOne and CCS milestone submissions](https://github.com/Rucknium/OSPEAD).

5. Possible intermediate hard fork before FCMP hard fork. @nahuhh , @xenumonero , `elongated`.

6. Research on [subnet deduplication for peer selection](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf) to reduce spy node risk.

7. Any other business

8. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1162 

# Discussion History
## Rucknium | 2025-03-08T17:28:42+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1167     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< v​tnerd:monero.social >__ hi     

> __< s​packle:monero.social >__ hi     

> __< a​ck-j:matrix.org >__ Hi     

> __< c​haser:monero.social >__ hello     

> __< j​berman:monero.social >__ *waves*     

> __< l​ordx3nu:matrix.org >__ hi     

> __< s​yntheticbird:monero.social >__ Hi     

> __< a​rticmine:monero.social >__ Hi     

> __< s​agewilder:unredacted.org >__ Hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< j​berman:monero.social >__ me: created an FCMP++ tx with the CLI on a local testnet, continuing with cleaner code organization. Also caught a virus so was out of commission past couple days. Back now     

> __< v​tnerd:monero.social >__ working on figuring out whats going on with haveno with the release branch updates. getting haveno running is a bit of a beast in itself     

> __< r​ucknium:monero.social >__ me: Wrote a draft getmonero.org blog post on OSPEAD: https://gist.github.com/Rucknium/e18c514f0ba7a6dc6c7f35f9c242a34a     

> __< NorrinRadd >__ vtnerd doing some haveno work?     

> __< v​tnerd:monero.social >__ no, just trying to figure out why their tests fail with recent monero changes     

> __< r​ucknium:monero.social >__ jeffro256: ping in case you need it     

> __< r​ucknium:monero.social >__ 3) Prize contest to optimize some FCMP cryptography code. https://github.com/j-berman/fcmp-plus-plus-optimization-competition     

> __< j​effro256:monero.social >__ Howdy     

> __< j​berman:monero.social >__ "How long do you believe it would be before the contest starts?" - Let's say we finalize rules today/tomorrow, and we have the general fund cover the contest prizes, we could feasibly open the contest for submissions by early April. That pushes your timeline up by just 2 weeks, so ya I'd say that estimate is fairly accurate     

> __< j​berman:monero.social >__ "Also, jberman, you shouldn't bench scalar_mul_divisor alone" - ok, valid points. I'll update that.     

> __< k​ayabanerve:matrix.org >__ I raised questions above on timeline until a winner is selected, from organization to fundraising to execution to selection, and aired the idea of auditing the current libs for an initial release.     

> __< j​berman:monero.social >__ Of note, I included a new clause in the competition rules that we can determine winners at our discretion (that would potentially disqualify such a submission / allow us flexibility in judging), but agree that is a reasonable point to fix for ec-divisors     

> __< r​ucknium:monero.social >__ IMHO, the CCS for fundraising needs to specify what happens with the funds if no submissions exceed to 20% speedup threshold. Probably makes sense to put it toward one of the FCMP CCS efforts (dev/research).     

> __< j​berman:monero.social >__ "If these libs are a bottleneck, I'd propose auditing the current libraries, being ready to ship them as-is" - I'm not comfortable with shipping tree building in wallets as is, it would slow down wallet sync a significant amount. I would re-work it to download missing tree elems if we don't get a significant speed up in time for v1 release     

> __< k​ayabanerve:matrix.org >__ The dev CCS is mine outright, with no distinct distributions/rollover, so I support that one being the fallback /s     

> __< j​effro256:monero.social >__ Yeah the timeline that Kayaba pointed out is probably pretty accurate, which makes it important to get the competition rolling soon if we're going to do it. There's a ton of stuff that we also need to do in the next 6 months, but the underlying FCMP lib is a dependency of most future dev work, and not everything has the same criticality to be audited upon release. For example: mul<clipped messag     

> __< j​effro256:monero.social >__ tisig code and hardware device application code.     

> __< j​berman:monero.social >__ My thinking behind proposing going with the general fund for this is three-fold: 1) speeds up the time to get the contest rolling, 2) relatively simple to handle the case where no submission exceeds the 20% threshold (funds stay in the fund), and 3) the fund is sitting on a lot of Monero for general development of which I think this qualifies     

> __< j​effro256:monero.social >__ If we do go down this path, I would wait a little bit until we finish integration, so that details of the API can be tweaked before auditing. AFAIK, the Monero integration will be the first live project using this crate(s) as a dependency, and a lot of QoL issues can be ironed out during this time     

> __< k​ayabanerve:matrix.org >__ And to think I just started to poke at auditing the SAL and associated multisig code 😱 Get out of my head jeffro     

> __< k​ayabanerve:matrix.org >__ Multisig specifically has an explicit line item under the research CCS FWIW     

> __< k​ayabanerve:matrix.org >__ jeffro256: Not to be rude, ec-divisors is like, two functions     

> __< k​ayabanerve:matrix.org >__ Said API is already well-suited to the stack, being designed for it, and integrated     

> __< a​ck-j:matrix.org >__ What are the plans to market the competition (if any)? Does anyone know of places where talented and qualified developers would communicate? We could maybe take an ad out on codeforce.com     

> __< k​ayabanerve:matrix.org >__ Then for helioselene, it doesn't have its own API. It uses the ff/group APIs     

> __< k​ayabanerve:matrix.org >__ The libs discussed re: the contest really aren't an API concern     

> __< s​yntheticbird:monero.social >__ Extensive meme operation that only ccryptographer understand would be a first step imo /s     

> __< j​effro256:monero.social >__ Lol yeah that part is fine, I meant more of the higher level stuff, mainly in the monero-fcmp-plus-plus crate     

> __< c​haser:monero.social >__ xmrCicada     

> __< NorrinRadd >__ podcasts, ACM, cryptographer journals, cryptographer reddit / other social media accounts      

> __< k​ayabanerve:matrix.org >__ Also, jberman, while I recommended benching new and scalar_mul_divisor together, new should have a weight applied to it (I think 12/13) as we do 12 news but 13 smds.     

> __< b​asses:matrix.org >__ just annouce it on getmonero.org blog?     

> __< NorrinRadd >__ not enough exposure      

> __< a​ck-j:matrix.org >__ I agree but doing that is simply not enough to attract talent outside the Monero community     

> __< k​ayabanerve:matrix.org >__ So a solution with a 10s new and 1s divisor is explicitly better than a solution with a 0s new and 11s divisor     

> __< j​effro256:monero.social >__ I say this b/c sometimes seemingly-harmless API changes can open up crypto vulnerabilities, like the EdDSA double-pubkey oracle attack     

> __< b​asses:matrix.org >__ how about CTF platforms?     

> __< k​ayabanerve:matrix.org >__ That's why I baked all the vulnerabilities into the *existing* API jeffro /s     

> __< j​berman:monero.social >__ where does new get called without a corresponding scalar_mul_divisor?     

> __< k​ayabanerve:matrix.org >__ Other way around jberman     

> __< j​berman:monero.social >__ true, same q     

> __< k​ayabanerve:matrix.org >__ We do two smds off one new for a single scalar, the key image generator blind     

> __< k​ayabanerve:matrix.org >__ It's against U for the blinded key image but against V for the commitment to itself IIRC     

> __< k​ayabanerve:matrix.org >__ That's also why the two functions exist: to save that single preprocess.     

> __< j​berman:monero.social >__ ok, and also where do you get the figures 12/13 from? assuming specific number of layers + 1 input to the proof?     

> __< j​berman:monero.social >__ on marketing, does someone want to help take that on? :)     

> __< k​ayabanerve:matrix.org >__ Yeah. More inputs doesn't change the scaling here.     

> __< k​ayabanerve:matrix.org >__ We do 5 smds per input, and 1 per layer per input *except for the last layer*. Assuming 8 layers...     

> __< k​ayabanerve:matrix.org >__ (So 11 news, 12 smds actually, sorry)     

> __< j​berman:monero.social >__ ok will take a look at that     

> __< j​berman:monero.social >__ would like to get sign-off on helioselene-contest soonish too if possible     

> __< j​berman:monero.social >__ on general timeline, are we in rough agreement that we should wait for the contest before auditing?     

> __< j​effro256:monero.social >__ I think so     

> __< j​berman:monero.social >__ and also does anyone have thoughts on the general fund for this contest? sounds like I'm the only proponent of that here     

> __< k​ayabanerve:matrix.org >__ If everything else is audited, and contest results are over a month out, I'd advocate auditing as-is     

> __< r​ucknium:monero.social >__ I would prefer that XMR from the General Fund be used for the contest.     

> __< rbrunner >__ I also think "Why not"     

> __< c​haser:monero.social >__ sounds sensible to me too. of course, it's easy for me to support the spending of others' money :)     

> __< k​ayabanerve:matrix.org >__ Eh, it's kinda up to core and we don't have too much say even as the respected community. I also don't know the current balance of the fund so I can't advocate any fiscal policy regarding it     

> __< j​berman:monero.social >__ "If everything else is audited, and contest results are over a month out, I'd advocate auditing as-is" -> this seems reasonable to me. In this case, I would likely re-work wallet side tree building which would take me a couple weeks     

> __< a​ck-j:matrix.org >__ I could spear head that and look into our options. We have a long list of researchers on moneroresearch.info who I could reach out to and gauge interest.     

> __< r​ucknium:monero.social >__ Let the IRC record show that "I would prefer that XMR from the General Fund be used for the contest." was up-thumbed via Matrix emoji reaction by tobtoht , chaser , SyntheticBird ,  jberman , xmrack , and rottenwheel     

> __< j​berman:monero.social >__ As of last month, the GF has 15,747 XMR: https://www.reddit.com/r/Monero/comments/1iixgk9/monero_general_fund_transparency_report_february/     

> __< c​haser:monero.social >__ if Core overall is against it, a compromise could be an agreement to a retroactive funding CSS.     

> __< j​berman:monero.social >__ Proposed prizes total 350 XMR, so about 2% of the fund     

> __< c​haser:monero.social >__ thanks Rucknium, it's easy to forget that reactions aren't preserved for the current historical record     

> __< nioc >__ IMO binaryFate would be the one to contact about using the general fund     

> __< k​ayabanerve:matrix.org >__ I don't think we can offer a prize we don't have, unless you mean to replenish the GF?     

> __< c​haser:monero.social >__ kayabanerve yes, that's what I was thinking of. the GF in that case would serve as someone who loans the funds to the contest.     

> __< k​ayabanerve:matrix.org >__ Thank you for the clarification :)     

> __< r​ucknium:monero.social >__ We are 50 minutes into the meeting. Let's move into the second business item unless there is something urgent left to discuss on this one.     

> __< j​berman:monero.social >__ Summing up updates on the contest:     

> __< j​berman:monero.social >__ - rough agreement here to request the GF cover the contest     

> __< j​berman:monero.social >__ - I'm requesting review on helioselene-contest     

> __< j​berman:monero.social >__ - I'll make changes to ec-divisors-contest in line with kayaba's suggestions     

> __< j​berman:monero.social >__ - xmrack willing to take on marketing the contest :) thank you     

> __< r​ucknium:monero.social >__ 4) Release of OSPEAD HackerOne and CCS milestone submissions. https://github.com/Rucknium/OSPEAD     

> __< r​ucknium:monero.social >__ plowsof was able to reproduce the small simulation on his own machine, with a few bumps in the road: https://github.com/Rucknium/OSPEAD/issues/1     

> __< r​ucknium:monero.social >__ Here is the draft getmonero.org blog post: https://gist.github.com/Rucknium/e18c514f0ba7a6dc6c7f35f9c242a34a     

> __< a​rticmine:monero.social >__ I am currently working my way through the OSPEAD release.     

> __< r​ucknium:monero.social >__ Maybe this agenda item can be combined with the next one, which is "Possible intermediate hard fork before FCMP hard fork. ofrnxmr  , xenu  , elongated  "     

> __< v​tnerd:monero.social >__ does it need to be a hard-fork? could it just be a new release branch forked from master that is still compatible with 0.18 ?     

> __< a​rticmine:monero.social >__ I was going to mention this. It is actually the kind of feedback I got from my interview on the Crypto Show.     

> __< a​rticmine:monero.social >__ There is a case here depending on the timeline for FCMP++ to be active on the main chain     

> __< r​ucknium:monero.social >__ vtnerd: No, but a hard fork would be "safest" because they you don't have anonymity puddles where some users/wallets update to the new decoy selection algorithm, and others do not.     

> __< c​haser:monero.social >__ I was surprised to read about this initiative. is there have time for it without causing any delays to the FCMP++ fork rollout?     

> __< rbrunner >__ Hmmm. But that all is anyway only up to the FCMP++ hardfork     

> __< s​packle:monero.social >__ Regarding the concern about a small number of users updating; would a gradual migration of the DSA significantly mitigate the issue? An example might be to select x/15 decoys from the new distribution, with x = (blocks past the update)/10000 ? My naive assumption is that shifting the decoys slowly over a period of time would prevent people from immediately standing out, giving the<clipped message>     

> __< s​packle:monero.social >__  user base time to adopt the new DSA.     

> __< c​haser:monero.social >__ s/have//     

> __< v​tnerd:monero.social >__ if the hardfork is for decoy selection algorithm, its unlikely it can be enforced by any consensus rules     

> __< a​rticmine:monero.social >__ One can increase the ring size and implement the scaling changes as well as apply OSPEAD     

> __< r​ucknium:monero.social >__ I'll quote myself from before the meeting:     

> __< r​ucknium:monero.social >__ > The problem with partial userbase upgrade is anonymity puddles. for example, according to my calculations in https://github.com/Rucknium/misc-research/blob/main/Monero-Fungibility-Defect-Classifier/pdf/classify-real-spend-with-fungibility-defects.pdf , if only 5% of users upgraded to the OSPEAD decoy selection algorithm, the attack success probability against them would be 32% (<clipped message     

> __< r​ucknium:monero.social >__ assuming perfect classification by DSA), actually higher than the 23.5% attack success against the current DSA. That would be a net loss in privacy.     

> __< k​ayabanerve:matrix.org >__ Actual issue to raise. Can hardware wallets sign a ring size 100? Such a signature would be >3 KB. I'd also ask for 64 but would guess 32 is fine.     

> __< k​ayabanerve:matrix.org >__ I say 100 to make the issue clear.     

> __< rbrunner >__ I wouldn't dare dragging any hardware wallet issues into any possible intermediate hardfork ...     

> __< k​ayabanerve:matrix.org >__ My advocacy is to push FCMP++ through rather than spend time here.     

> __< a​rticmine:monero.social >__ I really match the future FCMP 2 in 2 out TX size     

> __< rbrunner >__ We want them spend time on implementing FCMP++, IMHO     

> __< a​rticmine:monero.social >__ The timeline for FCMP++ is important here.     

> __< k​ayabanerve:matrix.org >__ ArticMine: I don't think HWW can do that without chunking the proof.     

> __< rbrunner >__ I am more or less with kayabanerve here: An intermediate hardfork could become an unwelcome distraction     

> __< r​ucknium:monero.social >__ spackle: Interesting idea. Yet, we don't have a good idea how quickly the ecosystem updates. With more effort, we could get an idea from historical instances (e.g. the 2021 decoy selection changes).     

> __< a​rticmine:monero.social >__ Very good point     

> __< rbrunner >__ And hay, it may sound harsh, but we are living for so long with those badly selected decoys, what is half a year more?     

> __< k​ayabanerve:matrix.org >__ Libs are done besides audit responses and a couple of raised API issues. I'm starting solicitation for the next spread of audits.     

> __< k​ayabanerve:matrix.org >__ Where is CARROT and integration? 👀     

> __< j​effro256:monero.social >__ jberman and I are hard at work in the integration mines     

> __< j​effro256:monero.social >__ Sorry it is just a slog     

> __< r​ucknium:monero.social >__ But, IIRC, isthmus commented to me that he does not see good value in trying to use estimates of historical adoption pace to forecast a future one for a DSA change without a hard fork     

> __< j​berman:monero.social >__ I just used the CLI to make a FCMP++ tx, so progress is good     

> __< rbrunner >__ But such a gradual migration wants to be coded and tested, that would eat dev hours, and make things more complex     

> __< a​rticmine:monero.social >__ Half a year does not justify two hard forks.  A year is a different question     

> __< c​haser:monero.social >__ it's impossible to predict with high certainty how quick the adoption would be. with the potential for anonymity puddles, it seems like a risky endeavor.     

> __< k​ayabanerve:matrix.org >__ How's the protocol changes? Ideally minimal, with y'all suffering on the wallet?     

> __< a​rticmine:monero.social >__ Without a HF for something else we can't implement OSPEAD     

> __< rbrunner >__ Really? A simple dummy version change for some important struct, done?     

> __< a​rticmine:monero.social >__ The only question I see here then is: How far can we push the existing proof in ring size without starting to break things     

> __< j​effro256:monero.social >__ I'm personally spending a lot of time on tx construction with our current flow as well as planning a solid base for future work, like multisig and HW wallets. Pruned transaction format didn't actually change that much for Carrot/FCMP++, we just have a new variant for `cryptonote::tx_out`. The prunable transaction format is changing a lot though. Most of the protocol work AFAIK is <clipped messag     

> __< j​effro256:monero.social >__ the curve tree implementation, which is pretty hairy     

> __< r​ucknium:monero.social >__ Something also to consider: The proposed OSPEAD-derived DSA that reduces attack success probability to 7.6% was tested against a single aggregate real spend distribution (2022 - 2024). It was tested that way since I assumed that this would go into the node-wallet decoy system that FCMP uses as a backup.     

> __< r​ucknium:monero.social >__ When the target and the shield have to stay in the same place, the shooter has a lower probability of hitting the target. When the target moves (i.e. week-to-week movements in user behavior) and the shield doesn't move, then the shooter has higher probability of hitting the target. I would want to re-run things with week-to-week variation. I did that a while ago with earlier data <clipped message     

> __< r​ucknium:monero.social >__ and got attack success probability down to about 11% IIRC. That's higher than the 7.6%.     

> __< s​gp_:monero.social >__ Personally I see the time to have done this as two years ago, and it's not worth an aggressive change for rings at this stage. All efforts should be on fcmp++     

> __< r​ucknium:monero.social >__ The real spend age distribution can change a lot from week to week: https://rucknium.github.io/OSPEAD/CCS-milestone-2/OSPEAD-docs/_book/real-spend-visualization.html     

> __< rbrunner >__ articmine: I fear that we may "break" HW firmware coders' goodwill with forcing them to update their stuff two times in relatively short succession     

> __< rbrunner >__ Also any web wallets may have to adjust for any new ring size, and block explorers, and I am sure I forget something here now     

> __< rbrunner >__ Frankly, any hour spent into someting "ringy" at this point in time is basically wasted IMHO     

> __< r​ucknium:monero.social >__ In the previous hard fork in August 2022, many "third-party" wallets didn't update in time: https://github.com/Rucknium/misc-research/tree/main/Monero-Nonstandard-Fees#determining-which-wallets-are-creating-transactions-with-nonstandard-fees     

> __< a​rticmine:monero.social >__ If I understand correctly the wallet is obfuscating the real spend from a malicious node     

> __< r​ucknium:monero.social >__ They had downtime of weeks and months     

> __< r​ucknium:monero.social >__ ArticMine: Right, with FCMP. And the "decoy method" is a backup method if building the FCMP tree in the wallet fails for some reason (or a wallet implementer doesn't want to do it). There is also a further use of it for a type of LWS find-receive key, but that won't be ready at the time of the hard fork according to jberman     

> __< r​ucknium:monero.social >__ Won't be ready at the time of the FCMP hard fork, I mean     

> __< s​yntheticbird:monero.social >__ so... at my understanding loose consensus is that focusing on fcmp++ is better, right?     

> __< r​ucknium:monero.social >__ We are 30 minutes past the hour. We can end the meeting here. Feel free to continue discussing after the meeting.     

> __< c​haser:monero.social >__ SyntheticBird I would agree. a each new fork has a significant overhead, plus I'm reminded of something about moratorium on EC crypto.     

> __< a​rticmine:monero.social >__ Thanks for hosting     

> __< d​oedl...:zano.org >__ "anonymity puddles" sounds scary, but how scary exactly ?     

> __< s​yntheticbird:monero.social >__ imagine a puddle     

> __< s​yntheticbird:monero.social >__ and its anonymous     

> __< s​yntheticbird:monero.social >__ it's THAT scary     

> __< d​oedl...:zano.org >__ "anonymity puddles" sounds scary, but how scary exactly ? -- (this refers to a statistical attack differentiating 2 distinct selection algo's distribution patterns)     

> __< c​haser:monero.social >__ believe me, they're not good. this is a good presentation on anonymity puddles:     

> __< c​haser:monero.social >__ Mitchell Krawiec-Thayer "Isthmus" - Visualizing Monero: A Figure is Worth a Thousand Logs     

> __< c​haser:monero.social >__ https://odysee.com/@monerocommunityworkgroup:8/monerokon-2019-visualizing-monero-a:c     

> __< d​oedl...:zano.org >__ "anonymity puddles" sounds scary, but how scary exactly ? -- (this refers to a statistical attack differentiating 2 distinct selection algo's distribution patterns, resulting from a soft fork)     

> __< d​oedl...:zano.org >__ oh, odysee, nice. downloading...     

> __< o​frnxmr:monero.social >__ Sorry.. my monero.social client stopped working today     

> __< o​frnxmr:monero.social >__ The idea here is that the differences between monero's release branch and master. Pushing master at the same time as fcmp++ is likely to introduce more issues than were ready to deal with     

> __< o​frnxmr:monero.social >__ Imo we should release v0.19 (pushing master to release) before fcmp++, giving us a chance to release fcmp++ without the extra baggage.     

> __< e​longated:matrix.org >__ There is no guaranteed timeframe for the FCMP++ hard fork. We can’t just wait for it while having poor decoy selection. The hard fork for the new DSA can be completed by the end of the year, providing breathing room for FCMP++ development rather than rushing a product.     

> __< o​frnxmr:monero.social >__ And if we're pushing master -> release, i see no reason why we shouldnt include jeffro's coonbase segregation pr and potentially an ospead based DSA.     

> __< o​frnxmr:monero.social >__ +randomx v2. A "small" hard fork that doesnt have many/any breaking changes is a good way to "wake up" the ecosystem and prepare them for the fcmp++ HF.     

> __< o​frnxmr:monero.social >__ My suggested timeline, articmine:monero.social , is releasing HF binaries ~may-june, for a hard fork in aug-oct. By then, hopefully, we'll have a real FCMP++ testnet hard fork, and be ready to put out mainnet hard fork binaries by january (3-4 months after testnet HF), with FCMP++ HF height set for sone time between march-july 2026     

> __< o​frnxmr:monero.social >__ I don't agree with raising ring size or any other unnecessary changes. Coinbase segregation + randomxv2 + ospead (if viable) + master (obv).     

> __< o​frnxmr:monero.social >__ We should drop gitian, boost, whatever backport stuff were wasting time on with release-v0.18, and get master out on mainnet. And IMO if we plan things properly, we have a better chance to ensure that the rest of the ecosystem is prepared for fcmp, as theyll be "woken up" by the "small" hard fork     

> __< s​yntheticbird:monero.social >__ I'm not particularly for a hard fork. at the moment. I'm convinced with a burst of motivation and efforts FCMP++ testnet can be ready in May.     

> __< s​yntheticbird:monero.social >__ However I have to agree on the branch thingy.     

> __< s​yntheticbird:monero.social >__ Just ship master ffs     

> __< o​frnxmr:monero.social >__ The dsa doesnt require a hf, but would be best imo if we nudge pools and hww manufacturers to dust off their monero devs and get ready for fcmp++hf.     

> __< o​frnxmr:monero.social >__ master should bring small, non-breaking changes. Randomx includes an old, unaddressed h1     

> __< o​frnxmr:monero.social >__ Pushing master to release is simple, but i think we should include at least jeffros' coinbase segregation code. Its basically finished a long time ago. Already tested on mainnet     

> __< o​frnxmr:monero.social >__ fcmp needs audits, testnet, then like 6 months between binary release and hard fork height     



# Action History
- Created by: Rucknium | 2025-03-04T21:25:13+00:00
- Closed at: 2025-03-15T16:38:46+00:00
