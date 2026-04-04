---
title: '[macOS, depends] build failure'
source_url: https://github.com/monero-project/monero/issues/6256
author: selsta
assignees: []
labels: []
created_at: '2019-12-19T13:38:30+00:00'
updated_at: '2020-01-05T01:07:23+00:00'
type: issue
status: closed
closed_at: '2020-01-05T01:07:23+00:00'
---

# Original Description
Using #6255 and #6231 

```
selsta@mbpR ~/d/m/c/depends> make
Building libiconv...
builddir="`pwd`"; cd libcharset && /Applications/Xcode.app/Contents/Developer/usr/bin/make all && /Applications/Xcode.app/Contents/Developer/usr/bin/make install-lib libdir="$builddir/lib" includedir="$builddir/lib"
cd lib && /Applications/Xcode.app/Contents/Developer/usr/bin/make all
/bin/sh ../libtool --mode=compile /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -mmacosx-version-min=10.8 -I. -I. -I.. -I./.. -I../include -pipe      -fvisibility=hidden -I/Users/selsta/dev/monero2/contrib/depends/x86_64-apple-darwin19.2.0/include     -DLIBDIR=\"/Users/selsta/dev/monero2/contrib/depends/x86_64-apple-darwin19.2.0/lib\" -DBUILDING_LIBCHARSET -DBUILDING_DLL -DENABLE_RELOCATABLE=1 -DIN_LIBRARY -DINSTALLDIR=\"/Users/selsta/dev/monero2/contrib/depends/x86_64-apple-darwin19.2.0/lib\" -DNO_XMALLOC -Dset_relocation_prefix=libcharset_set_relocation_prefix -Drelocate=libcharset_relocate -DHAVE_CONFIG_H -c ./localcharset.c
libtool: compile:  /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -mmacosx-version-min=10.8 -I. -I. -I.. -I./.. -I../include -pipe -fvisibility=hidden -I/Users/selsta/dev/monero2/contrib/depends/x86_64-apple-darwin19.2.0/include -DLIBDIR=\"/Users/selsta/dev/monero2/contrib/depends/x86_64-apple-darwin19.2.0/lib\" -DBUILDING_LIBCHARSET -DBUILDING_DLL -DENABLE_RELOCATABLE=1 -DIN_LIBRARY -DINSTALLDIR=\"/Users/selsta/dev/monero2/contrib/depends/x86_64-apple-darwin19.2.0/lib\" -DNO_XMALLOC -Dset_relocation_prefix=libcharset_set_relocation_prefix -Drelocate=libcharset_relocate -DHAVE_CONFIG_H -c ./localcharset.c -o localcharset.o
./localcharset.c:25:10: fatal error: 'fcntl.h' file not found
#include <fcntl.h>
         ^~~~~~~~~
1 error generated.
make[3]: *** [localcharset.lo] Error 1
make[2]: *** [all] Error 2
make[1]: *** [lib/localcharset.h] Error 2
make: *** [/Users/selsta/dev/monero2/contrib/depends/work/build/x86_64-apple-darwin19.2.0/libiconv/1.15-d8726941672/./.stamp_built] Error 2
```

# Discussion History
# Action History
- Created by: selsta | 2019-12-19T13:38:30+00:00
- Closed at: 2020-01-05T01:07:23+00:00
