---
title: no compilation with static option
source_url: https://github.com/monero-project/monero/issues/1090
author: Atrides
assignees: []
labels: []
created_at: '2016-09-17T22:39:24+00:00'
updated_at: '2017-09-30T09:36:21+00:00'
type: issue
status: closed
closed_at: '2017-09-30T09:36:21+00:00'
---

# Original Description
Works: "make debug-all"
Doesn't work: "make release-static-64"

[ 88%] Built target obj_p2p
make[3]: Verzeichnis „/tmp/2/monero-master/build/release“ wird betreten
Scanning dependencies of target p2p
make[3]: Verzeichnis „/tmp/2/monero-master/build/release“ wird verlassen
make[3]: Verzeichnis „/tmp/2/monero-master/build/release“ wird betreten
[ 88%] Linking CXX static library libp2p.a
make[3]: Verzeichnis „/tmp/2/monero-master/build/release“ wird verlassen
[ 88%] Built target p2p
make[3]: Verzeichnis „/tmp/2/monero-master/build/release“ wird betreten
Scanning dependencies of target simplewallet
make[3]: Verzeichnis „/tmp/2/monero-master/build/release“ wird verlassen
make[3]: Verzeichnis „/tmp/2/monero-master/build/release“ wird betreten
[ 88%] Building CXX object src/simplewallet/CMakeFiles/simplewallet.dir/simplewallet.cpp.o
[ 89%] Building CXX object src/simplewallet/CMakeFiles/simplewallet.dir/password_container.cpp.o
[ 89%] Linking CXX executable ../../bin/monero-wallet-cli
/tmp/2/monero-master/src/crypto/slow-hash.c: In function ‘cn_slow_hash’:
/tmp/2/monero-master/src/crypto/oaes_lib.c:944:2: warning: ‘aes_ctx’ may be used uninitialized in this function [-Wmaybe-uninitialized]
  free( __ctx );
  ^
/tmp/2/monero-master/src/crypto/slow-hash.c:532:15: note: ‘aes_ctx’ was declared here
     oaes_ctx *aes_ctx;
               ^
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunwind.a(elf64.o): In Funktion `xz_uncompressed_size':
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:194: Nicht definierter Verweis auf`lzma_stream_footer_decode'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:201: Nicht definierter Verweis auf `lzma_index_buffer_decode'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:205: Nicht definierter Verweis auf`lzma_index_size'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:210: Nicht definierter Verweis auf `lzma_index_end'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:207: Nicht definierter Verweis auf`lzma_index_uncompressed_size'
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:210: Nicht definierter Verweis auf `lzma_index_end'
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunwind.a(elf64.o): In Funktion`_Uelf64_extract_minidebuginfo':
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:278: Nicht definierter Verweis auf `lzma_stream_buffer_decode'
collect2: error: ld returned 1 exit status
src/simplewallet/CMakeFiles/simplewallet.dir/build.make:154: die Regel für Ziel „bin/monero-wallet-cli“ scheiterte
make[3]: *_\* [bin/monero-wallet-cli] Fehler 1
make[3]: Verzeichnis „/tmp/2/monero-master/build/release“ wird verlassen
CMakeFiles/Makefile2:1482: die Regel für Ziel „src/simplewallet/CMakeFiles/simplewallet.dir/all“ scheiterte
make[2]: **\* [src/simplewallet/CMakeFiles/simplewallet.dir/all] Fehler 2
make[2]: Verzeichnis „/tmp/2/monero-master/build/release“ wird verlassen
Makefile:138: die Regel für Ziel „all“ scheiterte
make[1]: **\* [all] Fehler 2
make[1]: Verzeichnis „/tmp/2/monero-master/build/release“ wird verlassen
Makefile:80: die Regel für Ziel „release-static-64“ scheiterte
make: **\* [release-static-64] Fehler 2


# Discussion History
## radfish | 2016-09-18T06:43:13+00:00
#907 duplicate? Specific to Trusty. Try uninstalling libunwind-dev and trying again.


## fluffypony | 2016-09-19T12:09:47+00:00
@radfish Xenial has the same issue, I could only build bins without libunwind.


## radfish | 2016-09-21T01:46:10+00:00
@fluffypony good to know; I did investigate it a bit in #907 but didn't get anywhere beyond excluding libunwind. Since it's affecting not only an old distro, it should be looked into again at some point.


## ghost | 2016-09-22T01:21:45+00:00
Don't forget #993 :)

(I'm also on Xenial)


## moneromooo-monero | 2017-08-15T22:37:57+00:00
This should be fixed, can you confirm ?

## moneromooo-monero | 2017-09-30T09:25:18+00:00
Believed fixed, no confirmation from reported.

+resolved

# Action History
- Created by: Atrides | 2016-09-17T22:39:24+00:00
- Closed at: 2017-09-30T09:36:21+00:00
