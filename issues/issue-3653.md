---
title: 'kawpow mining: CUDA and GPU recognized but hashrate stays n/a'
source_url: https://github.com/xmrig/xmrig/issues/3653
author: demi-portion
assignees: []
labels: []
created_at: '2025-04-21T09:31:16+00:00'
updated_at: '2025-06-28T10:27:03+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:27:03+00:00'
---

# Original Description
I got this issue while trying to mine RVN : xmrig finds the CUDA drivers and my GPU is recognized but the hashrate stays on n/a forever

- error message: KawPow failed to initialize DAG: <kawpow_prepare>:62 "out of memory"
- NVML failed to load (although I could do without)

I initially thought that the issue is with my GPU's memory being smaller than the current DAG size (>4Gb) but I got it working on a Windows machine with a GPU that also has only 4Gb

Btw there were some errors while compiling the CUDA plugin.

![Image](https://github.com/user-attachments/assets/d03fa443-aed7-4c43-91ac-c6fb365003f5)

![Image](https://github.com/user-attachments/assets/dea8afc1-154a-43df-8a4c-93f69c376b13)


# Discussion History
# Action History
- Created by: demi-portion | 2025-04-21T09:31:16+00:00
- Closed at: 2025-06-28T10:27:03+00:00
