---
title: 'Kovri: win32/64 build/test box logs out of session upon every RDP disconnect'
source_url: https://github.com/monero-project/meta/issues/7
author: anonimal
assignees: []
labels: []
created_at: '2016-11-12T06:18:44+00:00'
updated_at: '2016-12-02T23:02:52+00:00'
type: issue
status: closed
closed_at: '2016-12-02T23:02:52+00:00'
---

# Original Description
Upon every RDP disconnect, all my windows/running programs are closed. This makes run-time testing or building impossible unless I keep an RDP client session open 24x7.

I'm using xfreedrp with `/u:` `/p:` and `/v:` options.

# Discussion History
## luigi1111 | 2016-11-22T22:09:25+00:00
Hmm, can you configure the RDP settings on the host? (I don't know anything about this host)

## danrmiller | 2016-11-22T22:11:11+00:00
I can. Do you have a suggested setting?

## luigi1111 | 2016-11-29T22:01:29+00:00
@anonimal Any thoughts? Normally you can set an idle disconnect time as well as a time to end disconnected sessions. Maybe it makes sense to disable the latter altogether?

[pic](http://www.ryanbelanger.com/wp-content/uploads/2011/11/RDP-auto-logoff-2.png)

## anonimal | 2016-12-01T21:17:17+00:00
@luigi1111 I have no idea, I don't use windows (only for kovri and kovri-related). I'm using linux xfreerdp but even server-side I can't find pic-related or any RDP-related configuration options.

## Jaqueeee | 2016-12-01T21:20:15+00:00
With osx remote-desktop client i get the same behaviour on win32, but on win64 i don't loose my session on i disconnect/reconnect. Are they configured the same @danrmiller?

## danrmiller | 2016-12-02T03:14:48+00:00
Try the win32 host now, it's working for me. @Jaqueeee anonimal is using a different win64 machine than the one we use without the problem. Strangely, that machine with the unwanted logoff behavior is a copy of the vm that does work which you mentioned. I'll try making another copy.

To fix on win32, using gpedit.msc, I changed:

```Set time limit for disconnected sessions```,  
```End session when time limits are reached```, and
```Set time limit for active but idle remote desktop services sessions```

all from enabled to disabled under:
 
```Computer Configuration\Administrative Templates\Windows Components\Remote Desktop Services\Remote Desktop Session Host\Session Time Limits```

And rebooted. For anonimal's win64 machine those were already "undefined" instead of enabled so I set them to disabled and rebooted. It still didn't work, so I set the equivalent under User Configuration to disabled, and also tried setting the RDP-Tcp SecurityLayer to 0 in the registry under HKLM\System\CurrentControlSet\Control\Terminal Server\WinStations.

I'll try making a new copy of the working win64 machine, or give anonimal an account on that machine

## anonimal | 2016-12-02T23:02:52+00:00
Both win32/64 are successful for me now, thanks for the tedious windows work @danrmiller. @Jaqueeee if you still can't connect to win32 I'll re-open the issue.

# Action History
- Created by: anonimal | 2016-11-12T06:18:44+00:00
- Closed at: 2016-12-02T23:02:52+00:00
