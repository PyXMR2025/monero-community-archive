---
title: '[Feature request] [monerod] Display how many blocks left when syncing'
source_url: https://github.com/monero-project/monero/issues/4014
author: leafcutterant
assignees: []
labels: []
created_at: '2018-06-17T21:57:40+00:00'
updated_at: '2019-06-15T17:33:37+00:00'
type: issue
status: closed
closed_at: '2019-06-15T17:33:37+00:00'
---

# Original Description
For now you see two huge numbers with each new set of blocks that you download while you're catching up. This makes it difficult to tell how far you are from getting fully synced. Displaying a `Blocks left: XXXX` at the end of each sync info line would make life easier for non-GUI users.

# Discussion History
## Jorropo | 2018-06-18T05:22:01+00:00
It was made in #4020

## leafcutterant | 2018-06-18T12:29:12+00:00
Thanks, you're awesome and very quick! Closing this.

## leafcutterant | 2019-02-19T21:41:35+00:00
I'm reopening this as the solution implemented is insufficient.

What #4020 does is it displays percentage progress and how blocks are left *below a level of progress* (99% of the full blockchain height).

If the user has less than 1% of the full height to sync, this function won't help them to get a picture about their progress.

I propose always displaying how many blocks are left.

An additional improvement could be what I described in the second paragraph of my comment [here](https://github.com/monero-project/monero/pull/4020#issuecomment-407210275).

## moneromooo-monero | 2019-06-15T10:52:59+00:00
It does display the number of blocks left to sync now.

+resolved

# Action History
- Created by: leafcutterant | 2018-06-17T21:57:40+00:00
- Closed at: 2019-06-15T17:33:37+00:00
