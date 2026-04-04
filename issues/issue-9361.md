---
title: 'Disucssion: FIRST_REFRESH_GRANULARITY set too high; causing excessive node
  bandwidth / processing'
source_url: https://github.com/monero-project/monero/issues/9361
author: AlwaysCompile
assignees: []
labels:
- discussion
- more info needed
created_at: '2024-06-11T18:47:06+00:00'
updated_at: '2024-11-13T21:41:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
My friend was able to analyze the bugs reported in #9358 and the first issue is related to FIRST_REFRESH_GRANULARITY. This value is currently set to 1024, which means a user must re-download up to the last 1024 blocks and process them on every wallet startup.

The appears to have been created in 2018 here: https://github.com/monero-project/monero/pull/3998

In 2018 Monero had about 4,000 transactions per day. You can see this here: https://moneroj.net/translin/

In 2024 it has 40,000 transactions per day or 10x as many. Maybe in 2025 it will have 200,000 per day, who knows.

The point is that 1024 blocks was chosen in 2018 based on 2018 network numbers. Now it requires 10x the bandwidth and processing as it did in 2018 and ruins user experience and puts excessive demands on node operators.

I think that it makes sense to lower this number. In 2018 Monero had few users and few transactions, so it needed a higher number to provide more fuzziness to reduce tracking. Now, it has more users, more nodes, more transactions. So, a smaller number can provide the same level of protection as 2018.

In addition, unlike 2018, more users use Tor to defeat IP tracking. With Tor, a smaller number is also needed.

# Discussion History
## 0xFFFC0000 | 2024-11-13T19:32:27+00:00
This appears to me to be an invalid description.

`FIRST_REFRESH_GRANULARITY` is not about downloading that many blocks (or even hashes, as I am going to explain) [1]. 

`FIRST_REFRESH_GRANULARITY` is only passed to `get_short_chain_history` which is a way of creating a (very tiny) view of the blockchain [2]. 

For example: 
```
Blockchain:    [Genesis] ... [Base] ... [Block N-3] [Block N-2] [Block N-1] [Block N]
                                                                            ↓ Latest

Short Chain Collection (order of addition):
1. First 10 blocks: Every block
[N] → [N-1] → [N-2] → [N-3] → [N-4] → [N-5] → [N-6] → [N-7] → [N-8] → [N-9]

2. Then exponentially increasing gaps (multiplier *= 2):
[N-11] → [N-15] → [N-23] → [N-39] → ...

3. Finally adds:
- Base block (if not already included)
- Genesis block (if there's an offset)

Final list order: [N] → [N-1] → [N-2] → ... → [Base] → [Genesis]
```

And to be specific we use `FIRST_REFRESH_GRANULARITY` as a multiplier. Not the distance. 


1. https://github.com/monero-project/monero/blob/893916ad091a92e765ce3241b94e706ad012b62a/src/wallet/wallet2.cpp#L4036

2. https://github.com/monero-project/monero/blob/893916ad091a92e765ce3241b94e706ad012b62a/src/wallet/wallet2.cpp#L3012

# Action History
- Created by: AlwaysCompile | 2024-06-11T18:47:06+00:00
