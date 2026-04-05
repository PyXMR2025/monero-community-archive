---
title: xmrig-2.6.0-beta2 doesn't care of print-time setting
source_url: https://github.com/xmrig/xmrig/issues/554
author: adem4ik
assignees: []
labels:
- bug
created_at: '2018-04-15T12:40:09+00:00'
updated_at: '2018-04-19T14:17:15+00:00'
type: issue
status: closed
closed_at: '2018-04-19T14:17:14+00:00'
---

# Original Description
**Preconditions:**
xmrig-2.6.0-beta2-gcc-win64.zip or xmrig-2.6.0-beta2-msvc-win64.zip
Windows 10 x64

1) Set `print-time` to non-standard inside config.json, i.e. `"print-time": 30,`
2) Start the miner

**Result:** Speed is printed every 60 seconds
**Expected result:** Speed is printed every 30 seconds

# Discussion History
## xmrig | 2018-04-15T13:00:03+00:00
Fix will be included to next beta3 version.
Thank you.

## xmrig | 2018-04-19T14:17:14+00:00
Changes now in dev branch, if no critical bugs will be found I release beta3 tomorrow.

# Action History
- Created by: adem4ik | 2018-04-15T12:40:09+00:00
- Closed at: 2018-04-19T14:17:14+00:00
