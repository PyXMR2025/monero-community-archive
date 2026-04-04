---
title: 'Cuprate Meeting #1 - Tuesday, 2024-04-30, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/996
author: hinto-janai
assignees: []
labels: []
created_at: '2024-04-25T19:28:48+00:00'
updated_at: '2024-04-30T19:14:05+00:00'
type: issue
status: closed
closed_at: '2024-04-30T19:14:05+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

This marks the project's first weekly meeting, all interested parties from the community are free to join.
 
Note that there are currently communication issues with Matrix accounts created on the `matrix.org` server, consider using a different homeserver to see messages.

---

Location: [Libera.chat, #cuprate](https://libera.chat) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: boog900

---

Main discussion topics:
- Greetings
- Updates: What is everyone working on?
- Project: What is next for Cuprate?
- Any other business

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

# Discussion History
## hinto-janai | 2024-04-30T19:14:05+00:00
Logs:

```
18:00:18 - boog900: Meeting time! https://github.com/monero-project/meta/issues/996
18:00:26 - boog900: 1) Greetings
18:00:32 - SyntheticBird: Hello
18:01:30 - hinto: hi
18:01:50 - boog900: 2. Updates
18:02:54 - SyntheticBird: Me: I'm giving myself some time to properly read the database code this week, so that I can discuss your current advancements.
18:04:22 - hinto: me: finishing thread-pool impl, after that it should only be cleanup left
18:04:28 - m-relay: <p​lowsof> hi
18:05:20 - hinto: SyntheticBird: maybe wait until #117 is finished, there are still lots of docs to be written
18:06:17 - boog900: I am going to give a small update on my CCS seen as this is the first meeting, I have implemented the peer set and outbound connection maintainer so Cuprate can now maintain connections. I have also done the broadcast service, and created a crate that implements d++ I am yet to integrate it into the cuprate p2p code though. I have also started the block downloader 
18:06:32 - SyntheticBird: Fair enough. I'll focus on reinforcing my crypto understanding then. I have to understand bulletproof
18:06:51 - boog900: most of this was done in a separate branch which I have been splitting up over the past few days 
18:07:28 - boog900: any more updates or should we move on?
18:07:49 - SyntheticBird: no more work update i think
18:08:13 - boog900: Ok then. Project: What is next for Cuprate?
18:08:20 - hinto: is yamabiiko here?
18:08:36 - boog900: they said they would be...
18:08:40 - SyntheticBird: I don't think so.
18:10:16 - SyntheticBird: I want notify in this section of the meeting, that I'm planning on returning working on Cuprate development effort, at most June 23rd. This is later than I anticipated but I'll be able to work almost everyday during summer
18:11:33 - SyntheticBird: May I ask what are exactly the remaining part until cuprate being able to Sync and First release ?
18:14:08 - boog900: I still need to polish the block downloader, but when that is ready I think it would be relatively easy to shim the block downloader, consensus code and database together to test a sync.
18:14:39 - boog900: for first release though I would want to wait for the RPC interface to be completed 
18:16:16 - SyntheticBird: That is good sign. Regarding RPC, I haven't yet received your critics regarding my RPC UX proposal, I know many users are against the "Whitelisted RPC" change.
18:17:02 - SyntheticBird: Since yamabiiko RPC is still a design proposal, now would be the good time to know if we should incorporate proposal 1 or 3.
18:19:47 - hinto: i think we're still missing an overview of what RPC will actually look like, what the scope will be, etc
18:21:15 - SyntheticBird: Ok. For another day ig
18:21:41 - hinto: boog900: I can take your plans so far and create some rough drafts and we can go back-and-forth on an issue, or if you think it'll be faster you could write it all out
18:22:41 - Rucknium: I was asked in #MRL about the database interface. I didn't really give an answer since the black marbles had my attention. Monero lacks the Electrum server that bitcoin and its cousins have. `monerod` needs to be the verifier of consensus _and_ serve remote wallets. During the suspected black marble flood, public remote nodes were doing a poor job of both roles. Maybe consider setting up cuprate so that it is easy for another Electrum-like executable to serve the public remote node function:

https://www.sparrowwallet.com/docs/server-performance.html
https://blog.casa.io/electrum-server-performance-report-2022/
18:25:18 - SyntheticBird: <@rucknium:monero.social "I was asked in #MRL about the da..."> So, I presume the actual core RPC interface is too high-level for an Electrum-like server ?
18:26:15 - hinto: Rucknium: IIRC that was a problem due to the several internal components not sharing system resources efficiently, i.e. RPC, DB, etc?
18:27:21 - Rucknium: SyntheticBird: monerod? I don't know. The way that bitcoin-like electrum servers work is that the electrum software requests data from the bitcoin node through RPC. It builds an address index and other indices. With Monero the database would be different since there is no such thing as an address database possible.
18:27:44 - boog900: <@hinto:monero.social "boog900: I can take your plans s..."> I can write it out but it will probably still require some back and forth 
18:28:39 - SyntheticBird: <@boog900:monero.social "I can write it out but it will p..."> Sorry, what plans are we talking about ?
18:28:50 - Rucknium: IMHO (very humble opinion), it could be good to aim to separate the roles of serving wallets and the consensus verification. To serve many remote wallets requires a huge amount of data and monerod callot scale like that now.
18:29:09 - Rucknium: cannot scale*
18:29:21 - hinto: SyntheticBird: using axum + separating the RPC interface from the inner handler itself
18:31:14 - hinto: Rucknium: are you suggesting LWS (cuprate edition)?
18:31:22 - SyntheticBird: <@rucknium:monero.social "IMHO (very humble opinion), it c..."> That would require a very deep UX change. I've some ideas on mind and it should be possible, but I don't want to give you guarantee about it. Something to test for sure
18:32:09 - boog900: <@rucknium:monero.social "IMHO (very humble opinion), it c..."> The way Cuprate is designed requests will go straight to the DB without acquiring any locks, and requests that change the state of the DB will go to a specific task that handles that: tx-pool, syncer etc.  
18:32:10 - Rucknium: LWS is different than a remote node since LWS has the actual view keys of a wallet. When monerod serves remote wallets, it sends all the data without having the wallet's view key
18:33:17 - boog900: so it kinda is already separated inside Cuprate at least
18:33:36 - SyntheticBird: Cuprate is already much more parallelized than monerod and should be more horizontally scalable. Only benefit in doing what you propose would be to shift the RPC serving part in a second OS Process
18:33:41 - Rucknium: bitcoin and cousins have this nice Electrum software, but bitcoin actually needs to send much, much less data to wallets than Monero does because they can just do a database lookup and send the relevant txs.
18:34:22 - Rucknium: Ok. We will see in performance tests I hope :)
18:35:19 - boog900: someone could probably make a standalone binary that caches the top blocks and uses our yet to be created RPC crate to serve requests with the inner request handler going to the local cache or an actual node if it doesn't have the data 
18:35:19 - Rucknium: I am thinking especially of Cake and similar wallets that have to serve many users with its nodes. The black marble flood is a small fraction of what Monero is supposed to scale to.
18:35:55 - SyntheticBird: <@boog900:monero.social "someone could probably make a st..."> A 15 days cacher would actually be game-changing
18:36:18 - Rucknium: According to tuxsudo, Cake received hundreds of support requests per hour during the worst of the spam because user wallets couldn't sync quickly.
18:37:47 - hinto: okay, said simply: better plumbing? I think we can do that :)
18:38:13 - Rucknium: https://libera.monerologs.net/monero-community/20240402#c356862 <- tuxsudo comment
18:38:19 - SyntheticBird: So... A standalone top block cacher with in-memory database + a subset of new RPC specialized interface to accelerate in-between. Would that be viable ?
18:39:42 - boog900: It doesn't have to be in memory, it just has to relive the load from monerod
18:40:29 - SyntheticBird: A simple load balancer would have been good in this case
18:40:37 - SyntheticBird: oh wait no
18:41:03 - SyntheticBird: There others nodes in their load balancer are also dead because of the consensus verifier
18:42:00 - SyntheticBird: Ok I see now why you would want to have one consensus verifying process that link to multiple process serving wallet.
18:42:00 - boog900: monerod can't scale to loads of RPC requests, we need a program that can while still relying on monerod for the data 
18:42:56 - boog900: Anyway this should be possible with the RPC crate, although it would be separate from Cuprate 
18:43:52 - SyntheticBird: I'm don't think we really need it to be separate. It could just be an *amplified* version of the `bootstrap_daemon` functionality
18:44:40 - SyntheticBird: If set, Cuprate will just enable its RPC serving part, requesting all datas with a modified version of your original download you made to mimic the database
18:44:47 - boog900: true but then you would be storing the whole blockchain again, might as well just run Cuprate 
18:45:15 - SyntheticBird: Why would you be storing the blockchain again ?
18:45:48 - SyntheticBird: oh nvm you're right
18:46:57 - hinto: Rucknium: reading that backlog - do you know if networked/remote database storage a common setup in large deployments?
18:47:33 - Rucknium: IIRC monerod does not like to use networked storage
18:47:40 - SyntheticBird: iirc someone asked if they were using networked filesystem and cake said they were not using it. Tho their final step forwards is to move to bare-metal
18:48:06 - Rucknium: Something about LMDB causes crashes IIRC
18:48:16 - hinto: yes, specifically LMDB does not like it, but I believe the 2nd database backend Cuprate uses is fine with it
18:48:26 - Rucknium: Cake put the whole database in RAM
18:48:43 - SyntheticBird: Yes, they have a high-availbility RAM VPS
18:49:15 - Rucknium: RavFX has a five-node setup for his public remote node. You could ask him for details.
18:51:23 - boog900: anything else to discuss today?
18:51:39 - SyntheticBird: I've two other topics in mind
18:51:52 - boog900: go ahead 
18:53:28 - SyntheticBird: 1. Sudo-rs project recently achieved the exploit of passing from 300 dependencies to just 1 (libc). Should we, after first syncing and releases, promote at an effort at cleaning and minimizing dependencies ? `page_size` crate for example could be removed and added to `cuprate-helper`.

2. Should we make a small document on code style, contribution guideline ?
18:55:37 - hinto: re 1: occasional cleanup sounds good - also `page_size` is a dependency of `heed`, it's in our tree regardless
18:55:43 - hinto: re 2: we have a `CONTRIBUTING.md`
18:56:22 - SyntheticBird: > re 2: we have a `CONTRIBUTING.md`

Thanks I haven't seen it ><
18:56:41 - hinto: it isn't completely fill out though, lots of things to add there
18:57:57 - hinto: related: I'd like to add workspace lints eventually - enormous chore but I think sooner is better than later 
19:00:06 - boog900: I don't mind doing that on a case by case basis, but I don't want it to be too restrictive where we still using `allow` everywhere 
19:01:32 - hinto: I think it should be as least restrictive as possible in the workspace, then increasingly more per crate/module/file 
19:02:07 - SyntheticBird: Yes sounds like the way
19:02:43 - hinto: I'll create an issue laying out the particular lints, we can discuss it over time
19:03:02 - boog900: I think we can call it here, thanks everyone!
19:03:15 - SyntheticBird: Thanks
```

# Action History
- Created by: hinto-janai | 2024-04-25T19:28:48+00:00
- Closed at: 2024-04-30T19:14:05+00:00
