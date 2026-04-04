---
title: Monero Research Lab Meeting - Wed 24 September 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1272
author: Rucknium
assignees: []
labels: []
created_at: '2025-09-23T23:08:52+00:00'
updated_at: '2025-10-07T22:56:35+00:00'
type: issue
status: closed
closed_at: '2025-10-07T22:56:35+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Carrot follow-up audit](https://gist.github.com/jeffro256/12f4fcc001058dd1f3fd7e81d6476deb).

4. [Proof-of-Work-Enabled Relay ("PoWER")](https://github.com/monero-project/research-lab/issues/133).

5. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf). [Revisit FCMP++ transaction weight funcion](https://github.com/seraphis-migration/monero/issues/44).

6. [FCMP alpha stressnet planning](https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).

7. Mining pool centralization: [Temporary rolling DNS checkpoints](https://github.com/monero-project/monero/issues/10064), [Publish or Perish](https://github.com/monero-project/research-lab/issues/144), and [Lucky transactions](https://github.com/monero-project/research-lab/issues/145).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1268 

# Discussion History
## j-berman | 2025-09-24T00:04:18+00:00
Can we add PoWER to the agenda again: https://github.com/monero-project/research-lab/issues/133

## Rucknium | 2025-09-25T21:55:18+00:00
Logs:



> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1272     

> __< rucknium >__ 1. Greetings     

> __< articmine >__ Hi      

> __< rbrunner >__ Hello     

> __< jeffro256 >__ Howdy     

> __< DataHoarder >__ hullo     

> __< sgp_ >__ Hello     

> __< tomdooley:matrix.org >__ Here for moral support, have a great meeting!     

> __< ArticMine >__ Hi via IRC     

> __< jberman >__ waves     

> __< tevador >__ Hi     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< jberman >__ me: completed PR refactoring wallet2 refresh for FCMP++, opened draft PR to persist dest addrs when updating wallet from pre-FCMP++ to FCMP++, opened draft PR for documentation on the FCMP++ integration, some small cleanup PR's, reviewed some of jeffro's PR's     

> __< vtnerd >__ hi: me: working on carrot/fcmp stuff mostly (and some bug fixes). Spent some time diving into curve-trees to figure out how lws was going to handle. likely going to “punt” and giveaway privacy details to monerod (at least for first cut)     

> __< vtnerd >__ the problem is potential memory usage in tree_cache and otherwise having to duplicate the db from monerod into lws     

> __< rucknium >__ me: Analysis of respend behavior of outputs in invalidated txs after 18-block reorg: https://github.com/monero-project/monero/pull/10085#issuecomment-3313627068 . Rolling DNS checkpoints "formal" protocol as flowcharts (click arrows at bottom to see more flowcharts): https://cryptpad.disroot.org/diagram/#/2/diagram/view/yI43W1 [... too long, see https://mrelay.p2pool.observer/e/iYW6sbgKXzB4VEdJ ]     

> __< tevador >__ Me: Responding to the Veridise audit of Helios/Selene and working on a selfish mining mitigation proposal (work in progress).     

> __< jeffro256 >__ Me: Wrote a Rust library for CARROT (https://github.com/jeffro256/carrot-rs) and finished reviewing https://github.com/seraphis-migration/monero/pull/81. Personally excited for alpha stressnet      

> __< DataHoarder >__ supporting DNS checkpoints testing as needed, looking at ZMQ behavior during reorgs for p2pool mining specifically     

> __< articmine >__ Completed a new weight formula for transactions to address the issues with transaction weights and the penalty      

> __< vtnerd >__ DataHoarderdid you spot any other issues than the one in the pr?     

> __< DataHoarder >__ believe it or not the PR one was not related, we found it by chance by testing subaddress payouts on P2Pool.     

> __< DataHoarder >__ I have noticed that when switching to a shorter altchain (checkpointed one) ZMQ updates are not sent properly to P2Pool, or P2Pool ignores them     

> __< DataHoarder >__ I cannot confirm yet if other block/chain ZMQ messages are sent when switching to a shorter chain, noticed it when mining with p2pool on testnet and the network reorg'd against my longer chain (monero switched chain, but p2pool was left behind, and I saw no logs of ZMQ message being received for miner data)     

> __< vtnerd >__ hmm this could theoretical happen if the zmq buffer was full, but that is unlikely     

> __< rucknium >__ jeffro256:monero.social: Would you have time to review a draft of the tx invalidation blog post, just to check correctness? Probably have the draft ready for review in 6-24 hours.     

> __< DataHoarder >__ it's not a blocker (p2pool could workaround this) but I'll post in lounge about it if I can confirm the issue again with more logging in place     

> __< jeffro256 >__ Yes! Send me a DM whenever      

> __< rucknium >__ I mean correctness as "does Rucknium understand this technical point correctly?"     

> __< rucknium >__ jeffro256:monero.social: Thanks!     

> __< rucknium >__ 3. Carrot follow-up audit (https://gist.github.com/jeffro256/12f4fcc001058dd1f3fd7e81d6476deb).     

> __< jeffro256 >__ I'm sorry for the delay, I brought up some input pretty late into the discussion; we're going back over some finer points of their report     

> __< jeffro256 >__ Not much else to report      

> __< rucknium >__ 4. Proof-of-Work-Enabled Relay ("PoWER") (https://github.com/monero-project/research-lab/issues/133).     

> __< jberman >__ I updated the proposal to account for the latest discussion: 1) Equi-X (instead of RandomX), and 2) PoW once per connection, rather than per tx     

> __< tevador >__ FYI, Equi-X is about to be upgraded to v2 due to some issues with v1.     

> __< tevador >__ It's being coordinated with Tor.     

> __< jberman >__ (I received a dm for someone interested in taking on PoWER so I wanted to have the proposal reflect the latest state)     

> __< jberman >__ are the issues public?     

> __< tevador >__ Not public yet.     

> __< jberman >__ got it, thank you     

> __< rucknium >__ By "taking on PoWER" do you mean someone who wanted to implement it (write the code)?     

> __< jberman >__ yes     

> __< jberman >__ I would think an Equi-X v2 would be a drop-in replacement for v1, and the vast majority of code implemented on the Monero side would be unchanged     

> __< rbrunner >__ Will we have to write a C++ implementation of Equi-X ourselves?     

> __< jberman >__ I assume it would be used as an external submodule same way RandomX is used today     

> __< rbrunner >__ I mean the core algorithm. Guess somebody wrote that already     

> __< tevador >__ Yes, EquiX v2 will have the same interface as v1.     

> __< jberman >__ tevador wrote it in C: https://github.com/tevador/equix     

> __< rbrunner >__ Ah yes, thanks.     

> __< jberman >__ jeffro256:monero.social: you raised some pushback against PoW per connection, in case you want to re-raise that point     

> __< articmine >__ I will also raise pushback on this      

> __< jberman >__ what is your argument?     

> __< jeffro256 >__ Yes, I think that A) PoW per connection is much more complicated, adding a lot of unnecessary technical debt to our connection code, and B) that PoW should be reusable per-tx      

> __< articmine >__ User POW can be very harmful in hot climates, mobile devices etc     

> __< DataHoarder >__ so generate pow once, then it can be re-broadcast with same pow? > B) that PoW should be reusable per-tx      

> __< articmine >__ It is a myth that POW heat is irrelevant      

> __< jeffro256 >__ It should be reusable per tx to enable transaction propagation to be faster with new node connections      

> __< jeffro256 >__ DataHoarder: Yes      

> __< boog900 >__ jeffro256: I don't see the argument that this slows propagation       

> __< articmine >__ Still it can be a barrier      

> __< boog900 >__ you don't make new connections on tx broadcasts you use existing connections      

> __< boog900 >__ if anything needing to verify PoW on every hop would slow propagation       

> __< jberman >__ To minimize technical debt, it could be expected on first tx w/>8-inputs, and then the connection is verified for future txs. Would be a simple boolean per connection to keep track of     

> __< jeffro256 >__ boog900: For new connections. If PoW is reusable per-TX, then a node can flood the network with that TX instantly, whereas if PoW is done per-connection, then a node is "locked in" to its existing connections for TX propagation      

> __< jeffro256 >__ Also PoW per-connection opens the door to DoS against honest broadcasters     

> __< boog900 >__ jeffro256: locked in in the sense that they need to do PoW to open more connections .... they still have their current connections tho      

> __< boog900 >__ new connections aren't broadcasted to anyway      

> __< jeffro256 >__ Yes     

> __< boog900 >__ we only broadcast to current connections      

> __< articmine >__ I mean can the spam farm not be set up in some cold part of Canada or Russia?     

> __< jberman >__ If it's per tx, you have to deal with txs sitting in the pool longer than 10 blocks, which is arguably a significant area of technical debt that is likely more significant than a per-connection PoW     

> __< jeffro256 >__ boog900: New connections ask for mempool contents, which would also ostensibly be PoW enabled     

> __< boog900 >__ I also don't really see the technical debt argument they are both added complexity      

> __< boog900 >__ jeffro256: only when finished syncing IIRC      

> __< jeffro256 >__ You still have the 10 block problem with PoW-per-connection though? How is it avoided?     

> __< jeffro256 >__ boog900: Which is most nodes      

> __< boog900 >__ jeffro256: you don't need a timeout on the PoW?      

> __< boog900 >__ jeffro256: no I mean it only happens once a node syncs up not after      

> __< boog900 >__ like a synced node doesn't just a node which has finished syncing      

> __< jberman >__ "User POW can be very harmful in hot climates, mobile devices etc" -> honest devices constructing the tx in the first place is expected to be more CPU/work intensive than the PoW calculation. the PoW calculation is to raise the cost for malicious users who craft invalid txs at no cost     

> __< jeffro256 >__ boog900: You do still need a "timeout" or at least bind the PoW to some provably recent random data or a "challenge", so an attacker can't build up PoW for connections      

> __< boog900 >__ jeffro256: yes but it is per connection .. you don't need to repeat it      

> __< boog900 >__ with per tx after 10 blocks you can no longer send the tx to anyone      

> __< boog900 >__ without doing the PoW yourself      

> __< jberman >__ ^     

> __< jeffro256 >__ Why would the PoW timeout for per-TX necessarily be 10 blocks?      

> __< jberman >__ That's how I had it in the original proposal     

> __< jberman >__ If it's a lot longer, then the attacker can collect PoW hashes for a longer period of time     

> __< boog900 >__ jeffro256: because you can compute loads in reserve and flood all at once      

> __< articmine >__ > <jberman> "User POW can be very harmful in hot climates, mobile devices etc" -> honest devices constructing the tx in the first place is expected to be more CPU/work intensive than the PoW calculation. the PoW calculation is to raise the cost for malicious users who craft invalid txs at no cost     

> __< articmine >__ So the malicious user sets up the spam farm in some cold part of Canada. The malicious use uses the attack POW heat for space heating. There is no cost     

> __< boog900 >__ articmine: the cost is time      

> __< jberman >__ that's definitely added cost over 0     

> __< articmine >__ -40 = zero spam cost     

> __< boog900 >__ they can't just send bytes they have to find a PoW solution to send it      

> __< boog900 >__ better than no cost      

> __< articmine >__ -49 C or F     

> __< tevador >__ articmine: Not zero cost. They could be mining Monero instead of spamming. Opportunity cost.     

> __< rucknium >__ At least, there is an opportunity cost of not mining Monero blocks.     

> __< boog900 >__ https://github.com/monero-project/monero/blob/8d4c625713e3419573dfcc7119c8848f47cabbaa/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L2442     

> __< articmine >__ It is not the same because the amount is so sma     

> __< articmine >__ Snall     

> __< jberman >__ jeffro256:monero.social: do you see the argument in favor of per connection PoW? if not, I think we should table the discussion, and at least come to agreement that it makes sense for wallet API to allow specifying a max input so the other dev can start on this task?     

> __< boog900 >__ boog900: only once per run of monerod it seems      

> __< jeffro256 >__ jberman: I see the argument, I don't know if I'm entirely convinced, but yeah I can definitely start on that wallet API point      

> __< jberman >__ I think that may be a good task to pass over to the other dev, but your call, we can discuss later     

> __< jeffro256 >__ Perhaps you can let the aforementioned dev working on per-connection first, and both if he/she has the time, and then we can compare what the actualized complexity is      

> __< jberman >__ that sgtm     

> __< tevador >__ Slightly related note: Have we considered having a special connection type for block relay only? Those would not need any PoW. Bitcoin has it. Low-end devices could then still connect to the network.     

> __< rucknium >__ IIRC, by default bitcoin has 8 outbound connections for block + tx relay and 1-2 additional connections for block-only relay.     

> __< articmine >__ Now that is an interesting idea      

> __< jberman >__ The PoW per connection could be an optional thing done per connection, and if done, enables sending txs with >8 inputs over the connection     

> __< jberman >__ via tx relay     

> __< jeffro256 >__ jberman: This is how I imagined it, but there's still the issue of mempool fetching. Does that force the responder to upgrade the connection by doing PoW?     

> __< articmine >__ It is certainly better if it is done by the node     

> __< boog900 >__ jeffro256: seen as thats a response, no IMO     

> __< boog900 >__ you can't exactly spam txs with that      

> __< jeffro256 >__ But then that allows the responder to dump a load of invalid high-input txs to the requester     

> __< jeffro256 >__ Ostensibly, the requester would try validating at least 1      

> __< boog900 >__ jeffro256: the node ignores the rest if any 1 is invalid      

> __< boog900 >__ shouldn't be a DoS      

> __< jeffro256 >__ Assuming you can't trigger a node to make that request with high frequency     

> __< boog900 >__ jeffro256: current code wont, we just need to keep it in mind for future changes       

> __< rucknium >__ 5. Transaction volume scaling parameters after FCMP hard fork (https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf). Revisit FCMP++ transaction weight funcion (https://github.com/seraphis-migration/monero/issues/44).     

> __< rucknium >__ I will limit discussion of this item to 30 minutes maximum, unless there is an objection.     

> __< articmine >__  The major change is the overall weight applied to the transaction to mitigate the impact of the penalty.      

> __< articmine >__ The reasonable weights based number of inputs work very well      

> __< articmine >__ So we can easily have fees that are close to proportional to number of inputs or verification time      

> __< articmine >__ It is a major change in how WWE charge fees     

> __< articmine >__ So now the fee depends on the square of the weight      

> __< articmine >__ The next step is t get the size and verification times for all the peoofs     

> __< articmine >__ Any qt?     

> __< articmine >__ Questions?     

> __< articmine >__ I have the data for the membership proof weight formula already      

> __< articmine >__ So the proposed weights for this proof are in the latest proposal      

> __< jeffro256 >__ Sorry, but at the moment, I NACK making the fee a non-linear function of the weight. That has the same effect as making the weight a function of the square of the number of inputs, which we previously agreed that the weight of the tx should be a linear function of the number of inputs      

> __< jberman >__ I included the SAL proofs as well in the latest update to that comment     

> __< articmine >__ The penalty is non linear      

> __< articmine >__ The end fee is linear with the number of inputs      

> __< jeffro256 >__ Agreed on the penalty being non-linear. But the penalty isn't quadratic in the weight of 1 transaction, it is quadratic in the total size of all transactions in a block     

> __< jeffro256 >__ The base fee-per-vbyte should be calculated as a square of the backlog IMO, not as a square of the 1 tx weight      

> __< articmine >__ That way scaling works it is quadratic on each transaction. That is the point      

> __< articmine >__ It amounts to the same thing      

> __< jeffro256 >__ It doesn't amount to the same thing, especially when the penalty free zone isn't saturated. A 2-in tx should not cost 4x as a 1-in tx when the marginal penalty difference for both is 0.     

> __< articmine >__ The penalty for adding a transaction is quadratic with the TX weight      

> __< articmine >__ It doesn't cost 4x. It is linear      

> __< articmine >__ Because the weight goes as the square root      

> __< articmine >__ The latter is the point      

> __< jeffro256 >__ The penalty is not quadratic in the single TX weight, its quadratic in the total TX weights for that block, which results in different calculations for individual txs based on on-chain activity     

> __< jeffro256 >__ You mentioned that fee is a function of the square of the weight in your latest proposal, yes?     

> __< articmine >__ Iit is a simple formula for the additional penalty      

> __< jeffro256 >__ Oh so you're proposing weight be a function of the square root of the number of inputs?     

> __< articmine >__ Correct      

> __< articmine >__ That is the point      

> __< jeffro256 >__ Why that change?     

> __< jeffro256 >__ Versus keeping both linear      

> __< articmine >__ So that after the quadratic penalty is applied you get linear with the number of inputs      

> __< articmine >__ You mean changing the penalty to linear      

> __< articmine >__ I looked at that      

> __< articmine >__ This works better because it incentivizes effective block construction by the miner     

> __< articmine >__ The penalty has never been linear      

> __< jeffro256 >__ I meant weight function and fee function by "both", not changing the penalty function      

> __< articmine >__ It doesn't work      

> __< articmine >__ The quadratic penalty is in-between the weight function and the fee function      

> __< articmine >__ So apply square root weight, then quadratic penalty , then quadratic fee     

> __< jeffro256 >__ Okay I think I see the fundamental disagreement. You believe that the marginal loss of block emission due to the penalty is a quadratic function of each transaction weight. I believe that the marginal loss of block emission due to the penalty is a quadratic function of the total transaction weights in a block. Is this a correct assessment?     

> __< articmine >__ Yes      

> __< articmine >__ It is the difference in penalty      

> __< articmine >__ That matters      

> __< articmine >__ Apply the penalty right at the start of scaling      

> __< jeffro256 >__ What would it take to convince you that the marginal loss of block emission due to the penalty is a quadratic function of the total transaction weights in a block, and that the base fee-per-vbyte should be a quadratic function of that value, instead of being quadratic in the weight of one transaction?     

> __< jeffro256 >__ articmine: I disagree, this doesn't make sense for 99% of cases      

> __< jeffro256 >__ It only works in the worst case      

> __< articmine >__ You have to look at the game theory of the interaction between miners and users     

> __< articmine >__ Assume enlightened best interest      

> __< articmine >__ So yes the worst case controls     

> __< jeffro256 >__ So people should be paying fees 100% of the time as if they were pushing up the dynamic block size ?     

> __< articmine >__ Correct      

> __< jeffro256 >__ This is a bad idea IMO. That means that there's no downwards price incentive for keeping the block small      

> __< articmine >__ The lowest fee pays the marginal penalty      

> __< jeffro256 >__ People should be rewarded for not increasing the block size      

> __< articmine >__ jeffro256: You mean rewarded for not using Monero?     

> __< jeffro256 >__ For not making spam, yes. There is still a driving incentive for people to use Monero, which is its monetary and transactional utility over other currencies. But there needs to also be an incentive to not make unnecessary transactions      

> __< tevador >__ rucknium: It has been 30 minutes.     

> __< rucknium >__ 6. FCMP alpha stressnet planning (https://github.com/seraphis-migration/monero/issues/53#issuecomment-3053493262).     

> __< jberman >__ The blocker PR 81 has been accepted (thank you jeffro!), ofrn is now doing final testing with the latest state of that PR     

> __< jberman >__ Once I get a green light from ofrn, I'll make the PR setting alpha stressnet dates     

> __< jberman >__ (by setting hf blocks on testnet)     

> __< jberman >__ Thinking I'll write up a shareable post in that PR description, and we can share that post in the stressnet room, and reddit?     

> __< jberman >__ once the PR is accepted     

> __< jberman >__ And as per prior discussion, will target 7 days from the time of acceptance     

> __< rbrunner >__ That should do IMHO     

> __< rucknium >__ Note: I think as of today, the default decision will be to release my tx spamming code as open source. That lowers the barrier a little for a malicious actor to spam mainnet, but all my CCS work is supposed to be published open source. If that default choice should change, it could be discussed.     

> __< rucknium >__ 7. Mining pool centralization: Temporary rolling DNS checkpoints (https://github.com/monero-project/monero/issues/10064), Publish or Perish (https://github.com/monero-project/research-lab/issues/144), and Lucky transactions (https://github.com/monero-project/research-lab/issues/145).     

> __< rucknium >__ There is a bug that can occur in rare cases that will get a node stuck if it is enforcing DNS checkpoints. AFAIK, 0xfffc:monero.social   and ofrnxmr:monero.social  are investigating it.     

> __< rucknium >__ binaryFate has activated the checkpointer of testnet for the seven moneropulse domains: testpoints.moneropulse.xxx     

> __< ofrnxmr >__ 0xfffc:monero.social  is trying to fix the logic that caused reorged checkpointed nodes to get stuck. Will test one more time with the moneropulse domains, and if i break that checkpointer again, we'll switch back to ruckniums domains to speed up the testing     

> __< ofrnxmr >__ s/one more time/until it breaks again/     

> __< rucknium >__ I tested DNS resolver latency (important for agreement between the 7 records of the 7 domains). My preliminary results say that there is good performance when one of several specified DNS resolvers are used. There are mixed results when a machine's own default DNS resolver is used. It is easy to change resolvers for monerod with a terminal environmental variable.     

> __< rucknium >__ Do we have info about mining pools' willingness to turn on checkpoints? At least anything that can be shared publicly?     

> __< rucknium >__ I created a set of flow charts that provides a "formal" specification of the rolling DNS checkpoint protocol: https://cryptpad.disroot.org/diagram/#/2/diagram/view/yI43W1RWom0yoODUJzvAB5vAc9X9ujFVAsxGAxgMMyE/embed/      

> __< rucknium >__ Click the arrows that appear at the bottom of the pages to go to the next page.     

> __< rucknium >__ Once everything is finalized, there will be this flowchart and a narrative. And I hope some FAQs, too. The protocol helps users understand the proposal and how exactly it works.     

> __< rucknium >__ Anything more on temporary rolling DNS checkpoints, specifically?     

> __< venture >__ I already enabled dns checkpoints on my node, even though not active yet. Just to note, I got      

> __< venture >__ [RPC0]        ERROR   cn      src/cryptonote_core/cryptonote_core.cpp:1262    Transaction not found in pool     

> __< venture >__ quite regularly afterwards.. I don't think this was the case before     

> __< ofrnxmr >__ Thats unrelated     

> __< venture >__ hm ok     

> __< tevador >__ On the next topic, I'm working on an upgrade to Publish or Perish called "Share or Perish" with workshares. There are still minor issues to be solved before I can publish it.     

> __< rucknium >__ venture:monero.social: AFAIK, that's unrelated to DNS checkpoints and would usually happen when Qubic is withholding txs. DataHoarder  could confirm maybe     

> __< DataHoarder >__ that is normal venture. do you have p2pool?     

> __< rucknium >__ Thank you, tevador.     

> __< DataHoarder >__ that means you are trying to submit_block with unknown txs to your node     

> __< DataHoarder >__ it's fine, it happens in normal conditions     

> __< venture >__ tevador: Nice :)     

> __< venture >__ I have published some simulation results regarding PoP here     

> __< venture >__ https://github.com/venture-life/mining-simulator/blob/main/out/simulation-results.md#publish-or-perish-with-k3-and-d50     

> __< venture >__ DataHoarder: ah alright, thanks     

> __< venture >__ venture: turns out: deterministic selection doesn't change things.     

> __< venture >__ otherwise, quite good results I think. With 40% hashrate and close to 1 gamma, without mitigation, the revenue is around 57%. with PoP it drops to 47     

> __< rucknium >__ kayabanerve:matrix.org: I think finality layer is fine to discuss during this agenda item, too. I should add it to the links for this item in future agendas.     

> __< kayabanerve:matrix.org >__ Thank you. I have nothing to discuss there immediately and am here awaiting FCMP++ topics.     

> __< rucknium >__ venture:monero.social: How do those results compare to the results i the original PoP paper? Can they be compared?     

> __< venture >__ I think they roughly match. will double check     

> __< tevador >__ AFAIK it should be around 65% with no defenses and α=0.4     

> __< rucknium >__ kayabanerve:matrix.org: This is the last agenda item besides "any other business", which could include more FCMP++, of course.     

> __< kayabanerve:matrix.org >__ Oh, sorry. I thought sgp:magicgrants.org: had one added. My mistake.     

> __< tevador >__ We can discuss that also. Maybe after the meeting?     

> __< kayabanerve:matrix.org >__ Sorry for getting my wires crossed.     

> __< venture >__ yes, 66 is theoretical limit. but then people assume attacker has almost 0 propagation delay and a huge number of honest miners..      

> __< rucknium >__ sgp_: It was added and then deleted ^     

> __< sgp_ >__ oh, sorry I meant for it to be an agenda item for the update     

> __< kayabanerve:matrix.org >__ I just saw, yep     

> __< rucknium >__ DataHoarder: Could you discuss your empirical findings about Qubic's selfish mining profitability?     

> __< sgp_ >__ I should have just said "it will be a agenda item, with more to discuss later"     

> __< DataHoarder >__ I had to drop off, I can come with that later rucknium     

> __< rucknium >__ Thanks, DataHoarder     

> __< tevador >__ venture: so PoP doesn't do much for a low-gamma attacker? Qubic seems to be a low-gamma attacker. However, PoP doesn't stop 10+ deep reorgs. That's what my next proposal is intended for.     

> __< sgp_ >__ May I proceed with the FCMP++ curves stuff if there's no other business? Sorry I didn't mean to remove it fully     

> __< tevador >__ ^ Yes, we can continue with this item.     

> __< rucknium >__ tevador: Good. In the case of Qubic's behavior, I don't think just reducing the selfish mining economic incentive would deter Qubic or similar actor. Need something with more teeth.     

> __< venture >__ I think so yes. Really low-gamma attacker might even benefit from the propagation window to some extend. but it also caps high gamma profitability     

> __< rucknium >__ It seems that Qubic is selfish mining for its propaganda value more than direct economic mining reward profits.     

> __< bawdyanarchist:matrix.org >__ Preliminary results from my sim show that, a silent stubborn attacker can reorg 20 blocks with regularity. Under various selfish strategies and network loads, they dont appear any more profitable than an honest miner, until that 33% threshold (which is in line with a low gamma attacker).     

> __< rbrunner >__ Can somebody throw in a one-line quick definition of "low gamma"? Thanks!     

> __< rucknium >__ bawdyanarchist:matrix.org: Have you seen my theoretical/analytical analysis here? https://github.com/monero-project/research-lab/issues/102#issuecomment-2402750881 My "Table: Duration of meta attack to achieve attack success probability of 50 percent" supports your findings.     

> __< bawdyanarchist:matrix.org >__ rucknium:monero.social: Yes, but I havent compared my sim results to the theoretical values yet.     

> __< bawdyanarchist:matrix.org >__ rbrunner: The percent of honest hashpower that ends up mining on the attacker's branch, instead of the honest extension     

> __< bawdyanarchist:matrix.org >__ Typically driven by ping, or in some cases, eclipsing attacks.     

> __< venture >__ gamma is used in literature as an artifial metric between 0 and 1 how likely it is an honest miner will mine on the selfish-head given two branches of equal work... it's a metric for "connectivity" of the attacker     

> __< rucknium >__ Sounds good. My attacker follows a specific z stopping rule strategy that may differ from your attacker's strategy. But the general conclusion is the same: a large-minority attacker can achieve deep reorgs if it tries again and again.     

> __< bawdyanarchist:matrix.org >__ Their reorg lengths are significantly affected by their willingness to be "stubborn". Basically to tolerate the honest branch fully catching up, and then claiming the win after exiting the 0' state.     

> __< rucknium >__ I think I had some simulation code to double-check my formula results, but I didn't post it. I will try to look for it.     

> __< rbrunner >__ So no rented hash rate to jump over 51% for an hour or two not strictly needed for large reorgs?     

> __< tevador >__ No, just luck.     

> __< rucknium >__ rbrunner: Not necessary. But it is possible that Qubic is doing that, too.     

> __< bawdyanarchist:matrix.org >__ I'm adding summary metrics at the end of each round, and then adding sweeps to the input parameters, so I should be able to search a pretty wide range of input conditions, and summarize those findings.      

> __< rucknium >__ I computed the probability that Qubic acheived their 20-block reorg with 40% hashpower share (assuming difficulty = 100% hashpower share) and got 5% probability.     

> __< rucknium >__ I mean, it was amn 18-block reorg but they produced 20 blocks in that period     

> __< rucknium >__ an 18-block*     

> __< rucknium >__ That was 5% for a single attempt. And they have been attempting a lot.     

> __< rucknium >__ So, keep rolling the probability dice and you will succeed the the mining casino eventually.     

> __< rucknium >__ Probability computation was based on 66 minutes elapsing during the attack, according to block timestamps. And this R line: malicious.hashpower <- 0.4; pgamma(66, shape = 20, rate = 1/2 * malicious.hashpower)     

> __< rucknium >__ I'm pretty use that's the correct formula for this situation.     

> __< rucknium >__ pretty sure*     

> __< rucknium >__ Erlang distribution is a special case of the Gamma distribution.     

> __< bawdyanarchist:matrix.org >__ That looks surprisingly close to what I'm seeing in the sim. A ~20 block reorg could be possible about once per day (at ~33% selfish HP)     

> __< rucknium >__ Timing info based on https://github.com/WeebDataHoarder/Monero-Timeline-Sep14     

> __< rucknium >__ bawdyanarchist:matrix.org: Using the formula with 33% hashpower, I get a 20-block reorg with 50% every 1.53 days 😄     

> __< rucknium >__ Anyway, to the discussion about Helios-Selene parameter rigidity?     

> __< rucknium >__ I mean "with 50% probability every 1.53 days."     

> __< rucknium >__ I think my table scared kayabaNerve when I produced it last year. Maybe started him thinking about finality layers     

> __< sgp_ >__ Thanks Rucknium. Yes, I have an update on Helios-Selene     

> __< sgp_ >__ First, thanks to the community here for supporting the review of the curve selection, and of course a huge thanks to tevador for proposing the initial parameters and reviewing the latest discussions     

> __< kayabanerve:matrix.org >__ We can discuss it over email or here. Veridise noted our elliptic curves had am error in the selection script causing us to have to selected the third candidate, not the first, by accident. tevador corrected their script and issued a new gist above.     

> __< kayabanerve:matrix.org >__ One note is Veridise was also unhappy with our lack of twist security, despite the several reasons it's irrelevant, for the theoretical attack surface _and_ for the lack of reason _not_ to have a secure twist (as a later choice is functionally equivalent, with sufficiently-secure twist).     

> __< kayabanerve:matrix.org >__ I'd lean towards adding the requirement of a secure twist primarily to appease reviewers (as we already have to change the curve's definition) and secondarily out of an abundance of caution.     

> __< sgp_ >__ ref: https://gist.github.com/tevador/4524c2092178df08996487d4e272b096?permalink_comment_id=5772654#gistcomment-5772654     

> __< sgp_ >__ So in summary, the old proposed curves are out, and a new one will need to replace it. So a discussion needs to happen in the near future which ones should be picked. And there are arguably 3 options, depending on how much we care about twist security     

> __< tevador >__ As I said in the email, adding twist security would only be for show. It would have exactly zero practical impact on the implementation or the security of FCMP.     

> __< tevador >__ The original search conditions call for D = -1571315, which is what my gist is currenly using.     

> __< kayabanerve:matrix.org >__ I largely agree BUT it the importance of show here is that we have a clearcut review, if we disagree with the reviewers on importance.     

> __< kayabanerve:matrix.org >__ Even if we think this is unnecessary, it satisfies the review process _which is of its own merit_, and I see no reason _not_ to pick the identified option which is functionally equivalent albeit with a secure twist.     

> __< rucknium >__ Downside of searching for parameters with twist security? Will this affect stressnet performance in any meaningful way?     

> __< kayabanerve:matrix.org >__ It does update our criteria, but we're already updating the chosen curve.     

> __< tevador >__ Downside: we'll probably need a new search script implementation. My sage script is too slow to reach the D values that provide twist security.     

> __< kayabanerve:matrix.org >__ The only downside is that:     

> __< kayabanerve:matrix.org >__ - We're adding a meaningless criteria due to peer pressure (pessimist view)     

> __< kayabanerve:matrix.org >__ - We're changing our search criteria, but we're already changing the chosen result anyways     

> __< kayabanerve:matrix.org >__ None of this is of meaningful consequence to the implementation nor of any consequence to the performance     

> __< kayabanerve:matrix.org >__ tevador: They're only 5x bigger IIRC     

> __< kayabanerve:matrix.org >__ We can just run it 5x as long /s but not /s     

> __< jberman >__ One marginal benefit may be that others may have desire to use the curves for some other reason, and twist security may be relevant for them, which may lead to greater adoption / higher scrutiny on the libs     

> __< tevador >__ About 20x bigger.     

> __< kayabanerve:matrix.org >__ One moment     

> __< tevador >__ Than the correct one.     

> __< tevador >__ -1.5M vs -30M     

> __< kayabanerve:matrix.org >__ We prior chose     

> __< kayabanerve:matrix.org >__ 7857907     

> __< kayabanerve:matrix.org >__ We're now discussing     

> __< kayabanerve:matrix.org >__ 31750123     

> __< kayabanerve:matrix.org >__ That's 4x bigger that the prior choice.     

> __< tevador >__ or 92M was the other option.     

> __< kayabanerve:matrix.org >__ The fact the new selection is 5x faster to find shouldn't be considered relevant at this the IMO.     

> __< kayabanerve:matrix.org >__ Clarifying: finding curves only matters to reproduce our academia and justify our decision.     

> __< tevador >__ I think my original search ran for 1-2 days btw.     

> __< tevador >__ With 8 or 16 cores? Not sure.     

> __< tevador >__ Veridise seem to have a faster implementation.     

> __< kayabanerve:matrix.org >__ So it'll take a week in the future. That's unfortunate but acceptable.     

> __< sgp_ >__ Nothing else from me on this, other than to say if this interests you, please let me know. I'll keep talking with these two after the meeting     

> __< rucknium >__ Can this be run on the Monero Research Computing Cluster?     

> __< rucknium >__ Or just a single machine on that cluster?     

> __< tevador >__ Also adding "useless" search conditions can be seen as weakening the rigidity.     

> __< tevador >__ It would also be possible to remove the Crandall condition (which AFAIK we are not using anyways), then the result would be D = -15203.     

> __< rucknium >__ I will end the meeting here. Feel free to continue discussing. Thanks everyone.     

> __< sgp_ >__ Thanks rucknium     

> __< kayabanerve:matrix.org >__ No, current reductive algorithms take advantage of how 2**256 is congruent to a 128-bit value.     

> __< kayabanerve:matrix.org >__ I agree adding arbitrary conditions weakens rigidity. I don't believe this is reasonable to declare so arbitrary.     

> __< tevador >__ OK. So I think we can narrow it down to -1571315 or -31750123.     

> __< kayabanerve:matrix.org >__ Agreed     

> __< articmine >__ jeffro256: ... and how do you propose to tell ham and spam apart?     

> __< articmine >__ The answer is you can't.      

> __< articmine >__ What has worked is the current fees.      

> __< jeffro256 >__ The same way we've done it before: with fee pricing. We assume that spam is not "worth it" after a certain monetary amount, even though we can't actually discern spam. Generally, I think that we should penalize miners who expand the blocks past the current average weight. The miners will pass those costs onto the transaction c [... too long, see https://mrelay.p2pool.observer/e/xueFt7gKLUZkOHhE ]     

> __< articmine >__ Which is why I am not going to support a penalty free zone below 100x the reference transaction size. This is the current situation and it just works.      

> __< jeffro256 >__ Increasing the minimum penalty free zone is sort of orthogonal here, is it not? The actual limit doesn't really affect the argument AFAICT; we should either be pricing transactions as a quadratic function of their weight, or as a quadratic function of the total expected txs weights in a block.      

> __< articmine >__ jeffro256: Which is what my proposal does.  If we kept the maximum number of inputs at 8 or less, as was originally proposed then we could have kept the old way.     

> __< articmine >__ The only reason it has worked in the past is because we were way below the penalty free zone, so uneconomic large transactions got mined.     

> __< articmine >__ If a node relays transactions that are not economical to mine, and we are close to the top of the penalty free zone, we are simply setting up the stage for  DDDS attack with perfectly valid not economical transactions.[... more lines follow, see https://mrelay.p2pool.observer/e/5-3Gt7gKcG5iZGs2 ]     

> __< articmine >__ Of course the miners get penalized for growing the block weight. This does not change. Of course users are  incentivized to consolidate transactions. This now works because those consolidated transactions will get mined     

> __< articmine >__ The fee per input for my proposal once the membership proof weights are factored in is now lower for a larger number of inputs.  This was not the case before if we were close to or above the penalty free zone      

> __< articmine >__ I am for keeping fees to the minimum requirement for scaling.      

> __< articmine >__ What my proposal does is reduce the penalty for the large transactions not increase the fee     

> __< hinto >__ boog900:monero.social jeffro256:monero.social: sorry, missed the meeting, I am the one interested in PoWER     

> __< DataHoarder >__ 20:54:02 <rucknium> DataHoarder: Could you discuss your empirical findings about Qubic's selfish mining profitability?     

> __< hinto >__ for per connection PoW, can't an attacker build up connections then start spamming high input transactions practically for free?     

> __< boog900 >__ hinto: we disconnect on the first invalid tx      

> __< DataHoarder >__ the TL;DR: they were 82% efficient when selfish mining, but they improved and got 90% efficient. Efficiency was calculation of how good selfish mining they were doing     

> __< hinto >__ the transactions being spammed are all valid     

> __< DataHoarder >__ basically, they lost more overall than if they'd be mining straightforward. they have been doing that recently and their earnings have increased     

> __< hinto >__ won't nodes with high connection counts have a disproportionate amount of new load?     

> __< DataHoarder >__ monero had a 5% edge on pure earnings compared if qubic was mining directly     

> __< boog900 >__ hinto: PoW is only protection against invalid txs      

> __< boog900 >__ otherwise fee/cost to build the tx is the protection      

> __< DataHoarder >__ now that they are not doing selfish and they fixed some of their block delays, their efficiency is close to 100% and get very few orphans     

> __< DataHoarder >__ before even when not doing selfish they got orphaned a lot     

> __< boog900 >__ hinto: PoW in only done for outbound connections, inbound you only have to verify which is very cheap      

> __< DataHoarder >__ last two days they only had one orphan, comparable to normal Monero network rates     

> __< hinto >__ what is the challenge? if it is time bounded and invalid PoW causes a ban, won't time gaps between nonces have to be accounted for?     

> __< boog900 >__ hinto: I think the handshake response message should include some random challenge bytes and then the peer should optionally respond with a PoW message if they want to send txs with more than 8 inputs      

> __< boog900 >__ the PoW message being a new P2P message      

> __< hinto >__ and for RPC?     

> __< hinto >__ boog900: what about nodes that relay frequently e.g. exchanges?     

> __< boog900 >__ hinto: I guess something similar, maybe 2 new endpoints for the challenge and the response?      

> __< boog900 >__ hinto: as long as the txs are valid it should be fine      

> __< boog900 >__ PoW is only done per connection not per tx      



# Action History
- Created by: Rucknium | 2025-09-23T23:08:52+00:00
- Closed at: 2025-10-07T22:56:35+00:00
