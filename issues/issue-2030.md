---
title: Fails to compile against musl libc
source_url: https://github.com/monero-project/monero/issues/2030
author: ghost
assignees: []
labels: []
created_at: '2017-05-16T01:09:13+00:00'
updated_at: '2022-01-17T19:19:26+00:00'
type: issue
status: closed
closed_at: '2022-01-17T19:19:26+00:00'
---

# Original Description
Running Void Linux, with musl libc. Build fails due to musl's lack of execinfo.h.

```
In file included from /tmp/monero-0.10.3.1/contrib/epee/include/misc_log_ex.h:61:0,
                 from /tmp/monero-0.10.3.1/contrib/epee/include/serialization/keyvalue_serialization.h:31,
                 from /tmp/monero-0.10.3.1/src/p2p/p2p_protocol_defs.h:34,
                 from /tmp/monero-0.10.3.1/src/common/util.h:43,
                 from /tmp/monero-0.10.3.1/src/common/base58.cpp:39:
/tmp/monero-0.10.3.1/external/easylogging++/easylogging++.h:345:25: fatal error: execinfo.h: No such file or directory
 #   include <execinfo.h>
                         ^
compilation terminated.
make[3]: *** [src/common/CMakeFiles/obj_common.dir/build.make:63: src/common/CMakeFiles/obj_common.dir/base58.cpp.o] Error 1
make[2]: *** [CMakeFiles/Makefile2:486: src/common/CMakeFiles/obj_common.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [Makefile:141: all] Error 2
make: *** [Makefile:59: release-all] Error 2

```

# Discussion History
## danrmiller | 2017-05-16T19:20:13+00:00
This is the same case for OpenBSD. 

https://build.getmonero.org/builders/monero-static-openbsd-amd64/builds/4/steps/compile/logs/stdio

There are several platforms without execinfo. I think @moneromooo-monero said its used by easylogging to get stack trace info and so maybe we should just include it on glibc linux.

## moneromooo-monero | 2017-05-17T19:48:25+00:00
Can you try replacing it with elf.h and see if that builds ?

## danrmiller | 2017-05-21T21:02:38+00:00
@moneromooo-monero OpenBSD doesn't have an elf.h but it does have sys/exec_elf.h, which looks about the same. If I use that instead of execinfo.h I get "use of undeclared identifier" errors for val, backtrace, and backtrace_symbols.

@wang-gretzky What about on Void Linux?

## moneromooo-monero | 2017-05-22T07:30:34+00:00
Do you see these symbols anywhere ? If not, then I guess this can be disabled for that platform.

## danrmiller | 2017-06-11T23:53:44+00:00
> Do you see these symbols anywhere ?

No.

## moneromooo-monero | 2017-07-31T20:16:44+00:00
Does this work ? https://github.com/monero-project/monero/pull/2235

## misery | 2017-08-01T06:18:26+00:00
I added a package to AlpineLinux. Alpine uses musl: https://git.alpinelinux.org/cgit/aports/tree/testing/monero
There are some glitches to enable musl support. See the patches.

## moneromooo-monero | 2017-08-01T09:46:03+00:00
Interesting, I thought __has_include was a CLANG only thing. Looks like it's in GCC 5 now.
Also, ideally, the CMakeLists.txt patch should be unnecessary if the easylogging one is applied. What are the errors if it is omitted ?


## misery | 2017-08-01T10:06:27+00:00
Just to avoid a lot of warnings

```
In file included from /home/andre/aports/testing/monero/src/monero-0.10.3.1/contrib/epee/include/misc_log_ex.h:61:0,
                 from /home/andre/aports/testing/monero/src/monero-0.10.3.1/contrib/epee/include/serialization/keyvalue_serialization.h:31,
                 from /home/andre/aports/testing/monero/src/monero-0.10.3.1/src/cryptonote_basic/cryptonote_basic.h:46,
                 from /home/andre/aports/testing/monero/src/monero-0.10.3.1/src/blockchain_utilities/bootstrap_file.h:37,
                 from /home/andre/aports/testing/monero/src/monero-0.10.3.1/src/blockchain_utilities/blockchain_export.cpp:29:
/home/andre/aports/testing/monero/src/monero-0.10.3.1/external/easylogging++/easylogging++.h:205:11: warning: #warning "Stack trace not available for this compiler"; [-Wcpp]
 #         warning "Stack trace not available for this compiler";
           ^~~~~~~
```

_has_include will be in C++17

## moneromooo-monero | 2017-08-01T13:10:24+00:00
Ah, that makes sense, thanks.

## moneromooo-monero | 2017-08-02T10:11:21+00:00
I've updated the patch to remove the warning except once.

## danrmiller | 2017-10-12T04:50:24+00:00
This is what I get with #2235. I wonder if we might revive it since #2249 has been abandoned. I can give you access to an openbsd box.

```[ 43%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
In file included from /home/vagrant/monero/external/easylogging++/easylogging++.cc:18:
/home/vagrant/monero/external/easylogging++/easylogging++.h:216:13: warning: "Stack trace not available for this compiler"; [-W#warnings]
#           warning "Stack trace not available for this compiler";
            ^
/home/vagrant/monero/external/easylogging++/easylogging++.cc:718:1: warning: control may reach end of non-void function [-Wreturn-type]
}
^
/home/vagrant/monero/external/easylogging++/easylogging++.cc:1038:8: error: use of undeclared identifier 'val'
  if ((val == nullptr) || ((strcmp(val, "") == 0))) {
       ^
/home/vagrant/monero/external/easylogging++/easylogging++.cc:1038:36: error: use of undeclared identifier 'val'
  if ((val == nullptr) || ((strcmp(val, "") == 0))) {
                                   ^
/home/vagrant/monero/external/easylogging++/easylogging++.cc:1052:22: error: use of undeclared identifier 'val'
  return std::string(val);
                     ^
2 warnings and 3 errors generated.
```

## moneromooo-monero | 2017-10-12T08:08:41+00:00
Sure, I'll fix if I have access to one.

## moneromooo-monero | 2017-12-02T09:15:30+00:00
I think it's fixed with ston1th's latest commits.

## ston1th | 2017-12-04T22:57:10+00:00
@moneromooo-monero unfortunately my commits just fixed the OpenBSD part, not the musl libc.

I just fired an Alpine Linux VM to test some solutions (maybe a generic one) using `__has_include` and/or `__GNU_LIBRARY__`.

## danrmiller | 2017-12-05T16:24:22+00:00
@ston1th We have a builder for alpine, looks like its close, needs a -lz maybe? 
https://build.getmonero.org/builders/monero-static-alpine-3.5-x86_64/builds/1146/steps/compile/logs/stdio


## ston1th | 2017-12-05T17:37:37+00:00
@danrmiller 
Huh I'm bit confused now.
I tried to build master on Alpine 3.6 and got the `<execinfo.h>` error. I try a clean VM later on.

Anyway.. yes I think there needs to be a `-lz`.
But I'm not sure this will fix these two errors:
```
[ 91%] Linking CXX executable ../../bin/monero-wallet-rpc
../../external/easylogging++/libeasylogging.a(easylogging++.cc.o): In function `el::base::debug::StackTrace::generateNew()':
easylogging++.cc:(.text+0xc7da): undefined reference to `backtrace'
easylogging++.cc:(.text+0xc7e6): undefined reference to `backtrace_symbols'
```

@moneromooo-monero I looked through https://github.com/monero-project/monero/pull/2235 and I would like to add those two ([#2235-R17](https://github.com/monero-project/monero/pull/2235/files#diff-863b4856897c6b87c318d0d23a841411R17), [#2235-R212](https://github.com/monero-project/monero/pull/2235/files#diff-8d1543a579ef452b6020555d522ff978R212)) so we don't spam the build logs with warnings if execinfo is not available.

## moneromooo-monero | 2017-12-10T18:21:58+00:00
2900 is merged.

## TimeTravelersHackedMe | 2018-02-26T17:20:20+00:00
apk add libexecinfo-dev

## moneromooo-monero | 2018-10-01T11:38:27+00:00
Is this still happening ?

## andypost | 2018-10-23T22:44:01+00:00
meanwhile it happened again http://build.alpinelinux.org/buildlogs/build-edge-armhf/testing/monero/monero-0.13.0.2-r0.log
```
[  5%] No download step for 'generate_translations_header'
-- The most recent tag was at c93942e1ed
-- You are ahead of or behind a tagged release
In file included from /home/buildozer/aports/testing/monero/src/monero-0.13.0.2/external/easylogging++/easylogging++.cc:18:
/home/buildozer/aports/testing/monero/src/monero-0.13.0.2/external/easylogging++/easylogging++.h:216:10: warning: #warning "Stack trace not available for this compiler"; [-Wcpp]
 #        warning "Stack trace not available for this compiler";
          ^~~~~~~
```

## andypost | 2018-10-24T04:19:49+00:00
> apk add libexecinfo-dev

this also does not help and without patch it fails on linking
```
[ 80%] Linking CXX executable ../../bin/monero-blockchain-export
/usr/lib/gcc/x86_64-alpine-linux-musl/8.2.0/../../../../x86_64-alpine-linux-musl/bin/ld: ../../external/easylogging++/libeasylogging.a(easylogging++.cc.o): in function `el::base::debug::StackTrace::generateNew()':
easylogging++.cc:(.text+0xd51d): undefined reference to `backtrace'
/usr/lib/gcc/x86_64-alpine-linux-musl/8.2.0/../../../../x86_64-alpine-linux-musl/bin/ld: easylogging++.cc:(.text+0xd529): undefined reference to `backtrace_symbols'
collect2: error: ld returned 1 exit status
```

Ref https://travis-ci.org/alpinelinux/aports/builds/445387732

## cornfeedhobo | 2018-10-24T04:41:25+00:00
I can confirm this, but I think the issue might be [upstream](https://github.com/muflihun/easyloggingpp/issues/540). Currently using [a patch](https://github.com/cornfeedhobo/docker-monero/blob/master/easylogging.patch) as a workaround.

Edit: If libunwind is present, a completely different set of errors is reported, so the suggestion in the linked issue seems fruitless.

## cornfeedhobo | 2019-12-06T16:06:02+00:00
We're back to this failing for `0.15.x.x`. I haven't figured out a patch yet.

## cornfeedhobo | 2019-12-06T21:59:31+00:00
This disables the ~stack traces~ crash logs. Best compromise I can come up with right now.

`export CXXFLAGS="${CXXFLAGS} -DELPP_FEATURE_CRASH_LOG"`

## moneromooo-monero | 2019-12-18T03:09:35+00:00
This enables crash logs. Did you mean -U ?

## jbg | 2020-03-01T08:07:39+00:00
It builds successfully on Alpine with `-DELPP_FEATURE_CRASH_LOG`, so I guess it does disable crash logs @moneromooo-monero 

## codebling | 2021-01-09T07:45:31+00:00
For posterity (because this issue comes up first in a number of search results for musl-related linking errors, especially related to easylogging), the switch that did it for me was `-DSTACK_TRACE:BOOL=OFF` (every other patch or switch suggested in this thread either did not work or gives a 404).

Sorry for the necrobump

## cornfeedhobo | 2021-02-01T16:17:40+00:00
@codebling Can you elaborate on "not work"? I'm also confused by the 404 comment.

FWIW, I've been successfully building and running for over a year with disabled crash logs.

## codebling | 2021-02-01T17:44:47+00:00
@cornfeedhobo sorry the 404 was for some of the links posted, which purportedly contained solutions. Many links were dead. 

"Not work" meant could not get EasyLogging++ to compile and link. This was specifically about EL++, not specifically related to Monero compilation at all, and in that sense was a bit of a thread hijack. Though it's very possible that Monero will run into the same issues next time the project upgrades to a newer version of EL++. 



## cornfeedhobo | 2021-02-01T17:56:03+00:00
@codebling understood. Thanks for clarifying.

## dimandzhi | 2022-01-06T19:35:37+00:00


> apk add libexecinfo-dev

Compiling with both `-lexecinfo` and `-ldl` did it for me. I've lost the source where I've got this idea. Hope it helps anyone.

## cornfeedhobo | 2022-01-17T11:30:59+00:00
@danrmiller I think this issue can be closed with comments left open.

# Action History
- Created by: ghost | 2017-05-16T01:09:13+00:00
- Closed at: 2022-01-17T19:19:26+00:00
