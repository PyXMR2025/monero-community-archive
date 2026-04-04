---
title: The project need CMake 3.5.
source_url: https://github.com/monero-project/monero/issues/4348
author: ViperRu
assignees: []
labels: []
created_at: '2018-09-09T09:03:53+00:00'
updated_at: '2018-09-09T15:34:06+00:00'
type: issue
status: closed
closed_at: '2018-09-09T15:34:06+00:00'
---

# Original Description
According README.md is nessesary the CMake 3.0 or higher. The Ubuntu 14.04 LTS has CMake 3.2.2. The "make release" is terminated with the error:
```
lrelease version 4.8.6
-- Found MiniUPnPc: /usr/include/miniupnpc  
-- Using in-tree miniupnpc
CMake Error at external/miniupnp/miniupnpc/CMakeLists.txt:1 (cmake_minimum_required):
  CMake 3.5 or higher is required.  You are running version 3.2.2


-- Configuring incomplete, errors occurred
```
The project can be building after
```
cd external/miniupnp
git reset HEAD~1
git checkout -- *
cd -`
```

# Discussion History
## moneromooo-monero | 2018-09-09T10:51:29+00:00
Thanks. https://github.com/monero-project/monero/pull/4349

# Action History
- Created by: ViperRu | 2018-09-09T09:03:53+00:00
- Closed at: 2018-09-09T15:34:06+00:00
