---
title: xmrig opencl AMD integrated hash rate 0
source_url: https://github.com/xmrig/xmrig/issues/3779
author: jekv2
assignees: []
labels: []
created_at: '2026-02-04T03:05:18+00:00'
updated_at: '2026-02-05T00:11:40+00:00'
type: issue
status: closed
closed_at: '2026-02-05T00:11:40+00:00'
---

# Original Description
What could be the problem? When ran, the gpu is utilized and so is 15-20GB system ram.

<img width="1368" height="719" alt="Image" src="https://github.com/user-attachments/assets/b18a2b67-57ca-4e88-816d-c1b62726fbb8" />

# Discussion History
## SChernykh | 2026-02-04T08:30:35+00:00
The problem is RandomX is a CPU algorithm. Don't mine it on GPUs, especially integrated ones.

# Action History
- Created by: jekv2 | 2026-02-04T03:05:18+00:00
- Closed at: 2026-02-05T00:11:40+00:00
