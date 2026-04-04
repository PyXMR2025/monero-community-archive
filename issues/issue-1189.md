---
title: Monero Research Lab Meeting - Wed 16 April 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1189
author: Rucknium
assignees: []
labels: []
created_at: '2025-04-15T20:52:00+00:00'
updated_at: '2025-04-25T15:27:12+00:00'
type: issue
status: closed
closed_at: '2025-04-25T15:27:12+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. FCMP alpha testnet, stressnet, and public testnet planning.

4. Decide on publicising the method to find [proxy nodes](https://github.com/monero-project/research-lab/issues/126).

5. [Franzoni & Daza (2022). "Clover: An anonymous transaction relay protocol for the bitcoin P2P network"](https://moneroresearch.info/222).

6. [Yang, Xu, & Zhu (2025). "De-anonymizing Monero: A Maximum Weighted Matching-Based Approach."](https://moneroresearch.info/260)

7. [Release of OSPEAD HackerOne and CCS milestone submissions](https://github.com/Rucknium/OSPEAD). [Analysis of risk of new decoy selection algorithm without a hard fork](https://gist.github.com/Rucknium/fb638bcb72d475eeee58757f754acbee).

8. Any other business

9. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1186 

# Discussion History
## Rucknium | 2025-04-18T19:36:00+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1189     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< b​oog900:monero.social >__ Hi     

> __< c​haser:monero.social >__ hello     

> __< j​berman:monero.social >__ *waves*     

> __< b​randon:cypherstack.com >__ hola     

> __< v​tnerd:monero.social >__ Hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: I submitted two talk proposals to MoneroKon. One on spy nodes with boog900  and one on OSPEAD. Also working on applying xmrack 's machine learning code to the analysis of OSPEAD deployment risk without a hard fork.     

> __< r​ucknium:monero.social >__ surae: Do you want something added to the agenda?     

> __< v​tnerd:monero.social >__ me: still working on lws-frontend subaddresses (primarily) among other things related to that frontend project     

> __< b​randon:cypherstack.com >__ nope, just observin'     

> __< j​berman:monero.social >__ me: continuing with serialization of an FCMP++ blinds cache (for saving the expensive divisor calculations in the wallet cache early on so that wallets can construct FCMP++'s nearly instantaneously at tx construction time), nearly done, then working on addressing jeffro's PR comments over here: https://github.com/seraphis-migration/monero/pulls     

> __< j​effro256:monero.social >__ Howdy     

> __< r​ucknium:monero.social >__ 3) FCMP alpha testnet, stressnet, and public testnet planning.     

> __< j​effro256:monero.social >__ me: working on supporting all smaller `wallet2` features for Carrot txs as I see issues crop up. Examples: cold signing protocol, the superfluous main tx pubkey issue, scanning from transaction prefixes, payment proofs, etc     

> __< a​ntilt:we2.ee >__ ⏳     

> __< r​ucknium:monero.social >__ Tentatively, I think stressnet could commence two months after alpha testnet starts and/or one month after the FCMP++ coding competition ends, whichever is later     

> __< j​effro256:monero.social >__ tobtoht: mentioned that he already got Carrot/FCMP++ transaction construction working in Feather wallet which is really cool IMO     

> __< r​ucknium:monero.social >__ We know when the coding competition will end, so when might the alpha testnet start?     

> __< j​effro256:monero.social >__ A stressnet before the competition ends might be helpful for us to figure a baseline for speed earlier in development and focus on non-cryptography related issues     

> __< j​berman:monero.social >__ I think we can call the alpha testnet an alpha stressnet instead     

> __< j​berman:monero.social >__ On alpha stressnet: I think I can have my FCMP++ side of things ready within the next 3 weeks. I'd defer to jeffro on Carrot timeline for settling on a date     

> __< j​berman:monero.social >__ Main stressnet: I agree I think we can target for 1 month after the coding competition ends     

> __< r​ucknium:monero.social >__ To make it clear: I want some distance between alpha stressnet and "public" stressnet because it is harder to coordinate fixes on the fly with many community people running nodes.     

> __< r​ucknium:monero.social >__ I want alpha stressnet to hit problems first     

> __< j​effro256:monero.social >__ The problem with doing stressnet on the testnet is that future nodes have to download a bunch of bloat that isn't relevant anymore for future HFs     

> __< j​berman:monero.social >__ to be clear, wasn't proposing doing that on the testnet. Was assuming it would be a throwaway stressnet like last one     

> __< rbrunner >__ Yes, for sure don't make regular Monero testnet blockchain too big     

> __< r​ucknium:monero.social >__ I deferred to jeffro and jberman. jberman deferred to jeffro. Everyone is looking at jeffro256  👀     

> __< j​effro256:monero.social >__ Okay you're proposing doing a throwaway network but not making a distinction between stressnet and non-stressnet at first?     

> __< j​effro256:monero.social >__ At least for "alpha"     

> __< j​effro256:monero.social >__ Yeah I'm good with that !     

> __< j​berman:monero.social >__ It would be called "alpha stressnet" so distinct from non-stressnet     

> __< j​effro256:monero.social >__ Carrot, without multisig nor pratical hardware device support, should definitely be ready (and hopefully a bit more polished) in 3 weeks     

> __< j​berman:monero.social >__ (I've held off on discussing public testnet for now, because I think makes sense to settle on the stressnets first)     

> __< j​berman:monero.social >__ Awesome so we're on a similar timeline basically :)     

> __< j​effro256:monero.social >__ But view-only wallets, background sync, cold signing, transaction proofs, and basically all the other features I can think of off the top of my head should be ported to Carrot where needed within that timeframe     

> __< j​berman:monero.social >__ Proposing we target an alpha stressnet in 5 weeks then?     

> __< r​ucknium:monero.social >__ 5 weeks sounds great to me     

> __< r​ucknium:monero.social >__ Does this include the `monero-wallet-cli` and `monero-wallet-rpc` binaries?     

> __< j​effro256:monero.social >__ Yes     

> __< j​berman:monero.social >__ 5 weeks would be May 21st     

> __< r​ucknium:monero.social >__ Anyone object to initiating the alpha stressnet on May 21st?     

> __< r​ucknium:monero.social >__ I think that's settled. :D     

> __< rbrunner >__ Awsome     

> __< r​ucknium:monero.social >__ Unless there are big unforeseen problems     

> __< j​berman:monero.social >__ ACK/NACK on the date from jeffro I think would be good too     

> __< j​effro256:monero.social >__ ACK on May 21st     

> __< r​ucknium:monero.social >__ 4) Decide on publicising the method to find proxy nodes. https://github.com/monero-project/research-lab/issues/126     

> __< r​ucknium:monero.social >__ boog900 wanted to bring this up     

> __< j​berman:monero.social >__ Wait hang on, we can set up targets for the other nets too     

> __< r​ucknium:monero.social >__ Ok     

> __< j​berman:monero.social >__ Proposing 1 month after competition ends for main stressnet     

> __< j​berman:monero.social >__ August 27th     

> __< j​berman:monero.social >__ whoops sorry, July 27th*     

> __< j​effro256:monero.social >__ Will we need a whole month to setup?     

> __< r​ucknium:monero.social >__ jberman: Sounds good to me.     

> __< r​ucknium:monero.social >__ I don't know how long it will take to test and integrate the competition code     

> __< j​berman:monero.social >__ If the competition doesn't yield an improvement to helioselene, it may make sense to implement downloading tree elems for the tree cache instead of rebuilding the tree (or spending time on my end trying my hand at helioselene optimization too)     

> __< j​berman:monero.social >__ which could take 1-2 weeks     

> __< j​berman:monero.social >__ So 1 month would give time to both implement the code and/or do that^, and then 2 weeks of lead time for announcing the next stressnet / preparing binaries?     

> __< r​ucknium:monero.social >__ That sounds reasonable to me     

> __< j​effro256:monero.social >__ Maybe we should wait to set the date, then. If the competition goes well results-wise and the code is trivially integratable, and assuming we already have a good working alpha stressnet, we may only need a couple days between competition end and new network start     

> __< j​effro256:monero.social >__ Although not setting the date until a couple days before sort of defeats the purpose of setting a date     

> __< r​ucknium:monero.social >__ I think at least 2 weeks of notice for stressnet would be good.     

> __< j​berman:monero.social >__ Sounds good to me, we can loosely say here we're targeting that proposed date at the latest, but may set it earlier     

> __< j​berman:monero.social >__ Or just say we're targeting July for main stressnet without specifying the day     

> __< j​berman:monero.social >__ Until we're ready to (with at least 2 weeks of notice)     

> __< r​ucknium:monero.social >__ "Targeting July" sounds good     

> __< j​effro256:monero.social >__ I think a vague-ish time period is fine for testing networks     

> __< r​ucknium:monero.social >__ Are we ready to move on to the next agenda item?     

> __< j​berman:monero.social >__ Last thing     

> __< j​berman:monero.social >__ On public testnet: ideally this will run after all code is ready and merged (which means audited and reviewed). If we really push, I think we can complete all that 3 months after the main stressnet round of changes     

> __< j​berman:monero.social >__ More conservatively we'd give that 6 months     

> __< j​berman:monero.social >__ So perhaps we target Q4 for public testnet?     

> __< r​ucknium:monero.social >__ Sounds good to me     

> __< j​berman:monero.social >__ Alpha stressnet: May 21st     

> __< j​berman:monero.social >__ Main stressnet: July     

> __< j​berman:monero.social >__ Public testnet: Q4     

> __< r​ucknium:monero.social >__ How much code auditing and mathematics review would be done by then? Nearly all?     

> __< j​berman:monero.social >__ Should be all     

> __< r​ucknium:monero.social >__ There is a nice symmetry about the dates. Getting one unit vaguer on each step.     

> __< r​ucknium:monero.social >__ Which would give FCMP++ mainnet 2026. :P     

> __< r​ucknium:monero.social >__ 4) Decide on publicising the method to find proxy nodes. https://github.com/monero-project/research-lab/issues/126     

> __< r​ucknium:monero.social >__ boog900     

> __< b​oog900:monero.social >__ I think allowing people to see for themselves just how clear it is these nodes are proxies is more beneficial than keeping the method hidden. The fact they have used the same IPs that are known bad for years tells me they cannot change easily and even if they did constantly updating a banlist is not a good solution.     

> __< b​oog900:monero.social >__ We do have other methods to tell apart these nodes, although we would be revealing the best one IMO.      

> __< b​oog900:monero.social >__ I think at some point the method needs to be released for transparency anyway, we did tell the whole network to ban 40% of the reachable node's IPs.     

> __< b​oog900:monero.social >__ Just want to get opinions from MRL before I make it public, does anyone disagree with making it public?     

> __< j​berman:monero.social >__ No disagreement here     

> __< rbrunner >__ Sounds good.     

> __< r​ucknium:monero.social >__ It sounds good to me, especially if subnet deduplication can get into the next binary release. But even if it doesn't, it's ok to disclose.     

> __< r​ucknium:monero.social >__ binary release version*     

> __< j​effro256:monero.social >__ Did we decide that all the proxies originate from one entity? If not, some might change, even if others don't. There might be a psychological element that once they know how we trace them, then they finally get off their asses on do something about it     

> __< j​effro256:monero.social >__ Especially since it seems like a semi-smart coder could fix the issue relatively quickly     

> __< d​oedl...:zano.org >__ [flip flop] lets focus on subnet deduplication impl     

> __< b​oog900:monero.social >__ we haven't, IMO there are at most 2 entities as the nodes from the subnet blocks have slightly different behaviour than nodes from single IPs. The single IPs use a random public node, the subnet blocks use their own node.     

> __< j​effro256:monero.social >__ Well they can't fix many proxies within a small subnet, but they could fix the identifying issue     

> __< j​effro256:monero.social >__ We can focus on dedup'ing subnets without revealing the tracing methodology. Also, to be clear, I'm not totally against disclosure, but there's some downsides to doing so, and the downsides are irrevocable     

> __< d​oedl...:zano.org >__ ??     

> __< d​oedl...:zano.org >__ downsides?     

> __< r​ucknium:monero.social >__ Can't un-ring a bell     

> __< r​ucknium:monero.social >__ Ah, it has its own Wikipedia article: https://en.wikipedia.org/wiki/Unring_the_bell     

> __< r​ucknium:monero.social >__ > In law, unring the bell is an analogy used to suggest the difficulty of forgetting information once it is known.     

> __< d​oedl...:zano.org >__ dedup'ing subnets without revealing the tracing methodology - thats what I meant, of course     

> __< d​oedl...:zano.org >__ are there any open questions on how to impl dedup'ing ?     

> __< r​ucknium:monero.social >__ I don't think so. Just need someone who knows or can read the Monero netcode to implement it, AFAIK.     

> __< rbrunner >__ Yes, it may take some time until somebody comes around to do it     

> __< rbrunner >__ But still, that does not fully change the equation for me: more on the "plus" side of publishing the method     

> __< rbrunner >__ IMHO     

> __< j​effro256:monero.social >__ At least with subnet dedup implemented, people could drop the banlist if they're uneasy about it and get *most* of the spy nodes eliminated     

> __< b​oog900:monero.social >__ Another thing to add is that these nodes are not that effective against monerod. They have 75% of the IP:ports, 40% of the IPs but only make an average 15% of the outbound connections. Although we can't take back the method once public, I still think that allowing more people to see the method should lead to more of a push to impl real fixes.     

> __< d​oedl...:zano.org >__ From your research the method ca be guessed ? So why publish at all ?     

> __< r​ucknium:monero.social >__ We have a reservation from jeffro256  to disclosure right now. Can we return to this next week? (Maybe I am being selfish since I have three Rucknium-themed items left on the agenda).     

> __< r​ucknium:monero.social >__ Or I can push those item to next week instead     

> __< c​haser:monero.social >__ I'm sure this can wait at least another week     

> __< b​oog900:monero.social >__ I found it by sending different requests to these nodes, I think it is unlikely for someone unfamiliar with the P2P protocol to find it.     

> __< b​oog900:monero.social >__ yes     

> __< r​ucknium:monero.social >__ 5) Franzoni & Daza (2022). "Clover: An anonymous transaction relay protocol for the bitcoin P2P network". https://moneroresearch.info/222     

> __< r​ucknium:monero.social >__ boog900  and I have been looking more into this paper. IMHO, the paper doesn't meet the appropriate standard for seriously considering deploying Clover on the Monero network. Maybe it's a good protocol, but the paper doesn't prove and/or provide enough evidence for that hypothesis.     

> __< r​ucknium:monero.social >__ Question to the group: Would you like me and/or boog900  to write a technical review of Clover, like I did Goodell, Salazar, & Slaughter (2024). "Uniformly Most Powerful Tests for Ad Hoc Transactions in Monero": https://github.com/cypherstack/churn/issues/2     

> __< r​ucknium:monero.social >__ That way, you don't have to just "trust me" on it.     

> __< r​ucknium:monero.social >__ Two big issues I see right now are 1) Lemma 2 seems to have wrong assumptions, 2) They seem not to be measuring macro-averaged precision, which is what the Dandelion++ papers do. Instead, they may be using single-node precision, which makes less sense in the problem context.     

> __< b​randon:cypherstack.com >__ I did not see your review!     

> __< b​randon:cypherstack.com >__ bedtime reading :)     

> __< r​ucknium:monero.social >__ Ah, I should have contacted you directly. IIRC, I pinged Diego S. about it     

> __< r​ucknium:monero.social >__ Stay with us, since I'm going to reference your work in the next agenda item, too :D     

> __< d​iego:cypherstack.com >__ I did share it in internal chats     

> __< r​ucknium:monero.social >__ Thanks, Diego     

> __< j​effro256:monero.social >__ Yeah I'd read that ! Especially since it gets brought up so often as an alternative to D++ and has a lot of nice nominal properties, assuming that it actually works     

> __< r​ucknium:monero.social >__ Sounds good. I will probably have something by next meeting.     

> __< c​haser:monero.social >__ I think your criticism of the CS churn paper was well-founded, perhaps such a piece about Clover would encourage the authors to improve the paper, and maybe get it to a point where Monero is confident enough to use it instead of D++     

> __< r​ucknium:monero.social >__ 6) Yang, Xu, & Zhu (2025). "De-anonymizing Monero: A Maximum Weighted Matching-Based Approach." https://moneroresearch.info/260     

> __< r​ucknium:monero.social >__ Thanks xmrack  for finding this paper. It was posted just last week.     

> __< r​ucknium:monero.social >__ I read the paper     

> __< r​ucknium:monero.social >__ TL;DR: The paper tries a new graph-based attack on Monero user privacy. It's not very effective because 1) it doesn't have a good way to get initial edge "weights", i.e. the initial probability that a ring member is a real spend and 2) even when it does have good weights, the new technique doesn't add much more predictive power.     

> __< r​ucknium:monero.social >__ They suggest a "maximum weighted matching" (MWM) technique to try to re-construct the true transaction graph. I think this may be similar or identical to the "maximal matching" idea in a draft MRL research bulletin by Surae and Sarang that was never completed: "Disclosure Attacks and Privacy on Blockchains".     

> __< r​ucknium:monero.social >__ As I understand it, they start with initial probabilities that each ring member is the true spend (i.e. weights on the edges of the possible tx graph). Then they use an algorithm to figure out what is the most likely true tx graph. They use a new approximation algorithm from a 2022 paper, because trying a traditional algorithm would be computationally infeasible for the Monero blockchain.     

> __< r​ucknium:monero.social >__ But it looks like they don't get much additional predictive power, beyond what their initial probability weights give them. The closest thing to a head-to-head comparison is an F1-score of 0.8362 for the original guess-newest heuristic that Moser et al. (2018) use, which increases to 0.8400 when they add the MWM technique. IMHO, they should have had more comparisons.     

> __< r​ucknium:monero.social >__ isthmus speculated that the MAP Decoder attack, enabled by the OSPEAD estimates, could be used for initial weights for this type of analysis, increasing its power. IMHO, the results from this paper suggest that isthmus's fear may have been unfounded after all.     

> __< r​ucknium:monero.social >__ This just adds to the evidence that graph analysis at current ring size isn't very effective. Other evidence in the DM decomposition paper and my analysis of adding the DM decomposition to the flooding attack.     

> __< r​ucknium:monero.social >__ IMHO     

> __< rbrunner >__ Funny how much research those rings attract :)     

> __< r​ucknium:monero.social >__ The DM decomposition paper: Vijayakumaran, S. 2023, Analysis of CryptoNote Transaction Graphs using the Dulmage-Mendelsohn Decomposition https://moneroresearch.info/39     

> __< c​haser:monero.social >__ rbrunner: no wonder, they're the weakest link in the chain :)     

> __< r​ucknium:monero.social >__ Two other minor complaints: They say that spending patterns of output age are stable over time, but it's not true IMHO. If you look at transparent coins like BTC, BCH, LTC, and DOGE, the distributions change a lot from week to week.     

> __< r​ucknium:monero.social >__ My second minor complaint is that they make a strange choice for setting the initial probability weights. They sat it to just the value of the gamma or pareto probability distribution, when they should be considering the ratio of the decoy distribution (which is gamma) and the real spend, like the MAP Decoder does.     

> __< r​ucknium:monero.social >__ [waiting on people typing]     

> __< j​effro256:monero.social >__ > They sat it to just the value of the gamma or pareto probability distribution, when they should be considering the ratio of the decoy distribution (which is gamma) and the real spend, like the MAP Decoder does.      

> __< j​effro256:monero.social >__ Do you feel like that would have a meaningful impact on their research, perhaps tip in into being "slightly useful" category at determining true spends over what data is already in the weights?     

> __< d​oedl...:zano.org >__ they do not measure their effectiveness - do they ??     

> __< r​ucknium:monero.social >__ jeffro256: Maybe. AFAIK, they didn't publish their code. It could be "interesting" to re-run their technique with OSPEAD/Map Decoder. But it would not be a good use of time to re-implement their technique from scratch.     

> __< r​ucknium:monero.social >__ But the way to defeat the technique is to have a better decoy selection algorithm, anyway.     

> __< j​effro256:monero.social >__ <insert OSPEAD ad here>     

> __< r​ucknium:monero.social >__ They measure effectiveness against three datasets: the Moser et al. (2018) real txs that were de-anaonymized using the zero-decoy technique. xmrack 's testnet/stagenet txs that he generated and wrote his own paper about, 3) A set of completely sythetic datasets that they generated to test sensitivity of their results to ring size and decoy selection algorithm     

> __< d​oedl...:zano.org >__ they do: p.12 ~2% and "Monero's current anonymity remains robust"     

> __< r​ucknium:monero.social >__ > Experiment results reveal that the sampling algorithm plays a crucial role.     

> __< r​ucknium:monero.social >__ ^ which is a point many papers make. I list those papers and quotes at the top of https://github.com/Rucknium/OSPEAD/blob/main/CCS-milestone-1/pdf/PRIVATE-OSPEAD-Fully-Specified-Estimation-Plan.pdf     

> __< d​oedl...:zano.org >__ rucknium:monero.social: what are the fringe cases - after fcmp++ ?     

> __< r​ucknium:monero.social >__ That 2% gain over uniform random guessing is with xmrack 's data, who found similar gain using machine learning techniques.     

> __< r​ucknium:monero.social >__ The major ones are in network privacy IMHO     

> __< r​ucknium:monero.social >__ And post-quantum cryptography AFAIK     

> __< r​ucknium:monero.social >__ 7) Release of OSPEAD HackerOne and CCS milestone submissions. Analysis of risk of new decoy selection algorithm without a hard fork.  https://github.com/Rucknium/OSPEAD   https://gist.github.com/Rucknium/fb638bcb72d475eeee58757f754acbee     

> __< r​ucknium:monero.social >__ I have xmrack 's machine learning code working with the simulated old/new DSA ring data: https://github.com/Rucknium/Monero-Dataset-Pipeline     

> __< r​ucknium:monero.social >__ I'm having a computational scaling problem at the moment. 10,000 rings works without errors, but it appears to create overfitting. When I try to increase it to 1 million, it is taking 12 hours and counting. This is on one of the powerful MRL research computing machines.     

> __< r​ucknium:monero.social >__ That's all on that update     

> __< j​effro256:monero.social >__ Does this actually create real, signed ring MLSAG/CLSAG signatures ?     

> __< r​ucknium:monero.social >__ jeffro256: xmrack 's code does. What I'm doing is simulating rings and the rings of their one-hop antecedent txs, then feeding the data directly into the machine learning part.     

> __< r​ucknium:monero.social >__ *machine learning part of xmrack 's code in that repository     

> __< r​ucknium:monero.social >__ I just did a few updates to get things working with current Python module versions, and using .csv files instead of Python's Pickle file format.     

> __< j​effro256:monero.social >__ Without knowing anything else about that pipepline, perhaps this could be a target for optimization. `wallet2` transaction creation in general is very slow and unoptimized, and will be noticeable for the large numbers of transactions that you're simulating     

> __< r​ucknium:monero.social >__ I'm not directly using the wallet2 tx construction code in that repo for what I'm doing right now. The slowdown is in the ML analysis part.     

> __< j​effro256:monero.social >__ Ah     

> __< j​effro256:monero.social >__ Okay I'm out of my depth now     

> __< r​ucknium:monero.social >__ I use R to generate the simulated data: https://github.com/Rucknium/OSPEAD/blob/main/CCS-milestone-2/decoyanalysis/R/monte-carlo.R#L122-L478     

> __< j​effro256:monero.social >__ How long does that portion take?     

> __< r​ucknium:monero.social >__ The R code? Well, I worked a little hard to make it faster :)     

> __< r​ucknium:monero.social >__ About 5-10 minutes for 1 million rings and each of the ring member's antecedents.     

> __< r​ucknium:monero.social >__ `m + m^2 = 272` columns of data.     

> __< r​ucknium:monero.social >__ And I added decent documentation :D     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< j​effro256:monero.social >__ Dang...     

> __< r​ucknium:monero.social >__ The slow part was the intra-ring sorting by age, which was xmrack 's convention. (I'm not sure how much it affects the ML analysis, but I wanted to stick to his work.)     

> __< r​ucknium:monero.social >__ The other slow part (labor time, not computational) was the technical debt I put myself in when I wrote the initial version that used a 3-dimensional array 😅     

> __< r​ucknium:monero.social >__ Which seemed clever and reasonable at the time.     

> __< r​ucknium:monero.social >__ R doesn't use a crypto-secure RNG by default. It uses Mersenne Twister as default. AFAIK, that would be a lot faster than a crypto-secure RNG.     

> __< r​ucknium:monero.social >__ I also ignore "collisions" within a ring since I use draw with replacement. That decision shouldn't affect the results much.     

> __< k​ayabanerve:matrix.org >__ Rucknium: If you're bottlenecked by RNG, there's much faster options. Anything premised on the AES round function will be hardware accelerated to all hell.     

> __< r​ucknium:monero.social >__ kayabanerve: Thanks. Good to know. I'm not bottlenecked by RNG in this task.     

> __< k​ayabanerve:matrix.org >__ Well, not explicitly if bottlenecked, but burdened :p     



# Action History
- Created by: Rucknium | 2025-04-15T20:52:00+00:00
- Closed at: 2025-04-25T15:27:12+00:00
