---
title: 'Cuprate Meeting #92 - Tuesday, 2026-03-03, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1345
author: moo900
assignees: []
labels: []
created_at: '2026-02-24T18:48:42+00:00'
updated_at: '2026-03-03T18:27:59+00:00'
type: issue
status: closed
closed_at: '2026-03-03T18:27:59+00:00'
---

# Original Description
[Cuprate](https://github.com/Cuprate/cuprate) is an effort to create an alternative Monero node implementation.

Location: [Libera.chat, #cuprate](https://libera.chat/) | [Matrix](https://matrix.to/#/#cuprate:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account](https://www.getmonero.org/resources/user-guides/join-monero-matrix.html)

Time: 18:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: @Boog900

Please comment on GitHub in advance of the meeting if you would like to propose a discussion topic.

Main discussion topics:

- Greetings
- Updates: What is everyone working on?
- Project: What is next for Cuprate?
- Any other business

Previous meeting: #1342

# Discussion History
## moo900 | 2026-03-03T18:27:56+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
redsh4de: hello
```
```
hinto: hi
```
```
boog900: 2) updates
```
```
redsh4de: Submitted PR #590 - ports over most of hinto’s #528 exit code changes. Tied it together with my shutdown PRs, so that SIGINT/SIGTERM shutdowns also return their appropriate exit codes
```
```
boog900: me: self reviewing the tapes DB PR, found a couple things I forgot to finish with alt chains. Just going through a last pass over it now then it will be ready. 
```
```
redsh4de: Also pushed a small semantic change to my blockchain syncer PR.

Been running that one locally, works great - startup’s effectively instant upon a peer connection, and no-op downloader starts look to be eliminated
```
```
boog900: There is also an open PR to fjall to fix that bug with writes getting frozen 
```
```
hinto: me: same as last week, no updates (directly) related to Cuprate
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
boog900: Once the database is ready I will go back to work on the RPC
```
```
redsh4de: on standby right now, PRs open to feedback - will have time this week to adjust anything if necessary
```
```
jbabb: any open requests for contributions?  good targets for newcomers?
```
```
jbabb: just check the issues?
```
```
boog900: 0xfffc has recently stated their intention to begin working on Cuprate. In the past I have mostly alocated different people completly different areas of work to reduce the waiting on other people, however I think I want to try split up the RPC work. 
```
```
boog900: At least as an experiment. 
```
```
boog900: I will make some issues on this and then we can allocate tasks to whoever wants to help out on it. 
```
```
redsh4de: I’d be down to help whenever the time comes for it
```
```
boog900: Nice, will go throught the tapes PR then start making some issues. 
```
```
boog900: * Nice, will go through the tapes PR then start making some issues. 
```
```
boog900: anything else anyone wants to discuss today? 
```
```
boog900: hinto do you have a synced node with the current/old DB?
```
```
boog900: or anyone else, I am wondering how long it takes to build the fast sync hashes 
```
```
hinto: 
● cuprated.service
     Loaded: loaded (/etc/systemd/system/cuprated.service; enabled; preset: enabled)
     Active: active (running) since Mon 2025-12-01 22:14:12 UTC; 3 months 0 days ago
   Main PID: 3955640 (cuprated)
      Tasks: 16 (limit: 9516)
     Memory: 1.9G (high: 2.0G max: 2.0G available: 3.1M)
        CPU: 4d 12h 3min 26.792s
     CGroup: /system.slice/cuprated.service
             └─3955640 /home/cuprate/cuprated --config-file /home/cuprate/Cuprated.toml

Mar 03 18:05:32 vmi2497432 cuprated[3955640]: 2026-03-03T18:05:32.700044Z  INFO incoming_block{height=3622255 txs=78}: Successfully added block hash="51c65abf3c9ff3f096d5d4d3ba4e0eb7b06b29f6>
Mar 03 18:09:13 vmi2497432 cuprated[3955640]: 2026-03-03T18:09:13.523638Z  INFO incoming_block{height=3622256 txs=114}: Successfully added block hash="b989bb05cd5749ffbf46d2874868a9763ca39bf>
Mar 03 18:09:34 vmi2497432 cuprated[3955640]: 2026-03-03T18:09:34.535580Z  INFO incoming_block{height=3622257 txs=24}: Successfully added block hash="f377407943e7e5113e9842c4dbcfdb200e555ce4>
Mar 03 18:14:54 vmi2497432 cuprated[3955640]: 2026-03-03T18:14:54.697044Z  INFO incoming_block{height=3622258 txs=111}: Successfully added block hash="35f43ddbaf4ac07494753d4874122541b21e2c7>
Mar 03 18:15:04 vmi2497432 cuprated[3955640]: 2026-03-03T18:15:04.715851Z  INFO incoming_block{height=3622259 txs=0}: Successfully added block hash="0ae87fe395ec6c0486e0f22e2869ce76e8b38b50a>
Mar 03 18:15:58 vmi2497432 cuprated[3955640]: 2026-03-03T18:15:58.401650Z  INFO incoming_block{height=3622260 txs=17}: Successfully added block hash="fceaea96cd65f72832b96105fdfd4bea34eac1c0>
Mar 03 18:16:25 vmi2497432 cuprated[3955640]: 2026-03-03T18:16:25.790502Z  INFO incoming_block{height=3622261 txs=15}: Successfully added block hash="2f8bbae5396f324b896c2af51d5f0ac6a0d30c8a>
Mar 03 18:16:40 vmi2497432 cuprated[3955640]: 2026-03-03T18:16:40.593413Z  INFO incoming_block{height=3622262 txs=4}: Successfully added block hash="c24104841688e8c9d82b8e539a7a529cc64b03bb5>
Mar 03 18:19:40 vmi2497432 cuprated[3955640]: 2026-03-03T18:19:40.801950Z  INFO incoming_block{height=3622263 txs=65}: Successfully added block hash="b6b34af4d4f8b71d9ad32f5f10cfbbc148845e68>
Mar 03 18:21:15 vmi2497432 cuprated[3955640]: 2026-03-03T18:21:15.365723Z  INFO incoming_block{height=3622264 txs=20}: Successfully added block hash="35af4331618321c288d79837a3ed36569317483f>
lines 1-20/20 (END)

```
```
hinto: IIRC it only takes a few seconds
```
```
boog900: yeah the new DB is doing it in 150 milliseconds, which I don't rememeber the old DB doing. 
```
```
boog900: I don't have an old DB to test with tho :(
```
```
boog900: we can end here
```
```
boog900: thanks everyone!
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2026-02-24T18:48:42+00:00
- Closed at: 2026-03-03T18:27:59+00:00
