---
title: Monero Research Lab Meeting - Wed 01 July 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1415
author: Rucknium
assignees: []
labels: []
created_at: '2026-07-01T14:55:06+00:00'
updated_at: '2026-07-09T19:23:57+00:00'
type: issue
status: closed
closed_at: '2026-07-09T19:23:57+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [emsczkp research Bulletproofs* Milestone 2 completed](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626#note_36734).

4. [Post-quantum encryption](https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686). [Jamtis](https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#appendix-c-instant-sync-protocol).

5. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/).

6. [`monerosim`](https://github.com/Fountain5405/monerosim).

7. Any other business

8. Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs: #1410  

# Discussion History
## Rucknium | 2026-07-07T19:36:09+00:00
Logs

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1415     

> __< rucknium >__ 1. Greetings     

> __< neptunian:unredacted.org >__ Hello, all.     

> __< syntheticbird >__ Hi     

> __< rbrunner >__ Hello     

> __< emsczkp:matrix.org >__ hello     

> __< redsh4de:matrix.org >__ Hi     

> __< jberman >__ waves     

> __< vtnerd >__ hi     

> __< jeffro256 >__ Howdy     

> __< boog900 >__ Hi     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< rucknium >__ me: Keeping stressnet stressed and investigating bugs.     

> __< sgp_ >__ Hello     

> __< vtnerd >__ me: going through claude reports (via sgp_) on monero-lws, lwsf, and fhse repos     

> __< neptunian:unredacted.org >__ Some FHE shenanigans and stuff related to Raccoon-G.     

> __< jeffro256 >__ me: reworked a large portion of the Carrot libraries to support making OutProofV2 proofs to selfsends (currently possibly but unused behavior in wallet2)     

> __< jberman >__ Me: finalized the first set of FCMP++ integration PR's that were audited (thank you to UkoeHB  for reviewing), continued investigating rucknium:monero.social 's observed sporadic wallet errors (the double spend issue) and identified a bug and suspected culprit, reviewed jeffro256:monero.social 's hot-cold FCMP++/Carrot PR + other upstream PR's for next release, prepping stressnet v2.1     

> __< jeffro256 >__ me: reviewing PRs and going through views of my upstream PRs     

> __< rucknium >__ 3. emsczkp research Bulletproofs* Milestone 2 completed (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626#note_36734).     

> __< jpk68:matrix.org >__ Hello     

> __< gingeropolous >__ Me: trying to see if monerosim is done     

> __< rucknium >__ Last time emsczkp:matrix.org  discussed his progress. jberman:monero.social  intended to look at the revised paper IIRC.     

> __< emsczkp:matrix.org >__ I have nothing to add beyond what said during the previous meeting. It was great to see positive comments on socials     

> __< jberman >__ I haven't had a chance to dive, but the revised paper (and proofs) looks solid     

> __< neptunian:unredacted.org >__ jberman: ++     

> __< jberman >__ I think once the work is complete, it'll make sense to get another maths review on it, similar to how we've done for FCMP++     

> __< jberman >__ But reiterating, looking like great progress, and exciting results! Well done emsczkp:matrix.org     

> __< emsczkp:matrix.org >__ thank you!     

> __< rucknium >__ Last meeting, emsczkp:matrix.org asked whether it is OK to payout Milestone 2 of his CCS at this point or if more review is necessary.     

> __< jberman >__ I'm a +1 on payout     

> __< emsczkp:matrix.org >__ rucknium: Exactly, thank you for the clarification     

> __< rucknium >__ emsczkp:matrix.org: When the paper is complete, do you intend to submit it to a peer-reviewed journal or conference?     

> __< emsczkp:matrix.org >__ rucknium: yes, that's the goal     

> __< rucknium >__ That wouldn't necessarily be as rigorous as MRL would like it, but it would be at least another set of critical eyes on it.     

> __< rucknium >__ I mean, if the results were to be used in actual production Monero code.     

> __< rucknium >__ I am +1 on payout too, but I have not tried to understand the paper. Any other opinions here?     

> __< emsczkp:matrix.org >__ Exactly, and I’ll work on a submission to the first major conference on the subject asap     

> __< rucknium >__ emsczkp:matrix.org: Thank you.     

> __< neptunian:unredacted.org >__ emsczkp:matrix.org: Hope to see you at EUROCRYPT :-)     

> __< emsczkp:matrix.org >__ Thank you, community, for the support on this reseach , which I strongly believe in and it is a very long story to me     

> __< rucknium >__ luigi1111 luigi1111_  : FWIW, we have support in this MRL meeting to payout emsczkp:matrix.org  Milestone 2 of https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/626     

> __< rucknium >__ More discussion on this item?     

> __< rucknium >__ Thanks, emsczkp:matrix.org     

> __< rucknium >__ 4. Post-quantum encryption (https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686). Jamtis (https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#appendix-c-instant-sync-protocol).     

> __< tevador >__ No updates from me today.     

> __< neptunian:unredacted.org >__ Have there been any changes in regards to CSIDH and the security level assumptions?     

> __< neptunian:unredacted.org >__ I haven't kept up with it, apologies.     

> __< jberman >__ Not to my knowledge     

> __< tevador >__ I haven't seen any papers regarding that     

> __< neptunian:unredacted.org >__ I have no further comments in that case. I don't feel the need to try to find other primitives to use here, as I like CSIDH currently.     

> __< rucknium >__ 5. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/).     

> __< rucknium >__ DataHoarder set up a view key scanner on stressnet: https://stressnet.p2pool.observer/payments     

> __< jeffro256 >__ Thanks to j-berman for reviewing the hot/cold PR. It is in a good spot, I don't know if it will make it into v2.1, but I feel like it should be ready v soon      

> __< jeffro256 >__ Lots of review/implementation going on there      

> __< jberman >__ Aiming to put v2.1 out today or tomorrow that fixes the window GUI binary, hopefully also fixes the observed sporadic double spends as well     

> __< rucknium >__ And I provided the view keys to my spamming wallets. I have a basic set of tables at the bottom of https://stressnetnode1.redteam.cash/ that help me see which of my spam wallets are actually getting txs into blocks.     

> __< jberman >__ (The latter appears to be an upstream issue)     

> __< jeffro256 >__ j-berman also debugged several issues with the daemon and RPC, reviewing those fixes      

> __< rucknium >__ jeffro256:monero.social: Is the hot/cold PR the same one that speeds up getblock.bin?     

> __< jeffro256 >__ Completely separate      

> __< jeffro256 >__ The hot/cold wallet PR is here: https://github.com/seraphis-migration/monero/pull/52     

> __< jeffro256 >__ The RPC speedup PR is here: https://github.com/monero-project/monero/pull/10605     

> __< rucknium >__ More discussion about stressnet?     

> __< jeffro256 >__ j-berman did some really interesting profiling of LMDB related to 10605. I think that I might try to really reduce the complexity of that PR     

> __< jeffro256 >__ Then, in a separate PR, implement the separate pruned/prunable mempool database tables approach. The only thing I'm worried about is if it'll make normal daemon block processing slower      

> __< jeffro256 >__ After PR 9135, bulk block processing will skip the mempool, so it wouldn't apply their, but it would to top block propogation times (maybe)     

> __< jberman >__ I suspect impact to normal sync will be close to negligible     

> __< jeffro256 >__ I hope so      

> __< rucknium >__ I am excited for the speedup :)     

> __< rucknium >__ Thanks for all the work on it, including reviewers     

> __< jeffro256 >__ If LMDB has a large readahead, I can see that once the blockchain code starts touching prunable blobs during top block propgation, then the reads will be in-memory, and then the only additional overhead would be the 2x key lookups      

> __< jeffro256 >__ So I can see it being negligible, but we'll see      

> __< jeffro256 >__ At a certain point, trying to theorize about performance, w/o a demo, and with so many moving parts is basically astrology      

> __< rucknium >__ Does stressnet provide enough of a demo envionment?     

> __< jeffro256 >__ Yeah I'd definitely say so      

> __< jberman >__ It took 0.1s in that demo to read 20k keys and also the pruned blobs     

> __< jeffro256 >__ I can't remember, was the      

> __< jeffro256 >__ keys read in series, or was it lookup from the root each time?     

> __< jeffro256 >__ in the demo     

> __< rucknium >__ Crazy idea: Could I just apply that PR to the stressnet node code and hope it speeds up my spamming?     

> __< jberman >__ It's read in order, though I also tested locally with random read order and it was roughly equivalent     

> __< jeffro256 >__ Rucknium Yeah go for it, I don't think it should have any conflicts with other open PRs beside 10761     

> __< rucknium >__ Awesome. Thank you.     

> __< rucknium >__ More discussion of this item?     

> __< rucknium >__ 6. monerosim (https://github.com/Fountain5405/monerosim).     

> __< rucknium >__ Is gingeropolous:monero.social  here?     

> __< gingeropolous >__ Hi! Yep, here     

> __< rucknium >__ I think you were doing a tedious grid search for network parameters that would get closest to mainnet behavior.     

> __< gingeropolous >__ Yes, your review encouraged me to investigate the delta and see if I could narrow it     

> __< rucknium >__ What are your findings so far?     

> __< gingeropolous >__ I think it has been narrowed. I'm remote so I can't really link things right now, but the detailed findings can be found on the repo     

> __< gingeropolous >__ But yeah, the general idea seemed to be the 100% reachable network has a different behavior than mainnet, and the always on network in the sim also modified things     

> __< gingeropolous >__ So, those parameters can be toggled and managed via the config files for sim generation     

> __< rucknium >__ Fantastic. How was the unreachable nodes implemented?     

> __< gingeropolous >__ Just adding the --hide-my-port.     

> __< rucknium >__ Do you think you would have different results if trying --in-peers=0?     

> __< gingeropolous >__ As I'm typing it, I realize I could also also do it from the host level, as in each shadow thing could function as a firewall for that virtual entity     

> __< rucknium >__ in-peers would probably be stricter. Or combining them     

> __< rucknium >__ gingeropolous: Is that easy to do? That would probably mimic the actual network setup most closely     

> __< gingeropolous >__ Dude, yeah, it's a sim. We could test parameters for as long as the machines spin , and I look forward to doing so!     

> __< gingeropolous >__ Yeah, I could add that in.     

> __< rucknium >__ Because most unreachable are unreachable because of their NAT or similar external setup, not because of their monerod flag config options     

> __< gingeropolous >__ Indeed. I guess we could also mimic the ... Effective of that UPNP punch through or whatever? Because monero still tries, right? And sometimes it works.... Or just flat default firewall... Though I guess that can just get swallowed up in the config setting of % reachable ".....     

> __< rucknium >__ I don't know too much about the UPNP punch through, but maybe someone who does know could comment.     

> __< rucknium >__ Any more discussion of this agenda item?     

> __< gingeropolous >__ So I'm still not at the milestone? What do we think, 98%, 70%..... 🤗     

> __< rucknium >__ I think you are     

> __< sneedlewoods_xmr:matrix.org >__ I don't think we use upnp anymore https://github.com/monero-project/monero/pull/10012     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< jeffro256 >__ Thanks everyone      

> __< gingeropolous >__ Thank you all!     

> __< DataHoarder >__ 19:32:54 <rucknium> DataHoarder set up a view key scanner on stressnet: https://stressnet.p2pool.observer/payments     

> __< DataHoarder >__ FYI I support carrot-native scanning as well, if any of those were running. JSON is available in https://stressnet.p2pool.observer/payments.json which provides some further details, including TxProofV2 (InProof)     

> __< rucknium >__ I forgot to say that DataHoarder  has it for mainnet, too. Has the General Fund, CCS, Magic, and Bounties view keys at least: https://blocks.p2pool.observer/payments     




# Action History
- Created by: Rucknium | 2026-07-01T14:55:06+00:00
- Closed at: 2026-07-09T19:23:57+00:00
