---
title: 'Am I missing something, or can I not set the multihash for each thread ? '
source_url: https://github.com/xmrig/xmrig/issues/553
author: DrStein99
assignees: []
labels: []
created_at: '2018-04-15T01:54:56+00:00'
updated_at: '2018-04-15T01:57:45+00:00'
type: issue
status: closed
closed_at: '2018-04-15T01:57:45+00:00'
---

# Original Description
Is there a secret setting I can designate which thread affinities use 4k or 2k hash multi ?  

# Discussion History
## DrStein99 | 2018-04-15T01:57:45+00:00
Nevermind.  I was looking at the screen too long and it finally became visible to me:

"multihash-factor": 0,                      // number of hash blocks to process at a time (not set or 0 enables automatic selection of optimal number of hash blocks)
    "multihash-thread-mask" : null,             // for multihash-factors>0 only, limits multihash to given threads (mask), mask "0x3" means run multihash on thread 0 and 1 only (default: all threads)

# Action History
- Created by: DrStein99 | 2018-04-15T01:54:56+00:00
- Closed at: 2018-04-15T01:57:45+00:00
