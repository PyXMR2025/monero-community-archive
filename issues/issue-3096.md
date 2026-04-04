---
title: Build failing on Ubuntu 16.04.3 LTS
source_url: https://github.com/monero-project/monero/issues/3096
author: ghost
assignees: []
labels: []
created_at: '2018-01-10T17:16:41+00:00'
updated_at: '2018-07-08T04:13:32+00:00'
type: issue
status: closed
closed_at: '2018-01-19T05:21:16+00:00'
---

# Original Description
Did a make clean and the build failed. Deleted the entire monero directory, did a fresh git clone, and the build failed. Tried make release and the build still failed.

Log: https://paste.fedoraproject.org/paste/-8jNCsGWqi8mJJ37u75hkw

# Discussion History
## moneromooo-monero | 2018-01-10T20:46:10+00:00
Does this fix it ?

```
diff --git a/cmake/FindReadline.cmake b/cmake/FindReadline.cmake
index 7a11a27..9dd93d7 100644
--- a/cmake/FindReadline.cmake
+++ b/cmake/FindReadline.cmake
@@ -79,3 +79,6 @@ if(HAVE_COMPLETION_FUNCTION AND HAVE_COPY_TEXT)
   set(READLINE_FOUND TRUE)
 endif(HAVE_COMPLETION_FUNCTION AND HAVE_COPY_TEXT)
 
+if(Readline_LIBRARY STREQUAL "NOTFOUND")
+  set(Readline_LIBRARY "")
+endif()
```

## SpliffyMap | 2018-01-10T23:32:33+00:00
For me yesterday approved pull requests failed too with Ubuntu. Also I see it at build.getmonero.org. 

`[ 48%] Linking CXX executable ../../bin/monerod
/usr/bin/ld: ../../external/miniupnpc/libminiupnpc.a(miniupnpc.c.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC
../../external/miniupnpc/libminiupnpc.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
src/daemon/CMakeFiles/daemon.dir/build.make:285: recipe for target 'bin/monerod' failed
make[3]: *** [bin/monerod] Error 1
make[3]: Leaving directory '/home/dredas/Desktop/TESTCRYPTO/monero/build/release'
CMakeFiles/Makefile2:2692: recipe for target 'src/daemon/CMakeFiles/daemon.dir/all' failed
make[2]: *** [src/daemon/CMakeFiles/daemon.dir/all] Error 2`

## ghost | 2018-01-11T04:45:15+00:00
@moneromooo-monero Where do I insert that code? I assume some CMake.txt file? I’ve never done that before. 

## jtgrassie | 2018-01-11T06:15:13+00:00
#3099 fixes this.

## SpliffyMap | 2018-01-11T10:26:03+00:00
Not working for amd64 yet :)
![selection_035](https://user-images.githubusercontent.com/35120072/34820885-94dd6d20-f6ca-11e7-9afc-0f12757d7f98.png)


## moneromooo-monero | 2018-01-11T12:11:30+00:00
>@moneromooo-monero Where do I insert that code? I assume some CMake.txt file? I’ve never done that before.

In the file the patch refers to ? "patch -p1" then paste that in. Or "paste -p1 < filename"



## jtgrassie | 2018-01-11T12:13:11+00:00
@SpliffyMap yes you're right, looks like there are other issues beyond readline here.

## moneromooo-monero | 2018-01-11T15:54:00+00:00
And about the miniupnpc one, https://github.com/monero-project/monero/pull/3103 might fix it.

## SpliffyMap | 2018-01-11T16:37:56+00:00
For me it's good to go :+1: 
![selection_037](https://user-images.githubusercontent.com/35120072/34835780-886c41c2-f6fe-11e7-8041-73681f4a9356.png)


## ghost | 2018-01-11T17:01:19+00:00
PR #3099 fixes it for me

## SpliffyMap | 2018-01-11T17:35:24+00:00
But just tried on my remote node, and got this one. Looks very similar. 
![selection_038](https://user-images.githubusercontent.com/35120072/34838381-85babb5e-f706-11e7-846c-c16485971cb3.png)


## ghost | 2018-01-11T17:44:02+00:00
Oops never mind. Build w/3099 failed for me as well.

## SpliffyMap | 2018-01-11T18:56:05+00:00
Added same code  #3103 to /external/unbound/CMakeLists.txt and it builds on node too now :+1: 

## jtgrassie | 2018-01-11T19:03:49+00:00
@xmr-eric it needs both #3103 & #3099 I think.

## SpliffyMap | 2018-01-11T19:29:53+00:00
I used both too :)

## ghost | 2018-01-11T20:19:29+00:00
Build completed using both PRs. Thanks!

## ghost | 2018-01-11T21:46:17+00:00
I’ll wait for the PRs to get merged before I close this issue

## martinmatak | 2018-01-13T16:59:20+00:00
@xmr-eric How did you build it "using both PRs" ? What does it mean? How do you use that code? I know only how to clone a repository, not sure how to clone pull requests? Do you clone then repository and PR, or just the latter?

I would also like to build it as soon as possible, even if it's still not merged with master branch.

## qskousen | 2018-01-14T00:40:50+00:00
#3103 and #3099 helped my build, but now it fails building unit tests:

<code>
/usr/bin/ld: ../gtest/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
../gtest/libgtest.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
</code>

(I didn't ask it to build tests)

## Cova | 2018-01-14T05:44:33+00:00
I think this is the same issue behind the problem I'm having getting the docker container to build.  Except that #3103 and #3099 don't fix it for me.

> [ 96%] Linking CXX executable ../../bin/monero-blockchain-export
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_filesystem.a(operations.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_filesystem.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
make[3]: *** [bin/monero-blockchain-export] Error 1
src/blockchain_utilities/CMakeFiles/blockchain_export.dir/build.make:179: recipe for target 'bin/monero-blockchain-export' failed
make[3]: Leaving directory '/src/build/release'
CMakeFiles/Makefile2:2894: recipe for target 'src/blockchain_utilities/CMakeFiles/blockchain_export.dir/all' failed
make[2]: *** [src/blockchain_utilities/CMakeFiles/blockchain_export.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
[ 97%] Linking CXX executable ../../bin/monero-blockchain-import
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_filesystem.a(operations.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_filesystem.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
src/blockchain_utilities/CMakeFiles/blockchain_import.dir/build.make:185: recipe for target 'bin/monero-blockchain-import' failed
make[3]: *** [bin/monero-blockchain-import] Error 1
make[3]: Leaving directory '/src/build/release'
CMakeFiles/Makefile2:2842: recipe for target 'src/blockchain_utilities/CMakeFiles/blockchain_import.dir/all' failed
make[2]: *** [src/blockchain_utilities/CMakeFiles/blockchain_import.dir/all] Error 2
[ 97%] Linking CXX executable ../../bin/monerod
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_chrono.a(chrono.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_chrono.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
make[3]: *** [bin/monerod] Error 1
src/daemon/CMakeFiles/daemon.dir/build.make:286: recipe for target 'bin/monerod' failed
make[3]: Leaving directory '/src/build/release'
CMakeFiles/Makefile2:2770: recipe for target 'src/daemon/CMakeFiles/daemon.dir/all' failed
make[2]: *** [src/daemon/CMakeFiles/daemon.dir/all] Error 2
make[3]: Leaving directory '/src/build/release'
[ 97%] Built target obj_wallet
make[2]: Leaving directory '/src/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/src/build/release'
Makefile:68: recipe for target 'release-static' failed
make: *** [release-static] Error 2
The command '/bin/sh -c rm -rf build &&     if [ -z "$NPROC" ];then make -j$(nproc) release-static;else make -j$NPROC release-static;fi' returned a non-zero code: 2

## dEBRUYNE-1 | 2018-01-14T10:16:55+00:00
@Cibale Use these steps:

1. `git clone https://github.com/monero-project/monero.git`

2. `cd monero`

3. `git fetch origin pull/3103/head:3103-mooos-commit`

4. `git fetch origin pull/3099/head:3099-jtgrassies-commit`

5. `git checkout -b <name>`

6. `git merge 3099-jtgrassies-commit 3103-mooos-commit`

7. `make`





## martinmatak | 2018-01-14T13:11:43+00:00
@dEBRUYNE-1 thanks, but unfortunately it doesn't help me. I still can't build it. I receive error when linking CXX executable unit_tests

```
[ 97%] Linking CXX executable unit_tests
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
/usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1203: recipe for target 'tests/unit_tests/unit_tests' failed
make[3]: *** [tests/unit_tests/unit_tests] Error 1
make[3]: Leaving directory '/home/mmatak/dev/monero/build/release'
CMakeFiles/Makefile2:3869: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/all' failed
make[2]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/home/mmatak/dev/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/mmatak/dev/monero/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2
```

## moneromooo-monero | 2018-01-17T01:42:41+00:00
Works for me. What make/cmake command are you running exactly ?

## martinmatak | 2018-01-17T08:24:32+00:00
@moneromooo-monero 

I just type "make".. I am not sure how to give you more details than that.

@danrmiller 

How did you recompile it with -fPIC ? Where to set that flag? 

## moneromooo-monero | 2018-01-17T10:21:26+00:00
Since it seems to be using libgtest from your OS, maybe the easiest is to remove it, so it will use the one bundled with monero, which uses -fPIC.

## martinmatak | 2018-01-17T10:29:00+00:00
@moneromooo-monero 

So I did `sudo apt remove libgtest-dev` , and then tried again with `make`, but I still get the same error..

EDIT: 

Actually, after running `make clean` and then `make`, it worked.

Thanks!

## gldneagl | 2018-02-14T00:57:35+00:00
Thanks Cibale... that worked for me too

## ralphholz | 2018-04-16T05:57:08+00:00
Hi folks - I believe the current instructions for compiling this source code are wrong in README.md. 

As indicated, it works without the libgtest-dev dependency.

Sending through a PR for consideration.

## mmortal03 | 2018-07-08T04:13:32+00:00
@Cova Did you or anyone else find a solution to your problem? I'm getting the same errors as you when trying to do a make release-static on the current master. Removing libgtest-dev and libboost-all-dev from the system doesn't help. I also tried @dEBRUYNE-1 's suggested steps to Cibale, and these also didn't help.

# Action History
- Created by: ghost | 2018-01-10T17:16:41+00:00
- Closed at: 2018-01-19T05:21:16+00:00
