---
title: Can't build xmrig on raspberry os 11 aka "bullseye"
source_url: https://github.com/xmrig/xmrig/issues/2695
author: mglogowski
assignees: []
labels: []
created_at: '2021-11-15T01:12:16+00:00'
updated_at: '2021-11-15T18:48:07+00:00'
type: issue
status: closed
closed_at: '2021-11-15T18:48:07+00:00'
---

# Original Description
**Describe the bug**
Following the instructions to get a working xmrig. Using version 6.15.3 of xmrig

**To Reproduce**
doing
cmake .. -DCMAKE_BUILD_TYPE=Release -DARM_TARGET=7 -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_HWLOC=OFF -DWITH_TLS=OFF -DWITH_ASM=OFF
make -j 4 --environment-overrides --keep-going

---

pi@raspberry:~/SOURCE/XMRig/xmrig-6.15.3/build $ cmake .. -DCMAKE_BUILD_TYPE=Release -DARM_TARGET=7 -DWITH_OPENCL=OFF -DWITH_CUDA=OFF -DWITH_HWLOC=OFF -DWITH_TLS=OFF -DWITH_ASM=OFF
-- Use ARM_TARGET=7 (aarch64)
-- WITH_MSR=OFF
-- Configuring done
-- Generating done
-- Build files have been written to: /home/pi/SOURCE/XMRig/xmrig-6.15.3/build
pi@raspberry:~/SOURCE/XMRig/xmrig-6.15.3/build $ make -j 4 --environment-overrides --keep-going
[  2%] Built target ethash
[  6%] Built target argon2
[  6%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Client.cpp.o
[  7%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/FailoverStrategy.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Socks5.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/ProxyUrl.cpp.o
[  8%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/strategies/SinglePoolStrategy.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/Url.cpp.o
[  9%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/tools/LineReader.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/tools/NetBuffer.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Arguments.cpp.o
[ 11%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/cryptonote/BlockTemplate.cpp.o
[ 12%] Building C object CMakeFiles/xmrig-notls.dir/src/base/tools/cryptonote/crypto-ops-data.c.o
[ 12%] Building C object CMakeFiles/xmrig-notls.dir/src/base/tools/cryptonote/crypto-ops.c.o
[ 13%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/cryptonote/Signatures.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/cryptonote/WalletAddress.cpp.o
[ 14%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Cvt.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/String.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/tools/Timer.cpp.o
[ 16%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/AutoClient.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/EthStratumClient.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o
[ 18%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/benchmark/BenchConfig.cpp.o
[ 18%] Building C object CMakeFiles/xmrig-notls.dir/src/3rdparty/llhttp/llhttp.c.o
[ 19%] Building C object CMakeFiles/xmrig-notls.dir/src/3rdparty/llhttp/api.c.o
[ 20%] Building C object CMakeFiles/xmrig-notls.dir/src/3rdparty/llhttp/http.c.o
[ 20%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/api/Api.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/api/Httpd.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/api/requests/ApiRequest.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/api/requests/HttpApiRequest.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/Fetch.cpp.o
[ 23%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/HttpApiResponse.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/HttpClient.cpp.o
[ 24%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/HttpContext.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/HttpData.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/HttpListener.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/HttpResponse.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/DaemonClient.cpp.o
[ 27%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/stratum/SelfSelectClient.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/tools/TcpServer.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Hashrate.cpp.o
[ 29%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Threads.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Worker.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/Workers.cpp.o
[ 31%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/benchmark/Benchmark.cpp.o
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Workers.cpp: In static member function ‘static xmrig::IWorker* xmrig::Workers<T>::create(xmrig::Thread<T>*) [with T = xmrig::CpuLaunchData]’:
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Workers.cpp:229:63: warning: ‘new’ of type ‘xmrig::CpuWorker<1>’ with extended alignment 16 [-Waligned-new=]
  229 |         return new CpuWorker<1>(handle->id(), handle->config());
      |                                                               ^
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Workers.cpp:229:63: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Workers.cpp:229:63: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Workers.cpp:232:63: warning: ‘new’ of type ‘xmrig::CpuWorker<2>’ with extended alignment 16 [-Waligned-new=]
  232 |         return new CpuWorker<2>(handle->id(), handle->config());
      |                                                               ^
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Workers.cpp:232:63: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Workers.cpp:232:63: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Workers.cpp:235:63: warning: ‘new’ of type ‘xmrig::CpuWorker<3>’ with extended alignment 16 [-Waligned-new=]
  235 |         return new CpuWorker<3>(handle->id(), handle->config());
      |                                                               ^
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Workers.cpp:235:63: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Workers.cpp:235:63: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Workers.cpp:238:63: warning: ‘new’ of type ‘xmrig::CpuWorker<4>’ with extended alignment 16 [-Waligned-new=]
  238 |         return new CpuWorker<4>(handle->id(), handle->config());
      |                                                               ^
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Workers.cpp:238:63: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Workers.cpp:238:63: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Workers.cpp:241:63: warning: ‘new’ of type ‘xmrig::CpuWorker<5>’ with extended alignment 16 [-Waligned-new=]
  241 |         return new CpuWorker<5>(handle->id(), handle->config());
      |                                                               ^
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Workers.cpp:241:63: note: uses ‘void* operator new(std::size_t)’, which does not have an alignment parameter
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Workers.cpp:241:63: note: use ‘-faligned-new’ to enable C++17 over-aligned new support
[ 32%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/common/benchmark/BenchState.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/Cpu.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuBackend.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuConfig.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThread.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuThreads.cpp.o
In file included from /usr/include/c++/10/vector:72,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/base/crypto/Algorithm.h:25,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Threads.h:29,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/cpu/CpuConfig.h:23,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/cpu/CpuConfig.cpp:19:
/usr/include/c++/10/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const xmrig::Miner*&, const xmrig::Algorithm&, const xmrig::CpuConfig&, const xmrig::CpuThread&, const unsigned int&}; _Tp = xmrig::CpuLaunchData; _Alloc = std::allocator<xmrig::CpuLaunchData>]’:
/usr/include/c++/10/bits/vector.tcc:426:7: note: parameter passing for argument of type ‘std::vector<xmrig::CpuLaunchData>::iterator’ changed in GCC 7.1
  426 |       vector<_Tp, _Alloc>::
      |       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/10/bits/vector.tcc: In member function ‘std::vector<xmrig::CpuLaunchData> xmrig::CpuConfig::get(const xmrig::Miner*, const xmrig::Algorithm&) const’:
/usr/include/c++/10/bits/vector.tcc:121:21: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuLaunchData*, std::vector<xmrig::CpuLaunchData> >’ changed in GCC 7.1
  121 |    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
      |    ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 35%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/CpuWorker.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/BasicCpuInfo_arm.cpp.o
In file included from /usr/include/c++/10/vector:72,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/cpu/CpuThreads.h:23,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/cpu/CpuThreads.cpp:22:
/usr/include/c++/10/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const xmrig::CpuThread&}; _Tp = xmrig::CpuThread; _Alloc = std::allocator<xmrig::CpuThread>]’:
/usr/include/c++/10/bits/vector.tcc:426:7: note: parameter passing for argument of type ‘std::vector<xmrig::CpuThread>::iterator’ changed in GCC 7.1
  426 |       vector<_Tp, _Alloc>::
      |       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/10/bits/vector.tcc:426:7: note: parameter passing for argument of type ‘std::vector<xmrig::CpuThread>::iterator’ changed in GCC 7.1
In file included from /usr/include/c++/10/vector:67,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/cpu/CpuThreads.h:23,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/cpu/CpuThreads.cpp:22:
/usr/include/c++/10/bits/stl_vector.h: In constructor ‘xmrig::CpuThreads::CpuThreads(size_t, uint32_t)’:
/usr/include/c++/10/bits/stl_vector.h:1198:21: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
 1198 |    _M_realloc_insert(end(), __x);
      |    ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
/usr/include/c++/10/bits/stl_vector.h: In constructor ‘xmrig::CpuThreads::CpuThreads(const Value&)’:
/usr/include/c++/10/bits/stl_vector.h:1198:21: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
 1198 |    _M_realloc_insert(end(), __x);
      |    ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
/usr/include/c++/10/bits/stl_vector.h:1198:21: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::CpuThread*, std::vector<xmrig::CpuThread> >’ changed in GCC 7.1
 1198 |    _M_realloc_insert(end(), __x);
      |    ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
[ 36%] Building CXX object CMakeFiles/xmrig-notls.dir/src/backend/cpu/platform/lscpu_arm.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/config/Config.cpp.o
[ 38%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/config/ConfigTransform.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Controller.cpp.o
[ 39%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Miner.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig-notls.dir/src/core/Taskbar.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/JobResults.cpp.o
[ 41%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/Network.cpp.o
In file included from /usr/include/c++/10/map:60,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Threads.h:24,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/cpu/CpuConfig.h:23,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/core/config/Config.h:27,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/core/Miner.cpp:36:
/usr/include/c++/10/bits/stl_tree.h: In function ‘std::_Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::iterator std::_Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::_M_emplace_hint_unique(std::_Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::const_iterator, _Args&& ...) [with _Args = {const std::piecewise_construct_t&, std::tuple<xmrig::Algorithm::Id&&>, std::tuple<>}; _Key = xmrig::Algorithm::Id; _Val = std::pair<const xmrig::Algorithm::Id, double>; _KeyOfValue = std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >; _Compare = std::less<xmrig::Algorithm::Id>; _Alloc = std::allocator<std::pair<const xmrig::Algorithm::Id, double> >]’:
/usr/include/c++/10/bits/stl_tree.h:2458:7: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ changed in GCC 7.1
 2458 |       _Rb_tree<_Key, _Val, _KeyOfValue, _Compare, _Alloc>::
      |       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 42%] Building CXX object CMakeFiles/xmrig-notls.dir/src/net/strategies/DonateStrategy.cpp.o
In file included from /usr/include/c++/10/map:61,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/common/Threads.h:24,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/backend/cpu/CpuConfig.h:23,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/core/config/Config.h:27,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/core/Miner.cpp:36:
/usr/include/c++/10/bits/stl_map.h: In member function ‘void xmrig::MinerPrivate::getHashrate(rapidjson::Value&, rapidjson::Document&, int) const’:
/usr/include/c++/10/bits/stl_map.h:520:37: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ changed in GCC 7.1
  520 |    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
      |          ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  521 |      std::forward_as_tuple(std::move(__k)),
      |      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  522 |      std::tuple<>());
      |      ~~~~~~~~~~~~~~~                 
/usr/include/c++/10/bits/stl_map.h: In member function ‘void xmrig::Miner::execCommand(char)’:
/usr/include/c++/10/bits/stl_map.h:520:37: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ changed in GCC 7.1
  520 |    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
      |          ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  521 |      std::forward_as_tuple(std::move(__k)),
      |      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  522 |      std::tuple<>());
      |      ~~~~~~~~~~~~~~~                 
/usr/include/c++/10/bits/stl_map.h:520:37: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ changed in GCC 7.1
  520 |    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
      |          ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  521 |      std::forward_as_tuple(std::move(__k)),
      |      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  522 |      std::tuple<>());
      |      ~~~~~~~~~~~~~~~                 
[ 42%] Building CXX object CMakeFiles/xmrig-notls.dir/src/Summary.cpp.o
/usr/include/c++/10/bits/stl_map.h: In member function ‘virtual void xmrig::Miner::onTimer(const xmrig::Timer*)’:
/usr/include/c++/10/bits/stl_map.h:520:37: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ changed in GCC 7.1
  520 |    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
      |          ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  521 |      std::forward_as_tuple(std::move(__k)),
      |      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  522 |      std::tuple<>());
      |      ~~~~~~~~~~~~~~~                 
/usr/include/c++/10/bits/stl_map.h:520:37: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ changed in GCC 7.1
  520 |    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
      |          ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  521 |      std::forward_as_tuple(std::move(__k)),
      |      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  522 |      std::tuple<>());
      |      ~~~~~~~~~~~~~~~                 
/usr/include/c++/10/bits/stl_map.h:520:37: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ changed in GCC 7.1
  520 |    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
      |          ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  521 |      std::forward_as_tuple(std::move(__k)),
      |      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  522 |      std::tuple<>());
      |      ~~~~~~~~~~~~~~~                 
/usr/include/c++/10/bits/stl_map.h:520:37: note: parameter passing for argument of type ‘std::_Rb_tree<xmrig::Algorithm::Id, std::pair<const xmrig::Algorithm::Id, double>, std::_Select1st<std::pair<const xmrig::Algorithm::Id, double> >, std::less<xmrig::Algorithm::Id>, std::allocator<std::pair<const xmrig::Algorithm::Id, double> > >::const_iterator’ changed in GCC 7.1
  520 |    __i = _M_t._M_emplace_hint_unique(__i, std::piecewise_construct,
      |          ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  521 |      std::forward_as_tuple(std::move(__k)),
      |      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  522 |      std::tuple<>());
      |      ~~~~~~~~~~~~~~~                 
[ 43%] Building CXX object CMakeFiles/xmrig-notls.dir/src/xmrig.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig-notls.dir/src/hw/api/HwApi.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig-notls.dir/src/hw/dmi/DmiBoard.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig-notls.dir/src/hw/dmi/DmiMemory.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig-notls.dir/src/hw/dmi/DmiReader.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig-notls.dir/src/hw/dmi/DmiTools.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig-notls.dir/src/hw/dmi/DmiReader_unix.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/json/Json_unix.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Platform_unix.cpp.o
In file included from /usr/include/c++/10/vector:72,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/base/tools/String.h:27,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/hw/dmi/DmiBoard.h:25,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/hw/dmi/DmiReader.h:25,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/hw/dmi/DmiReader.cpp:21:
/usr/include/c++/10/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {xmrig::dmi_header*}; _Tp = xmrig::DmiMemory; _Alloc = std::allocator<xmrig::DmiMemory>]’:
/usr/include/c++/10/bits/vector.tcc:426:7: note: parameter passing for argument of type ‘std::vector<xmrig::DmiMemory>::iterator’ changed in GCC 7.1
  426 |       vector<_Tp, _Alloc>::
      |       ^~~~~~~~~~~~~~~~~~~
/usr/include/c++/10/bits/vector.tcc: In member function ‘bool xmrig::DmiReader::_ZN5xmrig9DmiReader6decodeEPh.part.0(uint8_t*)’:
/usr/include/c++/10/bits/vector.tcc:121:21: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<xmrig::DmiMemory*, std::vector<xmrig::DmiMemory> >’ changed in GCC 7.1
  121 |    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
      |    ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 48%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/kernel/Process_unix.cpp.o
[ 49%] Building CXX object CMakeFiles/xmrig-notls.dir/src/App_unix.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/VirtualMemory_unix.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/LinuxMemory.cpp.o
[ 51%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_blake256.c.o
[ 51%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_groestl.c.o
[ 52%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_jh.c.o
[ 53%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/cn/c_skein.c.o
[ 53%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnCtx.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnHash.cpp.o
[ 54%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/HugePagesInfo.cpp.o
In file included from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/crypto/cn/soft_aes.h:31,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/crypto/cn/CryptoNight_arm.h:35,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/crypto/cn/CnHash.cpp:27:
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/crypto/cn/sse2neon.h:122:2: error: #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
  122 | #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
      |  ^~~~~
[ 55%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/MemoryPool.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/Nonce.cpp.o
[ 56%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/common/VirtualMemory.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/aes_hash.cpp.o
In file included from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/crypto/cn/soft_aes.h:31,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/crypto/cn/CryptoNight_arm.h:35,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/crypto/cn/CnHash.cpp:27:
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/crypto/cn/sse2neon.h:7594:9: warning: ‘#pragma GCC pop_options’ without a corresponding ‘#pragma GCC push_options’ [-Wpragmas]
 7594 | #pragma GCC pop_options
      |         ^~~
[ 57%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/allocator.cpp.o
[ 58%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/blake2_generator.cpp.o
[ 59%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/blake2/blake2b.c.o
[ 59%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/bytecode_machine.cpp.o
make[2]: *** [CMakeFiles/xmrig-notls.dir/build.make:1603: CMakeFiles/xmrig-notls.dir/src/crypto/cn/CnHash.cpp.o] Error 1
[ 60%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/dataset.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/instructions_portable.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/randomx.cpp.o
[ 62%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/reciprocal.c.o
[ 62%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/soft_aes.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/superscalar.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/virtual_machine.cpp.o
[ 64%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/virtual_memory.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_compiled_light.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_compiled.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_interpreted_light.cpp.o
[ 66%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/vm_interpreted.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/Rx.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxAlgo.cpp.o
[ 68%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxBasicStorage.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxCache.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxConfig.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxDataset.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxQueue.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/rx/RxVm.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/randomx/jit_compiler_fallback.cpp.o
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/crypto/randomx/jit_compiler_fallback.cpp:31:9: warning: #pragma once in main file
   31 | #pragma once
      |         ^~~~
[ 72%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/argon2/Impl.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/astrobwt/AstroBWT.cpp.o
[ 74%] Building C object CMakeFiles/xmrig-notls.dir/src/crypto/astrobwt/salsa20_ref/salsa20.c.o
[ 74%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/kawpow/KPCache.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig-notls.dir/src/crypto/kawpow/KPHash.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/io/log/backends/SysLog.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig-notls.dir/src/base/net/http/HttpServer.cpp.o
make[2]: Target 'CMakeFiles/xmrig-notls.dir/build' not remade because of errors.
make[1]: *** [CMakeFiles/Makefile2:137: CMakeFiles/xmrig-notls.dir/all] Error 2
make[1]: Target 'all' not remade because of errors.
make: *** [Makefile:103: all] Error 2
make: Target 'default_target' not remade because of errors.


---

using 64 bit kernel:
pi@raspberry:~/SOURCE $ lscpu 
Architecture:                    aarch64
Byte Order:                      Little Endian
CPU(s):                          4
On-line CPU(s) list:             0-3
Thread(s) per core:              1
Core(s) per socket:              4
Socket(s):                       1
Vendor ID:                       ARM
Model:                           3
Model name:                      Cortex-A72
Stepping:                        r0p3
CPU max MHz:                     1800.0000
CPU min MHz:                     600.0000
BogoMIPS:                        108.00
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Vulnerable
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Vulnerable
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected
Flags:                           fp asimd evtstrm crc32 cpuid

**Expected behavior**
Hoping to get a successful build.


# Discussion History
## Spudz76 | 2021-11-15T02:00:24+00:00
aarch64 is `ARM_TARGET=8`

What version of gcc?  Looks like a broken one...

## mglogowski | 2021-11-15T02:01:54+00:00
pi@raspberry:~/Downloads $ gcc --version
gcc (Raspbian 10.2.1-6+rpi1) 10.2.1 20210110
Copyright (C) 2020 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

## mglogowski | 2021-11-15T02:06:21+00:00
tried using 8 in the cmake command. got similar error again:
[ 74%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/cn/CnHash.cpp.o
In file included from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/crypto/cn/soft_aes.h:31,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/crypto/cn/CryptoNight_arm.h:35,
                 from /home/pi/SOURCE/XMRig/xmrig-6.15.3/src/crypto/cn/CnHash.cpp:27:
/home/pi/SOURCE/XMRig/xmrig-6.15.3/src/crypto/cn/sse2neon.h:122:2: error: #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
  122 | #error "Unsupported target. Must be either ARMv7-A+NEON or ARMv8-A."
      |  ^~~~~


## Chrisigamer737 | 2021-11-15T06:13:50+00:00
There is a good video by network chuck on youtube about xmrig on the rpi. You may find that useful.

## Spudz76 | 2021-11-15T11:52:03+00:00
Can't probably hot-swap that CMake option, nuke build folder contents before giving different CMake options for best results.

## mglogowski | 2021-11-15T18:48:07+00:00
i wound up installing ubuntu 21 64bit for arm and everything now works. thx for your assistance. figured it was just os related issues.

# Action History
- Created by: mglogowski | 2021-11-15T01:12:16+00:00
- Closed at: 2021-11-15T18:48:07+00:00
