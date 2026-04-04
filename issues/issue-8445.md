---
title: Bad linker flags added when using mold with Linux
source_url: https://github.com/monero-project/monero/issues/8445
author: eklitzke
assignees: []
labels: []
created_at: '2022-07-20T01:04:16+00:00'
updated_at: '2022-07-20T01:19:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I can't build monero using [mold](https://github.com/rui314/mold) 1.3.1 as my linker on Linux. I've isolated the issue to a problematic line in CMakeLists.txt. It's not totally clear to me whether this should be considered a mold bug or if it's a problem in the monero cmake rules, so I'm reporting it for your consideration. Note that I don't have this issue with lld, suggesting that this is arguably a mold bug, but it's also not clear to me that the monero cmake rules are correct.

Here's how I am configuring and building monero (from a clean checkout of the 0.17.3.2 git tag, the latest release tag as I write this):

```
mkdir build
cd build
cmake -BRelease -GNinja -DBUILD_DOCUMENTATION=OFF -DBUILD_TESTS=OFF -DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_INSTALL_PREFIX=$HOME/.local -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON -DCMAKE_POLICY_DEFAULT_CMP0069=NEW -DUSE_CCACHE=OFF -DUSE_DEVICE_TREZOR=OFF -DUSE_LTO=ON -DCMAKE_C_COMPILER=clang-14 -DCMAKE_C_FLAGS="-Wno-unused-command-line-argument -fuse-ld=mold" -DCMAKE_CXX_COMPILER=clang++-14 -DCMAKE_CXX_FLAGS="-Wno-unused-command-line-argument -fuse-ld=mold" ..
cmake --build Release
```

This fails when building miniupnp with an error message like:
```
mold: fatal: cannot open error: No such file or directory
clang-14: error: linker command failed with exit code 1 (use -v to see invocation)
```

The exact clang invocation that is failing is:
```
/usr/bin/clang-14 -fPIC -Wno-unused-command-line-argument -fuse-ld=mold -pthread -DNDEBUG -Ofast -flto=thin  -Wl,--no-undefined -Wl,-undefined,error -shared -Wl,-soname,libminiupnpc.so.17 -o external/miniupnp/miniupnpc/libminiupnpc.so.2.2.1 external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/igd_desc_parse.c.o external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/miniupnpc.c.o external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/minixml.c.o external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/minisoap.c.o external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/minissdpc.c.o external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/miniwget.c.o external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/upnpcommands.c.o external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/upnpdev.c.o external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/upnpreplyparse.c.o external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/upnperrors.c.o external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/connecthostport.c.o external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/portlistingparse.c.o external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/receivedata.c.o external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/listdevices.c.o external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/addr_is_reserved.c.o
```

From the original error message ("mold: fatal: cannot open error: No such file or directory") it seems that there is some issue with how mold is parsing the command line, as it appears to think that "error" is the name of a file. If I run the exact same clang command as above but remove the part like "-Wl,-undefined,error" then I don't get an error, so that seems to be the part of the command that is tripping up the linker.

Based on this I realized that the "-Wl,-undefined,error" bit comes from the monero CMakeLists.txt file, and the issue is resolved if I make the following change:
```diff
diff --git a/CMakeLists.txt b/CMakeLists.txt
index ffb5abb82..7ed1c779c 100644
--- a/CMakeLists.txt
+++ b/CMakeLists.txt
@@ -129,7 +129,7 @@ function(forbid_undefined_symbols)
   # https://www.unix.com/man-page/linux/1/ld, --no-undefined, Report unresolved symbol references from regular object files.
   add_linker_flag_if_supported(-Wl,--no-undefined TMP)
   # https://www.unix.com/man-page/osx/1/ld/, -undefined, Specifies how undefined symbols are to be treated.
-  add_linker_flag_if_supported(-Wl,-undefined,error TMP)
+  #add_linker_flag_if_supported(-Wl,-undefined,error TMP)
   string(APPEND CMAKE_SHARED_LINKER_FLAGS ${TMP})
   string(APPEND CMAKE_MODULE_LINKER_FLAGS ${TMP})
   set(CMAKE_SHARED_LINKER_FLAGS ${CMAKE_SHARED_LINKER_FLAGS} PARENT_SCOPE)
```

Looking back at the original failing clang invocation, it has **both** "-Wl,--no-undefined" and "-Wl,-undefined,error". However from the comment in the CMakeLists.txt file, it seems to me that the intention is to use whichever of these two linker flags is supported, with the expectation that only one will pass the linker flag test and actually work. Therefore this could probably be fixed by only testing for the second flag if the first one wasn't added.

# Discussion History
## selsta | 2022-07-20T01:19:21+00:00
If you compile a simple test program with both of those linker flags can you also reproduce this issue?

There is a double space after `-flto=thin`, can you make sure that's unrelated? Because I'm confused how two supported linker flags can cause the "no such file" error message.

# Action History
- Created by: eklitzke | 2022-07-20T01:04:16+00:00
