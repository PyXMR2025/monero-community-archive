---
title: Old version in snap
source_url: https://github.com/monero-project/monero/issues/2519
author: unixfox
assignees: []
labels: []
created_at: '2017-09-24T10:18:20+00:00'
updated_at: '2017-12-02T09:48:23+00:00'
type: issue
status: closed
closed_at: '2017-12-02T09:48:23+00:00'
---

# Original Description
The snap package for monero isn't up to date, the version offered by the snap package is 0.10.2:
```
root@vps:~# snap info monero
name:      monero
summary:   "Monero: the secure, private, untraceable cryptocurrency https://getmonero.org"
publisher: vdo
contact:   vdo@greyfaze.net
description: |
  Monero is a private, secure, untraceable, decentralised digital currency.
  You are your bank, you control your funds, and nobody can trace your transfers
  unless you allow them to do so.
  
snap-id:     y81oQQmWpMo320VrXswl3YM65jYqEw30
channels:                 
  stable:    –                 
  candidate: –                 
  beta:      0.10.2-1 (1) 43MB -
  edge:      0.10.2-1 (1) 43MB -
```

@vdo 

# Discussion History
## tostercx | 2017-10-16T12:26:21+00:00
+1, please update the package @vdo - snap's protection of it's files makes it a PITA to update manually.

## vdo | 2017-11-20T21:35:46+00:00
https://github.com/monero-project/monero/pull/2847

## moneromooo-monero | 2017-12-02T09:13:51+00:00
+resolved

# Action History
- Created by: unixfox | 2017-09-24T10:18:20+00:00
- Closed at: 2017-12-02T09:48:23+00:00
