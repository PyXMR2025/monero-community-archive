---
title: Windows writes the GUI logfile to root of disk
source_url: https://github.com/monero-project/monero-gui/issues/1691
author: sanderfoobar
assignees: []
labels: []
created_at: '2018-10-21T22:08:01+00:00'
updated_at: '2018-12-29T21:02:29+00:00'
type: issue
status: closed
closed_at: '2018-12-29T21:02:29+00:00'
---

# Original Description
[reddit thread](https://www.reddit.com/r/Monero/comments/9q4anr/how_do_i_change_this_log_location_in_the_new_gui/)

```
< rbrunner> I checked with Procmon: It does want to create it in C:\ root, but is denied
```

Following needs investigation:

https://github.com/monero-project/monero-gui/blob/cd46edb23f0764b7bb7ee1171224881554be5d2f/Logger.cpp#L14

It might not be working correctly on Windows.

Loosely related: #1690

# Discussion History
# Action History
- Created by: sanderfoobar | 2018-10-21T22:08:01+00:00
- Closed at: 2018-12-29T21:02:29+00:00
