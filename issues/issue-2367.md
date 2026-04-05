---
title: Randomly my H/s goes from 3k to 300
source_url: https://github.com/xmrig/xmrig/issues/2367
author: randommemer
assignees: []
labels: []
created_at: '2021-05-11T19:46:02+00:00'
updated_at: '2021-05-16T05:55:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I've got a 10750h. Usually I get around 3300 H/s, when not using the laptop, with 25W power but sometimes the hashrate would go down to 200-300. Today it was like that the whole day and I noticed it only when I got back a few hours later. It stayed at around 300 H/s for 5-6 hours while I was away. Just now I got up from the laptop and it went down to 300 for maybe 15 minutes until 1-2 minutes before I sat back down.

# Discussion History
## Spudz76 | 2021-05-11T19:56:51+00:00
If Win10, disable the Memory Compression and the Memory Scanning tasks.

Howto is [over here on reddit](https://www.reddit.com/r/MoneroMining/comments/f18825/windows_10_tuning_guide_for_randomx_mining/) the two I am speaking of are down in the "optional" section number 3 and 4.

If the memory dumbness (either one) runs in the background ever, it kills all the memory bandwidth, leading to the hashrate destruction.

## randommemer | 2021-05-16T05:55:54+00:00
Thank you for the help. I will do so now.

# Action History
- Created by: randommemer | 2021-05-11T19:46:02+00:00
