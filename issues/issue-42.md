---
title: --max-cpu-usage=N
source_url: https://github.com/xmrig/xmrig/issues/42
author: walruzperil
assignees: []
labels: []
created_at: '2017-07-18T23:35:25+00:00'
updated_at: '2017-07-19T23:57:24+00:00'
type: issue
status: closed
closed_at: '2017-07-19T23:57:24+00:00'
---

# Original Description
Hello, can you explain how works --max-cpu-usage=N 
if i set --max-cpu-usage=10 it mean cpu load only 10%? 

# Discussion History
## xmrig | 2017-07-19T00:22:04+00:00
This option limit number of threads can be used in automatic mode. Has no effect if you manually specify thread count.

Some examples for 4C CPU:
* 75% = 3 threads
* 50% = 2 threads.
* 25% = 1 thread.
* 10% = 1 thread too, CPU usage about 25%.

# Action History
- Created by: walruzperil | 2017-07-18T23:35:25+00:00
- Closed at: 2017-07-19T23:57:24+00:00
