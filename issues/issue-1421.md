---
title: Monero Research Lab Meeting - Wed 15 July 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1421
author: Rucknium
assignees: []
labels: []
created_at: '2026-07-09T19:28:40+00:00'
updated_at: '2026-07-16T22:22:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. FCMP++ to-do list status. [Programming tasks](https://github.com/seraphis-migration/monero/issues/53). [Reviews and audits](https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/).

4. [Post-quantum encryption](https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686). [Jamtis](https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#appendix-c-instant-sync-protocol). [Repurposing `unlock_time` for relative locks with FCMP++](https://github.com/monero-project/research-lab/issues/161).

5. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/).

6. [`monerosim`](https://github.com/Fountain5405/monerosim).

7. Any other business

8. Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs: #1420 

# Discussion History
## Rucknium | 2026-07-16T22:22:20+00:00
Logs

> __< neptunian:unredacted.org >__ Good afternoon, all.     

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1421     

> __< tevador >__ Hi     

> __< ravfx:xmr.mx >__ o/     

> __< rucknium >__ 1. Greetings     

> __< rbrunner >__ Hello     

> __< boog900 >__ hi     

> __< articmine >__ Hi     

> __< vtnerd >__ Hi     

> __< jberman >__ waves     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< jeffro256 >__ Howdy     

> __< rucknium >__ me: Keeping stressnet stressed and helping troubleshoot there.     

> __< jeffro256 >__ me: reviewing FCMP++ PRs and upstream bug fixes, reworked my RPC  speedup PR , worked on some upstream bug fixes myself     

> __< vtnerd >__ Me: still working on getting the serialization pr 100%, getting closer to (hopefully) solving the weak ptr memleak, and lastly fixing the slowdowns on d++/p2p send code     

> __< jberman >__ me: FCMP++ integration PR's, stressnet debugging followup     

> __< neptunian:unredacted.org >__ me: Reading some fun things about lattice commitments and various other things.     

> __< tevador >__ I have this item for discussion: https://github.com/monero-project/research-lab/issues/161 (apologies for the late submission). Can be done in agenda item 4.     

> __< rucknium >__ tevador: Ok it can be discussed during item 4. Thanks.     

> __< rucknium >__ 3. FCMP++ to-do list status. Programming tasks (https://github.com/seraphis-migration/monero/issues/53). Reviews and audits (https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/).     

> __< jberman >__ * Still slowly making progress on getting integration code merged upstream     

> __< jberman >__ * Making progress on the major beta stressnet items, however, I would stlil say the beta is in a state where FCMP++/Carrot code doesn't need to be blocked from mainnet aka it seems to be in a good state     

> __< jeffro256 >__ As for the task list , since https://github.com/seraphis-migration/monero/pull/424 was merged and reviewed (thanks Ukoe), I can rebase the wallet knowledge proofs PR , and chug along with that      

> __< jberman >__ * UkoeHB has mentioned for multisig he has 1 last test he's working through     

> __< jberman >__ I don't have an update on what's next with hw wallets     

> __< ofrnxmr >__ Also, plowsof:matrix.org  performed wallet sync and cold signing on mobile wallet for stressnet     

> __< jeffro256 >__ I keep getting messages that the companies are looking jnto it, but so far nothing has materialized      

> __< jberman >__ hot/cold wallet stuff seems pretty close to the finish line as well thanks to jeffro256:monero.social     

> __< jberman >__ helioselene audit is still ongoing, and we're still discussing the next steps for another audit round on the circuit + gadget ipml internally     

> __< neptunian:unredacted.org >__ jeffro256: Which companies are looking into it if I may ask?     

> __< jeffro256 >__ Ledger, Trezor      

> __< plowsof >__ ofrnxmr yes , these transactions where all signed offline via DataHoarders stressnet payments explorer https://stressnet.p2pool.observer/payments?id=cat     

> __< plowsof >__ and vtnerds lwsf carrot branch     

> __< rucknium >__ plowsof: Thanks. Does that mean that the code that we know works is Go code?     

> __< UkoeHB >__ Yes working on multisig test. wallet2 is quite poorly designed for testing.     

> __< jpk68:matrix.org >__ Hello     

> __< rucknium >__ Anything more about this topic?     

> __< plowsof >__ afaict yes : for the end user - the difference is after you import the signed transaction set - there is another 10-20 seconds of work that is done (building the tree and things jeffro would know about) but thats all. signed/unsigned tx sizes are just as small as wallet2 tx's      

> __< rucknium >__ 4. Post-quantum encryption (https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686). Jamtis (https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#appendix-c-instant-sync-protocol). Repurposing unlock_time for relative locks with FCMP++ (https://github.com/monero-project/research-lab/issues/161).     

> __< tevador >__ The relative lock is a trade off which might be worth the slight leakage it would cause.     

> __< jeffro256 >__ I don't understand how making the unlock time relative does anything to help it support payment channels      

> __< neptunian:unredacted.org >__ jeffro256: If I'm reading it correctly, I think it's just addressing having a better unlock_time which would preserve the payment channels.     

> __< tevador >__ It allows the channel to have 2 presigned transactions: Withdraw (time-locked) and Punish (not locked). The Punish is used if Alice attempts to close the channel with an old state.     

> __< tevador >__ But I agree we should investigate specific protocols it would allow before implementing it.     

> __< jeffro256 >__ Ah I see. In that case, we would need to move the reference_block field to the signable portion of the transaction      

> __< articmine >__ tevador: Which works very well if the fees are much lower than the channel value.     

> __< jeffro256 >__ This would break tx chaining and make offline signing weirder      

> __< tevador >__ jeffro256: no, it does not need to be signed     

> __< tevador >__ only unlock_time = 1 is signed, so Alice cannot change that     

> __< rbrunner >__ I am still a bit confused. Their value does not rest on them being relative now, or does it? I could already lock up to the same block like any relative lock with the "old" locks     

> __< tevador >__ She can select whatever reference_lock / anchor_height she wants, but if block_height - anchor_height < 720, the transaction won't be relayed.     

> __< jberman >__ > <tevador> But I agree we should investigate specific protocols it would allow before implementing it.     

> __< jberman >__ I agree with this. If there is a specific protocol spec'd that could feasibly work, then it could make sense. FWIW moneromoo at one point highlighted how there is still a way for someone to hack that kind of unlock time behavior with the current unlock_time: by constructing a tx and putting it on chain with a specific unlock_time, and then pre-signing a tx with that output as an input     

> __< tevador >__ You need a relative lock to have payment channels that don't expire     

> __< neptunian:unredacted.org >__ I feel like the fake lock fix could be an issue. How many wallets would realistically be randomly setting unlock_time=1 for normal transactions?     

> __< rbrunner >__ Ah, the clock starts to tick with the mining of the tx, whenever that will be?     

> __< tevador >__ Yes, the block starts ticking when Alice submits the malicious old state transaction.     

> __< tevador >__ clock*     

> __< jeffro256 >__ But does that leave the door open to fraud by anyone who knows the rerandomizations by setting an arbitrary reference block? > <tevador> only unlock_time = 1 is signed, so Alice cannot change that     

> __< jeffro256 >__ *doesn't     

> __< tevador >__ No, you cannot make a valid membership proof for an enote that's not in the tree yet (it will be added ~700 blocks later)     

> __< tevador >__ unlock_time = 1 tells the consesus protocol to use an old tree root for the proof     

> __< tevador >__ Which proves that the transaction is spending only enotes older than 24 hours.     

> __< rbrunner >__ Are these new locks still per tx and not per output?     

> __< rucknium >__ IIRC, one of the reasons custom unlock time is being eliminated at the deployment of FCMP is that custom unlock time negatively affects the FCMP tree performance.     

> __< neptunian:unredacted.org >__ I think it's a bit of a UX issue to have random 24-hour locks on ordinary transactions.     

> __< tevador >__ neptunian: No, there would be no locks on random transactions.     

> __< tevador >__ The enote spent is ALREADY older than 24 hours, so there no wait time.     

> __< rucknium >__ And hasn't the issue with Monero-style locks been that when custom lock time arrives, you have a race in the txpool to spend the tx if multiple people have the right to spend it?     

> __< neptunian:unredacted.org >__ tevador: Ah. I see. Thanks for clarification.     

> __< tevador >__ The repurposed unlock_time doesn't work like the old one. It only affects tx validity, not subsequent spending.     

> __< jeffro256 >__ Yeah that could work. If we can do a gate on some cryptograpgic condition, then that would be pretty similiar to HTLCs     

> __< tevador >__ Basically, with unlock_time = 1, Alice has a pre-signed transaction that will become valid in 24 hours. After that, only the normal 10 block lock applies.     

> __< jeffro256 >__ tevador: *assuming no large changes in hashrate      

> __< tevador >__ ~24 hours*     

> __< jeffro256 >__ I agree with Berman that it would be nice to have at least 1 sketch of a real, useful payment channel before supporting it, but this version of time locks is much closer to actually supporting payment channels      

> __< tevador >__ I will try to add a protocol sketch to #161     

> __< UkoeHB >__ So it's a tx publish lock, not an enote lock as with the current timelocks. Yeah you can accomplish the same with timelocks by submitting a locked enote then chaining off it. So any protocol using relative locks would presumably already work.     

> __< tevador >__ No, it would not work.     

> __< jeffro256 >__ UkoeHB would the main difference here be that this relative lock doesn't put the compute / storage burden on tree builders?     

> __< tevador >__ Current unlock_time is unconditional, so it also prevents Bob from spending it with his Punish transaction.     

> __< tevador >__ The proposed unlock_time functionality would be used to only lock Alice's Withdraw transaction. AFAIK that can't be accomplished with the old locks.     

> __< UkoeHB >__ tevador: you can timelock a dummy enote, it doesn't have to be the funds actually transferred by the relatively-locked tx.     

> __< UkoeHB >__ jeffro256: yeah, and simplifying the payment channel workflow (if there is one)     

> __< tevador >__ OK, so we have a presigned dummy enote. Alice publishes just this dummy, waits 24 hours and then steals the funds from the wrong state transaction.     

> __< tevador >__ I haven't seen any workiable protocol using the current broken unlock_time feature.     

> __< UkoeHB >__ tevador: probably easier for you to post a sketch then I can logically disprove it (or fail to).     

> __< tevador >__ I will post a sketch     

> __< tevador >__ For proving, not disproving     

> __< neptunian:unredacted.org >__ I'd agree with Tevador about the relative lock being good given the slight leakage.      

> __< neptunian:unredacted.org >__ It may be best to wait for the full sketch, though.     

> __< UkoeHB >__ tevador: what about a 2-of-2 on the dummy so it can't be invalidated by Alice?     

> __< tevador >__ UkoeHB: You can try to sketch your protocol using the old locks. I'm strongly suspecting it won't work.     

> __< neptunian:unredacted.org >__ Ooh. A sketch-off.     

> __< rucknium >__ Thanks, tevador  . Anything more on this topic for now?     

> __< rucknium >__ 5. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/).     

> __< jberman >__ For v2.1, I'd like to have the elusive wallet tx rejection double spend errors fully solved. It seems there are a few issues it has exposed (also present in the current release monerod) that are leading to this rare edge case issue     

> __< rucknium >__ I'm starting to test the proposed fixes.     

> __< jberman >__ ^I've requested rucknium:monero.social run all the patches we have for identified issues (1 patch by vtnerd as well) + more detailed logging that would help us be certain we have fully solved it     

> __< jberman >__ And that logging also includes additional logging that would help us get to the bottom of a distinct issue of more frequent bans, seemingly caused by tx relay v2     

> __< jberman >__ Here's a tracker for beta v2.1 : https://github.com/seraphis-migration/monero/pull/415 , I'll updae that as we get more info on the issue with rucknium:monero.social 's majorly appreciated help     

> __< jberman >__ the code rucknium:monero.social is running includes the 3 PR's under the "sporadic double spend" bullet, and the "log missing requested pool tx" bullet     

> __< rucknium >__ Anything more on stressnet?     

> __< jberman >__ nothin from me     

> __< jeffro256 >__ vtnerd how is p2p SSL looking for stressnet?     

> __< rucknium >__ 5. monerosim (https://github.com/Fountain5405/monerosim).     

> __< rucknium >__ gingeropolous:monero.social seems to be working on improvements: https://github.com/Fountain5405/monerosim/commits/main/     

> __< rucknium >__ I don't know if there is anything to discuss.     

> __< plowsof:matrix.org >__ its claimed as being completed now https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589     

> __< rucknium >__ I think the task described in the CCS is completed.     

> __< plowsof >__ thanks for looking into this Rucknium 👍     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< articmine >__ Thanks      

> __< jeffro256 >__ Thanks everyone!     

> __< vtnerd >__ jeffro256: Sorry phone call came in. It was ready last I looked, I'll double check that before Friday     

> __< vtnerd >__ The d++ slowdown took precedence      

> __< vtnerd >__ vtnerd: I'm in the process of moving, so things are a bit hectic around here for another week or so     

> __< DataHoarder >__ 19:18:28 <rucknium> plowsof: Thanks. Does that mean that the code that we know works is Go code?     

> __< DataHoarder >__ This is scanning code, not signing code. I can only generate/verify SAL proofs, not FCMP. I can generate/sign full txs pre-FCMP++. I think plowsof just means "here's a list shown via my explorer" :)     

> __< plowsof >__ couldn't have said it better myself, thanks DataHoarder 😅     

> __< jeffro256 >__ tevador can I ping you again for mx25519 PR review plz ? The carrot_core dependencies are almost all merged, which would leave mx25519, I will PR the unclamped changes soon      

> __< tevador >__ OK     




# Action History
- Created by: Rucknium | 2026-07-09T19:28:40+00:00
