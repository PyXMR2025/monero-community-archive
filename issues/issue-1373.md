---
title: sudo make error
source_url: https://github.com/monero-project/monero/issues/1373
author: tanshaoliang
assignees: []
labels: []
created_at: '2016-11-24T08:51:36+00:00'
updated_at: '2016-12-14T02:44:40+00:00'
type: issue
status: closed
closed_at: '2016-12-06T07:54:42+00:00'
---

# Original Description
error msg is:
[ 25%] Building CXX object src/common/CMakeFiles/obj_common.dir/thread_group.cpp.o
/data/mbitmonero/monero/src/common/thread_group.cpp: In constructor ‘tools::thread_group::data::data(std::size_t)’:
/data/mbitmonero/monero/src/common/thread_group.cpp:59:15: error: no matching function for call to ‘tools::thread_group::data::node::node(<brace-enclosed initializer list>)’
   , stop(false) {
               ^
/data/mbitmonero/monero/src/common/thread_group.cpp:59:15: note: candidate is:
In file included from /data/mbitmonero/monero/src/common/thread_group.cpp:28:0:
/data/mbitmonero/monero/src/common/thread_group.h:101:12: note: tools::thread_group::data::node::node(tools::thread_group::data::node&&)
     struct node {
            ^
/data/mbitmonero/monero/src/common/thread_group.h:101:12: note:   no known conversion for argument 1 from ‘std::nullptr_t’ to ‘tools::thread_group::data::node&&’
/data/mbitmonero/monero/src/common/thread_group.cpp: In member function ‘void tools::thread_group::data::dispatch(std::function<void()>)’:
/data/mbitmonero/monero/src/common/thread_group.cpp:149:67: error: no matching function for call to ‘tools::thread_group::data::node::node(<brace-enclosed initializer list>)’
   std::unique_ptr<work> latest(new work{std::move(f), node{nullptr}});
                                                                   ^
/data/mbitmonero/monero/src/common/thread_group.cpp:149:67: note: candidate is:
In file included from /data/mbitmonero/monero/src/common/thread_group.cpp:28:0:
/data/mbitmonero/monero/src/common/thread_group.h:101:12: note: tools::thread_group::data::node::node(tools::thread_group::data::node&&)
     struct node {
            ^
/data/mbitmonero/monero/src/common/thread_group.h:101:12: note:   no known conversion for argument 1 from ‘std::nullptr_t’ to ‘tools::thread_group::data::node&&’
/data/mbitmonero/monero/src/common/thread_group.cpp:149:68: error: no matching function for call to ‘tools::thread_group::data::work::work(<brace-enclosed initializer list>)’
   std::unique_ptr<work> latest(new work{std::move(f), node{nullptr}});
                                                                    ^
/data/mbitmonero/monero/src/common/thread_group.cpp:149:68: note: candidate is:
In file included from /data/mbitmonero/monero/src/common/thread_group.cpp:28:0:
/data/mbitmonero/monero/src/common/thread_group.h:106:12: note: tools::thread_group::data::work::work(tools::thread_group::data::work&&)
     struct work {
            ^
/data/mbitmonero/monero/src/common/thread_group.h:106:12: note:   candidate expects 1 argument, 2 provided
make[3]: *** [src/common/CMakeFiles/obj_common.dir/thread_group.cpp.o] Error 1
make[3]: Leaving directory `/data/mbitmonero/monero/build/release'
make[2]: *** [src/common/CMakeFiles/obj_common.dir/all] Error 2
make[2]: Leaving directory `/data/mbitmonero/monero/build/release'
make[1]: *** [all] Error 2
make[1]: Leaving directory `/data/mbitmonero/monero/build/release'
make: *** [release-all] Error 2
---------------------------------
how to solve this problem? 
the more informations:
had modify the CMakelist.txt like this:

SET(CMAKE_INCLUDE_PATH ${CMAKE_INCLUDE_PATH} "/usr/include/boost")
SET(CMAKE_LIBRARY_PATH ${CMAKE_LIBRARY_PATH} "/usr/local/lib")

find_package(Boost)
----------------------------------
thanks.

# Discussion History
## moneromooo-monero | 2016-11-24T09:25:16+00:00
It is unexpected, and likely wrong, that you have boost headers in /usr/include and libraries in /usr/local/lib. Usually, /usr and /usr/local are two separate prefixes.
I would double check you're not using two mismatched boost versions.

## tanshaoliang | 2016-11-24T09:48:13+00:00
@moneromooo-monero thanks, you may be right. 
sudo apt-get install libboost-all-dev, missing the lib dir.  so, i wget an boost 1.58....
now, i try uninstall boost, and compile & install it again.

## ghost | 2016-11-24T13:24:18+00:00
If you look in the README.md under the section on the Raspberry Pi 2, I've included the steps to build and install boost from scratch. 

## tanshaoliang | 2016-11-28T08:50:54+00:00
@NanoAkron thanks, buy, the same error happened after reinstall the boost1.62.
err msg was:
/data/src/monero/src/common/thread_group.cpp:59:15: error: no matching function for call to ‘tools::thread_group::data::node::node(<brace-enclosed initializer list>)’
   , stop(false) {
               ^
/data/src/monero/src/common/thread_group.cpp:59:15: note: candidate is:
In file included from /data/src/monero/src/common/thread_group.cpp:28:0:
--------------------------------------------------------------------------------------------
the machine evironment is:
     os: Ubuntu 14.04.5 LTS
     cmake:3.2.2
     gcc:4.8
     boost:1.62 path:/usr/local
monero make print info:
root@VM-19-2-ubuntu:/data/src/monero# make
mkdir -p build/release
cd build/release && cmake -D BUILD_TESTS=ON -D CMAKE_BUILD_TYPE=release ../.. && make
-- Could not find DEVELOPER_LOCAL_TOOLS in env (not required)
-- BOOST_IGNORE_SYSTEM_PATHS defaults to OFF
-- Could not find DEVELOPER_LIBUNBOUND_OLD in env (not required)
-- Building for a 64-bit system
-- Building internal libraries as static
-- Could not find DATABASE in env (not required unless you want to change database type from default: lmdb)
-- Using LMDB as default DB type
-- Stack trace on exception enabled
-- Detecting version of miniupnpc in path: /usr/include/miniupnpc
-- Found miniupnpc version is pre v1.7
-- Using miniupnpc from local source tree (/external/miniupnpc)
-- Looking for libunbound
-- Found libunbound include (unbound.h) in /usr/include
-- Found libunbound shared library
-- Using 64-bit LMDB from source tree
-- Building on x86_64 for native
-- AES support enabled
-- Found Boost Version: 106200
-- Found Git: /usr/bin/git
-- Could NOT find GTest (missing:  GTEST_LIBRARY GTEST_MAIN_LIBRARY) 
-- GTest not found on the system: will use GTest bundled with this source
-- Configuring done
-- Generating done
-- Build files have been written to: /data/src/monero/build/release
------------------------------------------------------------------------------------
did somethting wrong ?

## moneromooo-monero | 2016-11-29T15:26:55+00:00
Looking at the code, it looks like the node struct had its default ctor deleted, and thread_group has a node member, so it needs intializing. I do not understand why this should work, I'll ask the author to have a look. Possibly it's legal and you've a too old compiler (current stated min version is 4.7.3, which might need bumping, or the code rearranging)

## vtnerd | 2016-11-30T05:01:03+00:00
This is failing on the usage of [aggregate initialization](http://en.cppreference.com/w/cpp/language/aggregate_initialization). This should be valid C++11 - Clang 3.1+ and Gcc 4.9+ accept it. If there is no user provided constructor, the struct can be initialized like a C-struct by member order, with unspecified members being value initialized.

Deleting the default constructor doesn't add much here because `unique_ptr` has user-provided constructors, and therefore is not a trivial default constructor. I got in the habit of marking the default constructor deleted because if the struct met all of the requirements for a trival default constructor, it meant the members could easily be uninitialized:

```c++
struct trivial_default_constructor {
   trivial_default_constructor() = delete;
   int foo;
   bool bar;
};
int main() {
  trivial_default_constructor uninitialized_members; // compiler error due to deletion!
  return 0;
}
```

So it was a quick/lazy way of ensuring all members were initialized, without having to specify any constructors. And default move/copy constructors are still generated by the compiler too.

Anyway, the `=delete()` can safely be removed in this instance. Does anyone have access to 4.7.3 gcc to verify that it builds? I have a Ubuntu 14.04 VM already, but has nothing related to monero on it. Will verify tomorrow if no one else has.

## vtnerd | 2016-12-01T03:07:53+00:00
@moneromooo-monero  may have  to consider increasing the minimum gcc version. That version does not have `std::map::emplace` or `std::unordered_map::emplace` which are used in `blockchain.cpp`. A bug report suggests these were added in gcc 4.8.

Edit: removed "we" from first sentence, as this is definitely not my decision.

## tanshaoliang | 2016-12-01T04:06:18+00:00
thanks all of you.
now, i solve this problem by checkout version v1.0.0 monero coding version.
i shouldnt get development version from git.@@!

## moneromooo-monero | 2016-12-11T14:01:21+00:00
This got forgot a bit, so I did it: https://github.com/monero-project/monero/pull/1431

vtnerd, please confirm this is correct. This will cause a default ctor to be generated, but should be fine AFAICT.

## vtnerd | 2016-12-14T02:44:40+00:00
Whoops, replied to this in the pull request. There should still be compilation issues in blockchain.cpp.

# Action History
- Created by: tanshaoliang | 2016-11-24T08:51:36+00:00
- Closed at: 2016-12-06T07:54:42+00:00
