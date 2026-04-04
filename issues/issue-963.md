---
title: Monero Research Lab Meeting - Wed 31 January 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/963
author: Rucknium
assignees: []
labels: []
created_at: '2024-01-31T17:02:53+00:00'
updated_at: '2024-02-07T16:58:36+00:00'
type: issue
status: closed
closed_at: '2024-02-07T16:58:36+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: How to confirm security of Monero's multisignature protocol? Do we need mathematical security proofs, and can we get them? Info:
- [Brandon Goodell and Sarang Noether (2018) "Thring Signatures and their Applications to Spender-Ambiguous Digital Currencies"](https://www.getmonero.org/resources/research-lab/pubs/MRL-0009.pdf)
- [Monero multi-signature patch review by Inference](https://community.rino.io/rino-multisig-pr8194-audit-20220627.pdf)
- [Rust alternative implementation](https://github.com/serai-dex/serai/blob/develop/coins/monero/src/wallet/send/multisig.rs) by @kayabaNerve

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

#959 

# Discussion History
## plowsof | 2024-02-04T19:33:35+00:00
Logs 
> __< r​ucknium:monero.social >__ MRL meeting in this room in two hours.     

> __< r​ucknium:monero.social >__ Meeting time! (oops, forgot to make the GitHub issue...)     

> __< rbrunner >__ Hello     

> __< v​tnerd:monero.social >__ hi     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< r​ucknium:monero.social >__ Here is the meeting GitHub issue: https://github.com/monero-project/meta/issues/963     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< v​tnerd:monero.social >__ me: spend a lot of time doing a review of jeffro256 changes to txpool handling, and continued slowly on lws "chain hardening". about 70% sure its worth hacking lws to do this, but without it you can easily spoof chains     

> __< v​tnerd:monero.social >__ the review of jeffro256 code looked good, but reverted some ZMQ "features"     

> __< r​ucknium:monero.social >__ Me: OSPEAD. isthmus will get me some data today probably. The processing "only" took a few hundreds of GB of RAM. I hope the hardware requirements can be reduced so that the analysis is easier to reproduce by others. The MAGIC Monero Fund approved the University of Zurich research group's EAE/churning research for a fundraising.     

> __< r​ucknium:monero.social >__ Once I get the isthmus data it takes about 5 days of additional processing. Then interpret the results.     

> __< rbrunner >__ https://monerofund.org/projects/ring_signature_ai gives me 500 Internal Server Error     

> __< v​tnerd:monero.social >__ yeah the funding site is down, I notified sgp about it about 20 minutes ago     

> __< rbrunner >__ Ok :)     

> __< r​ucknium:monero.social >__ uh oh. Ok we will try to fix. Thanks for telling us     

> __< rbrunner >__ But well, that's not even the Zurich fundraiser I think     

> __< r​ucknium:monero.social >__ no, it's not     

> __< v​tnerd:monero.social >__ yes, that link should be an older fundraiser     

> __< r​ucknium:monero.social >__ 3) Discussion. What do we want to discuss?     

> __< k​ayabanerve:matrix.org >__ I have misc more progress on Full Chain Membership Proofs, nothing to specifically note re: progress.     

> __< k​ayabanerve:matrix.org >__ Ideally, ideally, with Vector Commitments, we can get the bulletproof to     

> __< k​ayabanerve:matrix.org >__ 10 gates a scalar mul     

> __< k​ayabanerve:matrix.org >__ A few gates on misc     

> __< k​ayabanerve:matrix.org >__ n on set membership     

> __< k​ayabanerve:matrix.org >__ Such that we reach a power of 2 where n**p where p<6 > 500m.     

> __< k​ayabanerve:matrix.org >__ 50**5 is roughly that (with the power of 2 being 64).     

> __< k​ayabanerve:matrix.org >__ That'd make the cost of the FCMP roughly equal to 1 aggregate BP of 4 outs and 1 aggregate BP of 2 outputs (if my off-hand math is correct).     

> __< k​ayabanerve:matrix.org >__ Under current theory, ideally the FCMP circuit size will be halved from where it was prior (yet not at the above level).     

> __< k​ayabanerve:matrix.org >__ So performance of that is significantly improving re: theoretical architecture.     

> __< r​ucknium:monero.social >__ Nice. Does that affect verification time? Or the about the same verification time that you estimated earlier?     

> __< k​ayabanerve:matrix.org >__ Verification time is linear to circuit size, and this is all further improvement goals.     

> __< r​ucknium:monero.social >__ Pretty much the only think left to do with OSPEAD is to fit several distribution families to the real spend age data and pick the "best" one. Maybe someone has an opinion about which ones should be tried. I plan to fit a "small" number of distributions in total, but some of those distributions are generalizations of a large number of other distributions. i.e. if the parameter(s) o<clipped message     

> __< r​ucknium:monero.social >__ f a general distribution are set to particular values, it is equivalent to another more specialized distribution.     

> __< r​ucknium:monero.social >__ You can just search over the parameters space of the generalized distribution and you have "checked" if the specialized distribution fits better.     

> __< r​ucknium:monero.social >__ The two main generalized distributions that I will try are the Generalized Extreme Value and the Feller-Pareto distributions.     

> __< r​ucknium:monero.social >__ I will also try the Log-Gamma (the same family that we have now for decoys, but we will get different parameter values for the more accurate data). And the Noncentral F and Right-pareto Log-normal distributions.     

> __< r​ucknium:monero.social >__ I will mind the implementation complexity of these. If a more complex distribution is only slightly better in fit than a simple one, we may want to use the simple one.     

> __< v​tnerd:monero.social >__ I was just going to ask about that, because LWS is one of the few alternate implementations of decoy selection     

> __< r​ucknium:monero.social >__ Is there a list of probability distributions that can be easily added to the Monero codebase, like in `boost`?     

> __< s​gp_:monero.social >__ Yes, sorry about this. I'm not sure what happened :/ But I'm actively working on this\     

> __< r​ucknium:monero.social >__ Yes, so maybe if log-gamma with different parameters is almost as good as an alternative one, it is easier to just update those numbers in `wallet2` and other implementations that use log-gamma.     

> __< v​tnerd:monero.social >__ if its complex, at least provide a good re-usable API     

> __< v​tnerd:monero.social >__ there's boost accumulators and boost math that have statistics functions     

> __< v​tnerd:monero.social >__ thats about all I know, as I can't recall ever using either     

> __< rbrunner >__ No idea either.     

> __< r​ucknium:monero.social >__ The candidate distributions will be implemented in R. And some of those use C or C++ functions underneath. But many of them are licensed under GPL.     

> __< v​tnerd:monero.social >__ oh theres also boost special functions     

> __< v​tnerd:monero.social >__ ok so your providing the reference implementation in R, and one of the C++ programmers will have to port?     

> __< r​ucknium:monero.social >__ Maybe that is what would happen. The functions are defined mathematically. Even the most complex ones aren't hundreds of lines of code or anything.     

> __< v​tnerd:monero.social >__ that will work, there's a few people that can do a port (hopefully)     

> __< r​ucknium:monero.social >__ Some of them have better "documentation" than others. For example....     

> __< r​ucknium:monero.social >__ Feller-Pareto, which is probably the most general and most complex one: https://www.jstatsoft.org/article/view/v103i06     

> __< r​ucknium:monero.social >__ Has a whole article about how to implement, including numerical stability issues.     

> __< k​ayabanerve:matrix.org >__ There's also monero-serai which has its own implementation.     

> __< r​ucknium:monero.social >__ This replacement would be just for the random number generation. Generating a random output index. Then everything else about the decoy selection algorithm would be the same.     

> __< r​ucknium:monero.social >__ Like calculating the flow of outputs in the last year, etc     

> __< r​ucknium:monero.social >__ Anything more to discuss?     

> __< r​ucknium:monero.social >__ We can end the meeting here.     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2024-01-31T17:02:53+00:00
- Closed at: 2024-02-07T16:58:36+00:00
