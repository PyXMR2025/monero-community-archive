---
title: '[feature request] make a cancellation of pulling and parsing blocks in wallet'
source_url: https://github.com/monero-project/monero/issues/4335
author: naughtyfox
assignees: []
labels: []
created_at: '2018-09-03T17:39:41+00:00'
updated_at: '2019-04-15T09:34:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Wallet library processes blocks with bulk and processing of each bulk on mobile devices may take up to several minutes between requesting refresh pause and getting `refreshed` callback. 
We propose to make cancellation points in pulling-parsing blocks cycle to reduce time needed to stop synchronization. It will make mobile wallets interface more responsive. 
If you agree with this proposal we can implement it by ourselves.

# Discussion History
## moneromooo-monero | 2018-09-03T18:39:15+00:00
How about just setting a custom batch size ?

## naughtyfox | 2018-09-04T10:18:03+00:00
It may help to close an app faster, but it will affect sync proccess

## moneromooo-monero | 2018-09-04T11:54:41+00:00
Looking at the code, it's just down to some if(!m_run.load()) break; so it looks fine.

## naughtyfox | 2018-09-04T14:49:59+00:00
`pull_and_parse_next_blocks` takes a lot of time on devices and has no cancellation points

## moneromooo-monero | 2018-09-20T15:05:03+00:00
If you're going to do that, pony will starting making preliminary builds in the next few days, so be quick :)

## naughtyfox | 2018-09-20T17:40:13+00:00
I have patch for my branch. Just checked out if I can apply it to master and decided... no, I can't do it right now because my release-successor branch differs from current master too much and I can't guarantee I can provide working version in a few days. I propose to postpone it for a while. When new release is ready and we will merge release with our patches I will make PR. 

Thank you for noticing me.

## moneromooo-monero | 2019-04-14T10:11:12+00:00
I just saw that again while looking around. Time for a PR ?

## naughtyfox | 2019-04-15T09:34:30+00:00
I think this issue may be closed or postponed. When I have a chance to implement it properly I'll make a PR.

# Action History
- Created by: naughtyfox | 2018-09-03T17:39:41+00:00
