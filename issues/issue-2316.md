---
title: Limit the CPU usage web browsing while mining
source_url: https://github.com/xmrig/xmrig/issues/2316
author: hss78
assignees: []
labels: []
created_at: '2021-04-25T22:55:47+00:00'
updated_at: '2021-04-26T13:02:53+00:00'
type: issue
status: closed
closed_at: '2021-04-26T13:02:53+00:00'
---

# Original Description
Hey i am using "--cpu-priority 0" but it is still laggy for web browsing.Is it possible to use example %80 CPU usage for mining,so we can web browsing without lag ? Thanks.

# Discussion History
## snipeTR | 2021-04-25T22:57:49+00:00
cmd.exe /c start /LOW "xmrig" xmrig.exe

## hss78 | 2021-04-25T23:05:27+00:00
Will we add this to start.cmd ? Thanks

## Lonnegan | 2021-04-26T09:00:53+00:00
You can use pause-on-active in the config.json. When you set e.g. the number 5 instead of false, the miner pauses for 5 seconds when you click a website and resumes 5 seconds afterwards when you watch/read the website.

## hss78 | 2021-04-26T13:02:53+00:00
Thanks for the info

# Action History
- Created by: hss78 | 2021-04-25T22:55:47+00:00
- Closed at: 2021-04-26T13:02:53+00:00
