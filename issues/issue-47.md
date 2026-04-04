---
title: 'Build: Win64: "fork: Resource temporarily unavailable"'
source_url: https://github.com/monero-project/meta/issues/47
author: anonimal
assignees: []
labels: []
created_at: '2017-02-15T01:33:16+00:00'
updated_at: '2017-03-08T19:16:03+00:00'
type: issue
status: closed
closed_at: '2017-03-08T19:16:03+00:00'
---

# Original Description
`[main] make 4968 fork: child -1 - forked process 6800 died unexpectedly, retry 0, exit code 0xC0000142, errno 11`
https://build.getmonero.org/builders/kovri-all-win64/builds/210/steps/compile/logs/stdio

# Discussion History
## anonimal | 2017-02-15T23:07:47+00:00
Fixed in https://build.getmonero.org/builders/kovri-all-win64/builds/212

## anonimal | 2017-02-15T23:49:37+00:00
Spoke too soon https://build.getmonero.org/builders/kovri-all-win64

## Jaqueeee | 2017-02-16T21:59:34+00:00
@anonimal this was probably my fault. Killed some stuff when i was trying to debug the qt build. 

# Action History
- Created by: anonimal | 2017-02-15T01:33:16+00:00
- Closed at: 2017-03-08T19:16:03+00:00
