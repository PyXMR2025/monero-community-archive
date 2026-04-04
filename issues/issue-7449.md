---
title: Error in CMakeLists.txt building master
source_url: https://github.com/monero-project/monero/issues/7449
author: woodser
assignees: []
labels: []
created_at: '2021-03-06T16:00:57+00:00'
updated_at: '2021-03-07T03:52:10+00:00'
type: issue
status: closed
closed_at: '2021-03-07T03:52:09+00:00'
---

# Original Description
I'm seeing the following error building master with `make release-static`:

```
CMake Error at CMakeLists.txt:257 (message):
  Submodule 'external/miniupnp' is not up-to-date.  Please update all
  submodules with

  git submodule update --init --force

  or run cmake with -DMANUAL_SUBMODULES=1
```

Running `git submodule update --init --force` gives the error:
```
fatal: remote error: upload-pack: not our ref 544e6fcc73c5ad9af48a8985c94f0f1d742ef2e0
fatal: the remote end hung up unexpectedly
Fetched in submodule path 'external/miniupnp', but it did not contain 544e6fcc73c5ad9af48a8985c94f0f1d742ef2e0. Direct fetching of that commit failed.
```

The build succeeds with -DMANUAL_SUBMODULES=1.

# Discussion History
## moneromooo-monero | 2021-03-06T16:14:48+00:00
git submodule sync

## woodser | 2021-03-07T03:52:09+00:00
Yep that worked!

# Action History
- Created by: woodser | 2021-03-06T16:00:57+00:00
- Closed at: 2021-03-07T03:52:09+00:00
