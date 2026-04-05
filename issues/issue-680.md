---
title: Silently ignores missconfigured pools
source_url: https://github.com/xmrig/xmrig/issues/680
author: baryluk
assignees: []
labels:
- bug
created_at: '2018-06-06T21:48:47+00:00'
updated_at: '2020-08-19T01:26:52+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:26:52+00:00'
---

# Original Description
I added a pool into config.json with url that is not supported by xmrig (`startum+ssl://xyz.cc:13433`), and it continued running with other pools from the file, and acted like the first entry never existed.

Please do not do that, and instead report a problem and abort program.


# Discussion History
# Action History
- Created by: baryluk | 2018-06-06T21:48:47+00:00
- Closed at: 2020-08-19T01:26:52+00:00
