---
title: Consider adjusting default nblocks-per-sync
source_url: https://github.com/monero-project/monero/issues/654
author: iamsmooth
assignees: []
labels: []
created_at: '2016-02-11T18:57:08+00:00'
updated_at: '2017-11-03T03:20:51+00:00'
type: issue
status: closed
closed_at: '2017-11-03T03:20:51+00:00'
---

# Original Description
In #653 the current default of 1000 is reported to be 10x slower than 10000 on a HD. 

If the default is increased, users with low memory requirements could always set it lower as needed. 

However, we should at least identify the minimum memory requirement for 10000 and ensure it is reasonable mainstream before doing this.

Also, possibly some intermediate value would be a better tradeoff between performance and memory use.


# Discussion History
## ghost | 2016-09-30T00:23:45+00:00
#1129


## luigi1111 | 2016-12-15T18:06:41+00:00
@NanoAkron #1129 is about number of blocks to request from a peer; this issue is about DB sync (the former is 200, the latter is 1000).

## ghost | 2016-12-15T20:00:12+00:00
@luigi1111 What's the right way to proceed here?

## luigi1111 | 2016-12-16T00:16:59+00:00
I guess change it here if there is need https://github.com/monero-project/monero/blob/29735c8f8fda032833924285c2da7ea9b15a77c7/src/cryptonote_core/cryptonote_core.cpp#L328

## Gingeropolous | 2017-11-03T03:11:34+00:00
@iamsmooth , this has been fixed, right? or am I still conflating the two things as mentioned above....

## iamsmooth | 2017-11-03T03:20:51+00:00
This is old enough and was a performance issue. The database code is sufficiently different now that it should just be closed and another specific issue opened if there is an identified problem with the current code.

# Action History
- Created by: iamsmooth | 2016-02-11T18:57:08+00:00
- Closed at: 2017-11-03T03:20:51+00:00
