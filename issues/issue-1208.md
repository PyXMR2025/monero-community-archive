---
title: Monero Research Lab Meeting - Wed 21 May 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1208
author: Rucknium
assignees: []
labels: []
created_at: '2025-05-20T23:23:45+00:00'
updated_at: '2025-05-30T16:45:41+00:00'
type: issue
status: closed
closed_at: '2025-05-30T16:45:41+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. FCMP++ & divisors.

4. [_Maldo Map_ spy nodes research by jhendrix](http://maldomapyy5d5wn7l36mkragw3nk2fgab6tycbjlpsruch7kdninhhid.onion/) (Tor hidden service link)

5. Unit test for implementation of [subnet deduplication in peer selection algorithm](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf).

6. [Analysis of risk of new decoy selection algorithm without a hard fork](https://gist.github.com/Rucknium/fb638bcb72d475eeee58757f754acbee).

7. Web-of-Trust for node peer selection.

8. Any other business

9. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1204 

# Discussion History
## Rucknium | 2025-05-22T21:14:13+00:00
Logs:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1208     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< j​berman:monero.social >__ *waves*     

> __< v​tnerd:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< g​ingeropolous:monero.social >__ hi     

> __< a​rticmine:monero.social >__ Hi     

> __< j​hendrix:imagisphe.re >__ Hello     

> __< j​effro256:monero.social >__ Howdy     

> __< a​ntilt:we2.ee >__ ola     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< j​effro256:monero.social >__ Me: hot/cold wallet changes for after FCMP++, plus a bunch of smaller miscellaneous FCMP++ tasks.     

> __< j​berman:monero.social >__ me: updating the scan_tx feature for FCMP++ / an RPC to fetch paths in the tree by global output id     

> __< a​ntilt:we2.ee >__ started literature review of +20 papers on anomaly detection, self-organizing trust models and game theory in p2p nets.     

> __< 0​xfffc:monero.social >__ hi everyone     

> __< r​ucknium:monero.social >__ me: I have preliminary results from the custom loss function of the neural net learner to evaluate the privacy risk of deploying OSPEAD without a hard fork. I wrote a simple proof for the mixed strategy equilibrium of the adversary-protocol game for subnet deduplication. Continuing to test rbrunner's subnet deduplication implementation.     

> __< v​tnerd:monero.social >__ Me: completed tx construction in lws-frontend, minus some fee bugs. So working on that and completing remaining functions     

> __< 0​xfffc:monero.social >__ me: finished our new transaction relay protocol. Just cleaning it up and submitting it in a day or two. https://github.com/0xFFFC0000/monero/pull/60     

> __< r​ucknium:monero.social >__ flip flop: Check Cholex & Ignat (2024) "Sybil Attack Strikes Again: Denying Content Access in IPFS with a Single Computer" https://dl.acm.org/doi/10.1145/3664476.3664482     

> __< r​ucknium:monero.social >__ Cholez*     

> __< r​ucknium:monero.social >__ 3) FCMP++ & divisors.     

> __< o​frnxmr:monero.social >__ Me. Running fxmp++ testnet very painfully     

> __< o​frnxmr:monero.social >__ not ready for stressnet rucknium 

> __< j​berman:monero.social >__ What's painful?     

> __< o​frnxmr:monero.social >__ A lot is broken     

> __< j​berman:monero.social >__ A list would be solid     

> __< o​frnxmr:monero.social >__ Like, i couldnt send tx until i deleted and resynced the blockchain 4x, ffwd -> wallet is completely broken after a few hundred txs     

> __< r​ucknium:monero.social >__ AFAIK, we still don't have a document from Cypher Stack discussing their progress on the divisor review. It is OK if Cypher Stack wants to keep it non-public for now, but I wanted to check on it Diego Salazar     

> __< j​berman:monero.social >__ "i couldnt send tx" -> what error were you seeing?     

> __< o​frnxmr:monero.social >__ it segfaults     

> __< j​berman:monero.social >__ the wallet or node?     

> __< o​frnxmr:monero.social >__ Oh/ in the beginning.. i have the errors saves somewhere. I think i sent to jberman     

> __< o​frnxmr:monero.social >__ Wallet     

> __< r​ucknium:monero.social >__ This is what I was afraid of for the public stressnet. I wanted to have things break on the alpha stressnet so we could spam confidently.     

> __< o​frnxmr:monero.social >__ Jeffro**     

> __< j​effro256:monero.social >__ Yes I have it in the DM, I will forward to j-berman. I haven't seen that error yet, but I also haven't tried repro-ing yet in the way that you described. Although this is probably a good chat to have outside of MRL     

> __< r​ucknium:monero.social >__ Ideally, it would be possible to send one tx per second from a single RPC wallet     

> __< o​frnxmr:monero.social >__ More like 1 tx per 30sec     

> __< o​frnxmr:monero.social >__ (for 8 output)     

> __< j​berman:monero.social >__ Well, I guess turns out we made the right call postponing a public stressnet. Also worth sharing, jeffro256 shared instructions on how to run a local testnet for anyone who wants to help iron out bugs like this or get involved with development: https://github.com/seraphis-migration/monero/issues/47     

> __< o​frnxmr:monero.social >__ wrong call     

> __< j​berman:monero.social >__ ya would've been great if everyone spun up nodes and started complaining about how everything is broken     

> __< o​frnxmr:monero.social >__ yes     

> __< o​frnxmr:monero.social >__ How else would anyone know everyrhing is broken     

> __< rbrunner >__ We do know now, right?     

> __< o​frnxmr:monero.social >__ Yea, because i'm stubborn     

> __< r​ucknium:monero.social >__ Reflecting on divisors, I wonder if MRL expected miracles in a tidy time box. In other words, this level of mathematics requires more time than the quotes given to MRL by the cryptography firms.     

> __< r​ucknium:monero.social >__ Something to consider for the future.     

> __< j​berman:monero.social >__ This is because we left out the blinds cache, because divisors is postponed     

> __< r​ucknium:monero.social >__ Spamming has special requirements, which will need to be worked through. The blinds cache would eventually be exhausted     

> __< j​berman:monero.social >__ The blinds cache wasn't finished fwiw     

> __< rbrunner >__ I think some reviews went fine within the alloted time frame, perhaps not many ahead-indications that divisors would be so different     

> __< j​berman:monero.social >__ As in, jeffro and I still had work to do to harden it for usage     

> __< o​frnxmr:monero.social >__ btw ruck, my "spammer" just sends normal txs in a loop. Not submitting raw txs, nothing pregenerated etc     

> __< 0​xfffc:monero.social >__ I think we should have plan for extensive, long test, including stressnet, testnet of fcmp++ + carrot.     

> __< j​berman:monero.social >__ Agree with that^     

> __< o​frnxmr:monero.social >__ I wanted to release "my" testnet to public, but until my broken wallet issue is fixed i think its a waste of time     

> __< j​berman:monero.social >__ great so right call!     

> __< j​berman:monero.social >__ ;)     

> __< o​frnxmr:monero.social >__ no     

> __< o​frnxmr:monero.social >__ Itbtook like 3 days ans 1000+ tx to hit this condition     

> __< j​effro256:monero.social >__ It depends on how you structured your tx sending. The cache auto-refills, so it would work in the background. If you spaced out sending, b/c of the 20-minute lock time, you could ostensibly have it re-filling with a high-ish tx volume depending on how fast your machine is     

> __< j​berman:monero.social >__ Oh nice, that's good to hear     

> __< g​ingeropolous:monero.social >__ so we're still waiting on divisors report thing from cypher stack, right?     

> __< j​berman:monero.social >__ afaik yes^     

> __< rbrunner >__ Yes; the meeting log from last week has the details. Strong language :)     

> __< g​ingeropolous:monero.social >__ indeed. So whats the plan? Do we have a timeline from them?     

> __< 0​xfffc:monero.social >__ Sorry for hijacking the meeting. speaking of testing, this is the new sheriff in town: https://github.com/0xFFFC0000/benchmark-project      

> __< 0​xfffc:monero.social >__ Running stressnet on your local machine. with how many nodes you want. This is pre-pre-alpha. So very ugly code. But even at this step found a serious thing that I will disclose later.     

> __< j​berman:monero.social >__ "Itbtook like 3 days ans 1000+ tx to hit this condition" -> my "Oh nice, that's good to hear" was in response to this btw     

> __< r​ucknium:monero.social >__ AFAIK, the current plan, as last discussed in #no-wallet-left-behind:monero.social , is for jeffro and jberman to keep working on the integration work, which needs to be done regardless of divisors or not, and figure out someone else to write the non-divisor FCMP code, hopefully.     

> __< j​effro256:monero.social >__ Though yes if you intended to dump it all at once at didn't sufficiently fill up the cache, then it will run out pretty quickly     

> __< o​frnxmr:monero.social >__ the extremely large inputs is a separate issue, (for some reason 17000+xmr are locked eventually). but the double spend -> segfault wallet == i cant even resync the wallet. Its nice to find these issues as early as possible     

> __< r​ucknium:monero.social >__ I think we have learned all that we need to from Cypher Stack. The document would have the details, but the details aren't very important right now. IIRC, they estimate maybe 6 more months of effort to actually prove the soundness of divisors (or disprove them perhaps).     

> __< rbrunner >__ My understanding is that you can't give a timeline for something you don't fully know yet how hard it will get, or whether it will work out att all     

> __< r​ucknium:monero.social >__ But in the meantime, the non-divisors backup plan should be pursued.     

> __< j​berman:monero.social >__ "figure out someone else to write the non-divisor FCMP code" -> we should be good on this front (we have a strong candidate), but out of respect would request this is taken at my word at this point until I have confirmation     

> __< rbrunner >__ Oh the tension     

> __< o​frnxmr:monero.social >__ i think divisors integration (plan a) should be completed before moving on to plan b     

> __< o​frnxmr:monero.social >__ anyway, i'm done ranting. Hopefully jeff or 0x can fix the wallets     

> __< j​berman:monero.social >__ "(for some reason 17000+xmr are locked eventually). but the double spend -> segfault wallet == i cant even resync the wallet. Its nice to find these issues as early as possible" -> appreciate you testing this, can investigate it further     

> __< rbrunner >__ What's your reasoning, in short, about using the divisors already nevertheless?     

> __< j​effro256:monero.social >__ I think I agree with rbrunner in that these things can't really be assigned a timeline. If they truly are grid locked at the moment on agreeing on the validity of the security proofs, I really don't see any timeline given holding any weight. This isn't to knock Cypherstack, but that's just how cutting-edge R&D is     

> __< rbrunner >__ And well, don't we do this already in the code that you test now?     

> __< rbrunner >__ (the divisors)     

> __< o​frnxmr:monero.social >__ We assume that veridise's ACK, while rushed, was correct, and that CS more in-depth review will agree with it     

> __< o​frnxmr:monero.social >__ The code i test now, i think (dont know), is moving towards backup plan     

> __< g​ingeropolous:monero.social >__ jeffro256: yeah, understood.     

> __< rbrunner >__ With "assume" you mean "we speculate"?     

> __< o​frnxmr:monero.social >__ Yes     

> __< j​berman:monero.social >__ a completed divisors integration would include a blinds cache and hardened weight analysis, which seems ill-advised to spend cycles hardening, when instead we could work on need-to-be-completed tasks for either path a or b     

> __< r​ucknium:monero.social >__ jeffro256: Yes maybe I self-contradicted myself a little "expecting miracles in a tidy time box....And it will be done in 6 months!" :D     

> __< o​frnxmr:monero.social >__ Yes i agree on the common tasks, but not plan b (non-divisor path)     

> __< c​haser:monero.social >__ one comment from Diego last wee indicated that CS isn't exactly sure how far they are from having a clear conclusion on divisors. there was a perceived sense of urgency on their part, which made them draw a NACKing temporary conclusion for now. IIUC a total ACK or a total NACK on divisors could be anywhere from a few weeks from now (optimistic path) to 6+ months where only a full <clipped message>     

> __< c​haser:monero.social >__ formalization yield clear results, but for now it's all uncertain.     

> __< rbrunner >__ Might be a good idea to wait until somebody went so far into that plan b as to be able to give an estimate of work required     

> __< g​ingeropolous:monero.social >__ divisors is just an optimization, right? it won't even need a hard fork to plop in?     

> __< rbrunner >__ I mean, if that's only 2 weeks or so, in extreme, no sweat     

> __< j​berman:monero.social >__ it would need a hard fork     

> __< j​berman:monero.social >__ it's an optimization like BP+ was an optimization over BP     

> __< r​ucknium:monero.social >__ In magnitude, it's more like how BP was an optimization over non-BP RingCT txs, but for verification time instead of tx size.     

> __< r​ucknium:monero.social >__ AFAIK     

> __< o​frnxmr:monero.social >__ I think divisors are larger than non-divisor, but non costs more to verify     

> __< j​berman:monero.social >__ "Yes i agree on the common tasks, but not plan b (non-divisor path)" ok, well in the immediate term, the candidate working on non-divisors would not be working on anything else for FCMP++, so in the immediate term / until that's implemented, no resources are slated to be pulled away from anywhere else toward it     

> __< r​ucknium:monero.social >__ I would speculate that non-divisors FCMP with safe parameters may cause tx confirmation delays routinely.     

> __< a​rticmine:monero.social >__ How much larger?     

> __< j​berman:monero.social >__ Until it's implemented, jeffro and I can continue on common tasks for non-divisors and divisors, and then we can reconvene and discuss the optimal path forward dealing with divisors versus non-divisors     

> __< rbrunner >__ Sounds good to me, in any case     

> __< j​effro256:monero.social >__ Ahhhhh back in the dark ages when Borromean  ange proofs where >6 kilobytes per output     

> __< s​yntheticbird:monero.social >__ lmao     

> __< j​effro256:monero.social >__ IIRC non-divisor FCMPs will actually probably be slightly smaller     

> __< a​rticmine:monero.social >__ So I should complete the scaling on the basis of non divisors. It can then be changed later if we decide to go with divisors     

> __< j​berman:monero.social >__ As far as we know right now, we can pencil in (without actual figures): non-divisors would likely be slower to verify, smaller in byte size, and faster to construct     

> __< j​berman:monero.social >__ I don't want to share figures that turn out to be incorrect, so would probably be best not to assume what they'll be at this point     

> __< 0​xfffc:monero.social >__ I have a suggestion, how about having a list of bugs specifically for FCMP++ +  Carrot.     

> __< j​berman:monero.social >__ Have started to keep track of bugs over here: https://github.com/seraphis-migration/monero/issues     

> __< j​effro256:monero.social >__ You can use the issue tracker at https://github.com/seraphis-migration/monero/issues     

> __< j​effro256:monero.social >__ jinx     

> __< 0​xfffc:monero.social >__ a separate place, or list that we all can report, and keep track of the status. The reason why I am saying that is (1) I want all to see the status (2) each of us gonna encounter different issue running / testing.     

> __< o​frnxmr:monero.social >__ I think, until we have an academic NACK on divisors, we should be building torwars divisors ..     

> __< 0​xfffc:monero.social >__ ( that is just a suggstion, don't wanna hijack the topci )     

> __< o​frnxmr:monero.social >__ (for irc, my comment is reply to artic)     

> __< j​berman:monero.social >__ is something insufficient with those github issues 0xfffc ?     

> __< j​berman:monero.social >__ / keeping track there?     

> __< j​berman:monero.social >__ "I think, until we have an academic NACK on divisors, we should be building torwars divisors .." We have an academic NACK on divisors, one of the researchers thinks there is no way it'll work     

> __< 0​xfffc:monero.social >__ ( Nah, my second message was supposed to be attached to first one, but you and jeffro beat me and send the link faster) thanks I was not aware keep the FCMP++ + Carrot issues there.     

> __< o​frnxmr:monero.social >__ Jberman https://github.com/seraphis-migration/monero/issues/46     

> __< o​frnxmr:monero.social >__ This looks like same bug i had on the first few testnets i spun up     

> __< rbrunner >__ Frankly, I don't understand the hurry about going after divisors despite the situation is so foggy right now ...     

> __< rbrunner >__ Especially with jberman and jeffro256 have weeks of non-divisor-related work on their board     

> __< a​rticmine:monero.social >__ It is a simple  change to accommodate the  transaction weight change.      

> __< a​rticmine:monero.social >__ The question of how to price actual transaction size vs verification time is entirely a different matter, given the likely  change in verification time with divisors.     

> __< rbrunner >__ " one of the researchers thinks there is no way it'll work" We just fire that one? :)     

> __< s​yntheticbird:monero.social >__ science done right     

> __< j​berman:monero.social >__ to ease some of your frustration here / explain more of my perspective on why it's also nice to continue tasks on our end before opening up premature code very wide: here is an example of a PR that will lend itself to stronger handling of types across the C++/Rust FFI. The current code's handling is what may have lead to a segfault. Completing the full scope of this PR could solve<clipped message>     

> __< j​berman:monero.social >__  the segfault on its own without even needing further digging into its original cause with the current code: https://github.com/seraphis-migration/monero/pull/39     

> __< r​ucknium:monero.social >__ Not to be too critical, but the "divisors" that are being discussed were suggested by Liam Eagen, who also proposed BP++: https://moneroresearch.info/83     

> __< r​ucknium:monero.social >__ Later, sarang reviewed BP++ and thought its claims of soundness were not sufficiently supported: https://moneroresearch.info/217     

> __< r​ucknium:monero.social >__ But now sarang and Eagen are working together in the same firm, AFAIK 😁     

> __< s​yntheticbird:monero.social >__ I propose we ask author to review his own work     

> __< r​ucknium:monero.social >__ Anything more to discuss now on FCMP divisors?     

> __< j​berman:monero.social >__ We've made attempts but Eagen is pretty locked in on what they're doing now     

> __< 0​xfffc:monero.social >__ we were really thinking we can do Box in Rust and free in C?     

> __< s​yntheticbird:monero.social >__ sad but underestandable     

> __< s​yntheticbird:monero.social >__ It's actually possible     

> __< s​yntheticbird:monero.social >__ on paper     

> __< r​ucknium:monero.social >__ Barbie was right when she said "Math class is tough"     

> __< 0​xfffc:monero.social >__ WRONG     

> __< s​yntheticbird:monero.social >__ WHY CAPITALS     

> __< s​yntheticbird:monero.social >__ STOP YELLING AT ME     

> __< 0​xfffc:monero.social >__ ( oh it was not yelling, it was trump like. we can take this discussion to private DM if you are interested )     

> __< j​berman:monero.social >__ well it's been a TODO for many months now to not do that so, no     

> __< j​effro256:monero.social >__ You can for Rust types which implement `Copy` and not `Drop`     

> __< g​ingeropolous:monero.social >__ lol. So we need countermeasures for heavy non-divisor fcmp++ txs     

> __< r​ucknium:monero.social >__ Rust-C interaction is a -dev discussion. Or #no-wallet-left-behind:monero.social . We still have agenda items.     

> __< 0​xfffc:monero.social >__ ( That is such huge leap! There can be a lot of things. but for software as complex as FCMP++ going to deeply integrated into monero code base, I would take such a claim ( from Rust team or any other team ).  )     

> __< r​ucknium:monero.social >__ 4) Maldo Map spy nodes research by jhendrix . Tor hidden service link: http://maldomapyy5d5wn7l36mkragw3nk2fgab6tycbjlpsruch7kdninhhid.onion/     

> __< a​ntilt:we2.ee >__ iirc jhendrix observed that some "new gen" spy nodes can switch to full nodes, it that correct ?     

> __< j​hendrix:imagisphe.re >__ There were reachable nodes, but only for a day.     

> __< j​hendrix:imagisphe.re >__ A quick question about `--ban-list`. I received feedback from another community suggesting that instead of banning nodes, we could only disallow broadcasting transactions to them.     

> __< j​hendrix:imagisphe.re >__ I can see a few advantages to this approach:     

> __< j​hendrix:imagisphe.re >__ - Spy nodes won't know which peer has blocked them.     

> __< j​hendrix:imagisphe.re >__ - We can still use their resources to synchronize with the blockchain.     

> __< j​hendrix:imagisphe.re >__ Would it be useful?     

> __< r​ucknium:monero.social >__ I think that would be OK, but it requires a code change.     

> __< rbrunner >__ A little more like shadow-banning then     

> __< r​ucknium:monero.social >__ IIRC, that idea was considered, together with opt-out "banning" because that type of measure isn't as harsh, so maybe tolerable as opt-out instead of opt-in.     

> __< a​ntilt:we2.ee >__ for now they seem to avoid serving data, anyway     

> __< r​ucknium:monero.social >__ I don't know if there is a big value in not informing spy nodes that they are banned from specific nodes.     

> __< o​frnxmr:monero.social >__ those nodes still take up connection slots (sybil)     

> __< r​ucknium:monero.social >__ And they might even eventually be able to figure it out statistically, if they are receiving no stem-phase txs from a node.     

> __< a​ntilt:we2.ee >__ whats new on de-doubl'ing ?     

> __< o​frnxmr:monero.social >__ black hole nodes should be blocked/banned, not just silently allowed to parasite     

> __< rbrunner >__ In testing.     

> __< rbrunner >__ Careful to make nothing worse than before, only better ...     

> __< r​ucknium:monero.social >__ I had a few minor comments on the Maldo Map work:      

> __< r​ucknium:monero.social >__ > By default, every node connects to 12 peers to synchronize the blockchain, but we need to increase that number and recompile the software. To achieve this, we must make a few modifications to the cryptonote_config.h file.     

> __< r​ucknium:monero.social >__ It is not necessary to recompile. This behavior is available through the `in_peers` console command or RPC call or `--in-peers` startup flag.     

> __< s​yntheticbird:monero.social >__ I must agree on ofrnxmr on this one. Shadowbanning them is taking a potentially genuine connection slot and it seems more like a "political" decision to reassure the few "monero must not hard choose upon people" people.     

> __< r​ucknium:monero.social >__ > All of these represent remote full nodes, we like to call them public full nodes since they provide a service that allows anyone to download the blockchain from them, essentially, it's the same thing.     

> __< r​ucknium:monero.social >__ You can also sync blocks in the initial block download step from an unreachable node. It is just less likely to happen.     

> __< s​yntheticbird:monero.social >__ Also, iirc boog900 initial tests indicated that Cuprate was slower at syncing when pulling from spy nodes than genuine nodes     

> __< s​yntheticbird:monero.social >__ so even as a block synchronization service it's not ideal     

> __< b​oog900:monero.social >__ tbf that was more intuition - these nodes are proxies sending many requests to few nodes     

> __< g​ingeropolous:monero.social >__ ugh. we just need to get txs over i2p.     

> __< s​yntheticbird:monero.social >__ ah alr     

> __< r​ucknium:monero.social >__ Let's get into subnet deduplication.     

> __< r​ucknium:monero.social >__ 5) Unit test for implementation of subnet deduplication in peer selection algorithm. https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf     

> __< a​ntilt:we2.ee >__ thought about a script, using monerod ban + print_pl ...     

> __< r​ucknium:monero.social >__ I'm running this test of the mainnet behavior of rbrunner's subnet deduplication code     

> __< r​ucknium:monero.social >__ https://rucknium.github.io/xmrpeers/reference/peer.selection.test.html     

> __< r​ucknium:monero.social >__ https://github.com/rbrunner7/monero/tree/peers     

> __< r​ucknium:monero.social >__ It is passing the tests, but two notes:     

> __< r​ucknium:monero.social >__ 1) A chi-squared goodness-of-fit test is usually used to detect divergence of an empirical distribution from a theoretical/reference when the distribution is discrete/categorical. It seems that when there are lots of zeros in the empirical distribution, the chi-squared test rejects the null hypothesis when it shouldn't be rejected. This problem mostly affects the `gray_list` test <clipped message     

> __< r​ucknium:monero.social >__ because there are so many zeros. Advice online suggested to aggregate categories to eliminate the zeros, but it is best to avoid destroying information when practicing statistics. So I looked for alternative tests.     

> __< r​ucknium:monero.social >__ I tried a couple. A root-means-squared (RMS) goodness-of-fit test with simulated p-values seemed to fix the "problem" of zeros in the empirical distribution. Why? I don't know. I tried to search for information about why it works better, but didn't find anything. Because it works better in practice, I am using RMS to evaluate the implementation.     

> __< r​ucknium:monero.social >__ 2) The hypothesis test of selection from the `white_list` produces a "too high" p-value. This is not necessarily a problem, but it is strange. A _low_ p-value (e.g. 0.05, 0.01, 0.001,...) means that the null hypothesis is rejected and the implementation does not behave according to the expected reference distribution. A _high_ p-value may be just a fluke, or it may be that the emp<clipped message     

> __< r​ucknium:monero.social >__ irical distribution conforms "too closely" to the reference distribution than expected by pure chance.     

> __< r​ucknium:monero.social >__ For example, a fair 50-50 coin could be flipped 100 times. Getting exactly 50 heads and exactly 50 tails is the "most likely" outcome, but it would only occur with 8% probability. It would be more likely that there would be an excess of heads or tails, by chance. The p-value on a chi-squared test of this 50-50 empirical outcome would be about 1, the highest possible p-value.     

> __< r​ucknium:monero.social >__ AFAIK, rbrunner is looking into why the initial connection handshakes seem to fail at a high rate.     

> __< r​ucknium:monero.social >__ So, maybe that would be fixed or at least understood when this implementation code is submitted as a PR     

> __< rbrunner >__ Yes, seems that there is something strange in the attempts to find new white peers. Maybe was for years, with the old code already, will know more after this weekend     

> __< r​ucknium:monero.social >__ Related, maybe the number of attempts in a single "batch" should be increased from only 3.     

> __< b​oog900:monero.social >__ > AFAIK, rbrunner is looking into why the initial connection handshakes seem to fail at a high rate.     

> __< b​oog900:monero.social >__ could this be because of the amount of unreachable peers being injected into address books?     

> __< rbrunner >__ Those don't become *white* peers just like that, no?     

> __< b​oog900:monero.social >__ ah I thought we were talking about promotion to white peers, no these would be grey peers.     

> __< rbrunner >__ Gray peers seem to be ok, strangely, with about a 70% success rate to find a new one when "it's time"     

> __< r​ucknium:monero.social >__ It just seems to me that the handshakes fail too quickly. In about one millisecond. _And_, it seems that the first attempt from the gray_list has a much higher probability of success than the next ones in the same "batch". Since the candidates are being pulled with uniform probability from the gray_list, it would make more sense that the problem is with "our node", not the peers.     

> __< rbrunner >__ Will check that, as well.     

> __< rbrunner >__ The whole thing is quite dynamic, but not really complicated, and can be watched with logs and debugger quite nicely     

> __< r​ucknium:monero.social >__ Next things I am going to work on is getting https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf  into a form to be published as an MRL research bulletin (the first one in many years).  I think the last things I need are a description of the spy node-finding procedure and a description of Monero's peer selec<clipped message     

> __< r​ucknium:monero.social >__ tion algorithm, and its proposed new algorithm with subnet deduplication.     

> __< r​ucknium:monero.social >__ rbunner: There was also the matter of whether to avoid connecting to peers in a /16 that we are already connected to, or in a /24 that we are already connected to.     

> __< r​ucknium:monero.social >__ The status quo behavior is the /16 subnet (which is much larger), but the new code would avoid just the /24.     

> __< rbrunner >__ Yes, one of the main differences between "old" and "new" code. That's why I will go back to the old code at least once to compare.     

> __< r​ucknium:monero.social >__ I think I would favor keeping the same /16 behavior, but it may complicate the code more than to be worth it.     

> __< r​ucknium:monero.social >__ Tor and bitcoin have similar behavior at the /16 subnet level.     

> __< r​ucknium:monero.social >__ Anything more on subnet deduplication at this time?     

> __< a​ntilt:we2.ee >__ De-doupl'ing is a pre-requisite for all following metrics... btw     

> __< a​ntilt:we2.ee >__ so, tx for your work!     

> __< r​ucknium:monero.social >__ 6) Analysis of risk of new decoy selection algorithm without a hard fork. https://gist.github.com/Rucknium/fb638bcb72d475eeee58757f754acbee     

> __< r​ucknium:monero.social >__ TL;DR: With an even stronger method to attack user privacy, it seems that OSPEAD deployment without a hard fork may still provide more privacy than the status quo.     

> __< r​ucknium:monero.social >__ (By the way, that gist isn't updated yet)     

> __< r​ucknium:monero.social >__ I think I have a working neural net with the custom loss function. How is this different from my previous procedure? Instead of taking the output of the neural net as "static" and feeding it into a MAP Decoder/nonfungibility classifier as a separate stage, the neural net optimizer is feeding the real-spend-guess info back into its own optimization loop. This method could give stronger results.     

> __< r​ucknium:monero.social >__ It was difficult because I have to use a limited syntax. I believe that the neural net needs to form the analytical gradient (the slope of the function with respect to each choice parameter) for the loss function, so the type of operators I can use is limited.     

> __< r​ucknium:monero.social >__ The custom loss function's procedure is:     

> __< r​ucknium:monero.social >__ 1) Classify the tx as old-DSA or new-DSA. Also do this for the antecedent txs.     

> __< r​ucknium:monero.social >__ 2) If old-DSA, run the MAP Decoder attack.     

> __< r​ucknium:monero.social >__ 3) If new-DSA, yet none of the antecedent txs are classified as new-DSA, then run the MAP Decoder attack (but assume that the decoy distribution is new-DSA, so MAP Decoder is much less effective.)     

> __< r​ucknium:monero.social >__ 4) If new-DSA, but one or more of the antecedent txs are classified as new-DSA, then randomly choose one of them as the real spend. This is the nonfungibility classifier.     

> __< r​ucknium:monero.social >__ So far, I have found that the neural net optimizer chooses to just classify all txs as old-DSA. I think it does this because the MAP Decoder is so effective that it is better to misclassify the few txs that are new-DSA instead of trying to run the DSA classification and misclassifying some old-DSA as new-DSA and running the wrong MAP Decoder. Given this, the NN classifier does not<clipped message     

> __< r​ucknium:monero.social >__  get any advantage from mainnet having a non-zero share of txs be new-DSA .     

> __< r​ucknium:monero.social >__ I _can_ get the neural net to try to classify old/new if I artificially decrease the effectiveness of the old-DSA MAP Decoder in the loss function computation. The old/new classification, in that case, is pretty good (correlation about 0.7). So, it could work properly, in that way, if it wanted to. But it doesn't because that's not the more effective way to guess the real spend.     

> __< r​ucknium:monero.social >__ I have been testing for a new-DSA tx shares of 2, 5, 10, and 15%. Beyond 15%, the non-fungibility classifier could not get a higher hit rate than the old-DSA MAP Decoder, anyway. See Table 1 of     

> __< r​ucknium:monero.social >__ https://github.com/Rucknium/misc-research/blob/main/Monero-Fungibility-Defect-Classifier/pdf/classify-real-spend-with-fungibility-defects.pdf     

> __< rbrunner >__ So, we just have to push the share of new-DSA transactions over 15%, and we are good?     

> __< r​ucknium:monero.social >__ And I'm setting the probability of spending change to 75%, which is quite high and therefore favorable to the nonfungibility classifier. So a sort of like worst case scenario     

> __< r​ucknium:monero.social >__ Minor note: It looks like the custom loss function is not globally convex, so the optimization process can get "stuck" in a local non-optimal minimum. I tried different initial values to discover this. This means that it is important to test different starting values. At this time I only have loose control/understanding of how the neural net sets up and manages initial values in t<clipped message     

> __< r​ucknium:monero.social >__ he optimization process.     

> __< r​ucknium:monero.social >__ Let me know if that was confusing or needs clarification.     

> __< r​ucknium:monero.social >__ rbunner: Above 15% there is no question, IMHO, and all this additional analysis I have done since the initial `classify-real-spend-with-fungibility-defects.pdf` research note is not necessary. What I have been doing is trying to see if 0-15% adoption percentage would create a privacy risk beyond the status quo. I have not found evidence of that, yet. And I don't know another direc<clipped message     

> __< r​ucknium:monero.social >__ tion to go. I have tried three ways, and none of them suggest additional risk.     

> __< g​ingeropolous:monero.social >__ even with a hardfork, wallets can still use non-ospead right? or would the hardfork include some mandated tx version consensus?     

> __< r​ucknium:monero.social >__ I need to double check everything and put my scripts into a form that makes it easy to reproduce the results.     

> __< rbrunner >__ I see, thanks     

> __< r​ucknium:monero.social >__ gingeropolous: In a theoretical intermediate hard fork before FCMP deployment, which seems unlikely now, probably there would be no requirement to use a specific DSA, like there is now. But the vast majority of users would update their wallets to the latest software, which would have it.     

> __< r​ucknium:monero.social >__ Any more comments on this topic?     

> __< r​ucknium:monero.social >__ I want to say again, like I said before, that I am not very experienced with neural nets, so maybe something could be improved beyond what I've done. But some of the same principles of loss function minimization that I know well do still seem to apply here. So I've pushed onward with that knowledge.     

> __< r​ucknium:monero.social >__ 7) Web-of-Trust for node peer selection.     

> __< r​ucknium:monero.social >__ Want to discuss this more now, especially flip flop ? Or should we wait for the literature review you are doing?     

> __< a​ntilt:we2.ee >__ ( abandonned neural nets a long time ago and became a feedback-delay-networks pro :)     

> __< a​ntilt:we2.ee >__ My starting point:     

> __< a​ntilt:we2.ee >__ S. Wuthier, N. Sakib and S.-Y. Chang, "Positive Reputation Score for Bitcoin P2P Network," 2024 IEEE 21st Consumer Communications & Networking Conference (CCNC), Las Vegas, NV, USA, 2024, pp. 519-524     

> __< a​ntilt:we2.ee >__ https://drive.google.com/file/d/17S4N3eJvUePvO92ob_cIseeusQSMG0ly/view     

> __< a​ntilt:we2.ee >__ "...focusing on the peer’s behavior in relaying unique/new blocks and transactions." -> (proof of service)     

> __< r​ucknium:monero.social >__ flip flop: Do you want access to post papers on moneroresearch.info?     

> __< a​ntilt:we2.ee >__ not jet - thanks     

> __< a​ntilt:we2.ee >__ more on my review next meeting !     

> __< r​ucknium:monero.social >__ Looking forward to it :)     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< a​ntilt:we2.ee >__ But there is a lot of research out there on Dynamic trust metrics for peer-to-peer systems     

> __< a​ck-j:matrix.org >__ I didn’t want to interrupt the meeting but we (MAGIC committee) just launched a fundraising campaign to hire Ada Logics to develop fuzzing harnesses for the monerod RPC calls     

> __< a​ck-j:matrix.org >__ https://donate.magicgrants.org/monero/projects/fuzzing-monero-rpc     

> __< a​ck-j:matrix.org >__ Many of the hackerone reports crash monero nodes via malicious RPC calls. Currently there are no fuzzing tests in place to automate checks for these issues.     

> __< a​ck-j:matrix.org >__ https://hackerone.com/reports/2858802     

> __< a​ck-j:matrix.org >__ https://hackerone.com/reports/506595     

> __< a​ck-j:matrix.org >__ https://hackerone.com/reports/1511843     

> __< a​ck-j:matrix.org >__ https://hackerone.com/reports/1379707     

> __< a​ck-j:matrix.org >__ This is part of a larger push to develop more thorough fuzzing harnesses for monerod overtime. We are starting with the RPC calls as the external attack surface is the most vulnerable point which at worst could take down the entire network or allow an attacker remote code execution on nodes through memory corruption vulnerabilities.      

> __< a​ck-j:matrix.org >__ Developing these harnesses to work with oss-fuzz in a performant fashion is non-trivial which is why we contracted a firm led by the main contributor to oss-fuzz. Their solution will have the added benefit of fuzzing the networking stack at a low level.     

> __< s​yntheticbird:monero.social >__ let's agree on definition, you want to fuzz the RPC handler? The json-rpc handler? or Both?     

> __< s​yntheticbird:monero.social >__ at my understanding both but I prefer to be sure.     

> __< s​yntheticbird:monero.social >__ > Target at least 75% of Monero's RPC handlers, with a goal of 100% coverage.     

> __< s​yntheticbird:monero.social >__ Indicate a fuzzing of RPC handlers     

> __< s​yntheticbird:monero.social >__ > Their solution will have the added benefit of fuzzing the networking stack at a low level.     

> __< s​yntheticbird:monero.social >__ This indicate fuzzing the json-rpc handler     

> __< a​ck-j:matrix.org >__ Both     

> __< a​ck-j:matrix.org >__ From the statement of work     

> __< a​ck-j:matrix.org >__ “fuzzing to at least 75% of the Monero     

> __< a​ck-j:matrix.org >__ RPC handlers listed in the two links:     

> __< a​ck-j:matrix.org >__ https://docs.getmonero.org/rpc-library/monerod-rpc/#json-rpc-methods and     

> __< a​ck-j:matrix.org >__ https://docs.getmonero.org/rpc-library/monerod-rpc/#other-rpc-methods”     

> __< s​yntheticbird:monero.social >__ my bad that's not what i meant     

> __< s​yntheticbird:monero.social >__ By json-rpc handler i meant the part of the code that is parsing json into exploitable rpc values     

> __< s​yntheticbird:monero.social >__ By json-rpc handler i meant the part of the code that is parsing json into exploitable rpc requests     

> __< s​yntheticbird:monero.social >__ not the methods under `/json_rpc` endpoint     

> __< s​yntheticbird:monero.social >__ I am asking because imo RPC handler is completely worth fuzzing and I support this endeavor. But the json parser have a PR to replace it and as one of the vuln author already expressed, some parts of `contrib/epee` should be rewritten entirely. So I see little benefits in spending time on this, if so was planned.     

> __< s​yntheticbird:monero.social >__ spending time on the json parser for example     

> __< j​berman:monero.social >__ I've mentioned in the past setting up a harness that fuzzes both the epee handler (by sending crafted payloads), in addition to testing specific RPC endpoints fuzzing specific params     

> __< j​berman:monero.social >__ Although that's a fair argument the former may be less beneficial with new changes     

> __< a​ck-j:matrix.org >__ SyntheticBird: the statement of work specifically targets the RPC handlers within src/rpc used by the json and binary rpc calls above. I will update the campaign to be a bit more clear     

> __< r​ucknium:monero.social >__ What about the p2p-only communication? Levin protocol, etc. That's a smaller attack surface, but it can affect every node. I think only a minority of nodes expose their RPC services/ports. I suppose it's too late to change the scope of work.     

> __< r​ucknium:monero.social >__ IIRC, you can get an estimate of the share of nodes with open RPC services by requesting your node's peer list.     

> __< r​ucknium:monero.social >__ Yes, `get_peer_list` has an optional `rpc_port` field in its return value.     

> __< s​yntheticbird:monero.social >__ I tried to fuzz the levin handler during a week. Found nothing.     

> __< s​yntheticbird:monero.social >__ oh i did find something weird actually     

> __< a​ck-j:matrix.org >__ Rucknium: These are good questions, I will get back to you. It is not too late to change the proposal. Feedback and questions are welcome     

> __< r​ucknium:monero.social >__ There is definitely someone more knowledgeable than me on this topic of RPC vs p2p vulnerability to fuzzing, e.g. vtnerd     

> __< s​yntheticbird:monero.social >__ *vtnerd, the holy guardian of epee*     

> __< s​yntheticbird:monero.social >__ \* boss music starts to play \*     

> __< s​yntheticbird:monero.social >__ <del>oh i did find something weird actually</del> nvm i just remember i found an explanation     

> __< h​into:monero.social >__ xmrack: I believe many of the issues with RPC are comprised of relatively normal methods abusing `monerod`'s "intended" behavior, these only require knowledge on the related code and not necessarily fuzzing. I am aware of a few unreported ones but have not revealed them since there doesn't seem to be urgency, a knowledgeable/willing attacker, or the right incentives/push to allow <clipped message>     

> __< h​into:monero.social >__ for large fixes in that subsystem. If the scope of the proposal can be changed, I would advise that funding a review of the RPC code (and the related code it calls), precisely locating problematic areas, and pushing for patches would be a better use of resources than creating a fuzzing harness (although, that would be great and uncover things as well).     

> __< s​gp_:monero.social >__ A thorough review of the RPC code might require a different skillset, as far as I understand     

> __< s​yntheticbird:monero.social >__ As I said earlier, this is sagewilder message regarding fuzzing, they expressed the same opinion as hinto.     

> __< s​yntheticbird:monero.social >__ sagewilder is the author of the rpc memory exhaustion vuln report     

> __< s​yntheticbird:monero.social >__ I know im a hardcore fan and extreme shiller but this is an opportunity to involve Zellic.     

> __< s​yntheticbird:monero.social >__ I assume one of the best hackers on one of the ugliest part of monero codebase is without a doubt going to produce exciting results     

> __< s​yntheticbird:monero.social >__ sry it might be confusing im answering sgp_ but this is more of a general message, im not saying we should nack your fundraising     

> __< s​gp_:monero.social >__ I hear what you're saying, I personally just see this as a related (but still different and largely independent) project. It addresses similar concerns through two different, complimentary techniques that require different skillsets. But I'm here to start things that make sense; the committee decides what to pursue     

> __< s​gp_:monero.social >__ I'd love to do both :)     

> __< s​gp_:monero.social >__ The code rewrites aren't expected to change the RPC endpoints, right? So the fuzzing could still be used after the rewrites as well (but with potentially less usefulness since there may be other, bigger problems)?  Or am I not understanding     

> __< s​yntheticbird:monero.social >__ > The code rewrites aren't expected to change the RPC endpoints, right?     

> __< s​yntheticbird:monero.social >__ If the changes are contained within contrib/epee, yes     

> __< s​yntheticbird:monero.social >__ > So the fuzzing could still be used after the rewrites as well (but with potentially less usefulness since there may be other, bigger problems)?     

> __< s​yntheticbird:monero.social >__ Not really, it doesn't reduce its usefulness. RPC handler are an independent and worth it issue.     

> __< h​into:monero.social >__ that's unfortunate, I would have left a few +1 reactions but seems like I can't     



# Action History
- Created by: Rucknium | 2025-05-20T23:23:45+00:00
- Closed at: 2025-05-30T16:45:41+00:00
