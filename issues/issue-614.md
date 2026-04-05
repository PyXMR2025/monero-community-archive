---
title: new format for huge pages diag - pls describe meaning of fields after READY
  (CPU) threads
source_url: https://github.com/xmrig/xmrig/issues/614
author: lisergey
assignees: []
labels:
- question
created_at: '2018-05-07T10:55:02+00:00'
updated_at: '2018-05-07T20:26:47+00:00'
type: issue
status: closed
closed_at: '2018-05-07T20:26:47+00:00'
---

# Original Description
@xmrig, pls describe what each number in each field in the string means:
`READY (CPU) threads 6(12) huge pages 0/12 0.000000% memory 24.0 MB`
what is good sign and what is not?
thank you

# Discussion History
## xmrig | 2018-05-07T19:47:13+00:00
`threads 6(12)` you run 6 double hash threads, so it 12 virtual threads.
`huge pages 0/12 0.000000%` 0 of 12 (0%) huge pages allocated, it's bad.
`memory 24.0 MB` threads require 24 (6 * 2 * 2) MB of memory, it should fit into CPU cache.

## lisergey | 2018-05-07T20:17:59+00:00
So is it like that
`threads` **number of used threads**`(`**number of virtual threads**`)`
`huge pages` **used huge pages number**`/`**required huge pages number**  **persentage of used to required**`%`
`memory` **required size of memory for huge pages** `MB`
?

## lisergey | 2018-05-07T20:19:31+00:00
This new string is very informative and useful. Thank you!

## xmrig | 2018-05-07T20:23:44+00:00
> So is it like that

Exactly right, also previous versions can't partially allocate huge pages, was only 2 states 0% or 100%.

# Action History
- Created by: lisergey | 2018-05-07T10:55:02+00:00
- Closed at: 2018-05-07T20:26:47+00:00
