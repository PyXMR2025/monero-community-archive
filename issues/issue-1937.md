---
title: '"Failed to remove WinRing0 driver, error 1072"'
source_url: https://github.com/xmrig/xmrig/issues/1937
author: MoneroArbo
assignees: []
labels: []
created_at: '2020-11-09T13:04:56+00:00'
updated_at: '2020-11-13T19:18:48+00:00'
type: issue
status: closed
closed_at: '2020-11-13T19:18:48+00:00'
---

# Original Description
**Describe the bug**
An error message when starting xmrig 6.5.1, 6.5.0, and 6.4.0 that says:
```
[2020-11-08 12:45:10.227]  msr      service WinRing0_1_2_0 is already exists

[2020-11-08 12:45:10.259]  msr      failed to remove WinRing0 driver, error 1072

[2020-11-08 12:45:10.260]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
```
Hash rate is correspondingly low (about 12.5 kH on my 3900x instead of 13.5 kH)

**To Reproduce**
Honestly not sure exactly when this started happening to me. I am pretty sure that 6.5.0 was working correctly and the issue *may* have started with 6.5.1. However, it seems to have done something to my machine so that the older binaries don't work either. Even going all the way back to 6.4.0 has no effect. Rebooting has no effect.

I am of course launching the program as an administrator.

**Expected behavior**
For the old WinRing0 service to be removed and for the MSR mod to be successfully applied.

Config file is [here](https://paste.debian.net/1170575/)

While this is being looked at, I'm wondering, does anyone know of a way to remove / reset the WinRing0 service manually?

# Discussion History
## xmrig | 2020-11-09T13:29:05+00:00
Set `"verbose": 1,` in config, with this option miner will show the path to exists service file, it helps figure out what other application installed it.

Error 1072 means `ERROR_SERVICE_MARKED_FOR_DELETE` so likely it will be removed after reboot anyway.

WinRing0 is a very popular driver, many other software use it, in case if it installed and running `service WinRing0_1_2_0 is already exists` it just warning, the miner can reuse exists service, but it is not your case.
Thank you.


## MoneroArbo | 2020-11-09T13:54:01+00:00
Hey and thank you for the response. Just to reiterate, a normal reboot (using the Windows start menu) did NOT fix this.

I did get it working, however, by doing a "full" reboot with the command `shutdown /r /f /t 0`. Windows 10 has two different reboot modes, one "full" and one "hybrid", with hybrid being the default / standard reboot method.

Also, it turns out the other program that uses the service is CTR, a newish and I think popular program for tuning Ryzen CPUs on Windows, so this is something I think other miners may run into. Not sure what happened, since I have been running both programs together successfully for awhile. Maybe the WinRing0 service in xmrig was bumped to a version that's incompatible with the one CTR uses? At any rate, I updated CTR to the latest version and they seem to be getting along again.

No idea what the best solution here is going to be, if any. Maybe if nothing else it would be good to print the path to the existing service file by default?

Regardless, issue is resolved for me for now. Thanks again!

## xmrig | 2020-11-09T14:20:25+00:00
In normal conditions reuse service works fine, but in case if something went wrong, print path without verbose option is a good idea.
We all stuck with the same WinRing0, because it is only one known signed driver with required functionality. 
Thank you.

## xmrig | 2020-11-13T19:18:48+00:00
https://github.com/xmrig/xmrig/releases/tag/v6.5.2 The verbose option no longer required, was a little lazy to rewrite code, so now the path is always printed.
Thank you.


# Action History
- Created by: MoneroArbo | 2020-11-09T13:04:56+00:00
- Closed at: 2020-11-13T19:18:48+00:00
