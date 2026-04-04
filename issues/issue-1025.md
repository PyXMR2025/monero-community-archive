---
title: Monero Research Lab Meeting - Wed 19 June 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1025
author: Rucknium
assignees: []
labels: []
created_at: '2024-06-19T15:17:31+00:00'
updated_at: '2024-07-02T21:04:38+00:00'
type: issue
status: closed
closed_at: '2024-07-02T21:04:38+00:00'
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

5. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html).

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1022 

# Discussion History
## Rucknium | 2024-06-21T19:22:40+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1025     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< isthmus >__ Heya     

> __< rbrunner >__ Hello     

> __< k​ayabanerve:monero.social >__ 👋     

> __< vtnerd >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< spackle >__ hi     

> __< isthmus >__ I did some more work on/with my library for detecting a particular anomaly created by some non-wallet2 codebase that caches decoys and reuses them (across hundreds or thousands of transactions) https://pypi.org/project/ringxor/     

> __< r​ucknium:monero.social >__ me: Mostly Stressnet things. I wrote a Shiny app to collect and display stressnet data at https://monitor.stressnet.net/ . Set up a stressnet explorer at https://explorer.stressnet.net/ . Wrote a transaction spamming script ( + tested jeffro256 's new feature to make "outputs pay for fees" in a tx).     

> __< jberman >__ me: continued the fcmp trim_tree algo implementation     

> __< k​ayabanerve:matrix.org >__ I presented at Monerokon and have an update on Veridise.     

> __< rbrunner >__ Hmm, that stressnet explorer gives me "502 Bad Gateway" right now. Already spammed to death? :)     

> __< r​ucknium:monero.social >__ 3) Stress testing `monerod` https://github.com/monero-project/monero/issues/9348     

> __< spackle >__ testing is in progress     

> __< vtnerd >__ I finished stress testing LWS remote scanning. Everything looked as expected except for one outstanding bug report (unrelated to remote scanning). Still waiting to hear back on that     

> __< r​ucknium:monero.social >__ The node died earlier. Maybe the explorer is dead too. `xmrblocks uses more RAM and CPU than I expected.     

> __< vtnerd >__ also working on updating the serialization code again, will probably reduce the one PR a bit so that hopefully some more reviews (other than jeffro, thanks!) will come in     

> __< e​msczkp:matrix.org >__ Hi everyone, I hope my message gets through. I'm Emanuele Ph.D, I worked on the implementation of the compressed sigma-ipa and compared it with bp ipa     

> __< r​ucknium:monero.social >__ We already got reliable reproduction of out-of-memory error when a stressnet node has lots of connections: https://github.com/monero-project/monero/issues/9348#issuecomment-2170629015     

> __< r​ucknium:monero.social >__ By boog900     

> __< r​ucknium:monero.social >__ emsczkp: Hi! Do you want to bring up a topic at this meeting again? More discussion from you is welcome :) Maybe you can discuss at the FCMP agenda item     

> __< r​ucknium:monero.social >__ Any Monero protocol developers who want to test performance patches can sync a node to stressnet. It's a good time now to test. AFAIK we want to run stressnet for about two months. Discussion happens in #monero-stressnet:monero.social  and ##monero-stressnet on IRC     

> __< 0​xfffc:monero.social >__ ( hi )     

> __< e​msczkp:matrix.org >__ thanks you r​ucknium, i'll discuss at point FCMP     

> __< rbrunner >__ Is the traffic on stressnet now "at maximum" already?     

> __< r​ucknium:monero.social >__ No. I don't know where the maximum will be, but spackle is still sending out txs     

> __< rbrunner >__ Or all there plans to make happenings like "Now all we all spam together"?     

> __< rbrunner >__ Alright, will follow the Matrix room to learn more!     

> __< r​ucknium:monero.social >__ AFAIK, the spam timing will be loosely coordinated. Probably spackle can spam enough all by himself, but others can add more.     

> __< rbrunner >__ Don't want to complain, but a single source of transactions is probably ... not very typical :) Except if we have a spam wave, that is     

> __< r​ucknium:monero.social >__ That is true. I have 50,000 outputs ready to go into a spamming cycle. That would be about 75MB of txs in the txpool. The stressnet spamming started about two hours ago. I think we will see how things go and adjust.     

> __< r​ucknium:monero.social >__ 4) Potential measures against a black marble attack  https://github.com/monero-project/research-lab/issues/119     

> __< r​ucknium:monero.social >__ I don't really have anything to add to this agenda item right now. I think I will have the update that gives Alice a budget constraint by next meeting.     

> __< r​ucknium:monero.social >__ 5) Research Pre-Seraphis Full-Chain Membership Proofs.  https://www.getmonero.org/2024/04/27/fcmps.html     

> __< r​ucknium:monero.social >__ kayabanerve: , emsczkp     

> __< k​ayabanerve:monero.social >__ Veridise has completed a proof of the divisor technique. Their proof does force modifications to my R1CS gadget yet nothing notable here. I hope to, by next meeting, have a quote for the review of the proofs.     

> __< a​aron:cypherstack.com >__ Is this publicly available?     

> __< r​ucknium:monero.social >__ Fantastic!     

> __< k​ayabanerve:monero.social >__ Review of the R1CS gadget, as a specification, may or may not fit into the allocated hours. It may require an extension, say +5h (of 24h allocated) which would incur a further cost.     

> __< k​ayabanerve:monero.social >__ The R1CS gadget, which needs updates, accordingly may be done on a distinct contract OR the work there will continue next week on the current SoW, once I do my updates. We're seeing what's best now.     

> __< e​msczkp:matrix.org >__ I just wanted to say that my implementation shows a 50% optimization on verification times compared to the BP's IPA     

> __< k​ayabanerve:matrix.org >__ Aaron Feickert: Not yet. I asked for them to clarify some ambiguous notation. It's not breaking, it's just a bit wonky to read. Once I have that final PDF, or at least their confirmation that the one thus far shared is okay to publish (not an internal preprint), I'll share it. Ideally a day or two.     

> __< k​ayabanerve:matrix.org >__ emsczkp: Would you please share a link and clarify if you're delaying the verification to a final multiexp or not?     

> __< k​ayabanerve:matrix.org >__ (to the implementation. I'd be shocked if saving the inversions was so impactful)     

> __< e​msczkp:matrix.org >__ I can share the repositories. Just a second, I'll make it public. I haven't implemented the multi-exp version yet and I'm working on it     

> __< k​ayabanerve:matrix.org >__ I'll further clarify I'm holding off on soliciting quotes for further review until I do have the PDF to be shared, as necessary to get quotes. So ideally, in a day or two I can solicit quotes, and ideally we have them Monday for the meeting Wednesday? That somewhat applies weekend quotes, so the review quotes may be up to the wire on the meeting :/ Apologies.     

> __< r​ucknium:monero.social >__ kayabanerve: That sounds good to me. Thanks for doing all the coordination.     

> __< e​msczkp:matrix.org >__ this is the repo https://github.com/EmanueleSc/IV-IPA/ , the name is misleading because it would be the final idea... meanwhile "inner-sigma" i.e., the compressed sigma-ipa, and "inner" i.e., the BP IPA are implemented. I can share screenshots of benchmarks     

> __< a​aron:cypherstack.com >__ Is this approach formalized anywhere?     

> __< k​ayabanerve:monero.social >__ I'm also soliciting review of the GBP proofs, and have been for a week or so. There's one candidate in mind so I'm hoping that works out. Else, it'll be another candidate spread, likely Goodell and one or two other groups.     

> __< r​ucknium:monero.social >__ Aaron Feickert:  Scala, E., & Mostarda, L. 2024, Efficient inner-product argument from compressed $sigma$-protocols and applications. Paper presented at International Conference on Advanced Information Networking and Applications.  https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=221     

> __< e​msczkp:matrix.org >__ yes, the approach is formalized here https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=221&browserTabID=     

> __< k​ayabanerve:monero.social >__ With GBP proof review, we can move to auditing. With the divisor gadget also signed off on, we can move to its entire circuit?     

> __< r​ucknium:monero.social >__ ^ I think that's the paper     

> __< k​ayabanerve:monero.social >__ So progress being made on a few ends there.     

> __< k​ayabanerve:matrix.org >__ I'll ask Aaron Feickert, who is welcome to reply privately, if     

> __< k​ayabanerve:matrix.org >__ 1) They're happy with the notation in their proofs and are fine with me sending them off as-is. I assume so yet will double check.     

> __< k​ayabanerve:matrix.org >__ 2) They reached out to the original authors (_and_ specifically noted the H_i extraction)     

> __< k​ayabanerve:matrix.org >__ Oh, and 3) If they can confirm again (I did ask back in the day), the cross-product issue preventing more efficient H_i extraction is non-trivial and we should move forward with the protocol as-is.     

> __< a​aron:cypherstack.com >__ 1. The report made available at the CS repository should be fine for review by anyone interested.     

> __< a​aron:cypherstack.com >__ 2. We did reach out to the original authors (in early May), but did not hear back.     

> __< a​aron:cypherstack.com >__ 3. Correct, but I would be thrilled if someone found a way around this limitation :D     

> __< k​ayabanerve:matrix.org >__ In that case, I won't push it and will move forward with review as-is.     

> __< a​aron:cypherstack.com >__ That being said, I'd be shocked if there weren't typos in the notation somewhere...     

> __< a​aron:cypherstack.com >__ (but there are none I know of)     

> __< k​ayabanerve:matrix.org >__ I want to personally try out the above IP A, as an experiment on the verification times, as it'd save a few inversions. The claims of saving verifier scalings/50% are presumed notational artifacts at this time and not expected IRL.     

> __< k​ayabanerve:matrix.org >__ I literally implemented it off your notation >:(     

> __< k​ayabanerve:matrix.org >__ That implies correctness     

> __< k​ayabanerve:matrix.org >__ Or dyslexia on my end.     

> __< a​aron:cypherstack.com >__ Heh, I mean typos in general. Sorry, didn't mean to imply more!     

> __< e​msczkp:matrix.org >__ k​ayabanerve explains so will you test the solution?     

> __< e​msczkp:matrix.org >__ sorry but I always have the "federation problem" on the server and it's difficult to follow the chat perfectly     

> __< k​ayabanerve:matrix.org >__ https://libera.monerologs.net/monero-research-lab/20240619     

> __< k​ayabanerve:matrix.org >__ Refresh that every minute or so, as a workaround     

> __< k​ayabanerve:matrix.org >__ I will try it out with FCMPs specifically, as an experiment. If it saves a sufficiently notable amount of time, I'd likely request quotes as necessary to evaluate if we have the bandwidth to also move forward with it.     

> __< e​msczkp:matrix.org >__ ok thanks for the effort, I'm waiting for news and I hope that my contribution is the one expected in order to move forward     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< k​ayabanerve:matrix.org >__ I'd likely need to see those inversions save 5-10+%. The inversions are expensive, yet I'm not convinced they sufficiently weigh considering the amount of scalar matrix muls we currently face.     

> __< k​ayabanerve:matrix.org >__ That's off the total proof, not just the IPA.     

> __< r​ucknium:monero.social >__ Discussion can continue of course :)     

> __< e​msczkp:matrix.org >__ kayabanerve: Do you have a formal specification I can refer to? I would like to know more     

> __< e​msczkp:matrix.org >__ I know you have implemented bp+ , and are addressing GBP. I would like to have some material if possible     

> __< a​aron:cypherstack.com >__ You mean IPA challenge inversions? Those can also be batched, so as to replace multiple inversions with a single inversion and sequence of multiplications     

> __< a​aron:cypherstack.com >__ (assuming this is what you meant)     

> __< k​ayabanerve:monero.social >__ My looking into spending the time and effort on this, which expends limited bandwidth, would likely have the aforementioned reward necessary. The current IPA proof itself is available at     

> __< k​ayabanerve:monero.social >__ https://github.com/kayabaNerve/fcmp-plus-plus/blob/develop/crypto/generalized-bulletproofs/src/inner_product.rs     

> __< k​ayabanerve:matrix.org >__ I'm pulling up the benchmark command, one moment...     

> __< k​ayabanerve:matrix.org >__ Sorry, I became quite distracted. I sent on monero.social the link to the current IPA (see logs). The benchmarks can be run with `cargo test --all-features -p full-chain-membership-proofs -- --nocapture` from https://github.com/kayabaNerve/fcmp-plus-plus/.     

> __< k​ayabanerve:matrix.org >__ emsczkp:     

> __< e​msczkp:matrix.org >__ Thank you for the repo, i'll do some experiments on the ipa     

> __< k​ayabanerve:matrix.org >__ *--release     

> __< k​ayabanerve:matrix.org >__ One should also benchmark with the `--release` flag, added after `test` in the above command.   

# Action History
- Created by: Rucknium | 2024-06-19T15:17:31+00:00
- Closed at: 2024-07-02T21:04:38+00:00
