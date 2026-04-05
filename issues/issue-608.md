---
title: How can i put config inside xmrig.exe?
source_url: https://github.com/xmrig/xmrig/issues/608
author: LearnMiner
assignees: []
labels: []
created_at: '2018-05-06T13:47:56+00:00'
updated_at: '2018-06-08T03:14:49+00:00'
type: issue
status: closed
closed_at: '2018-05-06T15:16:35+00:00'
---

# Original Description
How can i punt my personal config in xmrig? 2.6.1

In 2.5.3 is in options.cpp but now how?

# Discussion History
## xmrig | 2018-05-06T14:16:02+00:00
Now config spited to 2 files:

 * [src/common/config/CommonConfig.cpp](https://github.com/xmrig/xmrig/blob/master/src/common/config/CommonConfig.cpp#L40) (common options, including pool address as before, Url replaced to Pool).
* [src/core/Config.cpp](https://github.com/xmrig/xmrig/blob/master/src/core/Config.cpp#L43) miner specific options.

## LearnMiner | 2018-05-06T15:16:00+00:00
thanks is working

## TheRogue27 | 2018-06-08T03:13:11+00:00
```
/root/xmrig/src/common/config/CommonConfig.cpp: In constructor 'xmrig::CommonConfig::CommonConfig()':
/root/xmrig/src/common/config/CommonConfig.cpp:61:79: error: no matching function for call to 'std::vector<Pool>::push_back(Pool*)'
     m_pools.push_back(new Pool("pool.example.com", 3333, "WALLET", "PASSWORD"));
                                                                               ^
In file included from /usr/include/c++/5/vector:64:0,
                 from /root/xmrig/src/common/config/CommonConfig.h:28,
                 from /root/xmrig/src/common/config/CommonConfig.cpp:32:
/usr/include/c++/5/bits/stl_vector.h:913:7: note: candidate: void std::vector<_Tp, _Alloc>::push_back(const value_type&) [with _Tp = Pool; _Alloc = std::allocator<Pool>; std::vector<_Tp, _Alloc>::value_type = Pool]
       push_back(const value_type& __x)
       ^
/usr/include/c++/5/bits/stl_vector.h:913:7: note:   no known conversion for argument 1 from 'Pool*' to 'const value_type& {aka const Pool&}'
/usr/include/c++/5/bits/stl_vector.h:931:7: note: candidate: void std::vector<_Tp, _Alloc>::push_back(std::vector<_Tp, _Alloc>::value_type&&) [with _Tp = Pool; _Alloc = std::allocator<Pool>; std::vector<_Tp, _Alloc>::value_type = Pool]
       push_back(value_type&& __x)
       ^
/usr/include/c++/5/bits/stl_vector.h:931:7: note:   no known conversion for argument 1 from 'Pool*' to 'std::vector<Pool>::value_type&& {aka Pool&&}'
CMakeFiles/xmrig.dir/build.make:134: recipe for target 'CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
```

## TheRogue27 | 2018-06-08T03:14:49+00:00
if i change the line to 
 `m_pools.push_back(new Pool*("pool.example.com", 3333, "WALLET", "PASSWORD"));`
i get 
```
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o
/root/xmrig/src/common/config/CommonConfig.cpp: In constructor 'xmrig::CommonConfig::CommonConfig()':
/root/xmrig/src/common/config/CommonConfig.cpp:61:79: error: new initializer expression list treated as compound expression [-fpermissive]
     m_pools.push_back(new Pool*("pool.example.com", 3333, "WALLET", "PASSWORD"));
                                                                               ^
/root/xmrig/src/common/config/CommonConfig.cpp:61:79: warning: left operand of comma operator has no effect [-Wunused-value]
/root/xmrig/src/common/config/CommonConfig.cpp:61:79: warning: right operand of comma operator has no effect [-Wunused-value]
/root/xmrig/src/common/config/CommonConfig.cpp:61:79: warning: right operand of comma operator has no effect [-Wunused-value]
/root/xmrig/src/common/config/CommonConfig.cpp:61:79: error: cannot convert 'const char*' to 'Pool*' in initialization
CMakeFiles/xmrig.dir/build.make:134: recipe for target 'CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2
```

# Action History
- Created by: LearnMiner | 2018-05-06T13:47:56+00:00
- Closed at: 2018-05-06T15:16:35+00:00
