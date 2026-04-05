---
title: compiled binary wont run on computers that dont have libmicrohttpd
source_url: https://github.com/xmrig/xmrig/issues/531
author: prismspecs
assignees: []
labels: []
created_at: '2018-04-09T15:55:22+00:00'
updated_at: '2018-04-10T05:04:34+00:00'
type: issue
status: closed
closed_at: '2018-04-10T05:04:34+00:00'
---

# Original Description
on MacOS, get this:

dyld: Library not loaded: /usr/local/opt/libmicrohttpd/lib/libmicrohttpd.12.dylib
  Referenced from: /Applications/Bail Bloc.app/Contents/Resources/app/miner_binaries/./bailbloc_worker
  Reason: image not found

can we package that into the compiled binary somehow?

# Discussion History
## djfinch | 2018-04-09T21:00:35+00:00
You've compiled xmrig with dynamic compile. you can either:
- compile as static (explicitly point cmake to libs)
```
cmake .. -DMHD_LIBRARY=/usr/local/opt/libmicrohttpd/lib/libmicrohttpd.a -DUV_LIBRARY=/usr/local/opt/libuv/lib/libuv.a
```
- copy missing .dylib on place
- install homebrew + deps on that machine
- compile with HTTPD OFF (if you don't need it)
```
-DWITH_HTTPD=OFF
```
Best solution is static recompile. Easiest is copy lib on place but its *****. 

UPDATE: Do not forget to link libuv.a, too.


## prismspecs | 2018-04-09T22:27:24+00:00
oh wow, thank you! this makes sense.

may i ask--it seems as though the Visual Studio Windows instructions account for this, so that should work as is? and then for Linux, I will need to include static versions of both libmicrohttpd and libuv much like what you describe for mac above?

thanks!

## djfinch | 2018-04-09T22:46:18+00:00
You're welcome. In case of Unix-like OS it's OK to use dynamic libraries as long as they are present in the system (native compile, miner is maybe a bit faster) but if you need them "portable" then static compile is mandatory (or provide dynamic libs (*.so) on target system via homebrew on osx or apt/yum/pacman on linux). Linux steps are similar but locations of static libs (.a) are quite different. It's very well described in WIKI pages. Regarding Windows - you need [these](https://github.com/xmrig/xmrig-deps/releases) pre-build static libs or make your own (I wouldn't recommend that as this is very time-consuming process).

## prismspecs | 2018-04-09T23:38:56+00:00
Great, it worked across the board, thank you again!

our project, www.bailbloc.com is very grateful for your help

## djfinch | 2018-04-10T00:35:27+00:00
It's all right. ;) Please close this issue if solved. Thanks!

# Action History
- Created by: prismspecs | 2018-04-09T15:55:22+00:00
- Closed at: 2018-04-10T05:04:34+00:00
