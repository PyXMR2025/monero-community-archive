---
title: Docker build might fail due to low memory
source_url: https://github.com/monero-project/monero/issues/2865
author: emilianbold
assignees: []
labels: []
created_at: '2017-11-26T13:03:40+00:00'
updated_at: '2017-12-26T12:16:24+00:00'
type: issue
status: closed
closed_at: '2017-12-26T12:16:24+00:00'
---

# Original Description
On macOS Docker is configured by default to use only 2GB of RAM.

Because the Dockerfile calls `make -j$(nproc)` it will fail because there won't be enough RAM for so many distributed jobs.

The error does not really make any reference to a low memory situation:

> c++: internal compiler error: Killed (program cc1plus)

One solution I prefer would be to remove the `-j$(nproc)` flag. This would make the build work, although it might be a bit slower.

The least, a warning message should be printed on low-memory docker containers.

# Discussion History
## moneromooo-monero | 2017-11-26T13:28:00+00:00
For the record, "Killed" is the OOM killer.



## moneromooo-monero | 2017-12-26T12:12:45+00:00
+resolved

# Action History
- Created by: emilianbold | 2017-11-26T13:03:40+00:00
- Closed at: 2017-12-26T12:16:24+00:00
