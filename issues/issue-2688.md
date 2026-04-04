---
title: undefined references linking zmq
source_url: https://github.com/monero-project/monero/issues/2688
author: danrmiller
assignees: []
labels: []
created_at: '2017-10-20T16:52:36+00:00'
updated_at: '2017-10-21T21:15:27+00:00'
type: issue
status: closed
closed_at: '2017-10-21T21:15:27+00:00'
---

# Original Description
I get several undefined reference errors trying to link monerod with libzmq on at least the below platforms, with the bindings wrapper from: https://github.com/zeromq/cppzmq/blob/master/zmq.hpp

If I need to build libzmq from source to match I will do so, but I opened this issue to see if the OS packages for libzmq can be used:

* debian stretch linux aarch64 - libzmq3-dev 4.2.1-4 
https://build.getmonero.org/builders/monero-static-debian-armv8/builds/2180/steps/compile/logs/stdio

* dragonflybsd v4.6.1 amd64 - libzmq4-4.1.5
https://build.getmonero.org/builders/monero-static-dragonflybsd-amd64/builds/1676/steps/compile/logs/stdio

* freebsd 10.3-RELEASE-p11 amd64 - libzmq4-4.2.2
https://build.getmonero.org/builders/monero-static-freebsd64/builds/2643/steps/compile/logs/stdio



# Discussion History
## moneromooo-monero | 2017-10-20T16:59:48+00:00
Install libpgm. Not sure whether it's meant to be optional or not, I'll ask tewinget.

## moneromooo-monero | 2017-10-20T17:12:43+00:00
Or maybe https://github.com/monero-project/monero/pull/2689 will do it, let's see.

## danrmiller | 2017-10-20T17:18:09+00:00
Thanks. I installed libpgm-dev on the debian aarch64 machine.  
There doesn't seem to be a package for dragonflybsd, will try #2689 
On the freebsd box, it seems it was already installed to /usr/local/lib/libpgm.a but not found:

/usr/local/lib/libpgm.so
/usr/local/lib/libpgm.a
/usr/local/lib/libpgm-5.2.so.0.0.122
/usr/local/lib/libpgm-5.2.so.0


## danrmiller | 2017-10-20T18:12:28+00:00
Thanks, #2689 seems to work, as now on the affected platforms I no longer get undefined references to pgm_* but still there are undefined references to NORM stuff.

https://build.getmonero.org/builders/monero-static-freebsd64/builds/2667/steps/compile/logs/stdio

https://build.getmonero.org/builders/monero-static-dragonflybsd-amd64/builds/1700/steps/compile/logs/stdio

## moneromooo-monero | 2017-10-20T18:37:56+00:00
Do you have a libnorm somewhere ?

## danrmiller | 2017-10-20T18:59:56+00:00
Only the dynamic libs. I'll install static libnorm?

## moneromooo-monero | 2017-10-20T19:48:21+00:00
I'll first make another cmake patch to see if that helps.

## moneromooo-monero | 2017-10-20T19:51:03+00:00
Try #2689 again.

## danrmiller | 2017-10-20T20:26:17+00:00
So it seems to work on freebsd and the new failure is from a separate issue?

https://build.getmonero.org/builders/monero-static-freebsd64/builds/2669/steps/compile/logs/stdio

But on dragonflybsd it has the same error:

https://build.getmonero.org/builders/monero-static-dragonflybsd-amd64/builds/1702/steps/compile/logs/stdio

I wouldn't expect it to matter, but shared libs exist for libnorm on the freebsd box, but nothing on the dragonflybsd machine.

## moneromooo-monero | 2017-10-20T20:32:00+00:00
Oops, some of my custom build flags leaked, fixing...

## moneromooo-monero | 2017-10-20T20:34:36+00:00
The first log looks like something weird happened to wallet2.a, which got corrupted somehow.

## danrmiller | 2017-10-20T21:56:28+00:00
rebuilt, no more waller2.a errors, just libnorm

https://build.getmonero.org/builders/monero-static-dragonflybsd-amd64/builds/1703/steps/compile/logs/stdio

https://build.getmonero.org/builders/monero-static-freebsd64/builds/2670/steps/compile/logs/stdio

## moneromooo-monero | 2017-10-20T22:11:34+00:00
If you run with VERBOSE=1, does the link command line include -lnorm, or a libnorm library file ?

## danrmiller | 2017-10-21T03:16:50+00:00
Nope. 

https://build.getmonero.org/builders/monero-static-freebsd64/builds/2673/steps/compile/logs/stdio



## moneromooo-monero | 2017-10-21T07:49:25+00:00
Please try new #2689 again. I missed a norm.

## danrmiller | 2017-10-21T21:15:27+00:00
Thanks that works

# Action History
- Created by: danrmiller | 2017-10-20T16:52:36+00:00
- Closed at: 2017-10-21T21:15:27+00:00
