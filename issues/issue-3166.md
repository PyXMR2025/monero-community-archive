---
title: Typo in readme
source_url: https://github.com/monero-project/monero/issues/3166
author: iamsmooth
assignees: []
labels: []
created_at: '2018-01-21T09:14:33+00:00'
updated_at: '2018-02-04T03:09:02+00:00'
type: issue
status: closed
closed_at: '2018-02-04T03:09:02+00:00'
---

# Original Description
> For this to be worthwhile, the machine should have one core and about 2GB of RAM available per thread

Correct is "... should have more than one core ..."


# Discussion History
## hyc | 2018-01-21T13:19:45+00:00
The previous sentence says "if your machine has several cores" so it's already established that you have more than one core. This sentence is correct - you must have [one core and 2GB of ram] per thread.

## iamsmooth | 2018-01-21T17:13:53+00:00
Ah, it makes sense read that way although not necessarily accurate either.
Hyperthreading often shows gains on compiles (have not tested this particular one), which wouldn't require a full hardware core per thread.


## moneromooo-monero | 2018-01-30T09:44:50+00:00
So... "your machine should have one thread per thread" ? :)

## hyc | 2018-01-30T14:12:44+00:00
When RAM is not a constraint, compiles tend to be I/O bound for reading source/headers and writing tmp files. In that case, hyperthreading can yield a gain on compile times. On a machine with plenty of RAM and effective OS caching I usually run "make -jX" where X is 50% more than available CPU cores, to minimize CPU idle time. On a machine where RAM is tight, there's no advantage.

## iamsmooth | 2018-02-04T03:07:16+00:00
> On a machine with plenty of RAM and effective OS caching I usually run "make -jX" where X is 50% more than available CPU cores

Which is not what the README suggests. Not a big deal though, people can figure out it and Monero compiles tend not to take an inordinately long time on decent hardware at this point anyway.



## iamsmooth | 2018-02-04T03:09:02+00:00
I'm closing this as the original issue of a typo was mistaken. If someone wants to _improve_ the compile instructions in the readme they don't need this issue to do so.

# Action History
- Created by: iamsmooth | 2018-01-21T09:14:33+00:00
- Closed at: 2018-02-04T03:09:02+00:00
