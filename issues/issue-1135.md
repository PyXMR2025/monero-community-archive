---
title: MSys2 Build Error
source_url: https://github.com/monero-project/monero-gui/issues/1135
author: Haafingar
assignees: []
labels:
- resolved
created_at: '2018-02-24T00:30:15+00:00'
updated_at: '2018-04-02T20:45:24+00:00'
type: issue
status: closed
closed_at: '2018-04-02T20:45:24+00:00'
---

# Original Description
Followed instructions on the README verbatum, not sure if this has something to do with the latest commits to Monero.

```
C:/msys32/mingw32/bin/../lib/gcc/i686-w64-mingw32/7.3.0/../../../../i686-w64-mingw32/bin/ld.exe: cannot find -lwallet_merged
C:/msys32/mingw32/bin/../lib/gcc/i686-w64-mingw32/7.3.0/../../../../i686-w64-mingw32/bin/ld.exe: cannot find -lepee
C:/msys32/mingw32/bin/../lib/gcc/i686-w64-mingw32/7.3.0/../../../../i686-w64-mingw32/bin/ld.exe: cannot find -lunbound
C:/msys32/mingw32/bin/../lib/gcc/i686-w64-mingw32/7.3.0/../../../../i686-w64-mingw32/bin/ld.exe: cannot find -leasylogging
collect2.exe: error: ld returned 1 exit status
make[1]: *** [Makefile.Release:202: release/bin/monero-wallet-gui.exe] Error 1
make[1]: Leaving directory '/home/Rig/monero-gui/build'
make: *** [Makefile:36: release] Error 2
```

Attached is the full output. Running Qt 5.9.4, boost 1.63.0
[Buildlog.txt](https://github.com/monero-project/monero-gui/files/1753642/Buildlog.txt)



# Discussion History
## yagamidev | 2018-02-25T14:03:01+00:00
The problem starts from here `mingw32-make: Leaving directory 'C:/msys32/home/Rig/monero-gui/monero`
Seems like there is an issue with the submodule.
What you can try yo do is trying compiling the Monero submodule first alone if it doesn't compile then the problem is coming from there.

## pazos | 2018-02-25T23:16:59+00:00
I'm in for testing. The error is during linking and seems related to #1139 (osx) and #1078 (linux).

## pazos | 2018-02-26T02:02:49+00:00
The README for windows is broken.We need to merge PRs #828 (update boost) and #1113 (Compile with stack protector).

Qt installation instructions should be simplified.

## danrmiller | 2018-02-26T02:24:56+00:00
The monero daemon portion will not build on windows until this issue https://github.com/monero-project/monero/issues/3296 is resolved.

## sanderfoobar | 2018-03-30T00:23:20+00:00
Since https://github.com/monero-project/monero/issues/3296 was resolved, can this too be resolved?

## danrmiller | 2018-04-02T20:41:49+00:00
Yes.

+resolved

# Action History
- Created by: Haafingar | 2018-02-24T00:30:15+00:00
- Closed at: 2018-04-02T20:45:24+00:00
