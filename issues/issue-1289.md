---
title: Monero Research Lab Meeting - Wed 29 October 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1289
author: Rucknium
assignees: []
labels: []
created_at: '2025-10-28T20:55:05+00:00'
updated_at: '2025-11-11T23:38:50+00:00'
type: issue
status: closed
closed_at: '2025-11-11T23:38:50+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Spy nodes](https://github.com/monero-project/meta/issues/1124).

4. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf). [Revisit FCMP++ transaction weight function](https://github.com/seraphis-migration/monero/issues/44). [Simple Market-Based Monero Fee Proposal](https://github.com/monero-project/research-lab/issues/152).

5. [FCMP alpha stressnet](https://monero.town/post/6763165).

6. Mining pool centralization: [Temporary rolling DNS checkpoints](https://github.com/monero-project/monero/issues/10064), [Share or Perish](https://github.com/monero-project/research-lab/issues/146), and [Lucky transactions](https://github.com/monero-project/research-lab/issues/145).

7. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1288 

# Discussion History
## Rucknium | 2025-11-04T23:00:34+00:00
Log

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1289     

> __< rucknium >__ 1. Greetings     

> __< articmine >__ Hi     

> __< vtnerd >__ hi     

> __< sgp_ >__ hello     

> __< hinto >__ hello     

> __< jberman >__ waves     

> __< jeffro256 >__ Howdy     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< rucknium >__ me: Looking at some changes in spy node behavior.     

> __< vtnerd >__ working on a lws db/msgpack bug. unable to reproduce locally, so I may have to move on unfortunately     

> __< jberman >__ Reviewed p2p SSL https://github.com/monero-project/monero/pull/8996 (thank you vtnerd:monero.social), continuing stressnet investigating / bug fixing (found and patched an issue in monerod where it over-counts pool weight in memory)     

> __< vtnerd >__ oh yeah, updated that pr too! looking good hopefully     

> __< articmine >__ I had to pause my scaling work to review this 10% scaling proposal      

> __< articmine >__ I have not had a chance to look at the latest version      

> __< rucknium >__ 3. Spy nodes https://github.com/monero-project/meta/issues/1124     

> __< jeffro256 >__ Me: working on extending integration of Carrot devices and Carrot-derived account keys in wallet2     

> __< jeffro256 >__ The goal is for Carrot-derived wallets to be available before the beta stressnet      

> __< jeffro256 >__ As well as hybrid wallets      

> __< rucknium >__ boog900:monero.social noticed that the spy node test is showing some spy nodes as false negatives, starting about a week ago: https://moneronet.info/     

> __< jeffro256 >__ They finally updated ;)     

> __< jeffro256 >__ Nice of them to wait until after the p2p selection improvements were reviewed and released      

> __< rucknium >__ These nodes are still on the same IP addresses. About 100 in DigitalOcean and 100 in Hetzner.     

> __< rucknium >__ The LionLink spy nodes have the same behavior as before.     

> __< rucknium >__ The MRL ban list is still valid. The network should be monitored for "metastasizing" behavior of the spy nodes, i.e. new spy nodes without the peerID fingerprint     

> __< rucknium >__ But, the spy nodes may still be detectable with other tests.     

> __< rucknium >__ This recent paper monitors packet data: Kopyciok, Y., Schmid, S., & Victor, F. 2025. Friend or Foe? Identifying Anomalous Peers in Moneros P2P Network. https://moneroresearch.info/280     

> __< rucknium >__ and finds a lot of anomalous behavior.     

> __< rucknium >__ Their code is open source, so I could try to run it. They use regular passive Monero nodes to collect the data, so it won't be as fast or complete as the network crawler scan that moneronet.info uses.     

> __< rucknium >__ AFAIK, syntheticbird:monero.social  discovered another way to deduce spy nodes.     

> __< rucknium >__ I could push Core to change the DNS ban list to include more spy nodes: https://github.com/monero-project/meta/issues/1242     

> __< rucknium >__ IMHO, this issue ^ is mature and has had time for comments.     

> __< rucknium >__ I set up moneronet.info because it shows pretty graphs and because it helps reveal changes in spy node behavior. It's doing its job 😁     

> __< rucknium >__ Any more comments on spy nodes?     

> __< sgp_ >__ a picture says 1000 words, nice     

> __< rucknium >__ 4. Transaction volume scaling parameters after FCMP hard fork (https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf). Revisit FCMP++ transaction weight function (https://github.com/seraphis-migration/monero/issues/44). Simple Market-Based Monero Fee Proposal (https://github.com/monero-project/research-lab/issues/152).     

> __< syntheticbird >__ Yes, but it isn't deterministic. Under some circumstances there could be false positives, but depending on some criteria we can limit them to probably zero. I'll need to go into some archives as librejo is now down and everything was collected on a private repository.  > <rucknium> AFAIK, syntheticbird:monero.social  discovered another way to deduce spy nodes.     

> __< syntheticbird >__ s/deterministic/100% accurate     

> __< rucknium >__ This discussion topic continues to be challenging. If there are suggestions about how to structure the discussion (especially in the future), please bring them :)     

> __< articmine >__ As I mentioned before I do not have to report anything new since I believe that addressing this new 10% proposal is required      

> __< sgp_ >__ I added two more aggressive scaling examples to my proposal. My proposal aims to simplify scaling and fees. Other parameters can be chosen, so feel free to ask me for different numbers.     

> __< sgp_ >__ 10% is my suggestion and one example parameter, but any other value (e.g. 50%) can be chosen if desired. I included numbers for 25% and 50% this morning     

> __< articmine >__ I agree that this topic is challenging primarily because of the sheer amount of fud and misinformation that has been imported from Bitcoin and related coins     

> __< articmine >__ As for this 10 % proposal my preliminary assessment is that it is a complete disaster and also a serious breach of the Monero's can Cryptonote social covenants     

> __< jberman >__ I think there are 2 core problems to solve on this front: 1) tx weight, and 2) scaling algo. Personally I would prefer to tackle the former first, and the latter second. They can be solved together in one pass, but I think we'd end up stuck in bikeshedding hell trying to     

> __< articmine >__ jberman: Actually the scaling algorithm need to be addressed first     

> __< spackle >__ At present, Monero's scaling design gives no consideration to the capabilities of the daemon. Regardless of the path chosen, I believe this must change in the future.     

> __< articmine >__ Since what we are ultimately dealing is fee incentives     

> __< sgp_ >__ My proposal works for any transaction weight calculation, so it would be fine to handle those separately from that perspective     

> __< ofrnxmr >__ sorry fkr dragging off topic, but what is "weight" ? Is this just some made up concept that is a combination of various factors, but then given a value?     

> __< ofrnxmr >__ (since its not the byte size on the tx, im not sure what its supposed to be)     

> __< articmine >__ sgp_: No it doesn't     

> __< DataHoarder >__ weight can be calculated by number of elements, byte size, or estimated cost of verification etc.     

> __< ofrnxmr >__ Monero seems to have weight and size used interchangeably throughout the codebase, but apparently they aren't the same thing     

> __< jeffro256 >__ ofrnxmr: Yeah basically. The idea of "weight" is a value assigned to how much space a transaction should take up in a block, and thus indirectly, what ratio of fees it should pay compared to other txs      

> __< jeffro256 >__ ofrnxmr: Yeah we love using inconsistent terminology in the codebase      

> __< sgp_ >__ weight = size + other relevant factors, whatever those are     

> __< jberman >__ on current mainnet BP+ txs, weight is byte size,with exception to BP+ txs with >2 outputs, which add marginally larger weight for the BP+ clawback     

> __< sgp_ >__ monero used to use size until verification became more costly for some things than others, that's why it changed     

> __< ofrnxmr >__ jeffro256: ban & block 🥲     

> __< jeffro256 >__ But IIRC, weight was the same as byte size until the first BP fork      

> __< ofrnxmr >__ Ok thanks     

> __< sgp_ >__ I don't have anything else to discuss from my end for this topic     

> __< ofrnxmr >__ (this of note because sum of fcmp txs != advertised block size)     

> __< articmine >__ sgp_: Same here     

> __< ofrnxmr >__ So the "1.4mb" block we see, only has like 800kb of txs. And a 130kb tx has a weight of like 700kb     

> __< jberman >__ the core pushback on weight = roughly byte size for FCMP++ comes from kayabanerve:monero.social, who argues this incentivizes larger txs over n broken up txs, to spend the same number of inputs     

> __< jeffro256 >__ jberman: I agree with j-berman on his point to try to determine weight now      

> __< jeffro256 >__ And I also think it should be approx eq to byte size b/c of the arguments enumerated last week     

> __< jberman >__ kayaba also expressed weight roughly = byte size would not be a blocker     

> __< ofrnxmr >__ on the subject of scaling, im firmly against uniformity taking precedent over scaling. Scaling is more important than uniformity     

> __< articmine >__ jeffro256: I can do this based upon my proposed scaling     

> __< jberman >__ I think the argument for weight roughly = byte size (simplicity, minimize byte size spending n inputs, minimize n outputs on the chain to spend n inputs), is sound enough to warrant the decision     

> __< rucknium >__ Maybe someone should calculate how much developer labor costs it would take for the service that needs to do lots of consolidation txs to develop and deploy the ideal tx algorithm, compared to just accepting a little higher fee costs for suboptimal consolidation. And then compare the actual costs to node operators for storing those txs, in the two methods.     

> __< jberman >__ I think participants today have rough consensus on weight roughly = byte size     

> __< rucknium >__ I think the difference would not be large.     

> __< articmine >__ jberman: Yes     

> __< DataHoarder >__ would pruned size (long term size for "small" nodes) be considered for weight?     

> __< jberman >__ No     

> __< jberman >__ rucknium: Is this analysis required to come to rough consensus here in your view?     

> __< rucknium >__ Has the discussion about tx weight concluded? (Or the minority voices been worn down enough to give up 😉 ?)     

> __< rucknium >__ jberman:monero.social: No. My point is that the points of contention are small details that don't matter much.     

> __< jberman >__ Ya I agree with that as well     

> __< jberman >__ > Or the minority voices been worn down enough to give up     

> __< jberman >__ I think simplicity in design over tinkering with minutiae details is a huge plus here to move forward with     

> __< rucknium >__ To continue ad absurdium, you could compute the labor cost to computing those figures, and then compute the cost to compute the ith, etc.     

> __< rucknium >__ I doubt there would be a large empirical effect if one option were chosen compared to the other.     

> __< jberman >__ Linear increasing fees was probably the main alternative, and then we end up stuck deciding how 1 input/output/extra should count toward the weight, and rehash similar arguments     

> __< jberman >__ All this to say, I think there is strong merit in the simplicity of (and arguments for) weight roughly = byte size, such that the detracting views are not strong enough to warrant deviation from it imo     

> __< rucknium >__ Lets move on to the next item. I will see if I can come up with more structure for the scaling discussion for next time. In the meantime, please feel free to share ideas for a structure.     

> __< rucknium >__ 5. FCMP alpha stressnet. https://monero.town/post/6763165     

> __< rucknium >__ I'm not a real programmer, but it seems to me that monerod is full of technical debt.     

> __< vtnerd >__ seen worse. its still manageable, but others may have different thoughts     

> __< articmine >__ rucknium: Yes, I agree and this debt needs to be repaid before the hard fork     

> __< DataHoarder >__ I'm a programmer, I agree, specially in the older parts of the codebase. They are usually also uncommented and have generic naming     

> __< vtnerd >__ there are some oddities with epee and how that hooks into things, I wish that was done a little differently. the refactor of the tcp server probably helped     

> __< articmine >__ I recognize that this may require additional time and resources      

> __< jberman >__ ofrn and I discussed blocker issues for mainnet launch: 1) OOM after synced (we're going to figure this out), 2) pool consistently cutting down to 1 tx (hopefully solved with the latest bug fix), 3) wallet complaining about double spends     

> __< articmine >__ Including CCS to fund the repayment of this devt     

> __< articmine >__ Debt     

> __< rucknium >__ I think jeffro256:monero.social  and jberman:monero.social 's fixes to the stressnet code created other problems, like OOM (RAM exhaustion). Fixing problems causing more problems seems to be a symptom of bad initial architecture.     

> __< DataHoarder >__ Ends up with fun side discovery trips like ge_fromfe_frombytes https://web.getmonero.org/resources/research-lab/pubs/ge_fromfe.pdf     

> __< boog900 >__ Its not just making the changes, its getting them reviewed and merged      

> __< jberman >__ The OOM was there from the start, we think it's related to something from the FCMP++ integration, potentially the FFI     

> __< boog900 >__ Monerod doesn't really move that fast, for good reason      

> __< DataHoarder >__ which now got fully resolved by kayaba&others     

> __< articmine >__ boog900: It is a lot of work that takes time. This needs to be recognized     

> __< jberman >__ > Fixing problems causing more problems     

> __< jberman >__ Just judging the stressnet channel, it seems to me like we have noticed actual improvement on connection issues and such. So it doesn't look like problems are increasing to me, but maybe you guys have a different experience ofrnxmr:monero.social rucknium:monero.social ?     

> __< DataHoarder >__ there's also the (probably coming at a later point) DNS checkpoints being intertwined with block check code which ends up hard blocking nodes when used on specific thresholds     

> __< rucknium >__ I mean the OOM on sync catch-up. My nodes with 8GB of RAM OOM'ed a lot on sync catch-up recently.     

> __< DataHoarder >__ I think major improvements have been done but the underlying technical debt is seen on mainnet as well     

> __< ofrnxmr >__ rucknium: The ooms have been there since the beginning     

> __< rucknium >__ Some of the connection problems are related to hard-coded limits. You can raise the limits, but that doesn't solve the architecture problems.     

> __< ofrnxmr >__ rucknium: This has existed on master/mainnet forever     

> __< DataHoarder >__ it's just surprises when things that have been with us all along end up not working fully, either to breakage (or never worked properly)     

> __< jeffro256 >__ jberman: I also thought that this was the case. My stressnet node has been taking up excessive RAM since v1.1      

> __< ofrnxmr >__ Its just not noticable due to checkpoints     

> __< DataHoarder >__ I think splitting what is FCMP++ issues vs mainnet would be a starter towards fixing these for beta stressnet?     

> __< rucknium >__ I don't mean that the fixes caused the problems directly, but the fixes can reveal another lay of problems. Sorry to have worded that poorly.     

> __< rucknium >__ another layer*     

> __< jeffro256 >__ Some of the fixes that we think are upstream issue have been adding to the FCMP++ upstreaming plan: https://github.com/seraphis-migration/monero/issues/103     

> __< jberman >__ rucknium: Node mines >4mb fluffy block, relays it to another node that doesn't accept >4mb blocks because of hardcoded limit. We now relay empty fluffly block as expected, and the limit shouldn't be 4mb anyway     

> __< ofrnxmr >__ rucknium: Its neither. Its that the blockchain has grown and extended periods of large blocks are exposing the long standing broken spans     

> __< DataHoarder >__ yeah. symptom vs actual problem     

> __< ofrnxmr >__ DataHoarder: They are, for the most part     

> __< jberman >__ jberman: The architecture is established to allow 0 tx fluffy blocks to relay, but we weren't using it     

> __< ofrnxmr >__ The last stressnet was when i showed the runaway spans to boog and 0xfffc     

> __< jberman >__ Some issues are definitely architectural and require significant structural changes. For example, I personally don't think daemons should keep any counter state in memory in sync with db, because that is bug-prone. But there are little bugs that are fixable like counting correctly that allow us to move forward     

> __< boog900 >__ ofrnxmr: I couldn't figure out the problem at the time, but I did find another issue. I think now I have found the problem: https://github.com/seraphis-migration/monero/issues/147#issuecomment-3446862454     

> __< rucknium >__ ofrnxmr:monero.social: Yes. I think about how rough last year's stressnet was, even after the small fixes that prevented netsplits. It's more than a year later. I don't know where the labor and expertise will appear to fix all these things in a short period of time so the node can scale smoothly.     

> __< DataHoarder >__ I can bring this to stressnet channel later, but do we want to do one last stressnet run with leak detectors or other tools engaged to gather data? for old or new issues     

> __< jberman >__ We have been, ASAN isn't proving helpful unfortunately     

> __< ofrnxmr >__ rucknium: Boog found a vuln associated with runaway spans. 0x attempted to fix them in the dynamic span pr. But they still arent reliably solved     

> __< jeffro256 >__ DataHoarder: I think that it would be great if someone could compile monerod in debug mode and set their OS to save core dumps on OOM then send me or Berman the core dump     

> __< kayabanerve:matrix.org >__ Sorry for being late. I've been working on some Ed25519 code and optimizations. I'll also note, somewhat as a circle-jerk but with relevance due to jeffro256's commentary, I've increasingly been working in code which doesn't allocate at all for usage within monero-oxide, and boog900:monero.social: has done remarkable work on a more efficient DB.     

> __< ofrnxmr >__ The dynamic span pr seems to work to keep the spans below 1gb, but it still runs away a bit, just not to 8gb     

> __< jeffro256 >__ It's probably not a "true" memory leak in the sense that the memory is still accessible, but something somewhere isn't being pruned. ASAN won't catch the former, but hand-inspecting the latter might      

> __< ofrnxmr >__ jeffro256: I havent had an running oom in a while and it seems to happpen when the txpool is huge     

> __< DataHoarder >__ 19:02:09 <jeffro256> DataHoarder: I think that it would be great if someone could compile monerod in debug mode and set their OS to save core dumps on OOM then send me or Berman the core dump     

> __< DataHoarder >__ ^ I can do that, I ran monerod in debug mode during first stressnet days... but I'd have to move this elsewhere, as the OOM is killing more important things     

> __< ofrnxmr >__ And only when the txpool is huge     

> __< DataHoarder >__ unbounded memory growth :)     

> __< DataHoarder >__ would relwithdebug info help?     

> __< jberman >__ only happening when tx pool is huge is actually interesting new info     

> __< ofrnxmr >__ jeffro256: it could very well be the txpool..     

> __< DataHoarder >__ oh woah     

> __< boog900 >__ Is this not just the OOM that txrealy v2 is trying to fix?      

> __< jeffro256 >__ DataHoarder: Debug build would probably be more helpful, but much, much slower to run / sync     

> __< ofrnxmr >__ boog900: Could be     

> __< DataHoarder >__ I have two core dumps of fcmp monero     

> __< DataHoarder >__ on debug mode     

> __< DataHoarder >__ from the 1st of October     

> __< jeffro256 >__ Was that OOM'ed too?     

> __< jeffro256 >__ That was before the fork tho, yeah?     

> __< jberman >__ have you had one since v1.3? > <ofrnxmr> I havent had an running oom in a while and it seems to happpen when the txpool is huge     

> __< ofrnxmr >__ yea, large txpool during spam attack caused nodes to repeatedlt oom     

> __< DataHoarder >__ probably it was during db conversion     

> __< ofrnxmr >__ jberman: No     

> __< DataHoarder >__ I would need to check system logs, it's SIGABRT     

> __< ofrnxmr >__ ofrnxmr: Or. maybe..     

> __< DataHoarder >__ since v1.3 I had two OOMs and one preventive restart from me     

> __< DataHoarder >__ where monerod was using 40+ GiB on stressnet with no RPC usage     

> __< ofrnxmr >__ I told you the last time i had one. Not sure the date on that, but the txpool went from 20mb to 200mb when it did     

> __< DataHoarder >__ I think we can discuss all of this on stressnet channel, if it's FCMP++ monero stressnet specific issues     

> __< ofrnxmr >__ the running oom is probably tx-relay     

> __< ofrnxmr >__ I think boog's right     

> __< ofrnxmr >__ 0xfffc:monero.social  pushed an update addressing vtnerd:monero.social 's review on master     

> __< jberman >__ Ok, generally I think we're going to need tx relay v2 and caching input validation (which is ready), and to observe alpha stressnet perf after both of those are in     

> __< ofrnxmr >__ I dont know if its "ready", but ive run it and it seems ok     

> __< rucknium >__ Let's count resources. Who thinks they are able to fix deep performance issues in monerod? Who would be willing to dedicate a lot of time to that in the next 6 months, 1 year, 2 years, etc.? Who thinks they could recruit new contributors who could and would do it?     

> __< jberman >__ If we see significantly improved behavior after that point, then I'd vote to move toward beta stressnet     

> __< rucknium >__ And there is a need to review proposed changes. What are the resources for that?     

> __< ofrnxmr >__ ofrnxmr: Main issue is that it still has amplification, as it requests missing txs from every peer at once. I think sequentially would be better, but other might disagree (?)     

> __< DataHoarder >__ you'd probably at least 2x of the resources for making the changes and then review     

> __< rucknium >__ This ^ type of work would be "good" to have before the FCMP hard fork, but it's most relevant for scaling discussions.     

> __< DataHoarder >__ specially if doing modifications/refactors as needed     

> __< jberman >__ Paging perfect-daemon     

> __< ofrnxmr >__ jberman: shhhhh     

> __< rucknium >__ jberman:monero.social: Well, need something to be reviewable.     

> __< jberman >__ I'm fine with reviewing whatever. I would personally like to prioritize FCMP++, Serai, and async scanner     

> __< jeffro256 >__ ofrnxmr: ofrnxmr:monero.social: run which one? Caching input validation or tx relay v2?     

> __< ofrnxmr >__ jeffro256: V2     

> __< ofrnxmr >__ Havent tested the caching input pr     

> __< ofrnxmr >__ With amplification, its still about = to boogs calculated 75% savings. W/o amplification, i think were upwards of 95% > <ofrnxmr> Main issue is that it still has amplification, as it requests missing txs from every peer at once. I think sequentially would be better, but other might disagree (?)     

> __< rucknium >__ More discussion about stressnet?     

> __< kayabanerve:matrix.org >__ I'll throw on that I rewrote my RPC code for Monero and it should be a fascinating presentation of why the RPC is frustrating to use as-is, circling into vtnerd's prior commentary on debt and the HTTP server.     

> __< ofrnxmr >__ I think its going well, and the IBD oom is a master issue that needs to be solved at some point (and doesnt req a hf to fix)     

> __< jberman >__ 0xfffc:monero.social: 9933 is ready for re-review?     

> __< ofrnxmr >__ I'll ask 0x to update & rebase the dynamic span pr and i'll retest it against stressnet.. it wasnt well received in review, but the general idea seemed to work well enough     

> __< DataHoarder >__ kayabanerve:matrix.org agree, reminds me of the other discussions a few weeks ago about undocumented areas or inconsistent usage or bad data on specific calls     

> __< 0xfffc >__ jberman: Yes, it has been reviewed once by vtnerd:monero.social . Of course there are still problems. ( since it is a huge PR ). But it is ready for review / testing.     

> __< ofrnxmr >__ jberman: I believe so.     

> __< jberman >__ dynamic span PR is in stressnet already and seemed ok to me. It was the restricted RPC PR that I had some thoughts on that we didn't include in stressnet     

> __< ofrnxmr >__ Dynamic bss is in stressnet,not dynamic span     

> __< jberman >__ ah, misread     

> __< ofrnxmr >__ Dynamic span was intended to curb the runaway spans by stopping download if sync time exceeded a set value     

> __< ofrnxmr >__ By default, only downloading what can be synced within 2mins. (it still runs away occasionally, but not to 8+gb)     

> __< ofrnxmr >__ https://github.com/monero-project/monero/pull/9495     

> __< boog900 >__ Yeah that PR didn't change the stripe_proceed_main condition IIRC, where I am almost certain the issue is     

> __< jberman >__ ok, I think I will pause continuing on OOM while already synced and focus on reviewing 9933 instead, and will review the issue boog pointed out for runaway spans     

> __< jberman >__ > <jberman> ofrn and I discussed blocker issues for mainnet launch: 1) OOM after synced (we're going to figure this out), 2) pool consistently cutting down to 1 tx (hopefully solved with the latest bug fix), 3) wallet complaining about double spends     

> __< jberman >__ but generally I think we want to solve these issues before mainnet launch. And once tx relay v2 + cache validated txs is in and perf observed, we decide on beta stressnet     

> __< rucknium >__ 6. Mining pool centralization: Temporary rolling DNS checkpoints (https://github.com/monero-project/monero/issues/10064), Share or Perish (https://github.com/monero-project/research-lab/issues/146), and Lucky transactions (https://github.com/monero-project/research-lab/issues/145).     

> __< ofrnxmr >__ i think we should release 2) (195) on stressnet and see if anyone runs into the issue again     

> __< jberman >__ typo?     

> __< ofrnxmr >__ Im running on a few nodes, but its not a consistent condition to reproduce, but atleast 3 people on 1.3 have hit it     

> __< ofrnxmr >__ 195 = the fix for the double counting of txs     

> __< jberman >__ agree wasn't sure what the 2) was before     

> __< DataHoarder >__ still blocked by the issue on monero around hitting a checkpoint in the wrong place     

> __< jberman >__ we can get a release out today. Possibly will include cache re-validation too     

> __< ofrnxmr >__ oh, yea, 2 = pool cutting down to 1x (which is a secondary cause of double spend errors)     

> __< jberman >__ DataHoarder: which issue is this one again sorry     

> __< rucknium >__ DataHoarder: DataHoarder: What are the resources needed to address the DNS checkpoint bug, in your opinion?     

> __< jberman >__ ah ya     

> __< DataHoarder >__ see jberman https://github.com/monero-project/monero/pull/10075#issuecomment-3418776630     

> __< DataHoarder >__ rucknium: a reproducer that can be fed via pop_blocks, restart, then feed blocks / txs via RPC in offline mode     

> __< DataHoarder >__ (that way we can literally script the steps and can verify the behavior to debug further and start untangling that)     

> __< DataHoarder >__ realistically it should get refactored to not be really tied together then it can get well unit tested     

> __< DataHoarder >__ that's a ... larger change, in a very consensus part of the logic     

> __< DataHoarder >__ someone that knows that consensus part well can attempt the fixes, but it's not great without a specific reproducer other than "get lucky when the checkpoints are set"     

> __< DataHoarder >__ I manually attempted to selfish mine myself and place the branch in the specific point it's supposed to trigger the issue, but it didn't (and instead got banned for several days by all testnet peers :D)     

> __< ofrnxmr >__ When i was repro, i was manually splitting the chain, causing reorgs, then plugging in checkpoint from the old chain     

> __< DataHoarder >__ from looking at ofrnxmr logs, the call gets called twice in quick succession, one passes and next one fails with the intended block to checkpoint     

> __< DataHoarder >__ so elsewhere it pops (?) and then it can't find the block again in db on next iteration     

> __< ofrnxmr >__ yeah, after getting the checkpoint, the first run through i think should notice that the checkpoint is associated with one of the alt chains, andreinstate the alt chain     

> __< DataHoarder >__ yep. then it tried to add the block, but it couldn't find the parent, which was the checkpointed block     

> __< ofrnxmr >__ Instead, it recognizes the alt chain as orphaned, and refused to reorg onto it, and pops back to before the checkpoint.. then rejects all new blocks     

> __< ofrnxmr >__ Rejects checkpointed block because its ordered. Rejects any other blocks because they dont match the checkpoint     

> __< DataHoarder >__ ^ can't find checkpoint as parent, yeah     

> __< ofrnxmr >__ Manually setting is_a_checkpoint to true, seems to "fix" it (first pass doesnt dall through), so that it reinstates the alt chain. i dont understand what is_a_checkpoint is supposed to do though     

> __< ofrnxmr >__ ..Just that setting it to true "fixes" it     

> __< DataHoarder >__ it forces reorg on it, instead of checking difficulty     

> __< DataHoarder >__ however that means every block is a checkpoint :)     

> __< DataHoarder >__ FCMP++ stressnet also took all the attention, so not much has been done on regular testnet ^ looking into this one     

> __< rucknium >__ I converted most of my testnet nodes to stressnet nodes. I could keep both stressnet and testnet on the same machines, but then the stressnet node would OOM kill everything :D     

> __< rucknium >__ Thanks for the explanations, DataHoarder  and ofrnxmr:monero.social  .     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< sgp_ >__ rucknium:monero.social: your comment about hashrate and XMR/USD price from earlier this week sparked some ideas in my head for scaling, and I may incorporate that idea in some form into my block size proposal     

> __< ofrnxmr >__ DataHoarder: Yeayea, i mean, i dont know what causes it to be true under normal circumstances     

> __< ofrnxmr >__ Because it doesn't seem to do anything.. but the function within it appears to do as advertised and reorg onto the checkpointed chain     

> __< sgp_ >__ My first impression is to use a decreasing hashrate/reward ratio from the prior year as an indicator of network contraction, but I'm still testing a few scenarios for that idea     

> __< sgp_ >__ rucknium:monero.social: I thought about it more, and I think hashrate is too unreliable on an indicator of price to use for anything important. If electricity costs grow faster than CPU speeds, then hashrate per miner reward will decrease. But that's not even the biggest issue. If a network decides to merge mine on Monero, an [... too long, see https://mrelay.p2pool.observer/e/g_Ss2MMKY21tQTZZ ]     

> __< ofrnxmr >__ Or the cost per hash decreases every year based on improvements in processing speed     

> __< sgp_ >__ The efficiency gain is fine for my initial intended use. I was considering using a decrease in hashrate/miner_reward compared to a year ago as a conservative indicator of XMR's decrease in value. But it's not reliable enough for even that due to the merge mine unknown. This is the response I was working on if you want more con [... too long, see https://mrelay.p2pool.observer/e/nsK-2MMKYlVTdkQw ]     

> __< spacekitty69420:matrix.org >__ sgp_: wouldnt the miner reward average be an estimate tho? unless there is an actual way to know how many invidiual rigs are mining on the network but i dont think its an actual thing tho     

> __< sgp_ >__ I don't think the average block reward per miner is a useful indicator, or at least I can't think of how to use that     

> __< articmine >__ sgp_: Of course. It is essentially fixed     

> __< articmine >__ It is called a tail emission      

> __< articmine >__ I suspect what you are really trying to measure is the rate of electricity consumption of the Monero network.      

> __< articmine >__ Since the block reward and the block frequency this would provide a price for Monero in terms of kWh      

> __< articmine >__ . block reward and block frequency are constant     



# Action History
- Created by: Rucknium | 2025-10-28T20:55:05+00:00
- Closed at: 2025-11-11T23:38:50+00:00
