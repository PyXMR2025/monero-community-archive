---
title: Limit bandwidth usage for each peer
source_url: https://github.com/monero-project/monero/issues/4393
author: nox956
assignees: []
labels: []
created_at: '2018-09-17T06:21:19+00:00'
updated_at: '2018-09-17T07:50:40+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I wonder is there a way to limit bandwidth usage for each peer.

I know that daemon came with function that limit down/up (limit_down/up) bandwidth usage, but when a single peer use a lot of bandwidth I found it will create high iowait and has bad effect to syncing with latest block intime.

The only way to prevent this problem is lower my global limit and it will ends up occured another problem - not enough bandwidth to communicate with all peers (maybe one of them still used almost all the bandwidth), so syncing with monero network might be delayed.

This situation happend severely to HDD or slower storage equipment, manually ban these nodes is not a longterm soulution, so I hope there is some way that I can limit bandwidth usage of "each" peer. 

Thanks!

# Discussion History
## moneromooo-monero | 2018-09-17T07:34:50+00:00
No. Seems like something worth adding though.

## nox956 | 2018-09-17T07:50:40+00:00
@moneromooo-monero  Thank you for your prompt reply, I'm really looking forward to that function, it will be easier for people to build their node with old computer or lower budget vps!

# Action History
- Created by: nox956 | 2018-09-17T06:21:19+00:00
