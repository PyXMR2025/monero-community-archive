---
title: 'Monero fails to compile on OpenBSD 6.4 '
source_url: https://github.com/monero-project/monero/issues/5013
author: somernr
assignees: []
labels: []
created_at: '2018-12-24T20:39:00+00:00'
updated_at: '2019-01-16T20:33:28+00:00'
type: issue
status: closed
closed_at: '2019-01-16T20:33:28+00:00'
---

# Original Description
Cloning from master & following the steps on the official readme. OpenBSD 6.4 is release - fully patched. I get to building monero then it fails:

`machine$ env DEVELOPER_LOCAL_TOOLS=1 BOOST_ROOT=/usr/local make -j 4 release-static`
`No closing parenthesis in archive specification`
`*** Parse error in /home/USER/monero: Error in archive specification: "(, .git/config)" (Makefile:32)`
`*** Parse error: Need an operator in 'endif' (Makefile:34)`
``Bad modifier: /\\ \(\)]|_|g'`/`git branch | grep '\* ' | cut -f2- -d' '| sed -e 's|[:/\\ \(\)]|_|g'`)``
`*** Parse error: Missing dependency operator (Makefile:37)`
``Bad modifier: /\\ \(\)]|_|g'`/`git branch | grep '\* ' | cut -f2- -d' '| sed -e 's|[:/\\ \(\)]|_|g'`)``
``Bad modifier: /\\ \(\)]|_|g'`/`git branch | grep '\* ' | cut -f2- -d' '| sed -e 's|[:/\\ \(\)]|_|g'`)"``
`*** Parse error: Need an operator in 'else' (Makefile:41)*** Parse error: Need an operator in 'endif' (Makefile:45)`

If you want me to post any config files just let me know! Thank you for all you do!

I apologize for the formatting - github doesn't like newlines inside double backticks for some reason.

# Discussion History
## danrmiller | 2018-12-24T20:58:45+00:00
try gmake?

## somernr | 2018-12-24T21:31:18+00:00
Thanks for the response Dan - it seems to be compiling now...so is there something I can post to help you identify why make is failing on OpenBSD?

## somernr | 2018-12-24T22:41:55+00:00
Hmm breaks consistently at 71%:
`[ 64%] Building C object src/blocks/CMakeFiles/blocks.dir/generated_checkpoints.c.o
gmake[3]: Leaving directory '/home/USER/monero/build/OpenBSD/master/release'
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:3:67: error: invalid digit '9' in octal constant
         113, 025, 000, 000, 050, 215, 203, 213, 102, 184, 196, 079, 009, 238, 168, 003,
                                                                  ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:3:72: error: invalid digit '9' in octal constant
         113, 025, 000, 000, 050, 215, 203, 213, 102, 184, 196, 079, 009, 238, 168, 003,
                                                                       ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:4:66: error: invalid digit '8' in octal constant
         133, 243, 135, 144, 190, 023, 199, 073, 220, 144, 210, 088, 004, 047, 040, 251,
                                                                 ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:6:16: error: invalid digit '8' in octal constant
         061, 083, 142, 097, 095, 061, 099, 002, 210, 064, 243, 233, 168, 175, 178, 211,
               ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:6:26: error: invalid digit '9' in octal constant
         061, 083, 142, 097, 095, 061, 099, 002, 210, 064, 243, 233, 168, 175, 178, 211,
                         ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:6:31: error: invalid digit '9' in octal constant
         061, 083, 142, 097, 095, 061, 099, 002, 210, 064, 243, 233, 168, 175, 178, 211,
                              ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:6:41: error: invalid digit '9' in octal constant
         061, 083, 142, 097, 095, 061, 099, 002, 210, 064, 243, 233, 168, 175, 178, 211,
                                        ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:8:27: error: invalid digit '8' in octal constant
         106, 163, 181, 008, 018, 025, 149, 122, 021, 179, 060, 031, 006, 039, 022, 240,
                          ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:8:32: error: invalid digit '8' in octal constant
         106, 163, 181, 008, 018, 025, 149, 122, 021, 179, 060, 031, 006, 039, 022, 240,
                               ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:8:77: error: invalid digit '9' in octal constant
         106, 163, 181, 008, 018, 025, 149, 122, 021, 179, 060, 031, 006, 039, 022, 240,
                                                                            ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:9:21: error: invalid digit '8' in octal constant
         116, 004, 085, 184, 153, 188, 059, 212, 042, 062, 034, 058, 195, 027, 197, 004,
                    ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:9:42: error: invalid digit '9' in octal constant
         116, 004, 085, 184, 153, 188, 059, 212, 042, 062, 034, 058, 195, 027, 197, 004,
                                         ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:9:67: error: invalid digit '8' in octal constant
         116, 004, 085, 184, 153, 188, 059, 212, 042, 062, 034, 058, 195, 027, 197, 004,
                                                                  ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:10:47: error: invalid digit '8' in octal constant
         185, 030, 159, 179, 113, 103, 064, 078, 230, 031, 172, 216, 048, 251, 037, 246,
                                              ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:10:72: error: invalid digit '8' in octal constant
         185, 030, 159, 179, 113, 103, 064, 078, 230, 031, 172, 216, 048, 251, 037, 246,
                                                                       ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:11:27: error: invalid digit '8' in octal constant
         179, 066, 016, 028, 143, 082, 005, 099, 134, 230, 117, 128, 237, 016, 092, 141,
                          ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:11:36: error: invalid digit '8' in octal constant
         179, 066, 016, 028, 143, 082, 005, 099, 134, 230, 117, 128, 237, 016, 092, 141,
                                   ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:11:46: error: invalid digit '9' in octal constant
         179, 066, 016, 028, 143, 082, 005, 099, 134, 230, 117, 128, 237, 016, 092, 141,
                                             ^
/home/USER/monero/build/OpenBSD/master/release/src/blocks/generated_checkpoints.c:11:81: error: invalid digit '9' in octal constant
         179, 066, 016, 028, 143, 082, 005, 099, 134, 230, 117, 128, 237, 016, 092, 141,
                                                                                ^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
20 errors generated.
[ 65%] Built target obj_rpc
gmake[3]: *** [src/blocks/CMakeFiles/blocks.dir/build.make:99: src/blocks/CMakeFiles/blocks.dir/generated_checkpoints.c.o] Error 1
gmake[3]: Leaving directory '/home/USER/monero/build/OpenBSD/master/release'
gmake[2]: *** [CMakeFiles/Makefile2:3513: src/blocks/CMakeFiles/blocks.dir/all] Error 2
gmake[2]: *** Waiting for unfinished jobs....
gmake[3]: Entering directory '/home/USER/monero/build/OpenBSD/master/release'
[ 67%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o
[ 71%] Built target obj_device_trezor
terminating with uncaught exception of type std::bad_alloc: std::bad_alloc
c++: error: unable to execute command: Abort trap (core dumped)
c++: error: clang frontend command failed due to signal (use -v to see invocation)
OpenBSD clang version 6.0.0 (tags/RELEASE_600/final) (based on LLVM 6.0.0)
Target: amd64-unknown-openbsd6.4
Thread model: posix
InstalledDir: /usr/bin
c++: note: diagnostic msg: PLEASE submit a bug report to http://llvm.org/bugs/ and include the crash backtrace, preprocessed source, and associated ru$
c++: note: diagnostic msg:
********************

PLEASE ATTACH THE FOLLOWING FILES TO THE BUG REPORT:
Preprocessed source(s) and associated run script(s) are located at:
c++: note: diagnostic msg: /tmp/wallet2-f2762d.cpp
c++: note: diagnostic msg: /tmp/wallet2-f2762d.sh
c++: note: diagnostic msg:

********************
gmake[3]: *** [src/wallet/CMakeFiles/obj_wallet.dir/build.make:63: src/wallet/CMakeFiles/obj_wallet.dir/wallet2.cpp.o] Error 254
gmake[3]: Leaving directory '/home/USER/monero/build/OpenBSD/master/release'
gmake[2]: *** [CMakeFiles/Makefile2:2364: src/wallet/CMakeFiles/obj_wallet.dir/all] Error 2
gmake[2]: Leaving directory '/home/USER/monero/build/OpenBSD/master/release'
gmake[1]: *** [Makefile:141: all] Error 2
gmake[1]: Leaving directory '/home/USER/monero/build/OpenBSD/master/release'
gmake: *** [Makefile:99: release-static] Error 2`

I don't have malloc.conf linked to any special flags - completely generic install. 

## moneromooo-monero | 2018-12-25T12:35:53+00:00
What is the output of:

> echo "12" | od -v -An -tu1

## somernr | 2018-12-25T17:09:56+00:00
Hi moneromooo!

`machine$ echo "12" | od -v -An -tu1`
`                   049 050 010`

## moneromooo-monero | 2018-12-25T19:08:42+00:00
And:

> echo "12" | od -v -An -tx1

## somernr | 2018-12-25T19:24:04+00:00
`machine$ echo "12" | od -v -An -tx1`
`          31  32  0a`

Thank you for the help - seriously.

## moneromooo-monero | 2018-12-25T19:25:22+00:00
np, https://github.com/monero-project/monero/pull/5016 should fix it.

## somernr | 2018-12-25T19:27:26+00:00
Thank you!

## moneromooo-monero | 2019-01-16T20:27:39+00:00
+resolved

# Action History
- Created by: somernr | 2018-12-24T20:39:00+00:00
- Closed at: 2019-01-16T20:33:28+00:00
