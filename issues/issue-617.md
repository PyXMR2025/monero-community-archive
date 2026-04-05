---
title: GCC 8.1.0 warnings.
source_url: https://github.com/xmrig/xmrig/issues/617
author: k0ste
assignees: []
labels: []
created_at: '2018-05-08T03:30:11+00:00'
updated_at: '2018-06-17T18:08:29+00:00'
type: issue
status: closed
closed_at: '2018-06-17T18:08:29+00:00'
---

# Original Description
```make
-- The C compiler identification is GNU 8.1.0
-- The CXX compiler identification is GNU 8.1.0
-- Check for working C compiler: /usr/bin/gcc
-- Check for working C compiler: /usr/bin/gcc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/g++
-- Check for working CXX compiler: /usr/bin/g++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found UV: /usr/lib/libuv.so  
-- Looking for syslog.h
-- Looking for syslog.h - found
-- Found MHD: /usr/lib/libmicrohttpd.so  
-- Configuring done
-- Generating done
-- Build files have been written to: /home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/build
Scanning dependencies of target cpuid
[  1%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/cpuid_main.c.o
[  3%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/asm-bits.c.o
[  5%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_amd.c.o
[  7%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/recog_intel.c.o
[  9%] Building C object src/3rdparty/libcpuid/CMakeFiles/cpuid.dir/libcpuid_util.c.o
[ 11%] Linking C static library libcpuid.a
[ 11%] Built target cpuid
Scanning dependencies of target xmrig
[ 13%] Building CXX object CMakeFiles/xmrig.dir/src/core/Config.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
[ 19%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/CommonConfig.cpp.o
[ 21%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigLoader.cpp.o
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/common/config/ConfigLoader.cpp:43:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h: In instantiation of ‘void rapidjson::GenericValue<Encoding, Allocator>::SetObjectRaw(rapidjson::GenericValue<Encoding, Allocator>::Member*, rapidjson::SizeType, Allocator&) [with Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; rapidjson::GenericValue<Encoding, Allocator>::Member = rapidjson::GenericMember<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >; rapidjson::SizeType = unsigned int]’:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:2363:9:   required from ‘bool rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::EndObject(rapidjson::SizeType) [with Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; StackAllocator = rapidjson::CrtAllocator; rapidjson::SizeType = unsigned int]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/reader.h:1736:18:   required from ‘rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::IterativeParsingState rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::Transit(rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::IterativeParsingState, rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::Token, rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::IterativeParsingState, InputStream&, Handler&) [with unsigned int parseFlags = 160; InputStream = rapidjson::FileReadStream; Handler = rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>; SourceEncoding = rapidjson::UTF8<char>; TargetEncoding = rapidjson::UTF8<char>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/reader.h:1832:58:   required from ‘rapidjson::ParseResult rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::IterativeParse(InputStream&, Handler&) [with unsigned int parseFlags = 160; InputStream = rapidjson::FileReadStream; Handler = rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>; SourceEncoding = rapidjson::UTF8<char>; TargetEncoding = rapidjson::UTF8<char>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/reader.h:487:46:   required from ‘rapidjson::ParseResult rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::Parse(InputStream&, Handler&) [with unsigned int parseFlags = 160; InputStream = rapidjson::FileReadStream; Handler = rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>; SourceEncoding = rapidjson::UTF8<char>; TargetEncoding = rapidjson::UTF8<char>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:2159:22:   required from ‘rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>& rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::ParseStream(InputStream&) [with unsigned int parseFlags = 160; SourceEncoding = rapidjson::UTF8<char>; InputStream = rapidjson::FileReadStream; Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:2185:70:   required from ‘rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>& rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::ParseStream(InputStream&) [with InputStream = rapidjson::FileReadStream; Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/common/config/ConfigLoader.cpp:211:23:   required from here
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:1952:24: warning: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of type ‘rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >::Member’ {aka ‘struct rapidjson::GenericMember<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >’} with no trivial copy-assignment; use copy-assignment instead [-Wclass-memaccess]
             std::memcpy(m, members, count * sizeof(Member));
             ~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/common/config/ConfigLoader.cpp:43:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:71:8: note: ‘rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >::Member’ {aka ‘struct rapidjson::GenericMember<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >’} declared here
 struct GenericMember {
        ^~~~~~~~~~~~~
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/common/config/ConfigLoader.cpp:43:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h: In instantiation of ‘void rapidjson::GenericValue<Encoding, Allocator>::SetArrayRaw(rapidjson::GenericValue<Encoding, Allocator>*, rapidjson::SizeType, Allocator&) [with Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; rapidjson::SizeType = unsigned int]’:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:2371:9:   required from ‘bool rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::EndArray(rapidjson::SizeType) [with Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; StackAllocator = rapidjson::CrtAllocator; rapidjson::SizeType = unsigned int]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/reader.h:1766:18:   required from ‘rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::IterativeParsingState rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::Transit(rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::IterativeParsingState, rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::Token, rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::IterativeParsingState, InputStream&, Handler&) [with unsigned int parseFlags = 160; InputStream = rapidjson::FileReadStream; Handler = rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>; SourceEncoding = rapidjson::UTF8<char>; TargetEncoding = rapidjson::UTF8<char>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/reader.h:1832:58:   required from ‘rapidjson::ParseResult rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::IterativeParse(InputStream&, Handler&) [with unsigned int parseFlags = 160; InputStream = rapidjson::FileReadStream; Handler = rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>; SourceEncoding = rapidjson::UTF8<char>; TargetEncoding = rapidjson::UTF8<char>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/reader.h:487:46:   required from ‘rapidjson::ParseResult rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::Parse(InputStream&, Handler&) [with unsigned int parseFlags = 160; InputStream = rapidjson::FileReadStream; Handler = rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>; SourceEncoding = rapidjson::UTF8<char>; TargetEncoding = rapidjson::UTF8<char>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:2159:22:   required from ‘rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>& rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::ParseStream(InputStream&) [with unsigned int parseFlags = 160; SourceEncoding = rapidjson::UTF8<char>; InputStream = rapidjson::FileReadStream; Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:2185:70:   required from ‘rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>& rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::ParseStream(InputStream&) [with InputStream = rapidjson::FileReadStream; Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/common/config/ConfigLoader.cpp:211:23:   required from here
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:1939:24: warning: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of type ‘class rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >’ with no trivial copy-assignment; use copy-assignment or copy-initialization instead [-Wclass-memaccess]
             std::memcpy(e, values, count * sizeof(GenericValue));
             ~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:540:7: note: ‘class rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >’ declared here
 class GenericValue {
       ^~~~~~~~~~~~
[ 23%] Building CXX object CMakeFiles/xmrig.dir/src/common/config/ConfigWatcher.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/common/Console.cpp.o
[ 26%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/Algorithm.cpp.o
[ 28%] Building CXX object CMakeFiles/xmrig.dir/src/common/crypto/keccak.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/ConsoleLog.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/FileLog.cpp.o
[ 34%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/Log.cpp.o
[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Client.cpp.o
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/common/net/Client.cpp:36:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h: In instantiation of ‘void rapidjson::GenericValue<Encoding, Allocator>::SetObjectRaw(rapidjson::GenericValue<Encoding, Allocator>::Member*, rapidjson::SizeType, Allocator&) [with Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; rapidjson::GenericValue<Encoding, Allocator>::Member = rapidjson::GenericMember<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >; rapidjson::SizeType = unsigned int]’:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:2363:9:   required from ‘bool rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::EndObject(rapidjson::SizeType) [with Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; StackAllocator = rapidjson::CrtAllocator; rapidjson::SizeType = unsigned int]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/reader.h:1736:18:   required from ‘rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::IterativeParsingState rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::Transit(rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::IterativeParsingState, rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::Token, rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::IterativeParsingState, InputStream&, Handler&) [with unsigned int parseFlags = 161; InputStream = rapidjson::GenericInsituStringStream<rapidjson::UTF8<char> >; Handler = rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>; SourceEncoding = rapidjson::UTF8<char>; TargetEncoding = rapidjson::UTF8<char>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/reader.h:1832:58:   required from ‘rapidjson::ParseResult rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::IterativeParse(InputStream&, Handler&) [with unsigned int parseFlags = 161; InputStream = rapidjson::GenericInsituStringStream<rapidjson::UTF8<char> >; Handler = rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>; SourceEncoding = rapidjson::UTF8<char>; TargetEncoding = rapidjson::UTF8<char>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/reader.h:487:46:   required from ‘rapidjson::ParseResult rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::Parse(InputStream&, Handler&) [with unsigned int parseFlags = 161; InputStream = rapidjson::GenericInsituStringStream<rapidjson::UTF8<char> >; Handler = rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>; SourceEncoding = rapidjson::UTF8<char>; TargetEncoding = rapidjson::UTF8<char>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:2159:22:   required from ‘rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>& rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::ParseStream(InputStream&) [with unsigned int parseFlags = 161; SourceEncoding = rapidjson::UTF8<char>; InputStream = rapidjson::GenericInsituStringStream<rapidjson::UTF8<char> >; Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:2175:62:   required from ‘rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>& rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::ParseStream(InputStream&) [with unsigned int parseFlags = 161; InputStream = rapidjson::GenericInsituStringStream<rapidjson::UTF8<char> >; Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:2200:58:   required from ‘rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>& rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::ParseInsitu(rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::Ch*) [with unsigned int parseFlags = 160; Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; StackAllocator = rapidjson::CrtAllocator; rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::Ch = char]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:2208:47:   required from ‘rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>& rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::ParseInsitu(rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::Ch*) [with Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; StackAllocator = rapidjson::CrtAllocator; rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::Ch = char]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/common/net/Client.cpp:523:29:   required from here
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:1952:24: warning: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of type ‘rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >::Member’ {aka ‘struct rapidjson::GenericMember<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >’} with no trivial copy-assignment; use copy-assignment instead [-Wclass-memaccess]
             std::memcpy(m, members, count * sizeof(Member));
             ~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/common/net/Client.cpp:36:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:71:8: note: ‘rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >::Member’ {aka ‘struct rapidjson::GenericMember<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >’} declared here
 struct GenericMember {
        ^~~~~~~~~~~~~
In file included from /home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/common/net/Client.cpp:36:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h: In instantiation of ‘void rapidjson::GenericValue<Encoding, Allocator>::SetArrayRaw(rapidjson::GenericValue<Encoding, Allocator>*, rapidjson::SizeType, Allocator&) [with Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; rapidjson::SizeType = unsigned int]’:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:2371:9:   required from ‘bool rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::EndArray(rapidjson::SizeType) [with Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; StackAllocator = rapidjson::CrtAllocator; rapidjson::SizeType = unsigned int]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/reader.h:1766:18:   required from ‘rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::IterativeParsingState rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::Transit(rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::IterativeParsingState, rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::Token, rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::IterativeParsingState, InputStream&, Handler&) [with unsigned int parseFlags = 161; InputStream = rapidjson::GenericInsituStringStream<rapidjson::UTF8<char> >; Handler = rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>; SourceEncoding = rapidjson::UTF8<char>; TargetEncoding = rapidjson::UTF8<char>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/reader.h:1832:58:   required from ‘rapidjson::ParseResult rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::IterativeParse(InputStream&, Handler&) [with unsigned int parseFlags = 161; InputStream = rapidjson::GenericInsituStringStream<rapidjson::UTF8<char> >; Handler = rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>; SourceEncoding = rapidjson::UTF8<char>; TargetEncoding = rapidjson::UTF8<char>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/reader.h:487:46:   required from ‘rapidjson::ParseResult rapidjson::GenericReader<SourceEncoding, TargetEncoding, StackAllocator>::Parse(InputStream&, Handler&) [with unsigned int parseFlags = 161; InputStream = rapidjson::GenericInsituStringStream<rapidjson::UTF8<char> >; Handler = rapidjson::GenericDocument<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>, rapidjson::CrtAllocator>; SourceEncoding = rapidjson::UTF8<char>; TargetEncoding = rapidjson::UTF8<char>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:2159:22:   required from ‘rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>& rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::ParseStream(InputStream&) [with unsigned int parseFlags = 161; SourceEncoding = rapidjson::UTF8<char>; InputStream = rapidjson::GenericInsituStringStream<rapidjson::UTF8<char> >; Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:2175:62:   required from ‘rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>& rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::ParseStream(InputStream&) [with unsigned int parseFlags = 161; InputStream = rapidjson::GenericInsituStringStream<rapidjson::UTF8<char> >; Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; StackAllocator = rapidjson::CrtAllocator]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:2200:58:   required from ‘rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>& rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::ParseInsitu(rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::Ch*) [with unsigned int parseFlags = 160; Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; StackAllocator = rapidjson::CrtAllocator; rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::Ch = char]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:2208:47:   required from ‘rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>& rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::ParseInsitu(rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::Ch*) [with Encoding = rapidjson::UTF8<char>; Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>; StackAllocator = rapidjson::CrtAllocator; rapidjson::GenericDocument<Encoding, Allocator, StackAllocator>::Ch = char]’
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/common/net/Client.cpp:523:29:   required from here
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:1939:24: warning: ‘void* memcpy(void*, const void*, size_t)’ writing to an object of type ‘class rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >’ with no trivial copy-assignment; use copy-assignment or copy-initialization instead [-Wclass-memaccess]
             std::memcpy(e, values, count * sizeof(GenericValue));
             ~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/3rdparty/rapidjson/document.h:540:7: note: ‘class rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >’ declared here
 class GenericValue {
       ^~~~~~~~~~~~
[ 38%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Job.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/Pool.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/FailoverStrategy.cpp.o
[ 44%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/strategies/SinglePoolStrategy.cpp.o
[ 46%] Building CXX object CMakeFiles/xmrig.dir/src/common/net/SubmitResult.cpp.o
[ 48%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/core/Controller.cpp.o
[ 51%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
[ 53%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 59%] Building CXX object CMakeFiles/xmrig.dir/src/workers/CpuThread.cpp.o
[ 61%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
[ 63%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/workers/MultiWorker.cpp.o
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
[ 69%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
[ 71%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 73%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/common/Platform_unix.cpp.o
[ 76%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o
[ 78%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu.cpp.o
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/Cpu.cpp: In static member function ‘static void Cpu::initCommon()’:
/home/k0ste/sandbox/AUR/xmrig/src/xmrig-2.6.2/src/Cpu.cpp:90:12: warning: ‘char* strncpy(char*, const char*, size_t)’ output may be truncated copying 63 bytes from a string of length 63 [-Wstringop-truncation]
     strncpy(m_brand, data.brand_str, sizeof(m_brand) - 1);
     ~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[ 82%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[ 84%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[ 86%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[ 88%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[ 90%] Building CXX object CMakeFiles/xmrig.dir/src/common/log/SysLog.cpp.o
[ 92%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
[ 94%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiRouter.cpp.o
[ 96%] Building CXX object CMakeFiles/xmrig.dir/src/common/api/Httpd.cpp.o
[ 98%] Building CXX object CMakeFiles/xmrig.dir/src/common/api/HttpRequest.cpp.o
[100%] Linking CXX executable xmrig
[100%] Built target xmrig
```

# Discussion History
## L1LjSHX | 2018-05-31T15:42:43+00:00
all good

# Action History
- Created by: k0ste | 2018-05-08T03:30:11+00:00
- Closed at: 2018-06-17T18:08:29+00:00
