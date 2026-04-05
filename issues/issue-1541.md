---
title: API /1/threads no longer functional
source_url: https://github.com/xmrig/xmrig/issues/1541
author: delawr0190
assignees: []
labels:
- question
created_at: '2020-02-08T04:09:38+00:00'
updated_at: '2020-02-08T21:14:33+00:00'
type: issue
status: closed
closed_at: '2020-02-08T21:14:33+00:00'
---

# Original Description
**Describe the bug**
The API endpoint /1/threads seems to no longer exist.  Was the endpoint changed, or removed?  If removed, would it be possible to get it back?  Otherwise, from the API endpoint, there's no way to differentiate between CPU threads and GPU threads.

**To Reproduce**
Run xmrig with the API enabled.

**Expected behavior**
/1/threads returns threads.

**Required data**
N/A

**Additional context**
N/A


# Discussion History
## xmrig | 2020-02-08T08:46:41+00:00
It replaced to `/2/backends`.
Thank you.

## delawr0190 | 2020-02-08T21:14:33+00:00
I found it.  Thank you for the information.

# Action History
- Created by: delawr0190 | 2020-02-08T04:09:38+00:00
- Closed at: 2020-02-08T21:14:33+00:00
