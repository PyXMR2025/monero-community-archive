---
title: Monero Research Lab Meeting - Wed 03 July 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1034
author: Rucknium
assignees: []
labels: []
created_at: '2024-07-02T21:11:09+00:00'
updated_at: '2024-07-22T20:05:07+00:00'
type: issue
status: closed
closed_at: '2024-07-22T20:05:07+00:00'
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

5. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html). Discuss hiring Cypher Stack for 4 days of work (38 XMR) reviewing [Veridise's proofs of the divisor technique](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/449#note_25181).

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1030 

# Discussion History
## Rucknium | 2024-07-05T20:25:31+00:00
Logs:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1034     

> __< k​ayabanerve:monero.social >__ 👋     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< jberman >__ *waves*     

> __< rbrunner >__ Hello     

> __< c​haser:monero.social >__ hello     

> __< v​tnerd:monero.social >__ Hi     

> __< j​effro256:monero.social >__ Howdy     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< k​ayabanerve:matrix.org >__ Organizing research/audits, as usual.     

> __< r​ucknium:monero.social >__ me: Helping with stressnet. Successfully (I think) ran the Dulmage-Mendelsohn Decomposition on a simulated set of transactions that have been flooded by black marbles. Running some stats on the mainnet p2p transaction logs to see if they have evidence of the black marble flooding.     

> __< j​effro256:monero.social >__ me: polishing fix PR for subaddress-related temporary scanning misses     

> __< jberman >__ me: grow_tree and trim_tree are approaching production-grade ready, continuing on trim_tree this week      

> __< v​tnerd:monero.social >__ I worked on LWS frontend API.     

> __< r​ucknium:monero.social >__ 3) Stress testing `monerod`  https://github.com/monero-project/monero/issues/9348     

> __< r​ucknium:monero.social >__ Maybe rbrunner can explain what he found in "Daemons processing big blocks may bump against serializer sanity checks and fail to sync" https://github.com/monero-project/monero/issues/9388     

> __< rbrunner >__ It's mostly described in the issue.     

> __< rbrunner >__ The short version: Sanity checks, put in place a few years ago, trigger if daemons asks other daemons for 20 very large blocks     

> __< rbrunner >__ because asking for 20 blocks is what they do per default     

> __< rbrunner >__ The immediate "band aid" measure on stressnet was syncing single blocks, before the root issue was known, which works     

> __< rbrunner >__ I submitted a PR to stressnet to go higher with the sanity checks     

> __< rbrunner >__ Durable and sensible solution might be to go dynamic with that number of blocks requested, depending on average blocksize     

> __< j​effro256:monero.social >__ Is that PR on spackle's repo?     

> __< rbrunner >__ Yes. 3 constants redefined bigger.     

> __< r​ucknium:monero.social >__ Here's rbrunner's that set sanity checks higher: https://github.com/spackle-xmr/monero/pull/12     

> __< rbrunner >__ The behavior is acutally quite funny: The daemon starts to disconnect every other daemon because it thinks they all send it corrupt data :)     

> __< r​ucknium:monero.social >__ Here's mine that just set default sync chunk to 1: https://github.com/spackle-xmr/monero/pull/8     

> __< j​effro256:monero.social >__ Damn 16K bytes per string is a really tiny limit lol     

> __< rbrunner >__ I think it's 16'000 strings.     

> __< j​effro256:monero.social >__ Ah I see, that makes more sense     

> __< r​ucknium:monero.social >__ We are at about 4MB block size now on stressnet. No one falls behind permanently, but there is some temporary fall-behind and re-org/orphaning at this block size: https://monitor.stressnet.net/     

> __< rbrunner >__ moneromooo mentioned that they just chose the limits more or less according to gut feeling, not as the result of some testing, or even simulation     

> __< rbrunner >__ So we probably should not give too much weight to their actual current values     

> __< r​ucknium:monero.social >__ ofrnxmr set up a stressnet block explorer at (onion hidden service): http://stressgguj7ugyxtqe7czeoelobeb3cnyhltooueuae2t3avd5ynepid.onion     

> __< j​effro256:monero.social >__ So blocks could have 820 txs per block, and if there's 20 blocks, then that would go over the string limit?     

> __< rbrunner >__ It seems so, yes. I saw it in the debugger go over the limit.     

> __< rbrunner >__ After getting around 30 MB of data     

> __< rbrunner >__ Although I could not find out where exactly, because that complicated templated serialization code was beyond my debugging fu     

> __< j​effro256:monero.social >__ Well another issue at hand is why the *serializer* doesn't check those limits while it is writing out     

> __< rbrunner >__ Well, duh, yes     

> __< rbrunner >__ I think it's protection about doctored data that blows up to gigabytes and brings down Monero daemons. Was a thing once as a possible attack, if I remember correctly     

> __< rbrunner >__ *protection against     

> __< rbrunner >__ Maybe vtnerd knows more     

> __< rbrunner >__ I don't plan to work more on this, I think somebody with better knowledge should find a good solution here     

> __< rbrunner >__ Going dynamic might not be trivial     

> __< v​tnerd:monero.social >__ The current limit was chosen somewhat arbitrarily by moo.  My new serializer often does limits based on wire size - a string is frequently required to be of minimum length, etc, instead of a max count. Unfortunately there are still some max counts in a few places that I didn't completely remove     

> __< r​ucknium:monero.social >__ Do any devs have requests for what spamming "configuration" to set up on stressnet? Right now we are spamming 1in/2out with 4MB blocks and a small txpool. We can increase the txpool, lower/raise block sizes, maybe try many-input txs to analyze "A lot of 150/2 transactions in the txpool causes memory spike / OOM" https://github.com/monero-project/monero/issues/9317     

> __< j​effro256:monero.social >__ Doing 1in/16out will let you create the highest number of transactions as quick as possible     

> __< j​effro256:monero.social >__ Maybe having 150 1-input txs will also cause the issue?     

> __< r​ucknium:monero.social >__ We are at about 20 txs/second being confirmed with 4MB blocks     

> __< rbrunner >__ I think there is nothing special with having 150 1-input transactions? Maybe I misunderstand.     

> __< rbrunner >__ We have hundreds of transactions going into a single block on stressnet now ...     

> __< k​ayabanerve:matrix.org >__ For byte spam, inputs is the way to go.     

> __< r​ucknium:monero.social >__ 150 1-input txs is sort of what we are doing now...over and over again     

> __< rbrunner >__ Without OOM problems, as far as I am aware     

> __< k​ayabanerve:matrix.org >__ (except you consume inputs faster than you make them)     

> __< j​effro256:monero.social >__ And you haven't run into the OOM issue at all?     

> __< r​ucknium:monero.social >__ Per byte of data, inputs also take longer to verify than outputs according to my tx performance tests     

> __< rbrunner >__ Seems so, yes     

> __< r​ucknium:monero.social >__ jeffro256: Low-RAM stressnet machines OOM if they have too many connections. On my 4GB node I've set connections to 4in/4out IIRC     

> __< rbrunner >__ All kinds of problems, but I did not hear about daemons running out of memory. Not on machines with "reasonable" amount of memory to start with     

> __< r​ucknium:monero.social >__ You can check the monitor node's RAM use, connections, CPU, etc on https://monitor.stressnet.net/     

> __< r​ucknium:monero.social >__ Or did the data collection go down?     

> __< j​effro256:monero.social >__ nice website ;)     

> __< r​ucknium:monero.social >__ I'll check that after the meeting     

> __< r​ucknium:monero.social >__ 4) Potential measures against a black marble attack. https://github.com/monero-project/research-lab/issues/119     

> __< r​ucknium:monero.social >__ I made progress on two topics.     

> __< r​ucknium:monero.social >__ A paper Vijayakumaran, S. 2023, "Analysis of Cryptonote transaction graphs using the Dulmage-Mendelsohn decomposition." Paper presented at 5th Conference on Advances in Financial Technologies (AFT 2023). https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=39     

> __< r​ucknium:monero.social >__ was released with a DM decomposition program written in Rust. I took the transactions that occurred during the suspected black marble flooding and eliminated the "black marbles" and removed black marble ring members from "real" txs. Then I ran the DM decomposition to see if even more ring members could be eliminated.     

> __< r​ucknium:monero.social >__ For more info on this attack, see Section 4 "Chain reaction graph attacks" of my https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-flood.pdf     

> __< r​ucknium:monero.social >__ According to my initial calculations, the suspected black marble flooding could reduce 0.5% of rings to effective ring size one (i.e. the real spend could be deduced) without trying any chain reaction graph attacks. In preliminary results, the Dulmage-Mendelsohn Decomposition can double that percentage to 1%. That number is within what I expected.     

> __< r​ucknium:monero.social >__ The other topic is analyzing p2p tx broadcast logs. I have two questions.     

> __< r​ucknium:monero.social >__ How is the time of queue set in src/cryptonote_protocol/levin_notify.cpp for fluff txs? I think nodes wait for some random time before sending a gossip message with the txs it has accumulated. How is that set?     

> __< r​ucknium:monero.social >__ The other question is whether Dandelion++ starts broadcasting at the "top of the minute", e.g. 17:31:00. In the data the gossip message arrival times are not uniformly distributed across the seconds of a minute. It almost looks like D++ does start broadcast at the top of the minute. I see higher probability of receiving a tx gossip message in the first 15 seconds of a minute. Then<clipped message     

> __< r​ucknium:monero.social >__  there is a smaller bump at about :40, which is the D++ embargo timeout time.     

> __< r​ucknium:monero.social >__ Another explanation is that some entity is broadcasting lots of txs at the top of the minute...like a spammer     

> __< v​tnerd:monero.social >__ I don't see how the code waits until the top of a minute, that sounds like something custom     

> __< r​ucknium:monero.social >__ Thanks. Then it's a possible fingerprint     

> __< r​ucknium:monero.social >__ If the gossip messages were uniformly distributed across a minute, then each second would have 1.667% of the messages. But what I am seeing is that the 10th second has 1.8%.     

> __< r​ucknium:monero.social >__ This is with about 15 million gossip messages. It cannot be random variation     

> __< r​ucknium:monero.social >__ Thanks to people who submitted monerod logs :)     

> __< r​ucknium:monero.social >__ I asked my first question because I noticed that txs were 'clumped" in gossip messages more than I expected.     

> __< rbrunner >__ Hmm, I wonder why you would care about minutes if you spam.     

> __< r​ucknium:monero.social >__ I mean, I want to understand the process of clumping     

> __< rbrunner >__ Ah, maybe some primitive throttle that results in this?     

> __< r​ucknium:monero.social >__ I don't think the spam script was set to maximum of what it was capable of.     

> __< r​ucknium:monero.social >__ 5) Research Pre-Seraphis Full-Chain Membership Proofs. Discuss hiring Cypher Stack for 4 days of work (38 XMR) reviewing Veridise's proofs of the divisor technique.  https://www.getmonero.org/2024/04/27/fcmps.html  https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/449#note_25181     

> __< r​ucknium:monero.social >__ kayabanerve: You wanted to discuss this     

> __< k​ayabanerve:matrix.org >__ Yep     

> __< k​ayabanerve:matrix.org >__ So the divisor proofs are complete, with ~3-4 hours to spare which is now moving to the R1CS circuit review as available.     

> __< k​ayabanerve:matrix.org >__ That means we need to     

> __< k​ayabanerve:matrix.org >__ 1) Have the proofs reviewed (which is arguable tertiary since Eagen originally proposed the technique)     

> __< k​ayabanerve:matrix.org >__ 2) Potentially be fine extending Veridise's contract 2-3 hours for the full R1CS review which should be less than a grand?     

> __< v​tnerd:monero.social >__ Oh that it is expected if I'm understanding you correctly. There's a fluff delay so txes will be grouped somewhat     

> __< k​ayabanerve:matrix.org >__ I solicited two quotes and received one from Cypher Stack on the proof review. It was 38 XMR @ 4 days (I believe 4 days of work, not 4 days of turnaround). cc Diego Salazar to confirm the quote if they're around.     

> __< v​tnerd:monero.social >__ But I wouldn't expect it to happen specifically at the top of a minute     

> __< d​iego:cypherstack.com >__ ye     

> __< k​ayabanerve:matrix.org >__ So that'd be my endorsement, and now subject to jberman 's co-endorsement (prior solicited yet needing an on-the-record version) and then MRL's.     

> __< r​ucknium:monero.social >__ vtnerd: Thanks. I skimmed the code with my non-C++ eyes and I couldn't find how the fluff timer is set. Every X seconds, with a random component?     

> __< k​ayabanerve:matrix.org >__ And then, I forgot to bring this up prior, but yes, I'd also like to confirm it's fine if we contract Veridise a few more hours as necessary to complete the R1CS review. It was projected at 5 hours and we're a bit short of that much time remaining. It's all reasonable to me.     

> __< v​tnerd:monero.social >__ I'm skimming the code to remind myself hold on     

> __< jberman >__ +1 for Cyper Stack divisor proof review, +1 for Veridise contract extension for R1CS review. Both sound solid to me     

> __< r​ucknium:monero.social >__ kayabanerve: Thanks. You said you solicited two quotes for the divisor proof review. Any info on the second one?     

> __< k​ayabanerve:matrix.org >__ I also have a tertiary topic I'd like to solicit MRL's opinion on, if we have a few minutes after the this Veridise discussion. It should be relatively brief, and is vaguely related to FCMPs, but I apologize if I should've brought it up prior and gotten it officially on the agenda. I only thought of it a couple days ago.     

> __< k​ayabanerve:matrix.org >__ I solicited two and received one.     

> __< k​ayabanerve:matrix.org >__ Because we didn't actually receive the other quote in a timely fashion (solicited over a week ago), we decided to move on with the proposal from CS which is reasonable and from the very trusted Aaron.     

> __< r​ucknium:monero.social >__ "Cyper Stack divisor proof review" and "Veridise contract extension for R1CS review" sound good to me.     

> __< rbrunner >__ From the little I can really judge this, good for me as well ...     

> __< k​ayabanerve:matrix.org >__ I will note we did not solicit a full spread as we originally did. Given the prior prices we've been quoted, I'm definitely preferring working with boutique firms (which is leading to not sending out as many emails and doing as many calls for results probably not worthwhile).     

> __< k​ayabanerve:matrix.org >__ rbrunner: Progress :D Exciting things :D Sign over more money and get more progress :D     

> __< rbrunner >__ Suuure :)     

> __< k​ayabanerve:matrix.org >__ On a much more legitimate and descriptive note, the divisor technique is a way to efficiently prove in-circuit a scalar multiplication.     

> __< k​ayabanerve:matrix.org >__ We use it to add (and remove) terms to Pedersen Commitments     

> __< k​ayabanerve:matrix.org >__ The divisor technique makes the cost 7 multiplicative constraints. Otherwise, it'd be 512.     

> __< k​ayabanerve:matrix.org >__ So it's 72x faster than prior state of the art.     

> __< v​tnerd:monero.social >__ The randomized timer is set per connection - slightly longer timeout for in connections. It gets set when there are no txes in the connection queue and gets flushed entirely when it expires. So you should see batches of txes sent     

> __< k​ayabanerve:matrix.org >__ The technique was posited by Eagen in 2022. Eagen's divisor work is largely subject to a lot of the same criticism as faced BP++. Aaron Feickert may be a more accurate person to comment as an individual who actually does review.     

> __< k​ayabanerve:matrix.org >__ Veridise was prior contracted to do a proper set of proofs for the technique, expanding on the rather sparse notes of Eagen on safety (~ half a page).     

> __< r​ucknium:monero.social >__ vtnerd: Thank you!     

> __< a​aron:cypherstack.com >__ I haven't done a thorough review of the divisor preprint, so I can't provide meaningful conclusions on that yet     

> __< k​ayabanerve:matrix.org >__ We now have a 12 page document establishing the background and security. While that's arguably already secondary review, Eagen being the primary source, tertiary review of the idea/secondary review of the proofs is reasonable.     

> __< a​aron:cypherstack.com >__ My very initial reading suggested that there could be similar issues as in BP++ (at least the initial version of BP++)     

> __< k​ayabanerve:matrix.org >__ So that's all this is. Hiring Cypher Stack/Aaron to do review and ensure we actually get such great performance safely :)     

> __< r​ucknium:monero.social >__ IMHO, giving the task of review to a skeptical reviewer is a good move. That's what is proposed AFAIK.     

> __< k​ayabanerve:matrix.org >__ By the numbers, I'll also note Veridise (with extension to complete the R1CS review) + this review by Cypher Stack is cheaper than both the Cypher Stack and Goodell quotes to do the proofs AFAICR.     

> __< k​ayabanerve:matrix.org >__ If no one has any objections, and the above summary provides sufficient clarity, I'd like to bring up my semi-adjacent topic. Would that be fine with you, Rucknium?     

> __< k​ayabanerve:matrix.org >__ (i ask as you execute our agenda)     

> __< r​ucknium:monero.social >__ Sounds great. I think we have loose consensus in favor of your two proposals today.     

> __< k​ayabanerve:matrix.org >__ 👍     

> __< k​ayabanerve:matrix.org >__ My other topic is simply how I want to contract review of the unreviewed hash function in Monero which we rely on for security.     

> __< k​ayabanerve:matrix.org >__ This is out of scope of the FCMP work, and the FCMP research budget, but I don't want to throw a researcher into submitting a CCS/MAGIC fundraise without a MRL endorsement.     

> __< k​ayabanerve:matrix.org >__ And I'd like to get this review done before the FCMP hard fork so if our unreviewed hash function is found unsafe, we can replace it at that time.     

> __< rbrunner >__ You mean the CryptoNight "slow hash"?     

> __< k​ayabanerve:matrix.org >__ I'm specifically referring to the bespoke hash to point within the Monero codebase, which has been documented yet not reviewed, and I would not be surprised if it had bias.     

> __< k​ayabanerve:matrix.org >__ If we're argue it as targeting 126 bits of security, and it has 110, it's fine yet should be deprecated and replaced (and we can replace it any time. Right now, the FCMP++ proposal has the key image generator a variable in the tree. It can be calculated however we want, including fixed to some constant if we had a proposal there)     

> __< k​ayabanerve:matrix.org >__ Hm. That's an interesting thought for its own line of research :D     

> __< k​ayabanerve:matrix.org >__ Yet to go back to my original point: bespoke hash to point probably not great. We don't know if it's great or acceptably bad or very bad. We should have this reviewed. If not great, FCMP++ should replace it with Elligator or similar.     

> __< k​ayabanerve:matrix.org >__ I'd just like to ask MRL that sounds reasonable and if I get a researcher to submit a CCS/MAGIC fund raise, they have backing on the premise being worthwhile.     

> __< a​aron:cypherstack.com >__ Any reason _not_ to simply go with Elligator, as it's well studied?     

> __< a​aron:cypherstack.com >__ Or is that "simply" carrying too much weight     

> __< k​ayabanerve:matrix.org >__ Performance, political capital, we still have to do this research to ensure supply hasn't been violated historically.     

> __< k​ayabanerve:matrix.org >__ Elligator (at least as used, which may be some variant) does two hash to points and sums them to create a non-biased point AFAIK.     

> __< k​ayabanerve:matrix.org >__ A lot of the hash to points discussed for standardization do so from my brief experience with them (which may be incomplete).     

> __< k​ayabanerve:matrix.org >__ So I don't want to propose a 50% perf drop without justification. We get the justification it's 'standard' but now we have two hash algos and the old is tech debt still needing impl/maintenance. Even if we said the security alone was sufficient, we still need to understand the security of the old one.     

> __< k​ayabanerve:matrix.org >__ And if the old one ends up secure, why move off?     

> __< a​aron:cypherstack.com >__ Yep, basically     

> __< k​ayabanerve:matrix.org >__ Considering its keccak256 with some method of determining a y coordinate which is valid, and recovering the x, my expectation/hope is that it's a bn254-esque issue.     

> __< k​ayabanerve:matrix.org >__ Deprecate, don't use, still out of human feasibility as understood today.     

> __< r​ucknium:monero.social >__ 50% perf drop on this operation means what percent drop on verifying a whole tx?     

> __< k​ayabanerve:matrix.org >__ Which means if we replace it, we're fine and can move on.     

> __< r​ucknium:monero.social >__ i.e. how important is it?     

> __< k​ayabanerve:matrix.org >__ Uhhhh right now or FCMP++s?     

> __< r​ucknium:monero.social >__ If you can give an answer on both     

> __< k​ayabanerve:matrix.org >__ Right now, we don't cache the key image generator. Every ring signature loads the output and re-runs the hash to point AFAIK.     

> __< k​ayabanerve:matrix.org >__ So input verification would decrease... 10-20%? Off-hand estimate?     

> __< k​ayabanerve:matrix.org >__ That hash to point will be 1/3 hash functions done by the CLSAG which is dominated by its hashes IIRC.     

> __< a​aron:cypherstack.com >__ Well, presumably you could use a faster hash function with Elligator, no?     

> __< a​aron:cypherstack.com >__ If you'd already be migrating     

> __< k​ayabanerve:matrix.org >__ Under FCMP++s, input verification doesn't do a hash to point. We calculate it once per output and save it to the tree.     

> __< k​ayabanerve:matrix.org >__ Like honestly, we may even be able to do a static point there now that I think about it.     

> __< a​aron:cypherstack.com >__ _e.g._ one of the BLAKEs     

> __< k​ayabanerve:matrix.org >__ Eh. No. We rely on the explicit hash to point to achieve a binding property in the linking tag and prevent using a view key to burn other outputs.     

> __< k​ayabanerve:matrix.org >__ So we'd need to at least solve that problem, and then also redo the considerations on related key attacks.     

> __< k​ayabanerve:matrix.org >__ And then even if it wasn't for those issues/necessities, we just had the composition reviewed and I can't sign off on that much time/effort when it's an optimization/protocol simplification at best.     

> __< k​ayabanerve:matrix.org >__ Anyways. Should be marginal under FCMP++s, off-hand I'd guess 10-20% worse CLSAG verification due to lack of caching.     

> __< k​ayabanerve:matrix.org >__ Aaron Feickert: I'd argue the end hash would need to be 20+% faster to be justified, and likely under the FCMP++ design (which determines and saves the key image). We can make the current CLSAG verify use a variable hash to point yet we'd have to track ring member age with the ring member which is a mess.     

> __< k​ayabanerve:matrix.org >__ (if we were picking a new function and justifying it based on performance. A 5% faster algorithm isn't worth complicating the specification)     

> __< a​aron:cypherstack.com >__ Could be interesting to time that out... Elligator-upon-some-BLAKE vs. CN     

> __< k​ayabanerve:matrix.org >__ Interesting to time out, I agree :D     

> __< a​aron:cypherstack.com >__ I've seen solid throughput numbers for the BLAKEs, but don't recall what that means for small inputs where "throughput" probably isn't really the measurement you want     

> __< k​ayabanerve:matrix.org >__ But again, historical review is necessary to ensure current integrity so I'd just like MRL's endorsement on an effort to find *someone* to review the current fn for bias/determine how much bias it has.     

> __< r​ucknium:monero.social >__ kayabanerve: Can you say if you have a candidate to attempt this?     

> __< k​ayabanerve:matrix.org >__ Worst case, it's not collision resistant and we need to start arguing the security of CryptoNote ring signatures? Does CLSAG's soundness hold even if the dynamic generator is non-uniform Aaron Feickert ?     

> __< k​ayabanerve:matrix.org >__ Rucknium: No, I asked one person and they deferred believing there to be better candidates. I don't want to cold email the Elligator people before knowing MRL endorses this research.     

> __< k​ayabanerve:matrix.org >__ Because I can cold email and organize a CCS, but then CCS will ask for MRL's opinion and we'll be in a MRL meeting a month from now (after I used a bunch of people's time) discussing the premise of this research as we are now :p     

> __< k​ayabanerve:matrix.org >__ I'd like to confirm the premise is agreed upon, find a candidate, and then have MRL solely review the specific proposal (not the premise of the proposal, which has become a stated goal)     

> __< r​ucknium:monero.social >__ I don't fully understand this specific issue, but I am in favor of funding research on potential vulnerabilities. It sounds like this is that.     

> __< k​ayabanerve:matrix.org >__ So don't worry, not going to ask to raise 100k ahead of time as a slush fund for this research :p     

> __< a​aron:cypherstack.com >__ It assumes the hash-to-point function can be modeled as a random oracle     

> __< k​ayabanerve:matrix.org >__ Yes but does it have to be a _good_ random oracle for _soundness_     

> __< k​ayabanerve:matrix.org >__ (I can follow up in DMs later, don't worry :) )     

> __< a​aron:cypherstack.com >__ Yeah, probably a little off topic for this meeting     

> __< a​aron:cypherstack.com >__ (basic answer... consequences of "bad" RO unclear)     

> __< r​ucknium:monero.social >__ I have a question: If it isn't as secure as we want, can the issue be eliminated on the blockchain by prohibiting new txs with that operation (e.g. use Elligator instead), or do the unspent outputs on the chain _need_ to use the old operation? So it would be harder to stop a vulnerability from being exploited later     

> __< k​ayabanerve:matrix.org >__ Yeah, so worst case (<110 bits of security), we'd do follow up work on the CN ring sigs/MLSAG/CLSAG to investigate impact.     

> __< k​ayabanerve:matrix.org >__ This effects the key image.     

> __< r​ucknium:monero.social >__ Can we get the opinion of tevador about this topic? Or jeffro256 ?     

> __< k​ayabanerve:matrix.org >__ Hm. Both affects and effects are arguable as valid there. I meant to type affects but I'm not sure I'm wrong for not doing so...     

> __< k​ayabanerve:matrix.org >__ But yeah, we can't move to Elligator universally without enabling double spending all historical outputs.     

> __< r​ucknium:monero.social >__ By the way, https://monitor.stressnet.net  is back. The data collector script had died.     

> __< k​ayabanerve:matrix.org >__ The exact implications of it being bad are unclear.     

> __< k​ayabanerve:matrix.org >__ I'd want to say under FCMP++, it'd only break unlinkability? I don't believe we argue soundness at all as premised on the hash to point?     

> __< a​aron:cypherstack.com >__ IIRC soundness would not be directly affected     

> __< k​ayabanerve:matrix.org >__ We output `I' = I + r_i V` and a commitment to `r_i`. The membership circuit asserts the r_i is consistent. Even if you found a relationship of I to V, it doesn't matter as we computationally bind to the V randomness.     

> __< k​ayabanerve:matrix.org >__ Right. So even if the existing points are biased, and you can find relationships for existing points, it shouldn't be an issue.     

> __< a​aron:cypherstack.com >__ At no point do things like commitment binding depend on any particular relationship between the hash output and other generators     

> __< k​ayabanerve:matrix.org >__ And we'd stop the ability to produce new unbiased points, so you could only work off what's already on-chain.     

> __< a​aron:cypherstack.com >__ (this was specifically checked)     

> __< k​ayabanerve:matrix.org >__ The larger concern is the existing ring signatures, MLSAG historically, and CLSAG. CLSAG very strongly transcripts and I hope its soundness to be fine. Ring signatures... may have some short Schnorr argument? MLSAG, I'd hope to follow CLSAG.     

> __< k​ayabanerve:matrix.org >__ But ring signatures' use of hash to point is incredibly load bearing, to a horrific degree.     

> __< k​ayabanerve:matrix.org >__ That's its own nightmare. Thankfully, FCMP++s mean we can finally deny TXs with ring signatures (they're still allowed today for migratory purposes).     

> __< k​ayabanerve:matrix.org >__ Anyways. Whole thing. Investigating the bias would be the first step to any discussion.     

> __< a​aron:cypherstack.com >__ FWIW I can take a closer look at the CLSAG security proofs later to investigate this more thoroughly     

> __< a​aron:cypherstack.com >__ It's a good question     

> __< a​aron:cypherstack.com >__ (anyone else is of course welcome to do this too)     

> __< k​ayabanerve:matrix.org >__ Part of me doesn't want you to waste your time before we determine bias, yet I'd explicitly be curious if MLSAG/CLSAG soundness holds upon a bad ROM here.     

> __< r​ucknium:monero.social >__ kayabanerve: A decision on this can wait until next meeting, right? Maybe get more opinions and discuss next time.     

> __< k​ayabanerve:matrix.org >__ it can? It just delays my contacting people. I have yet to hear any objections into this research which is obviously ambiguous, and in the worst case, enables forging key images/proofs.     

> __< a​aron:cypherstack.com >__ Eh, I'm curious :D     

> __< k​ayabanerve:matrix.org >__ So if you want the official position to be until next meeting, sure, yet I personally think the premise has been well received enough I'm fine moving forward.     

> __< a​aron:cypherstack.com >__ "Do random oracles actually exist" is a major load-bearing question for a lot of cryptography...     

> __< k​ayabanerve:matrix.org >__ But also yes, I'd love tevador's opinion.     

> __< k​ayabanerve:matrix.org >__ (And if I'm fine moving forward, I get it's not yet officially MRL backed and promise to not so represent it ;) )     

> __< k​ayabanerve:matrix.org >__ If MLSAG/CLSAG holds, the absolute worst case is we migrate all existing RCT outputs yet not all historical CN outputs. Then we turnstile those so it goes from inflation to theft.     

> __< k​ayabanerve:matrix.org >__ (migrate into FCMP++)     

> __< k​ayabanerve:matrix.org >__ I have nothing else to say immediately on this (and apologies it took much longer than expected), other than the above comment being *why* this review should complete *before* the FCMP++ PR is finalized. We can finish discussions next week for any official endorsement of the research topic (though yes, I'll probably start reaching out prior to the official endorsement). I have not<clipped message     

> __< k​ayabanerve:matrix.org >__ hing else to say on FCMPs other than congrats to CS for the new work.     

> __< r​ucknium:monero.social >__ --- END MEETING ---     

> __< r​ucknium:monero.social >__ Thanks, everyone.     

> __< s​gp_:monero.social >__ thank you     

> __< midipoet >__ Is the 'hash to point' function the only one in the current protocol that doesn't already have a formal review conducted (and one assumes published)?     

> __< k​ayabanerve:matrix.org >__ There are two hash to point functions, technically. Informally, decompress(keccak256()), which has a failure rate, and map(keccak256()), used for key image generators and without a failure rate.     

> __< k​ayabanerve:matrix.org >__ The former is only used for the generator `H`. The latter is used for key image generators and BP generators.     

> __< k​ayabanerve:matrix.org >__ Aaron Feickert: should be able to comment that the former is fine? They may decline to as the exact security properties may be difficult to define exactly, yet I've never heard it implied to be significantly faulty.     

> __< a​aron:cypherstack.com >__ The former should be fine, yes     

> __< k​ayabanerve:matrix.org >__ I'll also note Shen notated the function a bit, and cited other hash to points at the time (noting how this construction was distinct). Unfortunately, they didn't work on positing it as comparable/secure. My points of contact will presumably be the people who proposed the hash to points being standardized, some modern researchers, and potentially one or two who have similar constructions.     

> __< k​ayabanerve:matrix.org >__ (if anyone are similar)     

> __< midipoet >__ Excuse my ignorance, but why would the former be fine, and not the latter?      

> __< k​ayabanerve:matrix.org >__ Because decompression effectively forces rejection sampling until it finds a valid y.     

> __< k​ayabanerve:matrix.org >__ The map function does coercion which may produce a non-uniform y.     

> __< UkoeHB >__ The cryptonote hash-to-point originates in this paper: https://arxiv.org/pdf/0706.1448. And is informally described by Shen Noether in https://web.getmonero.org/resources/research-lab/pubs/ge_fromfe.pdf     

> __< midipoet >__ kayabanerve: i really appreciate that explanation. I actually think i understand it!      

> __< midipoet >__ UkoeHB: nice, thanks.      

> __< k​ayabanerve:matrix.org >__ UkoeHB: Shen described it as novel. TIL there is a citation for it.     

> __< k​ayabanerve:matrix.org >__ Do you have further background on where/when that was found? I'm pulling it up ro compare now     

> __< k​ayabanerve:matrix.org >__ *to     

> __< k​ayabanerve:matrix.org >__ Not to say the theory isn't related, yet the formula Shen notated do not appear present in the former paper.     

> __< k​ayabanerve:matrix.org >__ That could be notational, I won't claim to know either algorithm expertly after 10m, or could be a lack of equivalence.     

> __< k​ayabanerve:matrix.org >__ Or it could be how the former isn't for hashing to twisted edwards and the latter would have to embed the map from the Weierstrass curve in order to hash to a twisted edwards point.     

> __< k​ayabanerve:matrix.org >__ Pulled up ZtM. It cites the CryptoNote WP for that claim.     

> __< k​ayabanerve:matrix.org >__ Found the relevant citation in the CN WP. I'd have to ping Aaron Feickert on if the former actually lines up with the latter, assuming some Weierstrass map was crammed in?     

> __< UkoeHB >__ I never looked into the math of it, so not sure if the citation is accurate.   

# Action History
- Created by: Rucknium | 2024-07-02T21:11:09+00:00
- Closed at: 2024-07-22T20:05:07+00:00
