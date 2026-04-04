---
title: Monero Research Lab Meeting - Wed 15 October 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1281
author: Rucknium
assignees: []
labels: []
created_at: '2025-10-14T22:01:33+00:00'
updated_at: '2025-10-28T20:34:17+00:00'
type: issue
status: closed
closed_at: '2025-10-28T20:34:17+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Proof-of-Work-Enabled Relay ("PoWER")](https://github.com/monero-project/research-lab/issues/133).

4. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf). [Revisit FCMP++ transaction weight function](https://github.com/seraphis-migration/monero/issues/44).

5. [FCMP alpha stressnet](https://monero.town/post/6763165).

6. Mining pool centralization: [Temporary rolling DNS checkpoints](https://github.com/monero-project/monero/issues/10064), [Share or Perish](https://github.com/monero-project/research-lab/issues/146), and [Lucky transactions](https://github.com/monero-project/research-lab/issues/145).

7. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1278 

# Discussion History
## hinto-janai | 2025-10-28T19:33:31+00:00
@Rucknium I think PoWER can be removed for now, only small implementation details are left.

Sorry if it took too much time in the meetings.

## Rucknium | 2025-10-28T20:34:17+00:00
Logs

> __< jberman >__ I'll have limited availability in today's meeting unfortunately. I've been working pretty much exclusively on FCMP++ & Carrot stressnet issues. Repeating from last week, the issues we're seeing mainly seem to stem from existing issues in monerod. The FCMP++ & Carrot integration has had some hiccups, but for the most part the integration seems to be holding up well with hiccups patched     

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1281     

> __< rucknium >__ 1. Greetings     

> __< articmine >__ Hi     

> __< jeffro256 >__ Howdy     

> __< jeffro256 >__ jberman: I can second this, he's been working like a dog ;) I've also been working on working on existing issues in monerod which the stressnet exposed     

> __< hinto >__ hello     

> __< vtnerd >__ Hi     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< jeffro256 >__ It's been very interesting to say the least, and definitely highlights the importance of fixing existing issues of efficient transaction/block propagation b/c it'll be needed more than ever with 4x bigger txs     

> __< rucknium >__ me: Keeping stressnet stressed. Keeping stressnet infrastructure (e.g. https://stressnetnode1.moneronet.info/ , https://stressnetnode2.moneronet.info/ , and seed nodes) alive and well.     

> __< hinto >__ me: PoWER and looking into ZMQ for Cuprate     

> __< vtnerd >__ me: legacy and balance keys now fully work in lws. Now working on an official docker image, as btcpayserver really needs it     

> __< jeffro256 >__ Yay!     

> __< articmine >__ Me working on a write-up on the penalty and scaling.      

> __< rucknium >__ 3. Proof-of-Work-Enabled Relay ("PoWER") (https://github.com/monero-project/research-lab/issues/133).     

> __< hinto >__ I've updated my proposal from last meeting: https://github.com/monero-project/research-lab/issues/133#issuecomment-3377869740     

> __< hinto >__ The P2P interface is slightly different than RPC/ZMQ, it's a 1-time challenge/solution exchange     

> __< hinto >__ The RPC/ZMQ endpoint provides unique challenges per connection and holds them until an expiry time, solutions are verified at other TX relaying endpoints; these could be cleared occasionally or maybe cleaned if set.size() >= POWER_MAX_ACTIVE_NONCES     

> __< hinto >__ Unique connections are still left undefined but I think this can be decided elsewhere, for now I assuming some network details     

> __< jeffro256 >__ Maybe I'm misunderstanding the proposal, but keeping a finite set of valid certificates is a DoS vector      

> __< boog900 >__ I still believe requiring RPC connections to be held for PoW is fine      

> __< boog900 >__ And simplifies the protocol a lot      

> __< hinto >__ jeffro256: If there is no limit the node's memory can be exhausted     

> __< jeffro256 >__ The protocol shouldn't require holding potential certificates in the first place      

> __< jeffro256 >__ It should be holding already completed PoW only     

> __< boog900 >__ Wallet2 and monero-oxide both hold rpc connections     

> __< hinto >__ jeffro256: Doesn't there have to be a limit on this as well?     

> __< jeffro256 >__ Yes, but the attacker would have to do X seconds of PoW to store 16 bytes on your machine     

> __< DataHoarder >__ if this certificate/check can be generated from the connection details, it'd not be any extra data other than connection itself, bounded by connection limit     

> __< hinto >__ boog900: FYI this would bypass the state problems, RPC could exchange like P2P/ZMQ     

> __< DataHoarder >__ even if it has to store x bytes, it'd be bounded by connection limit     

> __< jeffro256 >__ And worst case scenario, they get to re-use PoW for a separate connection after doing many, many thousand of iterations of PoW. Whereas worst case scenario w/ your current proposal is that connections doing 0 PoW can lock out honest peers      

> __< hinto >__ Ok I see, I misunderstood the idea, I think that's acceptable     

> __< boog900 >__ hinto: It only means people who don't hold RPC connections can't relay >8 input txs     

> __< jeffro256 >__ The cert also needs to be signed (preferably symmetrically for performance) by the validating node, otherwise the attacker can make up challenges in advance      

> __< vtnerd >__ I guess lws gets to pass power along to client wallets? Otherwise the server has to do it which isnt ideal     

> __< articmine >__ What kind of expiry on the cert?     

> __< jeffro256 >__ In other words, creation of challenges should be stateless (besides the node's permanent signing keys), otherwise it poses a DoS vector to honest peers. The onus of storing ones's own validation information should be on the proving peer     

> __< DataHoarder >__ 19:19:43 <jeffro256> The cert also needs to be signed (preferably symmetrically for performance) by the validating node, otherwise the attacker can make up challenges in advance      

> __< DataHoarder >__ (I again bring up TOTP as an example of how challenges could be computed with a time factor on the go, based on an agreed "secret" information)     

> __< boog900 >__ Is there an issue I am not seeing by requiring people to hold RPC connections?      

> __< hinto >__ jeffro256: Is this necessary on a 128-bit nonce?     

> __< jeffro256 >__ DataHoarder: But why share secret information when secret information does not need to be shared?     

> __< DataHoarder >__ the TOTP result is shared     

> __< boog900 >__ boog900: Wallet2 does it, monero-oxide does it. If we think this is acceptable, then we don't need to handle certificates, used nonces etc     

> __< hinto >__ articmine: I think 1-5 minutes from the request would be okay     

> __< DataHoarder >__ not the secret part     

> __< DataHoarder >__ the agreed secret part doesn't specifically need to be sent over, it can be incoming connection details + local random secret     

> __< DataHoarder >__ to re-verify the TOTP() of this you just need the connection details + time it was generated at     

> __< articmine >__ hinto: That makes sense     

> __< jeffro256 >__ hinto: In my stateless proposal, yes. Not necessary in your proposal since it's infeasible to guess a 128-bit nonce generated on a node you don't operate     

> __< DataHoarder >__ that'd generate a nonce (of however many bits) you can verify when the proving peer brings back a PoW result (along with the above^)     

> __< jeffro256 >__ DataHoarder: How would the prover know your local random secret without asking you?     

> __< jeffro256 >__ DataHoarder: This is susceptible to front-loading attacks      

> __< DataHoarder >__ they don't, the prover doesn't run TOTP     

> __< DataHoarder >__ local node, when RPC connection that must be verified comes in, returns result of TOTP(details | secret | time) + time     

> __< jeffro256 >__ So the prover still has to request a challenge, yes?     

> __< DataHoarder >__ yes, but this challenge doesn't need storage by node     

> __< DataHoarder >__ it's also limited in time directly (As you get time when prover returns PoW, and can instantly remove these)     

> __< jeffro256 >__ Okay then I think we're talking about the same thing      

> __< syntheticbird >__ boog900: i love how no one answered you probably because they have doubt in mind but don't manage to put words on it.     

> __< syntheticbird >__ (i see no issue)     

> __< jeffro256 >__ boog900: Sorry, what specific actors you do mean by "people" and RPC to which software?     

> __< boog900 >__ Wallets holding RPC connections to monerod      

> __< boog900 >__ If we think this requirement is OK then we can just generate a random nonce on connection like we will do for P2P     

> __< jeffro256 >__ I think it should be optional, especially for local nodes. But I'm okay with supporting PoW for wallet->daemon connections, specifically for transaction submission endpoints      

> __< DataHoarder >__ as I suggested last time it's maybe better to have out of meeting conversations, but isn't it generally that 1) node must be able to generate challenges and not keep per-challenge state (single global state is ok as it's fixed byte size)  and 2) the prover must not be able to generate new nonces ahead of time (or collect too many without a defined     

> __< DataHoarder >__ expiration date) and 3) valid nonces for PoW have to expire after a defined amount      

> __< jeffro256 >__ I wouldn't support it for other endpoints      

> __< DataHoarder >__ unrestricted RPC could have it disabled, restricted RPC enabled?     

> __< boog900 >__ It would still work the same as your proposals, with an endpoint to get the challenge and an endpoint to submit      

> __< boog900 >__ Its just the challenge is for a specific connection so you cannot disconnect then reconnect and submit      

> __< hinto >__ DataHoarder: PoWER is skipped on local/trusted interfaces     

> __< jeffro256 >__ DataHoarder: Agreed. State per success-post-verification is okay though, and is probably necessary. But yeah further implementation details of the exact should probably be discussed on the Github issue, not in here      

> __< DataHoarder >__ post verification is bounded to RPC connection limits, so reasonable data usage there would be fine as it comes with a bound     

> __< jeffro256 >__ Not just RPC connection limits, but PoW recently performed      

> __< DataHoarder >__ Right. RPC connects/disconnect (doesn't keep TCP connection open) so ports are not relevant.     

> __< DataHoarder >__ If given expiration explicitly via generation these can be kept exactly as long as needed then removed away      

> __< boog900 >__ Tbf me and hinto have discussed it and he thought it would be unpopular to require wallets to hold connections.     

> __< boog900 >__ I disagree though and can't see an issue, it would simplify the protocol a lot.     

> __< jeffro256 >__ Oh hold connections?     

> __< jeffro256 >__ Yeah I wouldn't want to implement it like that      

> __< jeffro256 >__ It would probably break a lot of app developers' flows      

> __< jeffro256 >__ Just do PoW when submmiting a tx      

> __< boog900 >__ Wallet2 and monero-oxide both hold connections     

> __< boog900 >__ jeffro256: As long as you can do more than 1  request per connection you can still do this     

> __< vtnerd >__ one issue I’m seeing is with ZMQ router/dealer stuff. you can’t use those setups with PoWER probably     

> __< vtnerd >__ I dont know of anyone using those setups though     

> __< boog900 >__ jeffro256: Fwiw they will still work as long as you don't send a > 8-input tx     

> __< jeffro256 >__ boog900: Is wallet2 really doing that? Hmmm... Probably not ideal for remote node privacy     

> __< DataHoarder >__ alternatively have send_raw_transaction allow a list of transactions :)     

> __< hinto >__ FWIW I agree it would simplify everything, although agree with jeffro     

> __< boog900 >__ jeffro256: Why? Better than reconnecting for every request     

> __< articmine >__ boog900: Which is not a serious issue     

> __< hinto >__ I think we can further discuss on the issue, should we move on?     

> __< jeffro256 >__ boog900: Why would re-connecting ever be worse for privacy? Re-connecting means that RPC requests from different wallets with the same host have some mixing. It's not much, but it's something      

> __< boog900 >__ jeffro256: True but that's minimal and breaks my RPC PoWER idea D:     

> __< rucknium >__ 4. Transaction volume scaling parameters after FCMP hard fork (https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-07.pdf). Revisit FCMP++ transaction weight function (https://github.com/seraphis-migration/monero/issues/44).     

> __< articmine >__ Any questions on this?     

> __< articmine >__ In particular the square root weights     

> __< articmine >__ ...and quadratic fees     

> __< articmine >__ Seeing none I will continue with my writeup and suggest we move on     

> __< jeffro256 >__ For the record, I still NACK for the same reasons as last week, I just don't have anything new to add at the moment     

> __< rucknium >__ 5. FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< rucknium >__ There was a new stressnet release, version 1.2: https://github.com/seraphis-migration/monero/releases     

> __< rucknium >__ With large blocks, nodes are having problems staying connected. The release fixes a minor cause of the connection problems, but many more remain.     

> __< jeffro256 >__ Working through issues at the moment. Is there any specific issue someone wants to bring up or re-iterate?     

> __< rucknium >__ I am glad that you and jberman are invested in this stressnet ;)     

> __< rucknium >__ As you said, many of the issues are longstanding monerod issues, not specifically FCMP issues     

> __< rucknium >__ And we saw most of them on last year's stressnet     

> __< rucknium >__ Last year's stressnet just fixed the truly fatal issues, like irreparable netsplits.     

> __< mayhem69:matrix.org >__ I'm not sure if its an existing issue with monerod or with the stressnet version but these bans that are happening on stressnet are causing connectivity issues between peers:     

> __< mayhem69:matrix.org >__ https://github.com/seraphis-migration/monero/issues/180     

> __< rucknium >__ AFAIK, there is no easy way to clear all of your nodes' bans without restarting the node.     

> __< rucknium >__ Can some console command and/or RPC method be written to clear all bans?     

> __< rucknium >__ Even better, write something that can clear bans by CIDR subnet notation. Then you can clear all bans with a large CIDR, but clear specific subnets, too.     

> __< mayhem69:matrix.org >__ There is a script on of the guys made to clear the bans via the RPC which works but covers up the cause of the bans. If the bans are legit and supposed to happen then that is fine, the script that be used to clear the bans periodically.      

> __< DataHoarder >__ get_bans already exists, and set_bans as well. set_bans with ban: false should unban?     

> __< DataHoarder >__ could make something that is CIDR aware     

> __< jeffro256 >__ There's this script which I haven't tested yet: https://github.com/seraphis-migration/monero/issues/180#issuecomment-3405320886     

> __< jeffro256 >__ No idea if it works or not      

> __< jeffro256 >__ rucknium: This would be nice      

> __< mayhem69:matrix.org >__ Yes that is the script and its using get_bans and set_bans and it seems to resolve the issue. Just figured I would bring it up b/c it is annoying to have unban to get connectivity and not everyone running a node is doing so and as such I find my node gets isolated from the network quite often.      

> __< mayhem69:matrix.org >__ Anyway if this is expected behavior then that is fine. Just figured I would bring it up in case its not.      

> __< rucknium >__ An external script is useful, but having a dedicated way to do it would help ordinary stressnet users     

> __< rucknium >__ No, the bans aren't supposed to happen, but they do because nodes think you are misbehaving when the network has heavy load.     

> __< jeffro256 >__ Might be more serialization issues. We're looking into it. Better logging is a must going forward IMO      

> __< rucknium >__ IIRC, on last stressnet, the ban timeout was set low manually in a stressnet PR     

> __< jeffro256 >__ Or other levin limits      

> __< jeffro256 >__ rucknium: That could be done here      

> __< rucknium >__ Logging can stress a node too, AFAIK. That's double stress :D     

> __< spirobel:kernal.eu >__ aren't the bans cleared on restart? > <rucknium> Can some console command and/or RPC method be written to clear all bans?     

> __< rucknium >__ spirobel:kernal.eu: Yes, but often you don't want to restart.     

> __< rucknium >__ Last stressnet, restarting was very annoying since the node re-validated the entire txpool on restart. That's fixed for this one.     

> __< rucknium >__ I had a few out-of-memory crashes on an 8-GB RAM VPS with log level 2.     

> __< mayhem69:matrix.org >__ yes I notice bans occuring even when there is much load, seems to happen on my node when its syncing. And then its exacerbated b/c my node will try to connect to a node multiple times where I am banned and then my node bans then and its just a death spiral of bans.  I will try to add more info to the issue as I find it but I a [... too long, see https://mrelay.p2pool.observer/e/4tbFlL8KblM1WXNu ]     

> __< rucknium >__ Here it is: https://github.com/spackle-xmr/monero/pull/7 "Peer ban duration to 2 minutes"     

> __< jeffro256 >__ Will add to v1.3 TODO list      

> __< jeffro256 >__ thanks     

> __< rucknium >__ Is there a specific goal with stressnet debugging, such as "network can smoothly handle txpool size X and block size Y"?     

> __< spirobel:kernal.eu >__ rucknium: would it make sense to split the concept of peer bans from an exponential back off? usually in a distributed system you would do an exponential back off when a queue gets overloaded.      

> __< rucknium >__ This isn't the final FCMP stressnet, of course, but as the issues are being chipped away, it could be good to know when the, uh, sculpture is considered complete.     

> __< rucknium >__ monerod always feels ban-happy to me.     

> __< spirobel:kernal.eu >__ spirobel:kernal.eu: this peer ban death spiral sounds more like this type of situation when a back off would make sense compared to a ban       

> __< jeffro256 >__ Not yet, we didnt't have a specific mind in goal going into alpha, but you and everyone else have found a laundry list of good issues to work on in the short term. Perhaps future time period can have more focused goals      

> __< rucknium >__ Occasional bans on mainnet wouldn't be as much of a problem. On a small stressnet, you are banning one of only a few possible peers.     

> __< articmine >__ All these improvements on network efficiency also harden Monero against spam and DDOS attacks > <rucknium> Is there a specific goal with stressnet debugging, such as "network can smoothly handle txpool size X and block size Y"?     

> __< jeffro256 >__ It's hard to control measurement of "smoothness" on an asynchronous network of peers which you don't control      

> __< jeffro256 >__ But yes, I agree that more specific goals should be finalized before a final stressnet      

> __< DataHoarder >__ would the final stressnet have any block verification improvements (or multithreading?)     

> __< DataHoarder >__ it's still quite noticeable when mining as doing submit_block (or on miners) they will keep mining the old template for a while, as monero still has not verified the submitted block via RPC and this takes 5-20s     

> __< jeffro256 >__ Yes, it should. There are a few big CPU-time improvements in review at the moment      

> __< DataHoarder >__ this effectively makes that time in between "lost" for miners     

> __< jeffro256 >__ For example: https://github.com/monero-project/monero/pull/10157 should help that issue w/ large mempools      

> __< spirobel:kernal.eu >__ how is your impression of the current peer ban list code? I just know from the wallet work, that rpc requests from the wallet also ended up on this ban list and it felt like the bans were sprinkled into the code base.  > <jeffro256> It's hard to control measurement of "smoothness" on an asynchronous network of peers which you don't control      

> __< boog900 >__ IMO monero should do what bitcoin does and relay blocks after checking PoW but before verifying txs      

> __< jeffro256 >__ Assuming the change concept is sound, #10157 will be extended for FCMP++ txs      

> __< jeffro256 >__ There's also: https://github.com/seraphis-migration/monero/pull/101     

> __< DataHoarder >__ that is done by P2Pool now boog900     

> __< rucknium >__ boog900:monero.social: monerod doesn't do that now?     

> __< DataHoarder >__ so everyone benefits, not just P2Pool blocks     

> __< boog900 >__ yeah I know but we shouldn't rely on that IMO      

> __< DataHoarder >__ no, it has to verify transactions first     

> __< DataHoarder >__ or sending bad blocks to other nodes causes them get banned     

> __< rucknium >__ In most circumstances, I guess it won't matter much if everything works smoothly with fluffy blocks.     

> __< jeffro256 >__ boog900: I've also thought about this. It's not a bad idea. I wonder how it would affect network health with a miner of similar hashpower to Qubic ~33%, willing to cause disruption for no return      

> __< jeffro256 >__ rucknium: No, it verifies all consensus rules and input proofs before relaying      

> __< DataHoarder >__ 10157 looks good. specifically, if the received block is for the expected next height and all txs in mempool were verified to be valid, shouldn't this block have a quicker verification time? Or is the verification re-triggered?     

> __< jeffro256 >__ DataHoarder: It should yes. Transaction input verification is only re-triggered if the dereferenced chain state for a transaction is changed, which will only happen in a >10-block reorg     

> __< DataHoarder >__ then 10157 would cover these delays seen while mining, good.     

> __< jeffro256 >__ If it works, yes, it should.      

> __< rucknium >__ More on stressnet?     

> __< rucknium >__ Thank you all community members who are running stressnet nodes 🧡     

> __< rucknium >__ 6. Mining pool centralization: Temporary rolling DNS checkpoints (https://github.com/monero-project/monero/issues/10064), Share or Perish (https://github.com/monero-project/research-lab/issues/146), and Lucky transactions (https://github.com/monero-project/research-lab/issues/145).     

> __< DataHoarder >__ checkpoints, still waiting for fixes. If we can get a proper repro case (via modified submit_block on known monero state) it'd be great, that way can attach a debugger and look at it.     

> __< DataHoarder >__ Longer term splitting of the code paths as written in other channels makes more sense later on     

> __< DataHoarder >__ Qubic broke something last week on their side and while fixing it they re-enabled selfish mining for a few more days, before it being disabled. They managed several reorgs of varying depths (some 5-7?) with ~1.6-1.8 GH/s.     

> __< DataHoarder >__ They currently stay at around ~1.2 GH/s and have decided to withhold bonus XMR payments from miners after a vote to attempt to prevent their price going lower. Mining/marathon schedule unchanged.     

> __< rucknium >__ Thanks for keeping up with the Qubic movements, DataHoarder. What is "bonus XMR payments"?     

> __< DataHoarder >__ Before, if price at end of epoch was > than an amount (at start of epoch) miners would receive some XMR (converted to their token) in their payments. this was part of their profit calculations     

> __< DataHoarder >__ if it was below, it was instead converted to qubic and burned. now any xmr they find will always be burned.     

> __< DataHoarder >__ (their people kept complaining that miners dumped too much qubic on each payout)     

> __< DataHoarder >__ I don't think it's relevant to discuss for MRL, but an interesting note that has made them even less profitable compared to XMR or XMR+merge mining     

> __< rucknium >__ They are reducing the incentive to mine with Qubic now?     

> __< articmine >__ DataHoarder: The classic bear raid approach     

> __< DataHoarder >__ It was an incentive originally thought to reduce selling pressure (if you don't sell price will go up which means more Qubic for you next week and so on)     

> __< DataHoarder >__ it ofc, when they attracted short term miners, caused more selling pressure     

> __< DataHoarder >__ This was the reasoning on their side to why stop now, Rucknium: https://irc.gammaspectra.live/36558af247094870/image.png      

> __< DataHoarder >__ but yes. there is no extra incentive except you get Qubic instead of something else     

> __< DataHoarder >__ I think further questions around that could go onto -offtopic or -lounge if on topic enough ^\     

> __< articmine >__ Thanks for the Qubic update.      

> __< rucknium >__ For next week, should this go on the agenda? https://github.com/hbs/MoneroMisc/blob/master/CARROT-discussion.md     

> __< rucknium >__ It suggests allowing user to not have an outgoing view key that can see outbound txs.     

> __< rucknium >__ There was discussion in #monero-research-lounge:monero.social  about it.     

> __< articmine >__ I say let the discussion in Lounge continue first.     

> __< articmine >__ If there is some loose consensus there then bring it here     

> __< DataHoarder >__ There were some issues found with current schemes that would break current carrot construction if some of the keys were made the same, and the alternative was for users to keep using legacy wallets (with the lack of forward secrecy)     

> __< rucknium >__ articmine: Alright.     

> __< rucknium >__ We can end the meeting here. Thank you everyone.     

> __< articmine >__ Thanks      

> __< tevador >__ articmine: Legacy wallets also get forward secrecy under Carrot (from an attacker who doesn't know a public address). They also get Janus attack protection.     

> __< tevador >__ My recommendation would be to allow users to generate a legacy wallet (with k_s and k_v) instead of a new wallet (with the new keys, including the outgoing view key). This has good plausible deniability because all wallets made before the fork are legacy wallets anyways.     

> __< tevador >__ New wallets should definitely not be constructed with k_ps = s_ga because: (1) Such use was not part of the audit. (2) Doing so loses internal forward secrecy. (3) It's impractical because it needs the private spend key to scan for owned enotes.     

> __< tevador >__ *k_ps = s_vb     

> __< jberman >__ On stressnet: taking stock and looking at the issues, there is a lot we can solve in the short term/medium term to improve daemon performance before we hit a wall. I think we should continue to knock out these issues and then re-assess upon hitting a wall     

> __< jberman >__ Clearly the daemon is having issues with a 300mb pool and 5mb blocks, so I think a rational immediate goal is for the daemon to not have issues at these levels     

> __< jberman >__ Examples of issues with clear fixes that we can solve short/medium term:     

> __< jberman >__ Example1: daemons dropping a connection that finds a fluffy block >4MB. That is a clear issue with a simple fix (that we've now rolled out in alpha stressnet v1.2)     

> __< jberman >__ Example2: daemons re-relaying every complete tx in their pool every x interval causing dropped connections. We know how to fix that (tx relay v2 massively helps, and IMO this PR is helpful too: https://github.com/seraphis-migration/monero/pull/174)     

> __< kayabanerve:matrix.org >__ tevador: That sounds like the reasonable and practical way to make a new wallet without an OVK     



# Action History
- Created by: Rucknium | 2025-10-14T22:01:33+00:00
- Closed at: 2025-10-28T20:34:17+00:00
