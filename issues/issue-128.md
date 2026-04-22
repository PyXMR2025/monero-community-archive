---
title: How do I correct low hash rate in config file?
source_url: https://github.com/xmrig/xmrig/issues/128
author: ghost
assignees: []
labels:
- question
created_at: '2017-09-28T15:25:07+00:00'
updated_at: '2017-10-15T09:24:32+00:00'
type: issue
status: closed
closed_at: '2017-10-15T09:24:32+00:00'
---

# Original Description
I have an intel i5-5200U and I am only receiving around 40H/s, I see other people who are using various i5 CPU's that are getting much higher H/s.  Someone told me I might have a bunch of L3 cache misses, and I also read that this model only has 3MB of L3 cache which means i will only be able to run 1 or 2 processors.  This person also suggested I mess with the --cpu-affinity or --av flags, but i'm not sure how to configure this and what it would do.  I am new to this so I apologize for ignorance.  

# Discussion History
## xmrig | 2017-09-30T11:44:26+00:00
You can manually specify threads count, and see difference. Some people reports get maximum when use 4 threads, sounds crazy but. Huge pages is important it gives 10-30% boost.
Also it mobile CPU, with low TDP and specs looks like desktop i3.

# Action History
- Created by: ghost | 2017-09-28T15:25:07+00:00
- Closed at: 2017-10-15T09:24:32+00:00
