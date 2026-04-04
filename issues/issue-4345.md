---
title: 'Device not found in registry: ''Ledger'''
source_url: https://github.com/monero-project/monero-gui/issues/4345
author: mrusme
assignees: []
labels: []
created_at: '2024-08-25T21:31:27+00:00'
updated_at: '2024-08-26T00:43:17+00:00'
type: issue
status: closed
closed_at: '2024-08-26T00:43:17+00:00'
---

# Original Description
Running Gentoo Linux, system is up to date.

I have checked out the tag of the latest release, successfully built the binary and launched it. Upon opening an existing wallet, I see the following output in the terminal:

```
2024-08-25 21:27:41.334	E Device not found in registry: 'Ledger'. Known devices:
2024-08-25 21:27:41.334	E  - default
2024-08-25 21:27:41.335	E Error opening wallet: device not found: Ledger
2024-08-25 21:27:41.346	E Error opening wallet with password:  device not found: Ledger
```

The respective wallet however can be opened by other apps, e.g. the vendor's official manager app. Hence I would rule out any issues with `udev`.

I'd appreciate any hints on how to debug this further.

# Discussion History
## mrusme | 2024-08-26T00:43:17+00:00
The issue was that `dev-libs/hidapi` was not installed, yet `make release` didn't flag it obviously enough for me to notice. Oh well.

# Action History
- Created by: mrusme | 2024-08-25T21:31:27+00:00
- Closed at: 2024-08-26T00:43:17+00:00
