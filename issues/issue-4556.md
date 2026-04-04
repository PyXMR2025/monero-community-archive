---
title: unable to make with ubuntu 16.04
source_url: https://github.com/monero-project/monero/issues/4556
author: calidion
assignees: []
labels: []
created_at: '2018-10-11T10:38:22+00:00'
updated_at: '2019-02-01T06:11:13+00:00'
type: issue
status: closed
closed_at: '2019-02-01T06:11:13+00:00'
---

# Original Description

I am following this:

```
  cd monero
  git checkout v0.13.0.0
  make
```




```

mkdir -p build/"Linux/（头指针分离自_v0.13.0.2）"/release
cd build/"Linux/（头指针分离自_v0.13.0.2）"/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../../../.. && make
-- Building without build tag
-- Checking submodules
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled (using easylogging++)
-- Using OpenSSL include dir at /usr/include
-- Could NOT find HIDAPI (missing:  HIDAPI_LIBRARY HIDAPI_INCLUDE_DIR) 
-- Found miniupnpc API version 10
-- Using in-tree miniupnpc
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Could not find HIDAPI
-- Building on x86_64 for native
-- AES support enabled
-- Performing Test _fcf_protection=full_c
-- Performing Test _fcf_protection=full_c - Failed
-- Performing Test _fcf_protection=full_cxx
-- Performing Test _fcf_protection=full_cxx - Failed
-- Using C security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using C++ security hardening flags:  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong
-- Using linker security hardening flags:  -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack
-- Found Boost Version: 105800
-- Found readline library at: /usr
-- Found Git: /usr/bin/git
-- Could NOT find GTest (missing:  GTEST_INCLUDE_DIR) 
-- GTest not found on the system: will use GTest bundled with this source
-- Configuring done
-- Generating done
-- Build files have been written to: /home/eric/origin-monero
make[1]: Entering directory '/home/eric/origin-monero/build/Linux/（头指针分离自_v0.13.0.2）/release'
make[1]: *** 没有指明目标并且找不到 makefile。 停止。
make[1]: Leaving directory '/home/eric/origin-monero/build/Linux/（头指针分离自_v0.13.0.2）/release'
Makefile:85: recipe for target 'release-all' failed
make: *** [release-all] Error 2
```

# Discussion History
## calidion | 2018-10-11T10:42:26+00:00
and `git status`  got a lot changes to the code.

```
eric@eric-MacBookAir:~/origin-monero$ git status
头指针分离自 v0.13.0.2
尚未暂存以备提交的变更：
  （使用 "git add <文件>..." 更新要提交的内容）
  （使用 "git checkout -- <文件>..." 丢弃工作区的改动）
  （提交或丢弃子模组中未跟踪或修改的内容）

	修改：     Doxyfile
	修改：     Makefile
	修改：     external/db_drivers/liblmdb/Makefile
	修改：     external/miniupnp (修改的内容, 未跟踪的内容)

未跟踪的文件:
  （使用 "git add <文件>..." 以包含要提交的内容）

	CTestTestfile.cmake
	Doxygen.extra.css
	contrib/CTestTestfile.cmake
	contrib/Makefile
	contrib/epee/CTestTestfile.cmake
	contrib/epee/Makefile
	contrib/epee/src/CTestTestfile.cmake
	contrib/epee/src/Makefile
	external/CTestTestfile.cmake
	external/Makefile
	external/db_drivers/CTestTestfile.cmake
	external/db_drivers/Makefile
	external/db_drivers/liblmdb/CTestTestfile.cmake
	external/easylogging++/CTestTestfile.cmake
	external/easylogging++/Makefile
	src/CTestTestfile.cmake
	src/Makefile
	src/blockchain_db/CTestTestfile.cmake
	src/blockchain_db/Makefile
	src/blockchain_utilities/CTestTestfile.cmake
	src/blockchain_utilities/Makefile
	src/blocks/CTestTestfile.cmake
	src/blocks/Makefile
	src/checkpoints/CTestTestfile.cmake
	src/checkpoints/Makefile
	src/common/CTestTestfile.cmake
	src/common/Makefile
	src/crypto/CTestTestfile.cmake
	src/crypto/Makefile
	src/cryptonote_basic/CTestTestfile.cmake
	src/cryptonote_basic/Makefile
	src/cryptonote_core/CTestTestfile.cmake
	src/cryptonote_core/Makefile
	src/cryptonote_protocol/CTestTestfile.cmake
	src/cryptonote_protocol/Makefile
	src/daemon/CTestTestfile.cmake
	src/daemon/Makefile
	src/daemonizer/CTestTestfile.cmake
	src/daemonizer/Makefile
	src/device/CTestTestfile.cmake
	src/device/Makefile
	src/gen_multisig/CTestTestfile.cmake
	src/gen_multisig/Makefile
	src/mnemonics/CTestTestfile.cmake
	src/mnemonics/Makefile
	src/multisig/CTestTestfile.cmake
	src/multisig/Makefile
	src/p2p/CTestTestfile.cmake
	src/p2p/Makefile
	src/ringct/CTestTestfile.cmake
	src/ringct/Makefile
	src/rpc/CTestTestfile.cmake
	src/rpc/Makefile
	src/serialization/CTestTestfile.cmake
	src/serialization/Makefile
	src/simplewallet/CTestTestfile.cmake
	src/simplewallet/Makefile
	src/wallet/CTestTestfile.cmake
	src/wallet/Makefile
	src/wallet/api/CTestTestfile.cmake
	src/wallet/api/Makefile
	tests/CTestTestfile.cmake
	tests/Makefile
	tests/core_proxy/CTestTestfile.cmake
	tests/core_proxy/Makefile
	tests/core_tests/CTestTestfile.cmake
	tests/core_tests/Makefile
	tests/crypto/CTestTestfile.cmake
	tests/crypto/Makefile
	tests/difficulty/CTestTestfile.cmake
	tests/difficulty/Makefile
	tests/functional_tests/CTestTestfile.cmake
	tests/functional_tests/Makefile
	tests/fuzz/CTestTestfile.cmake
	tests/fuzz/Makefile
	tests/hash/CTestTestfile.cmake
	tests/hash/Makefile
	tests/net_load_tests/CTestTestfile.cmake
	tests/net_load_tests/Makefile
	tests/performance_tests/CTestTestfile.cmake
	tests/performance_tests/Makefile
	tests/unit_tests/CTestTestfile.cmake
	tests/unit_tests/Makefile

修改尚未加入提交（使用 "git add" 和/或 "git commit -a"）
```

## calidion | 2018-10-11T10:42:54+00:00
generated a lot files out of track.

## calidion | 2018-10-11T10:47:37+00:00
by 
```
cmake .

```
it can compile now.

but still there are a lot untracked files.

## moneromooo-monero | 2018-10-11T11:07:29+00:00
That might work better:

USE_SINGLE_BUILDDIR=1 make

From fresh tree though.

## calidion | 2018-10-11T11:15:47+00:00
@moneromooo-monero 

Thanks.
It's clean now.


## moneromooo-monero | 2018-10-11T12:03:19+00:00
What is the output of:

<pre>
git branch  | grep \* | cat -E
</pre>

Please copy/paste the entire line, whitespace and all, inside a \<pre\> \</pre\> tag pair so github does not mangle it.

## calidion | 2018-10-11T12:07:57+00:00
```
* （头指针分离自 v0.13.0.2）$
```



## moneromooo-monero | 2018-10-11T12:32:24+00:00
Can you paste th output of:

<pre>
ls /home/eric/origin-monero/build/Linux/（头指针分离自_v0.13.0.2）/release
</pre>


## calidion | 2018-10-11T13:29:31+00:00
seems nothing inside it. 

## calidion | 2018-10-11T13:38:56+00:00
```
CMakeFiles
```

## moneromooo-monero | 2018-10-11T14:17:45+00:00
One problem here is the space in the middle of the name. My git replaces with underscores. The Chinese characters are not a problem, it worked here. It appears to be a software version difference, probably (but not certainly) git.

BTW, there's no v0.13.0.0 tag apparently, there's v0.13.0.2 though.


## calidion | 2018-10-11T14:39:25+00:00
`v0.13.0.0` is from README.md
I use v0.13.0.2 instead.
So the README.md should be more accurate and carefully checked.

it would be very hard for us to start compiling if it is not checked but accidentally not working.


## moneromooo-monero | 2018-10-11T14:58:51+00:00
Indeed, things get fixed when things get found :)

## moneromooo-monero | 2018-10-26T09:29:02+00:00
What git version are you using ?

## calidion | 2018-10-26T14:52:00+00:00
```
git version 2.7.4
```

## calidion | 2018-10-27T23:01:29+00:00
```
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../../lib/libgtest.a(gtest-all.cc.o): relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC

```

still not working according to the readme.

## moneromooo-monero | 2018-10-27T23:15:03+00:00
Either install a fPIC libgtest, or remove it so the monero shipped one gets used.

## calidion | 2018-10-29T15:32:37+00:00
@moneromooo-monero any detailed instructions?

## moneromooo-monero | 2018-10-29T15:43:43+00:00
For building, probably in the libgtest README. For removing, in your distro's doc. For ubuntu, apt-get remove libgtest-dev I think.

## calidion | 2018-10-30T23:53:31+00:00
seems not working.

## shubhamudata77 | 2019-01-22T05:16:59+00:00
after make command ...
i am getting this error
mkdir -p build/"Linux/_HEAD_detached_at_v0.13.0.4_"/release
cd build/"Linux/_HEAD_detached_at_v0.13.0.4_"/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../../../.. && make
-- CMake version 3.5.1
-- Building without build tag
-- Checking submodules
CMake Error at CMakeLists.txt:189 (message):
  Submodules not up to date.  Please update with git submodule init && git
  submodule update, or run cmake with -DMANUAL_SUBMODULES=1


-- Configuring incomplete, errors occurred!
See also "/home/shubham/moneronew/build/Linux/_HEAD_detached_at_v0.13.0.4_/release/CMakeFiles/CMakeOutput.log".
Makefile:85: recipe for target 'release-all' failed
make: *** [release-all] Error 1


## xiphon | 2019-01-22T08:52:07+00:00
@shubhamudata77 

Please read the error log line by line, you will find the detailed message and the steps you have to perform to resolve the issue.

## calidion | 2019-02-01T06:11:13+00:00
passed by last stable version.

# Action History
- Created by: calidion | 2018-10-11T10:38:22+00:00
- Closed at: 2019-02-01T06:11:13+00:00
