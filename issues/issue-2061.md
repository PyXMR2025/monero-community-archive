---
title: '"WinRing0 failed to start" at startup of XMrig'
source_url: https://github.com/xmrig/xmrig/issues/2061
author: singsonn
assignees: []
labels: []
created_at: '2021-01-25T11:24:42+00:00'
updated_at: '2021-01-25T16:43:45+00:00'
type: issue
status: closed
closed_at: '2021-01-25T16:43:45+00:00'
---

# Original Description
Hello,

I have just installed the latest release of XMrig, and I am getting this error message related to Winring0 :

```
Failed to start WinRing0 driver, error 5
FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
```

![XMrig Error msg](https://i.imgur.com/ElYoO8c.png)

Any idea what can cause this error message? 

I have generated the configuration using the configuration wizard and am running it with Admin privileges.

Also I am running it on my CPU i7-7700k.

As a result, hashrate is quite low (~1500H/s).

Thanks for your help.

# Discussion History
## SChernykh | 2021-01-25T14:54:10+00:00
Error 5 is "access denied". Maybe antivirus is blocking it?

## Lonnegan | 2021-01-25T15:32:51+00:00
And it's not enough to run xmrig in an administrator account! You have to start it by right click / Run as administrator for higher privileges even if you are in an admin account already! This is perhaps also the reason why you cannot use huge pages yet.

## singsonn | 2021-01-25T16:43:45+00:00
Thank you both @SChernykh and @Lonnegan for your replies.

I have made sure that I am running it with Admin rights (right-click, then "Run as administrator"). Also, I don't have an antivirus installed. 

However, this made me think that I have extracted XMrig in a network folder. I have moved it back to my local node, and now I don't have this error message anymore when launching the executable.

Thanks again, the issue is now resolved. 

# Action History
- Created by: singsonn | 2021-01-25T11:24:42+00:00
- Closed at: 2021-01-25T16:43:45+00:00
