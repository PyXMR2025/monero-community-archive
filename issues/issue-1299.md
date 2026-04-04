---
title: Monero Research Lab Meeting - Wed 19 November 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1299
author: Rucknium
assignees: []
labels: []
created_at: '2025-11-18T22:39:59+00:00'
updated_at: '2025-11-28T20:47:18+00:00'
type: issue
status: closed
closed_at: '2025-11-28T20:47:18+00:00'
---

# Original Description

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Monero node fuzzing: past, present, & future. [Monero Node RPC Endpoints Now Have 100% Fuzzing Coverage](https://magicgrants.org/2025/11/17/Monero-RPC-Fuzzing).

4. P2Pool consolidation fees after FCMP hard fork. [Coinbase Consolidation Tx Type](https://github.com/monero-project/research-lab/issues/108).

5. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-11.pdf). [Revisit FCMP++ transaction weight function](https://github.com/seraphis-migration/monero/issues/44).

6. [FCMP alpha stressnet](https://monero.town/post/6763165).

7. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1296

# Discussion History
## Rucknium | 2025-11-25T23:23:58+00:00
Log

> __< jeffro256 >__ I'm sorry, I'm not going to be able to make this MRL meeting      

> __< sgp_ >__ You can skip item 6 unless someone else has something to talk about for that     

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1299     

> __< rucknium >__ 1. Greetings     

> __< articmine >__ Hi     

> __< jrkl23jlka >__ hello     

> __< vtnerd >__ Hi     

> __< jberman >__ waves     

> __< boog900 >__ hi     

> __< spackle >__ Hello     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< rucknium >__ me: Looking at research papers about p2pool mining scalability.     

> __< articmine >__ I have updated the spreadsheet with the weights and the scaling documents     

> __< vtnerd >__ Various bugs and small changes to lws and polishing up lookahead in lwsf. Need to move onto carrot/fcmp in lwsf too     

> __< jrkl23jlka >__ we saw there were some fee related proposals and decided to pass by drop some strong opinions     

> __< rucknium >__ Is ack-j:matrix.org  / xmrack:monero.social  present?     

> __< jberman >__ me: finished up deadlock PR upstream, finished first round review on tx relay v2 (will work with 0xfffc:monero.social on further changes this week), tested and integrated kayabanerve:matrix.org's  new change to the FCMP++ lib that brings memory usage of FCMP++ verification down to 250mb per call to verify (down from ~800mb), [... too long, see https://mrelay.p2pool.observer/e/iebOtMoKd3JQTkxj ]     

> __< rucknium >__ 3. Monero node fuzzing: past, present, & future. Monero Node RPC Endpoints Now Have 100% Fuzzing Coverage (https://magicgrants.org/2025/11/17/Monero-RPC-Fuzzing).     

> __< rucknium >__ AFAIK, someone from ADA Logics planned to be present at the meeting today.     

> __< syntheticbird >__ greetings gentlemens     

> __< ack-j:matrix.org >__ Yes thanks for the ping     

> __< ack-j:matrix.org >__ We (Magic) completed the first fuzzing proposal and released AdaLogics report in that blog post. The engagement discovered three RPC issues that affected the availability of monero nodes, which are all now fixed. We are looking to get feedback on our next fuzzing proposal targeting src/wallet src/p2p and src/fcmp_pp     

> __< ack-j:matrix.org >__ David from adalogics said they might join as well to answer questions     

> __< ack-j:matrix.org >__ Generally we look to increase code coverage as much as possible, but in a strategic manner     

> __< rucknium >__ I don't know about the code, but maybe in public appeals for funding, you can say why fuzzing is important in the title. I don't think ordinary people know what fuzzing is. Maybe "Automated search for exploitable vulnerabilities" or something.     

> __< syntheticbird >__ more like bugs, depending on what is fuzzed and how they can fin vulnerabilities that cannot be exploited     

> __< ack-j:matrix.org >__ I’ll word-smith the title a bit     

> __< syntheticbird >__ tho in this case the fuzzing done by ada is using the endpoits directly so same access as an attacker     

> __< syntheticbird >__ p2p seems to me to be the very next thing to do.      

> __< Guest678 >__ Hi!     

> __< Guest678 >__ everyone     

> __*__ jrkl23jlka likes people fuzzing around     

> __< syntheticbird >__ hi Guest678, please sit tight and listen to others. also everyone do not work, it's a discord thing.     

> __< Guest678 >__ I know I'm sorry, I am just messing with a monero discord server that has integrated this chat as a channel :)     

> __< ack-j:matrix.org >__ P2P fuzzing will be a main focus of the next project. Any crashes discovered there would likely be very high impact     

> __< rucknium >__ Guest678: Please do not allow any bridges from Discord in this channel to be able to send messages. Only read-only.     

> __< ack-j:matrix.org >__ I dont see David in here so we can likely skip to the next section if there are no other questions     

> __< syntheticbird >__ Are the findings of the fuzz public yet?     

> __< ack-j:matrix.org >__ We didn’t release specifics as the hackerone issues havent been publicized yet     

> __< ack-j:matrix.org >__ One thing to note is that these fuzzing harnesses will pay dividends in the long run as code changes are made to the master branch they will automatically be fuzzed using large amounts of compute     

> __< DataHoarder >__ ^ fuzzing is great, did that for consensus code, then C P2Pool had some, and found issues on both sides that way. and eternally finding edge cases that now stay as unit tests     

> __< jberman >__ Sounding like it was an effective and fruitful start, thanks for pushing this forward!     

> __< syntheticbird >__ fuzzing is like gambling. and gambling does push you to the edge cases of your life     

> __< syntheticbird >__ so gambling is a good thing     

> __< jberman >__ I +1 the main focus being on p2p. Happy to help with fcmp++ as well when they get to it     

> __< syntheticbird >__ i meant fuzzing     

> __< ack-j:matrix.org >__ David is joining shortly if there are any questions for him regarding the report     

> __< rucknium >__ ack-j:matrix.org: Thanks for arranging!     

> __< rucknium >__ The only thing I noticed about the fuzzing is that review and merger of the harness took a while. But that seems common for most PRs to the Monero codebase.     

> __< rucknium >__ Welcome, davkor:mozilla.org  !     

> __< davkor:mozilla.org >__ rucknium: One potential option for improving speed here would be to place the fuzzing harnesses in a different repository with less scrutiny on code introduced into the repo. In essence they don't have to live the same place as the main code. Am not sure if this would be preferable, but it's an option from OSS-Fuzz's perspective.     

> __< davkor:mozilla.org >__ rucknium: thank you!     

> __< davkor:mozilla.org >__ > <syntheticbird> Are the findings of the fuzz public yet?     

> __< davkor:mozilla.org >__ One thing to be aware of here is that OSS-Fuzz itself has a 90 day disclosure deadline, after which limited information on issues will be made public. Following a fix of an issue, OSS-Fuzz will also make limited information public, even if it's earlier than the 90 day deadline. Monero has been integrated into OSS-Fuzz for a nu [... too long, see https://mrelay.p2pool.observer/e/1u-9tcoKbWFXOTVf ]     

> __< jberman >__ Keeping this in the main repo seems ideal to me to make sure it remains updated as changes are made. The PR was opened Jul 18, first reviewed and approved Aug 13, merged in Sept. That doesn't seem too outlandish to me. And now that there is an established framework in use for RPC, I would expect the future PR's to be smoother anyway     

> __< davkor:mozilla.org >__ jberman: Yup, no problem from our side as well. One potential caveat is that once the harnesses are public someone may launch a huge compute effort to run them while they are still being reviewed. A small race could happen with who runs the fuzzing harnesses a lot the quickest. But I'd probably say that's a minor issue. A [... too long, see https://mrelay.p2pool.observer/e/n-7RtcoKeTBiZEV1 ]     

> __< syntheticbird >__ I'll just place here that i know people that didn't wait for the harness to fuzz parts that are currently unfuzzed     

> __< rucknium >__ Where is the compute power coming from by the way? GitHub?     

> __< syntheticbird >__ i'm not aware of any results so far form their parts     

> __< davkor:mozilla.org >__ rucknium: on OSS-Fuzz (https://github.com/google/oss-fuzz), Google     

> __< syntheticbird >__ so i don't think anyone actually somewhat qualified to exploit a findings with the harness would wait on it to be developed     

> __< jberman >__ Hm, so sounds like the alternative would be to keep the changes private somewhere until the harness has run some sufficient amount, and then open it up for review if nothing found     

> __< syntheticbird >__ that would slow down integration and try to solve a very unlikely scenario but that is a responsable approach.      

> __< davkor:mozilla.org >__ jberman: yeah, this is also what we did previously.     

> __< ack-j:matrix.org >__ ^ david and his team fuzzed the harnesses on their own hardware for a while waiting for the PR to merge     

> __< jberman >__ I do think that would be a reasonable approach to use for p2p     

> __< ack-j:matrix.org >__ Once merged I dont see a problem as no one is going to match the compute of google, but in review limbo there is a race condition     

> __< syntheticbird >__ ack-j:matrix.org: Are there documentation about the computer power of oss-fuzz. I doubt they are giving a dedicated super computer to every open source project registered     

> __< ack-j:matrix.org >__ It should be noted that this doesn’t introduce any dependency on google and google has no admin access to the monero codebase. They simply clone the monero repo and run the fuzzing harnesses we developed at a massive scale. They do this for free since monero is FOSS     

> __< jberman >__ gingeropolous:monero.social has a nice cluster of solid hardware that could be useful here. Order of ops for p2p could be 1) develop it, 2) run the harnesses for x period of time using ginger's compute cluster, 3) once satisfied, open the PR     

> __< rucknium >__ Any other comments or questions on this topic?     

> __< davkor:mozilla.org >__ When we developed the previous harnesses we ran it for XXX amount of hours but also looked at when coverage increase in the harness was starting to slow down, and then determined they don't find any low hanging bugs     

> __< rucknium >__ davkor:mozilla.org: Thanks for your work and joining the meeting today. If people have more feedback or questions, how can they reach you? Through ack-j:matrix.org  ? Do you accept DMs to your Matrix account?     

> __< jberman >__ thank you davkor:mozilla.org !     

> __< davkor:mozilla.org >__ rucknium: they can reach me on david⊙ac -- writing to ack-j:matrix.org is also one way of getting through to me as we have communication channels open.     

> __< rucknium >__ Thank you.     

> __< rucknium >__ 4. P2Pool consolidation fees after FCMP hard fork. Coinbase Consolidation Tx Type (https://github.com/monero-project/research-lab/issues/108).     

> __< rucknium >__ I looked through some research papers on the subject. It seems that most papers don't try to fix p2pool. Instead, they suggest using an Ethereum-compatible smart contract:     

> __< rucknium >__ Luu, Velner, Teutsch, & Saxena (2017) "SmartPool: Practical Decentralized Pooled Mining"     

> __< rucknium >__ Troutman & Laszka (2021) "PoolParty: Efficient Blockchain-Agnostic Decentralized Mining Pool"     

> __< rucknium >__ Papathanasiou, Kyriakidou, Pittaras, & Polyzos (2024) "Smart contract-based decentralized mining pools for Proof-of-Work blockchains"     

> __< rucknium >__ Sakurai & Shudo (2025) "FiberPool: Leveraging Multiple Blockchains for Decentralized Pooled Mining"     

> __< rucknium >__ I haven't seen anything in these papers that completely satisfies me.     

> __< rucknium >__ And I don't know if anyone would be willing to try to implement and deploy something like that for Monero.     

> __< rucknium >__ Any more comments on this topic for now?     

> __< DataHoarder >__ Sorry, I was away     

> __< DataHoarder >__ I have been looking to do multisig consolidation under FCMP++ N-of-N with presigned txs (and proof done later?)     

> __< DataHoarder >__ No more that sketches, I have started implementing FCMP++ parts themselves to experiment. Will ask questions elsewhere if I have any     

> __< rucknium >__ Thanks, DataHoarder     

> __< jberman >__ nice!     

> __< DataHoarder >__ no HTLCs, so no tx invalidation, but chaining is workable with fallbacks for non-cooperation     

> __< jrkl23jlka >__ PTLCs?     

> __< rucknium >__ 5. Transaction volume scaling parameters after FCMP hard fork (https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-11.pdf). Revisit FCMP++ transaction weight function (https://github.com/seraphis-migration/monero/issues/44).     

> __< articmine >__ I have uploaded 2025-11-02, which is the latest update      

> __< articmine >__ I had the.  proposed most recent weight     

> __< rucknium >__ Resolving the scaling and fee parameters question is becoming more time-sensitive as other blockers for the second (and most likely final) FCMP stressnet are being successfully addressed.     

> __< articmine >__ Without the adjustments for powers of 2      

> __< jberman >__ I started reviewing the latest and will complete my initial review within the next couple days     

> __< articmine >__ Great      

> __< articmine >__ Any questions?     

> __< rucknium >__ jrkl23jlka: Did you want to comment in this agenda item?     

> __< jrkl23jlka >__ We'd like to make a suggestion on the transaction pool fee distribution functions, mostly unrelated to what is being proposed. The idea of quantisation is to increase anonymity set, by having different users pay the same fees and get mixed in.      

> __< jrkl23jlka >__ But an alternative (and NOT mutually exclusive with quantisation) is to bias the fee probability distribution function towards a uniform distribution (i.e., max entropy state, "white noise" full spectrum),     

> __< jrkl23jlka >__ while still permitting for transaction priority assignements--by placing transactions fees in the range that represents the priority of the transaction,      

> __< articmine >__ How does this work with a fee market!     

> __< jrkl23jlka >__ but at a finer resolution by specifically picking underrepresented fee values in the fee distribution, thus promoting that distribution to become more uniform,     

> __< jrkl23jlka >__ much more like a predictable transaction queue representing transaction priorities.     

> __< jrkl23jlka >__ Like that users picking fees in advance for offchain transactions (such as in payment channel or atomic swaps) won't be fingerprinted too badly.     

> __< articmine >__ So instead of have five fee levels we have 5 fee ranges     

> __< jrkl23jlka >__  In general, custom wallets picking "the wrong" fee values won't fingerprint their users too bad either because its easier to hide in white noise (=uniform distribution) than on an highly structured, deterministic function.     

> __< jrkl23jlka >__ And clearly this does not requires consensus, just real-time, transaction-pool / blockspace based market dynamics.     

> __< rucknium >__ They will be fingerprinted anyway since they will reference an outdated merkle state in the FCMP tree     

> __< articmine >__ Yes this is not consensus      

> __< jrkl23jlka >__ articmine: not really 5 ranges, all you are trying to do is get a flat fee distribution     

> __< articmine >__ It adds noise around the fee levels      

> __< rucknium >__ Custom wallet implementations that choose a deterministic fee would likely create spikes in the uniform distribution.     

> __< jrkl23jlka >__ independent of quantization levels (u could have many bins, or treat 1 piconero as a bin), and that would work too     

> __< jrkl23jlka >__ articmine: exactly, it adds WHITE noise around fees     

> __< articmine >__ It is actually very interesting      

> __< jberman >__ "They will be fingerprinted anyway since they will reference an outdated merkle state in the FCMP tree" -> this isn't necessarily accurate, you can pre-sign and construct the membership proof without needing the spend key later     

> __< rucknium >__ jberman:monero.social: Ah, thanks.     

> __< jrkl23jlka >__ rucknium: then other wallets fix those spikes by spreading transactions around     

> __< jrkl23jlka >__ and pushing those peaks on the pdfs down     

> __< jrkl23jlka >__ *probability density function     

> __< articmine >__ I proposed a 1000 block buffer for median changes over the current 10 block that should help with this      

> __< articmine >__ It does create time for this kind of distribution      

> __< rucknium >__ You're saying that wallet software should actively watch the recent distribution of fees. Maybe a node could cache that and share with wallets. But you would have to have a very limited number of ...     

> __< rucknium >__ Wait, it honest wallets can observe the spike and "correct" it, the an adversary would also be able to notice the spikes before they are corrected.     

> __< rucknium >__ if honest wallets*     

> __< articmine >__ The idea is to introduce noise. How statically sound this would be is a research project of it's own      

> __< articmine >__ Statistically*     

> __< jrkl23jlka >__ we are only talking about real-time fee dynamics     

> __< jrkl23jlka >__ not long-range as articmine     

> __< kayabanerve:matrix.org >__ davkor:mozilla.org: ack-j:matrix.org: As a note, I'd love to see monerod with musl (as on Alpine) tested. musl sets a much smaller stack size by default which makes monerod (at least in the past) not run properly. Using the fuzzer to ascertain stack size requirements so we can use libc calls to ensure that stack size is provided to each context would be great.     

> __< articmine >__ The good thing about this is that it can be implemented after the hard forl     

> __< kayabanerve:matrix.org >__ Sorry for the interjection     

> __< kayabanerve:matrix.org >__ jberman:monero.social: which is one of the reasons why weight must be independent of the layers, yep     

> __< articmine >__ jrkl23jlka: Yes like a day or so     

> __< articmine >__ Fees are based on the long term median so there is more room timewise      

> __< jrkl23jlka >__ we are talking about what is currently in the transaction pool      

> __< articmine >__ I don't see a problem here     

> __< jrkl23jlka >__ and fees should be based on market dynamics and transaction priorities, not history     

> __< jrkl23jlka >__ people would pay 50 usd in btc fees on a almost empty tx pool, because the transaction pool was crowed a few hours before, and the past was not the present     

> __< articmine >__ The fee is based upon the penalty that the transaction would attract.. This is part of the fee market      

> __< articmine >__ Then of course there is supply and demand      

> __< articmine >__ It is not like Bitcoin where increasing prices do not increase supply. In Monero increasing price does add block space      

> __< articmine >__ So supply is increased      

> __< jrkl23jlka >__ but its about transients in transaction numbers     

> __< jrkl23jlka >__ real-time, instantaneous fees     

> __< jrkl23jlka >__ not scalling     

> __< jrkl23jlka >__ over long time ranges     

> __< articmine >__ Yes that is also part of the picture      

> __< jrkl23jlka >__ anyway, i think i made myself clear. uniform distribution is where the we hide the best     

> __< articmine >__ The penalty is paid on the short term median which is 100 blocks      

> __< articmine >__ So there is very short term scaling      

> __< jrkl23jlka >__ it does not matter what happens 100 blocks ago, if the transaction pool is empty     

> __< articmine >__ About 100 minutes      

> __< jrkl23jlka >__ theres available block space and you can pay little fees     

> __< articmine >__ jrkl23jlka: The block size limit does depend on the recent and past history     

> __< jrkl23jlka >__ that is an almost orthogonal dimension     

> __< articmine >__ I can go over this with you      

> __< rucknium >__ Any more discussion of this item for now?     

> __< jrkl23jlka >__ no     

> __< rucknium >__ 6. FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< ofrnxmr >__ 1.5 coming soon. ooms largely fixed, i think     

> __< rucknium >__ jberman:monero.social already gave an update on stressnet improvements at the beginning of the meeting. Anything else?     

> __< ofrnxmr >__ My only q is wen carrot?  but jeffro not here     

> __< jberman >__ Trying to get 1.5 out in the next couple days that should address OOM's and slow sync     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< articmine >__ Thanks      

> __< DataHoarder >__ I'll take a look to the linked papers, rucknium. But as you said they just implement the logic elsewhere (and the few I found myself assume there is an automated chain bridge, centralized or not, to be able to pass rewards)     

> __< jrkl23jlka >__ thank you for the meeting     

> __< jrkl23jlka >__ DataHoarder: you talked about transaction chaining. how far are we from being able to do PTLCs?     

> __< jrkl23jlka >__ s/PTLCs/point-time locked contracts     

> __< jrkl23jlka >__ we need a per output timelock, any current proposals on that?     

> __*__ jrkl23jlka does not follow monero development closely, so lagging a few years behind     

> __< DataHoarder >__ I have not looked at that within the scope of Monero. This implementation also requires full verification by other parties, including ones not directly involved in the multisig (or at least verified origin). It also needs to be fast relatively, though it can be generated ahead of time     

> __< DataHoarder >__ I'd recommend then looking at atomic swaps jrkl23jlka      

> __< jrkl23jlka >__ what atomic swaps?     

> __< jrkl23jlka >__ the btc one was using 2 time locks on teh btc side      

> __< jack_ma_blabla:matrix.org >__ monero doesnt have HTLCs & isnt coming with fcmp++ fork      

> __< jrkl23jlka >__ but it can have PTLCs jack_ma_blabla     

> __< jrkl23jlka >__ instead of hiding a secret in a preimage of a hash, u hide it in a scalar that can be represented by an ec point. and u leak the scalar through adaptor signatures, like in the atomic swaps     

> __< rucknium >__ DataHoarder: DataHoarder: Thanks     

> __< gingeropolous >__ so a random update on monerosim, sorry i keep missing the meetings. have job job during that time. I was going down a tangent to try and get some mining shim to work from within monerod. I'm going to abandon that and go back to getting the block controller version polished and ready for general use, because I think it might be [... too long, see https://mrelay.p2pool.observer/e/zqmHvsoKTk1vWTdM ]

# Action History
- Created by: Rucknium | 2025-11-18T22:39:59+00:00
- Closed at: 2025-11-28T20:47:18+00:00
