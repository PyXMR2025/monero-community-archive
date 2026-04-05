---
title: 'Build Error: error: call to constructor of ''rapidjson::GenericValue<rapidjson::UTF8<char>,
  rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >'' is ambiguous'
source_url: https://github.com/xmrig/xmrig/issues/1581
author: orklar
assignees: []
labels:
- bug
created_at: '2020-03-05T13:12:49+00:00'
updated_at: '2020-03-08T08:17:39+00:00'
type: issue
status: closed
closed_at: '2020-03-08T08:17:39+00:00'
---

# Original Description
**Describe the bug**
When trying to build (using the steps in both basic and advanced build) I get a build error: "error: call to constructor of 'rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >' is ambiguous"

**To Reproduce**
On MacOs Catalina 10.15.3, try and build using the latest version and build instructions.

**Expected behavior**
Succesfull build.

**Required data**
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpContext.cpp.o
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpResponse.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/http/HttpServer.cpp.o
[ 33%] Building CXX object CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o
In file included from .../xmrig/src/base/net/stratum/DaemonClient.cpp:38:
.../xmrig/src/3rdparty/rapidjson/document.h:1351:22: error: call to constructor of 'rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >' is ambiguous
        GenericValue v(value);
                     ^ ~~~~~
.../xmrig/src/3rdparty/rapidjson/document.h:1422:16: note: in instantiation of function template specialization 'rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >::AddMember<unsigned long>'
      requested here
        return AddMember(n, value, allocator);
               ^
.../xmrig/src/base/net/stratum/DaemonClient.cpp:339:16: note: in instantiation of function template specialization 'rapidjson::GenericValue<rapidjson::UTF8<char>, rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >::AddMember<unsigned
      long>' requested here
        params.AddMember("reserve_size", BlobReserveSize, allocator);
               ^
.../xmrig/src/3rdparty/rapidjson/document.h:712:14: note: candidate constructor
    explicit GenericValue(int i) RAPIDJSON_NOEXCEPT : data_() {
             ^
.../xmrig/src/3rdparty/rapidjson/document.h:718:14: note: candidate constructor
    explicit GenericValue(unsigned u) RAPIDJSON_NOEXCEPT : data_() {
             ^
.../xmrig/src/3rdparty/rapidjson/document.h:724:14: note: candidate constructor
    explicit GenericValue(int64_t i64) RAPIDJSON_NOEXCEPT : data_() {
             ^
.../xmrig/src/3rdparty/rapidjson/document.h:739:14: note: candidate constructor
    explicit GenericValue(uint64_t u64) RAPIDJSON_NOEXCEPT : data_() {
             ^
.../xmrig/src/3rdparty/rapidjson/document.h:751:14: note: candidate constructor
    explicit GenericValue(double d) RAPIDJSON_NOEXCEPT : data_() { data_.n.d = d; data_.f.flags = kNumberDoubleFlag; }
             ^
.../xmrig/src/3rdparty/rapidjson/document.h:754:14: note: candidate constructor
    explicit GenericValue(float f) RAPIDJSON_NOEXCEPT : data_() { data_.n.d = static_cast<double>(f); data_.f.flags = kNumberDoubleFlag; }
             ^
1 error generated.
make[2]: *** [CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2

 - OS: MacOS 10.15.3 Catalina

# Discussion History
## Avatar1912-Sam | 2020-03-06T06:23:06+00:00
I have the same problem with the new build I only get 36% before this error occurs:

[ 36%] Building CXX object CMakeFiles/xmrig.dir/src/backend/common/Workers.cpp.o
In file included from /Users/saxxx/xmrig/src/base/net/stratum/DaemonClient.cpp:38:
/Users/sxxx/xmrig/src/3rdparty/rapidjson/document.h:1351:22: error: 
      call to constructor of 'rapidjson::GenericValue<rapidjson::UTF8<char>,
      rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator> >' is ambiguous
        GenericValue v(value);
                     ^ ~~~~~
/Users/sxxx/xmrig/src/3rdparty/rapidjson/document.h:1422:16: note: 
      in instantiation of function template specialization
      'rapidjson::GenericValue<rapidjson::UTF8<char>,
      rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>
      >::AddMember<unsigned long>' requested here
        return AddMember(n, value, allocator);
               ^
/Users/sxxx/xmrig/src/base/net/stratum/DaemonClient.cpp:339:16: note: 
      in instantiation of function template specialization
      'rapidjson::GenericValue<rapidjson::UTF8<char>,
      rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>
      >::AddMember<unsigned long>' requested here
        params.AddMember("reserve_size", BlobReserveSize, allocator);
               ^
/Users/sxxxx/xmrig/src/3rdparty/rapidjson/document.h:712:14: note: 
      candidate constructor
    explicit GenericValue(int i) RAPIDJSON_NOEXCEPT : data_() {
             ^
/Users/sxxx/xmrig/src/3rdparty/rapidjson/document.h:718:14: note: 
      candidate constructor
    explicit GenericValue(unsigned u) RAPIDJSON_NOEXCEPT : data_() {
             ^
/Users/sxxx/xmrig/src/3rdparty/rapidjson/document.h:724:14: note: 
      candidate constructor
    explicit GenericValue(int64_t i64) RAPIDJSON_NOEXCEPT : data_() {
             ^
/Users/sxxxx/xmrig/src/3rdparty/rapidjson/document.h:739:14: note: 
      candidate constructor
    explicit GenericValue(uint64_t u64) RAPIDJSON_NOEXCEPT : data_() {
             ^
/Users/sxxxx/xmrig/src/3rdparty/rapidjson/document.h:751:14: note: 
      candidate constructor
    explicit GenericValue(double d) RAPIDJSON_NOEXCEPT : data_() { data_...
             ^
/Users/sxxx/xmrig/src/3rdparty/rapidjson/document.h:754:14: note: 
      candidate constructor
    explicit GenericValue(float f) RAPIDJSON_NOEXCEPT : data_() { data_....
             ^
1 error generated.
make[2]: *** [CMakeFiles/xmrig.dir/src/base/net/stratum/DaemonClient.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
xxx@Saschas-MacBook-Pro build % 

## xmrig | 2020-03-06T07:09:23+00:00
Fixed in master and dev branches and fix will be included to v5.8.2 release.
Thank you.

## xmrig | 2020-03-06T07:40:28+00:00
https://github.com/xmrig/xmrig/releases/tag/v5.8.2

## Avatar1912-Sam | 2020-03-06T09:23:34+00:00
Works now Thanks :-) 

# Action History
- Created by: orklar | 2020-03-05T13:12:49+00:00
- Closed at: 2020-03-08T08:17:39+00:00
