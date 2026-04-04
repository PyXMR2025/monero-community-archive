---
title: NetBSD (x86_64) build stops in randomx/srs/virtual_memory.cpp
source_url: https://github.com/monero-project/monero/issues/6592
author: thomasvaughan
assignees: []
labels: []
created_at: '2020-05-26T18:28:51+00:00'
updated_at: '2022-07-19T20:02:41+00:00'
type: issue
status: closed
closed_at: '2022-07-19T20:02:41+00:00'
---

# Original Description
Here's the stdout:

    [ 19%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/virtual_memory.cpp.o
    /home/t/usr/src/monero/external/randomx/src/virtual_memory.cpp: In function ‘void* allocLargePagesMemory(std::size_t)’:
    /home/t/usr/src/monero/external/randomx/src/virtual_memory.cpp:147:83: error: ‘MAP_HUGETLB’ was not declared in this scope
      mem = mmap(nullptr, bytes, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_HUGETLB | MAP_POPULATE, -1, 0);
                                                                                       ^~~~~~~~~~~
    /home/t/usr/src/monero/external/randomx/src/virtual_memory.cpp:147:97: error: ‘MAP_POPULATE’ was not declared in this scope
      mem = mmap(nullptr, bytes, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS | MAP_HUGETLB | MAP_POPULATE, -1, 0);

In case it helps, [here's a link to the mmap(2) manpage.](https://netbsd.gw.com/cgi-bin/man-cgi?mmap+2+NetBSD-current)
It gets past the above error if I add the following (hastily cut-and-pasted from elsewhere, so not necessarily sensible) immediately above the `#elif defined(__OpenBSD__)` on line 144:

    #elif defined(__NetBSD__)
        #define RESERVED_FLAGS PROT_MPROTECT(PROT_EXEC)
        mem = mmap(nullptr, bytes, PROT_READ | PROT_WRITE | RESERVED_FLAGS, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);

...but the build then stops at

    [ 52%] Linking CXX executable ../../bin/monero-wallet-rpc
    ld: ../common/libcommon.so: undefined reference to `el::base::debug::StackTrace::generateNew()'
    ld: ../common/libcommon.so: undefined reference to `el::base::debug::operator<<(std::ostream&, el::base::debug::StackTrace const&)'
    gmake[3]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:150: bin/monero-wallet-rpc] Error 1


# Discussion History
## moneromooo-monero | 2020-05-27T01:18:19+00:00
First one: report it to the randomx repo
Second one: try adding a check NetBSD to the ifdef list in external/easylogging++/ea_config.h

## thomasvaughan | 2020-07-05T12:51:58+00:00
The RandomX problem has been [fixed upstream](https://github.com/tevador/RandomX/issues/186), so it should be fixed here by #6698 

The easylogging problem looks like it's related to #2030 — monero *does* compile with `CXXFLAGS+="-DELPP_FEATURE_CRASH_LOG"`. In common with some [muscl-based linuxes](https://pkgs.alpinelinux.org/package/edge/main/x86/libexecinfo), NetBSD has an optional [libexecinfo package](http://cdn.netbsd.org/pub/pkgsrc/current/pkgsrc/devel/libexecinfo/README.html) to offset lack of GNU libc backtrace; and if it's installed, it's detected by FindBacktrace.cmake (a useful side-effect of the BOOST_ROOT variable pointing to the same tree — `Found Backtrace: /usr/pkg/lib/libexecinfo.so`), resulting in

    $ ldd easylogging.so | grep libexec
          -lexecinfo.1 => /usr/pkg/lib/libexecinfo.so.1
    
    $ ldd libcommon.so | grep libexec
          -lexecinfo.1 => /usr/pkg/lib/libexecinfo.so.1
    
    $ ldd monero-wallet-rpc | grep libexec
          -lexecinfo.1 => /usr/pkg/lib/libexecinfo.so.1

…even *with* the `-DELPP_FEATURE_CRASH_LOG` flag. So libexecinfo is presumably not fulfilling its intended purpose.

## moneromooo-monero | 2020-07-06T16:19:47+00:00
All fixed then ? You seem to imply there's some problem left with easylogging, but you also say it builds fine with the extra define (which should go in ea_config.h)

## thomasvaughan | 2020-07-07T14:27:21+00:00
Yes, it builds now, thank you; and it has synchronised more than half of the blocks from scratch. I may have been reading too much into the \[spurious?\] `warning "Stack trace not available for this compiler"` message from easylogging++.h. I'll submit a PR adding instructions to README.md, and the missing ` || defined(__NETBSD__)` in ea_config.h.

However, one of the tests fails: ` 7/21 Test  #7: unit_tests .......................***Failed  130.73 sec`.


Here's unit_tests.log:—

[unit_tests.log](https://github.com/monero-project/monero/files/4885339/unit_tests.log)


## moneromooo-monero | 2020-07-07T23:34:40+00:00
This does not show the failing test.
./build/wherever/unit_tests
This will show the failure(s).

# Action History
- Created by: thomasvaughan | 2020-05-26T18:28:51+00:00
- Closed at: 2022-07-19T20:02:41+00:00
