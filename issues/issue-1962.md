---
title: Kawpow memory issue...
source_url: https://github.com/xmrig/xmrig/issues/1962
author: berghemhack
assignees: []
labels: []
created_at: '2020-12-03T07:21:06+00:00'
updated_at: '2021-02-07T19:50:06+00:00'
type: issue
status: closed
closed_at: '2021-01-05T15:22:46+00:00'
---

# Original Description
.

# Discussion History
## Spudz76 | 2020-12-04T09:11:35+00:00
Would imagine the slower family card is goofing up the loop timing.  Is it stable with the 4GB Baffin disabled and just the three of the same 8GB card?

## ghost | 2021-02-07T18:07:27+00:00
This issue seems closed... ok. Don't blame me but I didn't want to open another ticket in this case. 
So I'm still having this kind of problem with my GTX 780 (3GB) and setted my virtual memory like : GPU mem size * number of GPU.  Am i right ?

Here the logs,
KawPow light cache for epoch 215 calculated (8488ms)
KawPow failed to initialize DAG: <kawpow_prepare>:62 "out of memory"

Anyone ?

## SChernykh | 2021-02-07T19:50:06+00:00
@M4shy KawPow DAG size is 2.7 GB now, it's not enough memory on a 3 GB card if you're running Windows 10. Try Windows 7 or Linux, they leave more GPU memory available for mining.

# Action History
- Created by: berghemhack | 2020-12-03T07:21:06+00:00
- Closed at: 2021-01-05T15:22:46+00:00
