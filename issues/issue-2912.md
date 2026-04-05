---
title: build_deps.sh fails on termux (armv7l) (missing binutils)
source_url: https://github.com/xmrig/xmrig/issues/2912
author: foxsouns
assignees: []
labels: []
created_at: '2022-01-31T17:07:30+00:00'
updated_at: '2022-02-03T05:48:02+00:00'
type: issue
status: closed
closed_at: '2022-02-03T05:47:40+00:00'
---

# Original Description
**Describe the bug**
when running build_deps.sh as described in the wiki, it fails. this seems to be something to do with the "archiver linker", as far as i can gather.

**To Reproduce**
follow the wiki for the advanced build on ubuntu, while on a termux instance, on an android phone with a armv7l processor.

**Expected behavior**
for build_deps.sh to succeed so i can compile the main xmrig

**Required data**
 - log
 ```
~/git/xmrig/scripts $ ./build_deps.sh && cd ../build
--2022-01-31 08:43:38--  https://github.com/libuv/libuv/archive/v1.42.0.tar.gz
Resolving github.com... 140.82.121.3
Connecting to github.com|140.82.121.3|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://codeload.github.com/libuv/libuv/tar.gz/v1.42.0 [following]
--2022-01-31 08:43:39--  https://codeload.github.com/libuv/libuv/tar.gz/v1.42.0
Resolving codeload.github.com... 140.82.121.9
Connecting to codeload.github.com|140.82.121.9|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1293478 (1.2M) [application/x-gzip]
Saving to: ‘v1.42.0.tar.gz’

v1.42.0.tar.gz   100%[=========>]   1.23M   180KB/s    in 7.1s

2022-01-31 08:43:47 (178 KB/s) - ‘v1.42.0.tar.gz’ saved [1293478/1293478]

+ libtoolize --copy
+ aclocal -I m4
+ autoconf
configure.ac:42: warning: The macro `AC_PROG_LIBTOOL' is obsolete.
configure.ac:42: You should run autoupdate.
m4/libtool.m4:99: AC_PROG_LIBTOOL is expanded from...
configure.ac:42: the top level
configure.ac:45: warning: $as_echo is obsolete; use AS_ECHO(["message"]) instead
/home/builder/.termux-build/autoconf/src/lib/m4sugar/m4sh.m4:692: _AS_IF_ELSE is expanded from...
/home/builder/.termux-build/autoconf/src/lib/m4sugar/m4sh.m4:699: AS_IF is expanded from...
/home/builder/.termux-build/autoconf/src/lib/autoconf/general.m4:2249: AC_CACHE_VAL is expanded from...
/home/builder/.termux-build/autoconf/src/lib/autoconf/general.m4:2270: AC_CACHE_CHECK is expanded from...
m4/ax_pthread.m4:88: AX_PTHREAD is expanded from...
configure.ac:45: the top level
+ automake --add-missing --copy
checking for a BSD-compatible install... /data/data/com.termux/files/usr/bin/install -c
checking whether build environment is sane... yes
checking for a race-free mkdir -p... /data/data/com.termux/files/usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking build system type... armv7l-unknown-linux-gnueabi
checking host system type... armv7l-unknown-linux-gnueabi
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables...
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether the compiler supports GNU C... yes
checking whether gcc accepts -g... yes
checking for gcc option to enable C11 features... none needed
checking whether gcc understands -c and -o together... yes
checking whether make supports the include directive... yes (GNU style)
checking dependency style of gcc... gcc3
checking for gcc way to treat warnings as errors... -Werror
checking if gcc supports __attribute__(( visibility("default") ))... yes
checking if gcc supports -fvisibility=hidden... yes
checking if gcc supports -fno-strict-aliasing flag... yes
checking if gcc supports -g flag... yes
checking if gcc supports -std=gnu89 flag... yes
checking if gcc supports -Wall flag... yes
checking if gcc supports -Wextra flag... yes
checking if gcc supports -Wno-long-long flag... yes
checking if gcc supports -Wno-unused-parameter flag... yes
checking if gcc supports -Wstrict-prototypes flag... yes
checking for ar... no
checking for lib... no
checking for link... link -lib
checking the archiver (link -lib) interface... unknown
configure: error: could not determine link -lib interface
~/git/xmrig/scripts $
```
 - Config file has not been touched, and isnt applicable here.
 - OS: termux under android 7.1.1
 ```
~/git/pickaxe/scripts $ uname -a
Linux localhost 3.10.49-gd6e399c #1 SMP PREEMPT Fri Apr 6 12:06:25 CST 2018 armv7l Android
```
**Additional context**
termux is an app that brings the linux userland to android devices. most things compile fine under termux, this looks like either a problem at libuv, or some unknown dependency that i am missing.

# Discussion History
## foxsouns | 2022-02-01T05:30:37+00:00
update: seems like [somebody else ran into this](https://pcre-dev.exim.narkive.com/MlGCsjbS/bug-2103-new-while-configuring-pcre-on-solaris-10-it-throws-error-could-not-determine-link-lib) in a completely different environment (on solaris, of all the unixs! haha) i still need to figure out what ar is, and what provides it. a quick look through debian's package list shows nothing.

## Spudz76 | 2022-02-01T07:36:52+00:00
That's in `binutils` if I remember correctly.  But the other dev packages should have pulled it in...

## foxsouns | 2022-02-01T21:43:55+00:00
@Spudz76 i did NOT have binutils installed. wild. check is valid now, compiles fine. other than maybe adding binutils as a dependency on the website (which, understandably, most people should already have, and that explains why it wasnt mentioned), id feel safe closing this issue.

## Spudz76 | 2022-02-01T22:38:53+00:00
Not sure I thought `build-essential` pulled it in as a dependency but it seems like it might not.  Regular Debian/Ubuntu must just have it by default in the base install while Pi Debians might be "light" and not set up for compiling on-device (many "embedded" systems expect cross-compile from a system with lots of RAM and CPU and disk space, so I wouldn't be surprised that basic compilation tools would be stripped for space).

There is no xmrig build doc for Pi and adding binutils to the Ubuntu doc is unnecessary.

## foxsouns | 2022-02-03T05:47:40+00:00
fair. closing this, but should be kept in mind for any future arm(xx) docs made in the future.

# Action History
- Created by: foxsouns | 2022-01-31T17:07:30+00:00
- Closed at: 2022-02-03T05:47:40+00:00
