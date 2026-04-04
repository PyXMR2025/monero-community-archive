---
title: busy wait
source_url: https://github.com/monero-project/monero/issues/8268
author: BebeSparkelSparkel
assignees: []
labels: []
created_at: '2022-04-19T12:14:40+00:00'
updated_at: '2022-04-25T17:45:20+00:00'
type: issue
status: closed
closed_at: '2022-04-25T17:45:20+00:00'
---

# Original Description
I have managed to sync the entire blockchain but now am having the problem of monerod busy waiting. While observing monerod with `top` the 2 core cpu is completely consumed with 100% Kernel and 100% Spin when it is waiting for more blocks. This effectively freezes the entire computer.

OS: OpenBSD 7.0

# Discussion History
## jeffro256 | 2022-04-21T01:37:57+00:00
Are you using an SSD or a hard drive? What kind of computer?

## BebeSparkelSparkel | 2022-04-21T21:13:28+00:00
The monero files are on an SSD.

Currently, not allowing incoming network transactions.

Hardware: Dell Inspiron 541, dual core, 4Gb ram

OS: OpenBSD 7.0

## jeffro256 | 2022-04-22T15:12:18+00:00
Might be related: https://github.com/monero-project/monero/issues/8210
Can you see if your message queues are overloaded?

## BebeSparkelSparkel | 2022-04-24T01:44:07+00:00
Ran for 90mins with no overflows listed with `dmesg`.
Also, I'm not sure why there would be overflows when no blocks need to be synced.

## jeffro256 | 2022-04-25T16:19:06+00:00
I would post this to https://reddit.com/r/monerosupport because it's not documenting a specific issue, and you're more likely to get help there.

## selsta | 2022-04-25T16:22:48+00:00
Seems to be a duplicate of https://github.com/monero-project/monero/issues/7027

Both on OpenBSD.

## BebeSparkelSparkel | 2022-04-25T17:45:20+00:00
Duplicate

# Action History
- Created by: BebeSparkelSparkel | 2022-04-19T12:14:40+00:00
- Closed at: 2022-04-25T17:45:20+00:00
