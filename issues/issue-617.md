---
title: Monero Dev Meeting - Sun 17 October 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/617
author: carrington1859
assignees: []
labels: []
created_at: '2021-10-03T19:59:05+00:00'
updated_at: '2021-10-27T18:37:35+00:00'
type: issue
status: closed
closed_at: '2021-10-27T18:37:35+00:00'
---

# Original Description
Location: [Libera.chat, #monero-dev](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-dev:monero.social?via=matrix.org&via=monero.social)

Time:
17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211017T170000&p1=1440)

Main discussion topics:

1. Greetings


2. Fee changes ( [PR](https://github.com/monero-project/monero/pull/7819) , [Discussion](https://github.com/monero-project/research-lab/issues/70), [Older Discussion](https://github.com/monero-project/monero/issues/5711) )
3. Decoy selection algorithm changes  ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480) )
a. Jberman's binning outline
b. Change to "recent spend window" from 10-60 to 10-20
4. [Ringsize increase](https://github.com/monero-project/research-lab/issues/79)
5. [UkoeHB's multisig refactor](https://github.com/monero-project/monero/pull/7877)
6. Removing unlock time ( [Removing/Fixing/Encrypting monero's timelocks](https://github.com/monero-project/research-lab/issues/78) ) (it also affects [binning](https://github.com/monero-project/research-lab/issues/84))
a. [Community feedback](https://www.reddit.com/r/Monero/comments/q0oiln/proposal_to_remove_timelock_feature/)
7. BP+ ( [1st Audit](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/197) , [2nd Audit](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/215) both have useful links)
a. Source code conflicts need to be resolved.
b. BP+ storage for a txid - type/size string (32 byte without leakage)
8. Proposal to deprecate integrated addresses (Discussions on [github](https://github.com/monero-project/monero/issues/7889) & [reddit](https://www.reddit.com/r/Monero/comments/pbixk6/request_for_community_input_proposal_to_deprecate/)).
9. Setting date for network upgrade.
10. Any other business
11. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: ?

Links to previous meeting including logs: 
https://github.com/monero-project/meta/issues/614

# Discussion History
## UkoeHB | 2021-10-17T18:29:21+00:00
```
[10-17-2021 17:02:04] <Rucknium[m]> Unless I am mistaken, a dev meeting is supposed to start now:
[10-17-2021 17:02:04] <Rucknium[m]> https://github.com/monero-project/meta/issues/617
[10-17-2021 17:03:45] <rbrunner> Yes, 17:00 UTC
[10-17-2021 17:04:59] <rbrunner> Just the two of us? Hard to believe :)
[10-17-2021 17:05:51] <sech1> I'm here and watching :)
[10-17-2021 17:06:15] <rbrunner> Zcash is much better than Monero!!! (That will get them out of hiding)
[10-17-2021 17:06:46] <UkoeHB> hi
[10-17-2021 17:07:01] <vtnerd_> Hi
[10-17-2021 17:07:41] <jberman[m]> hello :)
[10-17-2021 17:07:42] <UkoeHB> um since no one else bothers to do this, I guess I can jump in as chairman...?
[10-17-2021 17:08:04] <rbrunner> Splendid!
[10-17-2021 17:09:25] <UkoeHB> 2. Updates: any devs want to let us know what they are developing?
[10-17-2021 17:10:06] <UkoeHB> I continue to work on Seraphis PoC on my end. I am in the boring part where I code all the things I already figured out...
[10-17-2021 17:11:58] <jberman[m]> Wrote a PoC for a wallet-side binning algorithm here: https://github.com/monero-project/research-lab/issues/88
[10-17-2021 17:12:36] <UkoeHB> Thanks, I still haven't looked at this yet
[10-17-2021 17:13:37] <UkoeHB> Maybe no other dev work is being done? Do we even need a meeting? lol
[10-17-2021 17:13:57] <vtnerd_> I am going to push out my proposal for p2p encryption, and I am nearing completion on integrating the monero-lws serialization scheme into epee (as per selsta suggestion)
[10-17-2021 17:14:45] <UkoeHB> Cool thanks vtnerd_ 
[10-17-2021 17:15:07] <UkoeHB> Is that for p2p encryption between nodes, client to node?
[10-17-2021 17:15:14] <Rucknium[m]> I continue to work on OSPEAD. I wrote out a fairly precise mathematical description of a key part of it recently. I'm not sure that it quite qualifies as "dev" work, however, so I'm not sure whether it should be mentioned here.
[10-17-2021 17:15:33] <Rucknium[m]> There is also a defined agenda on the GitHub issue for the meeting.
[10-17-2021 17:15:41] <vtnerd_> yes, its to protect the p2p traffic (as opposed to the rpc traffic which is encrypted)
[10-17-2021 17:16:05] <fluffypony> vtnerd_: is the encryption opportunistic?
[10-17-2021 17:16:07] <vtnerd_> the p2p is tricky because authentication isn't realistic, and some community members asked about the Noise protocol (instead of TLS)
[10-17-2021 17:16:13] <vtnerd_> yes
[10-17-2021 17:16:22] <vtnerd_> there'll be options to specify authenticatio though
[10-17-2021 17:16:29] <fluffypony> ok cool 
[10-17-2021 17:16:35] <fluffypony> maybe in a few years we can make it mandatory
[10-17-2021 17:16:47] <vtnerd_> so node operators can specifcy a priority node, with auth
[10-17-2021 17:17:27] <fluffypony> maybe a simple auth could just be specifying a pubkey for that node
[10-17-2021 17:17:34] <vtnerd_> part of the spec was on making sure that it was "hidden" from the perspective of the ISP (even though the ISP could probably guess due to frequency of traffic)
[10-17-2021 17:17:38] <vtnerd_> yup
[10-17-2021 17:17:45] <fluffypony> sorta like .ssh/known_hosts
[10-17-2021 17:19:04] <vtnerd_> yeah close, but after some thought its mainly goign to be opportunistic because of the dynamic IP issue - auth is just tough in this p2p environment
[10-17-2021 17:19:26] <vtnerd_> and I think there'll be some encouragement to get the bootstrap nodes authed
[10-17-2021 17:20:31] <UkoeHB> Is selsta around to give us an update/overview of the dev cycle for next hardfork? Or anyone else who knows about it?
[10-17-2021 17:21:06] <UkoeHB> There are several pieces (in the agenda) waiting on review: fee PR, multisig PR
[10-17-2021 17:21:22] <UkoeHB> Ringsize increase
[10-17-2021 17:21:33] <vtnerd_> yeah, I need to the fee PR review, as promised
[10-17-2021 17:21:46] <vtnerd_> I should likely look at the multisig one too
[10-17-2021 17:22:30] <UkoeHB> I think h4sh3d mentioned he would look at multisig as well (maybe kayabaNerve too?)
[10-17-2021 17:23:49] <UkoeHB> We can try to reach a 'decision' about the ring size at next MRL meeting. Maybe a poll... lmao
[10-17-2021 17:23:51] <kayabaNerve> UkoeHB: Thanks for the info. I debated saying this back then, yet I was already a few hours past and didn't want to bother chat.
[10-17-2021 17:24:36] <kayabaNerve> I was solely interested in m-of-n multisigs and have an interest in ensuring they're preserved into the new protocol. I am absolutely not looking into developing them under the new system nor verifying the accuracy of the described potential system beyond pass/fail.
[10-17-2021 17:24:47] <h4sh3d> I mentioned that I’ll do a review, but also mentioned that I don’t what it to stop others to do it…
[10-17-2021 17:24:59] <kayabaNerve> While I may at some point want to be the cryptographer, I don't believe I have the skills.
[10-17-2021 17:25:06] <UkoeHB> Yeah I just meant from the review pov
[10-17-2021 17:25:48] <h4sh3d> *want it to stop others
[10-17-2021 17:26:03] <kayabaNerve> Got it. I solely want to verify inclusion m-of-n, and then I may write up a PoC depending on complexity. I'd love to do more, yet I'm no where near required cryptographic knowledge :p Just wanted to be absolutely clear
[10-17-2021 17:26:17] <UkoeHB> The more eyes, the better :). This is the first big piece of code with any real-world significance I have ever written.
[10-17-2021 17:28:13] <UkoeHB> Otherwise, it seems BP+ is ready to go for hardfork. The agenda mentions BP+ storage - has there been any interest in merging that feature?
[10-17-2021 17:29:35] <UkoeHB> Maybe can evaluate a potential PR once BP+ is merged. I am slightly concerned it would entail a large amount of code for fairly small gain. Not a huge concern.
[10-17-2021 17:32:08] <UkoeHB> Anyone have anything else to say? Otherwise we can call it quits. Attendance seems lacking...
[10-17-2021 17:33:26] <sech1> "9. Setting date for network upgrade." are we going to discuss this?
[10-17-2021 17:33:35] <sech1> or at least the next point release date?
[10-17-2021 17:33:39] <Rucknium[m]> Are we closer to the hardfork than we were two weeks ago? It seems yes, incrementally.
[10-17-2021 17:34:05] <UkoeHB> sech1: is there anyone involved in release planning actually here?
[10-17-2021 17:34:27] <rbrunner> I think that's pretty much selsta's show ...
[10-17-2021 17:34:52] <rbrunner> At least they are the one keeping the overview :)
[10-17-2021 17:36:12] <rbrunner> I also wonder whether we will get a new release branch, off master
[10-17-2021 17:36:46] <sech1> that's the necessary first step before hardfork :)
[10-17-2021 17:38:27] <rbrunner> If nothing else, I have a little varia, but maybe nobody here now knows that: What happened to this? Did is sizzle out, so to say?
[10-17-2021 17:38:28] <rbrunner> https://ccs.getmonero.org/proposals/anon-perfect-peer-to-peer-protocol.html
[10-17-2021 17:38:39] <UkoeHB> I wonder if I should try to make another multiisig PR to fix the Wagner attack with the FROST technique, before release. It was easy to fix in my seraphis multisig implementation (<200 lines?). But, there is more delay to review and so on.
[10-17-2021 17:39:20] <dEBRUYNE> rbrunner: The author is still regularly submitting patches to the Monero Github
[10-17-2021 17:39:39] <dEBRUYNE> e.g. -> https://github.com/monero-project/monero/pull/7999
[10-17-2021 17:39:41] <rbrunner> Ah, ok, so many small ones, not a big bang?
[10-17-2021 17:41:10] <wfaressuissia> "I wonder if I should try to make another multiisig PR to fix ..." do it too, otherwise what's the point of partialy fixed multisig ?
[10-17-2021 17:41:11] <coinstudent2048[> kayabaNerve: I can guide a bit for the math of multisig as described in ZtM2, but I do not know C++ and the structure of Monero code. I cannot build right now because my laptop is dead and I am currently using someone else's 😭.
[10-17-2021 17:41:34] <kayabaNerve> I actually don't know what the multisig discussion is about :p
[10-17-2021 17:41:39] <wfaressuissia> "https://github.com/monero-project/research-lab/issues/67" considering that is was mentioned long time ago
[10-17-2021 17:41:41] <kayabaNerve> It's why I said so much when I was summoned
[10-17-2021 17:41:45] <UkoeHB> wfaressuissia: well the address attacks are a lot easier to exploit. I think you need a multisig tx with >=9 inputs to exploit wagner.
[10-17-2021 17:41:58] <kayabaNerve> I figured it was about the Triptych work and immediately wanted to distance myself from any expectations
[10-17-2021 17:42:08] <kayabaNerve> UkoeHB makes it sound like a C++ Monero PR
[10-17-2021 17:42:26] <UkoeHB> kayabaNerve: it is unrelated to Triptych
[10-17-2021 17:42:34] <kayabaNerve> I would love more info :)
[10-17-2021 17:42:40] <wfaressuissia> " I think you need a multisig tx with >=9 in ..." then 16 should be reduced without fix for Wagner's attack
[10-17-2021 17:42:54] <UkoeHB> it is 16 output limit, infinite inputs
[10-17-2021 17:43:32] <kayabaNerve> Oh
[10-17-2021 17:43:38] <wfaressuissia> `constexpr std::uint32_t MULTISIG_MAX_SIGNERS{16};` I'm about this limit
[10-17-2021 17:43:53] <UkoeHB> the number of signers is unrelated (mostly)
[10-17-2021 17:44:07] <rbrunner> Yes, that's the number of outputs. You can easily construct 100-input txs
[10-17-2021 17:44:20] <kayabaNerve> Considering no one currently uses m-of-n, though I do personally insist it's preserved as I know how it can be used, I'm surprised to hear this got attention
[10-17-2021 17:44:38] <kayabaNerve> I'm also surprised to hear it has that limit which seems arbitrary (I do recognize it's 2^4)
[10-17-2021 17:45:08] <rbrunner> Well, 2/3 is very much in use
[10-17-2021 17:45:09] <dEBRUYNE> kayabaNerve: It's this PR -> https://github.com/monero-project/monero/pull/7877
[10-17-2021 17:45:20] <UkoeHB> I introduced the limit of 16 in my multisig PR because of combinatorial explosion during address generation with the MRL-0009 address gen approach.
[10-17-2021 17:45:32] <wfaressuissia> "the number of signers is unrelated (mostly)" number of participants in multisig is unrelated ?
[10-17-2021 17:45:38] <kayabaNerve> rbrunner: Good to know. I saw a Reddit post about a year ago where no one chimed in. I would've guessed the CCS used it though
[10-17-2021 17:45:40] <UkoeHB> unrelated to Wagner attack
[10-17-2021 17:45:41] <wfaressuissia> * max number ...
[10-17-2021 17:45:53] <kayabaNerve> And what's the Wagner attack?
[10-17-2021 17:46:07] <kayabaNerve> I'm very late to this party yet would love to learn more
[10-17-2021 17:46:13] <kayabaNerve> I do know of FROST though
[10-17-2021 17:46:17] <UkoeHB> It's actually Drijvers attack: https://github.com/UkoeHB/drijvers-multisig-tech-note
[10-17-2021 17:47:24] <rbrunner> Ah, now I see, MULTISIG_MAX_SIGNERS. Of course.
[10-17-2021 17:47:33] <UkoeHB> FROST address generation is more efficient if you have `N - M > 1`, so it could allow unlimited signers. But, I am not going to implement it.
[10-17-2021 17:48:15] <coinstudent2048[> UkoeHB: So we stick with commit-and-reveal?
[10-17-2021 17:48:34] <UkoeHB> coinstudent2048[: what do you mean? we don't have commit-and-reveal now
[10-17-2021 17:48:52] <UkoeHB> binonce signing is much easier to implement to mitigate Drijvers
[10-17-2021 17:48:52] <coinstudent2048[> sorry, that's address gen. never mind
[10-17-2021 17:50:23] <coinstudent2048[> UkoeHB: I never saw "address generation" so I thought you'll not implement FROST. sorry
[10-17-2021 17:50:25] <kayabaNerve> How does Drijvers attack work given it seems to rely on generating the same scalar for two different hashed values?
[10-17-2021 17:50:33] <UkoeHB> It would be helpful to me if someone else could implement the Drijvers fix for current Monero multisig. Can look at my demo here: https://github.com/UkoeHB/monero/blob/seraphis_perf/src/mock_tx/seraphis_composition_proof.cpp.
[10-17-2021 17:50:58] <UkoeHB> kayabaNerve: I wrote that tech note to explain my understanding.
[10-17-2021 17:52:16] <rbrunner> Is any of this stuff that only works if all signers are on the same release level? If yes, a hardfork would be a really good time to introduce it.
[10-17-2021 17:52:34] <rbrunner> Because only a hardfork forces update
[10-17-2021 17:53:23] <UkoeHB> rbrunner: you can also just change message serialization, so if two versions try to interact they will error out - forcing lower version to update
[10-17-2021 17:53:59] <rbrunner> Ok, yes. But might to lead to bad UX, right?
[10-17-2021 17:54:12] <UkoeHB> yep
[10-17-2021 17:55:04] <wfaressuissia> It's expected that parties in multisig can force each other to update client
[10-17-2021 17:56:17] <rbrunner> Still, a hardfork and after that a clean slate release-wise would be very nice for multisig. It's complicated enough as it is.
[10-17-2021 17:56:38] <rbrunner> Thus maybe not put too much into it now, IMHO.
[10-17-2021 17:56:52] <UkoeHB> one engineering aspect is the need to clear cached partial-tx stuff when updating
[10-17-2021 17:58:18] <UkoeHB> rbrunner: do you mean delay the Drijvers solution until after hardfork?
[10-17-2021 17:58:45] <rbrunner> Yes. Or maybe even delay until Seraphis, who knows. Depends how things develop.
[10-17-2021 17:59:34] <rbrunner> But I can't judge severity, I have to confess.
[10-17-2021 18:00:03] <rbrunner> Just thinking about the release schedule, and how to hardfork relatively early, to get bigger rings.
[10-17-2021 18:00:21] <UkoeHB> I will have more time to write a PR after Seraphis PoC is settled and paper is done. Maybe we can target the release after hardfork, unless someone wants to step up to the plate.
[10-17-2021 18:02:47] <vtnerd_> UkoeHB - the last link you posted doesn't work
[10-17-2021 18:03:18] <UkoeHB> https://github.com/UkoeHB/monero/blob/seraphis_perf/src/mock_tx/seraphis_composition_proof.cpp
[10-17-2021 18:03:20] <UkoeHB> period at end?
[10-17-2021 18:04:23] <wfaressuissia> "... I think you need a multisig tx with >=9 inputs to exploit wagner." is it your own hypothesis or it's proved somewhere already?
[10-17-2021 18:04:36] <vtnerd_> ah yeah obvious
[10-17-2021 18:04:36] <UkoeHB> `unit_tests/seraphis` has a demo of multisig signing
[10-17-2021 18:04:49] <UkoeHB> in that branch
[10-17-2021 18:05:35] <UkoeHB> wfaressuissia: these guys say 9: https://eprint.iacr.org/2020/945 (that's why I said 'I think')
[10-17-2021 18:07:21] <rbrunner> Not sure I understand: Stay under 9 inputs, problem solved?
[10-17-2021 18:09:31] <UkoeHB> The Drijvers attack requires concurrent signing attempts. The easiest way to get concurrent is multiple inputs (multiple parallel tx more rare/difficult).
[10-17-2021 18:09:57] <UkoeHB> Supposedly you need at least 9 concurrent attempts for the attack to be efficient.
[10-17-2021 18:10:58] <rbrunner> Sounds weird :)
[10-17-2021 18:12:26] <wfaressuissia> lambda = upper(log(256, 2))  == 8 ?
[10-17-2021 18:12:27] <wfaressuissia> why 9 ?
[10-17-2021 18:12:36] <UkoeHB> don't ask me lol
[10-17-2021 18:13:16] <UkoeHB> It's in their conclusion
[10-17-2021 18:13:47] <wfaressuissia> polynomial for l > lambda, ok
[10-17-2021 18:17:44] <UkoeHB> Btw there is a bounty on the Drijvers attack (https://github.com/haveno-dex/haveno/issues/103), maybe that can motivate someone :)
[10-17-2021 18:18:11] <UkoeHB> Anyway, I think we can end the meeting here. Thanks for attending everyone
```

# Action History
- Created by: carrington1859 | 2021-10-03T19:59:05+00:00
- Closed at: 2021-10-27T18:37:35+00:00
