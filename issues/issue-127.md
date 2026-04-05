---
title: Huge pages
source_url: https://github.com/xmrig/xmrig/issues/127
author: ITsenhong
assignees: []
labels: []
created_at: '2017-09-28T15:10:10+00:00'
updated_at: '2017-09-29T22:58:43+00:00'
type: issue
status: closed
closed_at: '2017-09-29T22:58:43+00:00'
---

# Original Description
In my case, Huge page is available but unenable. I hear someone say huge enable wI'll double hashrate, does it right? If yes how do i do it? Thanks!

# Discussion History
## ITsenhong | 2017-09-28T15:10:50+00:00
My CPU is Xeon 8 core

## stoffu | 2017-09-28T22:57:32+00:00
Try restarting your computer and launching the miner immediately when the system starts. This worked on my macOS (Intel Core i5 or i7) machines.

## ITsenhong | 2017-09-28T23:44:12+00:00
I will try your suggestions and reply soon. I have another question, My CPU is xeon 8 core with ~46MB L3 cache( using lscpi | grep "cache"). I set config with 8 thread now, when i set 16 thread, hashrate decrease. Does 8 thread best for me? Would you like suggest better confif for me!

## stoffu | 2017-09-29T01:20:27+00:00
I can't say much since I don't own any Xeon processors, but in general you find the best optimal setting by just trying various parameters.

## ITsenhong | 2017-09-29T22:58:43+00:00
After reset. Huge pages still disable. But thanks for help

# Action History
- Created by: ITsenhong | 2017-09-28T15:10:10+00:00
- Closed at: 2017-09-29T22:58:43+00:00
