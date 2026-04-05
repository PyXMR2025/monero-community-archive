---
title: Wont Compile on Raspberry Pi 3
source_url: https://github.com/xmrig/xmrig/issues/1218
author: tgwaste
assignees: []
labels: []
created_at: '2019-10-04T02:49:20+00:00'
updated_at: '2019-10-04T05:11:39+00:00'
type: issue
status: closed
closed_at: '2019-10-04T05:11:39+00:00'
---

# Original Description
pizero/usr/local/bin# git clone https://github.com/xmrig/xmrig.git
Cloning into 'xmrig'...
remote: Enumerating objects: 164, done.
remote: Counting objects: 100% (164/164), done.
remote: Compressing objects: 100% (120/120), done.
remote: Total 13528 (delta 90), reused 81 (delta 44), pack-reused 13364
Receiving objects: 100% (13528/13528), 4.97 MiB | 2.18 MiB/s, done.
Resolving deltas: 100% (9851/9851), done.
pizero/usr/local/bin# cd xmrig/
pizero/usr/local/bin/xmrig# mkdir build
pizero/usr/local/bin/xmrig# cd build/
pizero/usr/local/bin/xmrig/build# sudo cmake .. -DCMAKE_C_COMPILER=gcc-8 -DCMAKE_CXX_COMPILER=g++-8
sudo: unable to resolve host pizero: Name or service not known
-- The C compiler identification is GNU 8.3.0
-- The CXX compiler identification is GNU 8.3.0
-- Check for working C compiler: /usr/bin/gcc-8
-- Check for working C compiler: /usr/bin/gcc-8 -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/g++-8
-- Check for working CXX compiler: /usr/bin/g++-8 -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Use ARM_TARGET=7 (armv7l)
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found HWLOC: /usr/lib/arm-linux-gnueabihf/libhwloc.so
-- Found UV: /usr/lib/arm-linux-gnueabihf/libuv.a
-- Looking for __builtin___clear_cache
-- Looking for __builtin___clear_cache - found
-- Found OpenSSL: /usr/lib/arm-linux-gnueabihf/libcrypto.so (found version "1.1.1d")
-- Configuring done
-- Generating done
-- Build files have been written to: /usr/local/bin/xmrig/build
pizero/usr/local/bin/xmrig/build# sudo make -j4
sudo: unable to resolve host pizero: Name or service not known
Scanning dependencies of target argon2
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/argon2.c.o
[  1%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/core.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/genkat.c.o
[  3%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/encoding.c.o
[  4%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/impl-select.c.o
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/lib/blake2/blake2.c.o
[  5%] Building C object src/3rdparty/argon2/CMakeFiles/argon2.dir/arch/generic/lib/argon2-arch.c.o
[  6%] Linking C static library libargon2.a
[  6%] Built target argon2
Scanning dependencies of target xmrig
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Console.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuLaunchData.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonRequest.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/ConsoleLog.cpp.o
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/FileLog.cpp.o
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/Log.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/Watcher.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Base.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /usr/local/bin/xmrig/src/base/io/json/JsonChain.h:29,
                 from /usr/local/bin/xmrig/src/base/io/json/JsonChain.cpp:27:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>}; _Tp = rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>; _Alloc = std::allocator<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator> >]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator> >::iterator’ {aka ‘__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>*, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator> > >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseConfig.cpp.o
/usr/include/c++/8/bits/vector.tcc: In member function ‘bool xmrig::JsonChain::addFile(const char*)’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>*, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator> > >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc: In member function ‘bool xmrig::JsonChain::add(rapidjson::Document&&)’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>*, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator> > >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
[ 16%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/config/BaseTransform.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Entry.cpp.o
/usr/include/c++/8/bits/vector.tcc: In member function ‘bool xmrig::JsonChain::addRaw(const char*)’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>*, std::vector<rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator> > >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Process.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Signals.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/dns/DnsRecord.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/Http.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/BaseClient.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Client.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Job.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pool.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /usr/local/bin/xmrig/src/base/net/stratum/Pools.h:29,
                 from /usr/local/bin/xmrig/src/base/net/stratum/Pools.cpp:28:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {xmrig::Pool}; _Tp = xmrig::Pool; _Alloc = std::allocator<xmrig::Pool>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::Pool>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::Pool*, std::vector<xmrig::Pool> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc: In member function ‘void xmrig::Pools::load(const xmrig::IJsonReader&)’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::Pool*, std::vector<xmrig::Pool> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Arguments.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Buffer.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/String.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/tools/Timer.cpp.o
[ 33%] Building C object CMakeFiles/xmrig.dir/src/3rdparty/http-parser/http_parser.c.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Api.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/Httpd.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/ApiRequest.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/base/api/requests/HttpApiRequest.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
In file included from /usr/include/c++/8/map:60,
                 from /usr/local/bin/xmrig/src/base/net/http/HttpData.h:31,
                 from /usr/local/bin/xmrig/src/base/net/http/HttpContext.h:39,
                 from /usr/local/bin/xmrig/src/base/net/http/HttpContext.cpp:33:
/usr/include/c++/8/bits/stl_tree.h: In member function ‘std::pair<std::_Rb_tree_node_base*, std::_Rb_tree_node_base*> std::_Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::_M_get_insert_hint_unique_pos(std::_Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::const_iterator, const key_type&) [with _Key = long long unsigned int; _Val = std::pair<const long long unsigned int, xmrig::HttpContext*>; _KeyOfValue = std::_Select1st<std::pair<const long long unsigned int, xmrig::HttpContext*> >; _Compare = std::less<long long unsigned int>; _Alloc = std::allocator<std::pair<const long long unsigned int, xmrig::HttpContext*> >]’:
/usr/include/c++/8/bits/stl_tree.h:2146:5: note: parameter passing for argument of type ‘std::_Rb_tree<long long unsigned int, std::pair<const long long unsigned int, xmrig::HttpContext*>, std::_Select1st<std::pair<const long long unsigned int, xmrig::HttpContext*> >, std::less<long long unsigned int>, std::allocator<std::pair<const long long unsigned int, xmrig::HttpContext*> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const long long unsigned int, xmrig::HttpContext*> >’} changed in GCC 7.1
     _Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::
     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpServer.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/tools/TcpServer.cpp.o
[ 43%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Hashrate.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Threads.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/Cpu.cpp.o
/usr/local/bin/xmrig/src/backend/common/Workers.cpp: In static member function ‘static xmrig::IWorker* xmrig::Workers<T>::create(xmrig::Thread<xmrig::CpuLaunchData>*) [with T = xmrig::CpuLaunchData]’:
/usr/local/bin/xmrig/src/backend/common/Workers.cpp:171:66: warning: ‘new’ of type ‘xmrig::CpuWorker<1>’ with extended alignment 16 [-Waligned-new=]
         return new CpuWorker<1>(handle->index(), handle->config());
                                                                  ^
/usr/local/bin/xmrig/src/backend/common/Workers.cpp:171:66: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/usr/local/bin/xmrig/src/backend/common/Workers.cpp:171:66: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/usr/local/bin/xmrig/src/backend/common/Workers.cpp:174:66: warning: ‘new’ of type ‘xmrig::CpuWorker<2>’ with extended alignment 16 [-Waligned-new=]
         return new CpuWorker<2>(handle->index(), handle->config());
                                                                  ^
/usr/local/bin/xmrig/src/backend/common/Workers.cpp:174:66: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/usr/local/bin/xmrig/src/backend/common/Workers.cpp:174:66: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/usr/local/bin/xmrig/src/backend/common/Workers.cpp:177:66: warning: ‘new’ of type ‘xmrig::CpuWorker<3>’ with extended alignment 16 [-Waligned-new=]
         return new CpuWorker<3>(handle->index(), handle->config());
                                                                  ^
/usr/local/bin/xmrig/src/backend/common/Workers.cpp:177:66: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/usr/local/bin/xmrig/src/backend/common/Workers.cpp:177:66: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/usr/local/bin/xmrig/src/backend/common/Workers.cpp:180:66: warning: ‘new’ of type ‘xmrig::CpuWorker<4>’ with extended alignment 16 [-Waligned-new=]
         return new CpuWorker<4>(handle->index(), handle->config());
                                                                  ^
/usr/local/bin/xmrig/src/backend/common/Workers.cpp:180:66: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/usr/local/bin/xmrig/src/backend/common/Workers.cpp:180:66: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/usr/local/bin/xmrig/src/backend/common/Workers.cpp:183:66: warning: ‘new’ of type ‘xmrig::CpuWorker<5>’ with extended alignment 16 [-Waligned-new=]
         return new CpuWorker<5>(handle->index(), handle->config());
                                                                  ^
/usr/local/bin/xmrig/src/backend/common/Workers.cpp:183:66: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/usr/local/bin/xmrig/src/backend/common/Workers.cpp:183:66: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuBackend.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuConfig.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThread.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuThreads.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /usr/local/bin/xmrig/src/backend/cpu/CpuThreads.h:29,
                 from /usr/local/bin/xmrig/src/backend/cpu/interfaces/ICpuInfo.h:29,
                 from /usr/local/bin/xmrig/src/backend/cpu/Cpu.h:29,
                 from /usr/local/bin/xmrig/src/backend/cpu/CpuConfig.cpp:26:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {xmrig::CpuLaunchData}; _Tp = xmrig::CpuLaunchData; _Alloc = std::allocator<xmrig::CpuLaunchData>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::CpuLaunchData>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::CpuLaunchData*, std::vector<xmrig::CpuLaunchData> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc: In member function ‘std::vector<xmrig::CpuLaunchData> xmrig::CpuConfig::get(const xmrig::Miner*, const xmrig::Algorithm&) const’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuLaunchData*, std::vector<xmrig::CpuLaunchData> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/Config.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /usr/local/bin/xmrig/src/backend/cpu/CpuThreads.h:29,
                 from /usr/local/bin/xmrig/src/backend/cpu/CpuThreads.cpp:29:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const xmrig::CpuThread&}; _Tp = xmrig::CpuThread; _Alloc = std::allocator<xmrig::CpuThread>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::CpuThread>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
In file included from /usr/include/c++/8/vector:64,
                 from /usr/local/bin/xmrig/src/backend/cpu/CpuThreads.h:29,
                 from /usr/local/bin/xmrig/src/backend/cpu/CpuThreads.cpp:29:
/usr/include/c++/8/bits/stl_vector.h: In constructor ‘xmrig::CpuThreads::CpuThreads(size_t, uint32_t)’:
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/stl_vector.h: In constructor ‘xmrig::CpuThreads::CpuThreads(const Value&)’:
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/core/config/ConfigTransform.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/core/Miner.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/net/JobResults.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
In file included from /usr/include/c++/8/map:60,
                 from /usr/local/bin/xmrig/src/backend/common/Threads.h:29,
                 from /usr/local/bin/xmrig/src/backend/cpu/CpuConfig.h:29,
                 from /usr/local/bin/xmrig/src/core/config/Config.h:32,
                 from /usr/local/bin/xmrig/src/core/Miner.cpp:38:
/usr/include/c++/8/bits/stl_tree.h: In function ‘std::_Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::iterator std::_Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::_M_emplace_hint_unique(std::_Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::const_iterator, _Args&& ...) [with _Args = {const std::piecewise_construct_t&, std::tuple<xmrig::Algorithm::Id&&>, std::tuple<>}; _Key = xmrig::Algorithm::Id; _Val = std::pair<const xmrig::Algorithm::Id, double>; _KeyOfValue = std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >; _Compare = std::less<xmrig::Algorithm::Id>; _Alloc = std::allocator<std::pair<const xmrig::Algorithm::Id, double> >]’:
/usr/include/c++/8/bits/stl_tree.h:2411:7: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
       _Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/net/NetworkState.cpp.o
In file included from /usr/include/c++/8/map:61,
                 from /usr/local/bin/xmrig/src/backend/common/Threads.h:29,
                 from /usr/local/bin/xmrig/src/backend/cpu/CpuConfig.h:29,
                 from /usr/local/bin/xmrig/src/core/config/Config.h:32,
                 from /usr/local/bin/xmrig/src/core/Miner.cpp:38:
/usr/include/c++/8/bits/stl_map.h: In member function ‘void xmrig::MinerPrivate::getHashrate(rapidjson::Value&, rapidjson::Document&, int) const’:
/usr/include/c++/8/bits/stl_map.h:518:8: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
[ 58%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
/usr/include/c++/8/bits/stl_map.h: In member function ‘void xmrig::Miner::printHashrate(bool)’:
/usr/include/c++/8/bits/stl_map.h:518:8: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
/usr/include/c++/8/bits/stl_map.h: In member function ‘virtual void xmrig::Miner::onTimer(const xmrig::Timer*)’:
/usr/include/c++/8/bits/stl_map.h:518:8: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
/usr/include/c++/8/bits/stl_map.h:518:8: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ {aka ‘std::_Rb_tree_const_iterator<std::pair<const xmrig::Algorithm::Id, double> >’} changed in GCC 7.1
    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json_unix.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/base/kernel/Platform_unix.cpp.o
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/HwlocCpuInfo.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /usr/local/bin/xmrig/src/base/tools/String.h:30,
                 from /usr/local/bin/xmrig/src/base/kernel/Platform.h:32,
                 from /usr/local/bin/xmrig/src/net/strategies/DonateStrategy.cpp:31:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {xmrig::Pool}; _Tp = xmrig::Pool; _Alloc = std::allocator<xmrig::Pool>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::Pool>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::Pool*, std::vector<xmrig::Pool> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::emplace_back(_Args&& ...) [with _Args = {xmrig::Pool}; _Tp = xmrig::Pool; _Alloc = std::allocator<xmrig::Pool>]’:
/usr/include/c++/8/bits/vector.tcc:109:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::Pool*, std::vector<xmrig::Pool> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ^~~~~~~~~~~~~~~~~
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o
[ 66%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_blake256.c.o
In file included from /usr/include/c++/8/vector:69,
                 from /usr/local/bin/xmrig/src/backend/cpu/CpuThreads.h:29,
                 from /usr/local/bin/xmrig/src/backend/cpu/interfaces/ICpuInfo.h:29,
                 from /usr/local/bin/xmrig/src/backend/cpu/platform/BasicCpuInfo.h:29,
                 from /usr/local/bin/xmrig/src/backend/cpu/platform/HwlocCpuInfo.h:29,
                 from /usr/local/bin/xmrig/src/backend/cpu/platform/HwlocCpuInfo.cpp:41:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const xmrig::CpuThread&}; _Tp = xmrig::CpuThread; _Alloc = std::allocator<xmrig::CpuThread>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<xmrig::CpuThread>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
In file included from /usr/include/c++/8/vector:64,
                 from /usr/local/bin/xmrig/src/backend/cpu/CpuThreads.h:29,
                 from /usr/local/bin/xmrig/src/backend/cpu/interfaces/ICpuInfo.h:29,
                 from /usr/local/bin/xmrig/src/backend/cpu/platform/BasicCpuInfo.h:29,
                 from /usr/local/bin/xmrig/src/backend/cpu/platform/HwlocCpuInfo.h:29,
                 from /usr/local/bin/xmrig/src/backend/cpu/platform/HwlocCpuInfo.cpp:41:
/usr/include/c++/8/bits/stl_vector.h: In member function ‘void xmrig::HwlocCpuInfo::processTopLevelCache(hwloc_obj_t, const xmrig::Algorithm&, xmrig::CpuThreads&) const’:
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
[ 66%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_groestl.c.o
[ 67%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_jh.c.o
[ 68%] Building C object CMakeFiles/xmrig.dir/src/crypto/cn/c_skein.c.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnCtx.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Algorithm.cpp.o
In file included from /usr/local/bin/xmrig/src/crypto/cn/CnHash.cpp:35:
/usr/local/bin/xmrig/src/crypto/cn/CryptoNight_arm.h: In function ‘__m128i _mm_aesenc_si128(__m128i, __m128i)’:
/usr/local/bin/xmrig/src/crypto/cn/CryptoNight_arm.h:86:31: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) const __m128i zero = { 0 };
                               ^~~~
/usr/local/bin/xmrig/src/crypto/cn/CryptoNight_arm.h: In function ‘__m128i aes_round_tweak_div(const __m128i&, const __m128i&)’:
/usr/local/bin/xmrig/src/crypto/cn/CryptoNight_arm.h:400:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t k[4];
                             ^
/usr/local/bin/xmrig/src/crypto/cn/CryptoNight_arm.h:401:29: warning: requested alignment 16 is larger than 8 [-Wattributes]
     alignas(16) uint32_t x[4];
                             ^
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Coin.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/keccak.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/common/VirtualMemory.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/aes_hash.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/allocator.cpp.o
[ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/argon2_core.c.o
[ 77%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/argon2_ref.c.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2_generator.cpp.o
[ 79%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/bytecode_machine.cpp.o
[ 81%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/dataset.cpp.o
[ 82%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/instructions_portable.cpp.o
[ 83%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/randomx.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /usr/local/bin/xmrig/src/crypto/randomx/dataset.hpp:32,
                 from /usr/local/bin/xmrig/src/crypto/randomx/dataset.cpp:43:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const long long unsigned int&}; _Tp = long long unsigned int; _Alloc = std::allocator<long long unsigned int>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<long long unsigned int>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<long long unsigned int*, std::vector<long long unsigned int> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
[ 83%] Building C object CMakeFiles/xmrig.dir/src/crypto/randomx/reciprocal.c.o
In file included from /usr/include/c++/8/vector:64,
                 from /usr/local/bin/xmrig/src/crypto/randomx/dataset.hpp:32,
                 from /usr/local/bin/xmrig/src/crypto/randomx/dataset.cpp:43:
/usr/include/c++/8/bits/stl_vector.h: In function ‘void randomx::initCache(randomx_cache*, const void*, size_t)’:
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<long long unsigned int*, std::vector<long long unsigned int> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
[ 84%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/soft_aes.cpp.o
[ 85%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/superscalar.cpp.o
/usr/local/bin/xmrig/src/crypto/randomx/randomx.cpp: In function ‘void randomx_calculate_hash(randomx_vm*, const void*, size_t, void*)’:
/usr/local/bin/xmrig/src/crypto/randomx/randomx.cpp:437:34: warning: requested alignment 16 is larger than 8 [-Wattributes]
   alignas(16) uint64_t tempHash[8];
                                  ^
[ 86%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_machine.cpp.o
[ 87%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled_light.cpp.o
[ 88%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_compiled.cpp.o
[ 89%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted_light.cpp.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/randomx/vm_interpreted.cpp.o
[ 91%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/Rx.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxAlgo.cpp.o
[ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxCache.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxConfig.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxDataset.cpp.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/rx/RxVm.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/argon2/Impl.cpp.o
[ 97%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/log/backends/SysLog.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/Tls.cpp.o
[ 99%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpsClient.cpp.o
[100%] Linking CXX executable xmrig
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::Nonce()':
Nonce.cpp:(.text+0x38): undefined reference to `__atomic_store_8'
/usr/bin/ld: Nonce.cpp:(.text+0x4c): undefined reference to `__atomic_store_8'
/usr/bin/ld: Nonce.cpp:(.text+0x60): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::stop()':
Nonce.cpp:(.text+0x184): undefined reference to `__atomic_store_8'
/usr/bin/ld: Nonce.cpp:(.text+0x198): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o:Nonce.cpp:(.text+0x1ac): more undefined references to `__atomic_store_8' follow
/usr/bin/ld: CMakeFiles/xmrig.dir/src/crypto/common/Nonce.cpp.o: in function `xmrig::Nonce::touch()':
Nonce.cpp:(.text+0x1e0): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: Nonce.cpp:(.text+0x1f4): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: Nonce.cpp:(.text+0x208): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::storeStats()':
Worker.cpp:(.text+0x90): undefined reference to `__atomic_store_8'
/usr/bin/ld: Worker.cpp:(.text+0xbc): undefined reference to `__atomic_store_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::timestamp() const':
Worker.cpp:(.text._ZNK5xmrig6Worker9timestampEv[_ZNK5xmrig6Worker9timestampEv]+0x8): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Worker.cpp.o: in function `xmrig::Worker::hashCount() const':
Worker.cpp:(.text._ZNK5xmrig6Worker9hashCountEv[_ZNK5xmrig6Worker9hashCountEv]+0x8): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CpuLaunchData>::stop()':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv]+0x20): undefined reference to `__atomic_store_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4stopEv]+0x9c): undefined reference to `__atomic_fetch_add_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o: in function `xmrig::Workers<xmrig::CpuLaunchData>::tick(unsigned long long)':
Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy]+0x4c): undefined reference to `__atomic_load_8'
/usr/bin/ld: Workers.cpp:(.text._ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy[_ZN5xmrig7WorkersINS_13CpuLaunchDataEE4tickEy]+0x70): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<1u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj1EE18allocateRandomX_VMEv]+0x70): undefined reference to`__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<1u>::consumeJob()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj1EE10consumeJobEv[_ZN5xmrig9CpuWorkerILj1EE10consumeJobEv]+0x20): undefined reference to `__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o: in function `xmrig::CpuWorker<2u>::allocateRandomX_VM()':
CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj2EE18allocateRandomX_VMEv[_ZN5xmrig9CpuWorkerILj2EE18allocateRandomX_VMEv]+0x70): undefined reference to`__atomic_load_8'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/backend/cpu/CpuWorker.cpp.o:CpuWorker.cpp:(.text._ZN5xmrig9CpuWorkerILj2EE10consumeJobEv[_ZN5xmrig9CpuWorkerILj2EE10consumeJobEv]+0x20): more undefined references to `__atomic_load_8' follow
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/xmrig.dir/build.make:1709: xmrig] Error 1
make[1]: *** [CMakeFiles/Makefile2:73: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


# Discussion History
## tgwaste | 2019-10-04T05:11:39+00:00
Nevermind.  This worked better with an Ubuntu Pi Image.

# Action History
- Created by: tgwaste | 2019-10-04T02:49:20+00:00
- Closed at: 2019-10-04T05:11:39+00:00
