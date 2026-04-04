---
title: 'kovri-static-freebsd64: run Clang for nightly build'
source_url: https://github.com/monero-project/meta/issues/52
author: anonimal
assignees: []
labels: []
created_at: '2017-03-08T19:14:49+00:00'
updated_at: '2017-03-16T17:18:16+00:00'
type: issue
status: closed
closed_at: '2017-03-16T17:18:16+00:00'
---

# Original Description
3.8 or higher if possible.

# Discussion History
## danrmiller | 2017-03-09T00:14:09+00:00
https://build.getmonero.org/builders/kovri-static-freebsd64/builds/59/steps/compile/logs/stdio

> -- The C compiler identification is Clang 3.8.1
-- The CXX compiler identification is Clang 3.8.1
-- Check for working C compiler: /usr/local/bin/clang38
-- Check for working C compiler: /usr/local/bin/clang38 -- works
-- Check for working CXX compiler: /usr/local/bin/clang++38
-- Check for working CXX compiler: /usr/local/bin/clang++38 -- works

> [ 97%] Linking CXX executable ../../kovri
/usr/bin/ld: attempted static link of dynamic object `/usr/local/lib/libboost_system.so'
clang-3.8: error: linker command failed with exit code 1 (use -v to see invocation)
gmake[3]: *** [src/app/CMakeFiles/kovri-app.dir/build.make:220: kovri] Error 1

## anonimal | 2017-03-09T01:48:49+00:00
I can't reproduce this exact message but I'm able to statically build the kovri binary without issue (only when commenting out building the new utility binary though). When attempting to statically build the new utility binary on freebsd, I get:

```
[ 93%] Linking CXX executable ../../kovri-util
[ 98%] Built target kovri-app
CMakeFiles/kovri-util.dir/base.cc.o: In function `boost::program_options::typed_value<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, char>::name() const':
/usr/local/include/boost/program_options/detail/value_semantic.hpp:27: undefined reference to `std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > std::__1::operator+<char, std::__1::char_traits<char>, std::__1::allocator<char> >(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, char const*)'
../../libkovri-core.a(exception.cc.o): In function `kovri::core::Exception::Dispatch(char const*)':
/home/anonimal/kovri/src/core/util/exception.cc:(.text+0xcc8): undefined reference to `std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > std::__1::operator+<char, std::__1::char_traits<char>, std::__1::allocator<char> >(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, char const*)'
/usr/local/lib/libboost_log.a(global_logger_storage.o): In function `boost::log::v2s_mt_posix::sources::aux::throw_odr_violation(boost::typeindex::stl_type_index, boost::typeindex::stl_type_index, boost::log::v2s_mt_posix::sources::aux::logger_holder_base const&)':
libs/log/src/global_logger_storage.cpp:(.text+0x346): undefined reference to `std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > std::__1::operator+<char, std::__1::char_traits<char>, std::__1::allocator<char> >(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, char const*)'
libs/log/src/global_logger_storage.cpp:(.text+0x41c): undefined reference to `std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > std::__1::operator+<char, std::__1::char_traits<char>, std::__1::allocator<char> >(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, char const*)'
libs/log/src/global_logger_storage.cpp:(.text+0x4f2): undefined reference to `std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > std::__1::operator+<char, std::__1::char_traits<char>, std::__1::allocator<char> >(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, char const*)'
/usr/local/lib/libboost_log.a(global_logger_storage.o):libs/log/src/global_logger_storage.cpp:(.text+0x508): more undefined references to `std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > std::__1::operator+<char, std::__1::char_traits<char>, std::__1::allocator<char> >(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, char const*)' follow
clang-3.8: error: linker command failed with exit code 1 (use -v to see invocation)
gmake[3]: *** [src/util/CMakeFiles/kovri-util.dir/build.make:142: kovri-util] Error 1
gmake[3]: Leaving directory '/usr/home/anonimal/kovri/build'
gmake[2]: *** [CMakeFiles/Makefile2:300: src/util/CMakeFiles/kovri-util.dir/all] Error 2
gmake[2]: Leaving directory '/usr/home/anonimal/kovri/build'
gmake[1]: *** [Makefile:128: all] Error 2
gmake[1]: Leaving directory '/usr/home/anonimal/kovri/build'
gmake: *** [Makefile:155: release-static] Error 2
[anonimal@freebsd ~/kovri]$
```

I or @MoroccanMalinois should be able to fix this soon.

## anonimal | 2017-03-16T17:18:16+00:00
Fixed.

# Action History
- Created by: anonimal | 2017-03-08T19:14:49+00:00
- Closed at: 2017-03-16T17:18:16+00:00
