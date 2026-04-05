---
title: No output for -h and -V options if xmrig runs from Administrator (Win 10)
source_url: https://github.com/xmrig/xmrig/issues/407
author: YetAnotherRussian
assignees: []
labels: []
created_at: '2018-02-20T08:45:55+00:00'
updated_at: '2018-11-05T12:53:30+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:53:30+00:00'
---

# Original Description
1) Copy xmrig.exe somewhere
2) Create "start.bat" with the following content:

```
xmrig.exe -h
pause
```
or
```
xmrig.exe -V
pause
```
3) Set compatibility options for xmrig.exe => Run as administrator
4) Launch "start.bat" file

No output for -h and -V options. If you launch with full mining CLI string - new (second) console window is opened from admin, and the console output goes to it (mining works OK).

# Discussion History
# Action History
- Created by: YetAnotherRussian | 2018-02-20T08:45:55+00:00
- Closed at: 2018-11-05T12:53:30+00:00
