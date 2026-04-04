---
title: 'Request: build monero-core binary artifacts'
source_url: https://github.com/monero-project/meta/issues/14
author: Jaqueeee
assignees: []
labels: []
created_at: '2016-11-14T19:05:48+00:00'
updated_at: '2017-02-23T17:27:34+00:00'
type: issue
status: closed
closed_at: '2017-02-23T17:27:34+00:00'
---

# Original Description
Windows binaries needs to be built without avx cpu flags to be supported on older machines. 
- static libboost build with -mno-avx and same toolchain as qt5 prebuilt mingw binaries. Inspiration here: https://forum.getmonero.org/5/support/2510/building-monero-v0-9-2-on-win32
Qt 5 mingw install: http://download.qt.io/official_releases/qt/5.6/5.6.2/qt-opensource-windows-x86-mingw492-5.6.2.exe
- libwallet built with same toolchain
- monero-core build

Other platforms can be built with official instructions found in Readme.

# Discussion History
## danrmiller | 2016-11-15T00:13:07+00:00
Once #160 is merged, download links for the .exe for the win32 monero-core builds should work.

I can't retrigger the build for 160 because I think buildbot was down when the original webhook came in.

I'll look at the boost and other special build requirements and give an update.


## anonimal | 2017-01-03T14:18:51+00:00
Is this issue still applicable?

## danrmiller | 2017-01-03T21:35:27+00:00
Download links for the win32 GUI binaries don't include a monero daemon like the downloads for all the other platforms do.

The win32 daemon that buildbot successfully builds does not run properly because msys2 g++ uses POSIX threads and DWARF exception handling on this platform. We can leave this ticket open, or I can start a new issue for setting up an environment using a compiler with Win32 native thread support AND setjmp/longjmp exception handling. 

As far as I'm aware, currently if you don't configure and build this yourself, the only binary available is https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/4.9.3/threads-win32/sjlj/i686-4.9.3-release-win32-sjlj-rt_v4-rev1.7z/download 

@Jaqueeee 

> Windows binaries needs to be built without avx cpu flags to be supported on older machines.

Is this handled by the build.sh script in the monero-core repo?

> static libboost build with -mno-avx and same toolchain as qt5 prebuilt mingw binaries. Inspiration here: https://forum.getmonero.org/5/support/2510/building-monero-v0-9-2-on-win32
Qt 5 mingw install: http://download.qt.io/official_releases/qt/5.6/5.6.2/qt-opensource-windows-x86-mingw492-5.6.2.exe

What is the current suggestion for QT on win32? I think this might have changed since this issue was opened. I know we are currently using a 5.7 build, but I'm not sure the configuration.







## danrmiller | 2017-02-23T15:58:49+00:00
@Jaqueeee are we all set on tester builds for the GUI for now?

## Jaqueeee | 2017-02-23T17:27:32+00:00
@danrmiller yes!

# Action History
- Created by: Jaqueeee | 2016-11-14T19:05:48+00:00
- Closed at: 2017-02-23T17:27:34+00:00
