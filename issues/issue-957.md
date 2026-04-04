---
title: Monero Research Lab Meeting - Wed 17 January 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/957
author: Rucknium
assignees: []
labels: []
created_at: '2024-01-17T15:09:30+00:00'
updated_at: '2024-01-26T19:51:43+00:00'
type: issue
status: closed
closed_at: '2024-01-26T19:51:43+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: How to confirm security of Monero's multisignature protocol? Do we need mathematical security proofs, and can we get them? Info:
- [Brandon Goodell and Sarang Noether (2018) "Thring Signatures and their Applications to Spender-Ambiguous Digital Currencies"](https://www.getmonero.org/resources/research-lab/pubs/MRL-0009.pdf)
- [Monero multi-signature patch review by Inference](https://community.rino.io/rino-multisig-pr8194-audit-20220627.pdf)
- [Rust alternative implementation](https://github.com/serai-dex/serai/blob/develop/coins/monero/src/wallet/send/multisig.rs) by @kayabaNerve

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100). What are the bottlenecks for potential implementation?

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#954 

# Discussion History
## plowsof | 2024-01-25T11:43:57+00:00
Logs 
> __< r​ucknium:monero.social >__ MRL meeting here in two hours.     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/957     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< rbrunner >__ hello     

> __< dukenukem >__ Hola.     

> __< vtnerd >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< k​ayabanerve:matrix.org >__ I implemented GBPs into the FCMP repository. Variety of comments available from that.     

> __< r​ucknium:monero.social >__ me: OSPEAD. Related, I am pretty sure that the late December 2023 increase in tx volume ( https://bitinfocharts.com/comparison/monero-transactions.html#3m ) was someone spending many outputs as quickly as possible. The ring member age distribution shifted to be much younger than usual. In other words, probably spam like July-Aug 2021.     

> __< r​ucknium:monero.social >__ kayabanerve: You can save more time by explaining acronyms on first mention.     

> __< vtnerd >__ me: working on block difficulty computation in the "chain hardening" mode in lws. Still not sure the mode is worth it because I don't plan on having 2+ daemons for point of reference like p2p has     

> __< k​ayabanerve:matrix.org >__ The primary note is my impl is still ongoing. The circuit needs rearchitecture. The low level optimizations no longer still apply.     

> __< k​ayabanerve:matrix.org >__ The next comment is it may yield 2-6x performance increases *more than expected*. I was hoping for 35ms a proof. It may be a small fraction of that.     

> __< vtnerd >__ but basically Im trying to make sure the chain is valid with a certain level of difficulty, to make false chains from the daemon harder     

> __< k​ayabanerve:matrix.org >__ GBPs = Generalized Bulletproofs     

> __< k​ayabanerve:matrix.org >__ FCMPs = Full Chain Membership Proofs     

> __< r​ucknium:monero.social >__ kayabanerve: Did you see this paper? https://eprint.iacr.org/2024/047 "On Efficient and Secure Compression Modes for Arithmetization-Oriented Hashing". Anything applicable?     

> __< r​ucknium:monero.social >__ vtnerd: Similar to bitcoin SPV wallet?     

> __< k​ayabanerve:matrix.org >__ Their abstract is wrong :C     

> __< r​ucknium:monero.social >__ Not a good start     

> __< k​ayabanerve:matrix.org >__ Just the claim Monero uses this.     

> __< r​ucknium:monero.social >__ What makes GBP "generalized"? Why is ordinary BP a special case?     

> __< vtnerd >__ yes, its likely similar. monero-lws is designed to run 24/7, so its got a better chance at detecting timestamp frauds     

> __< k​ayabanerve:matrix.org >__ So we perform a Pedersen hash for free.     

> __< k​ayabanerve:matrix.org >__ Technically, there's the overhead of the second proof needed for its output, and the blinding we need go transfer said values.     

> __< k​ayabanerve:matrix.org >__ The unblinding is done in-circuit and is... 1.25 gates * 161 trits? 250 gates (which are R1CS constraints). I hope to get that to 1.     

> __< k​ayabanerve:matrix.org >__ *200 gates.     

> __< r​ucknium:monero.social >__ 3) Discussion. What do we want to discuss?     

> __< k​ayabanerve:matrix.org >__ They're 258 constraints for their smallest space Rucknium. It's competitive, yet don't believe it'd be faster, even though it'd remove the overhead of the other proof.     

> __< k​ayabanerve:matrix.org >__ (sorry if I went too far into the math there)     

> __< r​ucknium:monero.social >__ ^ That's referring to the paper I posted?     

> __< k​ayabanerve:matrix.org >__ *They're 231     

> __< rbrunner >__ You wrote of a probable spam attack late December. How long did that last?     

> __< rbrunner >__ (Maybe not an attack, but spam.)     

> __< k​ayabanerve:matrix.org >__ Yeah. It uses ~15% more constraints. It would let us avoid a second proof, if we trust their hash function. That may be a fair trade off EXCEPT I'm planning to further reduce our constraints *and* we don't have our hash function take more time as the base does (they do. More elements hashed, more steps taken).     

> __< r​ucknium:monero.social >__ rbrunner: About two weeks. Shorter than the July-Aug 2021, which was 6 weeks I think. https://bitinfocharts.com/comparison/monero-transactions.html#3m     

> __< rbrunner >__ I see. And I was hoping people start to buy each other Christmas gifts with Monero en masse ...     

> __< k​ayabanerve:matrix.org >__ So there's a bit of technical commentary which would need a full PoC to properly compare (2w-1m of work?). I don't think it'll end up more competitive *and* it has a fundamentally distinct security analysis.     

> __< r​ucknium:monero.social >__ Here was our analysis of the 2021 incident: https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60     

> __< rbrunner >__ I wonder what a spam wave of only 2 weeks should be "good" for     

> __< r​ucknium:monero.social >__ The tx volume chart has a similar shape, too. Spike to double the tx volume, then gradually decrease back to the usual tx volume.     

> __< k​ayabanerve:matrix.org >__ Distinctly, I'd like to raise an idea to note, though I apologize for how I've already spoken quite a bit as I vocalized my analysis of that paper.     

> __< k​ayabanerve:matrix.org >__ Class groups. They're an extremely weird niche of cryptography I used for a side project. I'm also half convinced they're the solution to everything.     

> __< k​ayabanerve:matrix.org >__ We can trustlessly define a class group such that we can operate on arbitrary ECC elements, scalars or field elements, within an EC-like abstraction.     

> __< k​ayabanerve:matrix.org >__ https://eprint.iacr.org/2022/419 is a constant sized, logarithmic verification time, ZK SNARK premised on them.     

> __< dukenukem >__ rbrunner: as Rucknium said, the ring member age distribution shifted to be much younger than usual. Deanonymization in a targeted set of txs., or specific tx., maybe?     

> __< k​ayabanerve:matrix.org >__ I'll make a research issue for it. No discussion is justified at this time. I just want to have people be aware of the term "class groups".     

> __< r​ucknium:monero.social >__ Yes, the spam incident can be a black marble attempt, but just double the tx volume isn't going to help an adversary much.     

> __< rbrunner >__ "solution to everything" meaning finding use in FCMPs as well?     

> __< r​ucknium:monero.social >__ On a different topic: koe did Seraphis performance tests for tx verification ( https://github.com/monero-project/research-lab/issues/91#issuecomment-1047191259 ). But would things be different if storage I/O was part of the verification time? I assume that raising ring size to 128 from 16 would increase the storage I/O requirements because monerod would have to pull all those outp<clipped message     

> __< r​ucknium:monero.social >__ ut public keys from the LMDB for each ring sig verification.     

> __< r​ucknium:monero.social >__ RavFX 🤐 (RavFX) has brought this up.     

> __< r​ucknium:monero.social >__ And how does Curve Trees compare in I/O requirements?     

> __< k​ayabanerve:matrix.org >__ rbrunner: the fact there's a trustless, constant sized, logarithmic verification time SNARK means all proofs we want can be done. At worst, they'd just be horrible garbage with a million statements due to operating over non-native arithmetic.     

> __< k​ayabanerve:matrix.org >__ Class groups do enable people to find subgroups of order of any prime. This was applied in CL15 for an encryption scheme as *the discrete log problem is easy* for their subgroups. I'm double checking now if native arithmetic was enabled within Dew, or if that's future research.     

> __< k​ayabanerve:matrix.org >__ Even if Dew offers it, it won't beat a proper ECC construction, nor do I believe it'd beat a properly applied IVC construction. Class groups are ~2000 bits. Orders of magnitude slower, yet also with currently unique features.     

> __< k​ayabanerve:matrix.org >__ If ECC is a round hole, and we ever have a square peg, we can hammer it in with class groups. That's the main comment at this time.     

> __< r​ucknium:monero.social >__ Do you just have to get the Merkle root from the database?     

> __< k​ayabanerve:matrix.org >__ They have O(1) storage complexity to verify proofs.     

> __< k​ayabanerve:matrix.org >__ They just need the tree root. There's no random reads from disk.     

> __< k​ayabanerve:matrix.org >__ We'd define said root as the root for 10 blocks ago, and once a block is 10 deep, update the tree with that block's new enotes. That does require ECC operations, and my PoC delayed said operations until all enotes were added to demonstrate a batch update.     

> __< r​ucknium:monero.social >__ Maybe the Seraphis I/O performance can be tested once devs in #no-wallet-left-behind:monero.social  have a Seraphis database.     

> __< r​ucknium:monero.social >__ I mean Seraphis with 128+ rings     

> __< k​ayabanerve:matrix.org >__ I also guess the tree edges, which are the elements updated, will be concise enough to fit into memory.     

> __< rbrunner >__ Yeah, I don't see anybody building something like a simulation just for such a speed test. Testing can probably indeed start if we have a Seraphis testnet running.     

> __< r​ucknium:monero.social >__ Anything more to discuss?     

> __< r​ucknium:monero.social >__ We can end the meeting here.     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2024-01-17T15:09:30+00:00
- Closed at: 2024-01-26T19:51:43+00:00
