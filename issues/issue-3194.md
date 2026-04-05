---
title: Combining two GPUs' VRAM
source_url: https://github.com/xmrig/xmrig/issues/3194
author: benthetechguy
assignees: []
labels: []
created_at: '2023-01-09T19:17:22+00:00'
updated_at: '2023-01-09T20:16:29+00:00'
type: issue
status: closed
closed_at: '2023-01-09T20:16:29+00:00'
---

# Original Description
I have a 4 GB Radeon RX 6400 that I would like to mine kawpow on when I'm not using the computer, but there's not enough VRAM for the DAG. I'm thinking of buying a second one for purposes unrelated to mining, and I was wondering if it would be a possibility to use their combined 8 GBs of VRAM to fit the DAG.

# Discussion History
## SChernykh | 2023-01-09T19:26:23+00:00
It will be too slow and limited by PCIe bandwidth which is 100-500 times less than VRAM bandwidth.

## benthetechguy | 2023-01-09T20:16:29+00:00
Alright. Thank you for clarifying.

# Action History
- Created by: benthetechguy | 2023-01-09T19:17:22+00:00
- Closed at: 2023-01-09T20:16:29+00:00
