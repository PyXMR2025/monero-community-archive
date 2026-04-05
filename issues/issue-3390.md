---
title: Dual EPYC issue;
source_url: https://github.com/xmrig/xmrig/issues/3390
author: SADA-POOL
assignees: []
labels: []
created_at: '2023-12-26T13:32:29+00:00'
updated_at: '2025-06-16T19:48:53+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:48:53+00:00'
---

# Original Description
I have dual 7T83 Epyc's on Supermicro H12DSi-N6 MB with 16x8GB DDR4 3200 RAM.
If I set xmrig config to use only one CPU cores (full 128 threads) I get 63kH on RandomX;
I cant get past 90kH when using both CPU's.
I tried multiple combinations of threads, nothing helps.
I'm using huge pages and 1GB pages.
Any idea what to do here next?

# Discussion History
# Action History
- Created by: SADA-POOL | 2023-12-26T13:32:29+00:00
- Closed at: 2025-06-16T19:48:53+00:00
