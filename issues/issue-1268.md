---
title: Monero Research Lab Meeting - Wed 17 September 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1268
author: Rucknium
assignees: []
labels: []
created_at: '2025-09-16T22:07:36+00:00'
updated_at: '2025-09-25T21:55:31+00:00'
type: issue
status: closed
closed_at: '2025-09-25T21:55:31+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Carrot follow-up audit](https://gist.github.com/jeffro256/12f4fcc001058dd1f3fd7e81d6476deb).

4. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf).

5. [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).

6. Mining pool centralization: [Temporary rolling DNS checkpoints](https://github.com/monero-project/monero/issues/10064), [Publish or Perish](https://github.com/monero-project/research-lab/issues/144), and [Lucky transactions](https://github.com/monero-project/research-lab/issues/145).

7. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1266 

# Discussion History
## Rucknium | 2025-09-19T21:06:59+00:00
Logs:
> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1268     

> __< rucknium >__ 1. Greetings     

> __< jberman >__ waves     

> __< vtnerd >__ Hi     

> __< rbrunner >__ Hello     

> __< spirobel:kernal.eu >__ hi     

> __< articmine >__ Hi:      

> __< spackle >__ Hi     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< ArticMine >__ Hi via IRC     

> __< guest55 >__ monerosim. I was able to get some real topology data to create a realistic network for the simulation     

> __< rucknium >__ me: Developing protocol and testing DNS rolling checkpoints https://github.com/monero-project/monero/issues/10064  https://gist.github.com/Rucknium/daf4d52976fc4d32e378771f2e45f8f1 . Analyzing the 18-block re-org on September 14: https://gist.github.com/Rucknium/d055e95c92b66ba7109194720e9dff2e     

> __< ArticMine >__ I have updated the fee and large block analysis     

> __< vtnerd >__ me: got carrot scanning into lws. Legacy, incoming, and balance keys are supported. LWS API only needed minor tweak. Testing is ongoing, and additional updates for subaddresses+incoming keys are needed     

> __< vtnerd >__ Spending fcmp++ is the next big push after getting incoming funds to work     

> __< spirobel:kernal.eu >__ looked at privacy expectations towards (remote) nodes and decoy selection code      

> __< DataHoarder >__ me: produced a timeline of the 18-block reorg on Sept 14th with included full block headers and missing transaction blobs for anyone to replicate the data, and a second-by-second timeline from received events on my node and stratum observers. Includes Tari/P2Pool witnesses.     

> __< DataHoarder >__ https://github.com/WeebDataHoarder/Monero-Timeline-Sep14/blob/master/README.md     

> __< jberman >__ me: opened PR for daemons to kick invalid txs from pool upon popping blocks (e.g. to handle a reorg) https://github.com/monero-project/monero/pull/10085, and for wallets to identify spends in the pool upon restore/if they're not the sending wallet (https://github.com/monero-project/monero/pull/10083), and continuing on the open fcmp++ refresh PR addressing review comments     

> __< bawdyanarchist:matrix.org >__ Very close to beta release for the sim.     

> __< rucknium >__ Ping jeffro256:monero.social     

> __< rucknium >__ 3. Carrot follow-up audit (https://gist.github.com/jeffro256/12f4fcc001058dd1f3fd7e81d6476deb).     

> __< jeffro256 >__ Howdy     

> __< jeffro256 >__ Cypherstack released the result last week, and I have been looking over it. Will probably okay it today or tomorrow     

> __< rucknium >__ Can you link the result?     

> __< jeffro256 >__ It's a draft at the moment      

> __< jeffro256 >__ I would want to make sure that Cypherstack's okay with releasing it first      

> __< rucknium >__ Ok. Any more on this item?     

> __< jeffro256 >__ No, hopefully should be wrapped out by next week      

> __< jeffro256 >__ *up     

> __< rucknium >__ 4. Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf).     

> __< rucknium >__ I will limit discussion on this item to 30 minutes maximum.     

> __< ArticMine >__ I have updated the fee calculations     

> __< ArticMine >__ My recommended proposal is C      

> __< ArticMine >__ This keeps the penalty free zone unchanges     

> __< ArticMine >__ increases the reference transaction size to 20000 bytes. This effectively doubles the fees     

> __< guest55 >__ can you provide the link? I don't see a "C" on that PDF     

> __< ArticMine >__ It does allow for transactions to scale with the low fee up to 20000 bytes or 8 input transactions     

> __< DataHoarder >__ It was updated in this commit. The files are TXSize2025R03C.ods / TXSize2025R03C.xls but no pdf was uploaded https://github.com/ArticMine/Monero-Documents/commit/edd9ed721f2a29190c34f51f0545894681da3627     

> __< ArticMine >__ There is a fee level increase for transactions above 20000 bytes of 4x     

> __< jberman >__ It doesn't look like fees are increasing linearly relative to input count     

> __< ArticMine >__ Fees for a 2 in 2 out transaction will be at current market rates about 0.03 USD     

> __< ArticMine >__ There is a step function at 9 inputs     

> __< ArticMine >__ It is approximately linear if one compares say 1 input with 128  inputs      

> __< ArticMine >__ Similarly for verification time     

> __< ArticMine >__ vs fees     

> __< hbs:matrix.org >__ ArticMine: What would the fee be for a 128 input tx?     

> __< ArticMine >__ 7301 micro XMR     

> __< ArticMine >__ it is actually lower per input than 2 inputs     

> __< plowsof >__ TXSize2025R03C.ods  https://cryptpad.fr/sheet/#/2/sheet/view/mkLJntiayhDr7PQbJUb6+vmOb-y4cGh5lZBxv8inArA/     

> __< ArticMine >__ I do believe this addresses most of the concerns     

> __< jberman >__ need more time to review it     

> __< ArticMine >__ I would suggest placing any more comments question in the GitHub thread This will also allow people to properly review this     

> __< tevador >__ Can you link the github thread?     

> __< guest55 >__ so a ~120 input tx can add 147 kb to the chain, takes 3 seconds to verify, and costs 0.007 monero     

> __< articmine >__ No 0.07 XMR     

> __< articmine >__ Or about 3 USD     

> __< jberman >__ tevador: https://github.com/seraphis-migration/monero/issues/44     

> __< articmine >__ Thank     

> __< articmine >__ Thanks      

> __< guest55 >__  7007 / 1e6 = 0.007 right?     

> __< tevador >__ Thanks. I was looking under monero-project and couldn't find it.     

> __< ArticMine >__ same here     

> __< hbs:matrix.org >__ 0.007 rather, very similar to the current fee for a 128 in / 2 out tx > <articmine> No 0.07 XMR     

> __< tevador >__ I still see 1MB penalty free zone in the .ods file, which is an increase from the current value.     

> __< ArticMine >__ No whe onne factor in the change in tx size     

> __< guest55 >__ 7007, move the decimal over 6 places to the left, gives you 0.007 . what am i doin wrong     

> __< ArticMine >__ It is actually a reduction     

> __< ywu999:matrix.org >__ hello     

> __< tevador >__ I think we can discuss this in the github thread.     

> __< ArticMine >__ if we increase the tx wight by a factor of 4X we should in crease the penalty free zone by a factor of 4x to keep fee scaling rate etc the same     

> __< ArticMine >__ so there a slight decrease     

> __< ArticMine >__ in goin from 1.2 MB to 1 MB     

> __< ofrnxmr >__ Thats 21usd > <articmine> No 0.07 XMR     

> __< ArticMine >__ It is 0.007 XMR      

> __< ArticMine >__ so about 2 USD     

> __< ofrnxmr >__ Ok gotcha     

> __< ArticMine >__ Any more questions?     

> __< rucknium >__ 5. FCMP alpha stressnet planning (https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).     

> __< rucknium >__ Work continues on https://github.com/seraphis-migration/monero/pull/81 , which is the last code to merge before alpha stressnet can occur, AFAIK.     

> __< ofrnxmr >__ There is another pr that builds on 81 as well (the parallel verification)     

> __< jberman >__ Yep, continuing on 81     

> __< ofrnxmr >__ I think, for the most part, its ready for a larger testnet. I still have periodic issues, but maybe easier to diagnose with a larger sample size. I might also spin up a normal private testnet to see if i can reproduce on master (txpool and double spend errors)     

> __< kayabanerve:matrix.org >__ I'd like to propose an update to the FCMP++ of a 10,000-output limit on miner transactions, which is absurd and >300KB, and accordingly shouldn't be a problem.     

> __< kayabanerve:matrix.org >__ (I bring it up now as we're discussing the new FCMP network and it's one slight tweak to the rules I'd like to have included)     

> __< kayabanerve:matrix.org >__ Any objections to the idea/chastisement for derailing the conversation?     

> __< ofrnxmr >__ yes. 300kb is too low. The penalty zone is proposed to move to 1000kb sir     

> __< tevador >__ ^ That's up for discussion.     

> __< jberman >__ No objection from me. sech1 probably has the most relevant opinion since p2pool is the only miner making multiple coinbase outputs per tx     

> __< ofrnxmr >__ Is there a limit today?     

> __< kayabanerve:matrix.org >__ 300KB for the _miner transaction alone_, which is currently allowed to be of infinite size.     

> __< kayabanerve:matrix.org >__ The block size itself.     

> __< ofrnxmr >__ the problem with too many is that thr outputs will be unspendable     

> __< kayabanerve:matrix.org >__ So you can request a TX, and a node can tell you it's 10 GB, and you won't know if that's true or not because you can't verify it until you've received all 10 GB.     

> __< kayabanerve:matrix.org >__ Hence why I'd like to set a bound on the per-TX size, which we have for non-miner TXs (1 MB).     

> __< ofrnxmr >__ .6/10000=0.00006, less than the fee to include the output     

> __< kayabanerve:matrix.org >__ But miner TXs are unbounded, so I'd like to introduce a bound so we can finally say TXs as a whole have a bound.     

> __< kayabanerve:matrix.org >__ 10,000 is just an absurd number no one should object to? I'm fine with lower, but P2Pool may want at least 1,000 in theory.     

> __< ofrnxmr >__ ofrnxmr: The other side of this, is if the blocj rewards is large due to fees     

> __< kayabanerve:matrix.org >__ So I don't think we can immediately agree on 1,000, but we should be able to immediately agree on 10,000 as without issue.     

> __< ofrnxmr >__ kayabanerve:matrix.org: I think p2pool is 2160 cc datahoarder sech1     

> __< jberman >__ Personal preference is lowest that p2pool is ok with     

> __< tevador >__ Why set a limit on the number of outputs and not the tx size?     

> __< DataHoarder >__ Depends on parameters. Usually 2160 unless dynamic difficulty kicks in     

> __< kayabanerve:matrix.org >__ Personal preference is 16     

> __< kayabanerve:matrix.org >__ :p     

> __< kayabanerve:matrix.org >__ tevador: Ugh, you're right, miner TXs still have extra unless the 1060 rule is also applied to miner TXs.     

> __< DataHoarder >__ Coinbase outputs are relatively cheap (view tag + output key + amount) as there are no expensive inputs     

> __< kayabanerve:matrix.org >__ 1060 is being promoted into consensus with FCMP++. I'd ask jberman to check if that covers miner TXs.     

> __< articmine >__ I was suggesting 160000 hard cap on TX size      

> __< DataHoarder >__ checked, only different one is nano but they all have a PPLNS window of 2160 which gives that amount of outputs + a bit more due to uncle blocks     

> __< articmine >__ 160000 bytes      

> __< kayabanerve:matrix.org >__ You're right I just want a miner TX size limit though. While extra + output bounds are the most straightforward way to achieve that IMO, I'm also fine saying miner TXs can't exceed 300KB.     

> __< DataHoarder >__ 700+ outputs is about 48 KiB in p2pool block header     

> __< DataHoarder >__ 27 KiB for 700+ on coinbase alone https://p2pool.io/explorer/tx/6d44248a92458b169ff4c939df8e21e43730e03c59386f792196f06bd0003150     

> __< kayabanerve:matrix.org >__ So 300KB would be ~7000     

> __< kayabanerve:matrix.org >__ I'm also fine saying all TXs must be <~150 KB for the record.     

> __< articmine >__ I still say 160 KB     

> __< DataHoarder >__ quick math gives about 92 KiB for 2160 outputs with some rough estimates     

> __< DataHoarder >__ if needed p2pool can change parameters around hardfork time, as miners will have to update regardless. has been done for view tags.     

> __< ofrnxmr >__ coinbases on fcmp are the same size as current?     

> __< DataHoarder >__ it's an ephemeral pubkey output     

> __< kayabanerve:matrix.org >__ FCMP++ shouldn't change the size of the miner transactions.     

> __< jeffro256 >__ kayabanerve:matrix.org: as written, I don't think the FCMP++ rules assert the size of tx extra on contains, but I think it's a good idea and it could be updated relatively easily     

> __< kayabanerve:matrix.org >__ Oh, CARROT commentary.     

> __< tevador >__ A general 160KB tx size limit would probably work. Enough for a 128/16 tx or >4000 miner outputs.     

> __< jeffro256 >__ kayabanerve:matrix.org: Carrot adds 18 bytes per output     

> __< DataHoarder >__ however, p2pool miners sweeping coinbase will blow their txs sizes under FCMP     

> __< kayabanerve:matrix.org >__ So, 1060 extra to miner transactions and transactions, 10,000 output limit to miner transactions _at a minimum_, and sounds like we're continuing to discuss ~150KB as a global rule?     

> __< DataHoarder >__ I don't know if a special kind of miner coinbase sweep would be allowed without privacy (if common p2pool case is desired) that coalesces all to one output     

> __< DataHoarder >__ Keep it in mind that sweeping 2160 outputs will take 2160/K transactions of K inputs     

> __< tevador >__ Was discussed here: https://github.com/monero-project/research-lab/issues/108     

> __< DataHoarder >__ we already have miners doing almost daily sweeps hitting the max size for tx     

> __< rucknium >__ If possible, I think special transparent sweeps for coinbases is OK.     

> __< DataHoarder >__ I bring it up each time, but if FCMP will limit that massively it can affect specifically current form of p2pool more than it does fee wise, and push people to centralized pools. I think it's fine discussing this outside the scope of this meeting, linked issue can be revived     

> __< rucknium >__ Maybe a can of worms has been opened.     

> __< ofrnxmr >__ rucknium: Always has been     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: I'm not hearing objections to 10,000 outputs as a limit for miner transactions so I'm taking my victory there.     

> __< DataHoarder >__ It's just not as much of a problem now but it's one of the main cons people talk about p2pool or which p2pool to select.     

> __< ofrnxmr >__ DataHoarder: 128input sweeps arent much bigger than 146 rct sweeps     

> __< rucknium >__ Yes, always has been opened, but at this specific meeting where Qubic response still needs to be discussed.     

> __< jberman >__ tevador: Worth double checking max tx size when there are n layers in the tree we're satisfied with. Current code has a limit of 12 layers, which supports a max of ~100 quadrillion outputs in the chain     

> __< DataHoarder >__ 10k outputs sounds more than reasonable, 2160 was selected due to limit on size broadcasted around     

> __< jberman >__ (the more layers in the tree, roughly the larger the FCMP++ proof)     

> __< tevador >__ It would actually be better if the "coinbase consolidation" tx didn't use ring signatures and only had one output. Such transactions would be very small and fast to verify (no membership proofs and range proofs needed) and would not leak any useful information since one output means the outputs have not changed ownership.     

> __< tevador >__ ^ quote from #108     

> __< articmine >__ DataHoarder: This would be applied to the transaction weight, which needs to be fixed for FCMP++ membership proofs. An increase in the tree must not change the weights of the proofs     

> __< articmine >__ jberman: I was referring to this comment     

> __< articmine >__ So yes the actual size in bytes can increase over the 160000 byte limit      

> __< rucknium >__ 6. Mining pool centralization: Temporary rolling DNS checkpoints (https://github.com/monero-project/monero/issues/10064), Publish or Perish (https://github.com/monero-project/research-lab/issues/144), and Lucky transactions (https://github.com/monero-project/research-lab/issues/145).     

> __< rucknium >__ I posted about rolling DNS checkpoints on monero.town: https://monero.town/post/6680879     

> __< rucknium >__ MoneroResearchL on Twiter posted about it too: https://xcancel.com/MoneroResearchL/status/1967336540037636427     

> __< rucknium >__ I think there is some community support and no major objections. Given the 18-block re-org on September 14, I think it should be deployed.     

> __< rucknium >__ I now have testnet checkpointing at these seven domains using a delegated DNS server though monero-highway: checkpoints2.redteam.cash checkpoints2.moneroconsensus.info checkpoints2.moneronet.info checkpoints2.townforgepool.net checkpoints2.townforger.net checkpoints2.moneroresearch.info checkpoints2.bchmempool.space     

> __< kayabanerve:matrix.org >__ My CCS still hasn't even been merged. That's fun for me.     

> __< rucknium >__ That matches the number of moneropulse checkpointing domains that will be used for the next release.     

> __< rucknium >__ DataHoarder:  and ofrnxmr:monero.social  are working with binaryFate to deploy testnet checkpoints on the moneropulse domains managed by the Core Team.     

> __< sgp_ >__ I'm for checkpoints as a temporary measure, with the understanding that them being enabled is bad long-term. I consider them being relied upon as an "emergency" and not something we should be complacent about     

> __< kayabanerve:matrix.org >__ I have objections to it, I just don't see value in voicing them.     

> __< kayabanerve:matrix.org >__ The concept is so centralizing I'd say it's unacceptable.     

> __< kayabanerve:matrix.org >__ And so on and so on     

> __< guest55 >__ yeah i just don't see any other immediate options     

> __< sgp_ >__ People who don't enable checkpoints could be forked off on a different network, which is a real concern. It's not really "opt-in"; there will be consequences for those who don't opt in (those who don't will potentially be on a different network)     

> __< articmine >__ There is a major misunderstanding here. The checkpoints are advisory. It is up to the miners to implement them. The latter is decentralized      

> __< DataHoarder >__ As a key part of their deployment, they remain opt-in. Using them will depend on also gathering a consensus of miners to back them and exchanges (if they desire to stay pinned)     

> __< tevador >__ It's probably enough if 4 pools enable them.     

> __< DataHoarder >__ The main change is that miners that don't opt-out of warnings might get warned in logs on their hourly fetch, but will not enforce them     

> __< articmine >__ It ultimately comes down to what the economic majority chooses. This is what happened in 2018 with Bitmain      

> __< DataHoarder >__ That is, if they are on a divergent chain.     

> __< guest55 >__ yeah but to sgps point, what does happen if a user's node doesn't have checkpoints enabled and they get the qubic chain     

> __< kayabanerve:matrix.org >__ Ethereum as a decentralized checkpoint server.     

> __< monerobull:matrix.org >__ articmine: an optional staking layer is "optional"     

> __< boog900 >__ It would be good to have an RPC method on monerod to add a checkpoint so that solutions acn be worked on without touching the core repo like kayabanerve:matrix.org has suggested     

> __< binaryFate >__ rucknium, DataHoarder: I'm ready to run some checkpointing script on testnet for moneropulse domains. Just not sure what's most up to date or what everybody decided to use for now. I think both of you had some work in progress?     

> __< DataHoarder >__ binaryFate: we do. we can talk after the meeting     

> __< articmine >__ ETH has serious centralization problems      

> __< DataHoarder >__ if they are not opt-in (default) they get warned hourly if they are still on their chain guest55      

> __< DataHoarder >__ if they are opt-out (no warnings) they don't get them     

> __< guest55 >__ i guess, based on qubics behavior, that chain would eventually stall out, and the node would find the real chain?     

> __< kayabanerve:matrix.org >__ But DNS servers don't articmine:monero.social: ?     

> __< sgp_ >__ I fundamentally disagree that checkpoints meant to disrupt re-orgs are "opt-in". Those who don't opt in will likely find themselves on the wrong network     

> __< DataHoarder >__ both will stay there until altchain with checkpoint grows past qubic's     

> __< rucknium >__ boog900:monero.social: That would be good. Yet, there is a workaround with the undocumented checkpoints.json file.     

> __< guest55 >__ but because monerod is ban heavy, would they ever make it back?     

> __< kayabanerve:matrix.org >__ (I know that isn't your position, but Ethereum is undeniably more decentralized)     

> __< monerobull:matrix.org >__ articmine: they have 70% of validators running OFAC MEV bots on a fully transparent network and still fail to censor effectively     

> __< tevador >__ Users who don't enable checkpoints will see the qubic's alt-chain for a couple blocks and then reorg back.     

> __< DataHoarder >__ guest55: I made it back on testnet after mistakenly releasing a 400+ alt chain while I was offline :)     

> __< rucknium >__ binaryFate: I had some prototype scripts for testing. I think DataHoarder 's scripts are best for production deployment. Thanks.     

> __< boog900 >__ rucknium: TIL     

> __< DataHoarder >__ and testnet has fewer nodes     

> __< rbrunner >__ A contrarian position would be to let Qubic make a few more >=10 reorgs until something breaks i.e. an exchange boots their coin off, and they are forced to stop     

> __< DataHoarder >__ +1 on having RPC method for querying runtime (not bundled) checkpoints and managing them     

> __< DataHoarder >__ that'd ease solutions on later stages if bandaid can be decentralized a bit more or altered while proper mid/long term solutions are in the works     

> __< DataHoarder >__ the first implementation is fail-safe with quite the sanity checks, failure mode is not issuing checkpoints     

> __< rucknium >__ guest55: guest55: The draft PR would reduce to 5 minutes the ban time of nodes banning because of incoming blocks inconsistent with the checkpoints. I think that should allow the network to heal quickly.     

> __< rucknium >__ boog900:monero.social: Check https://reddit.com/r/Monero/comments/2ixfe4/monday_monero_missives_weekly_report_october_6th/     

> __< guest55 >__ could we "just" increase the 10 block to 30?     

> __< sech1 >__ late answer to the ping, but: P2Pool doesn't use more than 2160 outputs in coinbase tx, so it's <= 2160*40 = 86400 bytes     

> __< articmine >__ monerobull:matrix.org: Censorship that does not work is actually worse than censorship that works. If the censorship does not work it leads to false accusations of innocent people     

> __< DataHoarder >__ the reality is if temporary rolling checkpoints are deployed, it might get them also attacked over time     

> __< DataHoarder >__ guest55: hardfork!     

> __< ywu999:matrix.org >__ If the DNS checkpoints is "opt-in", the qubic networked can still control 51% of the "non-opt-in" hash power, can     

> __< DataHoarder >__ also still doesn't fix it, they just need to target 30+ now     

> __< DataHoarder >__ harder to do, but they have been able to do more in the past, and released "early" before reaching the optimal height     

> __< spackle >__ Considering the objections, could there be an explicit time limit that this bandaid is in place? Perhaps set things so 1 year from now checkpoints return to normal?     

> __< ofrnxmr >__ They end up on the longest chain, so unless wubic has 51% hashrate indefinitely, theyll get forked back onto the longer chain > <guest55> yeah but to sgps point, what does happen if a user's node doesn't have checkpoints enabled and they get the qubic chain     

> __< rucknium >__ ywu999:matrix.org: Yes. Read "Paths to majority hashpower" section of https://github.com/monero-project/monero/issues/10064     

> __< kayabanerve:matrix.org >__ How secure are these DNS servers? What quorom is required? What happens if conflicting checkpoints are issued? what happens if a later checkpoint reorgs a former checkpoint?     

> __< DataHoarder >__ I think a maximum time (like eth's difficulty bomb lol) would at least keep conversations more focused spackle. But I think it's also better to have a continuous dialogue on what form the bandaid should be deployed as it's an exception, not the norm     

> __< ofrnxmr >__ guest55: Its reduced to 5mins for mismatched blocks     

> __< kayabanerve:matrix.org >__ Who exactly has the right to publish checkpoints? Who hosts the machines publishing checkpoints? Are their physical locations possible to identify?     

> __< DataHoarder >__ 20:25:14 <kayabanerve:matrix.org> How secure are these DNS servers? What quorom is required? What happens if conflicting checkpoints are issued? what happens if a later checkpoint reorgs a former checkpoint?     

> __< DataHoarder >__ checkpoints are not allowed to be issued if previous checkpoint is not part of the chain the new one is at     

> __< DataHoarder >__ that is one of the explicit sanity checks     

> __< tevador >__ The quorum is 5/7 matching checkpoints.     

> __< spirobel:kernal.eu >__ they are an old feature and have been activated before, right?     

> __< kill-switch:matrix.org >__ right, as a p2pool miner I have no intention of enabling checkpoints as I'm opposed to them from a centralization perspective, but also it's not a hard forking measure and so not a ripcord scenario (for me) if the network majority follows the dns.  Kayabanerve points out the practical security implications of such a centralizing measure of course     

> __< ofrnxmr >__ spirobel:kernal.eu: On testnet     

> __< DataHoarder >__ They have been "active" but with old records in them     

> __< articmine >__ Numerous times.     

> __< DataHoarder >__ 3/4 for current code, 5/7 with newer PR     

> __< articmine >__ In the Bitmain case it was due to an over 90% attack      

> __< ofrnxmr >__ Current code is >1/2+1, new is >2/3+1     

> __< spirobel:kernal.eu >__ articmine: was it a successful measure back then articmine:monero.social ?     

> __< guest55 >__ not to dig up old bones, but whats the problem with just a rolling 10 block finality thing? the boogieman of netsplit?     

> __< DataHoarder >__ guest55: hardfork and takes a long time to implement properly     

> __< guest55 >__ jah     

> __< DataHoarder >__ There are ways to spread control over the issuing servers. Due to the way monero verifies the DNS records, it must be ensured that ALL records are published in a matching way to ensure the agreement (eventual consistency across DNS cache). This could change at a later patch but it's not the current form.     

> __< ofrnxmr >__ DataHoarder: A rolling 10 block finality could be implemented by using the json file     

> __< DataHoarder >__ true. or RPC.     

> __< DataHoarder >__ The agreement on contents on this JSON can be done out of bounds (similar to what I was attempting on a branch on my DNS server)     

> __< DataHoarder >__ DNS repository* not server*     

> __< tevador >__ A rolling finality would chain split. And no, that's not hypothetical.     

> __< DataHoarder >__ Though without the ability to match records individually I abandoned that for a happier time     

> __< bawdyanarchist:matrix.org >__ Rolling finality checkpoint right now is a terrible idea. Qubic then just has to target the checkpoint to split the network.     

> __< rucknium >__ I have been experimenting with the checkpoints.json feature. Seems to work fine. You can set the update frequency as frequent as you want by modifying the source code.     

> __< articmine >__ spirobel:kernal.eu: Yes. Very much so     

> __< DataHoarder >__ tevador: rolling as in, keep the last N records, not just last record     

> __< rucknium >__ You just put the file in the same directory as the blockchain.     

> __< DataHoarder >__ same behavior selected as of now     

> __< DataHoarder >__ it doesn't work on DNS as of now, that is understood     

> __< helene:unredacted.org >__ Is the checkpoints.json feature documented anywhere? Would be nice to have that around :)     

> __< spirobel:kernal.eu >__ articmine: if its just a temporary measure and they have been used before with success during the bitmain days, I am unsure how practical the concerns are regarding decentralization. that said when it comes to the long term the comment earlier by sgp_:monero.social  made a lot of sense     

> __< spirobel:kernal.eu >__ should be an understanding that this is temporary and we need to do better.      

> __< rucknium >__ helene:unredacted.org: AFAIK, no. Except here: https://reddit.com/r/Monero/comments/2ixfe4/monday_monero_missives_weekly_report_october_6th/     

> __< spirobel:kernal.eu >__ just a measure for honest pools and nodes to coordinate      

> __< articmine >__ The other chain I believe is still around. It is called Monero Classic or Monero Original      

> __< DataHoarder >__ I think as soon as stable checkpoints bandaid is there the focus of whoever worked on this is to have them work on moving away from them as soon as possible     

> __< guest55 >__ i think we can come to a consensus that the blockchain is under attack     

> __< rbrunner >__ As the old dev that I am I just want to caution about the astonishing tendency of bandaids to become permanent     

> __< guest55 >__ so in the spirit of why this dns system was created it seems logical     

> __< ofrnxmr >__ Most ppl dont even know that monerod skips verification and sync most of the chain using centralized checkpoints (put there at every release)     

> __< DataHoarder >__ I have to hop off now. Will be around in a couple of hours if binaryFate / rucknium / ofrnxmr are up for a setup     

> __< sgp_ >__ I see DNS checkpoints as effectively saying "we are becoming centralized until we come up with something better". And yes to kayaba's point, using ETH or BTC in the interim would be more decentralized. Further, it's hard to be against PoS for "centralization" while running DNS checkpointing     

> __< ofrnxmr >__ Dns checkpoints add dns / networking, but otherwise are trusted just as your release binary is     

> __< DataHoarder >__ (Except difficulty is not checked)     

> __< DataHoarder >__ hash/height is     

> __< spirobel:kernal.eu >__ under attack sounds a bit dramatic. there is an entity that thinks purposely creating long reorgs is a good idea. dns checkpointing is a coordination tool by honest participants to get together and and remove this entity from the equation.      

> __< sgp_ >__ dns checkpoints may seem like an easy option, but they are a seriously damaging option with serious potential consequences     

> __< kayabanerve:matrix.org >__ Will adding DNS checkpoints be used as a reason to shut down research into a finality layer and then become permanent because 'there's no reason to remove them' and 'we have no alternative'?     

> __< ywu999:matrix.org >__ Could Qubic person in this chat as a "fierce" opponent of the discussion? The root problem is the economic incentive any way.     

> __< guest55 >__ but again DNS checkpointing isn't permanent.     

> __< guest55 >__ re: PoS comparison     

> __< spackle >__ At the very least there needs to be an explicit time limit.     

> __< ofrnxmr >__ kayabanerve:matrix.org: Ofrn says no     

> __< kill-switch:matrix.org >__ and not a hard fork eh     

> __< kayabanerve:matrix.org >__ We can soft fork a decentralized finality layer spackle:monero.social:     

> __< bawdyanarchist:matrix.org >__ sgp_:monero.social: I so rarely want to advocate acting in the interest of PR, but checkpointing to another chain is probably worse PR than a temporary activation of a backstop that was designed for this exact problem.     

> __< kayabanerve:matrix.org >__ guest55:  not spackle     

> __< DataHoarder >__ 20:36:36 <kayabanerve:matrix.org> Will adding DNS checkpoints be used as a reason to shut down research into a finality layer and then become permanent because 'there's no reason to remove them' and 'we have no alternative'?     

> __< ofrnxmr >__ spackle: Miners opt out whenever miners feel like it     

> __< kayabanerve:matrix.org >__ Sorry, wrong person replied to     

> __< DataHoarder >__ I will personally push for removing checkpoints in DNS as priority     

> __< spirobel:kernal.eu >__ sgp_: this coordination tool could be more resilient and decentralized, but at the same time it does not mean "we become centralized by using it" quite the opposite       

> __< kayabanerve:matrix.org >__ I'd be much less against DNS checkpoints if we had someone explicitly working on other designs for a finality layer and we had an agreement to form a transition plan completely off DNS checkpoints, whether better PoW or a decentralized solution     

> __< ofrnxmr >__ They can already opt-in today. The question is "when do we stop updating them"     

> __< helene:unredacted.org >__ > <kayabanerve:matrix.org> Will adding DNS checkpoints be used as a reason to shut down research into a finality layer and then become permanent because 'there's no reason to remove them' and 'we have no alternative'?     

> __< helene:unredacted.org >__ I'm interested in the finality layer research, and I do hope your proposal gets merged soon because I would be interested in knowing about the possible solutions you come up with :)     

> __< sgp_ >__ spirolbel I'm just trying to emphasize that these checkpoints are highly centralizing, even more so than the other considered options     

> __< kill-switch:matrix.org >__ for a hard fork, I much prefer as a first step, improving PoW to the state of the art as far as possible, which I am under the impression that PoP and lucky transactions targets that approach?     

> __< rbrunner >__ We still have the option to only activate if Qubic actually makes another >=10 reorg. Which may happen, or not.     

> __< guest55 >__ we're talking about finalizing a 10 block deep state     

> __< rbrunner >__ How is this called? It has a name     

> __< spirobel:kernal.eu >__ maybe the reason people are scared about the finality layer ccs is that it is the only alternative proposed at the moment for the long term.      

> __< ofrnxmr >__ The transition plan off of dns checkpoints: step 1. Stop pushing updates to them     

> __< spirobel:kernal.eu >__ there should be more      

> __< ofrnxmr >__ rbrunner: Grim trigger?     

> __< rbrunner >__ Yup!     

> __< guest55 >__ the network has already decided on finality. 1 centralized entity thinks otherwise.     

> __< rucknium >__ kayabanerve:matrix.org: I think there is general agreement that better PoW (& other) solutions should be investigated. They are being investigated.     

> __< kill-switch:matrix.org >__ with PoW in mind, has anyone on the MRL had any contact from Dr.K of Quai, regarding his PRS workshares proposal, that PR he was putting together?     

> __< rucknium >__ The grim has already been triggered.     

> __< spirobel:kernal.eu >__ sgp_: sgp_:monero.social: the checkpoints itself are not centralizing. the way they are communicated is through less than perfect means.     

> __< rbrunner >__ Rucknium: "The grim has already been triggered" Well, that's a matter of opinion. There is no threat yet, no?     

> __< rucknium >__ kill-switch:matrix.org: Yes. Check log of #monero-research-lounge:monero.social     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: Yes and no. I'm personally pissy and being a bitch about about how my CCS still isn't merged, and on a personal level, taking it as a rejection of my desired discussion topics.     

> __< spirobel:kernal.eu >__ kayabanerve:matrix.org: dont take it personally. things take time     

> __< kayabanerve:matrix.org >__ So we can dismiss this as my personal frustrations, but fundamentally, we are not investigating a finality layer other than DNS checkpoints at this time.     

> __< spirobel:kernal.eu >__ and are messy some times      

> __< ofrnxmr >__ rbrunner: 55 double spends and 115 invalid txs     

> __< rucknium >__ kill-switch:matrix.org: also available here: https://libera.monerologs.net/monero-research-lounge     

> __< kill-switch:matrix.org >__ ty     

> __< rbrunner >__ ofrnxmr: Yes. But that trigger works with a threat. We don't have one yet, in my opinion     

> __< kayabanerve:matrix.org >__ My offer to, a month ago, wasn't accepted and now we're here discussing DNS checkpoints without the benefit of having such research on hand.     

> __< helene:unredacted.org >__ spirobel:kernal.eu: They have reasons to take it personally from the discussions I've seen, but I do find the treatment they get for a CCS odd considering what they've done for Monero and how involved they are; even if I don't agree on everything with them.     

> __< kayabanerve:matrix.org >__ But I'll agree we're investigating DNS checkpoints and other non-finality-layer solutions.     

> __< guest55 >__ one perspective is that the honest mining participants should be coordinating this response     

> __< spackle >__ I am unhappy with this bandaid going into effect without explicit time constraints. People offering assurances or loose plans are not a substitute for knowing there is a hard limit to the action being taken.     

> __< spirobel:kernal.eu >__ helene:unredacted.org: the issue is that people are hesitant about the finality layer if its going to be presented as the only solution. it feels to them that it might be forced down their throat.       

> __< rucknium >__ kayabanerve:matrix.org: I think you may direct your comments at luigi1111  and perhaps articmine:monero.social  instead of the meeting participants as a whole.     

> __< ofrnxmr >__ spackle: Its already in effect, sir     

> __< rbrunner >__ Well, do we have a decision *when* the decision about merging kayabanerve's CCS will be taken? Don't think so.     

> __< ofrnxmr >__ Dns checkpoints can be updated at this very moment. They are already love in the codebase and have been for 10yrs     

> __< helene:unredacted.org >__ spirobel:kernal.eu: My understanding was that it was supposed to be an investigation and comparison between many of the possible options, but maybe I misunderstood.     

> __< spirobel:kernal.eu >__ I would say:  activate dns checkpoints. merge the finality layer ccs. encourage people to propose more solutions besides the finality layer      

> __< rucknium >__ spackle:monero.social: I would be OK with a maximum time limit equal to a conservative guess of deploying PoS finality layer, which is the longest-term of the proposals AFAIK.     

> __< spackle >__ ofrnxmr: only if you insist on thinking of things in a way to confuse the issue. There are clear differences to what is being discussed, I don't feel the need to type them out.     

> __< ofrnxmr >__ The only thing being discussed is pushing updates to them, and coordinating with pools to have them opt-in to respecting them     

> __< DataHoarder >__ 20:39:24 <rbrunner> We still have the option to only activate if Qubic actually makes another >=10 reorg. Which may happen, or not.     

> __< DataHoarder >__ The second grim trigger, no the third, no the fourth...     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: Completely fair. Thank you for pinging them.     

> __< helene:unredacted.org >__ I think pushing updates to them is fine as-is, it's not like they're being enforced in the first place     

> __< helene:unredacted.org >__ It's an opt-in feature that miners/pools might not enable at all     

> __< spirobel:kernal.eu >__ helene:unredacted.org: helene:unredacted.org: we can not have one person do this comparison and then give one recommendation. the community needs to come to a solution as a whole. there needs to be a discourse.     

> __< ofrnxmr >__ helene:unredacted.org: We wont be pushing updates to them unless we have cooperation of >50% of global hash     

> __< guest55 >__ how is that known?     

> __< ofrnxmr >__ By contacting them     

> __< rbrunner >__ DataHoarder: I certainly get what you mean. Still I stubbornly insist there was no proper first threat put up and communicated cleary.     

> __< rucknium >__ NOSH     

> __< spirobel:kernal.eu >__ DataHoarder: this is a good point. only activate if they do another one     

> __< helene:unredacted.org >__ spirobel:kernal.eu: just because you have one person doing some research doesn't mean it's absolute and that it overrides your personal research and everyone else's :)     

> __< DataHoarder >__ rbrunner: the threat was communicated and they even quoted us     

> __< kayabanerve:matrix.org >__ NOSH?     

> __< DataHoarder >__ about the damage that would be done if a 10+ reorg happened and invalidated transactions     

> __< rucknium >__ Nanopool, MoneroOcean, SupportXMR, Hashvault (NOSH). That is almost always enough for majority global hashpower.     

> __< rucknium >__ Check the 10064 issue plots that I made     

> __< spirobel:kernal.eu >__ helene:unredacted.org: in practice it does. and people are rightly concerned about that. other voices will simply be ignored if there is only this proposal and nothing else      

> __< kayabanerve:matrix.org >__ At this point, I understand DNS checkpoints. I just feel we have to be unequivocally clear that even 'opt-in', it's a failure of our decentralization and needs to be a priority to remove.     

> __< DataHoarder >__ 14:11:44 <DataHoarder> CfB has also specifically quoted our IRC conversations from #monero-research-lounge after becoming aware of the damage any 10+ attempt would do on September 1st https://irc.gammaspectra.live/d7cfad5f3e1bdbac/cfb_goi_tech.png yet still went to attempt it.     

> __< guest55 >__ agreed.     

> __< kayabanerve:matrix.org >__ Thank you for the reminder. I remember the topic, I just forgot the acronym.     

> __< guest55 >__ i don't think anyone wants DNS checkpoints.     

> __< guest55 >__ we may need them tho     

> __< ofrnxmr >__ Pools can coolude on their own if theyd like     

> __< kayabanerve:matrix.org >__ Yes, but we need to be clear in our humility and tone IMO.     

> __< rucknium >__ kayabanerve:matrix.org: "Without a doubt, Monero's consensus mechanism would be less decentralized if rolling DNS checkpoints were enabled." https://github.com/monero-project/monero/issues/10064     

> __< rucknium >__ I think this is clear     

> __< kayabanerve:matrix.org >__ This isn't just a response but a failure.     

> __< bawdyanarchist:matrix.org >__ yes, a failure of NC     

> __< kayabanerve:matrix.org >__ rucknium:monero.social: I hear you. That isn't as far as I'm stating though.     

> __< kayabanerve:matrix.org >__ But whatever, so long as we're on the same page     

> __< helene:unredacted.org >__ spirobel:kernal.eu: there have been many proposal in issues, and this is an odd way to see it if there's no one else to step up to contribute to this work in the first place...     

> __< helene:unredacted.org >__ s/in issues/in github issues/g     

> __< rbrunner >__ Implementing a proper finality layer, even if on the table *today*, takes many weeks, if not months. That may become an awfully painful wait.     

> __< guest55 >__ its an odd failure though. because as far as we know, they don't really have 51%.     

> __< guest55 >__ and furthermore the mess created by the re-org is because of the "space saving" output index system     

> __< helene:unredacted.org >__ it is certainly going to be a lot of dev time, testing, and audit time, yes...     

> __< kayabanerve:matrix.org >__ Ethereum could be done within a few weeks rbrunner:     

> __< tevador >__ kayabanerve: Are you suggesting that we do nothing (and see more 10+ deep reorgs) until a proper solution is implemented and tested?     

> __< rbrunner >__ kayabanerve: True, but with maybe two or three such >=10 reorgs in each one of those weeks     

> __< luigi1111 >__ kayaba can you update when delivery would be aimed at, given it's now a month later? The proposal looks mergeable to me (weighing support vs against), however I do share some of the concerns around the cost.     

> __< kayabanerve:matrix.org >__ > At this point, I understand DNS checkpoints. I just feel we have to be unequivocally clear that even 'opt-in', it's a failure of our decentralization and needs to be a priority to remove.     

> __< bawdyanarchist:matrix.org >__ I can see the headlines already: "Monero becomes vassal to Eth protection against Qubic!"     

> __< spirobel:kernal.eu >__ if considering dns checkpointing a failure then monero has already failed long ago as they were used already against bitmain. its just a coordination tool for honest participants. The finality layer would be another coordination tool that makes this process not depend on the domain name system and the box to propose the checkpointing      

> __< kayabanerve:matrix.org >__ I'd be much happier if we did DNS today and agreed we're open to transitioning to Ethereum as the server.     

> __< spirobel:kernal.eu >__ yeah eth checkpointing is not worth the extra effort      

> __< guest55 >__ y not do both     

> __< ofrnxmr >__ Yeah, lets not stuff eth into the codebase     

> __< tevador >__ I'm against using Ethereum. There are other possible solutions.     

> __< kayabanerve:matrix.org >__ luigi1111: same as before, a few weeks to a month.     

> __< DataHoarder >__ yes. and other alternatives or at least distributed issuance should come as priority > it's a failure of our decentralization and needs to be a priority to remove.     

> __< rbrunner >__ And stuff their blockchain full with our blocks, oh what fun :)     

> __< DataHoarder >__ Tari was used as a Witness chain for the recent reorg to prove our orphaned blocks were made     

> __< kayabanerve:matrix.org >__ Ethereum checkpointing is absolutely worth the effort compared to DNS.     

> __< DataHoarder >__ but that was just pure merge mine     

> __< DataHoarder >__ cool, deploy checkpoints, then move to eth kayabanerve:matrix.org?     

> __< DataHoarder >__ then remove them. instead of rushing eth checkpoints or anything else     

> __< tevador >__ DNS checkpoints that had already been implemented in monerod are taking 1 month+ to test and deploy (first discussed in August). I doubt anything more complex could be done in a month.     

> __< kayabanerve:matrix.org >__ Are we as a community willing to explore moving to Ethereum within the next few months? Can we get a show of support for that idea in this meeting? Should I change my work to explicitly be the design of Ethereum as a finality layer and prototype?     

> __< ofrnxmr >__ tevador: And hard forked?     

> __< kayabanerve:matrix.org >__ (with DNS checkpoints for now)     

> __< guest55 >__ i don't understand the ethereum proposal so i have no idea     

> __< kayabanerve:matrix.org >__ If we, widely, agree Ethereum is a better opt-in finality layer than Ethereum, and this is our priority, than I should re-scope accordingly.     

> __< tevador >__ Anthing but Ethereum...     

> __< ofrnxmr >__ I see more against ethereum than for ..     

> __< spirobel:kernal.eu >__ DataHoarder: what you said made sense as well. only deploy them if they do another long reorg.     

> __< rbrunner >__ kayabanerve: " Should I change my work to explicitly be the design ..." Strange question. I see the value of your book in *comparing* various approaches     

> __< rbrunner >__ Maybe I misunderstand however ...     

> __< DataHoarder >__ spirobel:kernal.eu I was joking there. they already did one. The checkpoints must be ready if they ever reach another 9+ height     

> __< kayabanerve:matrix.org >__ rbrunner: It's a priority issue.     

> __< DataHoarder >__ this can be monitored AND deployed to be there within minutes     

> __< kayabanerve:matrix.org >__ Else, luigi1111: As I said, a few weeks, and if the price is too much of an issue, please let me know where you want me to come down.     

> __< ofrnxmr >__ DataHoarder: Also, simply ENABLING checkpoints should discourage them from even attempting     

> __< kayabanerve:matrix.org >__ tevador: Ethereum has proven its censorship resilience and has the requires block space. Bitcoin, the only larger network, can't fit Monero blocks.     

> __< DataHoarder >__ I have half focus here and elsewhere, better to check here later     

> __< kayabanerve:matrix.org >__ We would have to publish the blocks onto the network. Else someone can say     

> __< kayabanerve:matrix.org >__ Checkpoint block X     

> __< kayabanerve:matrix.org >__ But never publish block X, and stall the chain     

> __< rbrunner >__ DataHoarder suffers a chain split :)     

> __< kayabanerve:matrix.org >__ Ethereum will let us do that for pennies. Bitcoin only has 1 MB every 10 minutes, which is insufficient throughput.     

> __< rbrunner >__ That's such an ugly, ugly hack     

> __< rbrunner >__ Those our blocks in their blockchain     

> __< kayabanerve:matrix.org >__ I can write a book on a finality layer in some weeks to a month, and that sounds to be the plan. If we requested, I could re-prioritize to Ethereum as an opt-in finality layer. That was all I was saying. Again, the plan on my end seems to be the book however.     

> __< sgp_ >__ personally I'd rather see effort spent on the finality layer     

> __< luigi1111 >__ kayaba it "seems" like an issue, I can't say for certain, but 100-150 is a more comfortable level. I'm unsure if this discussion is steering the direction of it(?) or if it's "ready to go" regardless     

> __< kayabanerve:matrix.org >__ rbrunner No. Ethereum explicitly supports this because of their layer twos.     

> __< kayabanerve:matrix.org >__ sgp_:monero.social: The ethereum finality layer or finality layer book?     

> __< sgp_ >__ finality layer book; Monero considering options for its own finality layer     

> __< sgp_ >__ that's just my opinion     

> __< kayabanerve:matrix.org >__ luigi1111: It seems like we're merging the book, but I opened a can of worms that will need another fifteen minutes to resolve. I'm willing to come down on the price, especially given recent increases, even though it could trend back the other way and screw me over.     

> __< kayabanerve:matrix.org >__ The book, got it, thank you for clarifying.     

> __< rbrunner >__ Well, if everything gets compared, I wouldn't mind working on that Ethereum abomination first :)     

> __< venture >__ was Mainline DHT assessed as DNS/eth alternative?     

> __< rucknium >__ venture:monero.social: AFAIK, no. What's that?     

> __< sgp_ >__ kayabanerve:matrix.org: maybe you and luigi can speak after the meeting and try to come to agreement on the price, then they can merge?     

> __< ofrnxmr >__ DHT isnt decentralized either iiuc     

> __< spirobel:kernal.eu >__ honestly didnt see the price as an issue. it seems like the objections are a result of being afraid that this will be presented as the only alternative that the community has to swallow without a proper discourse      

> __< kayabanerve:matrix.org >__ rbrunner: It's the concept of data availability.     

> __< kayabanerve:matrix.org >__ To checkpoint a block, we need to ensure it's valid. we can do it locally if we have the block. The issue is how do we get the block? Do we now have the block because of an issue with our internet, or was it never published?     

> __< kayabanerve:matrix.org >__ Ethereum, if we publish onto Ethereum, can assert the block is accessible.     

> __< sgp_ >__ it's research, and other things can be researched too. We aren't deciding to pick the nondescript finality layer     

> __< guest55 >__ and is there a point where our native hashrate is high enough to nullify the need for any of this     

> __< kill-switch:matrix.org >__ I would strongly prefer a soft fork approach even if DNS opt-in, followed by a hard fork first priority that improves our PoW NC from the simple ~35% to approaching a more robust ~50% using PRS/PoP/etc, and after that a hard fork that removes or supplants objective consensus with alternative finality, I would follow the PoW-on [... too long, see https://mrelay.p2pool.observer/e/idi8lLYKS2dVMzNj ]     

> __< tevador >__ FWIW, I'm planning another proposal that is a soft fork, decentralized and works against selfish mining and long reorgs if the attacker is <50%. Requires about 500 bytes of data in miner's tx_extra per block. PoW only.     

> __< kayabanerve:matrix.org >__ Because a variety of blockchains defer to Ethereum for finalizations (their layer twos), Ethereum added an explicit 'blob storage' API to store blocks and attest their accessibility. We'd presumably use that.     

> __< rbrunner >__ Didn't know, interesting. The madness has system.     

> __< kayabanerve:matrix.org >__ Anyways. My priority still seems to be the book, despite the can of worms I just opened. Sorry for opening it.     

> __< luigi1111 >__ kayaba: kk. I'll try to follow along a little bit. And yeah pricing is always double edged     

> __< guest55 >__ we all just need to mine more     

> __< venture >__ ofrnxmr: well.. DNS or Eth aren't either..     

> __< venture >__ rucknium:monero.social it's the DHT used by bittorrent     

> __< rbrunner >__ If you ask me kayabanerve should be able to work on that book for *at least* as much pay as those auditors got     

> __< sgp_ >__ this is not just a mining hashrate issue. It's a distinct disadvantage of a commodity mining algo. There will always be value in mitigating that risk, and I think finally getting new research into that is a good thing     

> __< rbrunner >__ all those FCMP++ reviewers and auditors, I mean     

> __< kayabanerve:matrix.org >__ Ugh. luigi1111: I can't DM you from Matrix. 180 XMR would be about the same USD as a month ago, although XMR is currently dropping and the original proposal still had concerns about price. I'd accept the current volatility though and at least move down to 175. If it has to be 150 to move forward, I'd be unhappy, but I'd rather [... too long, see https://mrelay.p2pool.observer/e/w7LNlLYKNFNXeERk ]     

> __< kayabanerve:matrix.org >__ rbrunner: I quoted <$200/hr if I worked on this _my_ full time and it takes about a month.     

> __< luigi1111 >__ 175 and clear up the ongoing "discussion" or whatever and let's proceed. To others, this is obviously not binding on what must be done on the protocol after publishing.     

> __< kayabanerve:matrix.org >__ That's about an accessibly priced auditor.     

> __< ofrnxmr >__ kayabanerve:matrix.org: How many hours is full time for a few weeks-a month?     

> __< kayabanerve:matrix.org >__ The ongoing discussion was on a book or on Ethereum. We do not have support for Ethereum lol, so that's resolved.     

> __< guest55 >__ sgp, perhaps. But if we had 20 Gh/s on the network because monero's worth a bajillion then we wouldn't be having these conversations     

> __< kill-switch:matrix.org >__ Has the possibility that qubics base hashrate potentially being botnet-heavy been discussed previously?  If so, I've seen a PoW algo tweak recommendations that suits a more memory-heavy or other approaches to shift the balance back towards people that have real cost incentives in the mining rather than being quite as botnet-friendly     

> __< kayabanerve:matrix.org >__ ofrnxmr: for me? I work 80-100 hours a week.     

> __< kayabanerve:matrix.org >__ I don't go out much...     

> __< bawdyanarchist:matrix.org >__ guest55: Selfish mining is a problem regardless of hashrate     

> __< ofrnxmr >__ Maybe if you quoted it as 360hrs     

> __< guest55 >__ yeah i agree on that. leave it to monero to have to deal with a flaw inherited from bitcoin     

> __< ofrnxmr >__ Looking at it as 160hrs makes it look like 400/hr     

> __< rucknium >__ I think some people are uncomfortable with DNS rolling checkpoints, but I don't recall anyone saying a flat "no". Am I correct?     

> __< kayabanerve:matrix.org >__ I'm fine with acknowledging we failed and the immediate stop gap, a failure of its own, of DNS checkpoints.     

> __< rbrunner >__ That's a really nice way to put it     

> __< guest55 >__ we failed to get the NGU so we have a high hashrate yep     

> __< spackle >__ I wish to see a explicit time limit for the proposed changes, but yes I think that is correct.     

> __< rucknium >__ Selfish mining was first modeled in 2014. Monero did not implement any countermeasures since then. This was a blindspot that an adversary has finally attacked.     

> __< kayabanerve:matrix.org >__ It's brutal, but it's unfortunately my view and why I largely put so much focus on a finality layer. I'm unconvinced PoW is rescuable. I want to ensure we don't trend towards long-term acceptance of DNS checkpoints as 'a feature'     

> __< guest55 >__ one question. are. u. mining.     

> __< rucknium >__ I would be ok with an explicit time limit if kayabanerve:matrix.org  would give a conservative estimate for a PoS finality layer deployment, since that's the countermeasures that would seem to take the most time.     

> __< kayabanerve:matrix.org >__ Ethereum as a finality layer? Within three months and unilaterally better than DNS.     

> __< kayabanerve:matrix.org >__ Ethereum is a shortcoming, not a failure, as it would remain decentralized.     

> __< kayabanerve:matrix.org >__ An independent finality layer? Year and a half.     

> __< spirobel:kernal.eu >__ the ethereum thing is not going to happen     

> __< rucknium >__ To deployment? Ok. 1.5 years     

> __< bawdyanarchist:matrix.org >__ Becoming a vassal to Eth is 100% a failure     

> __< kayabanerve:matrix.org >__ DNS is 200% a failure then.     

> __< kayabanerve:matrix.org >__ We become a vassal _and_ a vassal to a centralized entity.     

> __< bawdyanarchist:matrix.org >__ Do I misunderstand that you'd accept Eth checkpointing as a permanent solution?     

> __< bawdyanarchist:matrix.org >__ Or you're saying it's a better temporary solution than DNS?     

> __< kayabanerve:matrix.org >__ The latter.     

> __< rbrunner >__ I think that meeting may have run its productive course, more in the next meeting ...     

> __< rucknium >__ rbrunner: Good! We can end the meeting here. Discussion can continue.     

> __< kayabanerve:matrix.org >__ I don't believe Monero should forsake its consensus. I believe DNS checkpoints do so to a centralized entity and that demands immediate correction. Forsaking to a decentralized entity would not need to be immediately fixed, solely eventually.     

> __< rucknium >__ We didn't get to lucky txs, but tevador is already brewing another proposal     

> __< bawdyanarchist:matrix.org >__ In alot of ways I agree with you, that Eth checkpointing is more decentralized. But I dont think it's a PR move that Monero can afford to make.     

> __< ofrnxmr >__ im not entertaining eth, but wondering: who posts the block on eth     

> __< kayabanerve:matrix.org >__ luigi1111: Pushed reduction to 175 XMR, seems we are sticking with the current CCS as my priority.     

> __< kayabanerve:matrix.org >__ And yet centralized DNS updates is an acceptable PR move?     

> __< ofrnxmr >__ kayabanerve:matrix.org: That would be true if the checkpoints were reactive     

> __< luigi1111 >__ 👍     

> __< kayabanerve:matrix.org >__ ofrnxmr: whoever wants to checkpoint it, presumably the miner to ensure their block reward.     

> __< plowsof >__ https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/448#note_27745 any updates on the FCMP++ dev reviews     

> __< rbrunner >__ Yes, you can't spin that as easily as running on the back of another freaking coin / blockchain. Just PR "logic"     

> __< spirobel:kernal.eu >__ articmine:monero.social: how was it perceived during the bitmain days? > <kayabanerve:matrix.org> I don't believe Monero should forsake its consensus. I believe DNS checkpoints do so to a centralized entity and that demands immediate correction. Forsaking to a decentralized entity would not need to be immediately fixed, solely eventually.     

> __< kayabanerve:matrix.org >__ Eh, we'd probably gain a lot of attention from the Ethereum community. It'd be interesting to see.     

> __< kayabanerve:matrix.org >__ Anyways, it's not my priority and doesn't have to be discussed.     

> __< sgp_ >__ the news at the time around bitmain was mostly about the downsides of cpu algorithms     

> __< spirobel:kernal.eu >__ kayabanerve:matrix.org: monero becoming an eth l2 can already see the headlines     

> __< sgp_ >__ people chimed in saying that they were right, that nothing is actually asic resistant     

> __< ofrnxmr >__ ofrnxmr: this would mean that some centralized entity is forcing miners to roll back their blockchains     

> __< ofrnxmr >__ But that is not the plan. The plan is to checkpoint the existing chain a few blocks deep, to prevent certain reorgs     

> __< spirobel:kernal.eu >__ maybe some ethheads would actually buy and support monero. on the other hand their podcasts shill worldcoin and weird "proof of personhood" schemes      

> __< spirobel:kernal.eu >__ also "soul bound token" is a term that they use without thinking twice how weird and dystopian that sounds     

> __< ofrnxmr >__ So of a single miner can push a block to eth, this same miner is pushing a block to the dns operator, who is relaying said checkpoint to other miners     

> __< bawdyanarchist:matrix.org >__ "Monero become an Eth L2" ... It's a stench that, even if just as a temporary measure, would be nearly impossible to clear from the social sphere     

> __< kayabanerve:matrix.org >__ Miners would publish to and receive checkpoints from Ethereum if Ethereum was the finality layer.     

> __< tevador >__ Let's not waste time on Ethereum checkpointing please.     

> __< venture >__ DataHoarder: Thanks for the timeline. Quick follow-up, were the qubic blocks all disclosed / published to the network all at once in the end, or continuously so that there were 2 publicly known branches at equal length and only at the end published 2 blocks to override?     

> __< ofrnxmr >__ tevador, i was mostly trying to understand (for myself)     

> __< ofrnxmr >__ Not entertaining it     

> __< DataHoarder >__ all at once, venture     

> __< DataHoarder >__ see the logs     

> __< venture >__ will do, thanks     

> __< DataHoarder >__ in monero no alt was seen until that point     

> __< DataHoarder >__ I did not track when the transactions were sent exactly     

> __< venture >__ DataHoarder: you would need multiple monero nodes to confirm that? and an alt of same height as is already incorporated, would you have caught that? monerod would simply ignore I assume?     

> __< DataHoarder >__ I am querying couple nodes, and connected to a few thousand in several witness nodes     

> __< DataHoarder >__ I query alt_block hashes or whatever it is     

> __< DataHoarder >__ see blocks.p2pool.observer source code, as well     

> __< DataHoarder >__ (linked in page itself)     

> __< venture >__ ok, thanks     

> __< DataHoarder >__ alt blocks don't broadcast well. so detecting them can be challenging     

> __< DataHoarder >__ however, I can tell you their first blocks had withheld transactions and were not broadcasted until the entire chain was pushed     

> __< DataHoarder >__ which makes the first blocks non-broadcasteable     

> __< venture >__ ah okay, that confirms it     

> __< charutocafe:matrix.org >__ hi, sorry i don't mean to hijack important discussion so feel free to ignore and continue along, but is the idea of a fixed standard fee/kB that is part of consensus one we've embraced or plan to embrace? i've seen it proposed  many times in the past but nothing ever seemed materialize.     

> __< tevador >__ Fees set by consensus is a very bad idea. You'd need a hard fork for each fee change. AFAIK it has never been proposed.     

> __< charutocafe:matrix.org >__ would you expect fees to require being changed more frequently than monero naturally hard forks?     

> __< charutocafe:matrix.org >__ if each wallet effectively implements their own fee/kb it's a metadata "leak" that gets published on chain forever. i think it negatively impacts user privacy.     

> __< charutocafe:matrix.org >__ maybe it was never proposed at consensus and i just assumed it was     

> __< tevador >__ A relay rule would probably be enough to get wallet developers to behave.     

> __< charutocafe:matrix.org >__ yeah, that's probably wiser     

> __< DataHoarder >__ 21:02:17 <venture> was Mainline DHT assessed as DNS/eth alternative?     

> __< DataHoarder >__ I looked / suggested DHT, however, that can be killed easy. You could have it instead as part of P2P messages in monero, or well, as specially made monero transactions      

> __< DataHoarder >__ 21:10:39 <kill-switch:matrix.org> Has the possibility that qubics base hashrate potentially being botnet-heavy been discussed previously?     

> __< DataHoarder >__ quite some beefy machines on their network, thanks to nonce analysis     

> __< venture >__ yeah, I had a hunch that DHT wouldn't be robust enough for checkpointing.. just wanted to bring it up (you never know)     

> __< tigerix:matrix.org >__ I have just read this thread and am really surprised of the statements here.     

> __< tigerix:matrix.org >__ How is it even considered to use a centralized DNS instead of Ethereum (a solid decentralized option) as a temporary measure?     

> __< tigerix:matrix.org >__ We should always choose the best decentralized option available.     

> __< tigerix:matrix.org >__ Be consistent. Be responsible.[... more lines follow, see https://mrelay.p2pool.observer/e/19PulrYKLVdyQlRQ ]     

> __< DataHoarder >__ DNS checkpoints are being considered for them being available now, transitioning to another bandaid is fine as well as soon as possible. But none of these are *here*     

> __< DataHoarder >__ Like. They exist in the code. They can start being issued. Everything else takes longer, and this discussion of "stall until something better" was had end of August. Monero consensus is slow     

> __< DataHoarder >__ Bleeding while that is being decided, not so much     

> __< DataHoarder >__ Note any non-centralized checkpointing approach requires either hardforks (to not require full txs) or it must include all txs     

> __< spackle >__ For clarity's sake, I interpret 1.5 years to mean the final checkpoint published for this purpose shall be on or before 24 MARCH 2027. Perhaps a different deadline is desired, I just did not want to leave this conversation without being specific.     

> __< ywu999:matrix.org >__ So this meeting ends??     

> __< ywu999:matrix.org >__ So the weekly meeting always lasts about 4 hours, doesn't it? New here, not knowing what is the protocol of th emeeting.     

> __< DataHoarder >__ Not 4 hours, it ends as it needs, and people keep talking     

> __< rucknium >__ ywu999:matrix.org: Most meeting are about an hour. Meetings have been longer recently because of the selfish mining by Qubic.     

> __< rucknium >__ ywu999:matrix.org: The #monero-research-lounge:monero.social  room is good for casual chats.     

> __< ywu999:matrix.org >__ Thank for the response.     

> __< articmine >__ There was a strong community consensus and unity > <spirobel:kernal.eu> articmine:monero.social: how was it perceived during the bitmain days?     

> __< articmine >__ As for the aftermath there was a chain split. Most of the community members ignored the XMC/XMO Bitmain chain. A few of us myself included extracted the Bitmain chain and dumped it     

> __< articmine >__ DNS checkpoints are a temporary solution while the community reached consensus on one or more permanent solutions     

> __< articmine >__ It also allows for the consensus process to proceed without a gun to our heads     

> __< DataHoarder >__ the gun on our heads has been shot already     

> __< articmine >__ ...  and missed     

> __< DataHoarder >__ now they keep holding it and digging out further :)     

> __< DataHoarder >__ missed?     

> __< DataHoarder >__ I mean it happened as exactly as expected     

> __< DataHoarder >__ invalidated transactions, double spends later     

> __< 321bob321 >__ Currently where playing battleship     

> __< articmine >__ I remember when Bitcoin required 6 confirmations. This is like 30 for Monero      

> __< DataHoarder >__ no we are doing game theory and a pigeon is shitting around     

> __< DataHoarder >__ and loudly saying "it didn't happen" while we consider if getting shot again while we develop a full new ballistic shield powered by the gods energy around us is better than using a pocket shield you had all along, just need to insert batteries, not good enough but it's there     

> __< DataHoarder >__ this feels more like lounge convo anyhow     

> __< articmine >__ In my view we need to prioritize those solutions  that are most likely to get consensus, instead of arguing over the most controversial solutions.     

> __< articmine >__ POS to put it bluntly is maximum controversy as is checkpoints on POS chains     

> __< spirobel:kernal.eu >__ we should make sure that this is communicated clearly. that DNS checkpoints have been used before, that it was uncontroversial and resulted in the other chain dying.  > <articmine> As for the aftermath there was a chain split. Most of the community members ignored the XMC/XMO Bitmain chain. A few of us myself included extracted the Bitmain chain and dumped it     

> __< monero.arbo:matrix.org >__ articmine: this is what I've been saying     



# Action History
- Created by: Rucknium | 2025-09-16T22:07:36+00:00
- Closed at: 2025-09-25T21:55:31+00:00
