---
title: Monero Research Lab Meeting - Wed 08 October 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1278
author: Rucknium
assignees: []
labels: []
created_at: '2025-10-07T23:00:35+00:00'
updated_at: '2025-10-28T20:44:04+00:00'
type: issue
status: closed
closed_at: '2025-10-28T20:44:04+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Carrot follow-up audit](https://gist.github.com/jeffro256/12f4fcc001058dd1f3fd7e81d6476deb).

4. [Proof-of-Work-Enabled Relay ("PoWER")](https://github.com/monero-project/research-lab/issues/133).

5. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf). [Revisit FCMP++ transaction weight function](https://github.com/seraphis-migration/monero/issues/44).

6. [FCMP alpha stressnet](https://monero.town/post/6763165).

7. Mining pool centralization: [Temporary rolling DNS checkpoints](https://github.com/monero-project/monero/issues/10064), [Share or Perish](https://github.com/monero-project/research-lab/issues/146), and [Lucky transactions](https://github.com/monero-project/research-lab/issues/145).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1275 

# Discussion History
## Rucknium | 2025-10-11T15:51:32+00:00
Logs

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1278     

> __< rucknium >__ 1. Greetings     

> __< articmine >__ Hi     

> __< hinto >__ hello     

> __< rbrunner >__ Hello     

> __< jberman >__ waves     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< rucknium >__ jeffro256:monero.social: ping     

> __< jberman >__ me: mostly fcmp++/carrot alpha stressnet bug squashing / investigating     

> __< hinto >__ I've posted an implementation proposal for PoWER: https://github.com/monero-project/research-lab/issues/133#issuecomment-3377869740     

> __< rucknium >__ me: me: Helping get stressnet stressed. Squashed bugs in my R package to spam transactions on stressnet (https://github.com/Rucknium/xmrspammer). At least two other people are using it to spam. Keeping https://stressnetnode1.moneronet.info/ and https://stressnetnode2.moneronet.info/ collecting and displaying node performance data. Largest block so far was 10 MB in size AFAIK.     

> __< vtnerd >__ Me: still testing carrot integration in lws. The balance key, including spend tracking has been tested as working , but the subaddress+carrot balance key testing and integration is still on going. Should've be too bad     

> __< DataHoarder >__ me: updated own p2pool/monero libraries to support carrot/fcmp++ stressnet and provided some feedback on specific areas where p2pool might require changes (and changes were made, many thanks!). Made a light notes document for anyone making changes on mining related projects     

> __< DataHoarder >__ https://git.gammaspectra.live/P2Pool/consensus/src/branch/fcmp/monero/address/carrot/STRESSNET.md     

> __< jeffro256 >__ Howdy     

> __< rucknium >__ vtnerd:monero.social: Any thoughts about MyMonero shutting down?     

> __< articmine >__ Me working on the parameters for the sanity median.      

> __< articmine >__ Also researching un economical transaction attacks     

> __< 0xfffc >__ Hi everyone. Sorry for being late.     

> __< vtnerd >__ We've been wondering what they would do with carrot changes, the upgrade was going to be painful. I feel a little responsible for forging ahead with lwsf instead of upgrading their stack - otoh upgrading lwsf for carrot will be much easier because it hooks into monero codebase unlike mymonero     

> __< 0xfffc >__ Me: I was fighting with a syncing issue I had in stressnet. Will be involved this week on stressnet.     

> __< vtnerd >__ There's at least one lwsf based wallet in progress, but unclear whether it gets released, dtc     

> __< rucknium >__ 3. Carrot follow-up audit (https://gist.github.com/jeffro256/12f4fcc001058dd1f3fd7e81d6476deb).     

> __< rucknium >__ Anything about this item?     

> __< jeffro256 >__ No I think it can be closed now.      

> __< rucknium >__ 4. Proof-of-Work-Enabled Relay ("PoWER") (https://github.com/monero-project/research-lab/issues/133).     

> __< hinto >__ Some things left in my proposal are picking the target difficulty, and penalties for misbehaving nodes     

> __< articmine >__ My understanding is that PoWER was to be applied per connection      

> __< hinto >__ I also thought about only including a nonce in the challenge instead of including a recent block hash     

> __< jberman >__ Public RPC should expose it as an option as well     

> __< hinto >__ articmine:monero.social: it is     

> __< boog900 >__ hinto: yeah I would suggest that      

> __< articmine >__ Then only do it for large transactions?     

> __< boog900 >__ I would also make the nonce per connection      

> __< hinto >__ If it's a public API and it the transaction's input count is greater than POWER_INPUT_THRESHOLD (set to 8), then PoWER is mandatory in the proposal     

> __< articmine >__ jberman: I was referring to the above     

> __< jberman >__ "If it's a public API and it the transaction's input count is greater than POWER_INPUT_THRESHOLD (set to 8), then PoWER is mandatory in the proposal" -> this sgtm, spec makes it a little unclear in Interfaces section     

> __< jberman >__ I think just nonce no hash also sounds reasonable     

> __< DataHoarder >__ without a recent-ish hash these can be made well in advance, right?     

> __< DataHoarder >__ or nonce per connection that requires these to be calculated then     

> __< hinto >__ The point of the hash is to prevent building up PoW although with a large enough nonce (64 bits?) it should be okay?     

> __< DataHoarder >__ each hop would require that nonce for any large tx     

> __< boog900 >__ boog900: If you don't do this you allow multiple connections with 1 PoW solution      

> __< articmine >__ DataHoarder: Just ROC?     

> __< articmine >__ RPC     

> __< boog900 >__ hinto:monero.social: the nonce is the challenge right?     

> __< jberman >__ POWER_NONCE_WINDOW=60, POWER_NONCE_LEEWAY=1 -> as in, if a nonce is 100s old, it is accepted? but not if 130s?     

> __< hinto >__ yes     

> __< DataHoarder >__ RPC to node, this node then does PoW connections to other nodes... how do other nodes broadcast their txs? more PoW?     

> __< DataHoarder >__ they have to pay the price for someone making big txs -> they might as well drop all big txs     

> __< hinto >__ jberman:monero.social: yes, the previous could be accepted as leeway     

> __< DataHoarder >__ specially with dandelion++, where they spread it     

> __< articmine >__ The big TX price is paid by the wallet if it is RPC     

> __< boog900 >__ I don't think we need a LEEWAY or a timeout on a nonce if per connection      

> __< DataHoarder >__ if nonces can be reused per TX, that works. I'm talking about having it be per-connection     

> __< jberman >__ hinto: If the nonce has a max validity window of 120s, I don't see how block hash is better at preventing building up PoW unless I'm missing something     

> __< articmine >__ Correction Pubic RPC     

> __< articmine >__ Public      

> __< DataHoarder >__ but you can also submit txs via P2P, right?     

> __< boog900 >__ boog900: you can't build it up if you need to connect for your challenge first, unless I am missing something?      

> __< hinto >__ jberman: It must be a recent block hash, where as the nonce is just a integer that could be per-computed,  although this might be fine too since I think it will be infeasible to do so     

> __< jberman >__ boog900: if you allow lazy proofs on relay after making the initial connection, it seems to make sense     

> __< jberman >__ hinto: gotcha, might as well go for 128 bits of randomness imo     

> __< jeffro256 >__ One issue I see with a fixed nonce per daemon per time-frame: is it just as easy to open 1000 connections as it is 1. As soon as the PoW for that nonce for that timeframe is used, it can be reused for the other 999 connections.     

> __< hinto >__ boog900: The leeway is for the brief interim when the daemon refreshes its nonce, similar to OTP systems allow the previous code     

> __< boog900 >__ there is no need to refresh a nonce if it is per connection tho      

> __< boog900 >__ all connections have different nonces      

> __< hinto >__ hmm okay... that does make the RPC/ZMQ more complicated to implement, the current proposal is stateless on the daemon side     

> __< jeffro256 >__ Also: timing it around a moving window is clunky. The daemon should generate a symmetric secret on startup. Then have an endpoint where it issues new nonce every single request, returning a MAC-ed message with a challenge, timestamp, deadline, and difficulty target. If you can submit PoW for that specific challenge by the dead [... too long, see https://mrelay.p2pool.observer/e/-PHu8rwKeGNNcHZ1 ]     

> __< boog900 >__ we can always have different behavior for P2P/RPC PoWER     

> __< kayabanerve:matrix.org >__ Hello, sorry for being late, I received a time-sensitive email right and was replying as the meeting started. I have nothing I've worked on to publicly state yet other than more traditional development, and the hopes we'll have some paper work re: our Generalized Bulletproofs further touched up soon.     

> __< boog900 >__ but we are always going to need some sort of state to verify each connection has independent PoW     

> __< DataHoarder >__ you can make the randomness be tied to a local counter + incoming address details     

> __< articmine >__ Yes to avoid say 2000 connections using the same POW     

> __< DataHoarder >__ ip/port/other side id + local incrementing counter     

> __< articmine >__ BS company      

> __< articmine >__ Blockchain surveillance      

> __< DataHoarder >__ then you take a hash of this, that's the nonce, so you don't keep generating duplicates     

> __< boog900 >__ but you then need a counter which is state, right?      

> __< DataHoarder >__ or purely randomly generating it, would work as well, using both sides chosen entropy to agree on a nonce     

> __< DataHoarder >__ boog900: as a global counter to ensure it's not repeated, not per connection     

> __< hinto >__ jeffro256: would exposing that endpoint be an easy DoS vector?     

> __< jeffro256 >__ Shouldn't be. AES is pretty fast      

> __< hinto >__ I'm not sure how much impl complexity is okay for the wallet/vendor side it was kept simple     

> __< DataHoarder >__ anything other than deterministically calculating (hash this entropy) the nonce via connection parameters (and global randomness) would require state to be kept around, indeed     

> __< boog900 >__ DataHoarder: how would you keep track of what number you gave out?     

> __< boog900 >__ like if I keep responding to the PoW with the same number for the counter how would you tell its been used before?      

> __< DataHoarder >__ you know the incoming connection addr/port (and target port), you know your global randomnness (which may be changed depending on time, the counter), and getting the current nonce is H(connection || randomness || counter)     

> __< DataHoarder >__ you'd need to connect on same address/port with same origin IP and port. which in that case, the connection is not allowed     

> __< DataHoarder >__ (if peer id is kept, that is additional state)     

> __< boog900 >__ no what if I send a bad tx, then I can reconnect and send another tx with the same PoW      

> __< DataHoarder >__ aha. but that would ban the peer, right?     

> __< DataHoarder >__ bad tx     

> __< hinto >__ new nonce per unique connection does prevent PoW reuse, what would qualify as a "unique" connection?     

> __< hinto >__ I have thought about this too although couldn't an attacker send multiple transactions under a single IP?     

> __< DataHoarder >__ TCP connections are identified by the local ip/port + remote ip/port     

> __< boog900 >__ DataHoarder: true, I don't know how RPC would handle that but yeah      

> __< DataHoarder >__ the key part is involving the ip/port     

> __< DataHoarder >__ not just ip, as part of the nonce given out     

> __< articmine >__ hinto: No disconnect     

> __< boog900 >__ hinto: for P2P, txs are verified one at a time        

> __< DataHoarder >__ usually this source port is chosen randomly, so each connection on same ip would get different PoW nonces. In the case they reuse the same ip/port, this connection is not a valid TCP connection so it'd be refused     

> __< DataHoarder >__ this is assuming TCP is used.     

> __< DataHoarder >__ in case of Tor nodes, the ip/port combo is the local tor ip + random source port     

> __< DataHoarder >__ so to clarify, say you are running monero P2P or RPC on TCP 1.2.3.4:100, you get an incoming connection from 7.8.9.1:4567 . H(1.2.3.4:100 || 7.8.9.1:4567 || global random || global time counter) gives you the current connection nonce, like TOTP     

> __< DataHoarder >__ no other TCP connection can be concurrently active on the 1.2.3.4:100, 7.8.9.1:4567 pair     

> __< DataHoarder >__ if your node exposes multiple IP addresses or ports they could connect to the second ip/port, but that would also change the nonce     

> __< DataHoarder >__ regularly global time counter is increased like in TOTP > POWER_NONCE_WINDOW=60, POWER_NONCE_LEEWAY=1     

> __< DataHoarder >__ TOTP is 30, +-1     

> __< articmine >__ Is it possible here to get around a temporary ban after the first bad TX. I am not sure .     

> __< DataHoarder >__ so it's quite similar with those parameters, allow previous+current     

> __< DataHoarder >__ They could connect from a different ip, but that'd end up having to solve more PoW     

> __< boog900 >__ I'm not sure if this solves the complexity for hinto      

> __< boog900 >__ for p2p I think this is more complex      

> __< boog900 >__ but for RPC 🤷     

> __< hinto >__ If the scope keeps increasing, I think it would be a much simpler impl if it was PoW per TX     

> __< DataHoarder >__ RPC if connection is closed, it'd pick a different source port next connection. if connection is kept open (keep alive, or http/2) that'd allow multiple requests in     

> __< boog900 >__ rather than just generating a 16 byte value on connection and attaching it with the other connection details and using that for PoW      

> __< articmine >__ PoWER for bad node behavior in general can actually be very useful      

> __< articmine >__ No just a bad TX     

> __< boog900 >__ 👀     

> __< jberman >__ challenge/response dependent on network protocol I think is overly complex     

> __< jberman >__ single endpoint, add a little state per connection, I think is an acceptable level of complexity     

> __< DataHoarder >__ they are currently all TCP :)     

> __< articmine >__ I say trigger PoWER after:     

> __< articmine >__ 1) A significant time out      

> __< articmine >__ 2) Specific bad node behavior      

> __< DataHoarder >__ it could still be generated like this, or be state, I think how to generate this randomness can be left for out of meeting or later discussion, no? as long as we can guarantee for further topics that it is "unique" within relevant time periods     

> __< articmine >__ Or above      

> __< boog900 >__ For p2p we can pass in the handshake different values for difficulty depending on what the connecting node wants to do      

> __< boog900 >__ i.e. tx_relay_difficulty, minimum_difficulty etc     

> __< boog900 >__ but I would leave this for a later discussion       

> __< articmine >__ Yes      

> __< hinto >__ okay, I'll update the proposal further, I think we can move on     

> __< jberman >__ ty hinto     

> __< rucknium >__ 5. Transaction volume scaling parameters after FCMP hard fork (https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf). Revisit FCMP++ transaction weight function (https://github.com/seraphis-migration/monero/issues/44).     

> __< jberman >__ rucknium:monero.social: what was that huge block size on stressnet again?     

> __< rucknium >__ Almost 10MB     

> __< rucknium >__ http://stressgguj7ugyxtqe7czeoelobeb3cnyhltooueuae2t3avd5ynepid.onion/block/2850011     

> __< rucknium >__ ^ Tor browser required     

> __< jberman >__ 10MB blocks in <5 days of heavy stressing     

> __< rucknium >__ Mostly 1in/16out because of the spam pattern at the time.     

> __< rucknium >__ Penalty was almost completely used since I set those txs to highest fee.     

> __< articmine >__ My one comment here is that the penalty is quadratic with transaction weight. This leads to quadratic transaction fees with weight.      

> __< articmine >__ This being said the penalty does not have to be quadratic with number of  inputs, size, verification time etc      

> __< articmine >__ What happened with the 10 MB blocks?     

> __< articmine >__ On stressnet     

> __< jberman >__ Just saying on my end, 10MB block seems kind of high to me in less than a week     

> __< jberman >__ I still haven't had the chance to go through the latest proposal. But I'll be curious to see what max growth would look like under the latest     

> __< articmine >__ jberman: One actually needs ~20x factor to accomodate holiday shopping. This is the experience with VISA     

> __< articmine >__ At least before the advent of widespread delivery with a ~ week time factor      

> __< articmine >__ Delivery apps are like in store purchases here     

> __< rucknium >__ You can grow the block limit rapidly by paying high fees, which has happened on stressnet. When fees are set to their minimum, blocks grow very slowly.     

> __< jeffro256 >__ jberman: Tbf, last time I checked, the sum total of XMR in mempool fees was ~5.9 XMR, ~9.8x higher than block subsidy      

> __< jeffro256 >__ Normal fees are ~3% of block subsidy      

> __< articmine >__ So what is stopping stressnet is a lack of "spam"     

> __< articmine >__ To pay the fees      

> __< articmine >__ rucknium: That is by design     

> __< articmine >__ It also comes into play when one reaches the long term median cap     

> __< articmine >__ On the short term median      

> __< rucknium >__ AFAIK, on stressnet there have been three fee strategies. By default, my large-volume spam pays the min fee (tier 1). That level of fees can keep the txpool full and still fill blocks to their penalty-free limit so that the progress toward larger block sizes is not lost. ofrnxmr:monero.social 's spam pays tier 3 fees I think. [... too long, see https://mrelay.p2pool.observer/e/0_CU9LwKZHhhcmJI ]     

> __< rucknium >__ AFAIK, you would not get to 10MB blocks without paying very high fees. The 10MB block had fee total 10.8 XMR because most or all txs paid the tier 4 fee.     

> __< articmine >__ Are you limited by the amount of stressnet XMR?     

> __< rucknium >__ articmine:monero.social: It's manageable. Next stressnet, we should have a plan to systematically distribute XMR for spamming purposes.     

> __< DataHoarder >__ I can mine larger blocks by loss of profit but burning up base reward :)     

> __< rucknium >__ I have a lot of stressnet XMR because I had a lot of main-testnet XMR. And of course it transfer to the hard forked stressnet.     

> __< articmine >__ rucknium: Lower the difficulty on stressnet     

> __< rucknium >__ kico made a faucet, too     

> __< articmine >__ This may be issue here     

> __< rucknium >__ We are still in the scaling parameters agenda item     

> __< boog900 >__ surly you only need to pay as much XMR as the block reward spread across all txs to cause the block to increase?      

> __< boog900 >__ *cause the block to be the max size      

> __< articmine >__ Actually to max it out one needs 4x     

> __< articmine >__ The block reward      

> __< rucknium >__ https://faucet.xmr.pt/     

> __< DataHoarder >__ next time just 1000x reward :')     

> __< boog900 >__ articmine: ah ok      

> __< rucknium >__ Should we move on to the stressnet agenda item?     

> __< articmine >__ Realistically we should be looking at BSV max transactions rates to test this out      

> __< articmine >__ Sure     

> __< rucknium >__ 6. FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< rucknium >__ Several bugs have been identified already. Some fixed.     

> __< jberman >__ Will be pushing a fix for the edge case you identified of 2 block reorg immediately after wallet creation today, continuing investigation into connection issues that mostly seem to revolve around brushing up against byte size limits     

> __< jeffro256 >__ I'm currently looking into the higher-than-expected memory usage      

> __< articmine >__ https://coingeek.com/152-million-transactions-in-a-day-another-new-record-for-bsv/     

> __< rucknium >__ The FCMP transaction CPU verification efficiency has exceeded my expectations :)      

> __< articmine >__ rucknium: Still on a single thread?     

> __< rucknium >__ articmine: articmine:monero.social: Higher tx volume than now is possible, but nodes are already having connectivity issues, so it make not be useful to push it beyond where it is now.     

> __< articmine >__ What kind of bandwidth per node?     

> __< jberman >__ Could be wrong here, but seems like blocks the past day or so have been smaller than before. Some problems w/byte size limits trigger around 4mb, but it seems like people are still having connectivity issues the past day even though blocks haven't been that big?     

> __< rucknium >__ Yes, still single-threaded AFAIK. But, not too much worst than last year's RingCT stressnet, byte-for-byte. Of course, FCMP txs are larger than RingCT, so tx-for-tx it is much worse.     

> __< rucknium >__ jberman:monero.social: txpool is larger. I think that's the problem.     

> __< articmine >__ How is TX pool stored     

> __< rucknium >__ Yesterday, block size ran up and then the txpool was exhausted. That sends the block limit lower once the 100-block trailing median falls.     

> __< rucknium >__ articmine: We still have the mainnet tx relay that sends the whole tx to every peer. Bandwidth is a lot.     

> __< articmine >__ So then what are the limitations?     

> __< jberman >__ bugs     

> __< spackle >__ I'd like to briefly highlight the txpool self-limiting. It is visible on Rucknium's monitor node.     

> __< rucknium >__ And preventing different threads from blocking each other. I want to get cuprate on the next stressnet for a RingCT stress to compare.     

> __< jberman >__ spackle: that one has been on my list to tackle for a bit     

> __< rucknium >__ I think for next FCMP stressnet, the new tx weight and scaling parameters need to be implemented and PoWER.     

> __< rucknium >__ 0xfffc:monero.social and boog900:monero.social 's tx relay efficiency implementation could be good to test in the stressnet, too.     

> __< jberman >__ Worth mentioning, the issues we're seeing now for the most part don't seem to stem from FCMP++ (except that obvious reorg bug)     

> __< articmine >__ rucknium: I expect this to have a significant impact     

> __< rucknium >__ There was no complete network chaos and netsplits like the beginning of last year's stressnet. The main problems that caused that have been fixed AFAIK.     

> __< rucknium >__ jberman: jberman:monero.social: Good point to mention :)     

> __< jberman >__ tx weight and scaling 100%, I don't think PoWER is a requirement. PoWER is mostly a DDoS repellent, not expected to have an impact on node perf > <rucknium> I think for next FCMP stressnet, the new tx weight and scaling parameters need to be implemented and PoWER.     

> __< rucknium >__ More about stressnet? Stressnet discussion happens in #monero-stressnet:monero.social  on Matrix and ##monero-stressnet on Libera IRC.     

> __< articmine >__ I would not use PoWER on stressnet, at least for now      

> __< rucknium >__ 7. Mining pool centralization: Temporary rolling DNS checkpoints (https://github.com/monero-project/monero/issues/10064), Share or Perish (https://github.com/monero-project/research-lab/issues/146), and Lucky transactions (https://github.com/monero-project/research-lab/issues/145).     

> __< rucknium >__ Qubic did some selfish mining recently. Any more comments, DataHoarder?     

> __< DataHoarder >__ Not more comments other than they seem to get more hashrate recently (1.8 GH/s) but then also went down     

> __< DataHoarder >__ they stopped selfish mining now.     

> __< rucknium >__ DNS checkpoints implementation is stalled because of a edge case bug that is being tracked down. AFAIK, 0xfffc:monero.social  was working on it.     

> __< rucknium >__ I can't debug C++, so I cannot help there.     

> __< rucknium >__ I don't know how to push it toward completion. I think other devs either don't want to get distracted from their current work to try to finish implementing rolling DNS checkpoints, or don't fully agree with the approach. Or they agree but don't want to get blamed if it's deployed and something goes wrong 😉     

> __< rucknium >__ Or are maybe like tevador and agree with the approach, but only wants to code in clean pure C instead of getting into dirty C++ 😛     

> __< rucknium >__ Once stressnet can "coast", I hope to look more closely at Share or Perish, especially trying to implement a Markov Decision Process to analyze it.     

> __< rucknium >__ Any more discussion on this agenda item?     

> __< bawdyanarchist:matrix.org >__ I have preliminary results for selfish mining simulation under realistic network modeling and difficulty adjustment, sweeping through a range of permutations (strategies) they could use.     

> __< DataHoarder >__ 20:40:29 <rucknium> I can't debug C++, so I cannot help there.     

> __< DataHoarder >__ I tried to reproduce, but I don't have a proper repro case     

> __< bawdyanarchist:matrix.org >__ Ready to pubish, but I'm not sure if it's the best idea to give Qubic free analysis on which strategies are best for network disruption. It might not be real problem, but I thought I'd at least ask the question before publishing     

> __< rucknium >__ bawdyanarchist:matrix.org: How does it compare to results already published in the literature? Is the difference that you consider difficulty adjustment, but MDP papers do not?     

> __< bawdyanarchist:matrix.org >__ In terms of profitability, simulation corroborates the Eyal-Sirer (classic) selfish mining MDP, but diverged from the stubborn mining publication. The simulation models realistic network delays and difficulty adjustment. Gamma for example, is an output of the sim, not an input. Honest forks are created by modeled latency, as opposed to heuristics.     

> __< rucknium >__ Is this the first research where gamma is endogenous?     

> __< bawdyanarchist:matrix.org >__ As far as I'm aware, yes.     

> __< rucknium >__ (Endogenous means that the variable is determined inside the system, not a variable of the system that is assumed to have a particular value.)     

> __< spirobel:kernal.eu >__ what is this held back by now? https://github.com/monero-project/monero/pull/10075#discussion_r2407941460 saw this comment regarding monotonic time vs wall clock > <rucknium> DNS checkpoints implementation is stalled because of a edge case bug that is being tracked down. AFAIK, 0xfffc:monero.social  was working on it.     

> __< bawdyanarchist:matrix.org >__ When running with purely honest hashpower, and ping set at 70ms, I'm replicating Monero's natural fork rate, at about 0.24%. This is running with 9 total pools, mirroring hashrate distirbution we normally see.     

> __< bawdyanarchist:matrix.org >__ And yes, gamma is a derivative of the simulation, a byproduct of stochastic latency     

> __< rucknium >__ Maybe share it with me and DataHoarder. We (especially DataHoarder) can evaluate the risk of Qubic getting useful info from the research. Others could help, too.     

> __< rucknium >__ spirobel:kernal.eu: A specific sequence causes nodes that enforce checkpoints to fail to sync new blocks.     

> __< bawdyanarchist:matrix.org >__ Yes, I think it would be good for at least one other person to take a look privately first. The report is ready to go, and not terribly long.     

> __< DataHoarder >__ I can take a look 👍. Qubic already implemented other countermeasures from previous public discussions so they should be delayed (a reasonable time, not forever) until bandaid is there     

> __< rucknium >__ Sounds good to me. Thank you, bawdyanarchist:matrix.org , for working on this! It should be interesting.     

> __< rucknium >__ Any more discussion?     

> __< spirobel:kernal.eu >__ rucknium: so a second PR is necessary to address this part ? quoting ofrnxmr from the PR description here: Note: there is an issue unrelated to the PR that can leave nodes in a bad state     

> __< spirobel:kernal.eu >__ Node is reorged     

> __< spirobel:kernal.eu >__ Node receives a checkpoint that references the now orphaned chain[... more lines follow, see https://mrelay.p2pool.observer/e/kpfP9bwKa185UE53 ]     

> __< rucknium >__ spirobel:kernal.eu: Yes, I think that is it. It would be great if you wanted to help :D     

> __< rucknium >__ ofrnxmr:monero.social  , DataHoarder, and I could get the sequence running again on testnet     

> __< DataHoarder >__ in a bit. I tried attacking myself as well     

> __< spirobel:kernal.eu >__ rucknium:monero.social: i am busy with wallet code. Not going to promise anything :D     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< spirobel:kernal.eu >__ the logic of handling checkpoints should be separated from handling reorgs because of longest chain rule. It seems like part of the struggle is that those two consensus rules are intermingled.      

> __< spirobel:kernal.eu >__ This should also be a topic interesting for kaya as the same situation would apply to the finality layer      

> __< articmine >__ Thanks      

> __< spirobel:kernal.eu >__ my understanding is, (correct me if I am wrong) that a finality layer would be a more decentralized version of checkpointing. So practically its important to figure out the logic of this codepath and how to untangle it.      

> __< 0xfffc >__ https://github.com/monero-project/monero/pull/9933#issuecomment-3382892067      

> __< ofrnxmr >__ spirobel:kernal.eu: Yeah. There is 2 different codepaths that handle the reorg. The first goes through the conditions on L2090 of blockchain.cpp, and i believe the first is_a_checkpoint should be triggering here. But it always evaluates as false     

> __< ofrnxmr >__ The latter (i dont remember where it is) causes the chain to roll back to a block before the checkpoint (instead of switching to the alt chain that has the checkpoint). After which the node blocks a) incoming blocks that dont match the checkpoint b) incoming blocks that do match the checkpoint, but are orphaned c) newly mined blocks, because they dont match the checkpoint     

> __< ofrnxmr >__ Forcing is_a_checkpoint = true, seems to solve the issue. So thats as far as i understand whats going on     

> __< spirobel:kernal.eu >__ ofrnxmr: the logic really shouldnt be in this function as these two things are not related. Longest chain rule is normal operation, while checkpointing is above that. It is a separate rule so why should it be handled in the same function?      

> __< spirobel:kernal.eu >__ also we are in big trouble btw if the 6 dns domains give conflicting checkpoints. Are there measures in place to prevent this and assure there is consensus among the checkpointing nodes?      

> __< rucknium >__ The checkpointing script serves the same checkpoints to all domains. The only problem can happen with DNS record latency. If a supermajority of records received by a node that enforces the checkpoints don't match, then the node just doesn't bind the checkpoint.     

> __< spirobel:kernal.eu >__ We also have to separate here between nodes that miners operate and nodes that users rely on. Checkpointing is a tool for honest hashrate to coordinate and form the longer chain, even if a malicious party with a large amount of hashrate tries to disrupt the network.      

> __< spirobel:kernal.eu >__ Another aspect is that currently the blocking behavior is intermingled with this as well. We have 3 topics that need to get untangled: the two consensus rules and blocking behavior.      

> __< ofrnxmr >__ spirobel:kernal.eu: They have to be 2/3+1 agreeing before the node accepts them     

> __< ofrnxmr >__ So, in practice, 5/7 have to match     

> __< DataHoarder >__ 22:13:08 <spirobel:kernal.eu> also we are in big trouble btw if the 6 dns domains give conflicting checkpoints. Are there measures in place to prevent this and assure there is consensus among the checkpointing nodes?      

> __< DataHoarder >__ they will never set checkpoints that do not have previous checkpoint as part of their chain     

> __< bawdyanarchist:matrix.org >__ rucknium:monero.social: DataHoarder  I DM'd you with the link to a private github repo with the report.     

> __< datahoarder >__ You probably need to DM me bawdyanarchist:matrix.org     

> __< DataHoarder >__ This user is in IRC     

> __< DataHoarder >__ So send to the Monero.social one (funny how the bridge makes that work so well)     




# Action History
- Created by: Rucknium | 2025-10-07T23:00:35+00:00
- Closed at: 2025-10-28T20:44:04+00:00
