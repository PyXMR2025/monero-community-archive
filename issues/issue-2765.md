---
title: '6.16.1 crash on launch '
source_url: https://github.com/xmrig/xmrig/issues/2765
author: DavSingh1980
assignees: []
labels: []
created_at: '2021-12-01T08:52:52+00:00'
updated_at: '2021-12-01T10:41:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Runs fine on my ryzen 5959x win 10 rig on default config file but crashes after  i add my wallet and pool details.

**To Reproduce**
Add your pool and wallet details to config

**Expected behavior**
A clear and concise description of what you expected to happen.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: [e.g. Windows]
 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2021-12-01T10:41:37+00:00
v6.16.1 GCC Windows build is broken, use MSVC build. This is already fixed in the dev branch.

# Action History
- Created by: DavSingh1980 | 2021-12-01T08:52:52+00:00
