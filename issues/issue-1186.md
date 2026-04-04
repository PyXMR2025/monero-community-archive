---
title: Monero Research Lab Meeting - Wed 09 April 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1186
author: Rucknium
assignees: []
labels: []
created_at: '2025-04-08T20:31:12+00:00'
updated_at: '2025-04-18T19:36:40+00:00'
type: issue
status: closed
closed_at: '2025-04-18T19:36:40+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Prize contest to optimize some FCMP cryptography code](https://github.com/j-berman/fcmp-plus-plus-optimization-competition).

4. FCMP alpha testnet, stressnet, and public testnet planning.

5. [Release of OSPEAD HackerOne and CCS milestone submissions](https://github.com/Rucknium/OSPEAD). [Analysis of risk of new decoy selection algorithm without a hard fork](https://gist.github.com/Rucknium/fb638bcb72d475eeee58757f754acbee).

6. Research on [subnet deduplication for peer selection](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf) to reduce spy node risk.

7. Any other business

8. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1182 

# Discussion History
## Rucknium | 2025-04-11T22:09:06+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1186     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< v​tnerd:monero.social >__ hi     

> __< rbrunner >__ Hello     

> __< j​berman:monero.social >__ *waves*     

> __*__ dukenukem waves     

> __< c​haser:monero.social >__ hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< j​effro256:monero.social >__ howdy     

> __< j​berman:monero.social >__ me (copying mostly from my NWLB update): FCMP++ optimization contest launched! (blog post: https://www.getmonero.org/2025/04/05/fcmp++-contest.html). Coordinating with xmrack on additional comms (reddit, twitter, and additional outreach)     

> __< j​berman:monero.social >__ Also finished including the FCMP++ tree root in the PoW hash for each block. After much discussion with jeffro256, I settled on an approach that I think is very solid (it won't materially affect miners creating new block templates nor normal sync), and also happened to be straightforward to implement     

> __< j​berman:monero.social >__ This week I'm working on implementing caching pre-built blinds in the wallet in the background (so that tx construction is near-instant). Blinds construction takes on the order of seconds and does not have to run at tx construction time (i.e. can be pre-cached). The FCMP++ contest (on divisors specifically) will hopefully speed this up by at least 2x, but even a 2x speed-up remain<clipped message>     

> __< j​berman:monero.social >__ s on the order of seconds without caching     

> __< j​berman:monero.social >__ I'm also nearly complete with my current CCS, and plan to open another shortly     

> __< r​ucknium:monero.social >__ me: Finished re-running the OSPEAD procedure on data updated to March 30, 2025. Also scrutinizing some things in the Clover paper (alternative to Dandelion++) that seem to not add up. Bouncing some ideas off boog900 about that.     

> __< v​tnerd:monero.social >__ me: working on lws-frontend - subaddress handling and importing from block height     

> __< j​effro256:monero.social >__ me: Carrot tx construction in wallet2 is more or less completed and tested for non-HW devices and non-multisig: https://github.com/seraphis-migration/monero/blob/1b1eba93611a29389193c9d779c8e8b2988a935f/tests/unit_tests/wallet_tx_builder.cpp#L240     

> __< j​effro256:monero.social >__ Working on CLI/RPC integration and coming up with a weight function for FCMP++ txs     

> __< a​rticmine:monero.social >__ Hi sorry I am late     

> __< r​ucknium:monero.social >__ 3) Prize contest to optimize some FCMP cryptography code.     

> __< r​ucknium:monero.social >__ Anything to discuss on this except that the contest is posted?: https://www.getmonero.org/2025/04/05/fcmp++-contest.html     

> __< dukenukem >__ jberman re: FCMP++ contest, sharing it in this Sunday's Revuo, FWIW. Added to notes. Last one had 9 news, packed, had to skip a couple for next one.     

> __< j​berman:monero.social >__ Thanks :)     

> __< j​berman:monero.social >__ If anyone knows who runs the monero twitter account, would be good to announce the contest soon-ish (perhaps spacing the announcement from the release news makes sense)     

> __< dukenukem >__ I'll ping them about that as well.     

> __< j​berman:monero.social >__ ty     

> __< dukenukem >__ They should be boosting MoneroKon's last call for CfP submissions and now this.     

> __< dukenukem >__ (Haven't heard back, but they will get to it, eventually.)     

> __< r​ucknium:monero.social >__ 4) FCMP alpha testnet, stressnet, and public testnet planning.     

> __< r​ucknium:monero.social >__ Is it the right time to be discussing this ^, or wait longer?     

> __< j​effro256:monero.social >__ I think that this is a good time. Alpha testnets should be ready in the coming weeks, and it's always better to test sooner rather that later     

> __< j​berman:monero.social >__ +1^ we're very close I'd say     

> __< r​ucknium:monero.social >__ tobtoht has created a private testnet and created FCMP txs, but without CARROT IIRC.     

> __< j​effro256:monero.social >__ There probably will be many small breaking consensus changes every couple days though, so participants should make sure to stay updated     

> __< j​effro256:monero.social >__ Yes it would probably be without CARROT     

> __< dukenukem >__ Yeah, Rucknium. See: https://files.catbox.moe/ivyria.png     

> __< dukenukem >__ "I rebased Feather on top of j-berman's fcmp++ staging branch and set up a private testnet. Mining works. Tx construction isn't fully working yet with carrot changes. Looking forward to shipping a beta as soon as public testnet goes live."     

> __< j​berman:monero.social >__ Perhaps we come back next week with target dates?     

> __< r​ucknium:monero.social >__ I can take a role in stressnet again. I would want to 1) Fork from the public testnet with both `monerod` and `cuprate` nodes, 2) Spam pre-FCMP txs to get a baseline of performance now that we have some improvements after the last stressnet. It would also test `cuprate` performance. 3) Fork to enable FCMP, which would likely drop `cuprate` nodes, 4) Spam FCMP txs. Probably 1-2 months of stressnet     

> __< r​ucknium:monero.social >__ jberman: Sounds good.     

> __< r​ucknium:monero.social >__ We can probably get at least as many community participants in running stressnet nodes as last year.     

> __< j​berman:monero.social >__ FCMP++ stressnet pre-contest and post-contest would also be interesting     

> __< j​effro256:monero.social >__ Should we "rollback" the testnet or create a straight fork from the current chain tip?     

> __< r​ucknium:monero.social >__ Do you thinking the contest timeline should factor into the stressnet launch date?     

> __< r​ucknium:monero.social >__ jeffro256: For stressnet? I think we would do a fork from current chain tip.     

> __< r​ucknium:monero.social >__ If for the public testnet, I'm not sure     

> __< j​berman:monero.social >__ Public testnet would just have a future fork height hard-coded into the daemon, same as we've done it in the past     

> __< j​effro256:monero.social >__ I think this would probably be a good idea so we can get a semi-realistic look into the performance for tree building on a (almost) real database with many tx outputs     

> __< r​ucknium:monero.social >__ Sounds good. That's how the last stressnet worked, too.     

> __< j​berman:monero.social >__ a note fwiw, tree building code currently builds from genesis, so you could also migrate a current mainnet with the tree building code and it'll build the tree from genesis     

> __< j​berman:monero.social >__ on mainnet     

> __< rbrunner >__ Which will take quite a while, I guess?     

> __< j​berman:monero.social >__ it was on the order of several hours on my solid machine last I checked     

> __< j​berman:monero.social >__ "Do you thinking the contest timeline should factor into the stressnet launch date?" -> assuming you meant other way around here, I think a wait-and-see is fine for when the code is actually for a stressnet     

> __< j​berman:monero.social >__ is actually ready for*     

> __< j​berman:monero.social >__ (nvm you did not mean other way around, read it wrong sorry)     

> __< r​ucknium:monero.social >__ Sounds good. So let's bring back some rough dates for next week's meeting.     

> __< r​ucknium:monero.social >__ 5) Release of OSPEAD HackerOne and CCS milestone submissions. Analysis of risk of new decoy selection algorithm without a hard fork. https://github.com/Rucknium/OSPEAD https://gist.github.com/Rucknium/fb638bcb72d475eeee58757f754acbee     

> __< r​ucknium:monero.social >__ To get a more realistic real spend distribution for analyzing OSPEAD deployment risk, I re-ran the OSPEAD procedure with data updated to March 30, 2025.     

> __< r​ucknium:monero.social >__ There isn't a big difference in the results for OSPEAD deployment risk, using the classification procedure I've previously described.     

> __< r​ucknium:monero.social >__ Also, this time I tried to fit a `wallet2` distribution by optimizing over its gamma distribution parameters, with its re-allocation of the 10 block lock region to the `RECENT_SPEND_WINDOW`. This was following spackle 's suggestion to see if we can do the absolute minimum code changes, but just changing `GAMMA_SHAPE` and `GAMMA_RATE`.     

> __< r​ucknium:monero.social >__ I did not really get good results from that. The probability of MAP Decoder attack success against the aggregate real spend distribution with the `wallet2`-fitted distribution was 12%, but other distributions got as low as 7.5%. (Minimum possible is 1/16 = 6.25%     

> __< r​ucknium:monero.social >__ Maybe the fit was poor because:     

> __< r​ucknium:monero.social >__ 1) Maybe `RECENT_SPEND_WINDOW` should be a mutable parameter in the optimization procedure. That might make the optimization less stable because the objective function would have flat sections between the `RECENT_SPEND_WINDOW`'s integer-valued parameter space.     

> __< r​ucknium:monero.social >__ 2) Maybe the initial values in the optimization procedure could have been chosen better. Sometimes an optimizer will find a local minimum instead of the global minimum. With other distributions, I used a Maximum Likelihood Estimate to get initial values, but the `wallet2`distribution is not standard, so I had to approximate.     

> __< r​ucknium:monero.social >__ If I cannot find a way to get a better fit, then it would be best to revert the 2021 changes to the `wallet2` decoy selection algorithm and then have a "clean slate" distribution put in its place, IMHO.     

> __< r​ucknium:monero.social >__ The next step is to get the OSPEAD deployment risk training data into a good form that could be plugged into xmrack  's machine learning procedures:     

> __< r​ucknium:monero.social >__ https://github.com/ACK-J/Monero-Dataset-Pipeline/tree/main/DataScience     

> __< r​ucknium:monero.social >__ That's my update.     

> __< a​ntilt:we2.ee >__ as mentioned RECENT_SPEND_WINDOW's rather flat distribution I see as standing out.     

> __< j​effro256:monero.social >__ Rucknium do you happen to know why the `RECENT_SPEND_WINDOW` design decision was made in our current code?     

> __< r​ucknium:monero.social >__ jberman would be able to tell you his thought process.     

> __< a​ntilt:we2.ee >__ This is still not touched, right? (in the code it's a conditional)     

> __< j​berman:monero.social >__ This comment explains it: https://github.com/monero-project/monero/blob/3b01c490953fe92f3c6628fa31d280a4f0490d28/src/wallet/wallet2.cpp#L1055-L1079     

> __< r​ucknium:monero.social >__ AFAIK, it was an improvisation. It fixed the problem of the distribution being pushed back to chain tip, and then re-allocating it where it was needed most     

> __< j​effro256:monero.social >__ Oh I remember reading this part of the code, I just forgot derrr.. Thank you     

> __< r​ucknium:monero.social >__ flip flop: IMHO, the recent spend window idea isn't optimal, yes. It would be kept if it would be desired to keep code changes to absolute minimum     

> __< j​berman:monero.social >__ TL;DR the original paper didn't account for Monero's default unlock time, the suggested gamma shape and rate factored in the period in that window,  the original code was throwing away selections from that period, RECENT_SPEND_WINDOW is meant to ad hoc factor in that window     

> __< a​ntilt:we2.ee >__ >"So it returns an output that falls between 0 and the RECENT_SPEND_WINDOW." - this seems to be a practical issue     

> __< a​ck-j:matrix.org >__ I heard back from Kaggle. Their fee to host a contest is a flat 100k USD fee with a minimum 50k prize pool…     

> __< r​ucknium:monero.social >__ This is what I said back then: https://github.com/monero-project/monero/pull/7821#issuecomment-900763942     

> __< r​ucknium:monero.social >__ > From a statistical perspective, I support the latest version. What is accomplished here is "thickening" the probability density function of the selection algorithm in the section closest to zero. This more closely mimics the observed distribution of mixins + real spends. However, in the near future it is crucial that we consider moving away from the current selection algorithm t<clipped message     

> __< r​ucknium:monero.social >__ hat is based on Moser et al. 2018. I have some ideas about how to accomplish this.     

> __< a​ck-j:matrix.org >__ They wont do advertising for us, I dont believe     

> __< a​ck-j:matrix.org >__ *They wont allow us to buy advertising     

> __< j​berman:monero.social >__ "I heard back from Kaggle. Their fee to host a contest is a flat 100k USD fee with a minimum 50k prize pool…" -> haha, people pay 100k to list a contest with a prize pool of <100k? That doesn't make sense     

> __< r​ucknium:monero.social >__ Thank you xmrack     

> __< a​ck-j:matrix.org >__ Np, it was a long shot anyways     

> __< j​effro256:monero.social >__ subtle forshadowing     

> __< r​ucknium:monero.social >__ 6) Research on subnet deduplication for peer selection to reduce spy node risk. https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf     

> __< r​ucknium:monero.social >__ This update is actually based on work I did a while ago, but previous meetings were packed. It's about the protocol's decision to perform subnet deduplication or not, and the adversary's decision to rent IP address in subnet bulk or in distinct subnets.     

> __< r​ucknium:monero.social >__ I don't know if this is more than a footnote or technical curiosity:     

> __< r​ucknium:monero.social >__ According to more work I did on this, I think that both the adversary and the honest nodes use mixed strategies in the Nash equilibrium. A mixed strategy occurs when a player randomly chooses multiple strategies to actually play, usually with unequal probability between the strategies.     

> __< r​ucknium:monero.social >__ It may seem counterintuitive that players choose a strategy randomly, but it's an essential part of the Nash equilibrium concept. John Nash proved that every game has _at least one_ Nash equilibrium. However, there may be multiple Nash equilibria and the players might have to use mixed (randomized) strategies.     

> __< r​ucknium:monero.social >__ Anyway, I am putting together one or more MoneroKon talk proposals. Does a talk on spy nodes and countermeasures sound like a good idea?     

> __< r​ucknium:monero.social >__ Maybe jointly with boog900  if he wants?     

> __< c​haser:monero.social >__ I think it'd make a good talk topic     

> __< r​ucknium:monero.social >__ I may do OSPEAD, too, but there are tricky rules involved if I want to also submit OSPEAD to a journal like PoPETS.     

> __< j​effro256:monero.social >__ Yeah I'm terrible at statistics but the adversarial statistic-based games is really fascinating to me     

> __< rbrunner >__ Talk on spy nodes and strategies sounds good     

> __< r​ucknium:monero.social >__ 👍. Probably not much more than I have already discussed here and in my draft research note, but this is for the general Monero community audience, too. Talks can also impose some communication "discipline".     

> __< r​ucknium:monero.social >__ Any other items to discuss?     

> __< a​ntilt:we2.ee >__ ruck: IIRC your proposed solution (pseudo-code) already reached broad consensus ~4 weeks ago ?     

> __< r​ucknium:monero.social >__ flip flop: On subnet deduplication?     

> __< r​ucknium:monero.social >__ Oh, one more thing     

> __< a​ntilt:we2.ee >__ yep     

> __< b​oog900:monero.social >__ sure, I'll be down for that :)     

> __< r​ucknium:monero.social >__ I asked Claudia Diaz, longtime network privacy researcher, about our spy node problems: https://discuss.privacyguides.net/t/nym-and-nymvpn-next-gen-privacy-with-mixnet-and-vpn-service/25072/72     

> __< r​ucknium:monero.social >__ > About the spies, that’s a tough problem! if the spies are really smart they may be able to stay undetected since these are passive attacks. However if they made some mistake or tried used multiple nodes running in the same place, well, removing or avoiding them seems a sensible thing to do (but they may come back better hidden though).     

> __< r​ucknium:monero.social >__ Also asked her about Clover, and she said she hasn't read the paper.     

> __< r​ucknium:monero.social >__ flip flop: Probably, it would be good to discuss how to implement subnet deduplication in code and when it could be deployed. Maybe the next `monerod` release.     

> __< a​ntilt:we2.ee >__ tbh we assumed they are rather stupid - and stick to their IPs...     

> __< a​ntilt:we2.ee >__ tbh we assumed they are rather stupid - and stick to their IPs... [ which is not a bad assumption if we are dealing with bureaucracies ]     

> __< r​ucknium:monero.social >__ I don't know if Monero is their main target, or if BTC is the main target and they are just re-using the same IPs as their BTC spy nodes.     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< a​rticmine:monero.social >__ Thanks     

> __< a​ntilt:we2.ee >__ I had argued back then, that even then [ if they are fexible and switch IPs ] it could improve resiliency     

> __< r​ucknium:monero.social >__ flip flop: I think so, too. If by "resiliency" we mean robustness to blocking of Monero nodes in certain subnets. AFAIK, that's the main reason that BTC people use their ASmap. Not because of privacy, but for resistance against censorship and network partitioning attacks.     

> __< a​ntilt:we2.ee >__ ... and impl should be straight foreward. (jeffro256:monero.social said)     

> __< a​ck-j:matrix.org >__ Looks like monero twitter account is listening and tweeted out the competition :)     



# Action History
- Created by: Rucknium | 2025-04-08T20:31:12+00:00
- Closed at: 2025-04-18T19:36:40+00:00
