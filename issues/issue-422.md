---
title: Serialization.portability_wallet problem
source_url: https://github.com/monero-project/monero-gui/issues/422
author: ghost
assignees: []
labels: []
created_at: '2017-01-20T01:45:17+00:00'
updated_at: '2017-04-03T22:59:55+00:00'
type: issue
status: closed
closed_at: '2017-04-03T22:59:55+00:00'
---

# Original Description
Hi, 

I try to build from [AUR (ArchLinux) package](https://aur.archlinux.org/packages/monero-core-git) and I can not, the error message ...


[  FAILED  ] 4 tests, listed below:
[  FAILED  ] Serialization.portability_wallet
[  FAILED  ] Serialization.portability_outputs
[  FAILED  ] Serialization.portability_unsigned_tx
[  FAILED  ] Serialization.portability_signed_tx


This error occurs  building libwallet release (./build.sh)


Any ideas?


# Discussion History
## moneromooo-monero | 2017-01-21T11:19:11+00:00
This is a monero thing, not a GUI thing.
Does your monero tree have commit b3ca0c62 ? If not, that's likely the reason. If yes, please report this on https://github.com/monero-project/monero instead.

## ghost | 2017-03-29T03:44:28+00:00
Is this still an issue? Or can this thread be closed?

# Action History
- Created by: ghost | 2017-01-20T01:45:17+00:00
- Closed at: 2017-04-03T22:59:55+00:00
