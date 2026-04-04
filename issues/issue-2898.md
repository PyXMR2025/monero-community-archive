---
title: '"Refresh-from-block-height" has value of 0 after entering restore height'
source_url: https://github.com/monero-project/monero/issues/2898
author: dEBRUYNE-1
assignees: []
labels: []
created_at: '2017-12-08T11:08:13+00:00'
updated_at: '2018-01-08T14:48:28+00:00'
type: issue
status: closed
closed_at: '2018-01-08T14:48:28+00:00'
---

# Original Description
Steps to reproduce:

1. Create a new wallet w/ `--generate-from-view key <arg> `

2. Set a restore height (e.g. 1400000) .

3. Once it's fully refreshed, type `set`.

4. It'll show a `refresh-from-block-height` value of 0.

Haven't verified yet, but this probably happens with `--restore-deterministic-wallet` and `--generate-from-keys` too. 


# Discussion History
## snirp | 2017-12-09T23:08:45+00:00
Can verify that this happens with `--generate-from-keys`. Tried to create a view-only wallet and initially gave a blockheight 0. When trying to correct this from the settings, it remained at 0.

## moneromooo-monero | 2017-12-23T11:15:46+00:00
Works for me, did you use master ?

## dEBRUYNE-1 | 2017-12-23T14:43:27+00:00
I used release. I'll try to reproduce later with master. 

## dEBRUYNE-1 | 2018-01-08T14:41:08+00:00
+resolved

# Action History
- Created by: dEBRUYNE-1 | 2017-12-08T11:08:13+00:00
- Closed at: 2018-01-08T14:48:28+00:00
