---
title: Monero Research Lab Meeting - Wed 08 May 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1003
author: Rucknium
assignees: []
labels: []
created_at: '2024-05-07T20:41:26+00:00'
updated_at: '2024-05-15T19:38:44+00:00'
type: issue
status: closed
closed_at: '2024-05-15T19:38:44+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Potential measures against a black marble attack](https://github.com/monero-project/research-lab/issues/119).

4. [Generalized Bulletproofs Security Proofs](https://github.com/cypherstack/generalized-bulletproofs/releases/tag/final)

5. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html). 

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#999 

# Discussion History
## Rucknium | 2024-05-09T16:46:00+00:00
Logs:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1003     

> __< c​haser:monero.social >__ hello     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< a​aron:cypherstack.com >__ Hello!     

> __< jberman >__ *waves*     

> __< tevador >__ Hi     

> __< o​ne-horse-wagon:monero.social >__ Hello.     

> __< v​tnerd:monero.social >__ Hi     

> __< 0​xfffc:monero.social >__ hi everyone     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< tevador >__ FCMP related work. I did an analysis of Ristretto and we had some discussions with kayabaNerve how to simplify the tree hashing.     

> __< jberman >__ me: started FCMP integration (initial task is working on the tree in C++ = table design, code flow, and tests). The async scanner PR (faster scanning) was also merged into ukoe's Seraphis lib, going to start making bite-sized PR's to monero core over the next week in preparation. Also opened a new CCS     

> __< r​ucknium:monero.social >__ me: Working on the fee/ring size tradeoff to deter or defeat black marble flooding. And started working on using the Dulmage-Mendelsohn decomposition to analyze black marble flooding combined with "chain reaction analysis" from Section 4 "Chain reaction graph attacks" of https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-flood.pdf     

> __< v​tnerd:monero.social >__ Me: Lws-remote-scanning *still*. Expect to be finished this week, unless I hit another snag     

> __< k​ayabanerve:monero.social >__ As I said in NWLB, I worked extensively on FCMPs. The spec has been iterated with feedback, the GGBP updates made, and two auditors plan to submit SoW within two weeks. I meet a third today and have also distinctly discussed work with CS.     

> __< 0​xfffc:monero.social >__ Me: Wasted a lot of time last week. I am submitting minor PRs here and there. But overall my main task is performance benchmarking suite and then fixing the locking bottleneck we have.     

> __< r​ucknium:monero.social >__ 3) Potential measures against a black marble attack https://github.com/monero-project/research-lab/issues/119     

> __< r​ucknium:monero.social >__ For the fee/ring size tradeoff, I am computing these metrics for the most cost-effective fee/ringsize response to a specific adversary budget:     

> __< r​ucknium:monero.social >__ Adversary budget, nominal ring size, fee/byte, effective ring size when flooded by adversary's budget, user's cost for 2in/2out tx, user's tx size for 2in/2out tx, average block size (no flooding), Block size (continuous flooding), one year of blockchain growth (each combination of unpruned/pruned and no flooding/continuous flooding).     

> __< r​ucknium:monero.social >__ Any other metrics I should compute?     

> __< tevador >__ tx verification time     

> __< j​effro256:monero.social >__ Howdy     

> __< r​ucknium:monero.social >__ How can we get that? Have a private testnet with a specific modified ring size and do benchmarks?     

> __< c​haser:monero.social >__ Rucknium  I think that's doable without any networking element     

> __< k​ayabanerve:monero.social >__ Sorry, for a brief reminder, what's the ring size 40 verification time?     

> __< tevador >__ CLSAG benchmarks probably can be done without a private testnet     

> __< r​ucknium:monero.social >__ Verification time in practice and in theory may be different.     

> __< tevador >__ I think the seraphis github issue had some benchmarks     

> __< k​ayabanerve:monero.social >__ Yes and no. There's the unchanging verification time, and then the prep time.     

> __< r​ucknium:monero.social >__ If we just want to do theoretical verification time, I am ok with that, too. There is time to read the data from storage, too.     

> __< k​ayabanerve:monero.social >__ It's probably best to simulate the prep time off the mainnet DB?     

> __< tevador >__ https://github.com/monero-project/research-lab/issues/91     

> __< k​ayabanerve:monero.social >__ (So no actual testnet, just a DB)     

> __< c​haser:monero.social >__ tevador: that's quite a killer reference hardware koe used there     

> __< r​ucknium:monero.social >__ Tell a monero wallet to construct a K ring member tx from the mainnet database and then verify it? Ok. But probably it is better for someone else to code that since that's definitely not my comparative advantage.     

> __< r​ucknium:monero.social >__ IMHO the March suspected spam showed that monerod has hidden bottlenecks, so actual performance can be different from theoretical.     

> __< k​ayabanerve:monero.social >__ Grootle is 17ms no batching for 128. CLSAG is 24ms for 40?     

> __< tevador >__ https://github.com/monero-project/monero/blob/master/tests/performance_tests/sig_clsag.h     

> __< r​ucknium:monero.social >__ Ok. I will use koe's CLSAG benchmarks for now. If a C++ programmer wants to run more realistic benchmarks, that would be wonderful.     

> __< r​ucknium:monero.social >__ I started testing with a Rust implementation of the Dulmage-Mendelsohn decomposition released with this paper: Vijayakumaran (2023) "Analysis of Cryptonote transaction graphs using the Dulmage-Mendelsohn decomposition." https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=39     

> __< r​ucknium:monero.social >__ I am having some problems with the tests, but I don't know if it is a problem with the data I am submitting to the algorithm or if the algorithm is just slow (it is single-threaded for now).     

> __< r​ucknium:monero.social >__ That's all I have on this agenda item. Anything else on this item?     

> __< c​haser:monero.social >__ kayabanerve the benchmarks in koes's Seraphis paper are very close to 24 ms for a no-batch CLSAG 40     

> __< c​haser:monero.social >__ https://raw.githubusercontent.com/UkoeHB/Seraphis/master/seraphis/Seraphis-0-0-18.pdf#page=18     

> __< r​ucknium:monero.social >__ 4) Generalized Bulletproofs Security Proofs https://github.com/cypherstack/generalized-bulletproofs/releases/tag/final  Aaron Feickert     

> __< a​aron:cypherstack.com >__ Yes!     

> __< a​aron:cypherstack.com >__ kayabanerve identified an issue with the generalization in the report     

> __< a​aron:cypherstack.com >__ It had to do with cross-terms in inner products     

> __< a​aron:cypherstack.com >__ A fix was identified that works, but isn't as efficient as we'd hoped with the original idea     

> __< a​aron:cypherstack.com >__ The report has been updated to reflect this; I reissued the tag so existing links point to the right one (but the full git history is there)     

> __< a​aron:cypherstack.com >__ Kudos to kayabanerve for the find     

> __< k​ayabanerve:monero.social >__ Clarifying, the additional functionality isn't as efficient.     

> __< tevador >__ What is the performance impact?     

> __< k​ayabanerve:monero.social >__ The originally expected functionality is maintained for all intents and purposes.     

> __< a​aron:cypherstack.com >__ Right     

> __< k​ayabanerve:monero.social >__ We went from a     

> __< k​ayabanerve:monero.social >__ 2 + 2(c//2) poly     

> __< k​ayabanerve:monero.social >__ To a     

> __< k​ayabanerve:monero.social >__ 2 * (1 + c) poly     

> __< k​ayabanerve:monero.social >__ Yet we can halve the amount of needed c.     

> __< jberman >__ (rucknum : if you want complete end-to-end daemon testing with a larger ring size, then this PR is a good reference for what needs to change on the C++ side for the daemon to allow larger ring sizes if you get someone available to do that https://github.com/monero-project/monero/pull/8178/files)     

> __< k​ayabanerve:monero.social >__ Except for branches which demand a full c to themselves.     

> __< r​ucknium:monero.social >__ j​berman: Thanks. I remembered when you worked on the August 2022 hard fork you said that the ring size 11 -> 16 increase was not as simple as changing a few numbers in the code.     

> __< k​ayabanerve:monero.social >__ We can preserve the original formula without the new features. The new formula and new functionality is overall more efficient.     

> __< tevador >__ So everything is going according to the plan or better.     

> __< k​ayabanerve:monero.social >__ For GGBPs? Yes     

> __< tevador >__ I think we can move on to general FCMP discussion.     

> __< r​ucknium:monero.social >__ 5) Research Pre-Seraphis Full-Chain Membership Proofs. https://www.getmonero.org/2024/04/27/fcmps.html     

> __< tevador >__ An interesting find was that Ristretto doesn't actually help us to remove torsion completely. So we decided to go with the simpler solution of mul8.     

> __< k​ayabanerve:monero.social >__ The spec, gadgets, layers, and circuit are done. There's some cleanup I want to do on the top-level FCMP code and I need to support aggregate input proofs (which is multiple calls to the circuit).     

> __< k​ayabanerve:monero.social >__ Performance is extremely hard to benchmark. I said I could not do a production grade lib and would only do one sufficient for working with.     

> __< tevador >__ Also the membership proof was simplified to proving that (+/-K,+/-I,+/-C) is in the tree. So we ignore the signs. This allows us to remove the complexity of "permissible points".     

> __< r​ucknium:monero.social >__ Possible downside of torsion is that someone can write a Monero tx construction implementation that has a torsioned tx that the consensus verification would consider valid, but it would be fingerprintable, right? Like the strange txs that dangerousfreedom  found?     

> __< tevador >__ A side effect is that people will be able to "spend" -C, so effectively burn funds. But we don't see any issues with that.     

> __< k​ayabanerve:monero.social >__ I had the goal of 35ms in a batch of 10, the prior estimate. We are now clocking as low as 35ms for one and 10ms in a batch of 10. I hope a new Helios/Selene impl would get us ~2x further.     

> __< k​ayabanerve:monero.social >__ Rucknium: FCMPs torsion clears everything.     

> __< r​ucknium:monero.social >__ tevador: is it possible that a mathematics reviewer or a code auditor would see issues with that?     

> __< tevador >__ It should be reviewed during the audit, but I can't imagine what the problem would be.     

> __< k​ayabanerve:monero.social >__ To be clear, that does not preventing outputs with torsion. It just limits the torsion to that and that alone.     

> __< k​ayabanerve:monero.social >__ The more notable change of what tevador is discussing is the redefinition of key images from the point L to just the x coordinate.     

> __< tevador >__ re: torsion. Using Ristretto without torsion clearing actually reduces the anonymity set to 1/4 of the chain (all keys with the same torsion as the masked key).     

> __< tevador >__ So we need torsion clearing.     

> __< tevador >__ Yes, we are redefining key images by dropping the sign bit. Should be safe.     

> __< k​ayabanerve:monero.social >__ And Ristretto offers less torsion clearing (2 steps not 3), but that's not worth it.     

> __< tevador >__ I think there will be a migration of the key images table during the update. That's the most efficient solution.     

> __< r​ucknium:monero.social >__ The table in LMDB?     

> __< tevador >__ Yes.     

> __< r​ucknium:monero.social >__ jeffro256:  Any comments on this LMDB key images table migration? ^     

> __< k​ayabanerve:monero.social >__ It halves the amount of spendable outputs.     

> __< k​ayabanerve:monero.social >__ It means we need to ensure our address protocol can not only output uniqur keys yet keys with unique abs values.     

> __< k​ayabanerve:monero.social >__ We either need a LMDB migration OR to double our reads (one for +, one for -).     

> __< k​ayabanerve:monero.social >__ We may already need a migration. Are key images global or per pool?     

> __< jberman >__ what pool are you referring to there?     

> __< k​ayabanerve:monero.social >__ Amount     

> __< tevador >__ Global     

> __< jberman >__ ^global     

> __< k​ayabanerve:monero.social >__ Historical outputs are denominated.     

> __< k​ayabanerve:monero.social >__ Great, then we can either do 2x reads or a migration.     

> __< jberman >__ migration is fine     

> __< tevador >__ Btw, the migration of key images is effectively a soft fork. It makes double spend validation stricter.     

> __< k​ayabanerve:monero.social >__ It's justifications are on the gist, but it removes a minor DoS vector re: permissibility.     

> __< k​ayabanerve:monero.social >__ Crafted points could very feasibly trigger hundreds (thousands?) of additions on accumulation.     

> __< tevador >__ And it removes a lot of complexity from the specs and the implementation.     

> __< r​ucknium:monero.social >__ Monero hard forks are usually also soft forks, right? AFAIK, the definition of the two types of forks is that a hard fork allows new txs that used to be not valid and a soft fork prohibits types of txs that used to be valid.     

> __< tevador >__ Soft fork makes some previously valid transactions invalid, but previously valid remain valid.     

> __< k​ayabanerve:monero.social >__ Monero hard forks are hard.     

> __< jberman >__ handling compatibility between old nodes <> updated nodes before fork height sounds a bit tricky, but fine. sounds like we may have to keep the old table around up until the fork height     

> __< k​ayabanerve:monero.social >__ The addition of BP+ wouldn't be accepted by old nodes so BP+ was a HF.     

> __< k​ayabanerve:monero.social >__ Same with view tags, as we didn't use TX extra.     

> __< tevador >__ Correction: newly valid are also previously valid     

> __< jberman >__ or at least, nodes would need to keep key images around that don't pass the stricter height up until the fork height      

> __< jberman >__ stricter check*     

> __< tevador >__ Only if we expect someone to spend both KI and -KI. Otherwise both give the same result.     

> __< tevador >__ and producing both KI and -KI as valid key images implies solving the DLP     

> __< k​ayabanerve:monero.social >__ Due to the existence of the usage of a Htp tbc.     

> __< k​ayabanerve:monero.social >__ If we had a constant generator for key images, that would not be the case.     

> __< k​ayabanerve:monero.social >__ But since we use a hash to point, key images are binding to all components of the output key.     

> __< tevador >__ For example, when we fixed the octuple spending bug, we do the same check also for key images before the fix.     

> __< tevador >__ So we don't need to keep the less strict rule for old outputs. That was my point.     

> __< jberman >__ ok I follow, migration sounds fairly straightforward     

> __< tevador >__ Anyways, all this is just a performance optimization. AFAICS the math checks out.     

> __< k​ayabanerve:monero.social >__ In total, FCMP++s have had a lot of work done on development, have hit performance goals without the proper curve impls, and are moving steadily ahead on research.     

> __< jberman >__ integration moving full steam ahead as well     

> __< r​ucknium:monero.social >__ Fantastic. Any other business?     

> __< s​yntheticbird:monero.social >__ In the current trajectory, should we expect full public release in 1.5 years as planned ?     

> __< jberman >__ integration I think is still complete-able within 6 months fwiw     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< c​haser:monero.social >__ any retrospective thoughts on the May 3 consolidation flood, when we had a ~8 hour constant stream of 150/2's (https://i.opnxng.com/r/Monero/comments/1ci9l7g/in_todays_flood_attack_on_the_network/)? is there any indication that it's related to the March flood? are there any potential privacy implications or new insights into DDoS vectors? it still troubles me how this caused major<clipped message>     

> __< c​haser:monero.social >__  disruption to some nodes.     

> __< nioCat >__ there is another consolidation event today and the backlog is presently being cleared     

> __< c​haser:monero.social >__ nice catch. it's interesting that it's around the same of the week.     

> __< a​lex:agoradesk.com >__ The consolidation flood really affects nodes a lot. Feels like a DoS vector.     

> __< a​lex:agoradesk.com >__ Moreso than the tx flood aka black marble attack. 

# Action History
- Created by: Rucknium | 2024-05-07T20:41:26+00:00
- Closed at: 2024-05-15T19:38:44+00:00
