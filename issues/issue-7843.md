---
title: 'realease-v17: optional.hpp:1596:3: error: static assertion failed:'
source_url: https://github.com/monero-project/monero/issues/7843
author: moneroexamples
assignees: []
labels: []
created_at: '2021-08-09T10:07:30+00:00'
updated_at: '2021-08-12T09:44:21+00:00'
type: issue
status: closed
closed_at: '2021-08-12T09:44:21+00:00'
---

# Original Description
Started getting the following error on compilation of monero on Manjaro (gcc 11.1.0):

```
In file included from /usr/include/boost/optional/optional.hpp:33,                                                                                                                                                  
                 from /home/mwo/monero/tests/unit_tests/wipeable_string.cpp:29:                                                                                                                                     
/usr/include/boost/optional/optional.hpp: In instantiation of ‘std::basic_ostream<_CharT, _Traits>& boost::operator<<(std::basic_ostream<_CharT, _Traits>&, const boost::optional_detail::optional_tag&) [with CharT
ype = char; CharTrait = std::char_traits<char>]’:                                                                                                                                                                   
/usr/include/gtest/gtest-printers.h:215:9:   required from ‘static void testing::internal::internal_stream_operator_without_lexical_name_lookup::StreamPrinter::PrintValue(const T&, std::ostream*) [with T = boost:
:optional<epee::wipeable_string>; <template-parameter-1-2> = void; <template-parameter-1-3> = std::basic_ostream<char>&; std::ostream = std::basic_ostream<char>]’                                                  
/usr/include/gtest/gtest-printers.h:312:22:   required from ‘void testing::internal::PrintWithFallback(const T&, std::ostream*) [with T = boost::optional<epee::wipeable_string>; std::ostream = std::basic_ostream<char>]’                                              
/usr/include/gtest/gtest-printers.h:441:30:   required from ‘void testing::internal::PrintTo(const T&, std::ostream*) [with T = boost::optional<epee::wipeable_string>; std::ostream = std::basic_ostream<char>]’
/usr/include/gtest/gtest-printers.h:691:12:   required from ‘static void testing::internal::UniversalPrinter<T>::Print(const T&, std::ostream*) [with T = boost::optional<epee::wipeable_string>; std::ostream = std::basic_ostream<char>]’                              
/usr/include/gtest/gtest-printers.h:980:30:   required from ‘void testing::internal::UniversalPrint(const T&, std::ostream*) [with T = boost::optional<epee::wipeable_string>; std::ostream = std::basic_ostream<char>]’                                                 
/usr/include/gtest/gtest-printers.h:865:19:   [ skipping 2 instantiation contexts, use -ftemplate-backtrace-limit=0 to disable ]                                                                                    
/usr/include/gtest/gtest-printers.h:334:36:   required from ‘static std::string testing::internal::FormatForComparison<ToPrint, OtherOperand>::Format(const ToPrint&) [with ToPrint = boost::optional<epee::wipeable_string>; OtherOperand = boost::none_t; std::string = std::__cxx11::basic_string<char>]’                  
/usr/include/gtest/gtest-printers.h:415:45:   required from ‘std::string testing::internal::FormatForComparisonFailureMessage(const T1&, const T2&) [with T1 = boost::optional<epee::wipeable_string>; T2 = boost::none_t; std::string = std::__cxx11::basic_string<char>]’                                                   
/usr/include/gtest/gtest.h:1528:53:   required from ‘testing::AssertionResult testing::internal::CmpHelperEQFailure(const char*, const char*, const T1&, const T2&) [with T1 = boost::none_t; T2 = boost::optional<epee::wipeable_string>]’                              
/usr/include/gtest/gtest.h:1549:28:   required from ‘testing::AssertionResult testing::internal::CmpHelperEQ(const char*, const char*, const T1&, const T2&) [with T1 = boost::none_t; T2 = boost::optional<epee::wipeable_string>]’                                     
/usr/include/gtest/gtest.h:1564:23:   required from ‘static testing::AssertionResult testing::internal::EqHelper::Compare(const char*, const char*, const T1&, const T2&) [with T1 = boost::none_t; T2 = boost::optional<epee::wipeable_string>; typename std::enable_if<((! std::is_integral<_Tp>::value) || (! std::is_pointer<_Dp>::value))>::type* <anonymous> = 0]’                                                                
/home/mwo/monero/tests/unit_tests/wipeable_string.cpp:192:3:   required from here                         
/usr/include/boost/optional/optional.hpp:1596:3: error: static assertion failed: If you want to output boost::optional, include header <boost/optional/optional_io.hpp>                                             
 1596 |   BOOST_STATIC_ASSERT_MSG(sizeof(CharType) == 0, "If you want to output boost::optional, include header <boost/optional/optional_io.hpp>");                                                                 
      |   ^~~~~~~~~~~~~~~~~~~~~~~                    
/usr/include/boost/optional/optional.hpp:1596:3: note: ‘(sizeof (char) == 0)’ evaluates to false          
make[3]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:986: tests/unit_tests/CMakeFiles/unit_tests.dir/wipeable_string.cpp.o] Error 1                                                                  
make[3]: *** Waiting for unfinished jobs....         
make[3]: Leaving directory '/home/mwo/monero/build/release'                                               
make[2]: *** [CMakeFiles/Makefile2:4965: tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2          
make[2]: Leaving directory '/home/mwo/monero/build/release'                                               
make[1]: *** [Makefile:146: all] Error 2             
make[1]: Leaving directory '/home/mwo/monero/build/release'                                               
make: *** [Makefile:95: release] Error 2             

```

# Discussion History
## cirocosta | 2021-08-09T11:31:47+00:00
interesting  - when you mean `release-17`, are you talking about https://github.com/monero-project/monero/pull/7825?

I was able to successfully get a full build for the current HEAD (ed506006d2563c474e52db5a91ba2e20af86f30f): 

```
cmake .. \
  -DUSE_CCACHE=off \
  -DCMAKE_C_COMPILER=`which gcc-11` \
  -DCMAKE_CXX_COMPILER=`which g++-11`
```

being gcc from ubuntu's toolchain test builds (https://launchpad.net/~ubuntu-toolchain-r/+archive/ubuntu/test):

```
g++-11 (Ubuntu 11.1.0-1ubuntu1~20.04) 11.1.0
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

having found boost

```
-- Found Boost Version: 107100
```

on 

```
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=20.04
DISTRIB_CODENAME=focal
DISTRIB_DESCRIPTION="Ubuntu 20.04.2 LTS"
Linux 5.4.0-80-generic #90-Ubuntu SMP Fri Jul 9 22:49:44 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```





## selsta | 2021-08-09T18:36:00+00:00
Are you building release-v0.17 or v0.17.2.0?

## moneroexamples | 2021-08-09T22:05:56+00:00
I'm using `release-v0.17` branch: https://github.com/monero-project/monero/tree/release-v0.17

## selsta | 2021-08-09T22:07:05+00:00
Please try with #7825

## moneroexamples | 2021-08-11T08:59:43+00:00
@selsta Thank you. The patch fixes the issue.

## mj-xmr | 2021-08-11T13:52:25+00:00
If your issue is resolved, please close it, so that we have less to scroll, when looking for new tasks.

# Action History
- Created by: moneroexamples | 2021-08-09T10:07:30+00:00
- Closed at: 2021-08-12T09:44:21+00:00
