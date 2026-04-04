---
title: make release-static-64 fails on Ubuntu 16 where make works fine
source_url: https://github.com/monero-project/monero/issues/1255
author: Gingeropolous
assignees: []
labels: []
created_at: '2016-10-24T03:07:43+00:00'
updated_at: '2016-12-15T16:14:37+00:00'
type: issue
status: closed
closed_at: '2016-12-15T16:14:37+00:00'
---

# Original Description
/home/user/monero_head/src/crypto/oaes_lib.c:944:2: warning: ‘aes_ctx’ may be used uninitialized in this function [-Wmaybe-uninitialized]
  free( __ctx );
  ^
/home/user/monero_head/src/crypto/slow-hash.c:532:15: note: ‘aes_ctx’ was declared here
     oaes_ctx *aes_ctx;
               ^
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunwind.a(elf64.o): In function `xz_uncompressed_size':
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:194: undefined reference to`lzma_stream_footer_decode'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:201: undefined reference to `lzma_index_buffer_decode'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:205: undefined reference to`lzma_index_size'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:210: undefined reference to `lzma_index_end'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:207: undefined reference to`lzma_index_uncompressed_size'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:210: undefined reference to `lzma_index_end'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunwind.a(elf64.o): In function`_Uelf64_extract_minidebuginfo':
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:278: undefined reference to `lzma_stream_buffer_decode'
collect2: error: ld returned 1 exit status
src/simplewallet/CMakeFiles/simplewallet.dir/build.make:153: recipe for target 'bin/monero-wallet-cli' failed
make[3]: *_\* [bin/monero-wallet-cli] Error 1
make[3]: Leaving directory '/home/user/monero_head/build/release'
CMakeFiles/Makefile2:1492: recipe for target 'src/simplewallet/CMakeFiles/simplewallet.dir/all' failed
make[2]: **\* [src/simplewallet/CMakeFiles/simplewallet.dir/all] Error 2
make[2]: Leaving directory '/home/user/monero_head/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: **\* [all] Error 2
make[1]: Leaving directory '/home/user/monero_head/build/release'
Makefile:80: recipe for target 'release-static-64' failed
make: **\* [release-static-64] Error 2


# Discussion History
## moneromooo-monero | 2016-10-24T08:57:07+00:00
I think it's because the cmake machinery isn't using pkg-config, so doesn't realize libunwind needs liblzma now. You can try fixing that.


## luigi1111 | 2016-12-15T16:14:37+00:00
Move to #1457 

# Action History
- Created by: Gingeropolous | 2016-10-24T03:07:43+00:00
- Closed at: 2016-12-15T16:14:37+00:00
