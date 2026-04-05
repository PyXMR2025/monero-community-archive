---
title: I encountered an error about "fmt::v7::detail::"
source_url: https://github.com/xmrig/xmrig/issues/2135
author: sockx
assignees: []
labels:
- question
created_at: '2021-02-27T04:22:55+00:00'
updated_at: '2021-02-27T08:08:13+00:00'
type: issue
status: closed
closed_at: '2021-02-27T08:08:13+00:00'
---

# Original Description
I have executed
```
1. git clone https://github.com/xmrig/xmrig.git
2. mkdir xmrig\build && cd xmrig\build
3. cmake .. -G "Visual Studio 16 2019" -A x64 -DXMRIG_DEPS=c:\xmrig-deps\msvc2019\x64
```
My version of vs2019 and the installed components are as follows
![image](https://user-images.githubusercontent.com/32082618/109375394-5dbf3780-78f7-11eb-9d50-ef4bc3e8fc68.png)
![image](https://user-images.githubusercontent.com/32082618/109375388-5009b200-78f7-11eb-818e-231aa2eecd13.png)

when I tried to build xmrig, but I encountered the following error.
```text
PS C:\xmrig-6.9.0\build> cmake --build . --config Release
Microsoft (R) Build Engine version 16.1.76+g14b0a930a7 for .NET Framework
Copyright (C) Microsoft Corporation. All rights reserved.

  argon2-avx2.vcxproj -> C:\xmrig-6.9.0\build\src\3rdparty\argon2\Release\argon2-avx2.lib
  argon2-avx512f.vcxproj -> C:\xmrig-6.9.0\build\src\3rdparty\argon2\Release\argon2-avx512f.lib
  argon2-sse2.vcxproj -> C:\xmrig-6.9.0\build\src\3rdparty\argon2\Release\argon2-sse2.lib
  argon2-ssse3.vcxproj -> C:\xmrig-6.9.0\build\src\3rdparty\argon2\Release\argon2-ssse3.lib
  argon2-xop.vcxproj -> C:\xmrig-6.9.0\build\src\3rdparty\argon2\Release\argon2-xop.lib
  argon2.vcxproj -> C:\xmrig-6.9.0\build\src\3rdparty\argon2\Release\argon2.lib
  ethash.vcxproj -> C:\xmrig-6.9.0\build\src\3rdparty\libethash\Release\ethash.lib
  hwloc.vcxproj -> C:\xmrig-6.9.0\build\src\3rdparty\hwloc\Release\hwloc.lib
  xmrig-asm.vcxproj -> C:\xmrig-6.9.0\build\Release\xmrig-asm.lib
  format.cc
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1603,23): error C2672:  'fmt::v7::detail::make_arg': no matching overloaded func
tion found [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1598): message :  while compiling class template member function 'fmt::v7::forma
t_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,fmt::v7::basic_string_view<char>
,char *>::format_arg_store(const fmt::v7::basic_string_view<char> &,char *const &)' [C:\xmrig-6.9.0\build\xmrig.vcxproj
]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1642): message :  see reference to function template instantiation 'fmt::v7::for
mat_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,fmt::v7::basic_string_view<cha
r>,char *>::format_arg_store(const fmt::v7::basic_string_view<char> &,char *const &)' being compiled [C:\xmrig-6.9.0\bu
ild\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(2010): message :  see reference to class template instantiation 'fmt::v7::format
_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,fmt::v7::basic_string_view<char>,
char *>' being compiled [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/format-inl.h(2724): message :  see reference to function template instantiation 'Output
It fmt::v7::format_to<fmt::v7::detail::buffer_appender<char>,char[7],fmt::v7::string_view&,char*&,0>(OutputIt,const S (
&),fmt::v7::string_view &,char *&)' being compiled [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/format-inl.h(2724): message :         with [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/format-inl.h(2724): message :         [ [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/format-inl.h(2724): message :             OutputIt=fmt::v7::detail::buffer_appender<cha
r>, [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/format-inl.h(2724): message :             S=char [7] [C:\xmrig-6.9.0\build\xmrig.vcxpro
j]
C:\xmrig-6.9.0\src\3rdparty/fmt/format-inl.h(2724): message :         ] [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1605,1): error C2783:  'fmt::v7::detail::value<Context> fmt::v7::detail::make_ar
g(const T &)': could not deduce template argument for 'Context' [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1453): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1605,1): error C2783:  'fmt::v7::detail::value<Context> fmt::v7::detail::make_ar
g(const T &)': could not deduce template argument for '__formal' [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1453): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1605,1): error C2974:  'fmt::v7::detail::make_arg': invalid template argument fo
r 'Context', type expected [C:\xmrig-6.9.0\build\xmrig.vcxproj]
  Process.cpp
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1107): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1603,23): error C2672:  'fmt::v7::detail::make_arg': no matching overloaded func
tion found [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1598): message :  while compiling class template member function 'fmt::v7::forma
t_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,std::basic_string<char,std::char
_traits<char>,std::allocator<char>>,const char *>::format_arg_store(const std::basic_string<char,std::char_traits<char>
,std::allocator<char>> &,const char *const &)' [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1642): message :  see reference to function template instantiation 'fmt::v7::for
mat_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,std::basic_string<char,std::ch
ar_traits<char>,std::allocator<char>>,const char *>::format_arg_store(const std::basic_string<char,std::char_traits<cha
r>,std::allocator<char>> &,const char *const &)' being compiled [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(2082): message :  see reference to class template instantiation 'fmt::v7::format
_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,std::basic_string<char,std::char_
traits<char>,std::allocator<char>>,const char *>' being compiled [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\base\kernel\Process.cpp(167): message :  see reference to function template instantiation 'std::basi
c_string<char,std::char_traits<char>,std::allocator<char>> fmt::v7::format<char[6],std::string&,const char*&,char>(cons
t S (&),std::string &,const char *&)' being compiled [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\base\kernel\Process.cpp(167): message :         with [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\base\kernel\Process.cpp(167): message :         [ [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\base\kernel\Process.cpp(167): message :             S=char [6] [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\base\kernel\Process.cpp(167): message :         ] [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1605,1): error C2783:  'fmt::v7::detail::value<Context> fmt::v7::detail::make_ar
g(const T &)': could not deduce template argument for 'Context' [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1453): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1605,1): error C2783:  'fmt::v7::detail::value<Context> fmt::v7::detail::make_ar
g(const T &)': could not deduce template argument for '__formal' [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1453): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1605,1): error C2974:  'fmt::v7::detail::make_arg': invalid template argument fo
r 'Context', type expected [C:\xmrig-6.9.0\build\xmrig.vcxproj]
  BenchClient.cpp
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1107): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\base/net/stratum/Job.h(85,57): warning C4146:  unary minus operator applied to unsigned type, result
 still unsigned [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1603,23): error C2672:  'fmt::v7::detail::make_arg': no matching overloaded func
tion found [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1598): message :  while compiling class template member function 'fmt::v7::forma
t_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,xmrig::String>::format_arg_store
(const xmrig::String &)' [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1642): message :  see reference to function template instantiation 'fmt::v7::for
mat_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,xmrig::String>::format_arg_sto
re(const xmrig::String &)' being compiled [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(2082): message :  see reference to class template instantiation 'fmt::v7::format
_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,xmrig::String>' being compiled [C
:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\base\net\stratum\benchmark\BenchClient.cpp(390): message :  see reference to function template insta
ntiation 'std::basic_string<char,std::char_traits<char>,std::allocator<char>> fmt::v7::format<char[10],xmrig::String&,c
har>(const S (&),xmrig::String &)' being compiled [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\base\net\stratum\benchmark\BenchClient.cpp(390): message :         with [C:\xmrig-6.9.0\build\xmrig.
vcxproj]
C:\xmrig-6.9.0\src\base\net\stratum\benchmark\BenchClient.cpp(390): message :         [ [C:\xmrig-6.9.0\build\xmrig.vcx
proj]
C:\xmrig-6.9.0\src\base\net\stratum\benchmark\BenchClient.cpp(390): message :             S=char [10] [C:\xmrig-6.9.0\b
uild\xmrig.vcxproj]
C:\xmrig-6.9.0\src\base\net\stratum\benchmark\BenchClient.cpp(390): message :         ] [C:\xmrig-6.9.0\build\xmrig.vcx
proj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1605,1): error C2783:  'fmt::v7::detail::value<Context> fmt::v7::detail::make_ar
g(const T &)': could not deduce template argument for 'Context' [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1453): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1605,1): error C2783:  'fmt::v7::detail::value<Context> fmt::v7::detail::make_ar
g(const T &)': could not deduce template argument for '__formal' [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1453): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1605,1): error C2974:  'fmt::v7::detail::make_arg': invalid template argument fo
r 'Context', type expected [C:\xmrig-6.9.0\build\xmrig.vcxproj]
  BenchConfig.cpp
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1107): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1603,23): error C2672:  'fmt::v7::detail::make_arg': no matching overloaded func
tion found [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1598): message :  while compiling class template member function 'fmt::v7::forma
t_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,const unsigned long>::format_arg
_store(const unsigned long &)' [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1642): message :  see reference to function template instantiation 'fmt::v7::for
mat_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,const unsigned long>::format_a
rg_store(const unsigned long &)' being compiled [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(2082): message :  see reference to class template instantiation 'fmt::v7::format
_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,const unsigned long>' being compi
led [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\base\net\stratum\benchmark\BenchConfig.cpp(134): message :  see reference to function template insta
ntiation 'std::basic_string<char,std::char_traits<char>,std::allocator<char>> fmt::v7::format<char[4],const unsigned lo
ng&,char>(const S (&),const unsigned long &)' being compiled [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\base\net\stratum\benchmark\BenchConfig.cpp(134): message :         with [C:\xmrig-6.9.0\build\xmrig.
vcxproj]
C:\xmrig-6.9.0\src\base\net\stratum\benchmark\BenchConfig.cpp(134): message :         [ [C:\xmrig-6.9.0\build\xmrig.vcx
proj]
C:\xmrig-6.9.0\src\base\net\stratum\benchmark\BenchConfig.cpp(134): message :             S=char [4] [C:\xmrig-6.9.0\bu
ild\xmrig.vcxproj]
C:\xmrig-6.9.0\src\base\net\stratum\benchmark\BenchConfig.cpp(134): message :         ] [C:\xmrig-6.9.0\build\xmrig.vcx
proj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1605,1): error C2783:  'fmt::v7::detail::value<Context> fmt::v7::detail::make_ar
g(const T &)': could not deduce template argument for 'Context' [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1453): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1605,1): error C2783:  'fmt::v7::detail::value<Context> fmt::v7::detail::make_ar
g(const T &)': could not deduce template argument for '__formal' [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1453): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1605,1): error C2974:  'fmt::v7::detail::make_arg': invalid template argument fo
r 'Context', type expected [C:\xmrig-6.9.0\build\xmrig.vcxproj]
  DmiMemory.cpp
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1107): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1603,23): error C2672:  'fmt::v7::detail::make_arg': no matching overloaded func
tion found [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1598): message :  while compiling class template member function 'fmt::v7::forma
t_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,std::basic_string<char,std::char
_traits<char>,std::allocator<char>>,std::basic_string<char,std::char_traits<char>,std::allocator<char>>>::format_arg_st
ore(const std::basic_string<char,std::char_traits<char>,std::allocator<char>> &,const std::basic_string<char,std::char_
traits<char>,std::allocator<char>> &)' [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1642): message :  see reference to function template instantiation 'fmt::v7::for
mat_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,std::basic_string<char,std::ch
ar_traits<char>,std::allocator<char>>,std::basic_string<char,std::char_traits<char>,std::allocator<char>>>::format_arg_
store(const std::basic_string<char,std::char_traits<char>,std::allocator<char>> &,const std::basic_string<char,std::cha
r_traits<char>,std::allocator<char>> &)' being compiled [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(2082): message :  see reference to class template instantiation 'fmt::v7::format
_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,std::basic_string<char,std::char_
traits<char>,std::allocator<char>>,std::basic_string<char,std::char_traits<char>,std::allocator<char>>>' being compiled
 [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\hw\dmi\DmiMemory.cpp(235): message :  see reference to function template instantiation 'std::basic_s
tring<char,std::char_traits<char>,std::allocator<char>> fmt::v7::format<const char*,std::basic_string<char,std::char_tr
aits<char>,std::allocator<char>>,std::basic_string<char,std::char_traits<char>,std::allocator<char>>,char>(const S &,st
d::basic_string<char,std::char_traits<char>,std::allocator<char>> &&,std::basic_string<char,std::char_traits<char>,std:
:allocator<char>> &&)' being compiled [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\hw\dmi\DmiMemory.cpp(235): message :         with [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\hw\dmi\DmiMemory.cpp(235): message :         [ [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\hw\dmi\DmiMemory.cpp(235): message :             S=const char * [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\hw\dmi\DmiMemory.cpp(235): message :         ] [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1605,1): error C2783:  'fmt::v7::detail::value<Context> fmt::v7::detail::make_ar
g(const T &)': could not deduce template argument for 'Context' [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1453): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1605,1): error C2783:  'fmt::v7::detail::value<Context> fmt::v7::detail::make_ar
g(const T &)': could not deduce template argument for '__formal' [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1453): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1605,1): error C2974:  'fmt::v7::detail::make_arg': invalid template argument fo
r 'Context', type expected [C:\xmrig-6.9.0\build\xmrig.vcxproj]
  DmiReader.cpp
C:\xmrig-6.9.0\src\3rdparty\fmt\core.h(1107): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\hw\dmi\DmiReader.cpp(61,46): warning C4267:  'argument': conversion from 'size_t' to 'rapidjson::Siz
eType', possible loss of data [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1603,23): error C2672:  'fmt::v7::detail::make_arg': no matching overloaded func
tion found [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1598): message :  while compiling class template member function 'fmt::v7::forma
t_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,unsigned int,unsigned int,unsign
ed int>::format_arg_store(const unsigned int &,const unsigned int &,const unsigned int &)' [C:\xmrig-6.9.0\build\xmrig.
vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1642): message :  see reference to function template instantiation 'fmt::v7::for
mat_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,unsigned int,unsigned int,unsi
gned int>::format_arg_store(const unsigned int &,const unsigned int &,const unsigned int &)' being compiled [C:\xmrig-6
.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(2082): message :  see reference to class template instantiation 'fmt::v7::format
_arg_store<fmt::v7::basic_format_context<fmt::v7::detail::buffer_appender<char>,char>,unsigned int,unsigned int,unsigne
d int>' being compiled [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\hw\dmi\DmiReader.cpp(67): message :  see reference to function template instantiation 'std::basic_st
ring<char,std::char_traits<char>,std::allocator<char>> fmt::v7::format<char[9],uint32_t,uint32_t,uint32_t,char>(const S
 (&),uint32_t &&,uint32_t &&,uint32_t &&)' being compiled [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\hw\dmi\DmiReader.cpp(67): message :         with [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\hw\dmi\DmiReader.cpp(67): message :         [ [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\hw\dmi\DmiReader.cpp(67): message :             S=char [9] [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\hw\dmi\DmiReader.cpp(67): message :         ] [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1605,1): error C2783:  'fmt::v7::detail::value<Context> fmt::v7::detail::make_ar
g(const T &)': could not deduce template argument for 'Context' [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1453): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1605,1): error C2783:  'fmt::v7::detail::value<Context> fmt::v7::detail::make_ar
g(const T &)': could not deduce template argument for '__formal' [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1453): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1605,1): error C2974:  'fmt::v7::detail::make_arg': invalid template argument fo
r 'Context', type expected [C:\xmrig-6.9.0\build\xmrig.vcxproj]
C:\xmrig-6.9.0\src\3rdparty/fmt/core.h(1107): message :  see declaration of 'fmt::v7::detail::make_arg' [C:\xmrig-6.9.0
\build\xmrig.vcxproj]
```

# Discussion History
## xmrig | 2021-02-27T06:57:32+00:00
Your Visual Studio is very outdated, the current version is 16.8.6.
Thank you.


## sockx | 2021-02-27T08:08:06+00:00
Thank you very much, it works normally after upgrading to the latest version.

# Action History
- Created by: sockx | 2021-02-27T04:22:55+00:00
- Closed at: 2021-02-27T08:08:13+00:00
