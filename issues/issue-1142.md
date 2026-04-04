---
title: Monero Research Lab Meeting - Wed 15 January 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1142
author: Rucknium
assignees: []
labels: []
created_at: '2025-01-15T15:15:37+00:00'
updated_at: '2025-01-23T19:09:46+00:00'
type: issue
status: closed
closed_at: '2025-01-23T19:09:46+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Generalized Bulletproofs implementation audit](https://github.com/cypherstack/generalized-bulletproofs-code).

4. [FCMP++ tx size and compute cost](https://gist.github.com/kayabaNerve/c42aeae1ae9434f2678943c3b8da7898). [On MAX_INPUTS and MAX_OUTPUTS](https://gist.github.com/kayabaNerve/dbbadf1f2b0f4e04732fc5ac559745b7). [Monero FCMP MAX_INPUTS/MAX_OUTPUTS empirical analysis](https://gist.github.com/Rucknium/784b243d75184333144a92b3258788f6). [LATEST BENCHMARKS](https://github.com/jeffro256/clsag_vs_fcmppp_bench)

5. [Discussion: Post-quantum security and ethical considerations over elliptic curve cryptography](https://github.com/monero-project/research-lab/issues/131)

6. Any other business

7. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1138 

# Discussion History
## Rucknium | 2025-01-21T19:53:06+00:00
Logs

> __< r​ucknium:monero.social >__ MRL meeting in this room in about two hours.     

> __< s​agewilder:unredacted.org >__ Is this meeting open to external attendees?     

> __< r​ucknium:monero.social >__ sagewilder: Yes, always :)     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1142     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< s​yntheticbird:monero.social >__ Hi     

> __< s​yntheticbird:monero.social >__ first     

> __< v​tnerd:monero.social >__ hi     

> __< j​effro256:monero.social >__ Howdy     

> __< rbrunner >__ Hello     

> __< j​berman:monero.social >__ *waves*     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< j​effro256:monero.social >__ Carrot integration & benchmarking, FCMP++ benchmarking, reviewing FCMP++ integration     

> __< j​berman:monero.social >__ me: constructing and verifying FCMP++ proofs over the FFI is working, cleaning it up and organizing functions now, aiming to roll up wallet sync + FCMP++ prove/verify into the WIP PR     

> __< v​tnerd:monero.social >__ bug fixes for monerod     

> __< r​ucknium:monero.social >__ me: Submitted Milestone 2 of OSPEAD to the review panel. That's the initial improved decoy selection algorithm with all the code to statistically estimate it. Probably I will post it publicly in about a month. In the meantime, if any devs or researchers want a copy, let me know. I may discuss preliminary results next meeting.     

> __< r​ucknium:monero.social >__ 3) Generalized Bulletproofs implementation audit. https://github.com/cypherstack/generalized-bulletproofs-code     

> __< r​ucknium:monero.social >__ Anything to say about the audit?     

> __< c​haser:monero.social >__ it was a Christmas present to MRL.     

> __< j​berman:monero.social >__ The audit highlighted areas that could have more tests, I figure it would be nice if someone wanted to pick that up     

> __< r​ucknium:monero.social >__ Sounds good :)     

> __< r​ucknium:monero.social >__ 4) FCMP++ tx size and compute cost. On MAX_INPUTS and MAX_OUTPUTS. Monero FCMP MAX_INPUTS/MAX_OUTPUTS empirical analysis. LATEST BENCHMARKS: https://github.com/jeffro256/clsag_vs_fcmppp_bench     

> __< j​effro256:monero.social >__ From the results that I obtained on an AMD CPU and Intel CPU that I own, plus the results that other people have sent me, the speed for an 8-input FCMP++ transaction is the same as a 47-52 input CLSAG. Likewise, a 16-input FCMP++ transaction is the same as a 94-101 input CLSAG     

> __< r​ucknium:monero.social >__ From my read of the benchmarks, FCMP input proofs with a larger number of inputs are actually more efficient to verify than those with a smaller number of inputs. Am I missing something?     

> __< r​ucknium:monero.social >__ More efficient per input I mean     

> __< j​effro256:monero.social >__ Yes, but the effect seems start to to taper off after 8-input and they don't get much more efficient per-input after that     

> __< r​ucknium:monero.social >__ So the only issue is the initial verification for txpool and relay, which can be large for a tx with many inputs. The verification of a block with these txs would actually be more efficient with large number of inputs instead of breaking up the enote consolidation     

> __< r​ucknium:monero.social >__ And the main issue with txpool/relay is a malicious actor trying to DDoS a node with bad proofs, right?     

> __< j​effro256:monero.social >__ I'd have to check multi-tx batch times. I don't know if it improves the per-tx verification time or not.     

> __< j​effro256:monero.social >__ But yes the main goal with this whole affair of limiting input counts is to prevent DoS attacks with bad proofs     

> __< r​ucknium:monero.social >__ Does sech1 want to say something about this?     

> __< j​effro256:monero.social >__ If 100-input CLSAGs are acceptable now, I'd say we should allow 16-input FCMP++s     

> __< rbrunner >__ How limiting is that really? If I want to attack, and I am only allowed 4 inputs instead of 8, can't I simply send twice the number of transactions for the same effect?     

> __< sech1 >__ I can only repeat that comparing (supposedly) unoptimized FCMP++ code with an optimized production CLSAG code can be misleading     

> __< sech1 >__ I expect FCMP++ will get faster     

> __< r​ucknium:monero.social >__ Probably. Maybe could go even higher to 32.     

> __< j​effro256:monero.social >__ rbrunner: it does increase the latency between the time you sent the first one, and the time that we decide that we can ban you for X amount of time     

> __< r​ucknium:monero.social >__ rbrunner: I guess your node would get banned after the first bad tx     

> __< j​effro256:monero.social >__ Yes, I only expect FCMP++ to get faster, especially with high-performance field arithmetic     

> __< r​ucknium:monero.social >__ If FCMP verification gets faster, it should be worked on soon because the audits should audit optimized code.     

> __< rbrunner >__ Hmmm, but if you block me possibly after only a few bad apples, it again does not matter much how long that takes? Or do you think of attackers with hundreds of nodes at hand?     

> __< r​ucknium:monero.social >__ I don't like the idea of auditing an unoptimized implementation and deployed an optimized, unaudited one. But maybe others disagree.     

> __< rbrunner >__ I agree, auditing first and then tinker with the code further does not sound like the best of ideas ...     

> __< s​yntheticbird:monero.social >__ what about releasing unoptimized and next hard fork deploy the optimized + audited one     

> __< c​haser:monero.social >__ IMHO that could erode the margin of safety, as well as miss the opportunity to gradually decrease the number of possible tx shapes as part of the longer-term goal of increasing tx uniformity.     

> __< sech1 >__ It needs to be reasonably optimized before the audit. Reasonable = no crazy optimizations that hurt readability/maintainability, and no assembly code     

> __< j​berman:monero.social >__ The "unoptimized" part of the code expected to be sped up (via a contest, ideally) is sectioned off from other sections slated for immediate auditing I'm pretty sure. I'm generally content with putting more pressure on optimizing sooner rather than later though, the contest has been on the back of my mind     

> __< r​ucknium:monero.social >__ Should the contest be set up? Any issues holding it up?     

> __< s​agewilder:unredacted.org >__ Well it was supposed to be KayabaNerve organizing it, before the stepping back     

> __< s​agewilder:unredacted.org >__ I was interested. But no news since.     

> __< rbrunner >__ Was the idea to get the "award money" through a CCS? Or out of some already existing fund?     

> __< j​berman:monero.social >__ I can come back next week with a stronger fleshed out proposed next steps     

> __< r​ucknium:monero.social >__ jberman: Great. Thanks!     

> __< s​yntheticbird:monero.social >__ 0xfffc got competition     

> __< s​agewilder:unredacted.org >__ There were others known to be interested ?     

> __< s​yntheticbird:monero.social >__ Yes     

> __< r​ucknium:monero.social >__ I guess where we are in the MAX_INPUTS discussion is being thankful that jeffro256 set up the benchmark repo, then the code optimizations can be easily put into the repo when they are ready. Then a decision can be made based on the new benchmarks.     

> __< r​ucknium:monero.social >__ I could re-run my empirical analysis https://gist.github.com/Rucknium/784b243d75184333144a92b3258788f6 with the new jeffro256 benchmarks, too.     

> __< j​effro256:monero.social >__ Thanks for doing those calculations, having optimal consolidation times laid out like this is helpful     

> __< rbrunner >__ I wonder how far wallet app implementers will go supporting automatic consolidations, at least in early FCMP++ supporting versions     

> __< r​ucknium:monero.social >__ Probably "DAEMON: Transaction rejected" :P     

> __< r​ucknium:monero.social >__ As in, some of them won't realize there is a limit     

> __< r​ucknium:monero.social >__ Any more comments on this issue?     

> __< rbrunner >__ Lol     

> __< s​yntheticbird:monero.social >__ none that contribute     

> __< r​ucknium:monero.social >__ 5) Discussion: Post-quantum security and ethical considerations over elliptic curve cryptography https://github.com/monero-project/research-lab/issues/131     

> __< s​yntheticbird:monero.social >__ It's maths time!     

> __< rbrunner >__ Seem to wait for the next company to announce some step forward towards QC, to get to the top of people's minds again ...     

> __< s​yntheticbird:monero.social >__ rbrunner im already haunted, no need to add more     

> __< s​yntheticbird:monero.social >__ Kinda have to admit this section of the meeting is a little empty without Jeffro and Kayaba brainstorming     

> __< s​yntheticbird:monero.social >__ god bless cryptography nerds     

> __< j​effro256:monero.social >__ lol     

> __< j​effro256:monero.social >__ I wanted to throw up a point for discussion as it relates to how the generate-address wallet tier and quantum migrations interact     

> __< s​yntheticbird:monero.social >__ feel free     

> __< c​haser:monero.social >__ rbrunner: I think we're rather waiting for better/optimized signature algorithms to be invented.     

> __< s​yntheticbird:monero.social >__ chaser: kayabanerve just told let me a big NO. But i'm interested if PQ exchange can be done with KEM, because they generally have smaller sizes     

> __< j​effro256:monero.social >__ Basically, if a quantum computer sees any one of your Monero addresses, then they can 1) see all incoming enotes to that account, and 2) see where those incoming enotes were spent, if 2 enotes addressed to the same subaddress were spent more than once     

> __< c​haser:monero.social >__ "big NO" as to what?     

> __< j​effro256:monero.social >__ The generate-address tier with a quantum computer would be able to trim that down to seeing where incoming enotes are spent if they're spent at all     

> __< r​ucknium:monero.social >__ "if 2 enotes addressed to the same subaddress were spent more than once " Do not necessarily have to be spent in the same tx, right?     

> __< s​yntheticbird:monero.social >__ jeffro256: They can see all incoming enotes from the moment they break your address. Or the entirety of the incoming history?     

> __< j​effro256:monero.social >__ Nope, they can be spent anywhere on the chain     

> __< j​effro256:monero.social >__ They entirety of the incoming history, not including change and other self-sends     

> __< r​ucknium:monero.social >__ Does this mean....PQ churning defense!?!?     

> __< s​yntheticbird:monero.social >__ I feel like until we get some miracle PQ DSA, wallet will need to self-send automatically on receive then     

> __< j​effro256:monero.social >__ So there's a question on whether we should officially support delegated subaddress generation, since they get a more privileged look into the wallet history as compared to a normal external observer     

> __< j​effro256:monero.social >__ YES     

> __< s​yntheticbird:monero.social >__ Mind explaining for the mortals?     

> __< c​haser:monero.social >__ ...which is not so different from tevador's Monero Checks 😔     

> __< r​ucknium:monero.social >__ Churning was hypothesized to be a defense against ring signature analysis. And it may have a role even after FCMP activation, as a defense against quantum computers     

> __< j​effro256:monero.social >__ This is a good mitigation that hides the flow of funds out of the account. A PQ would still know which transactions you received XMR from other and which amounts, but then the trail would go cold     

> __< r​ucknium:monero.social >__ IIRC, there was s discussion on the Zcash forums about churning to defend against quantum computers, even for their shielded protocol     

> __< s​yntheticbird:monero.social >__ I didn't know that. Has this been discussed before? I would like to check moredetails     

> __< s​yntheticbird:monero.social >__ ah ok yes     

> __< rbrunner >__ With so much larger tx sizes, and so much longer verification times, making wallets to churn anything incoming automatically? Sounds like a hard sell to me     

> __< s​yntheticbird:monero.social >__ rbrunner i agree i feel the concern     

> __< rbrunner >__ Imagine receiving something on a non-high-end-smartphone taking a minute     

> __< j​effro256:monero.social >__ It's mentioned in the Carrot document, but I suck at writing so people didn't pick it up probably even if they read that     

> __< s​yntheticbird:monero.social >__ Monero, the money for rich people because poor cannot compute     

> __< c​haser:monero.social >__ jeffro: I picked it up, I think it was tangible     

> __< s​yntheticbird:monero.social >__ To answer your original question jeffro256: Yes i think we should officially support it. I don't mind supporting something that relies on Trust. As long as people are aware of it.     

> __< r​ucknium:monero.social >__ These posts:     

> __< r​ucknium:monero.social >__ https://forum.zcashcommunity.com/t/is-zcash-actually-quantum-private/40706     

> __< r​ucknium:monero.social >__ https://forum.zcashcommunity.com/t/churning-zcash-for-maximum-anonymity-and-privacy/40705     

> __< s​yntheticbird:monero.social >__ thx u so much     

> __< c​haser:monero.social >__ IMHO if removing delegated address generation hides a greater section of the tx graph from a QC, it's a worthwhile trade-off.     

> __< r​ucknium:monero.social >__ I need a reminder. How is the address generation delegation wallet tier different from current view keys?     

> __< s​yntheticbird:monero.social >__ Isn't delegation subaddress generation just about generating new subaddresses and thats all ?     

> __< r​ucknium:monero.social >__ Would that take away useful features from merchants?     

> __< j​effro256:monero.social >__ rbrunner: regarding churning costs, if you are receiving lots of inputs, you can do batch consolidation like how Rucknium laid out. You wouldn't really lose any privacy this way either since a quantum computer with your public address already knows you own all your incoming enotes     

> __< j​effro256:monero.social >__ For a classical computer, giving them the generate-address secret lets them generate subaddresses for you and gain *NO* on-chain information about transaction history     

> __< j​effro256:monero.social >__ Versus today, if you can generate addresses for them, you can also view-scan their wallet     

> __< r​ucknium:monero.social >__ Isn't it better to keep the generate-address tier because it protects merchants even more from a classical computer? And quantum computer risk is still speculative?     

> __< j​effro256:monero.social >__ That's a good point     

> __< j​effro256:monero.social >__ The goal for the generate-address tier was to make PoS systems or invoicing systems that are more secure, not needing private key info     

> __< j​effro256:monero.social >__ And using subaddresses instead of integrated addresses     

> __< rbrunner >__ Which is a solid win, right?     

> __< j​effro256:monero.social >__ Integrated addresses already fill this role, but they have their own issues     

> __< s​yntheticbird:monero.social >__ Is there loose consensus for keeping generate address tier then ?     

> __< rbrunner >__ Handling Monero is complex. Everything that simplifies is very welcome IMHO. Giving that up again for a spectre that may come to hount us in 10 or even 20 years - or maybe never?     

> __< c​haser:monero.social >__ it's a win for the merchant, a lose for current-era Monero users if/when quantum adversaries look at the blockchain.     

> __< c​haser:monero.social >__ and the blockchain doesn't forget     

> __< s​yntheticbird:monero.social >__ a lose only if they make use of it     

> __< s​yntheticbird:monero.social >__ which most users won't     

> __< c​haser:monero.social >__ hmm     

> __< r​ucknium:monero.social >__ Isn't it a loss only for people who use that tier _and_ the key information in that tier falls into the hands of an adversary?     

> __< s​yntheticbird:monero.social >__ Rucknium yes     

> __< r​ucknium:monero.social >__ Put it in a footnote in the docs and keep it :D     

> __< s​yntheticbird:monero.social >__ exactly     

> __< s​yntheticbird:monero.social >__ only real users are merchants and they are already vulnerable to this since they provide public addresses to pay them     

> __< c​haser:monero.social >__ ok, so it's basically a choice for the merchant as to which kind of risk to go with, and not a risk for the customer     

> __< j​effro256:monero.social >__ It would be a new risk to customer if the adversary knew the customers and the merchants public address, and the customer used the generate-address tier and that tier fell into the hands of the adversary, and the customer spent their money received from somewhere else into an address with only one spent into that merchants address     

> __< j​effro256:monero.social >__ Then the adversary could track the flow of funds from the customer to the mercant, whereas they wouldn't have been able to if the customer wasn't using the generate-address tier     

> __< r​ucknium:monero.social >__ Let's assume independence of events and multiply probabilities of each to see how likely that is :D     

> __< s​yntheticbird:monero.social >__ lmao     

> __< r​ucknium:monero.social >__ Thanks for the attention to detail, jeffro     

> __< s​yntheticbird:monero.social >__ yup     

> __< r​ucknium:monero.social >__ But they could do that anyway with the status quo view key tier, right?     

> __< rbrunner >__ It does get a bit extreme now with the scenarious :)     

> __< r​ucknium:monero.social >__ I mean, they will see the txs come in without a QC if they had the view key     

> __< j​effro256:monero.social >__ Well before FCMP++, all transactions will be traceable even without knowledge of any addresses     

> __< j​effro256:monero.social >__ (if you have a QC)     

> __< s​yntheticbird:monero.social >__ (((DLog solver under parentheses)))     

> __< j​effro256:monero.social >__ haha     

> __< j​effro256:monero.social >__ Yes, and also they can mainly see outgoing with ring signatures     

> __< j​effro256:monero.social >__ Because of probability and such     

> __< r​ucknium:monero.social >__ I mean, with a hypothetical FCMP view key without the address-generation tier. Merchants have to generate addresses somehow, unless they use integrated addresses     

> __< r​ucknium:monero.social >__ Or have a static address and track payments some other way.     

> __< j​effro256:monero.social >__ Yes. No QC, FCMP++, with private view-incoming key, one would be able to see all incoming enotes     

> __< s​yntheticbird:monero.social >__ We should get a QC just to automatically generate the gf transparency report     

> __< j​effro256:monero.social >__ What a lot of merchant software does to avoid integrated addresses and giving up that view key is to pregenerate thousands of addresses beforehand, and then load all those onto the frontend     

> __< r​ucknium:monero.social >__ Then an adversary could exhaust them by creating bogus invoices. But maybe adversaries have better things to attack     

> __< j​effro256:monero.social >__ Exactly     

> __< j​effro256:monero.social >__ Depends on how cheap it is to spam create invoices and how much they dislike this merchant     

> __< r​ucknium:monero.social >__ Let's end the meeting here. Feel free to continue discussing.     

> __< s​yntheticbird:monero.social >__ delicious meeting     

> __< v​tnerd:monero.social >__ late as per usual, was reading over the carrot spec again. I’m still in favor of the generate-address tier, despite the drawbacks mentioned     

> __< v​tnerd:monero.social >__ the majority of users won’t really run into an issue where it will matter either     

> __< s​agewilder:unredacted.org >__ Apologies if this isn't the right channel, but do you have an ETA for the FCMP++ in testnet?     

> __< s​yntheticbird:monero.social >__ in between 1 to 2 months iirc     

> __< s​yntheticbird:monero.social >__ if not i'll cry     

> __< j​berman:monero.social >__ I think we can get to *a* testnet in 1 to 2 months, but not pushing for the official testnet, because I figure we'd want code review / audits completed before deploying to testnet     

> __< j​berman:monero.social >__ When I say *a* testnet, I mean something like the stressnet     

> __< s​yntheticbird:monero.social >__ seems fair     

> __< s​yntheticbird:monero.social >__ I would have expected testnet to be more stressnet and stagenet to be what you call official testnet tho     

> __< s​agewilder:unredacted.org >__ It won't be a long wait, then.     

> __< j​berman:monero.social >__ From these docs (https://docs.getmonero.org/infrastructure/networks/), the testnet is for experimental release before mainnet (ideally I figure we want 1 testnet release, with code lined up ready to go), stagenet is supposed to be for app devs using monero (so stagenet expects mainnet parity)     

> __< rbrunner >__ "in between 1 to 2 months iirc" Is that a jberman estimate? Or jberman + jeffro256? Sounds a bit optimistic to me, frankly.     

> __< s​yntheticbird:monero.social >__ rbrunner you are pessimistic.     

> __< rbrunner >__ Right.     

> __< s​yntheticbird:monero.social >__ it's because of people like you that we stopped music in elevator     

> __< rbrunner >__ ?     

> __< s​yntheticbird:monero.social >__ idk something something not happy. I missed the joke sry     

> __< rbrunner >__ Ok :)     

> __< s​yntheticbird:monero.social >__ yeah ok make sense, another detached testnet  would make sense     

> __< rbrunner >__ No, I think it's ok to set ambitious goals among devs, e.g. as a motivation, but they can leak out e.g. to Reddit and rise unreasonable expectations there     

> __< rbrunner >__ Unfortunately     

> __< j​berman:monero.social >__ that's a me estimate, I'm not sure how long carrot integration would take but it sounds mostly ready     

> __< s​yntheticbird:monero.social >__ As redditor in denial, I disagree with you (I'm in denial)     

> __< o​frnxmr:monero.social >__ https://www.youtube.com/watch?v=u8Kt7fRa2Wc rbrunner     

> __< j​effro256:monero.social >__ Carrot integration into `wallet2`, without Carrot key hierarchy migration, is definitely achievable within the next month     

> __< rbrunner >__ o​frnxmr: Didn't know those "expert" videos yet, they are cool    


# Action History
- Created by: Rucknium | 2025-01-15T15:15:37+00:00
- Closed at: 2025-01-23T19:09:46+00:00
