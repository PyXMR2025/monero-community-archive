---
title: Monero Research Lab Meeting - Wed 18 May 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/706
author: Rucknium
assignees: []
labels: []
created_at: '2022-05-17T22:52:50+00:00'
updated_at: '2022-05-24T18:06:06+00:00'
type: issue
status: closed
closed_at: '2022-05-24T18:06:06+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

5. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

7. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

8. Any other business

9. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#702  

# Discussion History
## UkoeHB | 2022-05-18T18:49:44+00:00
```
[05-18-2022 17:00:38] <UkoeHB> meeting time: https://github.com/monero-project/meta/issues/706
[05-18-2022 17:00:38] <UkoeHB> 1. greetings
[05-18-2022 17:00:38] <UkoeHB> hello
[05-18-2022 17:01:02] <Rucknium[m]> Hi
[05-18-2022 17:01:04] <rbrunner> Hello
[05-18-2022 17:01:45] <jberman[m]> hello
[05-18-2022 17:01:59] <hyc> hi
[05-18-2022 17:02:08] <mj-xmr[m]> Hi :)
[05-18-2022 17:02:55] <dangerousfreedom> Hello
[05-18-2022 17:03:54] <UkoeHB> 2. updates; what has everyone been working on/planning to work on?
[05-18-2022 17:05:18] <mj-xmr[m]> I delivered the first working Python implementation of the Gamma Picker algo (part of the Decoy Algorithm) and was able to simulate the same behavior, that I did for the original C++ implementation. There are some visible differences, at least due to differences of the random number generator (Python's `... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/a7331e67b6adb21a1a6986e7ede4c8af57381fe0)
[05-18-2022 17:06:08] <mj-xmr[m]> C++ version for reference:
[05-18-2022 17:06:09] <mj-xmr[m]> https://user-images.githubusercontent.com/63722585/169068204-8e82eb8f-4151-48a9-85d4-c554cc231839.png
[05-18-2022 17:06:26] <hyc> for comparison purposes you should be able to write your own PRNG and use it in both impls
[05-18-2022 17:06:40] <mj-xmr[m]> Yep. Point.
[05-18-2022 17:06:53] <UkoeHB> me: Implemented a robust input selection solver for seraphis, pushed multisig PRs forward a bit, and updated jamtis to support self-spends better (e.g. churn). Next I will finally implement the full enote scanning workflow that I have been really looking forward to.
[05-18-2022 17:08:01] <Rucknium[m]> Working on the statistical model to estimate the effect of minexmr dot com's fee increase. I think I'll go with Vector Autoregression, treating the fee increase as an exogenous shock and fiat/XMR exchange rate and hashing difficulty as endogenous. Any input appreciated, especially from mj-xmr .
[05-18-2022 17:08:51] <dangerousfreedom> Im learning and implement in Python Bulletproofs and CLSAG as it is in the C++ code. I am also continuing scanning the blockchain with the LibSodium library.
[05-18-2022 17:08:51] <mj-xmr[m]> I'll chat you after I finalize the decoy (very soon)
[05-18-2022 17:10:29] <jberman[m]> finished up patching relatively trivial tor/i2p daemon connectivity bugs (my outgoing tor connections stay alive much longer now and I don't see tx submissions warnings nearly as often), I left the final one on the back-burner for now (see comment in 6938 for what that remaining one is), reviewed/provided guide to rbrunner on completing 8076, and for now moving back over to reviewing 7760
[05-18-2022 17:11:27] <rbrunner> Thanks for that, will start to work on 8076 this evening, let's see I will be able to get in before the branch or not
[05-18-2022 17:13:09] <UkoeHB> thanks for the updates
[05-18-2022 17:13:19] <UkoeHB> 3. discussion, anything to discuss?
[05-18-2022 17:14:48] <jberman[m]> aside from compilation errors/that reorg issue moneromoo submitted a patch for, anyone pick up on issues during testnet fork?
[05-18-2022 17:14:50] <Rucknium[m]> Do we want to discuss reducing the 10 block lock (MRL issue #102)?
[05-18-2022 17:15:22] <UkoeHB> Rucknium[m]: sure
[05-18-2022 17:16:20] <UkoeHB> my perspective is it will be difficult to evaluate whether changing the block limit is a good idea
[05-18-2022 17:16:46] * moneromooo agrees with that
[05-18-2022 17:17:21] <moneromooo> FWIW, smooth had a strong opinion against lowering it, and is a clever one (and yes, it's argument from authority)
[05-18-2022 17:17:58] <moneromooo> With higher network hash rate though, that argument feels maybe lessened a smidgen.
[05-18-2022 17:18:35] <hyc> why does magnitude of hashrate change things?
[05-18-2022 17:18:46] <moneromooo> Law of large numbers.
[05-18-2022 17:19:12] <moneromooo> The more hash rate, the less likely someone to have a huge part of it, and so the less likely to have large reorgs. I think.
[05-18-2022 17:19:31] <moneromooo> I guess with pools, that doesn't apply as much as it should though.
[05-18-2022 17:19:58] <jeffro256[m]> Yeah especially pools like minexmr
[05-18-2022 17:20:08] <hyc> yeah prob not a good argument with current pool situation
[05-18-2022 17:20:23] <UkoeHB> If there is a network problem/attack, the current stable situation could be disrupted quite a bit.
[05-18-2022 17:20:45] <moneromooo> Also, referencing outputs by pubkey helps the issue with invalidating lots of txes.
[05-18-2022 17:21:27] <hyc> we've discussed that before. did we decide to do that?
[05-18-2022 17:21:32] <Rucknium[m]> Just thinking out loud here and revisiting the active attacker scenario in UkoeHB 's MRL issue #95: If someone is spamming lots of transactions, don't they already have a good idea of which recently-referenced ring members are decoys since transactions that reference recent outputs would be referencing the attacker's own outputs?
[05-18-2022 17:21:34] <moneromooo> I don't think so.
[05-18-2022 17:21:51] <UkoeHB> doesn't help tx size though, and wouldn't be forward compatible with any deterministic reference solution
[05-18-2022 17:21:54] <rbrunner> How will Seraphis referencing outputs?
[05-18-2022 17:22:27] <UkoeHB> Rucknium[m]: yes that's the decoy set poisoning attack
[05-18-2022 17:23:04] <moneromooo> For tx size, we can have hybrid pubkey/index. New outputs by pubkey (non deterministic), older outs by index (deterministic).
[05-18-2022 17:23:06] <hyc> tx size presumably is only an issue for network bandwidth, as we would still store only output index on-disk
[05-18-2022 17:23:15] <UkoeHB> rbrunner: right now I have deterministic bins. Manually define a set of locations (indices) in the enote set, then deterministically select ring members from around those locations.
[05-18-2022 17:23:22] <jeffro256[m]> UkoeHB Maybe we could create pubkey-IDs which are hashed and/or truncated pubkeys to a certain length and which must also unique as well as the pubkeys themselves 
[05-18-2022 17:23:25] <moneromooo> Assuming lots more older ones (ie, > 10 blocks or whatever), tx size doesn't increase much.
[05-18-2022 17:24:19] <jberman[m]> Rucknium: yes, but if the attacker gets an honest user's tx that had made into the chain to invalidate, the honest user has a previously successful tx now fail, and then must re-construct that tx with even *more* decoys that everyone knows are decoys
[05-18-2022 17:24:46] <jeffro256[m]> UkoeHB You would get the benefit of reorg protection and hopefully they wouldn't take up too much more space than the (64-bit I think it is) current way of indexing outputs
[05-18-2022 17:24:57] <moneromooo> Though the "how to have deterministic while plugging N non deterministic outs" problem is not obvious, but doesn't seem insurmountable...
[05-18-2022 17:25:11] <UkoeHB> moneromooo: for me, deterministic means generating multiple locations from a single seed; it's hard to map a set of indeterminite locations into a deterministic representation
[05-18-2022 17:26:08] <moneromooo> Well, if your deterministic algorithm picks a locatoin that's too recent, then pubkeys are listed there (as many as needed to fill the bin).
[05-18-2022 17:26:19] <merope> If only the bins are deterministic but not the actual outputs selected, then where's the advantage? Any wallet who doesn't conform to that will stick out
[05-18-2022 17:27:27] <jeffro256[m]> endor00 If they didn't conform I feel like it would be hard to create a valid ring sig 
[05-18-2022 17:27:29] <merope> And if your implement the wallet such that it remembers which out it picked from that bin in case of a reorg/resubmit, then you might as well have deterministic inputs
[05-18-2022 17:27:37] <UkoeHB> jeffro256[m]: the reason I don't think supporting unique onetime addresses can work is it creates problems for 'tx engineering' things like atomic swaps. If you can block a tx-being-constructed from the chain by publishing one of its enotes, that would break any protocol that relies on the tx-being-constructed from being publishable.
[05-18-2022 17:30:09] <UkoeHB> merope: the outputs selected are deterministic, the bin locations are not
[05-18-2022 17:30:47] <jeffro256[m]> @Ukoe How would you be able to block? Just from virtue of smaller brute force space ?
[05-18-2022 17:30:49] <merope> Oooh ok, so random bin location but deterministic output within that bin
[05-18-2022 17:30:55] <jeffro256[m]> That seems like it could be tuned
[05-18-2022 17:31:41] <UkoeHB> jeffro256[m]: "and which must also unique as well as the pubkeys themselves " If you can't submit a tx because it contains some duplicate thing with another tx in the chain (other than key images).
[05-18-2022 17:33:35] <UkoeHB> All these annoying complexities are why I recommended 'floating outputs' last year (which wasn't received well...).
[05-18-2022 17:35:12] <UkoeHB> moneromooo: it's hard for me to imagine how it would work, although I'm open to suggestions
[05-18-2022 17:35:54] <jeffro256[m]> UkoeHB Except you can choose your own pubkey  which means you could control your own "pubkeyID" cause it would be determinsitically generated from the pubkey. It would add some overhead for sure (checking uniqueness), but a hash is involved, it could be hard for a bad actor to reverse engineer a value to conflict 
[05-18-2022 17:37:40] <UkoeHB> jeffro256[m]: anyone who is party to an off-chain tx engineering protocol (like atomic swaps) can see all the in-progress txs, so all they need to do is copy-paste the onetime address into a dummy output in another tx (with 0 amount); any duplicate check on onetime addresses will block the engineered tx from submission
[05-18-2022 17:37:54] <jeffro256[m]> I prefer binning though
[05-18-2022 17:38:24] <UkoeHB> prefer over what?
[05-18-2022 17:40:35] <moneromooo> UkoeHB: I was thinking somethig like: for (i in 0..N-1) { O=deterministic_pick(); if (age(O) > 10 && tx.outputs[i] != O) return false; return true; }
[05-18-2022 17:41:00] <moneromooo> Then the sender writes a pubkey, not an int, in any tx.outputs[i] which is young enough.
[05-18-2022 17:41:06] <moneromooo> A bit handwavy for sure.
[05-18-2022 17:41:43] <moneromooo> Basically when your deterministic_pick funciton returns something young enough, you allow anything.
[05-18-2022 17:41:57] <jberman[m]> referencing by pub key still doesn't fully negate the issue if decoys that are referenced are non-honest users' decoys which get reorged away (presumably whoever is triggering a deep reorg is also spamming to inflict max damage for this too). I think the root issue is still there
[05-18-2022 17:42:37] <UkoeHB> jberman[m]: +1
[05-18-2022 17:42:47] <jeffro256[m]> UkoeHB Oh yeah you're right, but what's stopping that from happening currently ? Pubkeys can only be sent to once, correct? Or is it just spent once ?
[05-18-2022 17:43:30] <moneromooo> Pubkeys are not forced unique.
[05-18-2022 17:43:50] <UkoeHB> moneromooo: I think that's floating outputs (what we have now). So you'd have a bunch of ring members deterministic, then optionally any number of additional members as 'floating' (not deterministic) pubkey references.
[05-18-2022 17:43:55] <moneromooo> They arguable should be. It was deemed not worth the bother (Extra db, extra lookup).
[05-18-2022 17:44:17] <UkoeHB> jeffro256[m]: right now the wallet will only try to spend the highest amount among outputs with the same onetime address
[05-18-2022 17:44:46] <UkoeHB> I originally wanted to enforce unique onetime addresses in my seraphis poc, until I realized the issue with off-chain tx engineering stuff.
[05-18-2022 17:45:31] <moneromooo> Does "I think that's floating outputs" imply a flaw with those ? I do not have the background knowledge to map it to the implied thing you refer to.
[05-18-2022 17:45:35] <kayabaNerve> UkoeHB: That's devious. I legitimately never considered that as an angle. ... new proposal for the RPC to allow checking if a one time key exists on chain so wallets can easily check that way?
[05-18-2022 17:46:00] <UkoeHB> moneromooo: not really, it's just an easier way to think about it imo
[05-18-2022 17:46:00] <jeffro256[m]> moneromooo Interesting. I had the misconception from somewhere a long time ago that pubkeys were completely unique but now it makes sense why they would not be. I guess you could "sort-of" patch that problem with relay rules, but its not a very strong guarantee 
[05-18-2022 17:46:21] <kayabaNerve> We have /is_key_image_spent but AFAIK, not /is_key_onchain to check against burning attacks
[05-18-2022 17:47:34] <UkoeHB> kayabaNerve: it's not like a wallet will make a duplicate onetime address on purpose (so idk what an RPC endpoint will gain you); you need a custom wallet
[05-18-2022 17:48:37] <kayabaNerve> My frustration is the only way a wallet can securely receive funds is if it knows the entire wallet history for all of time. An RPC route, against a trusted daemon, would allow it to only sync the relevant tail blocks of its existence and then simply check for each input it receives if it's malicious.
[05-18-2022 17:48:54] <kayabaNerve> It's not about sending such outputs. It's about extra certainty when receiving funds.
[05-18-2022 17:50:31] <UkoeHB> ah I suppose that would be useful (although then you also need to get all enotes with the same onetime address and figure out which one has the highest amount)
[05-18-2022 17:50:33] <kayabaNerve> As a side note, while I know we have trolls, I really hope our community doesn't devolve into commentary on paid trolls existing unless we have literal evidence of that. It tears the community apart while making us look insane. Another coin's community recently went down that path and it's... hell.
[05-18-2022 17:51:16] <kayabaNerve> UkoeHB: To optimize, sure, yet I personally care more about dropping the latter inputs as invalid and moving on.
[05-18-2022 17:51:42] <kayabaNerve> It's a simpler flow and the malicious sender burns funds you consider not received. Same as if they never sent.
[05-18-2022 17:51:53] <UkoeHB> that would open another vector for breaking tx engineering protocols
[05-18-2022 17:52:03] <kayabaNerve> How so?
[05-18-2022 17:52:25] <kayabaNerve> Send 0.0001 XMR, then send 1 XMR, yet it only considers 0.0001?
[05-18-2022 17:52:30] <UkoeHB> yes
[05-18-2022 17:52:44] <kayabaNerve> The malicious sender is definitively malicious though. It's perfectly fine to say they only sent 0.0001 and walk away accordingly.
[05-18-2022 17:53:14] <kayabaNerve> With the atomic swap proposal, it'd be a wrong amount lock. Sure, they had an offer for a valid amount lock... but who cares? They're actively malicious. Walk away.
[05-18-2022 17:53:18] <UkoeHB> no, the problem is assumptions that are made off-chain before anything is even submitted to the ledger
[05-18-2022 17:53:30] <kayabaNerve> ... oh
[05-18-2022 17:53:37] <kayabaNerve> Right, this is still a DoS
[05-18-2022 17:53:43] <kayabaNerve> ... got it
[05-18-2022 17:53:45] <kayabaNerve> yep
[05-18-2022 17:54:09] <kayabaNerve> And that's why we have is_key_image_spent because it's actually cryptographically secure
[05-18-2022 17:54:30] <UkoeHB> 👍
[05-18-2022 17:54:52] <UkoeHB> we are approaching the hour, anyone have other comments/questions to address? we didn't get too far on our 10-block-lock discussion lol
[05-18-2022 17:56:11] <jeffro256[m]> Still a hard problem, but I think we could sort of fix that with a robust zero-conf wallet 
[05-18-2022 17:56:39] <UkoeHB> how so?
[05-18-2022 17:56:51] <UkoeHB> the main issue is funds in the lock can't be spent at all
[05-18-2022 17:57:10] <UkoeHB> you could make a tx spending those funds and queue it up I guess
[05-18-2022 17:57:38] <jeffro256[m]> Yeah I think there's a wallet (cant remeber the name) that is working specifically on that problem
[05-18-2022 17:58:43] <jeffro256[m]> Or maybe it was just an idea thrown out there. If your wallet can guess (or you tell it) roughly how much money you're gonna spend and when, it can break it up into appropriate amounts 
[05-18-2022 17:59:18] <UkoeHB> ah yeah I heard about that project, not sure the status
[05-18-2022 17:59:30] <jeffro256[m]> And on the other side, accepting zero-conf txs as a small merchant in Monero is still pretty dang safe 
[05-18-2022 17:59:40] <moneromooo> Actually, there is a roundabout way :D Technically, Townforge is a fork of monero, and you can freely move money between output based and balance based, and when transacting between balance based, you have no lock period :D
[05-18-2022 17:59:53] <Rucknium[m]> I think that's Monerujo with "pocket change". It doesn't help the issues that Haveno and similar services will encounter, however.
[05-18-2022 17:59:55] <moneromooo> OK, it's cheeky because no ring sigs.
[05-18-2022 18:00:50] <moneromooo> (in the balance based section, there are ring sings in hte out based section of course)
[05-18-2022 18:01:28] <kayabaNerve> moneromooo: If it still has amount privacy, and you only ever fund new balance accounts (so you have a dedicated account to receive, and then you can create new accounts with deposits to send)... that's actually pretty qual
[05-18-2022 18:01:38] <UkoeHB> alrighty, that's the end of the hour; thanks for attending everyone
```

# Action History
- Created by: Rucknium | 2022-05-17T22:52:50+00:00
- Closed at: 2022-05-24T18:06:06+00:00
