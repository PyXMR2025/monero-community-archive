---
title: Unstable GUI
source_url: https://github.com/monero-project/monero-gui/issues/69
author: DiogenesNakamoto
assignees: []
labels: []
created_at: '2016-10-16T19:59:46+00:00'
updated_at: '2016-11-13T17:59:21+00:00'
type: issue
status: closed
closed_at: '2016-11-13T17:59:21+00:00'
---

# Original Description
I followed the steps for installing the GUI as outlined here, and everything went fine. I was able to create a new wallet, everything looked fine (albeit poor scaling on my 4k display). When I opened the wallet, the GUI was unstable with flickering distortion across all elements as seen here: http://imgur.com/a/6k6O3

I'm running a clean install of Ubuntu 16.04.1 and haven't had any issues with any other applications.


# Discussion History
## Jaqueeee | 2016-10-16T20:15:47+00:00
Thank you for testing!
We haven't seen this behavior before.  Could you please try opening the GUI again when the daemon is fully synced? I'm not sure if it's related, but just to ensure it isn't. 


## medusadigital | 2016-10-16T20:21:02+00:00
@DiogenesNakamoto probably the resolution. can you try change the resolution down and reopen monero-core?


## DiogenesNakamoto | 2016-10-16T20:30:07+00:00
I changed the resolution to 1080p and the scaling back to 1.0. As you can see, the password entry field looks normal, but the app is unchanged.

http://imgur.com/a/WJyZI


## DiogenesNakamoto | 2016-10-16T20:35:42+00:00
I am running two monitors on a Nvidia 980 Ti with Nvidia driver 370.28


## DiogenesNakamoto | 2016-10-16T21:55:39+00:00
deamon is synced. No change. In this image you can see that 2 elements are displayed correctly, the connection status indicator and the seed recovery box.

http://imgur.com/a/GadMe


## medusadigital | 2016-10-17T14:28:14+00:00
im experiencing the same issue on win 7 x64 today. 2560x1440. had no isses with ubuntu on 1440p(but other card)

very strange
![brokenfont](https://cloud.githubusercontent.com/assets/17108301/19441642/a5b136c4-9486-11e6-9fc7-7ce32e171a90.png)

GPU is also Nvidia, gtx 1070, v373.06


## Jaqueeee | 2016-10-17T15:44:05+00:00
Could you try to add this line to the bottom of monero-core.pro, rebuild and see if it makes any difference? @DiogenesNakamoto @medusadigital 

`QT_AUTO_SCREEN_SCALE_FACTOR = 1`


## DiogenesNakamoto | 2016-10-17T18:51:27+00:00
Added. No change.


## Jaqueeee | 2016-10-17T21:07:48+00:00
ok. thanks anyway


## kragol | 2016-10-19T10:25:01+00:00
I have the same problem on Arch Linux (up to date) using the KDE Plasma desktop. GPU is also Nvidia (GTX 970) using the proprietary driver 370.28.


## medusadigital | 2016-10-19T18:14:14+00:00
@kragol what resolution do you got? 


## kragol | 2016-10-20T06:50:49+00:00
@medusadigital my monitor's native resolution 1920x1080.


## dEBRUYNE-1 | 2016-10-26T16:21:42+00:00
This fixed the rendering issue for @medusadigital on Windows 64 bit. This also fixed the "white screen upon startup" in a Windows 10 VM without hardware acceleration. 
1. Download the following file:

64-bit:

https://sourceforge.net/projects/msys2/files/REPOS/MINGW/x86_64/mingw-w64-x86_64-mesa-11.2.0-1-any.pkg.tar.xz/download

32-bit:

https://sourceforge.net/projects/msys2/files/REPOS/MINGW/i686/mingw-w64-i686-mesa-11.2.0-1-any.pkg.tar.xz/download
1. Extract the file. 
2. Place `opengl32.dll` in the same folder as `monero-core` is located. 

Note that this will only work on Windows, but a similar approach should work on Linux and OS X too. 


## medusadigital | 2016-11-01T06:16:57+00:00
Issue is solved on windows, but how does the Linux fix look like?


## kragol | 2016-11-04T11:33:04+00:00
@medusadigital, the closest I could get to your fix on Linux was to replace the proprietary nvidia driver with the open source "nouveau" driver. It did not fix the problem.


## dEBRUYNE-1 | 2016-11-04T12:14:47+00:00
@kragol, could you try the following:

> So, try this if your are on Mac or Linux like OS from terminal:
> 
> export QMLSCENE_DEVICE=softwarecontext
> ./yourAppExecutable

It's from [here](http://lists.qt-project.org/pipermail/interest/2015-October/019486.html). 


## kragol | 2016-11-04T12:25:51+00:00
I guess I answered a bit too quickly...

After updating my system and recompiling everything just now, the problem seems to be gone. I'm not sure exactly what was the culprit. All I know is that I could not run monero-core after the system update because of a change of libboost version (1.61 -> 1.62). Also, I am back to using the nvidia proprietary driver.


## ghost | 2016-11-04T12:38:46+00:00
`boost` 1.62 seems to be incompatible with the current `master` branch. I had the same issue under MacOS, see for example #57 and #101.


## kragol | 2016-11-04T14:37:40+00:00
I can definitely build with `boost` 1.62 on Arch Linux (everything up to date). Maybe I was not clear but what I meant was that monero-core would not run when I updated boost to 1.62 because it was compiled with boost 1.61 at the time. After downloading the current `master` and recompiling with `boost` 1.62 everything seems OK.

Otherwise, I haven't had time to check that all programs in the monero suite work properly but at least they build without errors.


## DiogenesNakamoto | 2016-11-04T22:20:45+00:00
Issue is resolved on my system. I didn't update the system or make any changes to drivers. I simply rebuilt the app and it is displaying properly.


## medusadigital | 2016-11-06T09:16:05+00:00
Great. can finnaly be closed. good job everyone


## dternyak | 2016-11-13T17:54:09+00:00
@DiogenesNakamoto Can you close this issue?


## fluffypony | 2016-11-13T17:59:21+00:00
Closing as fixed


# Action History
- Created by: DiogenesNakamoto | 2016-10-16T19:59:46+00:00
- Closed at: 2016-11-13T17:59:21+00:00
