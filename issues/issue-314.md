---
title: No active pools, stop mining
source_url: https://github.com/xmrig/xmrig/issues/314
author: davwheat
assignees: []
labels: []
created_at: '2018-01-03T13:01:32+00:00'
updated_at: '2018-11-05T12:34:42+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:34:42+00:00'
---

# Original Description
My GPU miner sometimes says no active pools, stop mining on startup, other times it says connection reset by peer, and sometimes it says nothing at all.

Also if I try to switch from cryptonight-lite to just cryptonight it gives me a CUDA error

It works fine when mining CPU, but not GPU.

GPU: https://puu.sh/yTlL3/93ca6fb92a.png
CPU: https://puu.sh/yTlP2/2578642ab8.png

# Discussion History
## davidtavarez | 2018-01-03T13:24:36+00:00
You need to check if your connection with the pool. Maybe is really slow.

## davwheat | 2018-01-03T14:21:47+00:00
But how come it works on the CPU miner, but not the Nvidia GPU miner?

On 3 Jan 2018 1:24 pm, "David Tavarez" <notifications@github.com> wrote:

> You need to check if your connection with the pool. Maybe is really slow.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/314#issuecomment-355010803>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/AHEE5simPRAKql3cTYxUg9LJWExIlaW8ks5tG3-XgaJpZM4RRs2T>
> .
>


# Action History
- Created by: davwheat | 2018-01-03T13:01:32+00:00
- Closed at: 2018-11-05T12:34:42+00:00
