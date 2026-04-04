---
title: ./get_libwallet_api.sh several errors
source_url: https://github.com/monero-project/monero-gui/issues/152
author: grigio
assignees: []
labels: []
created_at: '2016-11-11T13:51:21+00:00'
updated_at: '2016-11-13T13:52:44+00:00'
type: issue
status: closed
closed_at: '2016-11-13T13:52:44+00:00'
---

# Original Description
I've installed all the deps on Ubuntu Gnome 16.04 x64 but I get errors
```
./get_libwallet_api.sh
...
Scanning dependencies of target version
[ 86%] Generating version/version.h
-- You are currently on commit 6a2bb62
usage: git rev-list [OPTION] <commit-id>... [ -- paths... ]
...
[ 84%] Building CXX object src/wallet/CMakeFiles/obj_wallet.dir/wallet_args.cpp.o
/home/grigio/Code/monero-core/monero/src/wallet/wallet_args.cpp:37:21: fatal error: version.h: File o directory non esistente
compilation terminated.
src/wallet/CMakeFiles/obj_wallet.dir/build.make:110: set di istruzioni per l'obiettivo "src/wallet/CMakeFiles/obj_wallet.dir/wallet_args.cpp.o" non riuscito
make[2]: *** [src/wallet/CMakeFiles/obj_wallet.dir/wallet_args.cpp.o] Errore 1
make[2]: *** Attesa per i processi non terminati....
...
[100%] Linking CXX executable ../../bin/monero-wallet-rpc
/usr/lib/gcc/x86_64-linux-gnu/5/libgcc_eh.a(unwind-dw2.o): nella funzione "_Unwind_Resume":
(.text+0x27f0): definizione multipla di "_Unwind_Resume"
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunwind.a(Resume.o):/build/libunwind-VOtC4T/libunwind-1.1/src/unwind/Resume.c:30: definito qui per la prima volta
/home/grigio/Code/monero-core/monero/src/crypto/slow-hash.c: In function ‘cn_slow_hash’:
/home/grigio/Code/monero-core/monero/src/crypto/oaes_lib.c:944:2: warning: ‘aes_ctx’ may be used uninitialized in this function [-Wmaybe-uninitialized]
  free( *_ctx );
  ^
/home/grigio/Code/monero-core/monero/src/crypto/slow-hash.c:532:15: note: ‘aes_ctx’ was declared here
     oaes_ctx *aes_ctx;
               ^
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunwind.a(elf64.o): nella funzione "xz_uncompressed_size":
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:194: riferimento non definito a "lzma_stream_footer_decode"
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:201: riferimento non definito a "lzma_index_buffer_decode"
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:205: riferimento non definito a "lzma_index_size"
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:210: riferimento non definito a "lzma_index_end"
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:207: riferimento non definito a "lzma_index_uncompressed_size"
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:210: riferimento non definito a "lzma_index_end"
/usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libunwind.a(elf64.o): nella funzione "_Uelf64_extract_minidebuginfo":
/build/libunwind-VOtC4T/libunwind-1.1/src/elfxx.c:278: riferimento non definito a "lzma_stream_buffer_decode"
collect2: error: ld returned 1 exit status
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:129: set di istruzioni per l'obiettivo "bin/monero-wallet-rpc" non riuscito
make[2]: *** [bin/monero-wallet-rpc] Errore 1
CMakeFiles/Makefile2:1329: set di istruzioni per l'obiettivo "src/wallet/CMakeFiles/wallet_rpc_server.dir/all" non riuscito
make[1]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Errore 2
Makefile:138: set di istruzioni per l'obiettivo "all" non riuscito
make: *** [all] Errore 2
~/Code/monero-core/monero/build/release ~/Code/monero-core/monero ~/Code/monero-core
~/Code/monero-core/monero ~/Code/monero-core



```

# Discussion History
## medusadigital | 2016-11-11T21:53:23+00:00
will hopefully resolve once https://github.com/monero-project/monero/pull/1325 is merged


## grigio | 2016-11-12T06:56:39+00:00
No, it's monero master broken https://github.com/monero-project/monero/issues/1328


## medusadigital | 2016-11-12T10:10:54+00:00
thats what i said, you need to wait until https://github.com/monero-project/monero/pull/1325 is merged, which is the solutuion to https://github.com/monero-project/monero/issues/1328


## medusadigital | 2016-11-12T19:40:48+00:00
seems still broken for now


## grigio | 2016-11-12T20:03:32+00:00
Yes still broken


## medusadigital | 2016-11-12T20:04:40+00:00
https://github.com/monero-project/monero/pull/1331 should disable it


## ghost | 2016-11-12T20:29:05+00:00
Off topic, but wouln't it be more efficient to include the `monero` project as Git submodule, instead of just fetching the HEAD and hoping that it is compatible with the GUI? A submodule would allow to "pin" a specific version of the `monero` Git repo ...


## medusadigital | 2016-11-13T12:32:49+00:00
seems to work now on my side. 

regrading the submodule: there are pros and cons. maybe its worth opening a separate issue so we can discuss it there. it was allready briefly mentioned here: https://github.com/monero-project/monero-core/issues/62 too


# Action History
- Created by: grigio | 2016-11-11T13:51:21+00:00
- Closed at: 2016-11-13T13:52:44+00:00
