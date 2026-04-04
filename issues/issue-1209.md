---
title: Streamlining compilation of dependencies for multi-core systems
source_url: https://github.com/monero-project/monero/issues/1209
author: ghost
assignees: []
labels: []
created_at: '2016-10-12T00:21:24+00:00'
updated_at: '2016-11-19T03:15:07+00:00'
type: issue
status: closed
closed_at: '2016-10-15T21:43:33+00:00'
---

# Original Description
I'm getting failed compiles with all values for `make -jx release` with x from 1 - 6 on my 4-core ARMv8 Cortex A53 system. It always seems to start around the 40% mark when it compiles `obj_rpc` or `obj_wallet`.

It only compiles reliably if I run it as a single-threaded process...which leaves me with compile times around 90 minutes and 3 cores just sat there twiddling their thumbs.

Is there any way we could tweak the compilation sequence in the makefiles to improve this? I freely admit this is beyond my abilities.


# Discussion History
## moneromooo-monero | 2016-10-12T08:11:53+00:00
There is a .NOTPARALLEL directive in GNU make. If you find how to shoehorn htat in cmake.


## ghost | 2016-10-12T10:01:00+00:00
Is it possibly due to the ordering of the dependencies within the various makefiles?


## ghost | 2016-10-12T23:15:07+00:00
A reasonable ordering of compilation through analysing the dependency graphs appears to be as follows:

Otshell_utils
Cryptonote_protocol
Mnemonics
+/- blocks
Crypto
Common
Blockchain_db
RingCT
Cryptonote_core
P2P
RPC
Wallet
Simplewallet
Daemonizer
Daemon

Does anyone know how to enforce this with cmake?


## moneromooo-monero | 2016-10-13T22:23:35+00:00
I was assuming the failed compiles were OOM, since you did not say. cmake should (but maybe does not) respect the dependencies. Maybe some of the cmake makefiles don't have the correct dependencies (ie, missing one).


## ghost | 2016-10-14T00:40:41+00:00
I thought it might be OOM as well, but it's even failing with -j2 when I've got a quad-core with 2GB of memory.

Am currently adding dependency lists and seeing what happens. Sadly not much by the look of things so far...

Also can't seem to get .NOTPARALLEL to work within a CMakeLists.txt file :(


## ghost | 2016-10-14T23:37:05+00:00
OK I just can't get this thing to compile with any value of -j, even -j2

Have increased my swapfile to 2GB, have also removed the dependencies and placed them explicitly in `/src/CMakeLists.txt`. Will push a PR so others can test or take a look but not expecting it to be merged.

Is there anyone we could call on to take a look at the build sequence?


## moneromooo-monero | 2016-10-15T15:36:18+00:00
If it's OOM, you'll usually get a "Killed" on the console. Otherwise you get normal GCC output.
If someone knows cmake and sees that, they can try to get it fixed if it's actually broken (ie, if your failures aren't just OOM)


## ghost | 2016-10-15T21:43:33+00:00
Thanks @moneromooo-monero I'll close this now after @iDunk5400's testing.


## radfish | 2016-11-18T23:27:10+00:00
Yes, 2GB is enough only for one thread (from my experience on Odroid U3). If you add swap and run with -j2 or more, it won't be killed by OOM killer, but it will thrash and your compile will take many hours.

There are several source files that are outliers wallet2.cpp and others that take a very large amount of memory and time to compile. I thought breaking apart those files into multiple chunks (to effectively parallelize their compilation) would be worth a try, but @hyc said he investigated this already.


## hyc | 2016-11-19T03:15:07+00:00
Yes, I tried breaking up the source files already. The source files themselves are already small, there's nothing to break up. The problem is all of the boost include files, which bloat up all the compiles. And that problem is the overuse of templates and other boost junk, which prevents us from just compiling small chunks into separate linkable object files - all of that gets recompiled by every reference to the include files. The fact that so many C++ header files in our source tree contain implementations instead of only API definitions makes each actual source file effectively orders of magnitude larger and much slower to compile. It's a pretty horrible layout and would take quite a bit of refactoring to prevent this problem from arising.


# Action History
- Created by: ghost | 2016-10-12T00:21:24+00:00
- Closed at: 2016-10-15T21:43:33+00:00
