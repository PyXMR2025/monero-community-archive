---
title: OSX mage debug linking error
source_url: https://github.com/monero-project/monero/issues/4444
author: ph4r05
assignees: []
labels: []
created_at: '2018-09-25T18:03:15+00:00'
updated_at: '2018-10-01T11:16:31+00:00'
type: issue
status: closed
closed_at: '2018-10-01T11:16:31+00:00'
---

# Original Description
I am trying to build the current master at 8bf5a00564ad0e86b4698008418e28036013ef9f on OSX 10.13.6 with `make debug` but I am getting errors like this:

```
Undefined symbols for architecture x86_64:
  "tools::LoggingPerformanceTimer::LoggingPerformanceTimer(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, unsigned long long, el::Level)", referenced from:
      rct::bulletproof_PROVE(rct::key const&, rct::key const&) in bulletproofs.cc.o
      rct::bulletproof_PROVE(unsigned long long, rct::key const&) in bulletproofs.cc.o
      rct::bulletproof_PROVE(std::__1::vector<rct::key, std::__1::allocator<rct::key> > const&, std::__1::vector<rct::key, std::__1::allocator<rct::key> > const&) in bulletproofs.cc.o
      rct::bulletproof_PROVE(std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> > const&, std::__1::vector<rct::key, std::__1::allocator<rct::key> > const&) in bulletproofs.cc.o
      rct::bulletproof_VERIFY(std::__1::vector<rct::Bulletproof const*, std::__1::allocator<rct::Bulletproof const*> > const&) in bulletproofs.cc.o
  "tools::LoggingPerformanceTimer::~LoggingPerformanceTimer()", referenced from:
      rct::bulletproof_PROVE(rct::key const&, rct::key const&) in bulletproofs.cc.o
      rct::bulletproof_PROVE(unsigned long long, rct::key const&) in bulletproofs.cc.o
      rct::bulletproof_PROVE(std::__1::vector<rct::key, std::__1::allocator<rct::key> > const&, std::__1::vector<rct::key, std::__1::allocator<rct::key> > const&) in bulletproofs.cc.o
      rct::bulletproof_PROVE(std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> > const&, std::__1::vector<rct::key, std::__1::allocator<rct::key> > const&) in bulletproofs.cc.o
      rct::bulletproof_VERIFY(std::__1::vector<rct::Bulletproof const*, std::__1::allocator<rct::Bulletproof const*> > const&) in bulletproofs.cc.o
  "tools::performance_timer_log_level", referenced from:
      rct::bulletproof_PROVE(rct::key const&, rct::key const&) in bulletproofs.cc.o
      rct::bulletproof_PROVE(std::__1::vector<rct::key, std::__1::allocator<rct::key> > const&, std::__1::vector<rct::key, std::__1::allocator<rct::key> > const&) in bulletproofs.cc.o
  "crypto::random32_unbiased(unsigned char*)", referenced from:
      rct::skGen(rct::key&) in rctOps.cpp.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
```

The linker command:

```
 "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld" -demangle -lto_library /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/libLTO.dylib -no_deduplicate -dynamic -dylib -arch x86_64 -dylib_install_name @rpath/libringct_basic.dylib -macosx_version_min 10.13.0 -o libringct_basic.dylib -headerpad_max_install_names CMakeFiles/obj_ringct_basic.dir/rctOps.cpp.o CMakeFiles/obj_ringct_basic.dir/rctTypes.cpp.o CMakeFiles/obj_ringct_basic.dir/rctCryptoOps.c.o CMakeFiles/obj_ringct_basic.dir/multiexp.cc.o CMakeFiles/obj_ringct_basic.dir/bulletproofs.cc.o -rpath /Users/dusanklinec/workspace/monero/build/Darwin/osx-boost-fix/debug/src/common -rpath /Users/dusanklinec/workspace/monero/build/Darwin/osx-boost-fix/debug/src/crypto ../common/libcommon.dylib ../crypto/libcncrypto.dylib /usr/local/opt/openssl/lib/libssl.dylib /usr/local/opt/openssl/lib/libcrypto.dylib -framework IOKit -framework CoreFoundation ../../contrib/epee/src/libepee.a /usr/local/opt/openssl/lib/libssl.dylib /usr/local/opt/openssl/lib/libcrypto.dylib -framework IOKit -framework CoreFoundation ../../external/easylogging++/libeasylogging.dylib /usr/local/lib/libsodium.dylib /usr/local/lib/libunbound.dylib /usr/local/lib/libboost_date_time.dylib /usr/local/lib/libboost_filesystem.dylib /usr/local/lib/libboost_system.dylib /usr/local/lib/libboost_thread.dylib /usr/local/lib/libboost_regex.dylib /usr/local/lib/libboost_chrono.dylib -lc++ -lSystem /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/clang/10.0.0/lib/darwin/libclang_rt.osx.a
```

For the simplicity I focus on a simple function `crypto::random32_unbiased(unsigned char*)` which is supposed to be exported from `cncrypto` library. 

```
nm build/Darwin/master/debug/src/crypto/libcncrypto.dylib  | grep 'unbias'
000000000001dd80 t __ZN6crypto17random32_unbiasedEPh
000000000004ee90 s __ZZN6crypto17random32_unbiasedEPhE5limit
```

The `t` means the symbol is non-external / local. When running the linker without `-demangle` the referenced random_unbiased function is `__ZN6crypto17random32_unbiasedEPh` which is exactly the non-exported symbol in the `libcncrypto.dylib`.

Inspection of the object file yields

```
nm CMakeFiles/obj_cncrypto.dir/crypto.cpp.o  | grep unbia
0000000000000a50 T __ZN6crypto17random32_unbiasedEPh
00000000000076d0 s __ZZN6crypto17random32_unbiasedEPhE5limit
```

So apparently linking step is making the function local.

So the problem is apparently in the visibility of the symbols. Any ideas why such error occur and how to fix it? :)

Repro info:

```
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ --version
Apple LLVM version 10.0.0 (clang-1000.11.45.2)
Target: x86_64-apple-darwin17.7.0
Thread model: posix
InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
```

Using Boost 1.64

Thanks!

# Discussion History
## ph4r05 | 2018-09-25T20:30:16+00:00
Adding the `__attribute__ ((visibility ("default")))` to the header file for unbiased function helps, in particular

```
__attribute__ ((visibility ("default"))) void random32_unbiased(unsigned char *bytes);
```

Causes

```
 nm libcncrypto.dylib | grep unbias
000000000001dd80 T __ZN6crypto17random32_unbiasedEPh
000000000004ee90 s __ZZN6crypto17random32_unbiasedEPhE5limit
```

Which fixes this particular error. 

## ph4r05 | 2018-09-25T20:42:19+00:00
So I've found the problem in https://github.com/monero-project/monero/blob/8bf5a00564ad0e86b4698008418e28036013ef9f/CMakeLists.txt#L772
`-fvisibility=hidden` 

After changing to `-fvisibility=default` I can build again! :)

# Action History
- Created by: ph4r05 | 2018-09-25T18:03:15+00:00
- Closed at: 2018-10-01T11:16:31+00:00
