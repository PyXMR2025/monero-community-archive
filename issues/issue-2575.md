---
title: Can't compile on OpenBSD
source_url: https://github.com/monero-project/monero/issues/2575
author: B4rb3rouss
assignees: []
labels: []
created_at: '2017-10-03T19:54:08+00:00'
updated_at: '2017-12-03T16:56:23+00:00'
type: issue
status: closed
closed_at: '2017-12-03T16:56:23+00:00'
---

# Original Description
When I try to compile monero on my OpenBSD (-current) machine, it fails.
I followed the README instructions (by the way, `make release-static-64` no longer exists apparently). I put zmq.hpp (found [here](https://raw.githubusercontent.com/zeromq/cppzmq/master/zmq.hpp) in `/usr/local/include`.

Here is the shown error : 

```
 env CC=egcc CXX=eg++ CPP=ecpp DEVELOPER_LOCAL_TOOLS=1 BOOST_ROOT=/usr/local/lib/ make release-static
mkdir -p build/release
cd build/release && cmake -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- Building without build tag
-- Found: env DEVELOPER_LOCAL_TOOLS = 1
-- BOOST_IGNORE_SYSTEM_PATHS defaults to ON
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled
-- Found miniupnpc API version 10
-- Using miniupnpc from local source tree for static build
-- Looking for libunbound
-- Using 64-bit LMDB from source tree
-- Building on amd64 for x86-64
-- AES support enabled
-- Found Boost Version: 105800
-- Could not find GNU readline library so building without readline support
-- Found Git: /usr/local/bin/git
Doxygen: graphviz not found - graphs disabled
-- Could NOT find Doxygen (missing: DOXYGEN_EXECUTABLE)
-- Configuring done
-- Generating done
-- Build files have been written to: /home/xavier/geek/gitreps/monero/build/release
-- You are currently on commit a2041c98
-- The most recent tag was at c9063c0b
-- You are ahead of or behind a tagged release
[  0%] Built target genversion
[  4%] Built target libminiupnpc-static
[ 28%] Built target unbound
[ 29%] Built target lmdb
[ 29%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
/home/xavier/geek/gitreps/monero/external/easylogging++/easylogging++.cc: In static member function 'static std::string el::base::utils::OS::getEnvironmentVariable(const char*, const char*, const char*)':
/home/xavier/geek/gitreps/monero/external/easylogging++/easylogging++.cc:1037:8: error: 'val' was not declared in this scope
   if ((val == nullptr) || ((strcmp(val, "") == 0))) {
        ^
/home/xavier/geek/gitreps/monero/external/easylogging++/easylogging++.cc:1051:22: error: 'val' was not declared in this scope
   return std::string(val);
                      ^
*** Error 1 in build/release (external/easylogging++/CMakeFiles/easylogging.dir/build.make:63 'external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o')
*** Error 1 in build/release (CMakeFiles/Makefile2:333 'external/easylogging++/CMakeFiles/easylogging.dir/all')
*** Error 1 in build/release (Makefile:141 'all')
*** Error 1 in /home/xavier/geek/gitreps/monero (Makefile:67 'release-static')

```

Any advice?
I found binaries for freeBSD and DragonlyBSD, it might be possible to use monero on OpenBSD.

# Discussion History
## moneromooo-monero | 2017-10-03T20:22:19+00:00
Is your compiler/system headers defining \_\_FreeBSD\_\_ ?

## B4rb3rouss | 2017-10-04T05:25:56+00:00
I don't think so, I use OpenBSD.

## moneromooo-monero | 2017-10-04T09:25:33+00:00
Oh I'm sorry, I am an idiot and misread :D

## moneromooo-monero | 2017-10-04T09:28:26+00:00
See https://github.com/monero-project/monero/pull/2249/files

The author doesn't have the time to make it fully work apparently, but maybe it helps. Testing report and fixes if it does not work out of the box would be appreciated :)

## B4rb3rouss | 2017-10-04T19:16:30+00:00
Thank you, I'll try this and let you know. :)

## B4rb3rouss | 2017-10-04T19:20:00+00:00
Compilation still fails, but not the same way : 
```

[ 29%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
In file included from /home/xavier/geek/gitreps/monero/external/easylogging++/easylogging++.cc:17:0:
/home/xavier/geek/gitreps/monero/external/easylogging++/easylogging++.h:210:11: warning:
#warning "Stack trace not available for this compiler"; [-Wcpp]
 #         warning "Stack trace not available for this compiler";
           ^
/home/xavier/geek/gitreps/monero/external/easylogging++/easylogging++.cc: In member function 'void el::base::VRegistry::setCategories(const char*, bool)':
/home/xavier/geek/gitreps/monero/external/easylogging++/easylogging++.cc:1966:5: error: 'm_categoriesString' was not declared in this scope
     m_categoriesString.clear();
     ^
/home/xavier/geek/gitreps/monero/external/easylogging++/easylogging++.cc:1968:8: error: 'm_categoriesString' was not declared in this scope
   if (!m_categoriesString.empty())
        ^
/home/xavier/geek/gitreps/monero/external/easylogging++/easylogging++.cc:1970:3: error: 'm_categoriesString' was not declared in this scope
   m_categoriesString += categories;
   ^
/home/xavier/geek/gitreps/monero/external/easylogging++/easylogging++.cc: At global scope:
/home/xavier/geek/gitreps/monero/external/easylogging++/easylogging++.cc:2009:38: error:
no 'std::string el::base::VRegistry::getCategories()' member function declared in class 'el::base::VRegistry'
 std::string VRegistry::getCategories() {
                                      ^
/home/xavier/geek/gitreps/monero/external/easylogging++/easylogging++.cc:3086:36: error:
no 'std::string el::Loggers::getCategories()' member function declared in class 'el::Loggers'
 std::string Loggers::getCategories() {
                                    ^
*** Error 1 in build/release (external/easylogging++/CMakeFiles/easylogging.dir/build.make:63 'external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o')
*** Error 1 in build/release (CMakeFiles/Makefile2:333 'external/easylogging++/CMakeFiles/easylogging.dir/all')
*** Error 1 in build/release (Makefile:141 'all')
*** Error 1 in /home/xavier/geek/gitreps/monero (Makefile:67 'release-static')

```

## moneromooo-monero | 2017-10-04T19:34:27+00:00
Do you have an easylogging++.h file installed somewhere (apart from the one monero ships) ?

## B4rb3rouss | 2017-10-05T16:44:05+00:00
No, this file isn't anywhere else.

## danrmiller | 2017-10-05T17:11:55+00:00
This is what I get when I try to build on openbsd:  
https://build.getmonero.org/builders/monero-static-openbsd-amd64/builds/537/steps/compile/logs/stdio

```
gmake[3]: Entering directory '/home/buildbot/slave/monero-static-openbsd-amd64/build/build/release'
[ 45%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
In file included from /home/buildbot/slave/monero-static-openbsd-amd64/build/external/easylogging++/easylogging++.cc:17:
/home/buildbot/slave/monero-static-openbsd-amd64/build/external/easylogging++/easylogging++.h:356:13: fatal error: 'execinfo.h' file not found
#   include <execinfo.h>
            ^
1 error generated.
```

Also see these for reference:

https://github.com/monero-project/monero/pull/2235

https://github.com/monero-project/monero/pull/2249




## moneromooo-monero | 2017-10-05T17:50:40+00:00
It really seems you have the wrong header... 
Can you check in external/easylogging++/easylogging++.h, search for m_filenameCommonPrefix, there should be three hits, the last one in a set of variable declarations. Can you paste the entirety of those ? There should be half a dozen or so. From the "private" line to the "};" line.


## B4rb3rouss | 2017-10-05T19:15:37+00:00
Here you go : https://framabin.org/?adfce01bc5faf107#tZD1vFcq2lCVo3HXiGuikC0Mcr04cmXBXjZPD1fHIgY=
(I don't have enough knowledge to check it myself)

## moneromooo-monero | 2017-10-05T19:26:25+00:00
This requires javascript. Can you try gist.github.com, or fpaste.org, or pastebin.mozilla.org ?

## B4rb3rouss | 2017-10-06T06:26:35+00:00
Here : https://gist.github.com/B4rb3rouss/cc1f864c122171d14e30fbb03b260369

## moneromooo-monero | 2017-10-06T07:45:24+00:00
This is not the current version of the file in the monero tree. Find what you've done to end up with an old version which does not correspond to the cc file, and fix this. If you did not make local changes to the tree, then "git reset --hard origin/master" ought to work (this will summarily destroy any change to the local repository).

## B4rb3rouss | 2017-10-06T15:31:42+00:00
Well, I didn't change anything ;/
A hard reset gave me the same issue, so I cloned again the repo from scratch. The compilation goes a little further : 

```[ 43%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/mdb.c.o
[ 44%] Building C object external/db_drivers/liblmdb/CMakeFiles/lmdb.dir/midl.c.o
[ 44%] Linking C static library liblmdb.a
gmake[3] : on quitte le répertoire « /home/xavier/geek/gitreps/monero/build/release »
[ 44%] Built target lmdb
gmake[3] : on entre dans le répertoire « /home/xavier/geek/gitreps/monero/build/release »
Scanning dependencies of target easylogging
gmake[3] : on quitte le répertoire « /home/xavier/geek/gitreps/monero/build/release »
gmake[3] : on entre dans le répertoire « /home/xavier/geek/gitreps/monero/build/release »
[ 45%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
/home/xavier/geek/gitreps/monero/external/easylogging++/easylogging++.cc:717:1: warning: control may reach end of non-void function [-Wreturn-type]
}
^
/home/xavier/geek/gitreps/monero/external/easylogging++/easylogging++.cc:1037:8: error: use of undeclared identifier 'val'
  if ((val == nullptr) || ((strcmp(val, "") == 0))) {
       ^
/home/xavier/geek/gitreps/monero/external/easylogging++/easylogging++.cc:1037:36: error: use of undeclared identifier 'val'
  if ((val == nullptr) || ((strcmp(val, "") == 0))) {
                                   ^
/home/xavier/geek/gitreps/monero/external/easylogging++/easylogging++.cc:1051:22: error: use of undeclared identifier 'val'
  return std::string(val);
                     ^
1 warning and 3 errors generated.
gmake[3]: *** [external/easylogging++/CMakeFiles/easylogging.dir/build.make:63: external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o] Error 1
gmake[3] : on quitte le répertoire « /home/xavier/geek/gitreps/monero/build/release »
gmake[2]: *** [CMakeFiles/Makefile2:333: external/easylogging++/CMakeFiles/easylogging.dir/all] Error 2
gmake[2] : on quitte le répertoire « /home/xavier/geek/gitreps/monero/build/release »
gmake[1]: *** [Makefile:141: all] Error 2
gmake[1] : on quitte le répertoire « /home/xavier/geek/gitreps/monero/build/release »
gmake: *** [Makefile:67: release-static] Error 2
```

still easylogging++ is problematic.

## moneromooo-monero | 2017-10-06T17:39:51+00:00
That's the problem that's fixed by the patch I linked you to earlier. I guess that's where the problem comes from, you copied the file from that tree ? If so, don't do that, do this: git cherry-pick X (with X being the branch you've got the patch on).


## B4rb3rouss | 2017-10-06T19:17:55+00:00
Yes, I copied the file you gave me.
If I try, to cherry-pick, git complains. I don't seem to use it correctly, sorry :/ 
```
$ git cherry-pick 2249
fatal: bad revision '2249'

git cherry-pick 617e0a3632b413f80da28a4eb779788d74b2da8b
fatal: bad object 617e0a3632b413f80da28a4eb779788d74b2da8b

```


## moneromooo-monero | 2017-10-06T19:39:19+00:00
I've merged this to current master: https://github.com/moneromooo-monero/bitmonero/tree/openbsd
You can use that branch as is to test.

## B4rb3rouss | 2017-10-06T19:52:57+00:00
Thank you a lot.
The compilation goes a little further. The last error seems to be related to a template : https://gist.github.com/B4rb3rouss/0d12d3587e05a5dfa9dacee533530623

## vtnerd | 2017-10-06T23:03:56+00:00
@B4rb3rouss This is probably either an older unsupported compiler (gcc 4.5 or older) OR boost configuration is not working on this OpenBSD alternate compiler. One quick test:
```c++
#include <boost/config.hpp>
#include <iostream>
int main () {
    std::cout << BOOST_GCC_VERSION << std::endl;
    return 0;
}
```
See what that outputs or if it fails to compile.

## B4rb3rouss | 2017-10-07T06:21:41+00:00
It fails to compile. On my OpenBSD -current, it's gcc 4.9.4.

```
test.cpp:2:28: error: boost/config.hpp: No such file or directory
test.cpp: In function 'int main()':
test.cpp:5: error: 'BOOST_GCC_VERSION' was not declared in this scope

```

## vtnerd | 2017-10-08T12:41:02+00:00
Ok, this doesn't help because `boost/config.hpp` should be present. Could you `-I /PATH_TO_BOOST` when compiling that test file? The minimum version of Boost has to be present or the cmake step would have failed.

## B4rb3rouss | 2017-10-08T18:07:08+00:00
Sorry, I'm not used to such issues.
Here what I have now  with`cpp -I /usr/local/include test.cpp` : https://gist.github.com/B4rb3rouss/ee85829a1246d55a86878c6f64dc5bbb

## iDunk5400 | 2017-10-09T00:00:22+00:00
`g++ -I /usr/local/include test.cpp -o test`

## B4rb3rouss | 2017-10-09T05:20:39+00:00
```
g++ -I /usr/local/include test.cpp -o test
test.cpp: In function 'int main()':
test.cpp:5: error: 'BOOST_GCC_VERSION' was not declared in this scope
```


## vtnerd | 2017-10-09T14:10:00+00:00
The compiler does not appear to identify itself as GCC, and therefore the Boost config disables `constexpr` since its support is unknown. The labeling of `constexpr boost::string_ref foo{...};` is problematic since the constructor within boost has its `constexpr` label stripped.

Before applying a fix I would like to know - what _actual_ version of GCC is this? My understanding is that the BSDs had to stick with an older GCC due to GPLv3 licensing issues. Was this supplemental compiler allowed to be distributed because none of the default packages were compiled with it? And if that is the case, why change the self identification string? Are there substantial changes to this compiler? I cannot find much information about this through web searches, guess I have not found the correct combination of words yet.

## vtnerd | 2017-10-09T14:10:41+00:00
OR wait, is this a version of clang actually?

EDIT: But original post says `egcc`, so weird.

## B4rb3rouss | 2017-10-10T19:27:07+00:00
Sorry, I'm not english and not a c++ dev, so I'm not sure to know how to give you proof of GCC version.

Can you please tell me how to test what you need (commands required), I'll put the output here.
Thank you for your interest.

## moneromooo-monero | 2017-10-10T19:31:08+00:00
Try:
egcc --version
eg++ --version


## moneromooo-monero | 2017-10-10T19:32:06+00:00
Oh, wait, you used CC=egcc, but I'm not sure cmake uses those, they're canonical autofoo vars...

OK, that seems to be accepted, so I'm updating my comment above,

## B4rb3rouss | 2017-10-11T06:09:06+00:00
Ok, here are the version on my system : 
```
$ egcc --version
egcc (GCC) 4.9.4
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

```
$ eg++ --version
eg++ (GCC) 4.9.4
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

```

## hucste | 2017-10-16T19:45:00+00:00
@B4rb3rouss : please, rename your first post, with the word '-current'. 
I'm going to attempt with OpenBSD 6.2 stable amd64 ;)

## ston1th | 2017-10-22T10:00:41+00:00
Hello guys,

im currently trying to build `monerod` latest release version v0.11.0.0 with `easylogging++` patched like advised above on OpenBSD 6.2 -stable.

The compiling works fine, but when it comes to linking `libunbound`, there seems to be problem with `libressl`.
The problem occours when linking the three functions `DSA_set0_key`, `DSA_set0_pqg` and `RSA_set0_key`, which are not provided by `libressl`:
```
../../external/unbound/libunbound.a(keyraw.c.o): In function `sldns_key_buf2dsa_raw':
keyraw.c:(.text+0x1da): undefined reference to `DSA_set0_pqg'
keyraw.c:(.text+0x1f0): undefined reference to `DSA_set0_key'
../../external/unbound/libunbound.a(keyraw.c.o): In function `sldns_key_buf2rsa_raw':
keyraw.c:(.text+0x33d): undefined reference to `RSA_set0_key'
collect2: error: ld returned 1 exit status
*** Error 1 in . (src/daemon/CMakeFiles/daemon.dir/build.make:266 'bin/monerod')
*** Error 1 in . (CMakeFiles/Makefile2:1895 'src/daemon/CMakeFiles/daemon.dir/all')
*** Error 1 in . (CMakeFiles/Makefile2:1907 'src/daemon/CMakeFiles/daemon.dir/rule')
*** Error 1 in /tmp/monero-0.11.0.0/build/release (Makefile:591 'daemon')
```

I think the cause is a missing `#define HAVE_LIBRESSL` in here [keyraw.c#L227](https://github.com/monero-project/monero/blob/master/external/unbound/sldns/keyraw.c#L227) and here [keyraw.c#L305](https://github.com/monero-project/monero/blob/master/external/unbound/sldns/keyraw.c#L305), which leads to going into the `#else` and using these functions.
Adding a `#define HAVE_LIBRESSL` to the top of `keyraw.c` seems to fix this, unfortunately I have no idea why this define is missing in the first place.

~~Running this build seems not to be able to sync with the network~~ (fixed in #2699).

## moneromooo-monero | 2017-10-22T10:50:34+00:00
The original configure.ac greps opensslv.h for VERSION_TEXT and matches LibreSSL. It's not obvious how to do this with cmake though.

## vtnerd | 2017-10-22T12:54:45+00:00
Ok, the OpenBSD 6.2 release notes indicate that the compiler switched to clang on x86 and amd64 for the base system compiler. So monero will compile on this system because of that change. It looks like the OpenBSD project typically supports a release for roughly 1 year. So either we need to declare no support for OpenBSD versions older than 6.2, or I need to find a fix for this compiler detection issue on OpenBSD 6.1 and earlier.

@moneromooo-monero @fluffypony @danrmiller @hyc thoughts?



## ston1th | 2017-10-22T13:08:47+00:00
I added this to the unbound CMakeLists.txt:

```
if ("${CMAKE_SYSTEM_NAME}" MATCHES OpenBSD)
  set(HAVE_LIBRESSL 1)
endif ()
```
Now the compilation fails here:
```
[ 22%] Building C object external/unbound/CMakeFiles/unbound.dir/services/cache/dns.c.o
In file included from /tmp/monero-0.11.0.0/external/unbound/services/cache/dns.c:41:0:
/tmp/monero-0.11.0.0/build/release/external/unbound/config.h:1123:30: error: operator '!' has no right operand
 #  if !HAVE_DECL_REALLOCARRAY
                              ^
*** Error 1 in . (external/unbound/CMakeFiles/unbound.dir/build.make:63 'external/unbound/CMakeFiles/unbound.dir/services/cache/dns.c.o': cd...)
*** Error 1 in . (CMakeFiles/Makefile2:205 'external/unbound/CMakeFiles/unbound.dir/all')
*** Error 1 in . (CMakeFiles/Makefile2:1907 'src/daemon/CMakeFiles/daemon.dir/rule')
*** Error 1 in /tmp/monero-0.11.0.0/build/release (Makefile:591 'daemon')
```

But at least we are entering the `#ifdef HAVE_LIBRESSL` here: config.h:1110
```
#ifdef HAVE_LIBRESSL
#  if !HAVE_DECL_STRLCPY
size_t strlcpy(char *dst, const char *src, size_t siz);
#  endif
#  if !HAVE_DECL_STRLCAT
size_t strlcat(char *dst, const char *src, size_t siz);
#  endif
#  if !HAVE_DECL_ARC4RANDOM && defined(HAVE_ARC4RANDOM)
uint32_t arc4random(void);
#  endif
#  if !HAVE_DECL_ARC4RANDOM_UNIFORM && defined(HAVE_ARC4RANDOM_UNIFORM)
uint32_t arc4random_uniform(uint32_t upper_bound);
#  endif
#  if !HAVE_DECL_REALLOCARRAY
void *reallocarray(void *ptr, size_t nmemb, size_t size);
#  endif
#endif /* HAVE_LIBRESSL */
```

Unfortunately I don't understand the error there..

## moneromooo-monero | 2017-10-22T13:22:16+00:00
That should likely be #ifndef HAVE_DECL_REALLOCARRAY, since those are usually either defined (typically to 1), or undefined. That, or that project defines to 0 instead of undefining, which is uncommon but possible. But since we use cmake instead of autofoo, we get all this brokenness.

## moneromooo-monero | 2017-10-23T14:36:49+00:00
The comments in config.h.in say to define to 0 in the negative case. However, examples found on the web use #ifdef. The documentation does not say. So... Replace with #ifndef HAVE_DECL_REALLOCARRAY.

## ston1th | 2017-10-23T14:47:07+00:00
I found another solution with just editing the CMakeLists.txt.
This seems to be more compatible if one want's to link against libressl.

EDIT:
```
# determine if we have libressl
check_symbol_exists(LIBRESSL_VERSION_TEXT "openssl/opensslv.h" HAVE_LIBRESSL)
# check if we have found HAVE_DECL_REALLOCARRAY already, so we can safely undefine and redefine it with value 1
if (HAVE_LIBRESSL AND HAVE_DECL_REALLOCARRAY)
  unset(HAVE_DECL_REALLOCARRAY CACHE)
  add_definitions(-DHAVE_DECL_REALLOCARRAY=1)
endif ()
```
This is currently dependent on finding `libressl` but we can also remove the `HAVE_LIBRESSL AND` part.

## moneromooo-monero | 2017-10-23T18:38:00+00:00
Oh, nice, that seems good for now.

## B4rb3rouss | 2017-10-26T08:24:52+00:00
@hucste : no, I'm on 6.2 -stable.


## ston1th | 2017-10-26T08:58:29+00:00
@B4rb3rouss applying all the patches suggested here, I was able to build the release version (I haven't tested monero-core yet).

Later this day I'll submit a PR targeting the latest changes (and also updating the OpenBSD build instructions for 6.2).

## ston1th | 2017-11-08T22:17:55+00:00
@moneromooo-monero I just found out I misread the easylogging++ part above. I thought it was already fixed in master.

Today, trying to build the latest master, the easylogging++ issue came back up.

Could we use 18bcd9a as a fix?

## moneromooo-monero | 2017-11-09T10:38:54+00:00
Yes, that patch seems good.

## moneromooo-monero | 2017-11-25T22:06:18+00:00
Is that fully fixed now ?

## ston1th | 2017-11-26T19:31:05+00:00
Yes I think so.
If @B4rb3rouss is also fine this can be closed.

## danrmiller | 2017-11-28T14:04:58+00:00
@vtnerd commented on Oct 22:

> Ok, the OpenBSD 6.2 release notes indicate that the compiler switched to clang on x86 and amd64 for the base system compiler. So monero will compile on this system because of that change. It looks like the OpenBSD project typically supports a release for roughly 1 year. So either we need to declare no support for OpenBSD versions older than 6.2, or I need to find a fix for this compiler detection issue on OpenBSD 6.1 and earlier.

I was already using clang for building on OpenBSD 6.0. I don't mind if support for this platform is declared to start with 6.2, since OpenBSD hasn't had steady support on monero and therefore not too many users yet. 

I will setup a buildbot builder using OpenBSD 6.2.
FYI, this is the error I'm getting on 6.0 with clang 3.8.0:
https://build.getmonero.org/builders/monero-static-openbsd-amd64/builds/1092/steps/compile/logs/stdio
```
[ 55%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o
/home/buildbot/slave/monero-static-openbsd-amd64/build/src/crypto/slow-hash.c:156:1: error: thread-local storage is not supported for the current target
THREADV uint8_t *hp_state = NULL;
^
/home/buildbot/slave/monero-static-openbsd-amd64/build/src/crypto/slow-hash.c:141:17: note: expanded from macro 'THREADV'
#define THREADV __thread
                ^
/home/buildbot/slave/monero-static-openbsd-amd64/build/src/crypto/slow-hash.c:157:1: error: thread-local storage is not supported for the current target
THREADV int hp_allocated = 0;
^
/home/buildbot/slave/monero-static-openbsd-amd64/build/src/crypto/slow-hash.c:141:17: note: expanded from macro 'THREADV'
#define THREADV __thread
                ^
```


## hucste | 2017-12-03T13:58:52+00:00
Hi, i confirm, i cant compile on my OpenBSD 6.2 stable. 

```
[ 90%] Building CXX object src/simplewallet/CMakeFiles/simplewallet.dir/simplewallet.cpp.o
In file included from /home/user/Documents/Dev/NotMine/monero/src/simplewallet/simplewallet.cpp:45:
In file included from /home/user/Documents/Dev/NotMine/monero/contrib/epee/include/include_base_utils.h:32:
In file included from /home/user/Documents/Dev/NotMine/monero/contrib/epee/include/misc_log_ex.h:52:
/home/user/Documents/Dev/NotMine/monero/external/easylogging++/easylogging++.h:210:11: warning: "Stack trace not available for this compiler"; [-W#warnings]
#         warning "Stack trace not available for this compiler";
          ^
1 warning generated.
[ 90%] Linking CXX executable ../../bin/monero-wallet-cli
../crypto/libcncrypto.a(oaes_lib.c.o): In function `oaes_key_gen':
/home/user/Documents/Dev/NotMine/monero/src/crypto/oaes_lib.c:(.text+0x1f1): warning: warning: rand() may return deterministic values, is that what you want?
../crypto/libcncrypto.a(oaes_lib.c.o): In function `oaes_sprintf':
/home/user/Documents/Dev/NotMine/monero/src/crypto/oaes_lib.c:(.text+0x92): warning: warning: sprintf() is often misused, please use snprintf()
/usr/local/lib/libboost_filesystem-mt.a(operations.o): In function `boost::filesystem::detail::directory_iterator_increment(boost::filesystem::directory_iterator&, boost::system::error_code*)':
libs/filesystem/src/operations.cpp:(.text+0x3fa2): warning: warning: strcpy() is almost always misused, please use strlcpy()
../crypto/libcncrypto.a(oaes_lib.c.o): In function `oaes_sprintf':
/home/user/Documents/Dev/NotMine/monero/src/crypto/oaes_lib.c:(.text+0x9d): warning: warning: strcat() is almost always misused, please use strlcat()
/usr/bin/../lib/libreadline.so.4.0: undefined reference to `tgetnum'
/usr/bin/../lib/libreadline.so.4.0: undefined reference to `tgoto'
/usr/bin/../lib/libreadline.so.4.0: undefined reference to `tgetflag'
/usr/bin/../lib/libreadline.so.4.0: undefined reference to `tputs'
/usr/bin/../lib/libreadline.so.4.0: undefined reference to `tgetent'
/usr/bin/../lib/libreadline.so.4.0: undefined reference to `tgetstr'
c++: error: linker command failed with exit code 1 (use -v to see invocation)
*** Error 1 in build/release (src/simplewallet/CMakeFiles/simplewallet.dir/build.make:133 'bin/monero-wallet-cli')
*** Error 1 in build/release (CMakeFiles/Makefile2:2218 'src/simplewallet/CMakeFiles/simplewallet.dir/all')
*** Error 1 in build/release (Makefile:141 'all')
*** Error 1 in /home/user/Documents/Dev/NotMine/monero (Makefile:67 'release-static')

```

One idea?

## ston1th | 2017-12-03T14:31:19+00:00
Yep, there is another PR pending to fix this: https://github.com/monero-project/monero/pull/2874

## hucste | 2017-12-03T16:19:09+00:00
OK, TY!
This seems to resolve the compil. 

```
[100%] Building CXX object src/blockchain_utilities/CMakeFiles/blockchain_import.dir/blocksdat_file.cpp.o
In file included from /home/user/Documents/Dev/NotMine/monero/src/blockchain_utilities/blocksdat_file.cpp:29:
In file included from /home/user/Documents/Dev/NotMine/monero/src/blockchain_utilities/blocksdat_file.h:37:
In file included from /home/user/Documents/Dev/NotMine/monero/src/cryptonote_basic/cryptonote_basic.h:46:
In file included from /home/user/Documents/Dev/NotMine/monero/contrib/epee/include/serialization/keyvalue_serialization.h:31:
In file included from /home/user/Documents/Dev/NotMine/monero/contrib/epee/include/misc_log_ex.h:52:
/home/user/Documents/Dev/NotMine/monero/external/easylogging++/easylogging++.h:210:11: warning: "Stack trace not available for this compiler"; [-W#warnings]
#         warning "Stack trace not available for this compiler";
          ^
1 warning generated.
[100%] Linking CXX executable ../../bin/monero-blockchain-import
../crypto/libcncrypto.a(oaes_lib.c.o): In function `oaes_key_gen':
/home/user/Documents/Dev/NotMine/monero/src/crypto/oaes_lib.c:(.text+0x1f1): warning: warning: rand() may return deterministic values, is that what you want?
../../external/db_drivers/liblmdb/liblmdb.a(mdb.c.o): In function `mdb_env_open':
/home/user/Documents/Dev/NotMine/monero/external/db_drivers/liblmdb/mdb.c:(text_env+0x368): warning: warning: sprintf() is often misused, please use snprintf()
/usr/local/lib/libboost_filesystem-mt.a(operations.o): In function `boost::filesystem::detail::directory_iterator_increment(boost::filesystem::directory_iterator&, boost::system::error_code*)':
libs/filesystem/src/operations.cpp:(.text+0x3fa2): warning: warning: strcpy() is almost always misused, please use strlcpy()
../crypto/libcncrypto.a(oaes_lib.c.o): In function `oaes_sprintf':
/home/user/Documents/Dev/NotMine/monero/src/crypto/oaes_lib.c:(.text+0x9d): warning: warning: strcat() is almost always misused, please use strlcat()
[100%] Built target blockchain_import

```
But, i dont understand where the monero binary?

```
$ ls -al
total 512
drwxr-xr-x  12 user  user     512 Dec  3 14:01 ./
drwxr-xr-x  11 user  user     512 Dec  3 13:58 ../
drwxr-xr-x   8 user  user     512 Dec  3 13:59 .git/
-rw-r--r--   1 user  user      47 Dec  3 13:59 .gitattributes
-rw-r--r--   1 user  user    1020 Dec  3 13:59 .gitignore
-rw-r--r--   1 user  user   28100 Dec  3 13:59 CMakeLists.txt
-rw-r--r--   1 user  user    7326 Dec  3 13:59 CMakeLists_IOS.txt
-rw-r--r--   1 user  user   11840 Dec  3 13:59 CONTRIBUTING.md
-rw-r--r--   1 user  user    1092 Dec  3 13:59 Dockerfile
-rw-r--r--   1 user  user  100716 Dec  3 13:59 Doxyfile
-rw-r--r--   1 user  user    1582 Dec  3 13:59 LICENSE
-rw-r--r--   1 user  user    5953 Dec  3 13:59 Makefile
-rw-r--r--   1 user  user    2209 Dec  3 13:59 README.i18n.md
-rw-r--r--   1 user  user   30978 Dec  3 13:59 README.md
drwxr-xr-x   3 user  user     512 Dec  3 14:01 build/
drwxr-xr-x   2 user  user     512 Dec  3 16:37 cmake/
drwxr-xr-x   7 user  user     512 Dec  3 13:59 contrib/
drwxr-xr-x   8 user  user     512 Dec  3 13:59 external/
drwxr-xr-x   2 user  user     512 Dec  3 13:59 include/
lrwxr-xr-x   1 user  user      12 Dec  3 13:59 snap@ -> contrib/snap
drwxr-xr-x  22 user  user    1024 Dec  3 13:59 src/
drwxr-xr-x  16 user  user     512 Dec  3 13:59 tests/
drwxr-xr-x   2 user  user     512 Dec  3 13:59 translations/
drwxr-xr-x   8 user  user     512 Dec  3 13:59 utils/

```

## moneromooo-monero | 2017-12-03T16:50:20+00:00
It's in build/whatever/bin

+resolved


## hucste | 2017-12-03T16:54:49+00:00
OK, i found-it! Ty... :+1: 


# Action History
- Created by: B4rb3rouss | 2017-10-03T19:54:08+00:00
- Closed at: 2017-12-03T16:56:23+00:00
