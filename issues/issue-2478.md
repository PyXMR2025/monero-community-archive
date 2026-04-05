---
title: pause on user activity
source_url: https://github.com/xmrig/xmrig/issues/2478
author: Blisk
assignees: []
labels: []
created_at: '2021-07-07T07:16:24+00:00'
updated_at: '2021-07-07T07:20:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When is xmrig started with one user and than login with another user it doesn't pause when user start to use computer.
For example if I login with my username and start xmrig, when I use computer xmrig pause activity.
But after that when I don't use computer for a while and my wife login with her username and password and xmrig still works it doesn't pause activity.

A clear and concise description of what the bug is.



# Discussion History
## SChernykh | 2021-07-07T07:20:15+00:00
Not a bug: https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getlastinputinfo

> This function is useful for input idle detection. However, GetLastInputInfo does not provide system-wide user input information across all running sessions. Rather, GetLastInputInfo provides session-specific user input information for only the session that invoked the function.


# Action History
- Created by: Blisk | 2021-07-07T07:16:24+00:00
