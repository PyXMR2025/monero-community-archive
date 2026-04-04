---
title: Monero Research Lab Meeting - Wed 06 August 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1250
author: Rucknium
assignees: []
labels: []
created_at: '2025-08-06T00:33:28+00:00'
updated_at: '2025-08-14T21:15:05+00:00'
type: issue
status: closed
closed_at: '2025-08-14T21:15:05+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Proposed Veridise reviews of Helioselene](https://gist.github.com/SamsungGalaxyPlayer/981e8281b91b49901f516eec54ee3c4d).

4. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf).

5. [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).

6. [Spy nodes](https://github.com/monero-project/research-lab/issues/126).

7. PoW mining pool centralization. [Monero Consensus Status](https://moneroconsensus.info/). [TEE-assisted Censorship-Resistant Block Template Production](https://github.com/monero-project/research-lab/issues/134).  [Nonoutsourceable Scratch-Off Puzzles to Discourage Bitcoin Mining Coalitions](https://soc1024.ece.illinois.edu/nonoutsourceable_full.pdf).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1247

# Discussion History
## Rucknium | 2025-08-08T21:16:54+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1250     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< a​rticmine:monero.social >__ Hi     

> __< s​gp_:monero.social >__ Hello     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< rbrunner >__ Hello     

> __< j​berman:monero.social >__ *waves*     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Launched https://moneroconsensus.info/ , which visualizes orphaned blocks and alternative chains, which would tend to appear with greater frequency if a mining pool with a large hashpower share used a selfish mining strategy. Working on adding to the web app by implementing trustless hashpower estimation based on Ozisik, Bissias, & Levine (2017) "Estimation of Miner Hash Rates<clipped message     

> __< r​ucknium:monero.social >__  and Consensus on Blockchains" https://arxiv.org/abs/1707.00082     

> __< v​tnerd:monero.social >__ Me: lwsf and monero_c are working, finally     

> __< j​effro256:monero.social >__ Howdy     

> __< v​tnerd:monero.social >__ Also looking at some other bugs     

> __< s​gp_:monero.social >__ rucknium thanks for setting up that site     

> __< j​berman:monero.social >__ me (repeating from the NWLB meeting Monday): ofrnxmr has been sharing solid bug reports on the FCMP++ integration, been working through them, submit a PR to get rid of initial block hash download on wallet restore from wallet2 + fix deep reorg handling + a slight refactor to wallet2 refresh + address issues ofrn/others have shared. Also got and shared current FCMP++ tx size and ve<clipped message>     

> __< j​berman:monero.social >__ rification time figures here: https://github.com/seraphis-migration/monero/issues/44#issuecomment-3150754862     

> __< a​rticmine:monero.social >__ I did a preliminary review on the FCMP++ transaction sizes and verification times. Will be calculating actual fees.      

> __< a​rticmine:monero.social >__ Have completed the sanity median change. It can work with minimal wallet impact.     

> __< a​rticmine:monero.social >__ The verification time can be taken care of with the multiple minimum node relay level based on size alone     

> __< a​rticmine:monero.social >__ There is no case for weights outside of the non consensus changes in the membership proofs     

> __< a​rticmine:monero.social >__ Otherwise just use actual size     

> __< r​ucknium:monero.social >__ 3) [Proposed Veridise reviews of Helioselene](https://gist.github.com/SamsungGalaxyPlayer/981e8281b91b49901f516eec54ee3c4d).     

> __< g​ingeropolous:monero.social >__ still working on monerosim. focusing on distributed block production     

> __< s​gp_:monero.social >__ Hey all, we received a quote to review the helioselene library that won the recent contest     

> __< s​gp_:monero.social >__ and a similar quote to provide additional documentation to explain why the helios/selene curve selection is safe in this application     

> __< s​gp_:monero.social >__ the details are in the gist, and I am here to answer any questions     

> __< s​gp_:monero.social >__ I believe that Veridise is especially skilled for the library project. Instead of just a review (which they will also do), they will do formal verification     

> __< s​gp_:monero.social >__ for the curve selection, I believe that they are skilled, though others are skilled for that as well. I checked with a few others and they don't have favorable availability     

> __< k​ayabanerve:matrix.org >__ This is modified w.r.t. other low hanging fruit and with an optimized impl of the non-optimized binary GCD. It isn't scoped to include any impl of the optimized GCD nor Rafael's BY inversion at this time. IMO, ideally we'd do the second impl properly, fairly compare the second and third, then move forward, but that'd take me three work days and I do not have the bandwidth. That's <clipped message     

> __< k​ayabanerve:matrix.org >__ why, despite a slower than optimal inversion discussion, we're still discussing moving forward now (as I synced with jberman and jeffro a week ago, though jeffro didn't directly give a reply).     

> __< k​ayabanerve:matrix.org >__ For curve selection, I do like Veridise but not so much I would say no to other competent candidates. Expanding a bit,     

> __< k​ayabanerve:matrix.org >__ tevador proposed Helios/Selene. I verified the choice back in the day.     

> __< k​ayabanerve:matrix.org >__ We're here now, with this optimized impl.     

> __< k​ayabanerve:matrix.org >__ More efficient curve choices are possible. We have a 127-bit Crandall constant, 128-bit when 256-bit aligned. I personally believe a 127-bit constant (when aligned) could be marginally more efficient, and a 104-bit constant would be *notably faster* on certain architectures.     

> __< k​ayabanerve:matrix.org >__ The contest revealed some of this insight, for clarity on timelinem     

> __< k​ayabanerve:matrix.org >__ But more efficient curves will take longer to find and Helios/Selene was the best choice prior. I don't find it necessary nor reasonable to start a new hunt at this time.     

> __< k​ayabanerve:matrix.org >__ So we should get external review of the choice of curve, to tie everything up in a nice bow, and that's the second quote from Veridise.     

> __< r​ucknium:monero.social >__ Those choices would be baked into consensus, right?     

> __< k​ayabanerve:matrix.org >__ But also, Helios/Selene is embedded entirely in the FCMP and can be trivially replaced in a new HF.     

> __< r​ucknium:monero.social >__ After the hard fork     

> __< k​ayabanerve:matrix.org >__ Impl isn't in consensus. Curve choice is. You can skip validating FCMP proofs to avoid requiring Helios/Selene. It has no other contamination.     

> __< s​gp_:monero.social >__ I think the ideal time to hunt for one would have been before the contest. Which is hard because the contest revealed some of these possibilities more clearly. I think helios/selene does the job, and swapping it out now would cause more hard (delay) than benefit     

> __< k​ayabanerve:matrix.org >__ It's not like outputs will now be on Helios or so.     

> __< k​ayabanerve:matrix.org >__ It really is just like if we HFd to a more efficient membership proof, to change the curve     

> __< s​gp_:monero.social >__ *harm not hard     

> __< k​ayabanerve:matrix.org >__ *caveats incurred by the fact we're baking the tree root into the header AFAIK, but eh, it's all fine     

> __< k​ayabanerve:matrix.org >__ Yeah. It's optimally a few percent faster, but an extra month of delay.     

> __< k​ayabanerve:matrix.org >__ I'm presenting everything on the table, even when the reasons to delay are bade choices to follow up on.     

> __< j​berman:monero.social >__ I'm a definite +1 on this proposal as is, looks great to me     

> __< r​ucknium:monero.social >__ A few percentage points is not anything to go chasing after at this stage IMHO. Thanks for the info, though.     

> __< j​berman:monero.social >__ Separately I've been thinking about opening bounties as incentive for research exploration for tasks like searching for a potentially more optimal curve, so it wouldn't need to hold back anything on timeline front, and if someone finds something that demonstrates a significant perf boost, then we can decide to potentially proceed with it then     

> __< rbrunner >__ Astonishing that they will *formal* verification of code     

> __< s​gp_:monero.social >__ rbrunner, see their last project here where they did something similar https://magicgrants.org/2025/08/05/Veridise-Gadgets-Circuit     

> __< j​berman:monero.social >__ Tasks like searching for a more optimal curve, optimizing prove(), and identifying and/or implementing further optimizations to helioselene     

> __< k​ayabanerve:matrix.org >__ It's Veridise's field of expertise. They'll formally verify the algorithm, not the x86 assembly, though.     

> __< k​ayabanerve:matrix.org >__ It's human review, and faith in compilers compiling, that will apply that result to our library.     

> __< r​ucknium:monero.social >__ plowsof has disallowed research bounties on bounties.monero.social     

> __< k​ayabanerve:matrix.org >__ I actually don't think we should look for a new curve and believe we should halt future ECC development, fite me :C     

> __< k​ayabanerve:matrix.org >__ But I'm for people making CCSs for faster impls     

> __< rbrunner >__ sgp: Thanks, interesting     

> __< k​ayabanerve:matrix.org >__ They actually FOSSd their translator tool. Now any circuit on the framework I built can be entered into their tool, Picus.     

> __< s​gp_:monero.social >__ rbrunner definitely give their report for that a read; they go into a lot of detail about how the translated it     

> __< r​ucknium:monero.social >__ This two-part Helioselene Review proposal by Veridise sounds good to me.     

> __< k​ayabanerve:matrix.org >__ (I did not hand write the thousands of equations which is an FCMP. I wrote functions which call functions which expand to thousands of equations while automatically handling labeling and layout)     

> __< j​berman:monero.social >__ The reason I thought of a bounty is because it could potentially attract devs who don't have the bandwidth to commit to a CCS, but with a large enough bounty, could try their hand at it in free time or whatever. I had one specific candidate in mind for this (Fabrizio)     

> __< k​ayabanerve:matrix.org >__ Heard with request we circle back on this jberman     

> __< s​gp_:monero.social >__ jeffro256: any feedback on these quotes?     

> __< rbrunner >__ For the little I can really judge, I am also ok with the proposal     

> __< k​ayabanerve:matrix.org >__ Also, FWIW, tevador proposed multiple curves before the contest. Helios/Selene was the best.     

> __< k​ayabanerve:matrix.org >__ The comments on a better curve is we can more specifically point to specific metrics and how it effects the current code.     

> __< k​ayabanerve:matrix.org >__ That doesn't mean such a curve exists/is feasible to find.     

> __< o​frnxmr:monero.social >__ I wouldn't say plowsof did, and i also thinks more about unsolicited (non mrl) bounties     

> __< r​ucknium:monero.social >__ IMHO, the conversation about research bounties on bounties.monero.social could be re-opened. I should have said that many people agreed that research bounties should be disallowed, and plowsof implemented it.     

> __< r​ucknium:monero.social >__ The problem with research bounties is verifying the quality of the work product and setting completion standards.     

> __< s​gp_:monero.social >__ Maybe allow them only with consensus in this channel; they are difficult to judge and keep focused unfortunately     

> __< s​gp_:monero.social >__ Anyway, that's all from me. I'll move forward with these quotes     

> __< k​ayabanerve:matrix.org >__ Research -1s proof verification plz     

> __< k​ayabanerve:matrix.org >__ +1 xmr     

> __< k​ayabanerve:matrix.org >__ +2 xmr     

> __< k​ayabanerve:matrix.org >__ +10 xmr     

> __< k​ayabanerve:matrix.org >__ Hi, I have a chatgpt account, here's research. Money?     

> __< r​ucknium:monero.social >__ sgp_: Do you want to get loose consensus from MRL today about this? I think it would be OK to do so.     

> __< s​gp_:monero.social >__ If possible, yes I would like loose consensus     

> __< k​ayabanerve:matrix.org >__ I thought we already had it     

> __< r​ucknium:monero.social >__ Everyone who has expressed an opinion has expressed a favorable opinion.     

> __< r​ucknium:monero.social >__ Anyone else?     

> __< k​ayabanerve:matrix.org >__ Is it not loose consensus until Rucknium officially declares it loose consensus     

> __< rbrunner >__ Lol     

> __< s​gp_:monero.social >__ well, you need to draw the line somewhere :)     

> __< o​frnxmr:monero.social >__ Can it be a curve /s     

> __< r​ucknium:monero.social >__ This is actually one of the few things that the chair should do. Unless we want to bootstrap this idea.     

> __< k​ayabanerve:matrix.org >__ Hey, I don't mind, I just thought we had it and I think you thought we did too     

> __< k​ayabanerve:matrix.org >__ (Hence why you said you'd move forward)     

> __< k​ayabanerve:matrix.org >__ Rucknium: sure :p     

> __< r​ucknium:monero.social >__ I mean, the chair shouldn't do much in these types of meetings, but this is one of the few duties, arguably.     

> __< r​ucknium:monero.social >__ I see loose consensus here in favor of "Helioselene Review" by Veridise for 36,250 USD equivalent or less https://gist.github.com/SamsungGalaxyPlayer/981e8281b91b49901f516eec54ee3c4d     

> __< s​gp_:monero.social >__ ty ty, I'll get these started asap then     

> __< r​ucknium:monero.social >__ kayabanerve: Don't tell them about that time I threatened to bring out Robert's Rules of Order in a MAGIC Monero Fund meeting :P     

> __< r​ucknium:monero.social >__ Thanks everyone for your work and input on these reviews and audits.     

> __< r​ucknium:monero.social >__ 4) [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf).     

> __< k​ayabanerve:matrix.org >__ sgp_: swears by those     

> __< k​ayabanerve:matrix.org >__ Maybe we should employ them?     

> __< k​ayabanerve:matrix.org >__ I think SGP misclicked the thumbs down by accident with how excited they were.     

> __< k​ayabanerve:matrix.org >__ /s, onto scaling?     

> __< a​rticmine:monero.social >__ Ok     

> __< a​rticmine:monero.social >__ I went over the TX sizes and verification times     

> __< k​ayabanerve:matrix.org >__ jberman Can you bring your link down, please?     

> __< j​berman:monero.social >__ https://github.com/seraphis-migration/monero/issues/44#issuecomment-3150754862     

> __< k​ayabanerve:matrix.org >__ Thank you     

> __< a​rticmine:monero.social >__ Two things are apparent      

> __< a​rticmine:monero.social >__ 1) Changing the minimum node relay fee based upon transmission size does take care of the verification time issues      

> __< a​rticmine:monero.social >__ 2) We should limit the use of transcription weights to the membership proofs and only to address non consensus changes in size     

> __< a​rticmine:monero.social >__ Otherwise just use the actual size     

> __< k​ayabanerve:matrix.org >__ I'm against actual size because of how actual size is dependent on VarInts.     

> __< k​ayabanerve:matrix.org >__ Estimating the weight impacts the fee impacts the TX size requires re-estimating the weight impacts the fee...     

> __< a​rticmine:monero.social >__ Doos this just apply to the membership proofs?     

> __< k​ayabanerve:matrix.org >__ I'd prefer a simple formula based on inputs, outputs, TX extra, even if it is effectively the TX size for the number it outputs.     

> __< k​ayabanerve:matrix.org >__ No, the fee is a VarInt.     

> __< a​rticmine:monero.social >__ I made we can use fixed weights based upon a set of initial size calculations     

> __< k​ayabanerve:matrix.org >__ It's a really stupid annoyance that *can* be replaced by a single-pass algorithm but that would cause a fingerprint     

> __< a​rticmine:monero.social >__ Then apply it based upon inputs, outputs, tx extra     

> __< rbrunner >__ Stupid question: We can't just serialize a little bit differently and drop those VarInts?     

> __< a​rticmine:monero.social >__ I see no problem with that     

> __< a​rticmine:monero.social >__ What I am against is building a verification time surcharge on the tx weight     

> __< v​tnerd:monero.social >__ I don't recall fee being a varint being that big of an issue, you estimate close to get actual size and the fee only has to be nudged by minimal amount     

> __< v​tnerd:monero.social >__ It is gross because both lwsf and wallet2 do a multi pass for fee calculation, but it's not terrible     

> __< a​rticmine:monero.social >__ The idea would be to use estimated fixed weights that are close enough instead of actual size to simply the wallet calculations     

> __< a​rticmine:monero.social >__ I am fine with that     

> __< rbrunner >__ Simplifying is very welcome IMHO     

> __< a​rticmine:monero.social >__ So is there a loose consensus on this weight approach?     

> __< k​ayabanerve:matrix.org >__ vtnerd: The fact the calculation depends on the result of the calculation is gross. The practical issue is whoever doesn't perform a recursive calculation will have observably different results on the block chain, allowing identifying the wallet used.     

> __< k​ayabanerve:matrix.org >__ I'm against removing the clawback if we allow 128 inputs.     

> __< j​berman:monero.social >__ I'm fine with it. jeffro256 's code already does it fwiw and it's pretty clean     

> __< o​frnxmr:monero.social >__ would this be, within a fre tier, a fixed fee per input? (+ extra for txextra)     

> __< o​frnxmr:monero.social >__ Fee* tier     

> __< k​ayabanerve:matrix.org >__ A 65 input TX will take as long to verify as a 128 input TX, and only benefits from batch verification if other 65+ input TXs are present.     

> __< a​rticmine:monero.social >__ The fee will be  at least 200x higher     

> __< j​berman:monero.social >__ tbc, I'm fine with the approach to determine weight based on n inputs, no outputs, and extra len     

> __< j​berman:monero.social >__ n outputs*     

> __< k​ayabanerve:matrix.org >__ So unless we limit the inputs to 8/16...     

> __< a​rticmine:monero.social >__ For 128 inputs     

> __< k​ayabanerve:matrix.org >__ But compared to 65 inputs, which has the same verification time?     

> __< a​rticmine:monero.social >__ I am actually in favour of limiting input to 16 or even 8     

> __< o​frnxmr:monero.social >__ the 8 inputs is already a pita on my testnet     

> __< k​ayabanerve:matrix.org >__ Yes, but unfortunately it seems at large, the plan is to not YET limit the inputs so.     

> __< k​ayabanerve:matrix.org >__ I think we need the clawback because of that decision.     

> __< k​ayabanerve:matrix.org >__ TBC, I'd love to limit the inputs and simplify out the clawback, later moving to indistinguishability.     

> __< a​rticmine:monero.social >__ I will be calculating fees for the table up to 128 inputs. This may give us a better idea     

> __< k​ayabanerve:matrix.org >__ But the vibe I have now is that we will only limit the amount of inputs when we mandate the amount of inputs.     

> __< k​ayabanerve:matrix.org >__ I believe that to be a poor decision, but it is a decision.     

> __< k​ayabanerve:matrix.org >__ Like, we can at least limit to 32 now so people do have to be more mindful w.r.t. aggregation     

> __< a​rticmine:monero.social >__ It takes into account the actual size and the additional fee level on node relay to make the larger size scale     

> __< k​ayabanerve:matrix.org >__ That way, we don't immediately jump from 128 to 8.     

> __< j​berman:monero.social >__ 65 input tx is taking 2.17s to verify, and is 80k bytes. 128 input tx is taking 3.44s to verify, and is 152k bytes     

> __< k​ayabanerve:matrix.org >__ Hm. That's not as immediately expected. They should share an MSM size....     

> __< a​rticmine:monero.social >__ Both would attract the maximum fee for scaling     

> __< k​ayabanerve:matrix.org >__ Oh. Right. The batch FCMP isn't perfectly aligned to powers of 2 anymore.     

> __< a​rticmine:monero.social >__ 200x minim     

> __< k​ayabanerve:matrix.org >__ Sorry, jberman, how's 50 and 140?     

> __< a​rticmine:monero.social >__ Then there is the size difference on top     

> __< j​berman:monero.social >__ actually correction: 65in-2out is taking 2.17s to verify, and is 80k bytes. 128in-2out is taking 3.42s, 150k bytes     

> __< a​rticmine:monero.social >__ I will have a fee table     

> __< j​berman:monero.social >__ 50in-2out: 1.33s, 62k bytes     

> __< a​rticmine:monero.social >__ For the next meeting     

> __< j​berman:monero.social >__ max tested was 128 inputs     

> __< o​frnxmr:monero.social >__ why would higher number of inputs result in a higher multiplier? as a hot dog vendor, its not _my_ fault that i have 100 customers spending 0.01xmr per day     

> __< a​rticmine:monero.social >__ because of scaling attacks by spamming the high input transactions with minimal cost because they never get to the miner     

> __< r​ucknium:monero.social >__ Some merchants charge a surcharge for paying in BTC because of its fees and the need to consolidate outputs. IIRC, BTCPay Server has a built-in option for this.     

> __< o​frnxmr:monero.social >__ Either i'm forced to create 13 transactions (paying for 8 in 2 out, potentially creating more dusty outputs) or burn my $ on fees by sending all at once     

> __< a​rticmine:monero.social >__ It is a way to DDOS the nodes with transactions that are very unlikely to be miined     

> __< a​rticmine:monero.social >__ The attack works very well in Bitcoin when their blockchain is congested     

> __< a​rticmine:monero.social >__ If there is a high verification cost , then it can be cost effective for the spammer     

> __< r​ucknium:monero.social >__ Let's keep moving:     

> __< o​frnxmr:monero.social >__ the fee doesnt matter if the tx isnt mined though     

> __< r​ucknium:monero.social >__ 5) [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).     

> __< r​ucknium:monero.social >__ Last meeting, jberman  said:     

> __< r​ucknium:monero.social >__ >  w.r.t. stressnet, I'd say let's get 1 more week to address above (refresh refactor, 9473, 8 input PR, and dynamic block sync size)     

> __< k​ayabanerve:matrix.org >__ And jberman Yeah, that's more what I was looking for. ~25% smaller but still most of the verification cost.     

> __< o​frnxmr:monero.social >__ My bc is up at 1.8mb blocks atm.     

> __< o​frnxmr:monero.social >__ Rucknium might have a better method of spamming, but i can produce transactions onky every 10-30 seconds or so     

> __< r​ucknium:monero.social >__ Last stressnet, I handled "slow" tx construction times and unstable wallet-to-node connections by having multiple nodes, each with one wallet connected. Just scaled horizontally.     

> __< j​berman:monero.social >__ Re: stressnet. The good news imo is it looks like the refresh refactor PR has effectively gotten rid of blocking bugs ofrn has reported. Perhaps ofrn can speak to that     

> __< o​frnxmr:monero.social >__ I assume the optimizations help with this? Also hard to spam continuosly due to the 8 inputs limit. Most of my txs have 4 destinations but use 8 inputs, and eventually fail because i dont have enough $ in 8 inputs     

> __< o​frnxmr:monero.social >__ Yeah, most/all of my major issues are resolved     

> __< j​berman:monero.social >__ less good news is seems we still need more time for review     

> __< r​ucknium:monero.social >__ My script controls tx construction so that the spam txs have only one input, unless I specifically request consolidation txs.     

> __< o​frnxmr:monero.social >__ I have multiple wallets and nodes, each wallet produces a tx every 10-40 seconds (bottlenecked at cpu) while it has available outputs     

> __< o​frnxmr:monero.social >__ i did this for a while, but ended up with dust that i cant spend :Dlol     

> __< r​ucknium:monero.social >__ Last time I was using the MRL research computing cluster for the spamming, which has plentiful CPU threads.     

> __< o​frnxmr:monero.social >__ Not enough $ in top 8 inputs to pay the fee     

> __< r​ucknium:monero.social >__ Abandon the dust.     

> __< j​berman:monero.social >__ fwiw, because prove() currently does not scale linearly (https://github.com/kayabaNerve/fcmp-plus-plus/issues/34), constructing >16 input txs will actually be slower than constructing multiple 8-inputs. though with >8 inputs allowed, you will have fewer outputs to make txs from in total     

> __< r​ucknium:monero.social >__ It's actually best to abandon wallets entirely after a while because the database that has to be searched becomes too large, IMHO.     

> __< o​frnxmr:monero.social >__ Yeah, i have. Txs are 8in2out (self spend) 8in3out (send to other 2 wallets) and 8in5out (self spend + send to other 2 wallets)     

> __< r​ucknium:monero.social >__ What more needs to be discussed on alpha stressnet this meeting?     

> __< k​ayabanerve:matrix.org >__ jeffro256: We get 8+ bytes of steg in the change output with CARROT, right?     

> __< o​frnxmr:monero.social >__ Rebasing to master     

> __< o​frnxmr:monero.social >__ Explorer     

> __< k​ayabanerve:matrix.org >__ What if we encrypted the block height of the OLDEST UNSPENT OUTPUT there?     

> __< a​ck-j:matrix.org >__ I can adapt my spammer from a while back to work on stressnet if interested      

> __< a​ck-j:matrix.org >__ https://github.com/ACK-J/Monero-Dataset-Pipeline/blob/main/run.sh     

> __< k​ayabanerve:matrix.org >__ Then scanning is scanning from the chain tip for a change output to learn where to scan from, if one doesn't care about the wallet history?     

> __< s​packle:monero.social >__ Not to harp on this point, but I believe the code sent to stress testing should be required to handle the 32MB blocks allowed in the near term by the new scaling.     

> __< a​rticmine:monero.social >__ Yes     

> __< o​frnxmr:monero.social >__ I'll share mine too. I think mine is probably more straight fwd     

> __< r​ucknium:monero.social >__ xmrack: Interesting suggestion. What would be the advantages? IIRC, your latest version had realistic delays in spending.     

> __< o​frnxmr:monero.social >__ Cant     

> __< j​berman:monero.social >__ I can work on this for next week     

> __< k​ayabanerve:matrix.org >__ Ugh, we lost jeffro an hour ago. Sorry, I just thought of that idea due to Rucknium: 's comment about abandoning wallets. This would allow using the same wallet, only abandoning its history, without issue.     

> __< j​berman:monero.social >__ I'd estimate work involved on the explorer to take 1-2 weeks. so unfortunately would punt this     

> __< o​frnxmr:monero.social >__ Serialization limits hold us back on max block size, but we can always bypass them hm     

> __< k​ayabanerve:matrix.org >__ (And obviously, history would still be retrievable, just with more work).     

> __< o​frnxmr:monero.social >__ Maybe duggavo can update his explorer to add txpool and other info     

> __< s​packle:monero.social >__ Why would you want to bypass the code you are stress testing in order for it to handle the scaling design? If there is a disconnect between performance and scaling design it should be addressed.     

> __< r​ucknium:monero.social >__ AFAIK, this data visualizer "should" at least allow a view of block size: https://github.com/Rucknium/monerod-monitor     

> __< r​ucknium:monero.social >__ I agree with spackle     

> __< o​frnxmr:monero.social >__ Bypass the serialization limits, i mean     

> __< o​frnxmr:monero.social >__ There are multiple prs open for changing them or addressing how we use them     

> __< a​ck-j:matrix.org >__ Rucknium: just another option, I’m not sure it has any advantages or even works anymore lol. The spending delays can be easily changed though like you said     

> __< a​rticmine:monero.social >__ One needs to generate the testnet spam using multiple devices in parallel to simulate the actual Monero network     

> __< j​berman:monero.social >__ If we wanted to block stressnet and wait until scaling design is settled, then I would advocate for a public testnet sooner     

> __< o​frnxmr:monero.social >__ Duggavo's moneroblock explorer lets yoy view block sized etc. Just uses rpc     

> __< o​frnxmr:monero.social >__ I'm using 3 devices, buut still not near mainnet speed     

> __< o​frnxmr:monero.social >__ Jberman, do the optimizations make tx construction faster?     

> __< r​ucknium:monero.social >__ IMHO, no need to wait until scaling design is settled before alpha stressnet. Alpha stressnet is for making sure all the code works with reasonable tx volume.     

> __< s​packle:monero.social >__ Agreed, no need to stop alpha testing. Just want to push that in the fullness of time this must be addressed.     

> __< j​berman:monero.social >__ AFAIK there are no immediate significant optimizations to tx construction on top of the code you're currently testing. Just allowance of >8 input txs, which again may even end up making tx construction slower than you're experiencing     

> __< o​frnxmr:monero.social >__ Yeah, so i think rucknium maybe you should join my testnet and see how well your fare with creating txs using better cpus     

> __< j​berman:monero.social >__ kayabanerve: would daelk ed25519 field arithmetic or faster inverse have a significant impact on tx construction? I don't recall of the top of my head     

> __< j​berman:monero.social >__ dalek* off*     

> __< r​ucknium:monero.social >__ ofrnxmr: Sounds good. Do you want to post in #monero-stressnet:monero.social  ? I may be able to test things late this week.     

> __< k​ayabanerve:matrix.org >__ However much faster HelioseleneField is now to where it was, Ed25519 Field Arithmetic would be Field25519.     

> __< k​ayabanerve:matrix.org >__ Faster inverse speeds up... Point compression most notably.     

> __< a​ck-j:matrix.org >__ In a similar vein as stressnet. Is it realistic to add fuzzing harnesses to the new fcmp cryptographic functions before mainnet? This way they can be fuzzed at scale before we go live     

> __< k​ayabanerve:matrix.org >__ Fuzzing for?     

> __< j​berman:monero.social >__ I would pencil it in as: not expected significant, so would welcome a surprise outcome of significant     

> __< r​ucknium:monero.social >__ 6)  [Spy nodes](https://github.com/monero-project/research-lab/issues/126).     

> __< a​ck-j:matrix.org >__ kayabanerve: similar to https://github.com/monero-project/monero/blob/master/tests/fuzz/bulletproof.cpp     

> __< r​ucknium:monero.social >__ I need to jump into the conversation jeffro256 and rbrunner are having about the details of subnet deduplication: https://github.com/monero-project/monero/pull/9939     

> __< r​ucknium:monero.social >__ 7) PoW mining pool centralization. [Monero Consensus Status](https://moneroconsensus.info/). [TEE-assisted Censorship-Resistant Block Template Production](https://github.com/monero-project/research-lab/issues/134).  [Nonoutsourceable Scratch-Off Puzzles to Discourage Bitcoin Mining Coalitions](https://soc1024.ece.illinois.edu/nonoutsourceable_full.pdf).     

> __< r​ucknium:monero.social >__ On that last paper, there is this reply: Chepurnoy & Saxena (2020) "Bypassing Non-Outsourceable Proof-of-Work Schemes Using Collateralized Smart Contracts" https://eprint.iacr.org/2020/044     

> __< r​ucknium:monero.social >__ Which I learned about from fluffypony.     

> __< r​ucknium:monero.social >__ > Using this, we show how to bypass previously proposed non-outsourceable Proof-of-Work schemes (with the notable exception for strong non-outsourceable schemes) and show how to build mining pools for such schemes.     

> __< r​ucknium:monero.social >__ I don't know what makes a "strong" non-outsourceable scheme and frankly I have not read either paper.     

> __< r​ucknium:monero.social >__ Like I said in my update, I made https://moneroconsensus.info/ to visualize potential malicious mining behavior. I am trying to implement a statistically rigorous and trustless estimator for network hashpower and hashpower of individual mining pools, based on Ozisik, Bissias, & Levine (2017) "Estimation of Miner Hash Rates and Consensus on Blockchains" https://arxiv.org/abs/1707.00082     

> __< a​ntilt:we2.ee >__ "strong" means that the identity of the claimer ("thief") remains anonymous     

> __< rbrunner >__ Sounds a bit like magic that such estimates should be possible ...     

> __< r​ucknium:monero.social >__ Mining pools would need to claim their blocks. The concept is not very difficult: just look at how much PoW each miner is adding to the blockchain.     

> __< r​ucknium:monero.social >__ There will be large confidence intervals when the time window is short.     

> __< a​ntilt:we2.ee >__ a hybrid method has been contemplated by sech1     

> __< a​ntilt:we2.ee >__ also: the paper requires a math phd, but wownero has implemented the basic idea afaik     

> __< r​ucknium:monero.social >__ Ozisik, Bissias, & Levine (2017) also suggest that mining pools report their best hashes frequently, which gives you a verifiable way to estimate hashpower at greater frequency. Basically, p2pool already does that as a side affect, as I understand it.     

> __< a​rticmine:monero.social >__ One concern I see here is to what extent are we encouraging cloud mining     

> __< o​frnxmr:monero.social >__ P2pool only knows its hashrate based on found pool shares. I think centralized pools are more granular because they lffer much lower difficulty shares / target job success at like 10-30 seconds     

> __< r​ucknium:monero.social >__ I don't think any centralized pools post their PoW hashes that don't clear the blockchain difficulty hurdle. They just report what they want on their API, which is not really verifiable AFAIK.     

> __< o​frnxmr:monero.social >__ agreed     

> __< s​packle:monero.social >__ To paraphrase sech1's writing: Demand the first coinbase output to be some % of the block reward (10% for example) and be signed with the private key, and the rest of the block reward can go to as many outputs as you need. Regular pools can still exist controlling 90% of the block reward, solo miners and P2Pool can exist too (P2Pool miners will receive 90% of the block reward regu<clipped message>     

> __< s​packle:monero.social >__ larly in small portions, and 10% in solo-like mode).     

> __< r​ucknium:monero.social >__ I think that moneroconsensus.info was "a hit". It's not very optimized yet, so users could have experienced performance issues. Anyone have issues so far?     

> __< r​ucknium:monero.social >__ Special thanks to DataHoarder who wrote the initial version of the pool data gatherer and quickly added a nice feature to capture orphaned blocks data when it was needed for this web app.     

> __< a​ntilt:we2.ee >__ plus such a change costs Qubic resources     

> __< s​packle:monero.social >__ Yes, it could apply to current events as well as the foreseeable future.     

> __< a​rticmine:monero.social >__ Qubic is turning on and off their Monero mining at a faster rate than is reported by the Monero blockchain.     

> __< r​ucknium:monero.social >__ I do like the direction of the conversation toward some balanced or hybrid approach in the block reward.     

> __< a​ntilt:we2.ee >__ here is a easy summary of the paper by socrates1024(amiller); https://bitcointalk.org/index.php?topic=309073.0     

> __< s​packle:monero.social >__ The relative simplicity makes the hybrid block reward interesting to me, and I do not see any misalignment with the broader goals of Monero.     

> __< a​ntilt:we2.ee >__ quote: >you would prove in zero-knowledge that you know a valid solution     

> __< a​ntilt:we2.ee >__ its a hard fork, but ultimately a valid defence     

> __< r​ucknium:monero.social >__ More conversation about mining centralization?     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< k​ayabanerve:matrix.org >__ There's an existing FCMP test which proves a proof, then malleates each and every byte in it, asserting it fails.     

> __< k​ayabanerve:matrix.org >__ since the FFI with Rust is premised on a simple byte buffer, it should be trivial to fuzz from C     

> __< k​ayabanerve:matrix.org >__ spackle: If it's of no distinction to all existing infra, why would it be of distinction to any infra?     

> __< s​packle:monero.social >__ kayabanerve: Can you be more specific/rephrase, I am not sure I follow.     

> __< s​packle:monero.social >__ If you are referring to the hybrid block reward approach, it makes a difference to all miners except solo.     

> __< c​ountbleck:matrix.org >__ I think it's broken right now     

> __< r​ucknium:monero.social >__ There was an alt chain longer than one block. It crashed the app. I am fixing now. I did warn that it was untested     

> __< k​ayabanerve:matrix.org >__ spackle: You say here regular pools can still exist, and so can P2Pool.     

> __< k​ayabanerve:matrix.org >__ If all existing infra continues, where does the distinction lie? What's the purpose?     

> __< s​packle:monero.social >__ kayabanerve: The purpose is to give an edge to solo miners and p2pool.     

> __< k​ayabanerve:matrix.org >__ How does P2pool *benefit*?     

> __< k​ayabanerve:matrix.org >__ Agreed on somewhat of an edge to solo miners     

> __< k​ayabanerve:matrix.org >__ (The edge is only maintained if there aren't ways to dodge this intent)     

> __< s​packle:monero.social >__ I believe there are ways to dodge the intent, but it enforces that pools have the option. Who would you rather mine with?     

> __< s​packle:monero.social >__ I see my paraphrasing hasn't done things justice, I'd ask you to reference the top of the discussion we had in this channel yesterday: https://libera.monerologs.net/monero-research-lab/20250805     

> __< r​ucknium:monero.social >__ CountBleck: Fixed.     

> __< c​ountbleck:matrix.org >__ oh cool, now I can continue lurking here to learn more about the Qubic situation     

> __< c​ountbleck:matrix.org >__ thanks :3     

> __< s​packle:monero.social >__ If only a single pool did not make people go through a workaround (which I imagine to be inconvenient), it would immediately be a massively better choice than the competition. As a happy coincidence, p2pool would do this by default.     

> __< a​rticmine:monero.social >__ One possible idea with signing the block is that at least one output with a minimum of 0.006 XMR be sent to the signing key. This effectively gives a bonus of 1% to the finder of the block. This is not an unreasonable burden on a pool.      

> __< a​rticmine:monero.social >__ This can also break botnets.     

> __< a​rticmine:monero.social >__ Still I would also like to see AGPL V3+ in the mining and pool code to mitigate cloud mining risks.     

> __< a​rticmine:monero.social >__ I know that such a stiff copyleft is controversial, but at least I see  a discussion on the subject of using copyleft to deter centralized attacks was warranted given the Qubic situation.     

> __< sech1 >__ Qubic lost block a59aa46587b8bbdb76714001e087124f87ff7ad5e44050b5205f7ea0e8147ac0 at height 3472150, but it's not visible on https://moneroconsensus.info/     

> __< b​oog900:monero.social >__ Did qubic mine 3472148 and 3472149?     

> __< sech1 >__ yes     

> __< sech1 >__ they kept selfish mining, but failed (got unlucky) with 3472150     

> __< b​oog900:monero.social >__ Hmm interesting .... Their selfish mining strategy is weird.     

> __< DataHoarder >__ It was there for a second then gone, or maybe it had not gotten data from API yet     

> __< r​ucknium:monero.social >__ I would guess that they are varying the number of blocks they withhold based on time elapsed since last block instead of setting it to a static chain length goal.     

> __< sech1 >__ yes, it looks like they withhold an altchain for a fixed time (2 minutes?)     

> __< sech1 >__ DataHoarder no, a59aa46587b8bbdb76714001e087124f87ff7ad5e44050b5205f7ea0e8147ac0 was never broadcasted to the network. So the API couldn't have seen it at all. That's the limitation of this tool     

> __< c​ountbleck:matrix.org >__ How are you determining whether a block is Qubic's?     

> __< sech1 >__ And one more orphaned Qubic block, 6667672881a08b4fe9158c47770e2b6e70d80cef38c8415e279a39a90b58200a at height 3472167     

> __< c​ountbleck:matrix.org >__ What's going on right now     

> __< c​ountbleck:matrix.org >__ nvm "Known bug that fails to assign some blocks to mining pools" is messing with me     

> __< o​frnxmr:monero.social >__ Thats regarding the explorer     

> __< o​frnxmr:monero.social >__ #monero-research-lounge  for more casual talk / questions. Plz and thx     




## slrslr | 2025-08-11T04:10:24+00:00
"Monero can move to a Proof of Stake system IMO, [Oxen](https://github.com/oxen-io/oxen-core) has created all of the code for a PoS based system where stakers produce new blocks in a cryptonote blockchain, would be good to see them consider this if someone gains 51% of the hashrate"

# Action History
- Created by: Rucknium | 2025-08-06T00:33:28+00:00
- Closed at: 2025-08-14T21:15:05+00:00
