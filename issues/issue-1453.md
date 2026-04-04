---
title: Add RPC Golang library under Libraries and helpers
source_url: https://github.com/monero-project/monero-site/issues/1453
author: MarinX
assignees: []
labels:
- 📚 docs
- enhancement
created_at: '2021-02-05T13:43:45+00:00'
updated_at: '2021-02-28T19:28:00+00:00'
type: issue
status: closed
closed_at: '2021-02-28T19:28:00+00:00'
---

# Original Description
Full RPC client written in Go:

[https://github.com/MarinX/monerorpc](https://github.com/MarinX/monerorpc)

Difference from other go libraries:
- Wallet and Daemon client
- Up to date (Wallet RPC version 1.3) (will try to keep it up to date with monero docs)
- Go module support
- Documented
- Written tests (wallet and daemon)

# Discussion History
## erciccione | 2021-02-27T09:06:23+00:00
This is a brand new library with only 2 commits. We don't do any vetting, but would be good to have at least the confirmation (from somebody external to the project) that it works.

## MarinX | 2021-02-28T19:28:00+00:00
@erciccione , understandable.
I will close this issue and re-open again once I have a list of people/projects using this library.
Thank you for the input.

# Action History
- Created by: MarinX | 2021-02-05T13:43:45+00:00
- Closed at: 2021-02-28T19:28:00+00:00
