---
title: Error during release-static-64 build on Ubuntu 16.04
source_url: https://github.com/monero-project/monero/issues/1412
author: gsovereignty
assignees: []
labels: []
created_at: '2016-12-06T15:20:39+00:00'
updated_at: '2017-10-03T10:12:22+00:00'
type: issue
status: closed
closed_at: '2017-10-03T10:12:22+00:00'
---

# Original Description
Not sure if libunwind is causing this or something else (I have libunwind 1.1-4.1). Will keep poking around but if anyone knows what's going on please let me know :)

```
[ 96%] Building CXX object src/daemon/CMakeFiles/daemon.dir/rpc_command_executor.cpp.o
/usr/lib/gcc/x86_64-linux-gnu/5/libgcc_eh.a(unwind-dw2.o): In function `_Unwind_Resume':
(.text+0x27f0): multiple definition of `_Unwind_Resume'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunwind.a(Resume.o):/build/libunwind-VOtC4T/libunwind-1.1/src/unwind/Resume.c:30: first defined here
/home/gareth/monero-experimenting/static-builds/2/monero-0.10.0/src/crypto/slow-hash.c: In function 'cn_slow_hash':
/home/gareth/monero-experimenting/static-builds/2/monero-0.10.0/src/crypto/oaes_lib.c:944:2: warning: 'aes_ctx' may be used uninitialized in this function [-Wmaybe-uninitialized]
  free( *_ctx );
  ^
/home/gareth/monero-experimenting/static-builds/2/monero-0.10.0/src/crypto/slow-hash.c:532:15: note: 'aes_ctx' was declared here
     oaes_ctx *aes_ctx;
               ^
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunwind.a(elf64.o): In function `xz_uncompressed_size':
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:194: undefined reference to `lzma_stream_footer_decode'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:201: undefined reference to `lzma_index_buffer_decode'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:205: undefined reference to `lzma_index_size'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:210: undefined reference to `lzma_index_end'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:207: undefined reference to `lzma_index_uncompressed_size'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:210: undefined reference to `lzma_index_end'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunwind.a(elf64.o): In function `_Uelf64_extract_minidebuginfo':
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:278: undefined reference to `lzma_stream_buffer_decode'
collect2: error: ld returned 1 exit status
src/blockchain_utilities/CMakeFiles/blockchain_export.dir/build.make:173: recipe for target 'bin/monero-blockchain-export' failed
make[3]: *** [bin/monero-blockchain-export] Error 1
make[3]: Leaving directory '/home/gareth/monero-experimenting/static-builds/2/monero-0.10.0/build/release'
CMakeFiles/Makefile2:1774: recipe for target 'src/blockchain_utilities/CMakeFiles/blockchain_export.dir/all' failed
make[2]: *** [src/blockchain_utilities/CMakeFiles/blockchain_export.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
/usr/lib/gcc/x86_64-linux-gnu/5/libgcc_eh.a(unwind-dw2.o): In function `_Unwind_Resume':
(.text+0x27f0): multiple definition of `_Unwind_Resume'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunwind.a(Resume.o):/build/libunwind-VOtC4T/libunwind-1.1/src/unwind/Resume.c:30: first defined here
/home/gareth/monero-experimenting/static-builds/2/monero-0.10.0/src/crypto/slow-hash.c: In function 'cn_slow_hash':
/home/gareth/monero-experimenting/static-builds/2/monero-0.10.0/src/crypto/oaes_lib.c:944:2: warning: 'aes_ctx' may be used uninitialized in this function [-Wmaybe-uninitialized]
  free( *_ctx );
  ^
/home/gareth/monero-experimenting/static-builds/2/monero-0.10.0/src/crypto/slow-hash.c:532:15: note: 'aes_ctx' was declared here
     oaes_ctx *aes_ctx;
               ^
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunwind.a(elf64.o): In function `xz_uncompressed_size':
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:194: undefined reference to `lzma_stream_footer_decode'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:201: undefined reference to `lzma_index_buffer_decode'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:205: undefined reference to `lzma_index_size'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:210: undefined reference to `lzma_index_end'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:207: undefined reference to `lzma_index_uncompressed_size'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:210: undefined reference to `lzma_index_end'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunwind.a(elf64.o): In function `_Uelf64_extract_minidebuginfo':
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:278: undefined reference to `lzma_stream_buffer_decode'
collect2: error: ld returned 1 exit status
src/blockchain_utilities/CMakeFiles/blockchain_import.dir/build.make:173: recipe for target 'bin/monero-blockchain-import' failed
make[3]: *** [bin/monero-blockchain-import] Error 1
make[3]: Leaving directory '/home/gareth/monero-experimenting/static-builds/2/monero-0.10.0/build/release'
CMakeFiles/Makefile2:1726: recipe for target 'src/blockchain_utilities/CMakeFiles/blockchain_import.dir/all' failed
make[2]: *** [src/blockchain_utilities/CMakeFiles/blockchain_import.dir/all] Error 2
[ 97%] Linking CXX executable ../../bin/monerod
/usr/lib/gcc/x86_64-linux-gnu/5/libgcc_eh.a(unwind-dw2.o): In function `_Unwind_Resume':
(.text+0x27f0): multiple definition of `_Unwind_Resume'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunwind.a(Resume.o):/build/libunwind-VOtC4T/libunwind-1.1/src/unwind/Resume.c:30: first defined here
/home/gareth/monero-experimenting/static-builds/2/monero-0.10.0/src/daemon/daemon.cpp: In member function 'run':
/usr/include/c++/5/bits/atomic_base.h:374:18: warning: 'rpc_commands' may be used uninitialized in this function [-Wmaybe-uninitialized]
  __atomic_store_n(&_M_i, __i, __m);
                  ^
/home/gareth/monero-experimenting/static-builds/2/monero-0.10.0/src/daemon/daemon.cpp:123:34: note: 'rpc_commands' was declared here
     daemonize::t_command_server* rpc_commands;
                                  ^
/home/gareth/monero-experimenting/static-builds/2/monero-0.10.0/src/crypto/slow-hash.c: In function 'cn_slow_hash':
/home/gareth/monero-experimenting/static-builds/2/monero-0.10.0/src/crypto/oaes_lib.c:944:2: warning: 'aes_ctx' may be used uninitialized in this function [-Wmaybe-uninitialized]
  free( *_ctx );
  ^
/home/gareth/monero-experimenting/static-builds/2/monero-0.10.0/src/crypto/slow-hash.c:532:15: note: 'aes_ctx' was declared here
     oaes_ctx *aes_ctx;
               ^
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunwind.a(elf64.o): In function `xz_uncompressed_size':
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:194: undefined reference to `lzma_stream_footer_decode'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:201: undefined reference to `lzma_index_buffer_decode'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:205: undefined reference to `lzma_index_size'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:210: undefined reference to `lzma_index_end'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:207: undefined reference to `lzma_index_uncompressed_size'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:210: undefined reference to `lzma_index_end'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunwind.a(elf64.o): In function `_Uelf64_extract_minidebuginfo':
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:278: undefined reference to `lzma_stream_buffer_decode'
collect2: error: ld returned 1 exit status
src/daemon/CMakeFiles/daemon.dir/build.make:263: recipe for target 'bin/monerod' failed
make[3]: *** [bin/monerod] Error 1
make[3]: Leaving directory '/home/gareth/monero-experimenting/static-builds/2/monero-0.10.0/build/release'
CMakeFiles/Makefile2:1658: recipe for target 'src/daemon/CMakeFiles/daemon.dir/all' failed
make[2]: *** [src/daemon/CMakeFiles/daemon.dir/all] Error 2
make[2]: Leaving directory '/home/gareth/monero-experimenting/static-builds/2/monero-0.10.0/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/gareth/monero-experimenting/static-builds/2/monero-0.10.0/build/release'
Makefile:80: recipe for target 'release-static-64' failed
make: *** [release-static-64] Error 2
```

# Discussion History
## ghost | 2016-12-06T18:19:12+00:00
Libunwind has caused problems for a few of us so far

## moneromooo-monero | 2016-12-06T22:44:37+00:00
Needs someone who groks cmake to make it use pkg-config, which would then use libunwind's pc file, with almost certainly adds liblzma.

## moneromooo-monero | 2016-12-10T11:18:55+00:00
Does https://github.com/monero-project/monero/pull/1421 help ?

## moneromooo-monero | 2016-12-10T11:36:56+00:00
Nevermind, someone with ubuntu tried it and it doesn't work.

## ghost | 2016-12-14T23:04:00+00:00
Hi @gazhayes would you try `sudo apt-get install -y liblzma-dev` and let us know if this fixes the issue for you?

## moneromooo-monero | 2016-12-16T21:45:37+00:00
Monero would need to try to link against it, whether installed or not.

## moneromooo-monero | 2016-12-23T17:22:38+00:00
New patch on https://github.com/monero-project/monero/pull/1421, which hopefully fixes it.

## xmrdog | 2017-01-01T14:44:16+00:00
I had the same problem on Ubuntu 16.04 LTS on `git checkout v0.10.1`.

Doing `apt-get remove --purge libunwind*` and `make clean`, and `make release-static` again, fixed the problem for me.

If `libunwind` is not really needed but causes problems if available, why have it as a dependency in the first place? What are the benefits?

## moneromooo-monero | 2017-01-01T16:23:25+00:00
It prints stack traces on exceptions, which helps debugging.

## moneromooo-monero | 2017-09-20T21:11:12+00:00
Fixed for those who had the problem ?

## moneromooo-monero | 2017-10-03T10:00:18+00:00
+resolved

# Action History
- Created by: gsovereignty | 2016-12-06T15:20:39+00:00
- Closed at: 2017-10-03T10:12:22+00:00
