---
title: '[Windows] [build.sh release]: MinGW master builds depends on libssp '
source_url: https://github.com/monero-project/monero-gui/issues/1148
author: pazos
assignees: []
labels: []
created_at: '2018-03-03T13:37:53+00:00'
updated_at: '2018-04-03T19:29:05+00:00'
type: issue
status: closed
closed_at: '2018-04-03T19:29:05+00:00'
---

# Original Description
Libssp is the GCC implementation of the Stack Smashing Protector compiler feature and is distributed as a part of MinGW. We just need to add this dll to releases/bin and we're ready to go. AFAIK this is a matter of modifying [windeploy_helper.sh](https://github.com/monero-project/monero-gui/blob/master/windeploy_helper.sh#L26).


# Discussion History
## pazos | 2018-03-20T23:59:01+00:00
fixed in #1190 

## pazos | 2018-04-03T18:31:34+00:00
Oops, #1190 doesn't help. It seems that libssp-0.dll needs to be copied from qt mingw libraries. (C:\Qt\Qtversion\Tools\mingw530_32\i686-w64-mingw32\lib\libssp-0.dll). Not from system mingw libraries. 

@rbrunner7 could you make another PR? 

## rbrunner7 | 2018-04-03T18:44:26+00:00
@pazos: Can you please elaborate what's the problem with the particular version of `libssp-0.dll` that gets copied now that you encountered? Anyway, your filename looks suspiciously like it's a 32bit file - needed is a 64bit file however. You do make a 64bit build, yes?

I tested with the file in question, and it's also the file that gets loaded if you run the GUI exe from a MSYS2 shell, so it is kind of hard for me to believe that file should be the wrong one.

## pazos | 2018-04-03T19:05:54+00:00
I'm building release-static for w32 in a w64 machine, I have the toolchain for 32 bits installed, but I'm using qt from qt.io, not from mingw. So libssp-0.dll isn't found in the mingw libraries and isn't copied during windows-deploy.sh


I think that you can't reproduce this issue unless you'll uninstall mingw-w64-i686-qt5/mingw-w64-x86_64-qt5 and try to build against external libraries.

## rbrunner7 | 2018-04-03T19:17:51+00:00
Well then, I don't think it's a good idea to change the "official", committed file `windeploy_helper.sh` for this particular combination that you use now:

First, "official" Monero has abandoned 32bit builds for the GUI wallet already quite some time ago, with no plans to revive those builds for Lithium Luna. Second, Monero's build environment has just now standardized on Qt as installed by the MSYS2 package, as far as I heard.

To me it seems that you have to cheat a little to get your particular private build running, but without any of those cheats really belonging into the official master source code because your requirements are so special.

## pazos | 2018-04-03T19:29:05+00:00
Yes, you're right!! I think we can modify the instructions for windows to:

1 - use mingw boost instead of build our own
2 - use mingw 64 bits toolchain
3 - add mingw-w64-x86_64-qt5 as part of the toolchain needed to build the gui

Closing this issue

# Action History
- Created by: pazos | 2018-03-03T13:37:53+00:00
- Closed at: 2018-04-03T19:29:05+00:00
