---
title: Build on aarch64 fails in DaemonClient.cpp
source_url: https://github.com/xmrig/xmrig/issues/2527
author: OTLabs
assignees: []
labels:
- bug
- arm
created_at: '2021-08-09T17:31:32+00:00'
updated_at: '2021-12-19T15:41:27+00:00'
type: issue
status: closed
closed_at: '2021-12-19T15:41:27+00:00'
---

# Original Description
**Describe the bug**
Build on aarch64 fails in DaemonClient.cpp

**To Reproduce**
Build on aarch64

**Expected behavior**
Successful build

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Build on aarch64 fails in DaemonClient.cpp with following error message:
```
297 /builds/otlabs/aports/testing/xmrig/src/xmrig-6.14.0/src/base/net/stratum/DaemonClient.cpp:68:98: error: narrowing conversion of '-1' from 'int' to 'char' [-Wnarrowing]
298   68 | static const char kZMQGreeting[64] = { -1, 0, 0, 0, 0, 0, 0, 0, 0, 127, 3, 0, 'N', 'U', 'L', 'L' };
299      |                                                                                                  ^
```
Full build log is available here:
https://gitlab.alpinelinux.org/otlabs/aports/-/jobs/458898#L297

# Discussion History
## xmrig | 2021-08-09T18:42:09+00:00
Should be [fixed](https://github.com/xmrig/xmrig/commit/f4cdc527b00571150e8521331928c75b44e071f9) in dev branch.
Thank you.

## xmrig | 2021-08-14T19:01:18+00:00
https://github.com/xmrig/xmrig/releases/tag/v6.14.1

## OTLabs | 2021-08-15T15:29:07+00:00
xmrig 6.14.1 biulds fine on aarch64. Thank you!

# Action History
- Created by: OTLabs | 2021-08-09T17:31:32+00:00
- Closed at: 2021-12-19T15:41:27+00:00
