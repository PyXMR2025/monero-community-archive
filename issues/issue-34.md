---
title: Compile for 32bit with VS2015
source_url: https://github.com/xmrig/xmrig/issues/34
author: RemezW
assignees: []
labels: []
created_at: '2017-07-10T16:57:34+00:00'
updated_at: '2017-07-19T23:58:22+00:00'
type: issue
status: closed
closed_at: '2017-07-19T23:58:22+00:00'
---

# Original Description
Hi! How i can compile 32bit version of xmrig on 64bit windows machine with VS2015? I successfully compiled 64 bit version, but not understand how do it with 32bit.. In Visual Studio available only x64 Release version. Thank you!

# Discussion History
## xmrig | 2017-07-10T17:03:38+00:00
When run cmake instead of `-G "Visual Studio 14 2015 Win64"` specify `-G "Visual Studio 14 2015"` and path to 32bit libuv.
Please note 32 bit msvc version noticeably slower than gcc version.
Thank you.

## RemezW | 2017-07-10T17:05:58+00:00
Okay! Thank you. I get it.
I correctly understand that the 32-bit version can work on 32-bit systems and 64-bit systems?

## xmrig | 2017-07-10T17:14:42+00:00
Yes.

# Action History
- Created by: RemezW | 2017-07-10T16:57:34+00:00
- Closed at: 2017-07-19T23:58:22+00:00
