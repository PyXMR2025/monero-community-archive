---
title: OS X Build Issue/Question
source_url: https://github.com/xmrig/xmrig/issues/252
author: taylovision
assignees: []
labels:
- question
created_at: '2017-12-10T19:06:31+00:00'
updated_at: '2017-12-16T12:28:35+00:00'
type: issue
status: closed
closed_at: '2017-12-16T12:28:35+00:00'
---

# Original Description
Whenever I pull up terminal and get xmrig running, I get the following:
```
$ make

[ 12%] Built target cpuid
[100%] Built target xmrig
```
When I run my mining pool and all right after, it all looks normal and runs fine. (seemingly)

My questions is this, is that 12% target cpuid an issue? Should I be concerned it's not mining at all?

# Discussion History
## xmrig | 2017-12-11T10:20:43+00:00
You no need make after succeful build. Run ./xmrig.
Thank you.

# Action History
- Created by: taylovision | 2017-12-10T19:06:31+00:00
- Closed at: 2017-12-16T12:28:35+00:00
