---
title: Possible error in build instructions in ReadMe.md
source_url: https://github.com/monero-project/monero-gui/issues/83
author: taushet
assignees: []
labels: []
created_at: '2016-10-23T20:35:59+00:00'
updated_at: '2016-10-27T07:14:44+00:00'
type: issue
status: closed
closed_at: '2016-10-27T07:14:44+00:00'
---

# Original Description
Following the instructions to the letter, this happened:

```
minertuxalpha@minertuxalpha-desktop:~/monero-core$ qmake
Project MESSAGE: Building with libunwind
WARNING: DESTDIR: Cannot access directory 'release/bin'
WARNING: langrel: Cannot access directory '/home/minertuxalpha/monero-core/release/bin/translations'
WARNING: langrel: Cannot access directory '/home/minertuxalpha/monero-core/release/bin/translations'
WARNING: langrel: Cannot access directory '/home/minertuxalpha/monero-core/release/bin/translations'
WARNING: langrel: Cannot access directory '/home/minertuxalpha/monero-core/release/bin/translations'
WARNING: langrel: Cannot access directory '/home/minertuxalpha/monero-core/release/bin/translations'
Failure to open file: /home/minertuxalpha/monero-core/Makefile
Unable to generate makefile for: /home/minertuxalpha/monero-core/monero-core.pro
```

However when  `sudo qmake:`

```
minertuxalpha@minertuxalpha-desktop:~/monero-core$ sudo qmake
Project MESSAGE: Building with libunwind
```

...it works fine. Just me, or everyone? 


# Discussion History
## jwinterm | 2016-10-23T20:54:56+00:00
Did you clone the repo as root or something? You should be able to access directories in your home folder.


## taushet | 2016-10-23T20:59:45+00:00
I know it seems strange, but no. I made a new terminal and followed the instructions to the letter. Is there any _downside_ to doing it with sudo?


## taushet | 2016-10-23T21:01:45+00:00
Fresh install of Ubuntu 16.04.1 LTS.


## mbg033 | 2016-10-23T22:49:45+00:00
There's definitely nothing that requires root privileges.


## mbg033 | 2016-10-23T22:51:43+00:00
Also, alternatively you can just invoke build.sh in the fresh (just cloned) project directory


## dternyak | 2016-10-25T18:15:10+00:00
Definitely just you, seems like a permission error. Fix with chmod

On Sunday, October 23, 2016, taushet notifications@github.com wrote:

> Following the instructions to the letter, this happened:
> minertuxalpha@minertuxalpha-desktop:~/monero-core$ qmake
> Project MESSAGE: Building with libunwind
> WARNING: DESTDIR: Cannot access directory 'release/bin'
> WARNING: langrel: Cannot access directory '/home/minertuxalpha/monero-
> core/release/bin/translations'
> WARNING: langrel: Cannot access directory '/home/minertuxalpha/monero-
> core/release/bin/translations'
> WARNING: langrel: Cannot access directory '/home/minertuxalpha/monero-
> core/release/bin/translations'
> WARNING: langrel: Cannot access directory '/home/minertuxalpha/monero-
> core/release/bin/translations'
> WARNING: langrel: Cannot access directory '/home/minertuxalpha/monero-
> core/release/bin/translations'
> Failure to open file: /home/minertuxalpha/monero-core/Makefile
> Unable to generate makefile for: /home/minertuxalpha/monero-core/
> monero-core.pro
> 
> However when sudo qmake:
> 
> minertuxalpha@minertuxalpha-desktop:~/monero-core$ sudo qmake
> Project MESSAGE: Building with libunwind
> 
> ...it works fine. Just me, or everyone?
> 
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> https://github.com/monero-project/monero-core/issues/83, or mute the
> thread
> https://github.com/notifications/unsubscribe-auth/AHf02UWeiK3z9o0MsUeRE5mzcbYJqKzXks5q28UwgaJpZM4KePb5
> .


# Action History
- Created by: taushet | 2016-10-23T20:35:59+00:00
- Closed at: 2016-10-27T07:14:44+00:00
