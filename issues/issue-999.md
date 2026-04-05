---
title: the correct way to stop from the program
source_url: https://github.com/xmrig/xmrig/issues/999
author: Boklazhenko
assignees: []
labels: []
created_at: '2019-03-20T05:16:54+00:00'
updated_at: '2019-08-02T11:56:07+00:00'
type: issue
status: closed
closed_at: '2019-08-02T11:56:07+00:00'
---

# Original Description
Hi, is exist the correct way to stop xmrig using programming? thx

# Discussion History
## timk74 | 2019-04-04T00:38:00+00:00
PostMessage(xmrigwnd, WM_CLOSE, 0, 0);

## Boklazhenko | 2019-04-04T12:13:40+00:00
unfortunately, it doesn't work. xmrig does not process WM_CLOSE


## timk74 | 2019-04-04T23:32:27+00:00
It's working.
`PostMessage(FindWindow('ConsoleWindowClass', 'C:\xmrig\xmrig.exe'), WM_CLOSE, 0, 0);`
Your program should have the same (or higher) security privileges and same user session as xmrig (ie, if xmrig started from the administrator, then your program must also be started from the administrator).

# Action History
- Created by: Boklazhenko | 2019-03-20T05:16:54+00:00
- Closed at: 2019-08-02T11:56:07+00:00
