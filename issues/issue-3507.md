---
title: Vendored unbound not present in the source code tar release
source_url: https://github.com/monero-project/monero/issues/3507
author: CamilleScholtz
assignees: []
labels: []
created_at: '2018-03-27T20:01:44+00:00'
updated_at: '2018-10-26T21:32:59+00:00'
type: issue
status: closed
closed_at: '2018-10-26T21:32:59+00:00'
---

# Original Description
See title :). All other vendored dependencies are, except for unbound.

# Discussion History
## moneromooo-monero | 2018-03-27T20:06:35+00:00
Probably because it got moved to a submodule.
AFAIK, the tarballs are made by github themselves, so unsure how to fix..

## anonimal | 2018-03-27T20:07:40+00:00
@onodera-punpun `$ git clone --recursive`

## CamilleScholtz | 2018-03-27T20:12:39+00:00
@anonimal The thing is when you download the tar release that's not possible.

## anonimal | 2018-03-27T20:32:50+00:00
Then clone.

## moneromooo-monero | 2018-10-26T20:48:08+00:00
Fixed in 0.13.0.4.

+resolved

# Action History
- Created by: CamilleScholtz | 2018-03-27T20:01:44+00:00
- Closed at: 2018-10-26T21:32:59+00:00
