---
title: Monero Wallet Transaction Exporter Bugs
source_url: https://github.com/monero-project/monero/issues/8193
author: ACK-J
assignees: []
labels: []
created_at: '2022-02-25T02:52:15+00:00'
updated_at: '2022-05-29T15:34:14+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
An issues I've been having with the exporter includes:
- There is an abundance of excess spaces between each comma-separated value, for example here is the heading once exported.
```
   block,direction,unlocked,                timestamp,              amount,     running balance,                                                            hash,      payment ID,           fee,                                                                                               destination,              amount,index,note

```
- The column named `hash` is not very descriptive and should probably be changed to `transaction hash`
- There is no `output public key` column, this is a very relevant piece of information that I am trying to use in my project

I appreciate all the hard work you guys put into the repo!

# Discussion History
## fiordiconio | 2022-02-25T09:31:30+00:00
Could anyone tell me in which file is this function written in ?


## ACK-J | 2022-02-25T15:59:22+00:00
@fiordiconio https://github.com/monero-project/monero/pull/8177#issue-1131521057 deals with similar issues and modified `src/simplewallet/simplewallet.cpp`. Hope this helps!

## fiordiconio | 2022-03-03T07:45:12+00:00
@ACK-J thank you, I will give that a look

# Action History
- Created by: ACK-J | 2022-02-25T02:52:15+00:00
