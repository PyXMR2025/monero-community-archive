---
title: Why my cpu load always is 50%, and can mac use 1GB PAGES?
source_url: https://github.com/xmrig/xmrig/issues/2369
author: MIKE-GUO233
assignees: []
labels:
- question
created_at: '2021-05-12T09:19:59+00:00'
updated_at: '2025-06-16T17:25:16+00:00'
type: issue
status: closed
closed_at: '2025-06-16T17:25:16+00:00'
---

# Original Description
I use my mac to mine the dogecoin, but my cpu load always is 50%. How to use 100% load to mine? I want to improve my hashrate. And the 1GB PAGES is unavailable, can I enable it?
![image](https://user-images.githubusercontent.com/60096490/117950831-2bde3e80-b346-11eb-826d-36fdd45cc9de.png)
![image](https://user-images.githubusercontent.com/60096490/117950942-43b5c280-b346-11eb-8940-eddec7fa01fc.png)


# Discussion History
## SChernykh | 2021-05-12T09:45:14+00:00
50% is normal for Intel CPUs, they are limited by the L3 cache - 2 MB per thread and 16 MB cache means 8 threads is optimal. 1 GB pages are available only on Linux.

## Spudz76 | 2021-05-13T13:13:47+00:00
And you don't have enough free memory to get all the 2MB hugepages although it managed to find 11 of them...

# Action History
- Created by: MIKE-GUO233 | 2021-05-12T09:19:59+00:00
- Closed at: 2025-06-16T17:25:16+00:00
