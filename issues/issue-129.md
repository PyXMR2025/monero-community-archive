---
title: 'Kovri: cache/upload PR''d dynamic builds on ARMv7/8 machines'
source_url: https://github.com/monero-project/meta/issues/129
author: anonimal
assignees: []
labels: []
created_at: '2017-10-21T11:17:32+00:00'
updated_at: '2017-10-24T14:27:53+00:00'
type: issue
status: closed
closed_at: '2017-10-24T14:27:47+00:00'
---

# Original Description
Similar to [monero's build](https://build.getmonero.org/downloads/monero-5609b35-linux-armv7.tar.gz), if we can afford the disk space then doing this will save time and help with testing.

# Discussion History
## danrmiller | 2017-10-21T21:08:21+00:00
Wouldn't you want static builds for this? What machines are you going to test these on, what are the shared libs setup on those?

## anonimal | 2017-10-22T06:42:16+00:00
The same machines they are built on. If we don't cache then I end up spending up to X hours re-building to test a PR.

## danrmiller | 2017-10-24T04:30:01+00:00
All set. See https://build.getmonero.org/builders/kovri-all-ubuntu-arm7/builds/504 and https://build.getmonero.org/builders/kovri-all-debian-arm8/builds/515 for examples. 

## anonimal | 2017-10-24T09:27:08+00:00
Thank you @danrmiller !

# Action History
- Created by: anonimal | 2017-10-21T11:17:32+00:00
- Closed at: 2017-10-24T14:27:47+00:00
