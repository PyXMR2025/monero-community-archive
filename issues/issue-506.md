---
title: Undefined symbols for architecture x86_64
source_url: https://github.com/xmrig/xmrig/issues/506
author: fogoat
assignees: []
labels: []
created_at: '2018-04-05T21:16:27+00:00'
updated_at: '2018-11-05T13:20:50+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:20:50+00:00'
---

# Original Description
macOS 10.12.6

Any thoughts?

> /xmrig/build$ cmake .. -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=gcc
> -- The C compiler identification is AppleClang 9.0.0.9000039
> -- The CXX compiler identification is AppleClang 9.0.0.9000039
> -- Check for working C compiler: /usr/bin/gcc
> -- Check for working C compiler: /usr/bin/gcc -- works
> -- Detecting C compiler ABI info
> -- Detecting C compiler ABI info - done
> -- Detecting C compile features
> -- Detecting C compile features - done
> -- Check for working CXX compiler: /usr/bin/gcc
> -- Check for working CXX compiler: /usr/bin/gcc -- works
> -- Detecting CXX compiler ABI info
> -- Detecting CXX compiler ABI info - done
> -- Detecting CXX compile features
> -- Detecting CXX compile features - done
> -- Found UV: /usr/local/lib/libuv.a  
> -- Looking for syslog.h
> -- Looking for syslog.h - found
> -- Found MHD: /usr/local/lib/libmicrohttpd.dylib  
> -- Configuring done
> -- Generating done
> -- Build files have been written to: /Users/sunk818/Downloads/xmrig/build


> /xmrig/build$ make
> [ 12%] Built target cpuid
> Scanning dependencies of target xmrig
> [ 14%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
> [ 17%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
> [ 19%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
> [ 21%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
> [ 23%] Building CXX object CMakeFiles/xmrig.dir/src/Console.cpp.o
> [ 25%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.o
> [ 27%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.o
> [ 29%] Building CXX object CMakeFiles/xmrig.dir/src/log/Log.cpp.o
> [ 31%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
> [ 34%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.o
> [ 36%] Building CXX object CMakeFiles/xmrig.dir/src/net/Job.cpp.o
> [ 38%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
> [ 40%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
> [ 42%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/FailoverStrategy.cpp.o
> [ 44%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/SinglePoolStrategy.cpp.o
> [ 46%] Building CXX object CMakeFiles/xmrig.dir/src/net/SubmitResult.cpp.o
> [ 48%] Building CXX object CMakeFiles/xmrig.dir/src/net/Url.cpp.o
> [ 51%] Building CXX object CMakeFiles/xmrig.dir/src/Options.cpp.o
> [ 53%] Building CXX object CMakeFiles/xmrig.dir/src/Platform.cpp.o
> [ 55%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
> [ 57%] Building CXX object CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.o
> [ 59%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
> [ 61%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
> [ 63%] Building CXX object CMakeFiles/xmrig.dir/src/workers/SingleWorker.cpp.o
> [ 65%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
> [ 68%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
> [ 70%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
> [ 72%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
> [ 74%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_mac.cpp.o
> [ 76%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
> [ 78%] Building CXX object CMakeFiles/xmrig.dir/src/Platform_mac.cpp.o
> [ 80%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu.cpp.o
> [ 82%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_keccak.c.o
> [ 85%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
> [ 87%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
> [ 89%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
> [ 91%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
> [ 93%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.o
> [ 95%] Building CXX object CMakeFiles/xmrig.dir/src/log/SysLog.cpp.o
> [ 97%] Building CXX object CMakeFiles/xmrig.dir/src/api/Httpd.cpp.o
> [100%] Linking CXX executable xmrig
> Undefined symbols for architecture x86_64:
>   "std::__1::__vector_base_common<true>::__throw_length_error() const", referenced from:
>       std::__1::enable_if<(__is_forward_iterator<unsigned short*>::value) && (is_constructible<unsigned short, std::__1::iterator_traits<unsigned short*>::reference>::value), void>::type std::__1::vector<unsigned short, std::__1::allocator<unsigned short> >::assign<unsigned short*>(unsigned short*, unsigned short*) in ApiState.cpp.o
>       NetworkState::latency() const in NetworkState.cpp.o
>       void std::__1::vector<unsigned short, std::__1::allocator<unsigned short> >::__push_back_slow_path<unsigned short>(unsigned short&&) in NetworkState.cpp.o
>       void std::__1::vector<ILogBackend*, std::__1::allocator<ILogBackend*> >::__push_back_slow_path<ILogBackend* const&>(ILogBackend* const&&&) in App.cpp.o
>       void std::__1::vector<addrinfo*, std::__1::allocator<addrinfo*> >::__push_back_slow_path<addrinfo* const&>(addrinfo* const&&&) in Client.cpp.o
>       void std::__1::vector<Url*, std::__1::allocator<Url*> >::__push_back_slow_path<Url*>(Url*&&) in DonateStrategy.cpp.o
>       void std::__1::vector<Client*, std::__1::allocator<Client*> >::__push_back_slow_path<Client* const&>(Client* const&&&) in FailoverStrategy.cpp.o
>       ...
>   "std::__1::this_thread::sleep_for(std::__1::chrono::duration<long long, std::__1::ratio<1l, 1000000000l> > const&)", referenced from:
>       DoubleWorker::start() in DoubleWorker.cpp.o
>       SingleWorker::start() in SingleWorker.cpp.o
>   "std::__1::chrono::steady_clock::now()", referenced from:
>       Hashrate::calc(unsigned long, unsigned long) const in Hashrate.cpp.o
>       Worker::storeStats() in Worker.cpp.o
>   "operator delete[](void*)", referenced from:
>       ApiState::genId() in ApiState.cpp.o
>       ApiState::~ApiState() in ApiState.cpp.o
>       ApiState::~ApiState() in ApiState.cpp.o
>       FileLog::onWrite(uv_fs_s*) in FileLog.cpp.o
>       Url::~Url() in Url.cpp.o
>       Url::~Url() in Url.cpp.o
>       Url::operator=(Url const*) in Url.cpp.o
>       ...
>   "operator delete(void*)", referenced from:
>       Api::release() in Api.cpp.o
>       ApiState::~ApiState() in ApiState.cpp.o
>       ApiState::~ApiState() in ApiState.cpp.o
>       ApiState::get(char const*, int*) const in ApiState.cpp.o
>       ApiState::finalize(rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>&) const in ApiState.cpp.o
>       std::__1::enable_if<(__is_forward_iterator<unsigned short*>::value) && (is_constructible<unsigned short, std::__1::iterator_traits<unsigned short*>::reference>::value), void>::type std::__1::vector<unsigned short, std::__1::allocator<unsigned short> >::assign<unsigned short*>(unsigned short*, unsigned short*) in ApiState.cpp.o
>       NetworkState::latency() const in NetworkState.cpp.o
>       ...
>   "operator new[](unsigned long)", referenced from:
>       ApiState::ApiState() in ApiState.cpp.o
>       ApiState::genId() in ApiState.cpp.o
>       ApiState::ApiState() in ApiState.cpp.o
>       FileLog::message(int, char const*, __va_list_tag*) in FileLog.cpp.o
>       Url::parse(char const*) in Url.cpp.o
>       Url::parseIPv6(char const*) in Url.cpp.o
>       Url::url() const in Url.cpp.o
>       ...
>   "operator new(unsigned long)", referenced from:
>       Api::start() in Api.cpp.o
>       ApiState::get(char const*, int*) const in ApiState.cpp.o
>       ApiState::finalize(rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>&) const in ApiState.cpp.o
>       bool rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >::Accept<rapidjson::PrettyWriter<rapidjson::GenericStringBuffer<rapidjson::UTF8<char>, rapidjson::CrtAllocator>, rapidjson::UTF8<char>, rapidjson::UTF8<char>, rapidjson::CrtAllocator, 0u> >(rapidjson::PrettyWriter<rapidjson::GenericStringBuffer<rapidjson::UTF8<char>, rapidjson::CrtAllocator>, rapidjson::UTF8<char>, rapidjson::UTF8<char>, rapidjson::CrtAllocator, 0u>&) const in ApiState.cpp.o
>       std::__1::enable_if<(__is_forward_iterator<unsigned short*>::value) && (is_constructible<unsigned short, std::__1::iterator_traits<unsigned short*>::reference>::value), void>::type std::__1::vector<unsigned short, std::__1::allocator<unsigned short> >::assign<unsigned short*>(unsigned short*, unsigned short*) in ApiState.cpp.o
>       rapidjson::PrettyWriter<rapidjson::GenericStringBuffer<rapidjson::UTF8<char>, rapidjson::CrtAllocator>, rapidjson::UTF8<char>, rapidjson::UTF8<char>, rapidjson::CrtAllocator, 0u>::StartObject() in ApiState.cpp.o
>       rapidjson::PrettyWriter<rapidjson::GenericStringBuffer<rapidjson::UTF8<char>, rapidjson::CrtAllocator>, rapidjson::UTF8<char>, rapidjson::UTF8<char>, rapidjson::CrtAllocator, 0u>::StartArray() in ApiState.cpp.o
>       ...
>   "___cxa_pure_virtual", referenced from:
>       vtable for Worker in Worker.cpp.o
> ld: symbol(s) not found for architecture x86_64
> clang: error: linker command failed with exit code 1 (use -v to see invocation)
> make[2]: *** [xmrig] Error 1
> make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
> make: *** [all] Error 2
> 

# Discussion History
## bs3vcenk | 2018-04-06T09:14:45+00:00
Change `CMAKE_CXX_COMPILER` to `g++`

# Action History
- Created by: fogoat | 2018-04-05T21:16:27+00:00
- Closed at: 2018-11-05T13:20:50+00:00
