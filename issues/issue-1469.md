---
title: Error during make on 5.5.0
source_url: https://github.com/xmrig/xmrig/issues/1469
author: nabeards
assignees: []
labels:
- bug
created_at: '2019-12-29T22:08:15+00:00'
updated_at: '2020-01-21T22:14:42+00:00'
type: issue
status: closed
closed_at: '2020-01-21T22:14:42+00:00'
---

# Original Description
Trying to build with the tag 5.5.0 checked out, and I get the following errors:
```
CMakeFiles/xmrig.dir/src/base/kernel/Env.cpp.o: In function `xmrig::Env::expand(char const*)':
Env.cpp:(.text+0x813): undefined reference to `std::regex_iterator<__gnu_cxx::__normal_iterator<char const*, std::string>, char, std::regex_traits<char> >::regex_iterator(__gnu_cxx::__normal_iterator<char const*, std::string>, __gnu_cxx::__normal_iterator<char const*, std::string>, std::basic_regex<char, std::regex_traits<char> > const&, std::bitset<11ul>)'
Env.cpp:(.text+0x829): undefined reference to `std::regex_iterator<__gnu_cxx::__normal_iterator<char const*, std::string>, char, std::regex_traits<char> >::regex_iterator()'
Env.cpp:(.text+0x83b): undefined reference to `std::regex_iterator<__gnu_cxx::__normal_iterator<char const*, std::string>, char, std::regex_traits<char> >::operator!=(std::regex_iterator<__gnu_cxx::__normal_iterator<char const*, std::string>, char, std::regex_traits<char> > const&)'
Env.cpp:(.text+0x861): undefined reference to `std::regex_iterator<__gnu_cxx::__normal_iterator<char const*, std::string>, char, std::regex_traits<char> >::operator*()'
Env.cpp:(.text+0xa54): undefined reference to `std::regex_iterator<__gnu_cxx::__normal_iterator<char const*, std::string>, char, std::regex_traits<char> >::operator++()'
collect2: error: ld returned 1 exit status
make[2]: *** [xmrig] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
```

This is on CentOS 7.7. 5.4.0 builds without issue.

# Discussion History
## nabeards | 2019-12-29T22:25:23+00:00
It looks like `std:regex_iterator` isn't available before gcc 4.9, max available on CentOS 7 is gcc 4.8.5.

## xmrig | 2019-12-29T22:28:27+00:00
I will add ability to build without env variables support (new feature added in v5.5).
Thank you.

## nabeards | 2019-12-29T22:32:25+00:00
Awesome, thank you for the quick reply!

## frankfpb | 2019-12-29T23:44:58+00:00
the same problem:
[100%] Linking CXX executable xmrig
CMakeFiles/xmrig.dir/src/base/kernel/Env.cpp.o: In function `xmrig::Env::expand(char const*)':
Env.cpp:(.text+0x803): undefined reference to `std::regex_iterator<__gnu_cxx::__normal_iterator<char const*, std::string>, char, std::regex_traits<char> >::regex_iterator(__gnu_cxx::__normal_iterator<char const*, std::string>, __gnu_cxx::__normal_iterator<char const*, std::string>, std::basic_regex<char, std::regex_traits<char> > const&, std::bitset<11ul>)'
Env.cpp:(.text+0x819): undefined reference to `std::regex_iterator<__gnu_cxx::__normal_iterator<char const*, std::string>, char, std::regex_traits<char> >::regex_iterator()'
Env.cpp:(.text+0x82b): undefined reference to `std::regex_iterator<__gnu_cxx::__normal_iterator<char const*, std::string>, char, std::regex_traits<char> >::operator!=(std::regex_iterator<__gnu_cxx::__normal_iterator<char const*, std::string>, char, std::regex_traits<char> > const&)'
Env.cpp:(.text+0x851): undefined reference to `std::regex_iterator<__gnu_cxx::__normal_iterator<char const*, std::string>, char, std::regex_traits<char> >::operator*()'
Env.cpp:(.text+0xa44): undefined reference to `std::regex_iterator<__gnu_cxx::__normal_iterator<char const*, std::string>, char, std::regex_traits<char> >::operator++()'
collect2: error: ld returned 1 exit status
CMakeFiles/xmrig.dir/build.make:4889: ошибка выполнения рецепта для цели «xmrig»
make[2]: *** [xmrig] Ошибка 1
CMakeFiles/Makefile2:73: ошибка выполнения рецепта для цели «CMakeFiles/xmrig.dir/all»
make[1]: *** [CMakeFiles/xmrig.dir/all] Ошибка 2
Makefile:83: ошибка выполнения рецепта для цели «all»
make: *** [all] Ошибка 2


## xmrig | 2019-12-30T09:19:43+00:00
Fixed in master (accidentally commit to it) and dev branches.
Thank you.

## frankfpb | 2020-01-01T16:59:53+00:00
Thanks all right now. gcc version 4.8.4 (Debian 4.8.4-1) 

## nabeards | 2020-01-21T22:14:42+00:00
Works correctly now.

# Action History
- Created by: nabeards | 2019-12-29T22:08:15+00:00
- Closed at: 2020-01-21T22:14:42+00:00
