---
title: 'simpleminer: static build fails to link on Ubuntu Trusty'
source_url: https://github.com/monero-project/monero/issues/907
author: anonimal
assignees: []
labels: []
created_at: '2016-07-12T21:40:05+00:00'
updated_at: '2017-02-18T05:46:45+00:00'
type: issue
status: closed
closed_at: '2017-02-18T05:46:45+00:00'
---

# Original Description
Also tested on gcc 5.3.0 with same results. [Complete log for 4.8.5 attached](https://github.com/monero-project/bitmonero/files/360281/log.txt).

tl;dr:

```
[ 82%] Building CXX object src/wallet/CMakeFiles/wallet.dir/wallet2.cpp.o
Linking CXX executable ../../bin/simpleminer
/usr/lib/gcc/x86_64-linux-gnu/4.8/libgcc_eh.a(unwind-dw2.o): In function `_Unwind_Resume':
(.text+0x2ae0): multiple definition of `_Unwind_Resume'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libunwind.a(Resume.o):/build/buildd/libunwind-1.1/src/unwind/Resume.c:30: first defined here
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libunwind.a(elf64.o): In function `xz_uncompressed_size':
/build/buildd/libunwind-1.1/src/elfxx.c:194: undefined reference to `lzma_stream_footer_decode'
/build/buildd/libunwind-1.1/src/elfxx.c:201: undefined reference to `lzma_index_buffer_decode'
/build/buildd/libunwind-1.1/src/elfxx.c:205: undefined reference to `lzma_index_size'
/build/buildd/libunwind-1.1/src/elfxx.c:210: undefined reference to `lzma_index_end'
/build/buildd/libunwind-1.1/src/elfxx.c:207: undefined reference to `lzma_index_uncompressed_size'
/build/buildd/libunwind-1.1/src/elfxx.c:210: undefined reference to `lzma_index_end'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libunwind.a(elf64.o): In function `_Uelf64_extract_minidebuginfo':
/build/buildd/libunwind-1.1/src/elfxx.c:278: undefined reference to `lzma_stream_buffer_decode'
collect2: error: ld returned 1 exit status
make[3]: *** [bin/simpleminer] Error 1
make[3]: Leaving directory `/home/anonimal/bitmonero/build/release'
make[2]: *** [src/miner/CMakeFiles/simpleminer.dir/all] Error 2
```

Can this be confirmed as an upstream issue? All dependencies are from default trusty repositories.

_Note: static build passes on Arch._


# Discussion History
## moneroexamples | 2016-07-12T22:23:42+00:00
I think you are missing libunwind  installed. Have you tried installations instructions here:

https://github.com/moneroexamples/compile-monero-09-on-ubuntu-16-04


## anonimal | 2016-07-12T22:54:37+00:00
``` bash
$ apt-cache policy libunwind8-dev | head -n2
libunwind8-dev:
  Installed: 1.1-2.2ubuntu3
```


## moneroexamples | 2016-07-13T00:36:32+00:00
Did you try this? Seems to be path problem:
- http://stackoverflow.com/questions/36626562/while-installing-caffe-in-ubuntu15-04-undefined-reference-to-lzma-index-buffer


## anonimal | 2016-07-13T00:59:54+00:00
```
$ make clean && export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/ && make -j3 release-static
...
[ 82%] Building CXX object src/wallet/CMakeFiles/wallet.dir/wallet2.cpp.o
Linking CXX executable ../../bin/simpleminer
/usr/lib/gcc/x86_64-linux-gnu/4.8/libgcc_eh.a(unwind-dw2.o): In function `_Unwind_Resume':
(.text+0x2ae0): multiple definition of `_Unwind_Resume'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libunwind.a(Resume.o):/build/buildd/libunwind-1.1/src/unwind/Resume.c:30: first defined here
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libunwind.a(elf64.o): In function `xz_uncompressed_size':
/build/buildd/libunwind-1.1/src/elfxx.c:194: undefined reference to `lzma_stream_footer_decode'
/build/buildd/libunwind-1.1/src/elfxx.c:201: undefined reference to `lzma_index_buffer_decode'
/build/buildd/libunwind-1.1/src/elfxx.c:205: undefined reference to `lzma_index_size'
/build/buildd/libunwind-1.1/src/elfxx.c:210: undefined reference to `lzma_index_end'
/build/buildd/libunwind-1.1/src/elfxx.c:207: undefined reference to `lzma_index_uncompressed_size'
/build/buildd/libunwind-1.1/src/elfxx.c:210: undefined reference to `lzma_index_end'
/usr/lib/gcc/x86_64-linux-gnu/4.8/../../../x86_64-linux-gnu/libunwind.a(elf64.o): In function `_Uelf64_extract_minidebuginfo':
/build/buildd/libunwind-1.1/src/elfxx.c:278: undefined reference to `lzma_stream_buffer_decode'
collect2: error: ld returned 1 exit status
make[3]: *** [bin/simpleminer] Error 1
make[3]: Leaving directory `/home/anonimal/bitmonero/build/release'
make[2]: *** [src/miner/CMakeFiles/simpleminer.dir/all] Error 2
```

No luck. :frowning: 


## radfish | 2016-07-13T22:55:42+00:00
If you just uninstall libunwind-dev, the build succeeds. If that's workable, then, disregard the rest.

Looks like the `_Unwind_Resume` is defined by both libunwind and libgcc. Linking one of them dynamically makes the linker happy: either rremoving -static-libgcc or changing to -Wl,-Bdynamic -lunwind.

lzma_\* undefs: (1) if link line is changed to link libunwind dynamically, then the linker pulls liblzma automatically without even having -llzma on the link line, and linking succeeds (2) if link line is changed to link libgcc dynamically, liblzma(.a) is not pulled in automatically, but if specified manually with -Wl,-Wstatic -llzma (along with same for libunwind), then the build also succeeds.

Sidenote: the debian libunwind contains `libunwind-1.1/debian/patches/fix-lzma-linking.patch`, which looks as if it is adding -lzma, but I guess this fix is not working or smth.

Given that the static build still has some dynamic libraries (libc, libm, libdl, libpthread), it seems reasonable to just add libunwind to that list of exceptions, as a special case for gcc 4.8. Then, if the user has no libunwind-dev installed, the static build will succeed. Else, if libunwind is installed, then it (and lzma) will be linked dynamically.


## anonimal | 2016-07-14T03:40:15+00:00
Thanks @radfish, its workable.

I don't actually use Ubuntu; I stumbled onto this when preparing #909 so, when this ticket is resolved and a decision is made about Travis, then hopefully we can squeeze-in the static build (Note: [max time limit was reached](https://travis-ci.org/anonimal/bitmonero/builds/144319713) when I tried to build both - but that was without tweaking).


# Action History
- Created by: anonimal | 2016-07-12T21:40:05+00:00
- Closed at: 2017-02-18T05:46:45+00:00
