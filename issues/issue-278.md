---
title: HUGE PAGES available, disabled Windows XP sp3
source_url: https://github.com/xmrig/xmrig/issues/278
author: sergneo
assignees: []
labels: []
created_at: '2017-12-20T06:48:57+00:00'
updated_at: '2018-03-14T23:43:29+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:43:29+00:00'
---

# Original Description
The 32-bit version says that huge pages are available but disabled. Tried to add to boot.ini /PAE and(or) the /noexecute=AlwaysOn.
Cleaned the memory memreduct still huge pages disabled. On Windows 7 32 I have achieved the result, everything works successfully. What to do to make them work on Windows XP ? Is this even possible?

CPU "Intel(R) Celeron(R) CPU G1610 @ 2.60GHz"
the memory module 4 GB

# Discussion History
## yuhong | 2017-12-21T03:28:16+00:00
XP don't support it AFAIK.

## sergneo | 2017-12-21T06:06:32+00:00
Win Server 2003 Enterprise 32bit works, checked.

## yuhong | 2017-12-21T06:07:14+00:00
Yea, I think that was the first version of Windows to support it.

## fonix232 | 2017-12-21T11:23:33+00:00
Why would you even use XP today? Okay, I understand it's a low-resource system, but it's full of security holes. Windows Server Core would be a better option IMO.

## sergneo | 2017-12-21T15:46:55+00:00
This can not be considered, because it is not home computers.

## fonix232 | 2017-12-21T16:23:17+00:00
Even worse then. Use a stripped-down version of 7 or 10, or anything but XP. Heck, even a Linux setup would be more secure (albeit more work too). XP has no use nowadays, and apart from embedded, air-gapped systems, it should die out ASAP.

# Action History
- Created by: sergneo | 2017-12-20T06:48:57+00:00
- Closed at: 2018-03-14T23:43:29+00:00
