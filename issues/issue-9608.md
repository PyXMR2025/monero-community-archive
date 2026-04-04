---
title: Getting undefined reference errors when trying to build with make fuzz
source_url: https://github.com/monero-project/monero/issues/9608
author: personnumber3377
assignees: []
labels: []
created_at: '2024-12-10T01:47:16+00:00'
updated_at: '2024-12-14T22:05:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi!

When I try to run `make fuzz` , I get these errors during the build:

```

/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_event_new':
(.text+0x162): undefined reference to `event_set'
/usr/bin/ld: (.text+0x16e): undefined reference to `event_base_set'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_timer_add':
(.text+0x1ef): undefined reference to `event_set'
/usr/bin/ld: (.text+0x1fc): undefined reference to `event_base_set'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_event_base_free':
(.text+0x275): undefined reference to `event_base_free'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `ub_default_event_base':
(.text+0x2f5): undefined reference to `event_base_new'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `ub_get_event_sys':
(.text+0x3c7): undefined reference to `event_get_version'
/usr/bin/ld: (.text+0x3dd): undefined reference to `event_base_get_method'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_event_del':
(.text+0x1b9): undefined reference to `event_del'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_timer_add':
(.text+0x215): undefined reference to `event_add'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_event_add':
(.text+0x239): undefined reference to `event_add'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_event_base_loopexit':
(.text+0x249): undefined reference to `event_base_loopexit'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_event_base_dispatch':
(.text+0x259): undefined reference to `event_base_dispatch'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_signal_del':
(.text+0x299): undefined reference to `event_del'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_timer_del':
(.text+0x2a9): undefined reference to `event_del'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_signal_add':
(.text+0x2b9): undefined reference to `event_add'
collect2: error: ld returned 1 exit status
make[3]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:153: bin/monero-wallet-rpc] Error 1
make[3]: Leaving directory '/home/oof/monero/build/Linux/master/fuzz'
make[2]: *** [CMakeFiles/Makefile2:3159: src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2
make[2]: Leaving directory '/home/oof/monero/build/Linux/master/fuzz'
make[1]: *** [Makefile:146: all] Error 2
make[1]: Leaving directory '/home/oof/monero/build/Linux/master/fuzz'
make: *** [Makefile:163: fuzz] Error 2


```

anyone know a good solution?

# Discussion History
## personnumber3377 | 2024-12-10T01:48:51+00:00
Maybe this here: https://github.com/NLnetLabs/unbound/issues/299 is somehow related?

## personnumber3377 | 2024-12-10T01:53:32+00:00
I think the culprit is the `-D STATIC=ON` in the Makefile. It specifies that a static binary should be built, but something goes wrong in the link process.

## personnumber3377 | 2024-12-10T02:36:51+00:00
This bug I think is something to do with the compiler. If I run this:

```


release-static-linux-x86_64:
	mkdir -p $(builddir)/release
	cd $(builddir)/release && cmake -D STATIC=ON -D CMAKE_C_COMPILER=afl-gcc -D CMAKE_CXX_COMPILER=afl-g++ -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=fuzz -D BUILD_TAG="linux-x64" $(topdir) && $(MAKE)

```

then I get this error:

```
-- Looking for -Wl,--no-undefined linker flag
-- Looking for -Wl,--no-undefined linker flag - found
-- Looking for -Wl,-undefined,error linker flag
-- Looking for -Wl,-undefined,error linker flag - found
CMake Error at CMakeLists.txt:247 (message):
  Undefined symbols test failure: expect(FALSE), success(TRUE)
Call Stack (most recent call first):
  CMakeLists.txt:253 (forbid_undefined_symbols)


-- Configuring incomplete, errors occurred!
make: *** [Makefile:139: release-static-linux-x86_64] Error 1
```

but if we set the compiler to cc and c++, then the compilation continues normally, therefore this has something to do with the compiler:

like so:

```
release-static-linux-x86_64:
	mkdir -p $(builddir)/release
	cd $(builddir)/release && cmake -D STATIC=ON -D CMAKE_C_COMPILER=cc -D CMAKE_CXX_COMPILER=c++ -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=fuzz -D BUILD_TAG="linux-x64" $(topdir) && $(MAKE)
```

that continues to compiling normally.


## selsta | 2024-12-13T23:04:23+00:00
Does https://github.com/monero-project/monero/pull/9463 help?

## personnumber3377 | 2024-12-14T22:05:42+00:00
Hi!

Thanks for the response. I tried to compile with this in the `Makefile`:

```
fuzz:
        mkdir -p $(builddir)/fuzz
        cd $(builddir)/fuzz && cmake -D STATIC=ON -D OSSFUZZ=ON -D SANITIZE=ON -D BUILD_TESTS=ON -D USE_LTO=OFF -D CMAKE_C_COMPILER=afl-gcc -D CMAKE_CXX_COMPILER=afl-g++ -D ARCH="x86-64" -D CMAKE_BUILD_TYPE=fuzz -D BUILD_TAG="linux-x64" $(topdir) && $(MAKE)
```

and I am still getting the same error:

```
[!] WARNING: You are using outdated instrumentation, install LLVM and/or gcc-plugin and use afl-clang-fast/afl-clang-lto/afl-gcc-fast instead!
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_signal_new':
(.text+0xbe): undefined reference to `event_set'
/usr/bin/ld: (.text+0xcb): undefined reference to `event_base_set'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_event_new':
(.text+0x162): undefined reference to `event_set'
/usr/bin/ld: (.text+0x16e): undefined reference to `event_base_set'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_timer_add':
(.text+0x1ef): undefined reference to `event_set'
/usr/bin/ld: (.text+0x1fc): undefined reference to `event_base_set'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_event_base_free':
(.text+0x275): undefined reference to `event_base_free'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `ub_default_event_base':
(.text+0x2f5): undefined reference to `event_base_new'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `ub_get_event_sys':
(.text+0x3c7): undefined reference to `event_get_version'
/usr/bin/ld: (.text+0x3dd): undefined reference to `event_base_get_method'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_event_del':
(.text+0x1b9): undefined reference to `event_del'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_timer_add':
(.text+0x215): undefined reference to `event_add'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_event_add':
(.text+0x239): undefined reference to `event_add'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_event_base_loopexit':
(.text+0x249): undefined reference to `event_base_loopexit'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_event_base_dispatch':
(.text+0x259): undefined reference to `event_base_dispatch'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_signal_del':
(.text+0x299): undefined reference to `event_del'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_timer_del':
(.text+0x2a9): undefined reference to `event_del'
/usr/bin/ld: /usr/lib/x86_64-linux-gnu/libunbound.a(ub_event_pluggable.o): in function `my_signal_add':
(.text+0x2b9): undefined reference to `event_add'
collect2: error: ld returned 1 exit status
```

It works if I change the afl compiler to the normal gcc and g++ so I think it may have something to do with the specific compiler version I am using.

# Action History
- Created by: personnumber3377 | 2024-12-10T01:47:16+00:00
