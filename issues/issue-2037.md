---
title: Add a task size param
source_url: https://github.com/xmrig/xmrig/issues/2037
author: ahTy
assignees: []
labels:
- duplicate
created_at: '2021-01-12T09:41:50+00:00'
updated_at: '2021-01-13T01:26:03+00:00'
type: issue
status: closed
closed_at: '2021-01-12T11:39:23+00:00'
---

# Original Description
**Describe the question**
Compared with the number of threads, the intel server cpu three-level cache cannot allocate 2M three-level cache per thread, so there is a great waste of resources

**To Reproduce**
Add a task size param  to avoid the problem of three-level cache jitter, then we can dynamically adjust the number of threads of our own cpu and the size of the three-level cache

# Discussion History
## xmrig | 2021-01-12T11:39:00+00:00
https://github.com/xmrig/xmrig/blob/master/doc/CPU.md you can play with various threads configurations. Please note in your case for RandomX algorithms the limiting factor is L2 cache.
Thank you.


## xmrig | 2021-01-12T11:39:23+00:00
Duplicate #2036

## ahTy | 2021-01-13T01:26:03+00:00
> [https://github.com/xmrig/xmrig/blob/master/doc/CPU.md，](https://github.com/xmrig/xmrig/blob/master/doc/CPU.md)您可以使用各种线程配置。请注意，对于您的RandomX算法，限制因素是二级缓存。
> 谢谢。

I have 15M L3 cache, 16 Threads. Can I adjust the size of the task to allow me to use more threads

The problem now is that my L3 cache is only 15M. When I run more threads, I will encounter the problem of the 3L cache jitter, and my efficiency will decrease at this time.

I want to reduce the size of the task once, so that my L3 cache can accommodate more tasks at the same time

# Action History
- Created by: ahTy | 2021-01-12T09:41:50+00:00
- Closed at: 2021-01-12T11:39:23+00:00
