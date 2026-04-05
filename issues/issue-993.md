---
title: Issue with v2.14.1 (32bit)
source_url: https://github.com/xmrig/xmrig/issues/993
author: DeadManWalkingTO
assignees: []
labels: []
created_at: '2019-03-15T14:41:35+00:00'
updated_at: '2020-10-05T14:03:53+00:00'
type: issue
status: closed
closed_at: '2019-03-17T12:27:23+00:00'
---

# Original Description
Windows XP
-------------

![001](https://user-images.githubusercontent.com/34924727/54465767-8939cd80-4785-11e9-8f2c-98b765645547.png)

Entry point error:
GetTicCount64 at KERNEL32.dll

*Compile to 64bit system with MSYS2 (32bit).
*On Windows 7 32bit works fine.
*Original exe (xmrig-2.14.1-gcc-win32.zip) working fine both Windows XP & Windows 7 32bit.

Any idea?

# Discussion History
## DeadManWalkingTO | 2019-03-16T13:30:54+00:00
It's MSYS2 issue after update.
Standard version works fine.

## 0xTract0r | 2020-08-18T07:07:05+00:00
How did you solve it?

## DeadManWalkingTO | 2020-10-05T14:03:53+00:00
> 
> 
> How did you solve it?

1. Backup MSYS2.
2. Download the new MSYS2 Installer.
3. Fresh install.
4. Copy my "user" folder.
5. After that Issue Solved.

# Action History
- Created by: DeadManWalkingTO | 2019-03-15T14:41:35+00:00
- Closed at: 2019-03-17T12:27:23+00:00
