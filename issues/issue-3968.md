---
title: Build instructions for submodules
source_url: https://github.com/monero-project/monero/issues/3968
author: CjS77
assignees: []
labels: []
created_at: '2018-06-09T09:30:14+00:00'
updated_at: '2018-10-20T19:32:55+00:00'
type: issue
status: closed
closed_at: '2018-10-20T19:32:55+00:00'
---

# Original Description
This gets me every time the submodule dependencies change, mainly because `git submodule` is pretty unintuitive.

So this doesn't seem to work when compiling an update, though one feels it should:
`cd monero && git submodule init && git submodule update` and then compilation fails.

but

`cd monero && git submodule update --init --recursive`

seems to do the trick.

I would also stick this command in the [Build Instructions](https://github.com/monero-project/monero#build-instructions) rather than the setup instructions because 
1) it's idempotent
2) You need to run it pretty often when compiling a new release.








# Discussion History
## moneromooo-monero | 2018-10-20T19:04:46+00:00
The build system now tells you about it.

+resolved

# Action History
- Created by: CjS77 | 2018-06-09T09:30:14+00:00
- Closed at: 2018-10-20T19:32:55+00:00
