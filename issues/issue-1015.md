---
title: Monero Research Lab Meeting - Wed 29 May 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1015
author: Rucknium
assignees: []
labels: []
created_at: '2024-05-28T20:33:53+00:00'
updated_at: '2024-06-05T22:50:29+00:00'
type: issue
status: closed
closed_at: '2024-06-05T22:50:28+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Potential measures against a black marble attack](https://github.com/monero-project/research-lab/issues/119).

4. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html).

5. Any other business

6. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1012 

# Discussion History
## Rucknium | 2024-06-03T21:53:21+00:00
> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1015     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< v​tnerd:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< a​rticmine:monero.social >__ Hi     

> __< c​haser:monero.social >__ hello     

> __< 0​xfffc:monero.social >__ Hi     

> __< jberman >__ *waves*     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< u​ntraceable:monero.social >__ hi     

> __< r​ucknium:monero.social >__ me: Finished the first draft of "Defeating a Black Marble Flood Against Monero: Best Options for Ring Size and Transaction Fee": https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-optimal-fee-ring-size.pdf     

> __< v​tnerd:monero.social >__ Me: completed LWS remote scanning, looking at how to stress test it to ensure its faster than local only     

> __< jberman >__ me: set up fcmp lmdb tree implementation, implemented grow_tree in the db + tests, now working on trim_tree and still ironing out the implementation     

> __< r​ucknium:monero.social >__ 3) Potential measures against a black marble attack https://github.com/monero-project/research-lab/issues/119     

> __< r​ucknium:monero.social >__ My analysis ^ suggests that a large increase in ring size and a modest increase in fee/byte are good ways to deter a black marble flood or at least limit its impact on effective ring size. We were unsure of how quickly FCMP research and implementation would be moving, but it seems to be on schedule for the optimistic timeline. So a hard fork to increase ring size and/or fee might not make sense.     

> __< r​ucknium:monero.social >__ Did chaser  have any thoughts on the document?     

> __< c​haser:monero.social >__ yes, just a sec. what is the latest prospective timeline for FCMP deployment?     

> __< r​ucknium:monero.social >__ jberman: is the 1.5 years estimate to mainnet the best guess now?     

> __< selsta >__ I'm going to repeat what I said a couple days ago in a different channel, a large increase to the ring size is going to risk the stability of the network if we don't fix the known daemon inefficiency bugs first. We currently have issues with nodes falling behind and nodes running out of memory during high transaction volume.     

> __< r​ucknium:monero.social >__ selsta: How would the Monero Project accomplish the inefficiency fix?     

> __< c​haser:monero.social >__ selsta: you're talking about the many-input transaction stress, right?     

> __< jberman >__ I'd say we're on target for fcmp's and now it's ~1.3 years to mainnet maybe faster     

> __< r​ucknium:monero.social >__ I agree with you that monerod has not performed as well as hoped with the recent tx volumes     

> __< a​rticmine:monero.social >__ So we have to make the daemon inefficiency part of a HF for larger ring size     

> __< selsta >__ rucknium: we need devs to find a way to reproduce the issue in a local test setting and then work on a fix     

> __< jberman >__ I think selsta's assessment is fair there also. We need hands to focus on improving daemon inefficiencies     

> __< r​ucknium:monero.social >__ spackle wanted to run a benchtest network. Maybe he could help organize something.     

> __< selsta >__ the problem is that some bugs require a large amount of connections to reproduce which makes it more difficult in a local network     

> __< r​ucknium:monero.social >__ I would be willing to help, too.     

> __< a​rticmine:monero.social >__ As far as the scaling design a ring 64 or 60 can be accommodated with a 4x increase in fees.     

> __< a​rticmine:monero.social >__ The fee increase can be optionally reversed with FCMP     

> __< selsta >__ c​haser: many-input tx can trigger this out of memory issue, yes     

> __< r​ucknium:monero.social >__ Would setting up a testnet with many cheap VPSes be a good way to start testing?     

> __< a​rticmine:monero.social >__ We would use a 400000 / 800000 byte reference transaction weight. Depending on the fees     

> __< c​haser:monero.social >__ selsta: I see. do you also imply there are also other things that can trigger it?     

> __< selsta >__ it might make more sense to edit the source code in a way that simulates a lot of connections, instead of setting up a lot of VPS     

> __< rbrunner >__ Sounds like a good idea     

> __< spackle >__ For what it is worth, I ran a private testnet on a single machine and loaded the mempool with transactions (over 500MB). I did not see any unusually large memory or cpu burden in that circumstance.     

> __< selsta >__ this is the github issue for the out of memory issue: https://github.com/monero-project/monero/issues/9317     

> __< jberman >__ I would probably start by spinning up many local testnet daemons and stress testing, instead of going VPS route first     

> __< a​rticmine:monero.social >__ I can proceed with the scaling design to accommodate both up to ring 64 and a future FCMP     

> __< selsta >__ the current theory is that the fluff queue is making a copy of each transaction for each network peer, which can cause a memory spike if a lot of large transactions are submitted at once     

> __< jberman >__ I think it's a reasonable theory that should be reproducible     

> __< r​ucknium:monero.social >__ In my statistical analysis on tx verification performance, it seemed that verifying one byte of input data took 150% longer than verifying one byte of output data. In other words, if an adversary wanted to get the maximum CPU usage for their XMR budget, they would create lots of inputs.     

> __< rbrunner >__ It says something about the complexity of the code if such a theory stays a theory for some longer time :)     

> __< r​ucknium:monero.social >__ I don't know if my tentative statistical results comparing input and output verification time (not explicitly in the paper) are consistent with what's supposed to be happening with the cryptography in theory.     

> __< a​rticmine:monero.social >__ One question regarding daemon effectively. Can we minimize the number of times the tx proofs are transmitted. So only once between tx relay and block relay?     

> __< jberman >__ yes: https://github.com/monero-project/monero/issues/9334     

> __< r​ucknium:monero.social >__ If the bottleneck is tx propagation to so many nodes, then boog900 's proposal may help a lot: "Change how transactions are broadcasted to significantly reduce P2P bandwidth usage" https://github.com/monero-project/monero/issues/9334     

> __< selsta >__ the other bug is that nodes can fall behind, most of the times it happens during RPC traffic. it's less critical but still annoying for users that rely on remote nodes.     

> __< selsta >__ in my opinion both of these bugs would be critical to fix before we can increase the ring size significantly     

> __< a​rticmine:monero.social >__ So if I understand correctly the same approach can be used for mined blocks     

> __< rbrunner >__ And well, it's possible that much larger rings would trigger problems that we are not yet aware at all     

> __< c​haser:monero.social >__ so my understanding is the memory issue seems to be regardless of whether the transaction is large because of inputs of outputs. is that right?     

> __< r​ucknium:monero.social >__ Ok. Let's make a task force or something. spackle could lead. selsta can answer questions. 0xfffc  could help with database things. Maybe boog900 , rbrunner7 , and vtnerd  could be involved.     

> __< v​tnerd:monero.social >__ That proposal will probably have minimal effects on tx propagation time, unless some of the timers are removed     

> __< 0​xfffc:monero.social >__ I am onboard.     

> __< jberman >__ the rw lock was the stab at the solution to nodes falling behind, wondering how that's going / if that issue was reproduced: https://github.com/monero-project/monero/pull/9181     

> __< selsta >__ jberman: problem is that we are not able to reproduce the issue locally     

> __< selsta >__ so unclear if the rw lock helps     

> __< 0​xfffc:monero.social >__ It is overall in good shape, though there is a bug that sgp reported. Causing speed up 20% initially, but after a while causing slowdown 20%. But during my work on it I realize need a performance benchmark suite.     

> __< 0​xfffc:monero.social >__ Exactly as selsta explained it.     

> __< jberman >__ got it     

> __< 0​xfffc:monero.social >__ Performance benchmark suite will basically a best solution. Spin up multiple node private testnet, then run your scenario. And evaluate the results.     

> __< 0​xfffc:monero.social >__ If we had that performance suite, rw-lock fix would be trivial and much simpler work.     

> __< 0​xfffc:monero.social >__ I took stab at the performance suite. (Will send the link) but had to go for a leave for personal reasons.     

> __< 0​xfffc:monero.social >__ Reporting to community: I have NOT abandoned the work, not I forgot. I just had to fix a few personal issues. Hopefully will be working full time on it from Sunday June 2nd.     

> __< r​ucknium:monero.social >__ Thanks, 0xfffc . Do you want to try to organize some things together to get a benchmark testnet running?     

> __< spackle >__ I am happy to do what I can, though I will openly admit that I lack the expertise of selsta/others. My thought was to run a testnet fork specifically for abuse, but if selsta can simulate many connections that may be the direct route.     

> __< 0​xfffc:monero.social >__ P.S.      

> __< 0​xfffc:monero.social >__ https://github.com/0xFFFC0000/benchmark-project/blob/main/benchmark_project.cpp     

> __< 0​xfffc:monero.social >__ This basically manages daemon as separate processes. Eventually we want to run nodes as different daemon objects via C++ code (instead of spin up different processes)     

> __< rbrunner >__ Sounds quite ambitious. And may have different performance characteristics, worst case.     

> __< 0​xfffc:monero.social >__ If anyone wants to work together, I am 100% onboard. Just to make sure, I might not be able to code myself until June 2nd. (After that I will write code myself too).      

> __< 0​xfffc:monero.social >__ But available to talk and share my view 24/7 on matrix until then.     

> __< 0​xfffc:monero.social >__ ( code is extremely ugly. It is just a draft )     

> __< r​ucknium:monero.social >__ rbrunner: That is my question about "simulating connections". How do we know we are not catching the bottlenecks if we do not have as realistic a test environment as possible?     

> __< spackle >__ I can restart/publish the testnet fork I made if that is helpful. Not that forking testnet is difficult, but I do have it ready.     

> __< 0​xfffc:monero.social >__ ( i took the idea from a professor paper from Imperial College London. They wrote a simulation for Bitcoin. Running different Bitcoin nodes on NS2 -network simulator- then evaluating. Will send the link to their paper here in few moments. )     

> __< r​ucknium:monero.social >__ I will put this benchmark testnet idea on next week's MRL agenda to encourage progress :)     

> __< rbrunner >__ Rucknium: Fair enough. But at least, with the right "trick", simulating many connections should be quite easy, unlike turning the Monero daemon into a proper C++ class that you can instantiate at will     

> __< rbrunner >__ Probably ...     

> __< r​ucknium:monero.social >__ Any other comments about monerod performance and black marble flood defense?     

> __< c​haser:monero.social >__ tevador has an anti-spam proposal to modify the clawback such that weight-per-outputs is constant for all output counts when in=1. (https://github.com/monero-project/research-lab/issues/119#issuecomment-2131169865). it makes one of the simplifications in Rucknium's paper more realistic, and I wonder what everyone thinks of it.     

> __< 0​xfffc:monero.social >__ I agree. For the time being we can simulate this without going into the whole simulation hassle. But honestly I am not much familiar with the connection side. But next week I can help.     

> __< a​rticmine:monero.social >__ The clawback is currently at 80%     

> __< r​ucknium:monero.social >__ IMHO, we could add the modified clawback to a hardfork with larger ring size. Probably it doesn't affect most users since most users never send a tx with more than 2 outputs. Some wallets don't even have the capability to send more than 2 output txs.     

> __< a​rticmine:monero.social >__ I don't see much room there     

> __< a​rticmine:monero.social >__ An option for large number of outputs is to require a higher minimum node relay fee     

> __< r​ucknium:monero.social >__ Yes, it probably won't have a large impact. And the suspected March 2024 flooder used 2-out txs anyway, so apparently the incentive to make 16-out txs wasn't very large for them.     

> __< a​rticmine:monero.social >__ For those outputs     

> __< c​haser:monero.social >__ I agree, but the sentiment seems to be that monerod bottlenecks may make a larger ring size fork nonviable.     

> __< c​haser:monero.social >__ that doesn't mean there won't be another actor who realizes this advantage     

> __< spackle >__ I was thinking a stressnet could be added to the permanent codebase as a limited yearly network. Runs for a few months each year, starting with a unqiue pre-programmed initialization each time and rejecting blocks after a certain height.     

> __< r​ucknium:monero.social >__ Unless I am missing something, the monerod bottlenecks + ring size increase only matters for "normal" non-spam tx volume. an adversary can spam to try to knock nodes offline by just creating more txs at current ring size instead of fewer txs with larger rings.     

> __< r​ucknium:monero.social >__ We may have some FCMP updates     

> __< r​ucknium:monero.social >__ 4) Research Pre-Seraphis Full-Chain Membership Proofs https://www.getmonero.org/2024/04/27/fcmps.html     

> __< c​haser:monero.social >__ oh, I see     

> __< r​ucknium:monero.social >__ Anything to discuss about FCMP at this meeting?     

> __< jberman >__ the Veridise statement of work is signed and they are onboarded     

> __< r​ucknium:monero.social >__ Excellent     

> __< r​ucknium:monero.social >__ Any other business?     

> __< c​haser:monero.social >__ I have a question about your paper: your largest ring size option (60) won out in all budget scenarios. is this a tendency that could extend beyond 60 with your current model?     

> __< r​ucknium:monero.social >__ chaser: I didn't test it explicitly, but if we raise the upper constraint, I expect that an even larger ring size would be most cost-effective. The 60 upper limit was set based on some conversations here a while ago.     

> __< c​haser:monero.social >__ got it, thanks     

> __< c​haser:monero.social >__ also, a question to Artic: what did you mean that "I don't see much room there" (w.r.t. the clawback)?     

> __< a​rticmine:monero.social >__ One question I have regarding the ring size proposal is would. 64. be optimal from the perspective of OSPEAD and binning since it is 4x the current Ring size?     

> __< a​rticmine:monero.social >__ It is currently at 80% of the size gain over 2/2 tx per output     

> __< r​ucknium:monero.social >__ With binning we would probably want a number that is easily divisible. At this time I don't know if we are considering binning at the same time as a hypothetical pre-FCMP hard fork. For OSPEAD, there is not specific threshold or divisibility that is better, except larger is better.     

> __< a​rticmine:monero.social >__ So there isn't much more we can claw back     

> __< r​ucknium:monero.social >__ chaser: I just re-ran it with the limit to ring size 200. The optimum still goes to the maximum, 200. The way to produce results in the model more in favor of a fee increase is to increase the `m` multiplier in the model that affects the cost of node operators. Right now it is times two the estimated storage cost for the network.     

> __< a​rticmine:monero.social >__ I was considering 64 for ease of transition from 16     

> __< a​rticmine:monero.social >__ For ring size     

> __< c​haser:monero.social >__ I see. I don't think though that tevador's proposal necessarily needs to be construed as the clawback. you can also think of it as an additional penalty term.     

> __< c​haser:monero.social >__ Rucknium thanks for checking it! good to know.     

> __< c​haser:monero.social >__ 60/64 already sounds quite large though, but good to know     

> __< rbrunner >__ Would this get us into FCMP tx size territory, more or less?     

> __< r​ucknium:monero.social >__ With ring size 200, the time to verify a block's worth of txs during normal tx volume is about 6 seconds. That starts to become a problem. Anyway, I think most people think ring size 200 is too higher, except for gingeropolous ;P     

> __< r​ucknium:monero.social >__ too high*     

> __< c​haser:monero.social >__ rbrunner: definitely     

> __< r​ucknium:monero.social >__ IIRC, the latest estimated from kayabanerve  say that a FCMP-sized tx would be about ring size 40     

> __< c​haser:monero.social >__ n=60 2/2 is ~5300 B     

> __< c​haser:monero.social >__ I recall 5500 B from Kayaba for 2/2 FCMP++     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< a​rticmine:monero.social >__ My understanding for FCMP 2/2 was around 3099 bytes     

> __< a​rticmine:monero.social >__ 3000 bytes     

> __< a​rticmine:monero.social >__ This is the latest I heard     

> __< c​haser:monero.social >__ huh. I think I remembered this, is this outdated? https://libera.monerologs.net/monero-research-lab/20240402#c357039     

> __< a​rticmine:monero.social >__ Yes     

> __< spackle >__ The scaling algorithm massively expands the potential of the verification time issue. ArticMine: do I recall correctly that you were considering setting the surge factor to 16?     

> __< a​rticmine:monero.social >__ Yes     

> __< a​rticmine:monero.social >__ The verification time issue needs parallel processing     

> __< a​rticmine:monero.social >__ That is the only long term solution since CPU speed is not where the gains are. The gains are in number of cores     

> __< k​ayabanerve:monero.social >__ Apologies for not being present. I wrote more code regarding FCMP++s, demoed the TX modifications, and we're following up with Veridise as necessary.     

> __< k​ayabanerve:monero.social >__ 2 inputs is only a few hundred bytes larger than 1 input.   

# Action History
- Created by: Rucknium | 2024-05-28T20:33:53+00:00
- Closed at: 2024-06-05T22:50:28+00:00
