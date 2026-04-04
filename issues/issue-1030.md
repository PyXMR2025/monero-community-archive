---
title: Monero Research Lab Meeting - Wed 26 June 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1030
author: Rucknium
assignees: []
labels: []
created_at: '2024-06-25T22:57:45+00:00'
updated_at: '2024-07-05T20:26:16+00:00'
type: issue
status: closed
closed_at: '2024-07-05T20:26:16+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Stress testing `monerod`](https://github.com/monero-project/monero/issues/9348)

4. [Potential measures against a black marble attack](https://github.com/monero-project/research-lab/issues/119).

5. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html).

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1025 

# Discussion History
## Rucknium | 2024-07-02T21:06:09+00:00
Logs:


> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1030     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< a​aron:cypherstack.com >__ Hello     

> __< spackle >__ hello     

> __< rbrunner >__ Hello     

> __< narodnik >__ hi     

> __< h​into:monero.social >__ hi     

> __< c​haser:monero.social >__ hello     

> __< k​ayabanerve:monero.social >__ 👋     

> __< vtnerd >__ hi     

> __< jberman >__ *waves*     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Helping with stressnet. And I have the visualization of the two new solution concepts for best fee and ring size for defense against black marble attacks.     

> __< spackle >__ me: misc. stressnet tasks     

> __< vtnerd >__ a number of bug fixes to LWS and ZMQ. Re-started "frontend" lib work for LWS (after hearing the wallet2 update)     

> __< jberman >__ me: fcmp grow_tree and trim_tree algorithms     

> __< 0​xfffc:monero.social >__ Hi     

> __< k​ayabanerve:monero.social >__ Soliciting quotes to review the divisor proof, one already acquired. Both should be here by Monday. We're also trying to move forward with the divisor R1CS specification.     

> __< k​ayabanerve:monero.social >__ *specification review.     

> __< narodnik >__ kayaba, if you need auditor intros/recommendations, i can help with that     

> __< r​ucknium:monero.social >__ 3) Stress testing `monerod` https://github.com/monero-project/monero/issues/9348     

> __< spackle >__ The main thing to share is that we experienced serious issues with larger blocks. Consistent ~1.5MB blocks required lowering '--block-sync-size' for block propagation and network synchronization to function.     

> __< spackle >__ Each miner was isolated to separate chains and other nodes could not sync until the change was made.     

> __< r​ucknium:monero.social >__ spackle, do you want to discuss stressnet?     

> __< d​iego:cypherstack.com >__ Hi     

> __< spackle >__ That is the brief overview. Rucknium performed an investigation on the limits of the current software, and I imagine they would like to speak on it: https://gist.github.com/Rucknium/f092b0ad5870f6038226c39af529152c     

> __< r​ucknium:monero.social >__ Right. By default, monerod has `--block-sync-size` set to 20 for recent (last several years) blocks on mainnet. A chunk of 20 blocks was too much once block size reached 1.5MB.     

> __< r​ucknium:monero.social >__ I lowered it one unit at a time. I was able to sync once I set it to 14. Roughly, I think that monerod can sync block chunks when they are 20-25MB and lower.     

> __< r​ucknium:monero.social >__ If this happened on mainnet, probably there would be a netsplit and chainsplit until a lot of the network restarted their nodes with a lower `--block-sync-size`     

> __< rbrunner >__ And it seems the daemon isn't "aware" that there is a problem, does not error out, does not warn, just does not progress anymore?     

> __< r​ucknium:monero.social >__ It just says "Sync data returned a new top block candidate: 2521517 -> 2524276 [Your node is 2759 blocks (3.8 days) behind]" again and again. And then starts banning peers.     

> __< rbrunner >__ Splendid :)     

> __< c​haser:monero.social >__ do we know if this limitation is imposed by the amount of data or the amount of computation? similar behavior was observed with ~300 kB mainnet blocks with 150-in/few-out transactions.     

> __< r​ucknium:monero.social >__ I didn't try to turn on deeper log levels. The problem is reliably reproducible on stressnet if you pop blocks down to before the block size "hill". Developers can turn on the appropriate log levels and categories     

> __< jberman >__ log-level 2 would yield useful info here, and obviously would be nice to have someone focus on this asap     

> __< r​ucknium:monero.social >__ In the newest release on stressnet, I just set the value to `1` to make sure it syncs ok: https://github.com/spackle-xmr/monero/pull/8     

> __< r​ucknium:monero.social >__ You can see where in the code the defaults are controlled. It is sort of a very basic control based on hard-coded block heights.     

> __< rbrunner >__ Thankfully it would be quite expensive to push blocksize up to that "hill" on mainnet     

> __< c​haser:monero.social >__ (and on mainnet, `--block-sync-size  1` also got rid of the problem)     

> __< r​ucknium:monero.social >__ spackle, do you have an estimate on how much in fees it would take with the minimum fee (20 nanoneros/byte)?     

> __< spackle >__ Certainly expensive to do quickly.     

> __< spackle >__ Not on hand, one moment...     

> __< jberman >__ what are this machine's specs?     

> __< r​ucknium:monero.social >__ I pushed up block size to 1.5MB quickly by spamming priority 4 (highest) fees on stressnet.     

> __< r​ucknium:monero.social >__ Here's a plot of the block sizes during the stress testing: https://github.com/spackle-xmr/chaindata_graphics/blob/main/stressnet_block_size_26_JUN.png     

> __< r​ucknium:monero.social >__ And here is spackle's one-week report: https://reddit.com/r/Monero/comments/1doyde9/stressnet_first_week_report/     

> __< rbrunner >__ I don't quite understand the axes on that plot ...     

> __< r​ucknium:monero.social >__ jberman: The machine that I used for the testing here https://gist.github.com/Rucknium/f092b0ad5870f6038226c39af529152c ?     

> __< jberman >__ yes     

> __< r​ucknium:monero.social >__ It's one of the Monero Research Computing Cluster's machines: 3900x 24 thread, 32GB ram, 1TB nvme.     

> __< r​ucknium:monero.social >__ It only had outgoing connections.     

> __< jberman >__ got it     

> __< spackle >__ A quick simulation shows min fees would expand the block size to 1.66MB in 8500 blocks at a cost of ~107 XMR.     

> __< spackle >__ *after 8500 blocks     

> __< r​ucknium:monero.social >__ rbrunner: AFAIK, the vertical is number of bytes in a block and the horizontal is just number of blocks since the stressnet testing started last Wednesday.     

> __< rbrunner >__ Ok, thanks     

> __< r​ucknium:monero.social >__ spackle: Thanks a ton for all your work on that simulation code that can give us an answer so quickly :)     

> __< spackle >__ I'll be the first to say it is not perfect, but I do think it paints a generally accurate picture.     

> __< rbrunner >__ So in less than 2 weeks and for less than USD 20'000 you can aspire and try to bring the Monero network to partial standstill.     

> __< r​ucknium:monero.social >__ That's about 12 days. I think what we are doing on stressnet now is just spamming minimum fees and seeing the growth rate of the blocks.     

> __< rbrunner >__ Pretty sobbering.     

> __< r​ucknium:monero.social >__ Here my webapp that shows live stressnet data: https://monitor.stressnet.net/     

> __< r​ucknium:monero.social >__ rbrunner: I agree. Stressnet has shown the issue. Now software engineers can decide what to do about it :)     

> __< r​ucknium:monero.social >__ You could have a quick fix by lowering the default values or look into what causes the problem deeper.     

> __< rbrunner >__ It may well be that the correction will be quite easy, once the problem is on the table.     

> __< r​ucknium:monero.social >__ Some other things: Node startup with a large txpool (600MB) takes about an hour. 0xfffc wrote a patch that decreased the time by 2-5x. Thank you! Still, that's slow, and it can be worked on more AFAIK. Node<->wallet connects are hard to establish when the txpool is very large, too.     

> __< r​ucknium:monero.social >__ Anything else about stressnet? Stressnet conversation happens in #monero-stressnet:monero.social  and ##monero-stressnet on IRC     

> __< p​reland:monero.social >__ Cmon guys let’s reach 1m pending in mem_pool 🔥     

> __< p​reland:monero.social >__ (Btw gigabytes and bytes look the same on the monitor)     

> __< jberman >__ if another dev isn't on this by next week's MRL meeting, I'll shift priority from fcmp's to this barring objection     

> __< 0​xfffc:monero.social >__ Parallelization of startup txpool load, is indirectly related to rwlock. So I went back to rwlock work.      

> __< 0​xfffc:monero.social >__ If we merge rwlock, we can write  parallelization of txpool load.  Which would even speed it up substantially     

> __< r​ucknium:monero.social >__ preland: The default txpool size is about 600MB. That gets about 250,000 txs. We can't get higher without increasing the default (can be changed with a flag at startup)     

> __< h​into:monero.social >__ 0xfffc: what causes txpool loading to take that long? curious on the details     

> __< r​ucknium:monero.social >__ preland: Thanks for input. The monitor is a rough draft. I haven't done anything with the units yet. B = "billion".     

> __< 0​xfffc:monero.social >__ we are validating every txis.     

> __< h​into:monero.social >__ and it is done sequentially?     

> __< r​ucknium:monero.social >__ AFAIK, single-threaded 😎  (the sunglasses are ironic)     

> __< r​ucknium:monero.social >__ The CPU load is on one thread at startup     

> __< r​ucknium:monero.social >__ You could probably do batch verification, too, AFAIK     

> __< r​ucknium:monero.social >__ The startup time is inconvenient, but it's potentially a bigger problem if nodes shut down during high tx volumes, then they need a long time to restart.     

> __< r​ucknium:monero.social >__ The stressnet node release is running 0xfffc 's patch already     

> __< r​ucknium:monero.social >__ We had about 40 nodes on stressnet at the start. Maybe 25-30 now.     

> __< r​ucknium:monero.social >__ 4) Potential measures against a black marble attack. https://github.com/monero-project/research-lab/issues/119     

> __< 0​xfffc:monero.social >__ yes, of course.     

> __< 0​xfffc:monero.social >__ https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/cryptonote_core/tx_pool.cpp#L1793     

> __< r​ucknium:monero.social >__ I updated https://black-marble-defense-params.redteam.cash/ with visualizations for the two new solution concepts. The first is the best fee and ring size at a specific effective ring size. The second is the best fee and ring size at a specific "budget" for Alice, i.e. the total cost of aggregate tx fees plus the cost of storage to node operators.     

> __< r​ucknium:monero.social >__ I think sgp_  was interested in this.     

> __< r​ucknium:monero.social >__ These solution concepts align with the expectation that as node storage costs are higher (i.e. adjust the `m` parameter up), it is more attractive to defeat black marbles by raiding the fee instead of raising the ring size.     

> __< r​ucknium:monero.social >__ We don't have much time in the usual hour, so we can move to FCMP     

> __< r​ucknium:monero.social >__ 5) Research Pre-Seraphis Full-Chain Membership Proofs. https://www.getmonero.org/2024/04/27/fcmps.html     

> __< r​ucknium:monero.social >__ kayabanerve: ^     

> __< k​ayabanerve:monero.social >__ 👋     

> __< k​ayabanerve:monero.social >__ Aaron also has news beyond my own.     

> __< a​aron:cypherstack.com >__ Cypher Stack has complete its FCMP++ report and provided a draft to kayabanerve     

> __< a​aron:cypherstack.com >__ Cypher Stack has completed its FCMP++ report and provided a draft to kayabanerve     

> __< r​ucknium:monero.social >__ Great!     

> __< k​ayabanerve:monero.social >__ I only saw after the meeting started, hence my lack of announcement in intro, apologies there.     

> __< a​aron:cypherstack.com >__ Once any issues are addressed and inevitable typos fixed, we'll get it posted to GitHub (along with TeX source)     

> __< k​ayabanerve:monero.social >__ Delivered this morning though :)     

> __< jberman >__ good news :)     

> __< a​aron:cypherstack.com >__ The gist is that the technique should be suitable for its intended use case, given some conditions on how proving systems are instantiated     

> __< a​aron:cypherstack.com >__ We also proved an optimization secure     

> __< k​ayabanerve:monero.social >__ I'm still reading through, so I apologize I can't immediately provide my own summary.     

> __< rbrunner >__ Almost suspicious how clear the FCMP sailing has been so far :)     

> __< k​ayabanerve:monero.social >__ My notation has been thoroughly critiqued.     

> __< k​ayabanerve:monero.social >__ Yet we now have GBP proofs (which I'm soliciting review for), divisor proofs (also soliciting review for), and the composition proofs (I say as I read through the document supposedly with them).     

> __< k​ayabanerve:monero.social >__ Once we get the necessary secondary reviews for GBPs/divisors, we should be able to move forward with audits on each.     

> __< k​ayabanerve:monero.social >__ And with the divisor R1CS spec being reviewed, we can then request Veridise to do formal verification of the rest of our spec or do it ourselves before moving to auditing there.     

> __< k​ayabanerve:monero.social >__ I don't have much more to say on this end. jberman may on the integration side?     

> __< jberman >__ hoping to have a documented spec of the grow_tree and trim_tree implementations within the next 2 weeks. haven't been particularly simple to implement     

> __< k​ayabanerve:monero.social >__ Mind if I ping you on your thoughts about the rust ffi side of things 👀 Been fine, been a leading cause of issues...?     

> __< s​gp_:monero.social >__ cool stuff! Thanks for adding that dot to the graph     

> __< jberman >__ hah course. ffi stuff has been mostly fine, it's more capturing the edge cases on the algo side unrelated to the ffi     

> __< k​ayabanerve:monero.social >__ I want it on the record Rust is mostly fine :p     

> __< r​ucknium:monero.social >__ sgp_: If you sweep the two lines through the plot area, you get similar optima because they are both downward-sloping lines. The main difference between the two solutions is the effective ring size line is more convex (higher second derivative) than the budget line.     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< a​aron:cypherstack.com >__ Excited to share the FCMP++ report once it's reviewed :D     

> __< e​msczkp:matrix.org >__ Hi everyone, sorry I'm late (chat and logs is not working). Few updates on my side: i worked on multi-exp, compressed sigma IPA provides effectively the multi-exp now. I'll test on the kayabaNerve fcmp github repo my solution, also with batching, and compare it. I'll keep you updated ...     

> __< e​msczkp:matrix.org >__ I haven't asked for funds yet. We could discuss it when I see improvements in verification times of 5-10% (as kayabanerve said), right ?     

> __< r​ucknium:monero.social >__ https://libera.monerologs.net/ is giving 504 error for me     

> __< k​ayabanerve:matrix.org >__ I'd be interested in moving forward with it if it benefited performance 5-10%. That'd be non-trivial, and due to it being a drop-in replacement (not redoing all the GBP work), it'd potentially be feasible to review within our time span. I'd have to see that time for myself to ask the community thought's on the effort, and then we'd be discussing paying for review of the proof to e<clipped message     

> __< k​ayabanerve:matrix.org >__ nsure its security holds.     

> __< k​ayabanerve:matrix.org >__ I don't want to trouble you with the dev work on your end, if it is something you're unfamiliar with. I'm truly happy to take the responsibility there :) I just have to sit down and do it 😅     

> __< a​aron:cypherstack.com >__ You mean this is a drop-in replacement of the BP IPA?     

> __< a​aron:cypherstack.com >__ And therefore could be reviewed independently?     

> __< k​ayabanerve:matrix.org >__ Yep, which I wrote as a dedicated proof already. Should be feasible within just 100 lines or so.     

> __< k​ayabanerve:matrix.org >__ Yep, GBPs would remain.     

> __< k​ayabanerve:matrix.org >__ *I impl'd as a dedicated proof already     

> __< k​ayabanerve:matrix.org >__ I believe it already has security proofs for the same properties as the BP IPA, emsczkp obviously the better person to confirm with.     

> __< a​aron:cypherstack.com >__ I would certainly be interested in conducting such a review :D     

> __< p​reland:monero.social >__ Yeah I understood that—though it did make me scratch my head for a second when the total blockchain size was 10.3 bytes     

> __< k​ayabanerve:matrix.org >__ So we'd be doing proof review _if_ the performance justifies it as more than a point of interest not worth the political capital and effort on.     

> __< k​ayabanerve:matrix.org >__ (not to be rude to the theory. I actually quite like a design done without the inversions. I just already have had "scope creep" discussions and a distinct IPA is right on that fence :p )     

> __< k​ayabanerve:matrix.org >__ But yeah, 5-10% off the FCMP++ verification would be non-negligble and very worth discussng.     

> __< a​aron:cypherstack.com >__ The security proof given for that protocol is not nearly as detailed as the original BP IPA     

> __< e​msczkp:matrix.org >__ thanks kayabaNerve. Yes the security proofs are there and I have also extended them,  I would be happy if anyone wants to discuss it. I would like to personally test the solution on fcmp, also to avoid committing your effort before being 5-10% verif sure     

> __< a​aron:cypherstack.com >__ Oh, you expanded on the proofs to provide better detail?     

> __< e​msczkp:matrix.org >__ Yes!     

> __< a​aron:cypherstack.com >__ Nice     

> __< a​aron:cypherstack.com >__ Are you one of the original authors as well?     

> __< a​aron:cypherstack.com >__ (if you care to say)     

> __< a​aron:cypherstack.com >__ I'd be interested to see the updated proofs, for sure     

> __< e​msczkp:matrix.org >__ I'm the author     

> __< a​aron:cypherstack.com >__ Apologies if this was discussed earlier, but is there a reason why you'd expect to see practical efficiency benefits, given that inversions are batched?     

> __< k​ayabanerve:matrix.org >__ It mainly has benefits for the prover who has reduced MSMs while proving.     

> __< a​aron:cypherstack.com >__ Ah, I see     

> __< a​aron:cypherstack.com >__ I was only considering the verifier     

> __< k​ayabanerve:matrix.org >__ For the verifier, it removes... 24 inversions at our scale?     

> __< a​aron:cypherstack.com >__ If you're batching, you only have one actual inversion     

> __< k​ayabanerve:matrix.org >__ Sure, yet that's still 256 scalar muls knocked out.     

> __< a​aron:cypherstack.com >__ (although you do more muls)     

> __< a​aron:cypherstack.com >__ So the 5-10% informal target was for proving, ya?     

> __< a​aron:cypherstack.com >__ Not verifying?     

> __< e​msczkp:matrix.org >__ the multi-exp on verfier should save several MSMs too     

> __< a​aron:cypherstack.com >__ Even when combining challenges to a single MSM?     

> __< e​msczkp:matrix.org >__ my target would be the verifier, but the prover should also benefit if I'm not mistaken     

> __< e​msczkp:matrix.org >__ Yess I see many msm saved     

> __< a​aron:cypherstack.com >__ I'm thinking in terms of Equation 105 in the BP preprint (page 29)     

> __< a​aron:cypherstack.com >__ Where would the savings come from in that case?     

> __< e​msczkp:matrix.org >__ this in multi-exp but I want to see batching too, I will work on this in the next few days     

> __< a​aron:cypherstack.com >__ Just from the `L`- and `R`-type terms?     

> __< a​aron:cypherstack.com >__ Surely you wouldn't get anything from the generators if you're doing generating combining?     

> __< a​aron:cypherstack.com >__ *challenge combining     

> __< a​aron:cypherstack.com >__ I think the most helpful thing for investigating verifier performance would be something akin to Equation 105     

> __< a​aron:cypherstack.com >__ (of course, it would be for the AC protocol)     

> __< e​msczkp:matrix.org >__ I should calculate the challenges more lightly, this from multiexp if I remember equation 105     

> __< k​ayabanerve:monero.social >__ My target was the verifier. I'll also bench prover yet I'd need much higher prover perf to justify that. Most of our proving time isn't IPA dominated AFAIK yet the divisor Poly's.     

> __< k​ayabanerve:monero.social >__ The verifier saving MSMs is notational, not practical.     

> __< k​ayabanerve:monero.social >__ I'd be surprised by 5-10% verifier perf increase. I wouldn't be surprised by that much on the prover. I'd want the prover to be 20+% though.     

> __< k​ayabanerve:monero.social >__ (And again, that may due 50% off the IP A, but I can only care about the entire FCMP++ membership proof) 

# Action History
- Created by: Rucknium | 2024-06-25T22:57:45+00:00
- Closed at: 2024-07-05T20:26:16+00:00
