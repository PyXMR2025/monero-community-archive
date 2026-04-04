---
title: Monero Research Lab Meeting - Wed 13 August 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1254
author: Rucknium
assignees: []
labels: []
created_at: '2025-08-12T21:33:07+00:00'
updated_at: '2025-08-23T16:34:56+00:00'
type: issue
status: closed
closed_at: '2025-08-23T16:34:56+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf).

4. [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).

5. [Spy nodes](https://github.com/monero-project/research-lab/issues/126).

6. PoW mining pool centralization. [Monero Consensus Status](https://moneroconsensus.info/). [Bolstering PoW to be Resistant to 51% Attacks, Censorship, Selfish Mining, and Rented Hashpower](https://github.com/monero-project/research-lab/issues/136). [Mining protocol changes to combat pool centralization](https://github.com/monero-project/research-lab/issues/98).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1250 

# Discussion History
## ghost | 2025-08-13T09:48:28+00:00
@Rucknium Could you please prioritize # 6 above the other points?
I think I speak for a lot of people here saying this issue is quite concerning & requires immediate attention since a successful attack on the network would result in the loss of trust in the ecosystem and once lost, it'll be nearly impossible to get back. At the time of writing, a 6-7 block reorg was demonstrated to have happened in the past few days thanks to your amazing tools & work with the help of other devs. A solution to this problem is needed yesterday & frankly monero should've addressed this issue a long time ago considering the historical progress in this field of research.


## cyborg2384 | 2025-08-13T13:32:54+00:00
@Rucknium Yes # 6 seems the most important issue given recent events, especially discussing the option of raising tx fees as a measure to mitigate the risk of selfish mining. The game theory seems solid to me, how it rewards honest miners at the expense of those who mine empty blocks and also how it could simply attract more hash power to the ecosystem, which would be a big positive.

## Rucknium | 2025-08-13T15:12:44+00:00
@lancilloties @cyborg2384 : Thanks for your input and interest in the issues here. I usually prefer to put items that will have a long discussion with indefinite end as the last item on the agenda so I don't have to artificially terminate the conversation to turn to other agenda items. If everything goes well, we can get through the first agenda items quickly and leave plenty of time for discussion of mining centralization.

## ghost | 2025-08-13T15:17:15+00:00
@Rucknium while I'm at it, you should know there's an official discord now & it would be really cool to have you there :) a lot of people there are using your tools/research & appreciating them. Also, thanks for addressing our concerns.

## Rucknium | 2025-08-14T21:14:38+00:00



> __< r​ucknium:monero.social >__ This may be an unusual meeting. On the agenda is PoW mining pool centralization: https://github.com/monero-project/meta/issues/1254     

> __< r​ucknium:monero.social >__ This topic is fundamental to the Monero project. I will request more structure than usual for that agenda item.     

> __< r​ucknium:monero.social >__ The purpose of the discussion at _this_ meeting is not to decide any changes to Monero's consensus protocol and blockchain security model, but to start to plot out an Research & Development plan toward addressing weaknesses, both theoretical and empirical.     

> __< r​ucknium:monero.social >__ I propose that the structure of the discussion on the mining centralization agenda item be:     

> __< r​ucknium:monero.social >__ 1) I anticipate that there may be more readers and writers than at a usual MRL meeting. Therefore, start by stating your relationship to the Monero project and areas of knowledge/expertise (if any). "Ordinary user" is a fine response. Participation by new participants is fine and encouraged.     

> __< r​ucknium:monero.social >__ 2) State what you consider to be the major problem(s) with Monero's consensus protocol and blockchain security model, if you think there are any problems. This includes problems that have actually occurred and theoretical problems that are possible but have not yet occurred. Do not respond to each other at this point in time.     

> __< r​ucknium:monero.social >__ 3) State what you consider to be Monero's ideological and ethical principles, especially as they are relevant to potential solutions to mining pool centralization. Feel free to rank the importance of these principles. Again, don't respond to each other at this point in time.     

> __< r​ucknium:monero.social >__ 4) General open-ended discussion on potential solutions to the mining pool centralization problem.     

> __< r​ucknium:monero.social >__ (Don't post these now. Wait until the mining centralization agenda item comes up.)     

> __< r​ucknium:monero.social >__ If anyone has suggestions for this structure, please suggest them.     

> __< k​ayabanerve:matrix.org >__ Of course Rucknium:     

> __< a​rticmine:monero.social >__ I would suggest that we separate the discussion between:     

> __< a​rticmine:monero.social >__ 1) Improvements and fixes to the existing POW., both at consensus and node relay      

> __< a​rticmine:monero.social >__ 2) The introduction of non POW consensus mechanisms such as but not limited to      

> __< a​rticmine:monero.social >__ Trusted Execution Environments     

> __< a​rticmine:monero.social >__ Proof of Stake Hybrid solutions      

> __< a​rticmine:monero.social >__ Other non POW consensus solutions     

> __< a​rticmine:monero.social >__ 2) Is way more controversial than 1)     

> __< a​rticmine:monero.social >__ So we should start with 1)     

> __< r​ucknium:monero.social >__ ArticMine: That sounds great to me. Can I insert your two bullet points into my #4 above?     

> __< a​rticmine:monero.social >__ Of course     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1254     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< a​rticmine:monero.social >__ Hi     

> __< b​oog900:monero.social >__ hi     

> __< rbrunner >__ Hello     

> __< c​haser:monero.social >__ hello     

> __< s​pirobel:kernal.eu >__ hi     

> __< s​gp_:monero.social >__ Hello     

> __< v​tnerd:monero.social >__ Hi     

> __< h​bs:matrix.org >__ Hi     

> __< s​packle:monero.social >__ hello     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Improvements to https://moneroconsensus.info/ , which monitors orphaned blocks and mining pool centralization. Writing up simulation results for questions on review of PR #9939 "p2p: Improved peer selection with /24 subnet deduplication to disadvantage 'spy nodes'" https://github.com/monero-project/monero/pull/9939 (Will post an hour or two after the meeting).     

> __< wownero_maxi >__ hello     

> __< a​fungible:matrix.org >__ Greetings. Looking forward to the meeting discussion.     

> __< a​rticmine:monero.social >__ Me working on the fee calculations.     

> __< a​rticmine:monero.social >__ The results are posted after the size estimates     

> __< r​ucknium:monero.social >__ 3) [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf).     

> __< a​rticmine:monero.social >__ https://github.com/seraphis-migration/monero/issues/44     

> __< a​rticmine:monero.social >__ I posted the link s to the fee results here     

> __< o​frnxmr:monero.social >__ bug hunting & testing some fcmp stuff     

> __< a​rticmine:monero.social >__ The enforcement of the requirement that all transactions are economical to mine regardless of size is the basis for the calculations     

> __< a​rticmine:monero.social >__ We have to take into account the quadratic nature of the penalty     

> __< o​frnxmr:monero.social >__ my kiss take on fcmp fees/scaling: for fcmp fees i think we should do.. same 300kb standard median. larger txs mean fees will bump up to "normal" tier more often. Unimportant fee = 0.00002xmr per (input+output), other tiers same multipliers as current     

> __< a​rticmine:monero.social >__ This more than compensates for the verification time costs     

> __< o​frnxmr:monero.social >__ The verification is linear per input afaict     

> __< a​rticmine:monero.social >__ Keeping the median unchanged failed in 2017     

> __< wownero_maxi >__ Long-time XMR user here. By XMR user, I mean I actually use it as a currency. I also mine. I have also attended Monerotopia. I typically take a hands-off approach, but in this instance, I'd be remiss not to speak up for other silent XMR users and encourage cypherpunk and decentralized values. It's easier to keep liberty we have, than to regain it once it's lost. I look forward to hearing      

> __< wownero_maxi >__ everyone out. That is all.     

> __< s​yntheticbird:monero.social >__ wrong chat     

> __< s​yntheticbird:monero.social >__ => #monero     

> __< c​haser:monero.social >__ maybe wrong agenda item     

> __< r​ucknium:monero.social >__ This would be the right chat if it were during the mining centralization item, which comes later     

> __< s​yntheticbird:monero.social >__ mea culpa all rights to the moderator, Rucknium our supreme leader     

> __< wownero_maxi >__ sorry. Please continue     

> __< o​frnxmr:monero.social >__ wdym?     

> __< o​frnxmr:monero.social >__ In 2017, didnt tx sizes decrease? I dont recall the history of the median changes     

> __< r​ucknium:monero.social >__ This? https://www.getmonero.org/2017/12/11/A-note-on-fees.html     

> __< a​rticmine:monero.social >__ The transactions were to big to scale so were stuck. A second hard fork was needed to fix the issue     

> __< o​frnxmr:monero.social >__ I'm running fcmp right now with 8mb blocks (15mb at peak)     

> __< a​rticmine:monero.social >__ Basically if one increases the tx size by a factor of 3 then the base has to increase by a factor of 3. Fees then stay the same     

> __< r​ucknium:monero.social >__ Was it that a large tx could not fit in a block when the block size median had not been raised yet?     

> __< a​rticmine:monero.social >__ The fees get very high     

> __< a​rticmine:monero.social >__ This is good to know     

> __< a​rticmine:monero.social >__ It means that the proposal increase in the base median makes sense     

> __< a​rticmine:monero.social >__ Take a look at the 128 input TXs to see what I meam     

> __< a​rticmine:monero.social >__ The key ratio is tx weight/ long term median     

> __< r​ucknium:monero.social >__ I will keep the meeting moving...     

> __< r​ucknium:monero.social >__ 4) [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).     

> __< r​ucknium:monero.social >__ AFAIK, ofrnxmr has been trying to trigger bugs on his private testnet.     

> __< r​ucknium:monero.social >__ So that an alpha stressnet can begin.     

> __< r​ucknium:monero.social >__ Will the alpha stressnet fork from the public testnet, like the last stressnet, or start from genesis?     

> __< r​ucknium:monero.social >__ I think for the "public stressnet", fork from testnet would be good because performance issues could develop when the blockchain already has some GB in it.     

> __< r​ucknium:monero.social >__ jberman and jeffro256  aren't here right now to give an idea of how they view the exact launch process. But ofrnxmr  could take the lead maybe. That would take some labor off their shoulders.     

> __< j​effro256:monero.social >__ Oops sorry, thanks for the ping     

> __< a​rticmine:monero.social >__ This also impacted the fee discussion     

> __< j​effro256:monero.social >__ I haven't looked at Artic's recent comments on the tx weight GH issue, but I'm going to do that today.     

> __< j​effro256:monero.social >__ Rn I'm reviewing and testing the 128-in FCMP++ PR, seems good so far. The contest code is more or less ready to go for usage in the stressnet. I think that we could start planning the date for the stressnet now, but I might hold off until j-berman is here     

> __< o​frnxmr:monero.social >__ "Will the alpha stressnet fork from the public testnet, like the last stressnet, or start from genesis?" << mine starts from genesis, _but_ the fees are different pre-tail emission     

> __< a​rticmine:monero.social >__ There was a major spike in fees in 2017 with the introduction of ring ct     

> __< a​rticmine:monero.social >__ Tx size ~13500 bytes for 2 in 2 out     

> __< r​ucknium:monero.social >__ Ok. The stressnet launch planning discussion can occur outside of the meeting time, especially so jberman  can give input.     

> __< o​frnxmr:monero.social >__ Jeffro, i'm also running the 128in pr. I think this shoukd definitely be included in stressnet     

> __< j​effro256:monero.social >__ Forking from an existing network would yield more accurate DB migration times, more accurate FCMP tree handling times, etc. However, it might be an overhead that outweights its benefits     

> __< v​enture:monero.social >__ sorry, to chime in.. but it burns to ask.. was it not decided to restrict 8-in, 8-out (fan-in/fan-out) for FCMP? why these 128-in fee calcs? please ignore if it's out of place     

> __< j​effro256:monero.social >__ Rucknium: at what chain size would it not be worth it in your opinion to use an existing network ?     

> __< o​frnxmr:monero.social >__ I'm going to get my blocks up to ~20+mb and then share my binaries so rucknium and others can try it out     

> __< o​frnxmr:monero.social >__ Jeffro, testnet is only abt 7gb iirc. My db is around 1gb currently     

> __< o​frnxmr:monero.social >__ (But those 7gb take like 12hrs to sync.. )     

> __< j​effro256:monero.social >__ What seems to be a rough agreement right now is to allow >8-in/8-out txs at the consensus level, but require PoW to *relay* larger txs in the mempool     

> __< r​ucknium:monero.social >__ jeffro256: I don't know. I like forking from testnet since as ofrnxmr  said, the fees and scaling, etc. And it was not difficult to do it last stressnet (but the code has changed a lot with FCMP, of course).     

> __< j​effro256:monero.social >__ Probably b/c there are hardly any peers     

> __< o​frnxmr:monero.social >__ no, due to checkpoints     

> __< o​frnxmr:monero.social >__ Lack-of*     

> __< j​effro256:monero.social >__ Or lack thereof?     

> __< r​ucknium:monero.social >__ Didn't new testnet checkpoints get added?     

> __< o​frnxmr:monero.social >__ Not to the monero-project. We only added them to the stressnet     

> __< j​effro256:monero.social >__ Okay let's do that     

> __< r​ucknium:monero.social >__ 5) [Spy nodes](https://github.com/monero-project/research-lab/issues/126).     

> __< j​effro256:monero.social >__ That's interesting, I wouldn't have thought that it would take that long to verify 7GB worth of tx proofs, but I haven't ever actually profiled it     

> __< r​ucknium:monero.social >__ jeffro256:  had a question about simplification of the code in github.com/monero-project/monero/pull/9939 to have the "already-connected" subnet qualification to be made at the `/24` subnet level instead of the current `16` level. According to my simulations, it makes very little difference given the current network structure, assuming the spy nodes found by boog900     

> __< j​effro256:monero.social >__ (for testnet w/o checkpoints at least)     

> __< b​oog900:monero.social >__ its all the PoW hashes too     

> __< r​ucknium:monero.social >__ When honest nodes have the default 12 outbound connections, setting the "already-connected" subnet qualification to the `/16` subnet level gets you an average of 1.048 connections to the spy nodes. When it is `/24`, the average is 1.064. A very small increase.     

> __< r​ucknium:monero.social >__ I will post teh write-up and code on the PR     

> __< rbrunner >__ TIA     

> __< r​ucknium:monero.social >__ Like I said before the meeting, I want some structure in the next agenda item on mining pool centralization.     

> __< r​ucknium:monero.social >__ The purpose of the discussion at _this_ meeting is not to decide any changes to Monero's consensus protocol and blockchain security model, but to start to plot out a Research & Development plan toward addressing weaknesses, both theoretical and empirical.     

> __< j​effro256:monero.social >__ But there is also geographical distribution concerns also, not related to spy nodes. How does going from /16 to /24 affect that? A less diverse set of already-connected peers might slow down tx&block propagation for those farthest away from the "center" of the node graph     

> __< r​ucknium:monero.social >__ jeffro256: I can look into that. I have the actual IP addresses of a network scan, so I can translate that into geography     

> __< r​ucknium:monero.social >__ Thanks     

> __< r​ucknium:monero.social >__ For the next agenda item:     

> __< r​ucknium:monero.social >__ 1) I anticipate that there may be more readers and writers than at a usual MRL meeting. Therefore, start by stating your relationship to the Monero project and areas of knowledge/expertise (if any). "Ordinary user" is a fine response. Participation by new participants is fine and encouraged.     

> __< j​effro256:monero.social >__ Thank you for doing that     

> __< r​ucknium:monero.social >__ 2) State what you consider to be the major problem(s) with Monero's consensus protocol and blockchain security model, if you think there are any problems. This includes problems that have actually occurred and theoretical problems that are possible but have not yet occurred. Do not respond to each other at this point in time.     

> __< r​ucknium:monero.social >__ 3) State what you consider to be Monero's ideological and ethical principles, especially as they are relevant to potential solutions to mining pool centralization. Feel free to rank the importance of these principles. Again, don't respond to each other at this point in time.     

> __< r​ucknium:monero.social >__ 4) General open-ended discussion on potential solutions to the mining pool centralization problem. The discussion will proceed:     

> __< r​ucknium:monero.social >__ 1) Improvements and fixes to the existing POW., both at consensus and node relay     

> __< r​ucknium:monero.social >__ 2) The introduction of non POW consensus mechanisms such as but not limited to A) Trusted Execution Environments, B) Proof of Stake Hybrid solutions, C) Other non POW consensus solutions     

> __< r​ucknium:monero.social >__ Agenda item:     

> __< r​ucknium:monero.social >__ 6) PoW mining pool centralization. [Monero Consensus Status](https://moneroconsensus.info/). [Bolstering PoW to be Resistant to 51% Attacks, Censorship, Selfish Mining, and Rented Hashpower](https://github.com/monero-project/research-lab/issues/136). [Mining protocol changes to combat pool centralization](https://github.com/monero-project/research-lab/issues/98).     

> __< a​ntilt:we2.ee >__ could we agree on jeffro256 proposed changes now ?     

> __< r​ucknium:monero.social >__ The context of this is Qubic's selfish mining strategy where they have perfromed a few blockchain re-organizations recently. One was 7 blocks deep.     

> __< k​ayabanerve:matrix.org >__ FCMP++ R&D     

> __< k​ayabanerve:matrix.org >__ Serai Developer     

> __< k​ayabanerve:matrix.org >__ PoW vulnerability to coordinated actors at scale risking double spends and censorship.     

> __< k​ayabanerve:matrix.org >__ Decentralization and privacy.     

> __< a​rticmine:monero.social >__ I have been involved with the Monero project since 2014 and with POW mining since 2011 Have worked on Monero scaling and have been on the core team since 2016     

> __< r​ucknium:monero.social >__ 1) Me: I have been providing research analysis for Monero's privacy and security for about four years. I am an empirical microeconomist. My areas of knowledge are statistics, economics, and game theory. I have chaired the weekly MRL meetings for a while.     

> __< c​haser:monero.social >__ 1] Monero Research Lab regular and researcher of blockchain technologies in general.     

> __< rbrunner >__ 1) Monero dev since 2017. Chair of the weekly Monero Tech Meetings. Frequent poster in the Monero subreddit.     

> __< o​frnxmr:monero.social >__ 1. ofrnxmr. Monero abuser     

> __< o​frnxmr:monero.social >__ 2. ability to invalidate txs w/ a deep enough reorg, and no "rules" or protections against it. Exampke: we have a 10 block lock, but there is no enforcement that 10 blocks are actually final     

> __< o​frnxmr:monero.social >__ 3. payments. reliable and immutable.     

> __< c​haser:monero.social >__ 2] I see two factors regarding Monero's current consensus that create a problem: 1) the mining algorithm is geared toward general-purpose hardware which is easy to access/rent, 2) the reward issuance in dollar terms is currently low both relative to other cryptos and the global availability of general-purpose hardware. these make attacks in the Nakamoto consensus (e.g. selfish min<clipped message>     

> __< c​haser:monero.social >__ ing, or a 51% attack,) more feasible than desired.     

> __< a​rticmine:monero.social >__ I see the Qubic situation as an attack on Monero's decentralization. There is also a lot of history since the principals in Qubic were also related to Bytecoin, an over 83% pre mine from which Monero was forked in 2014     

> __< a​rticmine:monero.social >__ There is a lot of history and bad blood here     

> __< r​ucknium:monero.social >__ 2) Problems: Low security budget at the current real purchasing power of 1 XMR. Behavior of individual miners to concentrate in a few pools (unclear why this occurs). Using a "flow" to protect a "stock", i.e. only a flow of PoW rewards protects the stock of the value that users keep in the XMR in their possession.     

> __< a​ntilt:we2.ee >__ 1] scientist: physical modeling with recursive filter networks     

> __< kanzure >__ is there a reasonably good writeup of the reorgs and, in particular, the contents of the reorgs and transaction equivalency (or lack thereof)?     

> __< s​gp_:monero.social >__ Longtime user     

> __< s​gp_:monero.social >__ I wish to keep the majority of Monero's PoW advantages and ethos, while strategically mitigating some of the most significant downsides of pure nakamoto consensus. Notably, these are decentralization, accessibility, censorship resistance, and fair issuance.     

> __< s​gp_:monero.social >__ I do not believe PoW "tweaks" will address the most significant issues of nakamoto consensus in Monero. I believe that a TFL approach is most likely to yield the best tradeoffs.     

> __< rbrunner >__ 2) The main problem I see is that Monero is too small, simply put.     

> __< a​rticmine:monero.social >__ 3 The above says it very well     

> __< sech1 >__ I have been asked to pass this message from discord: "I think I speak for a lot of people here saying the issue of mining pool centralization is quite concerning & requires immediate attention since a successful attack on the network would result in the loss of trust in the ecosystem and once lost, it'll be nearly impossible to get back. At the     

> __< sech1 >__ time of writing, a 6-7 block reorg was demonstrated to have happened in the past few days thanks to rucknium's amazing tools & work with the help of other devs. A solution to this problem is needed yesterday & frankly monero should've addressed this issue a long time ago considering the historical progress in this field of research."     

> __< j​ohn_r365:monero.social >__ sgp_: TFL = Trailing Finality Layer?     

> __< r​ucknium:monero.social >__ kanzure: The tx contents of the re-orged blocks did not change. You can check this with `print_pool_stats` in your `monerod` console. No double spend txs attempted.     

> __< kanzure >__ thank you rucknium. that is interesting.     

> __< r​ucknium:monero.social >__ 3) Principles: Privacy, decentralization, accessibility, fungibility.     

> __< v​enture:monero.social >__ ordinary user, somewhat technical background and somewhat studied monero technicals. also, sporadic donor     

> __< v​enture:monero.social >__ 2.      

> __< v​enture:monero.social >__ - double-spend attacks if >51% is reached, less likely since there the attacker would be known to be affiliated with the majority block producer. would presumably give way to legal recourse since this would be plain theft     

> __< v​enture:monero.social >__ - censorhip, restricting txs somehow. this is also the reason why i think that any finality might come short of mitigation since nothing can be finalized what wasn't accepted by a centralized PoW provider     

> __< c​haser:monero.social >__ 3] principles:     

> __< c​haser:monero.social >__ * privacy. a solution shouldn't leave users, and ideally miners/validators too, any worse off than the current level.     

> __< c​haser:monero.social >__ * censorship-resistance. same as previous point.     

> __< c​haser:monero.social >__ * decentralization.     

> __< c​haser:monero.social >__ * resilience. if a solution works, it should work in highly adversarial settings too.     

> __< c​haser:monero.social >__ * avoiding high complexity.     

> __< c​haser:monero.social >__ * integrity of monetary policy. leave it intact, or at least never increase the overall issuance rate of XMR.     

> __< c​haser:monero.social >__ * asset integrity. the consensus protocol shouldn't issue a secondary asset.     

> __< c​haser:monero.social >__ * open-mindedness. judge solutions based on how they work and what they achieve, not where they come from or what narratives are attached to it.     

> __< s​gp_:monero.social >__ yes, FTL = trailing finality layer     

> __< s​gp_:monero.social >__ yes, TFL = trailing finality layer     

> __< s​yntheticbird:monero.social >__ Faster than light?     

> __< a​ntilt:we2.ee >__ 2] I pointed out that CPU hashrate may be rented 4 month ago and suggested a 2nd BFT layer based on Eigentrust - now called "finality layer"     

> __< o​frnxmr:monero.social >__ When i said "payments, reliable and immutable", it should go without saying: confidential, accessible, and decentralized     

> __< s​pirobel:kernal.eu >__ what is the benefit of a finality layer compared to proof stake?     

> __< rbrunner >__ 3) Monero should stay "trustless" and "permissionless". Otherwise forget all the fuss and use credit cards and paypal.     

> __< r​ucknium:monero.social >__ That stated, Qubic can make it appear that a double-spend against a victim occurred, by double-spending to itself. Then, a "double spend" tx would appear in the nodes, but there would be no actual victim, just propaganda value.     

> __< a​ntilt:we2.ee >__ both are variants of BFT, one not based on wealth     

> __< r​ucknium:monero.social >__ Has everyone who wanted to speak on the first three bullet points spoken?     

> __< a​rticmine:monero.social >__ On principals:     

> __< a​rticmine:monero.social >__  We need to stay away from TEEs The Intel ME is an example of a TEE that even the NSA in the US found obnoxious      

> __< a​rticmine:monero.social >__ We also need t stay away from hybrid POS systems     

> __< s​pirobel:kernal.eu >__ which one is not based on wealth? its not like cpus and electricity are free     

> __< s​pirobel:kernal.eu >__ arcticmine: yes.     

> __< r​ucknium:monero.social >__ Now we will get into General open-ended discussion on potential solutions to the mining pool centralization problem. First: Improvements and fixes to the existing POW., both at consensus and node relay.     

> __< r​ucknium:monero.social >__ (Note: discussion of non-PoW solutions will follow after this first point discussion.)     

> __< a​rticmine:monero.social >__ I would suggest instead that we focus on hardening our existing POW both at the consensus and node really levels     

> __< s​pirobel:kernal.eu >__ what is the security budget currently and how much would the attack cost increase by this measure ?     

> __< c​ountbleck:matrix.org >__ Is this where tevador's bandwidth-based idea comes in?     

> __< r​ucknium:monero.social >__ There was a paper published recently in a top economics journal. It was circulated as a draft for a few years: Budish, E. (2025). "Trust at Scale: The Economic Limits of Cryptocurrencies and Blockchains", The Quarterly Journal of Economics, 140(1), 1–62.  https://moneroresearch.info/101     

> __< m​rmatrixer:matrix.org >__ Where can I watch the meeting?     

> __< r​ucknium:monero.social >__ Part of the abstract:      

> __< r​ucknium:monero.social >__ > This article shows that Nakamoto’s novel form of trust, while undeniably ingenious, is deeply economically limited. The core argument is three equations. A zero-profit condition on the quantity of honest blockchain “trust support” (work, stake, etc.) and an incentive-compatibility condition on the system’s security against majority attack (the Achilles heel of all forms <clipped message     

> __< r​ucknium:monero.social >__ of permissionless consensus) together imply an equilibrium constraint, which says that the “flow” cost of blockchain trust has to be large at all times relative to the benefits of attacking the system. This is extremely expensive relative to traditional forms of trust and scales linearly with the value of attack. In scenarios that represent Nakamoto trust becoming a more signi<clipped message     

> __< r​ucknium:monero.social >__ ficant part of the global financial system, the cost of trust would exceed global GDP. Nakamoto trust would become more attractive if an attacker lost the stock value of their capital in addition to paying the flow cost of attack, but this requires either collapse of the system (hardly reassuring) or external support from rule of law.     

> __< a​rticmine:monero.social >__ I like both trevador's idea and Sech1's with 1%     

> __< j​effro256:monero.social >__ 1. Full-time developer paid thru Monero CCS since 2023. User since late 2017. Formal education in computer science and distributed systems, and working knowledge of elliptic-curve-based cryptography.     

> __< j​effro256:monero.social >__ 2. One issue that I believe to have been a large one for some time is the lacking present security budget due to a front-heavy monetary emission policy. Unfortunately, this is hard to change after the fact. This *can* be helped by furthering adoption and raising XMR price to make financial attacks against PoW harder / riskier.     

> __< j​effro256:monero.social >__ 3. Principles: privacy, fungability, decentralization, permissionless, ease-of-use, honoring past social contracts, salability over time&space, battle-hardening, research-focus     

> __< a​rticmine:monero.social >__ Both can be implt     

> __< a​rticmine:monero.social >__ Implemented     

> __< r​ucknium:monero.social >__ CountBleck: Yes, it could. That's https://github.com/monero-project/research-lab/issues/98     

> __< a​ntilt:we2.ee >__ I want to point out that BFT may be tied to a resource we control... and thats the community (trust) itself.     

> __< r​ucknium:monero.social >__ Keith Meister: You're watching it right now. It's all text-based.     

> __< kanzure >__ do the monero developers consider monero PoW hard-fork to be substantially different from (say for example) successfully deploying a bitcoin PoW hard-fork? do the present conditions exceed anyone's notions for requiring a PoW hard-fork? just curious.     

> __< s​gp_:monero.social >__ Personally, I don't think that any clear issues arose from RandomX. RandomX worked exactly as intended. Nakamoto consensus worked exactly as intended. An adversary selfishly mined blocks and lost more money than they made, though this doesn't factor in free PR value     

> __< s​gp_:monero.social >__ Certain tweaks could be made to make pool mining less competitive, which could help reduce the advantage of mining pools and could help with decentralization. The tevador proposal, while interesting, may _increase_ centralization by turning away small miners (it raises their costs to require a node in some circumstances). In any case, I don't see these as addressing the "core" pro<clipped message>     

> __< s​gp_:monero.social >__ blem, even if certain tweaks are considered appropriate and selected. Another proposal needs to be considered in conjunction, imho     

> __< k​ayabanerve:matrix.org >__ Sorry to jump in, but this is very wrong.     

> __< k​ayabanerve:matrix.org >__ But yes, we should focus on PoW immediately per Rucknium's chairing     

> __< k​ayabanerve:matrix.org >__ I like tevador's proposal but am concerned about the risk a higher percentage of honest miners disappear than malicious miners, while in such a delicate state.     

> __< k​ayabanerve:matrix.org >__ tevador did respond to this concern though.     

> __< a​rticmine:monero.social >__ As for the security budget a lot of the issue with Qubic is shifting of miners to their centralized pool     

> __< a​rticmine:monero.social >__ We also have to be careful here that we do not create a cure that is far worse than the desise     

> __< r​ucknium:monero.social >__ sgp_: I agree that it honest mining pools could become less concentrated, e.g. no honest mining pools above 5% total hashpower, the Qubic attack could still happen. Reducing honest mining pool centralization is good, but much more would be needed.     

> __< rbrunner >__ +1     

> __< k​ayabanerve:matrix.org >__ That isn't to say I drop my concern, just to say tevador has their own opinion.     

> __< o​frnxmr:monero.social >__ I dont think they _shifted_ miners, but attracted (or rented) dormant hashrate     

> __< k​ayabanerve:matrix.org >__ rbrunner: can you clarify which message you're supporting, please?     

> __< rbrunner >__ ArticMine's     

> __< rbrunner >__ Cure versus desease     

> __< s​gp_:monero.social >__ There are many bad options indeed :)     

> __< o​frnxmr:monero.social >__ +1 on avoiding cures that are worse than the cancer     

> __< rbrunner >__ We have it in our hands to destroy Monero all on our own :)     

> __< k​ayabanerve:matrix.org >__ Thank you     

> __< s​pirobel:kernal.eu >__ how much in dollar terms cost is it currently to perform a 51% attack on monero? I have read people say its 75 million or just a few hundred k     

> __< k​ayabanerve:matrix.org >__ I'm not entirely convinced tevador's proposal is guaranteed to be better than worse re: the current malicious pool, but I support it generally.     

> __< r​ucknium:monero.social >__ kayabanerve: I would ask Matrix-side commentators to do the same by prefixing their response comments with the username of the user they are responding to. This helps keep IRC-side logs, which are used for the GitHub issue, understandable.     

> __< a​rticmine:monero.social >__ They have my being that successful on raw sustainable hash power. What Qubic is being very successful is in creating a social engineering attack.      

> __< a​rticmine:monero.social >__ When I see radical proposals that go against the basic principles of Monero, I see their success     

> __< k​ayabanerve:matrix.org >__ $1 because by adding $1 in outside incentives, you'll pay the highest reward for hash power, and a hyper-efficient capitalist market will have all hash power go to you /s     

> __< a​rticmine:monero.social >__ This discussion is my evidence     

> __< s​pirobel:kernal.eu >__ we dont even have a clear number, right? is there a ball park figure ?     

> __< r​ucknium:monero.social >__ spirobel: About 432 XMR is emitted to miners every day. That is called the "security budget".     

> __< s​pirobel:kernal.eu >__ thats not much to secure billions of dollar in market cap     

> __< rbrunner >__ spirobel: They currently seem to pay with their own coin, emissioned weekly out of thin air, for free     

> __< r​ucknium:monero.social >__ Here are some tables endor00  produced a while ago:  "51% attacks and mining incentives"  https://gist.github.com/endorxmr/a13dce62ae1ba4676a1ed0311d96bf07     

> __< j​effro256:monero.social >__ Which works as long as the AI-hype-ponzi machine keeps pouring in money to Qubic's coin     

> __< rbrunner >__ Exactly. That can take a while :)     

> __< o​frnxmr:monero.social >__ articmine  the best proposal ive heard, was sent to me in dm (and sent to pool operators). For pools to collude with one another to perform a real 51% attack with the goal of censoring qubic's blocks. i had to go to bed after reading that     

> __< c​haser:monero.social >__ spirobel: it's a function of the inflation rate, a very delicate balance that all assets need to keep, not just Monero.     

> __< a​ntilt:we2.ee >__ 100.000$ / month for 1GH     

> __< s​gp_:monero.social >__ ofrnxmr: that only works so long as they have a minority hashpower, even if everyone else agreed to do that. If they got the majority for a sustainer period, then that wouldn't work. And we're back to square 1     

> __< s​pirobel:kernal.eu >__ lets say you are a whale right now, if you wanted to contribute to the security of the network you would have to sell part of your xmr to mine at a loss. so there is a negative feedback loop here. PoW just adds sell pressure and no security     

> __< tevador >__ Pool centralization has been an issue long time before qubic. Miners don't care. Even 0% fee is not enough to make miners move to p2pool. That's why #98 was proposed.     

> __< o​frnxmr:monero.social >__ Spg, i forgot the /s. It was actually proposed, but asking to be 51%d is.. against monero core values     

> __< a​rticmine:monero.social >__ Which would stop them dead in their tracks right now     

> __< c​haser:monero.social >__ jeffro256: right, they're currently probably sustainable because they're dumping their coin on retail investors who buy into the hype.     

> __< s​gp_:monero.social >__ let's all centralize around one big pool but it's actually trustworthy and only denies blocks by bad people /s, ofc     

> __< a​rticmine:monero.social >__ They are not close to 51% on a sustainable basis     

> __< o​frnxmr:monero.social >__ "we hate big pools. also: hey pools, can you combine and 51% attack the network?"     

> __< s​gp_:monero.social >__ I personally think that on the PoW tweak front, tevador's proposal is the most realistic, by far. That's where discussion should focus around in the future     

> __< a​rticmine:monero.social >__ One can even use node relay e orphan malicious blocks     

> __< a​rticmine:monero.social >__ To     

> __< o​frnxmr:monero.social >__ sgq, I think node relay stuff is my preferred direction     

> __< tevador >__ Realistic short-term mitigations are: 1) Renting hashrate to help the network. 2) Temporarily raising tx fees (as a relay rule).     

> __< a​ntilt:we2.ee >__ are there any ideas on how to fade in #98 slowely ??     

> __< j​effro256:monero.social >__ That's assuming we can differentiate Qubic blocks from non-Qubic blocks, which would probably rely on nodes connecting into Qubic mining pools     

> __< m​rmatrixer:matrix.org >__ Where can I watch the meeting?     

> __< o​frnxmr:monero.social >__ youre in the meeting now, keith     

> __< 1​7lifers:matrix.org >__ here. scroll up.     

> __< 1​7lifers:matrix.org >__ i got some fresh popcorn ready to last the whole meeting     

> __< m​rmatrixer:matrix.org >__ Which users are the devs?     

> __< a​rticmine:monero.social >__ No checking how the block structure compares to an honest block structure.     

> __< o​frnxmr:monero.social >__ also cc kayabanerve  what about an orphaned blocks difficulty addition, or uncle blocks etc     

> __< s​gp_:monero.social >__ I suppose I'm also for higher tx fees. But it's not a complete solution     

> __< s​pirobel:kernal.eu >__ pow is nostalgia. why not rip off the band aid? if just 10% of xmr holders stake we have a security budget in the hundreds of millions  much more than 432 xmr     

> __< o​frnxmr:monero.social >__ So the diff isnt based on "5gh" when there is really 7gh mining     

> __< j​effro256:monero.social >__ I thought Qubic patched that recently     

> __< a​rticmine:monero.social >__ If the difference is big enough block or delay     

> __< s​gp_:monero.social >__ articmine wouldn't that just cause split consensus?     

> __< k​ayabanerve:matrix.org >__ I'm not immediately sure if allowing referencing orphaned uncles to increase the network's difficulty would be good or not. I'd guess not, because whoever includes the orphans would face the wrath.     

> __< o​frnxmr:monero.social >__ wouldnt everyone include the orphans?     

> __< a​rticmine:monero.social >__ If Qubic is forced to mine honest block the harm in the attack is diminished     

> __< r​ucknium:monero.social >__ IMHO, raising tx fees as a relay rule won't work for two reasons: 1) You would still not have enough fee, as a percentage of block reward. 2) It is easy to get around nodes that update to new node relay rules, so txs would still get to miners. This happened with nonzero lock time.     

> __< b​oog900:monero.social >__ what would including orphans even fix here?     

> __< k​ayabanerve:matrix.org >__ Agreed but there's no good way to require a block is honest.     

> __< o​frnxmr:monero.social >__ The diff is artificially low. This would create an acxurate difficulty     

> __< c​haser:monero.social >__ you could allocate a minor part of the issuance to reward orphan inclusion.     

> __< o​frnxmr:monero.social >__ Chaser, thats how uncle blocks work, no?     

> __< b​oog900:monero.social >__ but that would just slow blocks down rather than stop a selfish mining attack     

> __< k​ayabanerve:matrix.org >__ *agreed a miner forced to mine honest blocks diminishes the attack.     

> __< a​rticmine:monero.social >__ Yes, but nothing forces nods to relay dishonest blocks     

> __< k​ayabanerve:matrix.org >__ I mean, it's bad for the network.     

> __< k​ayabanerve:matrix.org >__ Selfish mining is based on withholding a longer chain so adversaries are mining on old data.     

> __< b​oog900:monero.social >__ qubic created a lot of orphans during their attack that they didn't broadcast you would be rewarding them     

> __< c​haser:monero.social >__ ofrnxmr: I believe so, yes     

> __< k​ayabanerve:matrix.org >__ Taking longer to switch to the best chain is on purposely keeping yourself on an old chain.     

> __< r​ucknium:monero.social >__ https://kevinnegy.github.io/Selfish%20Mining%20Re-Examined.pdf     

> __< r​ucknium:monero.social >__ >  ETH, on the other hand, shows that a new selfish miner with any hash rate and any γ value can at least break-even. This finding is entirely due to the uncle block reward system that exists in ETH, which is described in more detail in Appendix A.     

> __< k​ayabanerve:matrix.org >__ If honest miners are *randomly* behind the actual longest chain, they can immediately close the gap by switching and have the best odds of the actual next block.     

> __< r​ucknium:monero.social >__ According to my interpretation, giving uncle rewards can promote selfish mining, at least below the usual 33% hahspower threahold ^     

> __< s​pirobel:kernal.eu >__ benefit of PoS is faster finality, higher TPS, no inflation. whales are naturally incentivized to protect network security by staking. tx fees will be enough to compensate stakers.     

> __< s​gp_:monero.social >__ spirobel: I believe that discussion is tabled for later     

> __< a​rticmine:monero.social >__ ETH has serious orphan blocks issues due to relativistic (physics) effects     

> __< c​haser:monero.social >__ Rucknium: interesting, thank you for noticing that     

> __< j​effro256:monero.social >__ Allowing uncle blocks also removes the current implicit penalty for slow block propagation, which can de-stabilize the network     

> __< a​rticmine:monero.social >__ It takes a finite amount of time for light to travel over fibre optic cable     

> __< v​enture:monero.social >__ if orphaning blocks skews the hashrate down, and given the general attack vector of having too few miners... how about rewarding net hashrate / difficulty increase? Incorporating that in a sort of dynamic block reward tied to a set difficulty over time?     

> __< v​enture:monero.social >__ Currently, it has a negative feedback loop, every new miner diminishes the returns of existing ones     

> __< s​yntheticbird:monero.social >__ in practice the hashrate goes up when the price goes up     

> __< s​yntheticbird:monero.social >__ it has been observed forever     

> __< b​oog900:monero.social >__ you would be changing the emission then presumably     

> __< s​pirobel:kernal.eu >__ flip flop: if we assume 100 k for 1 month of 1GH it means the only reason this attack is not performed its because its hard to acquire that much cpus without kyc     

> __< s​yntheticbird:monero.social >__ I honestly wouldn't see anyone wishing to avoid kyc attack monero. On the other end I easily see people wanting to attack monero to not having to worry about kyc.     

> __< rbrunner >__ Lol. We do know who attacks us right now, no?     

> __< o​frnxmr:monero.social >__ Rbrunner, we dont know who he works with/for     

> __< s​pirobel:kernal.eu >__ sgp_:  the question is really related. 98 is just more band aid if at all     

> __< a​ntilt:we2.ee >__ right     

> __< s​pirobel:kernal.eu >__ we cant even measure the impact properly     

> __< k​ayabanerve:matrix.org >__ spirobel: which is why it's being discussed _next_.     

> __< a​rticmine:monero.social >__ A 51% attack against Monero could be considered a criminal act in many jurisdictions so avoiding KYC would make sens     

> __< s​gp_:monero.social >__ spirobel: I agree with the practical challenge of renting hashrate. A thief swapping xmr to btc or whatever is incentivized to rent hashrate if they can to double spend. That's certainly an important scenario that Monero's consensus needs to be prepared for     

> __< k​ayabanerve:matrix.org >__ Oh, sorry if I replied regarding the wrong thing spirobel     

> __< s​gp_:monero.social >__ rentable hashrate is one of the most significant disadvantages of a cpu friendly algo     

> __< v​enture:monero.social >__ ArticMine: not quite, only the double-spend is criminal. not having more than 51%.     

> __< v​enture:monero.social >__ So yes, since qubic is public, double-spend is unlikely. Censorship/kyc attack after having achieved 51 more so IMHO.     

> __< s​gp_:monero.social >__ asic friendly hashrates are more centralized around manufacturing, but it's harder to "driveby" doublespend     

> __< r​ucknium:monero.social >__ sgp_: Weakness and a strength. Network recovery after an attack is easier with CPU-mineable since no one could have bought up all the CPUs.     

> __< a​rticmine:monero.social >__ Attack against a computer network are criminal. There is no exception for privacy preserving decentralized networks     

> __< v​enture:monero.social >__ which renders even a finalizing layer mute, when you can't get your tx in the PoW block provider's block in the first place.     

> __< a​ntilt:we2.ee >__ the sad answer is that high decentralization... has not been demonstrated in practice. In practice, we trust.     

> __< r​ucknium:monero.social >__ And even a strength for defenders to rent their own defense hashpower if there is advance notice, as in this Qubic case.     

> __< s​yntheticbird:monero.social >__ I wouldn't count on geopolitical superpower to apply their law to such an extent     

> __< s​gp_:monero.social >__ rucknium yeah I'm not pro asic, but the cpu friendly algo has the downside of these social, ponzi-driven social attacks being easier to rally up     

> __< a​rticmine:monero.social >__ They may not have a choice     

> __< s​gp_:monero.social >__ "there are pros and cons" ha     

> __< NIck_ >__ ArticMine Apologies for intervening but in most jurisdictions wouldn't an entity need to press charges for this to be an effective deterrent ? As long as i am aware there is no Monero Foundation legal entity at this moment to be able to do that... That's an assumption you can of course defend your point just bringing something up. :)     

> __< a​rticmine:monero.social >__ There is also the risk of decentralized litigation     

> __< r​ucknium:monero.social >__ Anyone familiar with a review research article on hardening PoW blockchain consensus?     

> __< rbrunner >__ Anyway, I think tevador idea proposed in "98" would take months of finalizing and hardforking into service. That may well be too late for our *immediate* "Qubic problem"     

> __< a​rticmine:monero.social >__ Anyone hurt by the attack could press charges     

> __< s​gp_:monero.social >__ new included mining pool service: lawyers for civil litigation     

> __< s​pirobel:kernal.eu >__ ArticMine: if its down to this and we are ready to admit it: why do we need to buy cpus to secure the network and gift money to utility companies? we could reduce inflation to zero and tell bitcoiners: there will only ever be 18 million monero. And cost of attack would be orders of magnitude higher than it is now     

> __< a​rticmine:monero.social >__ It is one of many possible options     

> __< v​enture:monero.social >__ 51% attacks are not criminal. taking over an org / hostile take-overs happen even in stock markets. but I'm not an expert     

> __< r​ucknium:monero.social >__ IMHO, probably the best short-term defense is people adding more hashpower, from their own machines or renting hashpower, during the Qubic hashpower spikes.     

> __< NIck_ >__ with that in mind miners could theoretically press charges for yesterday's attack for making them miss profits from the orphaned blocks i am unsure how realistic that would be     

> __< s​pirobel:kernal.eu >__ its the only option that is sensible. I saw someone mention he is willing to sell xmr to rent hashrate to secure the network. so currently we have negative inflation proof of stake. people love monero so much they are willing to pay to secure it.     

> __< s​yntheticbird:monero.social >__ Let's not be naive here, both US and Europe jurisdictions would be delighted to hear XMR plunged to death. That is without considering lobbyist and corruption. There is no chance that civils will achieve a case against Qubic. On the other end, it just take one grant from an ally/strategic country to Qubic to transform the case into a geopolitical mess that will slow/stuck things e<clipped me     

> __< s​yntheticbird:monero.social >__ ven further. Qubic have the high grounds here     

> __< a​rticmine:monero.social >__ I remember when an individual said that Bitcoin was not money in 2011. The SEC fitted the individual for an orange jumpsuit.     

> __< r​ucknium:monero.social >__ I will do a broad literature search on articles about hardening PoW blockchain consensus without altering its fundamentals. Any other specific actions to take on PoW-based research?     

> __< b​oog900:monero.social >__ how would you prove your didn't just disconnect from the network and happen to reconnect once they overtook the mainchain?     

> __< rbrunner >__ Don't forget that courts, litigations etc. usually drags on freaking years. People, that's not useful.     

> __< b​oog900:monero.social >__ the miner disconnect from the network^     

> __< r​ucknium:monero.social >__ In the next 5 minutes I will move us to discussing non-PoW options, unless there are really new things brought up about PoW.     

> __< v​enture:monero.social >__ the shoe is always on the other foot with these guys. it's a commodity here, but money there *sigh     

> __< b​oog900:monero.social >__ on Monero this would be enough to invalidate pretty much all txs if they reorged more than 10 blocks     

> __< s​pirobel:kernal.eu >__ rucknium: proof of work is nostalgia.     

> __< b​oog900:monero.social >__ would checkpoints fall under PoW?     

> __< o​frnxmr:monero.social >__ Hyc's rolling hash of hashes     

> __< s​pirobel:kernal.eu >__ also: pos would help with the eclipse / sybill attack of nodes     

> __< s​yntheticbird:monero.social >__ spirobel can you wait on the rucknium to bring the next point     

> __< j​effro256:monero.social >__ We could still use checkpoints with PoS. Is that what you are asking?     

> __< s​yntheticbird:monero.social >__ spirobel can you wait on rucknium to bring the next point     

> __< r​ucknium:monero.social >__ boog900: IMHO, checkpoints with current PoW fits in this section. Could fit in the next section, too.     

> __< b​oog900:monero.social >__ I wouldn't be for a distributed version like that, but not allowing reorgs beyond 10 blocks is something I have been liking the thought of more and more     

> __< s​gp_:monero.social >__ checkpoints most closely fall under PoS/TFL, unless you are implying daily/hourly monerod software releases :p     

> __< o​frnxmr:monero.social >__ Sgp, we have dns checkpointing, so it doesnt require releases.     

> __< b​oog900:monero.social >__ no rolling checkpoints I think it what bitcoin cash calls just not allowing reorgs beyond 10 blocks     

> __< b​oog900:monero.social >__ beyond X blocks^     

> __< s​gp_:monero.social >__ boog900: that leads to split consensus with nodes though. What chain does a newly syncing node follow? The highest hashrate one, or a different one with less work that other nodes claim they saw first?     

> __< o​frnxmr:monero.social >__ i dont buy the bootstrapping is as a blocker     

> __< b​oog900:monero.social >__ it would be the highest hashrate with the hope an attacker can't keep up forever     

> __< b​oog900:monero.social >__ they would have a period where they can get new nodes but the real chain should overtake them eventually     

> __< r​ucknium:monero.social >__ Arguably, BCH has an bigger sword of Damocles hanging over its head than Monero does, with its SHA256 hashing. And BTC people wanting to kill it since 2017.     

> __< o​frnxmr:monero.social >__ The chain which the majority of your peers are on     

> __< s​gp_:monero.social >__ so during the attack we have two networks     

> __< rbrunner >__ If BCH does that, I guess they came up with a solution for these bootstrapping problems?     

> __< b​oog900:monero.social >__ sadly     

> __< b​oog900:monero.social >__ better than a big reorg IMO     

> __< o​frnxmr:monero.social >__ We already have 2 networks during attack     

> __< r​ucknium:monero.social >__ BSV (Bitcoin Satoshi's Vision) had an attacker that mined empty blocks for a awhile IIRC. A rolling checkpoint wouldn't fix that.     

> __< s​gp_:monero.social >__ currently nodes have clear instructions about which chain to prefer. With the same info, nodes will agree on which is the single "correct" one     

> __< o​frnxmr:monero.social >__ your node can currently get thrown onto a bad chain during bootstrap     

> __< s​gp_:monero.social >__ this would have two nodes running the same code, depending on their view of the network, disagree     

> __< s​yntheticbird:monero.social >__ thats wht highest hashrate make more sense     

> __< s​yntheticbird:monero.social >__ imo     

> __< o​frnxmr:monero.social >__ Has happened to me a few times, wjen malicious nodes decided to share a bad chain ~ block 1.5million     

> __< b​oog900:monero.social >__ only new nodes would be affected     

> __< r​ucknium:monero.social >__ Let's go to the next sub-item:     

> __< r​ucknium:monero.social >__ 2) The introduction of non POW consensus mechanisms such as but not limited to A) Trusted Execution Environments, B) Proof of Stake Hybrid solutions, C) Other non POW consensus solutions     

> __< k​ayabanerve:matrix.org >__ Rucknium: Actually, it could have helped.     

> __< s​gp_:monero.social >__ while the attack is ongoing, the network is stalled and there are 2 networks     

> __< b​oog900:monero.social >__ hopefully new nodes would not have the same economic impact as reorging old nodes     

> __< e​longated:matrix.org >__ Why should nodes accept consecutive empty blocks, if their mempool is not empty ?     

> __< o​frnxmr:monero.social >__ A) nah b) i only like proof of pow c) no comment     

> __< k​ayabanerve:matrix.org >__ If a finality layer is sufficiently quick to achieve finality, even if a malicious miner tries to reorg out honest blocks, they may already be finalized.     

> __< b​oog900:monero.social >__ stalled? we would have 1 correct and 1 that is ahead for as long as they want to keep the wasted mining     

> __< k​ayabanerve:matrix.org >__ They just have to be the first broadcast block for the finality layer to observe, if it's sufficiently responsive.     

> __< wownero_maxi >__ I and the miners I work with only like PoW. Absent PoW, we move to other cryptocurrencies. Simple as.     

> __< s​gp_:monero.social >__ I consider TFL a more robust mechanism than "don't reorganize past 10 blocks"     

> __< s​yntheticbird:monero.social >__ elongated i had the exact same thought but this is hard to get right as depending on the node local scope     

> __< b​oog900:monero.social >__ a lot more complicated though     

> __< j​effro256:monero.social >__ Tbf, this is already technically true for 1-block-deep reorgs. If there's two chains with the same exact height, b/c of the difficulty calculation lag, a node will choose whichever one it saw first, then switch to the chain which has the next block built on top of it, so on and so forth.     

> __< o​frnxmr:monero.social >__ also: theres no reason why qubic _has_ to share empty blocks. They can effectively stuff the blocks to the brim and make for an arguable worse attack     

> __< r​ucknium:monero.social >__ What is a Trailing Finality Layer?     

> __< j​effro256:monero.social >__ i.e. there's no "tie-breaker" rule     

> __< r​ucknium:monero.social >__ Or link me something that you think explains it well.     

> __< s​gp_:monero.social >__ the complication is worth it imo to avoid potentially prolonged split consensus     

> __< e​longated:matrix.org >__ Let’s say a node accepts 2 empty blocks, if miner is not clearing mempool (even half of it) the miner is malicious?     

> __< k​ayabanerve:matrix.org >__ With an asynchronous consensus algorithm, like the one I posited, we'd achieve consensus however frequently the environment allows (limited by processing speed, bandwidth, and latency). Because we wouldn't have a hard requirement on any performance, anyone could run a validator over any network (such as Tor).     

> __< s​gp_:monero.social >__ I'm less concerned about a 1-block reorg since those essentially need to happen in honest scenarios as well     

> __< o​frnxmr:monero.social >__ Attacker just switches to mining full blocks of their own txs     

> __< k​ayabanerve:matrix.org >__ We can use an asynchronous consensus algorithm to finalize existing Monero blocks (PoW). This would prevent them from being reorganized off of.     

> __< c​haser:monero.social >__ Rucknium: https://electriccoin.co/blog/the-trailing-finality-layer-a-stepping-stone-to-proof-of-stake-in-zcash/     

> __< k​ayabanerve:matrix.org >__ This would ideally prevent selfish mining and ensure X% of hash rate actually earns an average of X% of blocks, if sufficiently responsive.     

> __< k​ayabanerve:matrix.org >__ More definitely, it stops deep re-orgs.     

> __< s​pirobel:kernal.eu >__ what is the security benefit of the finality layer over PoS?     

> __< k​ayabanerve:matrix.org >__ It also lets us replace the 10-block lock with a finality-block lock. Outputs can be spent once the block creating them is finalized. This would, ideally, reduce the 10-block lock to just a few seconds (so effectively non-existent).     

> __< a​rticmine:monero.social >__ How is this finality layer secured?     

> __< k​ayabanerve:matrix.org >__ We would need to decide validators, which we'd presumably do via PoS.     

> __< e​longated:matrix.org >__ Pos ?     

> __< c​haser:monero.social >__ I believe a stake-based finality layer as an overlay to the current Nakamoto consensus is the best option, and viable without compromising on any of Monero's principles. I'm categorically against any solutions involving trusted execution environments (Intel SGX, etc.) because of their nature of being trusted, potentially backdoored from day 0, and frequent in-the-wild exploits.     

> __< a​rticmine:monero.social >__ So we are back t POS?     

> __< k​ayabanerve:matrix.org >__ PoS is just proof of stake and can mean many things. Zano's PoS allows someone who stakes to produce a block. Here, PoS entitles one to participate in a live network to finalize blocks.     

> __< a​rticmine:monero.social >__ For security     

> __< b​oog900:monero.social >__ would they be rewarded for staking?     

> __< s​pirobel:kernal.eu >__ kayabanerve:  why not just switch to PoS ?     

> __< s​gp_:monero.social >__ using PoS for the finality layer instead of entirely helps maintain more of Monero's PoW values. It's not perfect all around, but it _may_ be the best bang for our buck all around     

> __< rbrunner >__ kayabanerve, that recent paper that you linked to, is it really so attractive as title and abstract seem to suggest? Is that a substantial improvement of "state of the art"? https://eprint.iacr.org/2024/677     

> __< s​gp_:monero.social >__ fwiw, I am quite worried of a large service (e.g. exchange) effectively halting the finalizations (and in effect, the network). I think that's a real risk that needs to be carefully considered in the TFL design     

> __< s​pirobel:kernal.eu >__ sgp_: in other words: there is no scientifically sound reason, just nostalgia for PoW     

> __< s​gp_:monero.social >__ arguably, "fair distribution of new coins" is a reason     

> __< k​ayabanerve:matrix.org >__ The TEE solution I proposed has been withdrawn and I maintain is fundamentally misunderstood by anyone still yelling against it because TEEs are insecure.     

> __< c​haser:monero.social >__ spirobel: Nakamoto proof of work is fundamentally more sound, lower complexity and ensures wider participation in block validation over longer spans of time. it's a good ground to build on IMHO.     

> __< r​ucknium:monero.social >__ At the end of the meeting, I want to list specific actions that specific people will take to advance this issue. Keep that in mind.     

> __< o​frnxmr:monero.social >__ Spriobel wants to eliminate the emission as well     

> __< a​rticmine:monero.social >__ POS has a fundamental flaw that cannot be solved. What the network cannot determine is whether the person putting up the stake is actually long Monero in this case.      

> __< a​rticmine:monero.social >__ Sure the stalker has put up XMR. But. What prevents the stalker from borrowing XMR and then selling it creating a larger short position in XMR than the stake.      

> __< a​rticmine:monero.social >__ Then the stalker has an incentive to create havoc on the network in order to devalue his debt     

> __< e​longated:matrix.org >__ Pow+pos is more sensible     

> __< k​ayabanerve:matrix.org >__ But regardless, we can move on.     

> __< k​ayabanerve:matrix.org >__ boog900: I'd propose 20-50% of the emissions.     

> __< e​longated:matrix.org >__ They will need large number of pos nodes to do that ?     

> __< k​ayabanerve:matrix.org >__ spirobel: PoW as a first pass has some arguments, as it arguably means we have a VDF in our consensus protocol _and_ it reduces the amount of options voted on.     

> __< k​ayabanerve:matrix.org >__ https://github.com/monero-project/research-lab/issues/135#issuecomment-3169589987     

> __< k​ayabanerve:matrix.org >__ rbrunner: That paper was notable for not using PKC. By simplifying out PKC, there schemes resolves as PQ.     

> __< k​ayabanerve:matrix.org >__ Overall, it's quite notable for being direct and clean though.     

> __< k​ayabanerve:matrix.org >__ It is still of cubic communication complexity in one area though, which we'd accept or we could discuss improving with non-PQ cryptography if too slow to evaluate.     

> __< o​frnxmr:monero.social >__ Articmine, thats why i only like the idea of staking coinbases     

> __< k​ayabanerve:matrix.org >__ Sorry, my messages have failed to send for the last minute.     

> __< a​rticmine:monero.social >__ Fractional reserve banking is the death of PaoS     

> __< o​frnxmr:monero.social >__ "proof of pow"     

> __< s​pirobel:kernal.eu >__ we established before in this chat that 1gh is 100k per month and the only reason keeping people from performing this attack is that it is illegal and this amount of hashrate is hard to acquire without kyc     

> __< s​gp_:monero.social >__ articmine does that not _also_ impact PoW? Go short XMR, rent hashrate, 51%....     

> __< k​ayabanerve:matrix.org >__ The biggest risk of the finality layer is a malicious set of validators can halt the network, and try to double spend at that moment they finalize two different blocks, yep.     

> __< a​rticmine:monero.social >__ Staking coinbase does not prevent going short     

> __< b​oog900:monero.social >__ I still like the no reorgs past 10 blocks :)     

> __< b​oog900:monero.social >__ No need to decrease emission for miners      

> __< b​oog900:monero.social >__ No need to worry about exchanges     

> __< k​ayabanerve:matrix.org >__ boog900: as a blind rule?     

> __< c​haser:monero.social >__ boog900: there's no need for that if you make block-winning miners the validators, and *require* them to participate in the finalization process for N blocks afterwards to claim their PoW reward.     

> __< e​longated:matrix.org >__ What if attacker does 51% starting with that hf ? Only they get coinbase and control pos     

> __< b​oog900:monero.social >__ yes     

> __< a​rticmine:monero.social >__ We know that CEXs have gone short Monero. POS is a way to bail them out     

> __< s​pirobel:kernal.eu >__ ArticMine: same goes for CPU hashing power. the difference is that we have to waste money in the current case. lets say you are a whale right now, if you wanted to contribute to the security of the network you would have to sell part of your xmr to mine at a loss. so we currently have negative inflation PoS and call it proof of work.     

> __< k​ayabanerve:matrix.org >__ I'm against staking 'blocks mined' or their coinbases.     

> __< b​oog900:monero.social >__ now someone with 51% just needs enough blocks     

> __< tevador >__ The fundamental issue of PoS are long range attacks (you can buy lots of empty wallets and roll back the chain from the time they had enough funds to stake). Ethereum solves this by "asking a friend which chain is the real one".     

> __< k​ayabanerve:matrix.org >__ I'm against an arbitrary re-org depth.     

> __< a​rticmine:monero.social >__ Not so simple. The Canadian winter is coming     

> __< k​ayabanerve:matrix.org >__ tevador: You'd need the stakes of the ancient _validator set_, not just ancient wallets, assuming the first validator set is trusted.     

> __< a​rticmine:monero.social >__ Then there is excess solar     

> __< k​ayabanerve:matrix.org >__ That's one of the pleasant things about keeping PoW around: it serves a VDF to some degree. If you're initially syncing and see two different chains, they should have vastly different amounts of work.     

> __< k​ayabanerve:matrix.org >__ *first validator set is checkpointed     

> __< r​ucknium:monero.social >__ What is VDF?     

> __< b​oog900:monero.social >__ its not ideal but none of this is and its simple     

> __< a​ntilt:we2.ee >__ sorry I can't see how this train of thought is any different from a regular "short"     

> __< tevador >__ Checkpoint = "asking a friend" solution.     

> __< a​rticmine:monero.social >__ I still see no answer to fundamental POS security     

> __< c​haser:monero.social >__ kayabanerve: for that they would get slashed, no?     

> __< k​ayabanerve:matrix.org >__ Verifiable Delay Function Rucknium, sorry.     

> __< c​haser:monero.social >__ boog900: indeed, it can't protect against 51% attacks.     

> __< j​effro256:monero.social >__ Yeah this would seem to just further entrench mining pools, especially if they started just creating coinbase outputs out to a single self-owned address, and then splitting from there     

> __< a​ntilt:we2.ee >__ thats why going hybrid is needed     

> __< k​ayabanerve:matrix.org >__ chaser If the active validator set (as needed to double spend) yes.     

> __< o​frnxmr:monero.social >__ mining pools have to issue payouts. Cant mine "used" coins     

> __< o​frnxmr:monero.social >__ Cant stake*     

> __< a​rticmine:monero.social >__ That is the bear attack on POS. The short is incentivized to cause harm to the network to profit     

> __< r​ucknium:monero.social >__ flip flop: You need to give the username of who you are replying to, especially when the user is on the IRC side.     

> __< r​ucknium:monero.social >__ IRC side can't see which message is being replied to on the Matrix side.     

> __< a​rticmine:monero.social >__ From the short     

> __< s​gp_:monero.social >__ I personally think the idea of keeping PoW "in charge" at the front, while backstopping it with PoS, is a reasonable sell     

> __< b​oog900:monero.social >__ hybrid doesn't fix that     

> __< s​yntheticbird:monero.social >__ The finality layer really looks good. Is there no way to limit the damage of a malicious staker over time ?     

> __< k​ayabanerve:matrix.org >__ Qubit could've shorted Monero before attacking it with PoW though?     

> __< s​gp_:monero.social >__ slashing     

> __< g​ingeropolous:monero.social >__ the hybrid just feels like we're adding a new door to exploit     

> __< s​gp_:monero.social >__ yay design decision we need to solve     

> __< k​ayabanerve:matrix.org >__ boog900: PoW + FL can potentially enable trade-offs regarding long range attacks and historical validator sets.     

> __< s​pirobel:kernal.eu >__ ArticMine: you always end up with proof of stake no matter what. with proof of work you just need to jump through additional hoops that are unnecessary. from a pragmatic perspective the cost of attack would be an order of magnitude higher if monero was proof of stake. no way you can hedge this with shorts on kyc exchanges     

> __< k​ayabanerve:matrix.org >__ We're replacing the PoW 51% attack risk with the issues of PoS.     

> __< k​ayabanerve:matrix.org >__ (if we add a FL)     

> __< a​rticmine:monero.social >__ Adding layers and complexity does not hide the fundamental flaw in POS     

> __< c​haser:monero.social >__ kayabanerve: I'd be interested to hear your reasons     

> __< j​effro256:monero.social >__ Yeah I guess it depends on how long you can delay payouts / what % fee you take     

> __< s​pirobel:kernal.eu >__ buying cpus or asics + wasting money on electricity is a form of stake     

> __< b​oog900:monero.social >__ kayabanerve: why no fixed max reorg depth?     

> __< k​ayabanerve:matrix.org >__ Isn't the existence of shorts fundamentally an incentive to on purposely damage something?     

> __< s​yntheticbird:monero.social >__ spirobel if you really feel like you need to shill pure PoS, try make that feeling go away.     

> __< tevador >__ Fixed reorg depth leads to permanent chain splits.     

> __< s​yntheticbird:monero.social >__ you're unhelpful at spamming Articmine your point over and over     

> __< c​haser:monero.social >__ jeffro256: what do you mean by "splitting from there?"     

> __< s​gp_:monero.social >__ tevador: agree     

> __< g​ingeropolous:monero.social >__ stake is permanent. if qubic had acquired enuf to perform a 51% on PoS.... then what?     

> __< k​ayabanerve:matrix.org >__ chaser Either the window is short, and a 51% attack enables compromising the PoS layer too, or the window is long, and miners have to stick around for a year.     

> __< r​ucknium:monero.social >__ spirobel: IMHO, your zero-inflation proposal for PoS collides with the collective action problem, at least for small stakers: If my validation is a drop in the bucket, why bother? It's more costly to me to validate than the small benefit I am getting to secure the chain. Or public goods problem, whatever term you prefer.     

> __< s​pirobel:kernal.eu >__ ArticMine: pow is an added layer of complexity to proof of stake. it just means you need to buy cpus and send a check to your utility company to proof your stake in the network     

> __< k​ayabanerve:matrix.org >__ boog900: Assumes a synchronous network and enables getting nodes stuck on alt-chains when syncing.     

> __< a​rticmine:monero.social >__ A failing exchange could easily do this . MtGox staking Bitct?     

> __< g​onbat.zano:zano.org >__ Respondind to ArticMine:  To borrow such a large amount of the supply of a multi billion dollar coin you will still need more resources in the form of collateral than what it costs to rent CPUs     

> __< g​onbat.zano:zano.org >__ Both PoW and PoS fall to actors with unlimited resources, it just takes way more with PoS     

> __< a​rticmine:monero.social >__ Bitcoin     

> __< k​ayabanerve:matrix.org >__ gingeropolous: Social slash.     

> __< s​pirobel:kernal.eu >__ same problem currently with pow rucknium. pow is just a different colored version of proof of stake with added inefficiency and hoops     

> __< j​effro256:monero.social >__ chaser: a mining pool normally pays out directly in the coinbase tx b/c of lower bytesize, but if we were to switch to only being able to stake coinbase outputs, a pool could pay out to itself, stake that output, and then when done, pay out in a regular tx     

> __< g​ingeropolous:monero.social >__ pls explain to me like ive never really dug into PoS fixits     

> __< k​ayabanerve:matrix.org >__ If the PoS layer fails, the Monero community deploys a hard fork to choose a chain and invalidate the malicious stake.     

> __< g​ingeropolous:monero.social >__ jesus monkeybut     

> __< b​oog900:monero.social >__ same with reorg?     

> __< o​frnxmr:monero.social >__ I said somewhere else "pow pools may run "staking pools" where they stake your coins and pay extra if you dont withdraw them", but thats, imo, better (and less static) than exchanges running staking pools with people's "long term savings"     

> __< b​oog900:monero.social >__ max reorg depth^     

> __< a​rticmine:monero.social >__ Any dishonest CEX can borrow XMR at no cost     

> __< k​ayabanerve:matrix.org >__ PoS halts on such a catastrophe. PoW will re-org. A re-org depth limit won't re-org but also won't halt at all.     

> __< o​frnxmr:monero.social >__ Mining pool dont usually pay out in the coinbase, only p2pool does that     

> __< k​ayabanerve:matrix.org >__ Unless you say any 10-block alt chain causes a halt. Then I can go halt every node right now. Give me a week.     

> __< tevador >__ Btw, have we considered renting some hashrate tomorrow? When qubic comes back to try again. Not sure if that's an ethical use of the general fund.     

> __< o​frnxmr:monero.social >__ Artic, like tradeogre staking zano deposits     

> __< c​haser:monero.social >__ kayabanerve: a finality layer can't stop a 51% attack anyway, so... regarding window length, I'm sure we can come up with a reasonable middle-ground between 10 blocks and 1 year.     

> __< g​onbat.zano:zano.org >__ To artictime: If a CEX adquires 51% of XMR supply, they have vastly exceeded the budget needed to attack using PoW     

> __< k​ayabanerve:matrix.org >__ ... a finality layer explicitly stops a 51%  attack?     

> __< g​ingeropolous:monero.social >__ 51% of what is currently staking     

> __< k​ayabanerve:matrix.org >__ (as in, deep re-orgs)     

> __< b​oog900:monero.social >__ the chance of a non malicious 10 block reorg is incredibly small     

> __< o​frnxmr:monero.social >__ No, they dont jeed a budget to have 51% of the _staked_ xmr     

> __< o​frnxmr:monero.social >__ They just need deposits     

> __< k​ayabanerve:matrix.org >__ There are too many ongoing conversations for me to properly participate in.     

> __< tevador >__ boog900 you can't limit the reorg depth, otherwise an attacker can cause a permanent chain split.     

> __< o​frnxmr:monero.social >__ gonabat     

> __< b​oog900:monero.social >__ best you can do is selfish mine 9 blocks send them out and hope to split the network on the next block     

> __< s​pirobel:kernal.eu >__ rucknium you can look in the other channels people are willing to rent aws servers to protect monero with rented hashrate. there is so much belief and power in this community that people are going out of their way to incur costs to protect the network. it is a pos system where you lose money if you stake and people still do it     

> __< g​ingeropolous:monero.social >__ yeah, what is the current topic of discussion?     

> __< k​ayabanerve:matrix.org >__ chaser A finality layer stops deep re-orgs for as long as it stands.     

> __< k​ayabanerve:matrix.org >__ gingeropolous: You're right a PoS finality layer could be captured. We'd generally assume that won't happen, as we assumed it for PoW, but now are revisiting.     

> __< k​ayabanerve:matrix.org >__ boog900: You can't halt on a 10-block re-org though. You have to halt on any 10-block alt chain existing because you don't know which side you're on (the malicious one or the honest one).     

> __< r​ucknium:monero.social >__ **Topic is: The introduction of non POW consensus mechanisms such as but not limited to A) Trusted Execution Environments, B) Proof of Stake Hybrid solutions, C) Other non POW consensus solutions **     

> __< k​ayabanerve:matrix.org >__ boog900: You're assuming a synchronous network.     

> __< b​oog900:monero.social >__ I wasn't calling for a halt fwiw     

> __< s​pirobel:kernal.eu >__ another benefit of having validators with stake is that we can use this to prevent ecllipse attacks of nodes     

> __< k​ayabanerve:matrix.org >__ But that was my original point. A finality layer failure causes a halt. A PoW failure doesn't.     

> __< s​yntheticbird:monero.social >__ Other non POW consensus solutions? What if the finality layer was based on Proof of Space \/s     

> __< o​frnxmr:monero.social >__ tevador it will he hard to rent hashrate using xmr during a 51%. We have some btc though?     

> __< r​ucknium:monero.social >__ ofrnxmr: I was looking at that BTC, too :D. miningrigrentals takes BTC.     

> __< g​onbat.zano:zano.org >__ To ofrnxmr: What's harder/more expensive? An exchange custoding 51% of staked XMR or an entity adquiring 51% of pow. I think that's the key.     

> __< g​onbat.zano:zano.org >__ I'm inclined to believe the prior is less likely     

> __< k​ayabanerve:matrix.org >__ I believe I would like to draft a CCS to write a book going over the design questions for a finality layer, potential options, and my recommendations. I believe this presentation will be informative and while it won't answer if we should have a finality layer, may clarify what one is and the trade offs present.     

> __< g​onbat.zano:zano.org >__ Especially if staking promotes self custody, can be done     

> __< o​frnxmr:monero.social >__ gonbat the latter. The former costs nothing     

> __< k​ayabanerve:matrix.org >__ Would people here be receptive to such a CCS to create such documentation and provide a recommendation for IF we were to adopt a finality layer?     

> __< g​ingeropolous:monero.social >__ was there any merit in what i posted on the github thing     

> __< g​ingeropolous:monero.social >__ i dunno if that qualified as non-PoW, or if i should wait for a PoW based thing     

> __< k​ayabanerve:matrix.org >__ This is my attempt to establish a proper conversation topic on the overwhelming flood of messages regarding the concept of a finality layer.     

> __< s​yntheticbird:monero.social >__ jokes on you I can't read     

> __< o​frnxmr:monero.social >__ I'd +1 the research     

> __< k​ayabanerve:matrix.org >__ gingeropolous: Can you clarify?     

> __< tevador >__ It would cost around 0.04 BTC for 100 MH/s for 24 hours. Part of the cost would be recouped with mined XMR.     

> __< g​ingeropolous:monero.social >__ the idea was that mining a block gives you a "credit" to add a block to the chain in the future, in some rolling window.     

> __< rbrunner >__ kayabanerve: Currently looks to me as the least unreasonable proposal on the table, so to say. I think it should get elaborated.     

> __< k​ayabanerve:matrix.org >__ > chaser Either the window is short, and a 51% attack enables compromising the PoS layer too, or the window is long, and miners have to stick around for a year.     

> __< g​ingeropolous:monero.social >__ basically, creating some kind of "past work means you do good work".     

> __< k​ayabanerve:matrix.org >__ was my comment here on that idea, which I even mentioned in my GH issues when first posted.     

> __< a​rticmine:monero.social >__ I believe we would need to address the underlying security of the proposed POS firts     

> __< k​ayabanerve:matrix.org >__ ArticMine: If you believe PoS never has anything at stake (but PoW does), I'm unsure how you want us to address that other than by agreeing with you.     

> __< o​frnxmr:monero.social >__ gonbat kucoin and kraken probably hold more xmr in reserves than any other entity. Kucoin has (likelt falsly) claimed to have 9million xmr. This costs them negative amounts, as they are paid when a user uses their service. They pay nothing. Example: tradeogre was / is staking zano. They dont pay _anything_ for this stake     

> __< k​ayabanerve:matrix.org >__ ... or by renaming PoS to Proof of Coin so it's not about if anything is at stake, but just about a decentralized way to select people to issue finality.     

> __< a​rticmine:monero.social >__ Focusing on the top layer does not address the base POS layer issues     

> __< s​pirobel:kernal.eu >__ gonbat: ArticMine ofrnxmr CEX only have paper monero those are excluded from staking. serious note: it makes no sense for an exchange to do a 51% attack and there is no CEX that holds that much XMR. so they would have to buy it     

> __< c​haser:monero.social >__ I will support such a CCS, both in spirit and with my donation     

> __< s​gp_:monero.social >__ the threshold is lower than 51% afaik     

> __< s​gp_:monero.social >__ for pos     

> __< k​ayabanerve:matrix.org >__ 34% is the academic bound for consensus in any asynchronous network.     

> __< s​gp_:monero.social >__ I think it's conceivable that an exchange could have 34% of staked coins     

> __< k​ayabanerve:matrix.org >__ In an asynchronous network, Monero only requires one malicious node by the way.     

> __< g​onbat.zano:zano.org >__ To ofrnxmr: if it's confirmed that over 51% of XMR Is custodied then I'd stay away from PoS     

> __< g​onbat.zano:zano.org >__ however if that's not yet the case, PoS can be used to incentivize self custody, by disallowing delegations     

> __< s​pirobel:kernal.eu >__ sgp_: true. still the practical cost of attack is orders of magnitude higher than a 51% attack against a pow network     

> __< k​ayabanerve:matrix.org >__ I'll reiterate the potential to social slash.     

> __< s​gp_:monero.social >__ Access to capital isn't precisely the same as cost     

> __< k​ayabanerve:matrix.org >__ The community can always issue a HF invalidating all staked coins if the shakers misbehave, even if they do so in a way so catastrophic, it halts the current chain.     

> __< g​ingeropolous:monero.social >__ so social slash just means that a bunch of people decide that the bad actors blocks shouldn't be included     

> __< g​ingeropolous:monero.social >__ so we could just get all the existing pools to make an agreement to mine on each others blocks and we'd have a similar thing     

> __< k​ayabanerve:matrix.org >__ No. If the finality layer is co-opted, we can issue a hard fork resetting it, burning all staked coins.     

> __< o​frnxmr:monero.social >__ gonbatfire : its not 51% of xmr, but 51% of the staked xmr. Kucoins 9-10million is clearly fake.     

> __< g​ingeropolous:monero.social >__ hmmm... the we     

> __< g​ingeropolous:monero.social >__ WE     

> __< s​pirobel:kernal.eu >__ thats why its good that monero is anti custody. it will be much secure than other coins that are held in large percentages by exchanges (that still are unlikely to commit extremely self damaging crimes all at the same time )     

> __< k​ayabanerve:matrix.org >__ We, the Monero community.     

> __< g​onbat.zano:zano.org >__ To ofrnxmr: then that would be a matter of getting everyone to stake, much easier/meaningful than getting everyone to mine     

> __< g​ingeropolous:monero.social >__ sounds permissioned and centralized to me, but that could be just me     

> __< s​yntheticbird:monero.social >__ Brother luigi decide when to release     

> __< s​yntheticbird:monero.social >__ I think this is already centralized enough     

> __< s​gp_:monero.social >__ there's also a _risk_ that networks like Serai/Thorchain/whatever get strong acceptance _and_ are programmed to stake     

> __< o​frnxmr:monero.social >__ And open for coopting / infilatration at the community level( see bitcoin)     

> __< g​ingeropolous:monero.social >__ codes not the network bro     

> __< k​ayabanerve:matrix.org >__ It's about as permissioned as us deciding to do a HF banning Qubic from mining (if we could) and then getting the community to download and run the new release.     

> __< g​onbat.zano:zano.org >__ I wouldn't like that     

> __< k​ayabanerve:matrix.org >__ I'm noting a social slash would be the same complexity and process.     

> __< g​ingeropolous:monero.social >__ permanent solutions to temporary problems. Look, if the chain was unusable and everything was falling apart then sure, maybe.     

> __< o​frnxmr:monero.social >__ qubic, and anyone, should be allowed to mine. But the network should protect against "breaking" itself, whether intentionally or unintentionally.     

> __< g​ingeropolous:monero.social >__ we got a 6 block re-org     

> __< a​rticmine:monero.social >__ Yes specifically banning Qubic is the same. Who is proposing this     

> __< a​rticmine:monero.social >__ I cannot support this finality layer     

> __< b​oog900:monero.social >__ 7* :)     

> __< s​yntheticbird:monero.social >__ stonks     

> __< v​enture:monero.social >__ an immediate band-aid for deep-reorgs would be raising the cost to mine a block, ie. lower the block frequency?     

> __< g​onbat.zano:zano.org >__ To gingeropolous:  Qubic can go away tomorrow, there's still the long time issue of only needing 100k to attack for a month, security budget needs to raise, and price alone won't cut it     

> __< b​oog900:monero.social >__ that would make it easier to remove more PoW?     

> __< c​haser:monero.social >__ kayabanerveI in a trailing finality layer as you propose it, what would happen if a malicious pool attempts a reorg that's deeper than the trailing span?     

> __< k​ayabanerve:matrix.org >__ It wouldn't be acknowledged. Nodes would always follow a blockchain descending from the last finalization.     

> __< o​frnxmr:monero.social >__ this would make it more difficult to reorg, no? - changing to 4 minute blocktimes causing a dbling of the difficulty. (Also increases size of p2pool payouts, and blocks(?))     

> __< g​ingeropolous:monero.social >__ aight, lemme try and summarize my idea again. There's a rolling window. When you mine a block, a new protocol decreases the friction for you to add a block in the future. The more friction you have (by being a new miner) means that nodes question whether to add your 7 blocks to the chain tip. The less friction you have, means that your future block will be added to chain tip without question     

> __< g​ingeropolous:monero.social >__ obvi difficult to implement during an attack.     

> __< k​ayabanerve:matrix.org >__ That would seem to encourage centralizing to just a few pools, if not one or two?     

> __< c​haser:monero.social >__ kayabanerve: in that case, how would a node syncing from genesis decide between two conflicting chains?     

> __< s​yntheticbird:monero.social >__ so you would add mining state into blocks?     

> __< b​oog900:monero.social >__ I would have assumed reorging 2 blocks at half the difficulty would've been harder than 1, but I could be wrong     

> __< g​ingeropolous:monero.social >__ no, normal miners could still have decreased friction.     

> __< k​ayabanerve:matrix.org >__ chaser There should never be two distinct finalized chains.     

> __< s​gp_:monero.social >__ gingeropolous: does this not encourage consolidation around a single pool? I don't follow     

> __< k​ayabanerve:matrix.org >__ That's either a catastrophic error, or we could adopt a synchronous tiebreaker based on most work exclusively for initial block downloading.     

> __< s​pirobel:kernal.eu >__ i support the finality layer idea, also because staked validators can help with the eclipse / spam attack on nodes.     

> __< g​ingeropolous:monero.social >__ So your a solo miner. You mine a block. You have high friction because you don't mine blocks that often. Your block makes it to another node. They have to choose whether to add your block. Your single block has high friction, but its a single block.     

> __< j​effro256:monero.social >__ venture: no. If we increase the block time, the *amount of time* that a reorg spans is the same, just a fewer number of blocks. It has no effect on security or really UX, except now that the block time is higher. It may result in a lower block propogation time to block time ratio, which increases stability, but that really isn't a huge issue in the context of this discussion     

> __< g​ingeropolous:monero.social >__ Now say you are an attacker. You mine 6 blocks. You have high friction because you don't mine that often. This 6 block thing comes to a node. The node goes "hey, you have high friction. I don't think I should add these blocks"     

> __< v​enture:monero.social >__ boog900: current successful re-orgs with less than 51% happen only by luck over time, Ruckniums meta attack. that would be mitigated somewhat if the difficulty for a block was doubled (ie, 4-min blocks)     

> __< o​frnxmr:monero.social >__ ginger, isnt this backwards? Amd is pro-pool, anti solominer?     

> __< Soiled >__ Have we thought about working on making propagation faster for all blocks     

> __< g​ingeropolous:monero.social >__ if the attacker only sent 1 block, then yeah, the node may consider adding it     

> __< s​gp_:monero.social >__ 1 year block times here we go /s     

> __< j​effro256:monero.social >__ gingeropolous: this is more or less uncle blocks, yeah?     

> __< k​ayabanerve:matrix.org >__ This seems to optimize mining around low friction nodes which will be frequent miners, AKA large pools, and would simultaneously eliminate p2pool which can't identify itself as a pool in its current form.     

> __< k​ayabanerve:matrix.org >__ (or at least, never let it get to a lower friction state)     

> __< a​rticmine:monero.social >__ Are there any other non POW proposals under consideration?     

> __< g​ingeropolous:monero.social >__ it depends on how large the window is     

> __< g​ingeropolous:monero.social >__ and the main thing is to prevent selfish mining     

> __< Soiled >__ has anyone looked into Stellar's Proof of Agreement?     

> __< b​oog900:monero.social >__ I would have thought more blocks lowers the part luck plays     

> __< g​ingeropolous:monero.social >__ there's no reason a 6 block re-org from the same miner should come to a node and the node go "yup this is obviously better than what i have"     

> __< Soiled >__ I think the main way we can prevent selfish mining is taking a page from Bitcoin book from 2015 with what they did with FIBRE     

> __< g​ingeropolous:monero.social >__ and selfish mining is the mechanism of double spend 51% attacks blah blah     

> __< a​ntilt:we2.ee >__ yes     

> __< k​ayabanerve:matrix.org >__ Non-BFT PoS and using Ethereum for finality would be the other non-PoW non-FL discussions.     

> __< k​ayabanerve:matrix.org >__ (Or using BTC)     

> __< v​enture:monero.social >__ boog900: seemingly, but re-orgs "roll-back" in time, and the odds of finding a block is higher with more frequent blocks.     

> __< s​yntheticbird:monero.social >__ I'll also redrop the Proof of Space which is way harder to rent     

> __< b​oog900:monero.social >__ I would not want to depend on another network     

> __< Soiled >__ I don't think we should depend on other chains     

> __< g​ingeropolous:monero.social >__ i mean i'd prefer merge mining with BTC over anything else. Easy enough to fork away from if BTC gets compromized     

> __< s​gp_:monero.social >__ I know kayaba rescinded TEE due to it not helping with the 51% PoW attack, but TEE is one option to keep in mind due to it potentially being useful at mitigating individual tx censorship. I only mention this for completeness, I'm not actually _for_ TEE at this stage     

> __< k​ayabanerve:matrix.org >__ SyntheticBird: PoS is still _a_ PoW.     

> __< a​ntilt:we2.ee >__ tell me more...     

> __< o​frnxmr:monero.social >__ "if btc gets compromised" welcome to 2017?     

> __< s​yntheticbird:monero.social >__ A lot of problems seems easy to eliminate through forking unsurprisingly     

> __< g​ingeropolous:monero.social >__ well i'll run my idea through my simulator and see how solo miners do     

> __< b​oog900:monero.social >__ but the odds of finding more blocks with the same PoW as one big one with luck would be smaller     

> __< k​ayabanerve:matrix.org >__ I rescinded it because it doesn't really help with anything sgp_:     

> __< Soiled >__ P2Pool are already able to take one block into a single network packet and sends it to many peers at once, with packet sizes less than 1 KiB. but this is just in the p2pool software, is there anyway this can be implement for all nodes so that non-p2pool pools get the same ability     

> __< s​yntheticbird:monero.social >__ very true, the second point stand tho. cpu is easier to rent than storage     

> __< Soiled >__ Bitcoin was compromised by Blockstream a while ago     

> __< s​yntheticbird:monero.social >__ I'm not shilling it btw, just notating it here     

> __< k​ayabanerve:matrix.org >__ It fails during a 51% attack and doesn't solve anything not already 'solved' when there isn't a 51% attack.     

> __< a​rticmine:monero.social >__ The Intel ME is a TEE. A rather controversial one     

> __< s​pirobel:kernal.eu >__ sgp_:  i 100% agree with ArticMine  when it comes to TEE. tee is just horrific and we should not entertain this     

> __< k​ayabanerve:matrix.org >__ > The TEE solution I proposed has been withdrawn and I maintain is fundamentally misunderstood by anyone still yelling against it because TEEs are insecure.     

> __< k​ayabanerve:matrix.org >__ It's fun how I said this almost an hour ago.     

> __< Soiled >__ lol     

> __< s​yntheticbird:monero.social >__ I was gonna quote it     

> __< o​frnxmr:monero.social >__ hey. I'm not pretending to understand it     

> __< s​gp_:monero.social >__ I brought it back, I thought it could still help with anti censorship. I'll sync on this later and we can drop further discussion here     

> __< r​ucknium:monero.social >__ I aim to not break any meeting length records again, so I would like to have the "main part" of the discussion end in 15 minutes. Of course, discussion can continue in this room and #monero-research-lounge:monero.social  . At the end, I want specific people to commit to specific steps to advance this R&D agenda.     

> __< k​ayabanerve:matrix.org >__ The only actionable item here that I see is one of two:     

> __< k​ayabanerve:matrix.org >__ - Attempt rough consensus on a fee policy     

> __< k​ayabanerve:matrix.org >__ - Attempt rough consensus on if my CCS would be received or immediately declined as work on a path we haven't agreed to take, even though my CCS would be to write how that path would look     

> __< a​ntilt:we2.ee >__ can you point me to a description?     

> __< k​ayabanerve:matrix.org >__ I don't believe we'll agree to any hard forks today, and I'm unsure there's any other relay rules we can discuss today.     

> __< s​yntheticbird:monero.social >__ I'm personally interested into having your CCS completed before discussing it     

> __< s​gp_:monero.social >__ (or if anyone else wants to help with TFL research)     

> __< Soiled >__ Pumping up the fee can help with miner profitability, does anyone know the average amt a block receives in fees?     

> __< k​ayabanerve:matrix.org >__ I would like to not spend a few hours drafting a CCS to explore, explain, and recommend a FL unless that would potentially be accepted depending on if the proposal itself is fair.     

> __< k​ayabanerve:matrix.org >__ (I don't charge millions of dollars)     

> __< a​rticmine:monero.social >__ How about the proposals from trevador and Sech1 that have effectively been sidelined?     

> __< k​ayabanerve:matrix.org >__ flip flop: The first would be as in Zano, the second would be exactly what it says.     

> __< s​yntheticbird:monero.social >__ can someone link sech1 proposal?     

> __< k​ayabanerve:matrix.org >__ Those require hard forks. I don't believe we'll agree on a hard fork today.     

> __< s​yntheticbird:monero.social >__ im all for tevador one but as rbrunner said it will take time to implement     

> __< k​ayabanerve:matrix.org >__ SyntheticBird: Miners sign their blocks and get a minimum percent of the reward.     

> __< r​ucknium:monero.social >__ I personally don't support a fee change in the short term because it does not help with the short-term problem. In the medium or long term, fee policy changes could be a good idea, especially if it were linked to PoW difficulty as an oracle for the purchasing power of 1 XMR.     

> __< Soiled >__ Is that to prevent the hidden mining tactic pubic tried doing?     

> __< s​pirobel:kernal.eu >__ I think we should have another one that rips the band aid off completely. no inflation PoS     

> __< o​frnxmr:monero.social >__ - 10 block reorg limit. Doesnt require hf, can be opt-in.     

> __< o​frnxmr:monero.social >__ - sanity check on block contents. Not accepting lower quality blocks that arrive later than higher quality ones     

> __< o​frnxmr:monero.social >__ - potential block frequency change     

> __< k​ayabanerve:matrix.org >__ Also, no one has to listen to me as I try to co-opt Rucknium's position of chair. I'm only trying to steer to what could happen today because:     

> __< k​ayabanerve:matrix.org >__ 1) I explicitly have self-interest     

> __< k​ayabanerve:matrix.org >__ 2) I figure we'll continue discussions this next week and only need the meeting for summaries, reasonable clarification (< 2 hours of it), and rough consensus     

> __< s​gp_:monero.social >__ I'm sorry but an opt-in 10 block reog limit is literally you opting in to run on a different network than everyone else if anything goes wrong     

> __< k​ayabanerve:matrix.org >__ Soiled: No, it's to reduce pool mining.     

> __< Soiled >__ Gotcha     

> __< k​ayabanerve:matrix.org >__ ofrnxmr: The first assumes a synchronous network. The second keeps miners on worse block chains when being attacked.     

> __< o​frnxmr:monero.social >__ Blame bch. Theirs is entirely modifiable with a runtime flag 😅     

> __< Soiled >__ BCH good     

> __< b​oog900:monero.social >__ and not is opting to run on a chain which could have a load of txs removed by an attacker?     

> __< k​ayabanerve:matrix.org >__ Instead of miners immediately jumping to a longer chain to best purpose their work, they'd continue on a worst chain by choice 🤮     

> __< o​frnxmr:monero.social >__ We literally have cjeckpoints rhat do this already     

> __< o​frnxmr:monero.social >__ Dns checkpoints can force those who opt-in onto a core-decided chain     

> __< k​ayabanerve:matrix.org >__ It makes selfish mining easier as now, even when you do finally publish, you don't have competition.     

> __< b​oog900:monero.social >__ yeah if someone reorgs beyond checkpoints we would have multiple chains right now     

> __< o​frnxmr:monero.social >__ Peopke running 18.3.4 can reorg deeper rhan 18.4.1     

> __< k​ayabanerve:matrix.org >__ We can move to a single checkpoint of the last PoW-only block if we adopt a finality layer /s     

> __< b​oog900:monero.social >__ We can add rules that prioritizes chains that were published for longer     

> __< k​ayabanerve:matrix.org >__ ... that literally just wastes honest hash power     

> __< s​gp_:monero.social >__ option Z: monero devs run the finality layer exclusively with frequent DNS checkpoints #centralization     

> __< b​oog900:monero.social >__ a 9 block alt chain should not be mined on if a 9th block comes from the previous main chain     

> __< k​ayabanerve:matrix.org >__ It has honest hash power waste time on a worse chain, before they actually mine a candidate chain     

> __< o​frnxmr:monero.social >__ - sanity check on block contents. Not accepting lower quality blocks that arrive later than higher quality ones     

> __< o​frnxmr:monero.social >__ Boog, thats similar to this     

> __< k​ayabanerve:matrix.org >__ For chains of equal work, I believe nodes already prefer the first seen? No?     

> __< g​ingeropolous:monero.social >__ i mean, thats why the DNS checkpoint system was created, for defense etc, afaik     

> __< o​frnxmr:monero.social >__ Sgp: isnt that why the dns-checkpoints flag was created     

> __< j​effro256:monero.social >__ kayabanerve:  Yes     

> __< b​oog900:monero.social >__ split network > 1000 block reorg     

> __< k​ayabanerve:matrix.org >__ So your proposal boog900 would only help for chains of more work and less time seen vs less work and more time seen, which is why it wastes honest hash     

> __< o​frnxmr:monero.social >__ First seen, but they will reorg to longest chain, even ia longest is selfish     

> __< b​oog900:monero.social >__ temp split network*     

> __< a​rticmine:monero.social >__ Are there any more items on the agenda?     

> __< k​ayabanerve:matrix.org >__ It also allows taking advantage of network conditions to make a second-seen chain less preferred, even if first broadcast     

> __< b​oog900:monero.social >__ possibility of*     

> __< r​ucknium:monero.social >__ There are no more items on the agenda     

> __< k​ayabanerve:matrix.org >__ ArticMine: My attempts for rough consensus on two items I thought we may be able to, and more running in circles.     

> __< Soiled >__ Has anyone considered faster block propagation     

> __< k​ayabanerve:matrix.org >__ Or none per the official agenda :p     

> __< s​yntheticbird:monero.social >__ Sir it's been 7 months, can i sleep now?     

> __< b​oog900:monero.social >__ this was part of the 10 block max reorg FWIW     

> __< b​oog900:monero.social >__ it would only be for blocks close to the boundary     

> __< b​oog900:monero.social >__ to try mitigate the risks of a chain split     

> __< k​ayabanerve:matrix.org >__ That assumes a synchronous network :///     

> __< b​oog900:monero.social >__ a small price to pay     

> __< k​ayabanerve:matrix.org >__ Considering synchronous networks don't exist IRL?     

> __< k​ayabanerve:matrix.org >__ They're solely ideal models of computers?     

> __< k​ayabanerve:matrix.org >__ I disagree.     

> __< k​ayabanerve:matrix.org >__ We should move to a solution which works in asynchronicity.     

> __< b​oog900:monero.social >__ as long as their is not someone constantly wasting an immense amount of hashes keeping the bad chain it'll resolve it self eventually     

> __< b​oog900:monero.social >__ if not a simple update to the built in checkpoints will kill it     

> __< k​ayabanerve:matrix.org >__ The fact sticky chains wastes any hash power of honest miners presumably decreases honest miner profitability.     

> __< b​oog900:monero.social >__ we have never had a 8 to 9 block reorg so it would be very small     

> __< k​ayabanerve:matrix.org >__ And re: a max re-org depth, no, the difficulty on the alt will trend to 0 and be infinitely cheap to keep alive indefinitely.     

> __< k​ayabanerve:matrix.org >__ Not really when an adversary is already so large and doing all of these attacks?     

> __< b​oog900:monero.social >__ it would have less PoW eventually?     

> __< k​ayabanerve:matrix.org >__ It'd tip in their favor further.     

> __< k​ayabanerve:matrix.org >__ But with a max re-org depth, they won't re-org back to the chain with the most work boog900:     

> __< j​effro256:monero.social >__ boog900:  Guaranteed network splits at 10 blocks would certainly increase the incentive for an attacker to go for a 10-block reorg     

> __< k​ayabanerve:matrix.org >__ I will no longer be present here in the remnants of the meeting but solely popping in occasionally. Bye y'all.     

> __< a​rticmine:monero.social >__ I just don't see these highly controversial solutions where there is clearly little consensus as an option.     

> __< a​rticmine:monero.social >__ 1) TEEs . Thankfully this has been withdrawn      

> __< a​rticmine:monero.social >__ 2) 2 POS hybrid solutions.     

> __< a​rticmine:monero.social >__ The harm in my view is that the above are distracting the community from even considering way less disruptive proposals, that are way less controversial.     

> __< s​yntheticbird:monero.social >__ good night     

> __< s​yntheticbird:monero.social >__ ArticMine, this is the non-PoW section     

> __< s​yntheticbird:monero.social >__ we are deemed to discuss controversial changes     

> __< n​oname-user0:matrix.org >__ hybrid solutions are more forward looking imho     

> __< r​ucknium:monero.social >__ I don't see a lot of support for immediate relay-rule fee changes. kayabanerve  has a proposal on the table for him to draft a CCS on Trailing Finality Layer research (the proposal would be subject to all the normal discussion and vetting as any other CCS, if proposed). What does everyone think of the proposal to write a CCS proposal?     

> __< b​oog900:monero.social >__ true, but you would need to publish at the exact right time and also have those blocks ready and mined     

> __< o​frnxmr:monero.social >__ +1 of research proposal. I dont see any problem with looking into it     

> __< b​oog900:monero.social >__ also this is why I mentioned prioritizing the chain that got reorged?     

> __< b​oog900:monero.social >__ maybe if you got reorged at 9 blocks the limit is dropped?     

> __< h​ardenedsteel:monero.social >__ are there estimation of the hashrate of the attack?     

> __< h​ardenedsteel:monero.social >__ we can roughly calculate how much hashrate coming by observing staled (orphaned) blocks     

> __< h​ardenedsteel:monero.social >__ https://static.learnmeabitcoin.com/technical/blockchain/51-attack/equation-success.png     

> __< a​rticmine:monero.social >__ Good day     

> __< s​pirobel:kernal.eu >__ ArticMine: the pow game has been plaid out. its either asics, gpus or cpus. I personally think the endgame for private digital cash is zero inflation pos with 1-10 second finality. (default path sub 2 second finality)     

> __< g​onbat.zano:zano.org >__ ArticMine: how much do you think Monero security budget needs to increase? 2x, 10x?      

> __< g​onbat.zano:zano.org >__ The latter only happens with drastic approaches     

> __< b​oog900:monero.social >__ for the reorged chain only*     

> __< r​ucknium:monero.social >__ I will search the research literature for ways to harden PoW consensus. I will also try to get a basic understanding of Trailing Finality Layer and the research on Proof-of-Stake failure modes. I haven't looked into PoS much because PoW-only was taken for granted.     

> __< s​gp_:monero.social >__ I think Zcash's resources are a good starting point for TFL research     

> __< j​effro256:monero.social >__ I'm heading out. Good meeting, y'all, thanks to everybody who participated.     

> __< a​ntilt:we2.ee >__ https://electriccoin.co/blog/the-trailing-finality-layer-a-stepping-stone-to-proof-of-stake-in-zcash/     

> __< c​haser:monero.social >__ Rucknium: Kayaba said they'll write the proposal only if there's a good chance of it being accepted so it's not in vain. can anyone here give such a guarantee? I personally see the mentioned exploratory work as useful and support the effort.     

> __< Soiled >__ One Weird Trick to Stop Selfish Miners > https://eprint.iacr.org/2014/007.pdf     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< s​yntheticbird:monero.social >__ Thanks     

> __< s​gp_:monero.social >__ Thank you Rucknium for breaking this up and focusing the discussion!     

> __< k​ayabanerve:matrix.org >__ I more meant if MRL is cool with it chaser     

> __< Soiled >__ Have a good one yall     

> __< v​enture:monero.social >__ Thanks, good night.     

> __< r​ucknium:monero.social >__ Feel free to continue discussing here or in #monero-research-lounge:monero.social     

> __< k​ayabanerve:matrix.org >__ Because Monero Community will want MRL to sign off     

> __< k​ayabanerve:matrix.org >__ So I wanted to ask if MRL may even sign off, and not ouright refuse it because we aren't currently working on a FL, and it sounds like yes     

> __< s​pirobel:kernal.eu >__ Rucknium:  also look into how much the security budget and cost of attack is in PoW vs PoS that would be helpful in having an informed discussion and if a hybrid would ever make sense from an economic point of view     

> __< c​haser:monero.social >__ kayabanerve: got it. several people said yes here, none against     

> __< s​gp_:monero.social >__ Shower thought on the 10 block lock (I haven't thought it through that thoroughly): it might incentivize pools to only publish their combined blocks in 10-block batches (?)     

> __< s​gp_:monero.social >__ *10 block reorg limit     

> __< n​oname-user0:matrix.org >__ it's optional to follow it. it's more of a suggestion. and if you dont agree to --enforce-dns-checkpointing then you will naturally still follow the normal longest chain rules afaik. so this would cause some serious network splits unless the enforce flag was default.     

> __< r​ucknium:monero.social >__ HardenedSteel: I tried using the method of Ozisik, Bissias, & Levine (2017) "Estimation of Miner Hash Rates and Consensus on Blockchains" https://arxiv.org/abs/1707.00082     

> __< r​ucknium:monero.social >__ but I don't get the iterative algorithm to converge. I will try again sometime.     

> __< s​pirobel:kernal.eu >__ kayabanerve: i dont think a hybrid pow pos system makes sense, but I still support your proposal because it moves the discussion forward.     

> __< h​ardenedsteel:monero.social >__ can you look up on that: https://learnmeabitcoin.com/technical/blockchain/51-attack/     

> __< h​ardenedsteel:monero.social >__ https://matrix.monero.social/_matrix/media/v1/download/monero.social/hZYSyVFKoYEDsvMZfzAASiqM     

> __< r​ucknium:monero.social >__ spirobel: Ok. That is a lot to do in a week (with everything else), but I can get to it eventually.     

> __< h​ardenedsteel:monero.social >__ there's also ruby code calculate     

> __< h​ardenedsteel:monero.social >__ given time span, the attacker roughly has ~20% hashrate     

> __< s​pirobel:kernal.eu >__ its the first question you have to ask rucknium. because if the conclusion is that pow is vastly less secure more expensive than pos: why bother with pow and hybrid systems?     

> __< r​ucknium:monero.social >__ I think the case has already been made that with side-payments, cost to attack PoS can be the cost of paying an interest rate.     

> __< r​ucknium:monero.social >__ But I will have to look into the research!     

> __< s​pirobel:kernal.eu >__ the state of the art on consensus systems currently is between alpenglow and Mysticeti     

> __< s​pirobel:kernal.eu >__ everything else is a sideshow of obscure low market cap stuff or highly theoretical     

> __< r​ucknium:monero.social >__ HardenedSteel: Thanks. I just skimmed it. I think mine is better :D https://github.com/monero-project/research-lab/issues/102#issuecomment-2402750881     

> __< r​ucknium:monero.social >__ I think they are using the original Satoshi formula, which had a small error.     

> __< m​rmatrixer:matrix.org >__ What users are the official devs?     

> __< h​ardenedsteel:monero.social >__ > Here's the equation from the Bitcoin Whitepaper (Section 11):     

> __< g​onbat.zano:zano.org >__ Current Pure PoS impmementation like ETH have very centralized ways to avoid long range attacks, it's why Zano sticks to hybrid even though we believe PoS is superior     

> __< s​pirobel:kernal.eu >__ the issue with zano is that its a very small community so its centralized in any case.     

> __< g​onbat.zano:zano.org >__ let's move to lounge     

> __< s​pirobel:kernal.eu >__ the game is between ETH, solana and (in theory) sui     

> __< s​pirobel:kernal.eu >__ ok     

> __< f​reeman:cypherstack.com >__ Hi all! I've been OOTL recently, but does anyone have an analysis estimating the Qubic control percentage, based on probability of replacing the top X blocks? I would be very interested in comparing anyone's analysis, thanks     

> __< h​ardenedsteel:monero.social >__ read a bit little above     

> __< h​ardenedsteel:monero.social >__ read little bit above     

> __< f​reeman:cypherstack.com >__ I should have been more thorough 😅 thanks a ton, I look forward to reading these     

> __< h​ardenedsteel:monero.social >__ judging from the table and https://moneroconsensus.info/      

> __< h​ardenedsteel:monero.social >__ around ~23%     

> __< r​ucknium:monero.social >__ Freeman Slaughter: IMHO, the is hard to estimate because their hashpower changes a lot from hour to hour. For a reliable estimate you need a large sample size at a constant hashrate. Plus, they don't broadcast the attacking chains that they mine, when they are trying that strategy. PlusPlus, their true strategy is unknown, i.e. we don't know why they try to mine long attacking cha<clipped message     

> __< r​ucknium:monero.social >__ ins sometimes and not other times.     

> __< r​ucknium:monero.social >__ I mean they don't broadcast the chain that end up losing the race     

> __< h​ardenedsteel:monero.social >__ it may looking like they dont have constant hashrate because they dont broadcast the all chains     


# Action History
- Created by: Rucknium | 2025-08-12T21:33:07+00:00
- Closed at: 2025-08-23T16:34:56+00:00
