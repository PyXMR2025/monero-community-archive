---
title: 'Cuprate Meeting #74 - Tuesday, 2025-11-04, UTC 18:00'
source_url: https://github.com/monero-project/meta/issues/1287
author: moo900
assignees: []
labels: []
created_at: '2025-10-28T18:51:15+00:00'
updated_at: '2025-11-04T18:28:48+00:00'
type: issue
status: closed
closed_at: '2025-11-04T18:28:48+00:00'
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

Previous meeting: #1283

# Discussion History
## moo900 | 2025-11-04T18:28:46+00:00
## Meeting logs
```
boog900: 1) greetings 
```
```
hinto: hello
```
```
boog900: 2) updates 
```
```
hinto: me: debugging monerod (I am starting to miss Rust tooling)
```
```
boog900: Me: I tried to sync on a HDD to test the new database and got quite painful results so spent time trying to improve performance there  
```
```
hinto: It might be a bit early although I also started a draft for a Cuprate 2025 progress report, similar to: https://www.reddit.com/r/Monero/comments/1ij2sw6/cuprate_2024_progress_report, it currently contains updates on the roadmap (https://github.com/Cuprate/cuprate/issues/376) which I think was fairly accurate for this year in terms of scope
```
```
boog900: I will be trying a sync again in a few minutes to see if I managed to improve things 
```
```
boog900: weirdly it is faster on an SSD so 🤷
```
```
hinto: What are the HDD specs? RPM and/or MB/s? 
```
```
boog900: 7200rpm 
Drive Transfer Rate 600 MBps (external)
Internal Data Rate 	210 MBps

```
```
boog900: it took like 15 hours to sync the first 1,300,000 blocks 
```
```
boog900: I don't know how monerod would compare 
```
```
boog900: I stopped it after that 
```
```
hinto: personally I think the current sync speeds are already more than good enough, it is already _multiples_ faster than `monerod`
```
```
hinto: although it seems you have an insatiable desire for speed
```
```
boog900: 15 hrs to sync that many blocks means we were looking at months for the sync time
```
```
boog900: I have already made the changes now anyway lol lets hope they improved things 
```
```
boog900: 3) Project: What is next for Cuprate?
```
```
hinto: would the rest of the chain take that long? I know it is slower although surely only a few days?
```
```
boog900: I can sync the first 1,300,000 blocks in minutes on my SSD
```
```
boog900: the full chain takes 2 hrs 
```
```
boog900: anything you want to discuss this meeting hinto 
```
```
hinto: Not much, although there are a few small PRs that would be nice if they were merged since CI is broken
```
```
hinto: typos, doc comments, clippy fixes etc need to be applied
```
```
boog900: sure will get to them now 
```
```
hinto: I'm also wondering if it is worth continuing with the ZMQ proposal, it is getting pretty long and I could be spending time on just implementing  
```
```
hinto: Up to you since these proposals are mostly to discuss impl details upfront before work
```
```
boog900: I don't think you need to write out everything, a rough overview would be good though 
```
```
boog900: do you have a draft ready now?
```
```
hinto: It's a skeleton with many missing details to fill out, I'll shorten it and post it soon
```
```
boog900: alright thanks 
```
```
hinto: There's still a few misc CI stuff left, I'll make a PR
```
```
hinto: other than that, I have nothing else to discuss
```
```
boog900: ok we can end here, thanks 
```
```
boog900: !meeting 
```

# Action History
- Created by: moo900 | 2025-10-28T18:51:15+00:00
- Closed at: 2025-11-04T18:28:48+00:00
