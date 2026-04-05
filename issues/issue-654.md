---
title: how to change xmrig cpu miner process name
source_url: https://github.com/xmrig/xmrig/issues/654
author: lighttech1
assignees: []
labels:
- question
created_at: '2018-05-29T00:07:16+00:00'
updated_at: '2018-07-25T07:31:26+00:00'
type: issue
status: closed
closed_at: '2018-05-30T09:06:21+00:00'
---

# Original Description
hello, i would like to change xmrig cpu miner process name in task manager can anyone help me please

# Discussion History
## k0ste | 2018-05-29T02:34:28+00:00
`mv xmrig not_xmrig`

## xmrig | 2018-05-30T09:06:21+00:00
Change it in [version.h](https://github.com/xmrig/xmrig/blob/master/src/version.h) and recompile or use alternative way, tools like Resource Hacker can change it too without compilation.
Thank you.

## emailyc | 2018-07-25T07:31:26+00:00
how to change the name of the compiled .exe file?

# Action History
- Created by: lighttech1 | 2018-05-29T00:07:16+00:00
- Closed at: 2018-05-30T09:06:21+00:00
