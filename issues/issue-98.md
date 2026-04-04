---
title: Transaction history should be sorted descending by height per default
source_url: https://github.com/monero-project/monero-gui/issues/98
author: medusadigital
assignees: []
labels: []
created_at: '2016-11-01T17:35:34+00:00'
updated_at: '2016-11-11T10:41:33+00:00'
type: issue
status: closed
closed_at: '2016-11-11T10:41:33+00:00'
---

# Original Description
Transaction history should be sorted descending by height per default

# Discussion History
## M5M400 | 2016-11-02T08:42:01+00:00
or alternatively fix the 'sort by date' function. currently it only sorts correctly by day, leaving transactions of the same day unsorted

![screenshot from 2016-10-27 15-17-51](https://cloud.githubusercontent.com/assets/22886679/19921885/4f99dcd0-a0e0-11e6-99e3-fe2e3f02c5b1.png)


## taushet | 2016-11-02T21:27:39+00:00
Can the date/time be converted to timestamp and sorted thereafter? This seems like a simple one.


## mbg033 | 2016-11-03T20:29:16+00:00
Fixed here:
https://github.com/monero-project/monero-core/pull/104


## M5M400 | 2016-11-04T09:34:42+00:00
@mbg033 date sort fix confirmed, thx


## medusadigital | 2016-11-06T09:43:31+00:00
initial sorting not implemented yet (which was the reason for this ticket in the first place), issue has to stay open


## mbg033 | 2016-11-06T12:45:14+00:00
Added fix:
https://github.com/monero-project/monero-core/pull/119


# Action History
- Created by: medusadigital | 2016-11-01T17:35:34+00:00
- Closed at: 2016-11-11T10:41:33+00:00
