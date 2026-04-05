---
title: Question
source_url: https://github.com/xmrig/xmrig/issues/2558
author: Roki100
assignees: []
labels: []
created_at: '2021-08-25T02:37:04+00:00'
updated_at: '2025-06-16T20:50:42+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:50:42+00:00'
---

# Original Description
Hello, what changes does xmrig make to the os when launching with admin (windows)?
Which ones are permanent and how to avoid them? i would like to mine with MSR (as it seems to not be permanent at all and be reset on reboot by the os itself from what i've read) only in free time for fun, not as a job/big mining thats why i would like to avoid any permanent changes to my os, like huge pages and stuff like that

# Discussion History
## SChernykh | 2021-08-25T07:15:33+00:00
MSR mod works only while xmrig is running. Even if xmrig crashes, reboot will restore MSR to the original state.

## Roki100 | 2021-08-25T14:19:35+00:00
> MSR mod works only while xmrig is running. Even if xmrig crashes, reboot will restore MSR to the original state.

what about huge pages?

## Spudz76 | 2021-08-25T19:58:07+00:00
It uses [standard calls to the security subsystem](https://github.com/xmrig/xmrig/blob/master/src/crypto/common/VirtualMemory_win.cpp#L128) and adds one privilege to the current user account.

Which is all based on the example [from here](https://docs.microsoft.com/en-us/windows/win32/memory/awe-example).

To remove it you would dig into users control panel and find the "Lock pages in memory" element and set it back to default.

## Roki100 | 2021-08-26T16:47:53+00:00
> It uses [standard calls to the security subsystem](https://github.com/xmrig/xmrig/blob/master/src/crypto/common/VirtualMemory_win.cpp#L128) and adds one privilege to the current user account.
> 
> Which is all based on the example [from here](https://docs.microsoft.com/en-us/windows/win32/memory/awe-example).
> 
> To remove it you would dig into users control panel and find the "Lock pages in memory" element and set it back to default.

where more specifically can i find this in control panel?
edit: i just want to specify i use win10 home

## Spudz76 | 2021-08-26T20:19:07+00:00
I don't know someone else has to chime in.  I run Win7.

# Action History
- Created by: Roki100 | 2021-08-25T02:37:04+00:00
- Closed at: 2025-06-16T20:50:42+00:00
