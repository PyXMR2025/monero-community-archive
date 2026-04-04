---
title: 'Cuprate Meeting #2 - Tuesday, 2024-05-07, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1000
author: Boog900
assignees: []
labels: []
created_at: '2024-05-01T01:27:52+00:00'
updated_at: '2024-05-09T15:47:07+00:00'
type: issue
status: closed
closed_at: '2024-05-09T15:47:07+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

> Note that there are currently communication issues with Matrix accounts created on the matrix.org server, consider using a different homeserver to see messages.

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: boog900

Main discussion topics:
- Greetings
- Updates: What is everyone working on?
- Project: What is next for Cuprate?
- Any other business

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Last meeting with logs: #996

# Discussion History
## Boog900 | 2024-05-09T15:46:58+00:00
Logs:

```
18:00:05 - boog900 (@boog900:monero.social): Meeting time https://github.com/monero-project/meta/issues/1000
18:00:15 - boog900 (@boog900:monero.social): 1) Greetings
18:00:42 - yamabiiko: Hi all
18:00:50 - rottenwheel: Hello! 
18:01:46 - m-relay: <plowsof> Hi
18:02:02 - SyntheticBird: Hi
18:02:08 - hinto (@hinto:monero.social): hello
18:02:25 - boog900 (@boog900:monero.social): 2. Updates: What is everyone working on?
18:04:16 - SyntheticBird: me: Took sometimes to better understand monero crypto. Actually focusing on bulletproof. Since last meeting I now comprehend EC basics and pedersan commitment.
18:05:46 - hinto (@hinto:monero.social): me: taking a short break, planning to return with thoughts on current research/development, specifically RPC and the FCMP++ paper
18:06:24 - SyntheticBird: You deserve a break, you've done well your CCS
18:06:28 - boog900 (@boog900:monero.social): Me: I found some issues in our cross-block batch verification, transactions that are currently valid can become invalid without being double spent and our consensus code did not account for that. I tried to find a solution that would work with how we currently do it but the all the ideas I have had are too expensive. 
18:07:42 - yamabiiko: Started looking into different RPC impls, also evaluating boog's input on the proposal to get an overall picture on how would the work be structured 
18:07:50 - boog900 (@boog900:monero.social): this would only effect syncing, my plan now is to just remove cross-block batch verification and in the future look into staged syncing, i.e. checking blocks PoW, then signatures etc.
18:09:06 - kayabanerve (@kayabanerve:matrix.org): 👋
18:09:23 - boog900 (@boog900:monero.social): lets move on ..
18:09:26 - boog900 (@boog900:monero.social): 3. Project: What is next for Cuprate?
18:09:42 - SyntheticBird: Can we say database is now working ?
18:10:56 - boog900 (@boog900:monero.social): Yeah, but we haven't actually done a full sync yet  
18:11:01 - kayabanerve (@kayabanerve:monero.social): I can answer questions/provide context.
18:11:52 - SyntheticBird: <@kayabanerve:monero.social "I can answer questions/provide c..."> Regarding FCMP++ ?
18:12:31 - kayabanerve (@kayabanerve:monero.social): That was my intent but I also can comment on cryptography in general and monero-serai :p
18:13:14 - hinto (@hinto:monero.social): boog900: what are your thoughts on creating a binary to test all components so far?
18:14:02 - hinto (@hinto:monero.social): purely for internal testing, not a binary for the public
18:14:06 - m-relay: <plowsof> Serai was mentioned here on the xmr eth atomic swap protocol https://github.com/AthanorLabs/atomic-swap/issues/512#issuecomment-2067118349
18:18:36 - boog900 (@boog900:monero.social): <@hinto:monero.social "boog900: what are your thoughts ..."> I am currently working towards something like that, the p2p code is not ready to a start the binary just yet 
18:18:48 - hinto (@hinto:monero.social): kayabanerve: what is your workload currently? would you be okay with a larger documentation PR to `monero_serai`? it would need your review for correctness
18:19:26 - SyntheticBird: <@boog900:monero.social "I am currently working towards s..."> Should we start discussing the `cuprated` draft PR in parallel ?
18:19:32 - boog900 (@boog900:monero.social): It shouldn't take too much longer though, to be at that stage 
18:19:35 - hinto (@hinto:monero.social): also wondering what your thoughts on serialization, does integrating serde/borsh/bincode make sense?
18:20:00 - kayabanerve (@kayabanerve:monero.social): hinto: I have a branch tidying monero-serai. If you build on it, I'd love it.
18:20:47 - kayabanerve (@kayabanerve:monero.social): I only want to support the Monero serialization. Its sane enough, necessary, and accordingly without debate.
18:21:25 - kayabanerve (@kayabanerve:monero.social): Anyone can make a bincode wrapper by wrapping an object and impl'ing bincode for the wrapper
18:21:30 - m-relay: <plowsof> For visibility: hintos new coprate proposal https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/456
18:21:57 - boog900 (@boog900:monero.social): <@syntheticbird:monero.social "Should we start discussing the `..."> I think the testing binary should be pretty minimal, we could discuss `cuprated` but I don't think it will be needed for a little while 
18:22:08 - kayabanerve (@kayabanerve:monero.social): I explicitly don't want serde as these types should not be used with serde_json
18:24:11 - boog900 (@boog900:monero.social): monerod provides txs in json format from some RPC methods, right? 
18:24:47 - Rucknium: boog900: Yes
18:25:17 - kayabanerve (@kayabanerve:monero.social): Which is distinct from the layout monero-serai uses
18:25:45 - kayabanerve (@kayabanerve:monero.social): Hence calling out deriving serde
18:26:05 - wolf left the room
18:26:14 - Rucknium: Call `/get_transactions` and set `decode_as_json` to `true`
18:26:18 - SyntheticBird: btw hinto I know you planned on checking the documentation of core RPC on getmonero.org. Could you also note what disparities you have seen. My OpenRPC document should be up to date. I have minor modifications to do and I'll try pushing it to monero core repository. So any report is appreciated
18:26:57 - SyntheticBird: could you also note somewhere what disparities you happen to see*
18:26:57 - hinto (@hinto:monero.social): kayabanerve: `monero-tidy` is the branch to send docs to?
18:27:12 - hinto (@hinto:monero.social): SyntheticBird: I can link PRs/issues here if you want
18:27:21 - hinto (@hinto:monero.social): (if there are any)
18:27:30 - kayabanerve (@kayabanerve:matrix.org): We'd need dedicated RPC types. Those I'm fine placing serde on. I'm just not fine spending the time/effort on RPC types and would rather a periphery crate.
18:27:43 - kayabanerve (@kayabanerve:matrix.org): hinto: Sounds correct :)
18:30:13 - boog900 (@boog900:monero.social): The RPC design issue (I don't think it's been linked yet): https://github.com/Cuprate/cuprate/issues/106
18:30:50 - boog900 (@boog900:monero.social): I left another comment after last weeks meeting, if anyone wants to discuss that 
18:32:16 - SyntheticBird: <@boog900:monero.social "I left another comment after las..."> I've seen it and the`State<S>` definition is the idiomatic way to do so. I've no critics on the `Router` being sent instead of started by the crate
18:32:38 - SyntheticBird: to do so and its fine to me*
18:34:38 - SyntheticBird: Also, afaiu vtnerd recently pushed SSL support for monerod connections, do we need to do something about it at the moment ?
18:35:07 - SyntheticBird: https://github.com/monero-project/monero/pull/8996
18:35:12 - SyntheticBird: PR for reference
18:36:37 - boog900 (@boog900:monero.social): I am not planning to do anything until it's merged 
18:37:13 - SyntheticBird: that's fair
18:37:27 - boog900 (@boog900:monero.social): when it is, I'll add support for it in Cuprate as well 
18:40:41 - SyntheticBird: If there are no more question I think we can move on to next section
18:41:27 - boog900 (@boog900:monero.social): 4. Any other business
18:42:00 - boog900 (@boog900:monero.social): hintos CCS, any comments on that? 
18:45:05 - yamabiiko: I might plan a CCS too in order to be more available for contribution, when the time is right
18:45:12 - yamabiiko: Or as hinto mentioned next CCS could be split
18:47:31 - hinto (@hinto:monero.social): boog: how do you see work being split after the RPC interface?
18:47:33 - hinto (@hinto:monero.social): assuming I finish on time and yamabiiko is available in ~3 months
18:52:44 - boog900 (@boog900:monero.social): hmm, I don't think the RPC inner request handler would be too much work and after that it's the binary and ZMQ 
18:53:23 - boog900 (@boog900:monero.social): depending on how fast I complete my current CCS I would probably start work on the binary 
18:53:45 - hinto (@hinto:monero.social): yamabiiko: are there other components you prefer working on?
18:54:57 - boog900 (@boog900:monero.social): Tor/I2p support but that would be tied up with my current work on the P2P so I will have to finish that before anyone can start on it 
18:56:11 - boog900 (@boog900:monero.social): It would probably be a good idea for me to create an issue with a list of tasks that need to be completed ...
18:56:12 - yamabiiko:  I guess it will depend on what's available/best to work on in around 2 months
18:56:35 - SyntheticBird: <@boog900:monero.social "It would probably be a good idea..."> I think so too. I'll let everyone decide and pick whats left tbh
18:57:00 - boog900 (@boog900:monero.social): <@syntheticbird:monero.social "I think so too. I'll let everyon..."> I mean some stuff should be prioritized 
18:58:36 - SyntheticBird: <@boog900:monero.social "I mean some stuff should be prio..."> you can specify the priority towards public release in the issue
19:01:46 - SyntheticBird: before the end
19:02:28 - SyntheticBird: Maybe we should include miri into the github action. I remember it was brought to discussion in one of the PR recently. Shouldn't we include it sooner than later ?
19:03:09 - Rucknium: Not cuprate-related, but Rust ∩ Monero related: I've worked a little with an implementation of the Dulmage-Mendelsohn decomposition written in Rust: https://github.com/avras/cryptonote-analysis/blob/main/src/bin/dmdec.rs . The DM decomposition can help eliminate decoys in the Monero tx graph in certain cases. The implementation is single-threaded. I'm not sure if the algorithm can be changed to multi-threaded, but if it can, is there any interest in a bounty offer of 1-2 XMR to make it multi-threaded?
19:04:23 - boog900 (@boog900:monero.social): <@syntheticbird:monero.social "Maybe we should include miri int..."> I am unsure it would provide much benefit, I don't think we have any unsafe that isn't bindings, which miri doesn't support IIRC. If we do then yes 
19:05:56 - SyntheticBird: <@rucknium:monero.social "Not cuprate-related, but Rust ∩ ..."> "help elminiate decoys". Could this be used in top of the decoy algorithm to detect weak ring candidates ?
19:07:18 - Rucknium: SyntheticBird: Technically yes, but at ring size 16 the DM decomposition isn't very effective. But it can be more effective if you combined DM decomposition with black marble flooding, which is what I am doing.
19:07:37 - hinto (@hinto:monero.social): Rucknium:

1. It depends on what that program does, but I suggest looking into https://en.wikipedia.org/wiki/GNU_parallel
2. Do you have an intersection key on your keyboard?
19:08:25 - Rucknium: IIRC Monero's old "blackball" algorithm does something similar t othe DM decomposition, but Monero's old algorithm would not be as effective as the DM decomposition at eliminating decoys.
19:09:04 - SyntheticBird: <@rucknium:monero.social "IIRC Monero's old "blackball" al..."> Sorry for the dumb question but is the selection algorithm node related or wallet related ?
19:10:12 - Rucknium: 1) I will look at it. 2) I was waiting for the end of the meeting, so I looked up the intersection symbol and copy-pasted :)
19:11:14 - Rucknium: SyntheticBird: The wallet selects decoys. The node provides the wallet with the statistical distribution of output ages, The wallet applies it decoy selection algorithm to the distribution its gets from the node.
19:13:11 - Rucknium: Here's info on Monero's blackball tool: https://monero.stackexchange.com/questions/8225/how-can-i-use-monero-blockchain-blackball-to-improve-my-privacy
19:14:42 - boog900 (@boog900:monero.social): <@rucknium:monero.social "Not cuprate-related, but Rust ∩ ..."> Is this just because it's slow? or do you specifically want it multi-threaded?  
19:15:24 - SyntheticBird: Should we end the meeting and continue on rucknium question ?
19:15:49 - Rucknium: Yes it's slow. I don't know exactly what the problem is. The original paper said it finished running in 4 hours, but I have a different subset of the blockchain that _should_ be smaller, and it has been running for days.
19:16:57 - Rucknium: There are a huge number of threads on the Monero Research Computing Server/Cluster, but the process can only use one for now.
19:17:24 - boog900 (@boog900:monero.social): whoa ok, I can look at trying to make it quicker, does the repo contain data to test with?
19:17:49 - boog900 (@boog900:monero.social): yeah we can end the meeting here thanks everyone!
19:19:41 - hinto (@hinto:monero.social): Rucknium: if the data set being operated on can't be split easily then you can ignore GNU parallel
19:19:55 - hinto (@hinto:monero.social): thanks everyone
```

# Action History
- Created by: Boog900 | 2024-05-01T01:27:52+00:00
- Closed at: 2024-05-09T15:47:07+00:00
