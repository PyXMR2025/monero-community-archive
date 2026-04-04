---
title: 'Build: Ubuntu64: virtual memory exhausted: Cannot allocate memory'
source_url: https://github.com/monero-project/meta/issues/16
author: anonimal
assignees: []
labels: []
created_at: '2016-11-20T01:06:33+00:00'
updated_at: '2016-11-20T13:03:35+00:00'
type: issue
status: closed
closed_at: '2016-11-20T13:03:35+00:00'
---

# Original Description
Despite ~3GiB unallocated memory, buildslave is not releasing ~80% of swap while idle(?) (not currently building anything according to top). As a result, attempting to build kovri with gcc for testing results in OOM.

I can use clang for now, but can we still up the swap (or find another solution)?

# Discussion History
## danrmiller | 2016-11-20T03:28:12+00:00
for now i restarted the buildslave which freed it but we can talk about another solution if it happens again.

@linux64:~$ free
              total        used        free      shared  buff/cache   available
Mem:        3080680      282464     2295032        2100      503184     2623268
Swap:       2097148       17504     2079644


## anonimal | 2016-11-20T13:03:35+00:00
Thanks @danrmiller. I'll reopen if this becomes an issue again.


# Action History
- Created by: anonimal | 2016-11-20T01:06:33+00:00
- Closed at: 2016-11-20T13:03:35+00:00
