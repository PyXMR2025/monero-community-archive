---
title: Unable to find entry point GetHostNameW in WS2_32.dll
source_url: https://github.com/xmrig/xmrig/issues/2574
author: jututt
assignees: []
labels:
- bug
created_at: '2021-09-07T11:51:03+00:00'
updated_at: '2021-09-30T04:49:52+00:00'
type: issue
status: closed
closed_at: '2021-09-30T04:49:52+00:00'
---

# Original Description
When trying launching latest 6.15.0 on my Win7 x64 machines, both GCC and MSVC, it crashes and displays error message as per title (roughly translated to english by me).
Previous 6.14.1 works fine

# Discussion History
## xmrig | 2021-09-07T19:14:24+00:00
Seems libuv dropped support for Windows 7 https://github.com/libuv/libuv/issues/3260 
Thank you.


## Spudz76 | 2021-09-07T22:24:51+00:00
Thanks for the heads-up, I will be running Win7 until the end of ESU ([January 10, 2023](https://docs.microsoft.com/en-us/lifecycle/faq/extended-security-updates)) guess the workaround is to not upgrade libuv unless they reverse their terrible decision.

## SChernykh | 2021-09-17T10:06:55+00:00
#2586 

## jututt | 2021-09-30T04:49:52+00:00
closed with 6.15.1

# Action History
- Created by: jututt | 2021-09-07T11:51:03+00:00
- Closed at: 2021-09-30T04:49:52+00:00
