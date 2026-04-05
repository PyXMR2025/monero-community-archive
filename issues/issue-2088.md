---
title: KawPow failed to initialize DAG
source_url: https://github.com/xmrig/xmrig/issues/2088
author: ghost
assignees: []
labels: []
created_at: '2021-02-07T18:19:39+00:00'
updated_at: '2021-02-08T21:00:36+00:00'
type: issue
status: closed
closed_at: '2021-02-08T21:00:36+00:00'
---

# Original Description
I'm having this kind of problem with a GTX 780 (3GB) and setted my virtual memory like : GPU mem size * number of GPU. Am i right ?

Here the logs,
KawPow light cache for epoch 215 calculated (8488ms)
KawPow failed to initialize DAG: <kawpow_prepare>:62 "out of memory"

Anyone ?

# Discussion History
## SChernykh | 2021-02-07T19:50:35+00:00
@M4shy KawPow DAG size is 2.7 GB now, it's not enough memory on a 3 GB card if you're running Windows 10. Try Windows 7 or Linux, they leave more GPU memory available for mining.

## ghost | 2021-02-08T10:10:22+00:00
Thanks for reply. I've using linux distros as server, my gnome desktop stills somewhere on a older laptop... I didn't know for the memory size. What do you mean by leaving more GPU memory ? With win10, I've tested a min and a max pagefile size [3000, 5000] (mb), the err remains the same.

## SChernykh | 2021-02-08T10:14:25+00:00
NVIDIA drivers on Windows 10 reserve 20% of GPU memory so you only have 2.4 GB available on a 3 GB GPU.

# Action History
- Created by: ghost | 2021-02-07T18:19:39+00:00
- Closed at: 2021-02-08T21:00:36+00:00
