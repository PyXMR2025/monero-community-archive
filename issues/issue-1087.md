---
title: tests don't build in msys/mingw on win64 because gtest fails to build
source_url: https://github.com/monero-project/monero/issues/1087
author: radfish
assignees: []
labels: []
created_at: '2016-09-17T20:32:08+00:00'
updated_at: '2017-09-05T16:42:24+00:00'
type: issue
status: closed
closed_at: '2017-09-05T16:42:24+00:00'
---

# Original Description
Just to document, I don't really care about it. By default top-level targets don't build tests.

Sidenote: there is no gtest package for msys, so can't test that.

``````
redfish@winpond MINGW64 ~/monero/build
$ cmake -G "MSYS Makefiles" -DARCH="x86-64" -D STATIC=ON -DCMAKE_TOOLCHAIN_FILE=../cmake/64-bit-toolchain.cmake -D MSYS2_FOLDER=c:/msys64 -DCMAKE_BUILD_TYPE=Debug -DBUILD_TESTS=ON ..```
$ make -j2 2>&1 VERBOSE=1 | tee -a build.log   
``````

```
In file included from C:/msys64/home/redfish/monero/tests/gtest/src/gtest-all.cc:45:0:
C:/msys64/home/redfish/monero/tests/gtest/src/gtest-port.cc: In constructor 'testing::internal::ThreadWithParamBase::ThreadWithParamBase(testing::internal::ThreadWithParamBase::Runnable*, testing::internal::Notification*)':
C:/msys64/home/redfish/monero/tests/gtest/src/gtest-port.cc:377:9: error: class 'testing::internal::ThreadWithParamBase' does not have any field named 'thread_'
       : thread_(ThreadWithParamSupport::CreateThread(runnable,
         ^~~~~~~
In file included from C:/msys64/home/redfish/monero/tests/gtest/include/gtest/internal/gtest-internal.h:40:0,
                 from C:/msys64/home/redfish/monero/tests/gtest/include/gtest/gtest.h:58,
                 from C:/msys64/home/redfish/monero/tests/gtest/src/gtest-all.cc:39:
C:/msys64/home/redfish/monero/tests/gtest/src/gtest-port.cc: In member function 'void testing::internal::ThreadWithParamBase::Join()':
C:/msys64/home/redfish/monero/tests/gtest/src/gtest-port.cc:386:38: error: 'thread_' was not declared in this scope
   GTEST_CHECK_(::WaitForSingleObject(thread_.Get(), INFINITE) == WAIT_OBJECT_0)
                                      ^
C:/msys64/home/redfish/monero/tests/gtest/include/gtest/internal/gtest-port.h:1297:37: note: in definition of macro 'GTEST_CHECK_'
     if (::testing::internal::IsTrue(condition)) \
                                     ^~~~~~~~~
make[2]: *** [tests/gtest/CMakeFiles/gtest.dir/build.make:63: tests/gtest/CMakeFiles/gtest.dir/src/gtest-all.cc.obj] Error 1
```


# Discussion History
## danrmiller | 2016-10-11T16:18:14+00:00
> Sidenote: there is no gtest package for msys, so can't test that.

The package is called mingw-w64-x86_64-gtest. The tests run using that package for me, and I get the same error as you with the vendored lib.


## radfish | 2016-11-18T23:48:26+00:00
@danrmiller Ok, gtest must have been added or I missed it (is there an i686 package too?). Did you have to change CMakeLists.txt to build against the gtest installed via the package? I assume not. If so, I'll update the list of deps in README and close this.


## danrmiller | 2016-11-19T02:33:30+00:00
Yes there is a mingw-w64-i686-gtest package too. You don't have to change anything, the existing cmake/make setup finds it.


## luigi1111 | 2016-12-15T17:15:44+00:00
Seems resolved by installing the required package(s). @radfish please advise if untrue.

## danrmiller | 2016-12-19T23:58:21+00:00
@luigi1111 We can't use the msys2 pacman packages successfully anymore on 64-bit windows, so included vendored libs not working is an issue; The 64-bit windows build is failing https://build.getmonero.org/builders/monero-static-win64/builds/463 with this error:

`In file included from C:/msys64/mingw64/include/gtest/gtest.h:58:0,
                 from C:/msys64/home/vagrant/slave/monero-static-win64/build/tests/unit_tests/http_auth.cpp:29:
C:/msys64/home/vagrant/slave/monero-static-win64/build/tests/unit_tests/http_auth.cpp: In member function 'virtual void HTTP_Auth_MissingAuth_Test::TestBody()':
C:/msys64/home/vagrant/slave/monero-static-win64/build/tests/unit_tests/http_auth.cpp:222:3: error: no matching function for call to 'testing::AssertionResult::AssertionResult(boost::optional<epee::net_utils::http::http_response_info>)'
   EXPECT_TRUE(auth.get_response(epee::net_utils::http::http_request_info{}));`

@vtnerd mentions here https://github.com/monero-project/monero/pull/1444#issuecomment-266921865 that "The build bots are using an older GTest header than the one included with the project."

On the 64-bit windows machine we are using mingw-w64-x86_64-gtest 1.7.0-1. The monero README lists the minimum version of gtest as 1.5. 
 
So on 64-bit windows we cannot build the tests with the vendored lib or the package.

## vtnerd | 2016-12-20T00:13:47+00:00
I was looking at this earlier today. Currently, GTest 1.8 is needed because of the aforementioned patch. I see no reason to increase the necessary version, so I was planning to make a few changes to the relevant test cases to work with older GTest versions.

## luigi1111 | 2016-12-20T23:40:06+00:00
Ok, reopening.

## vtnerd | 2016-12-21T00:17:51+00:00
I think (and hope) [this](https://github.com/monero-project/monero/pull/1475) fixed it. 

## danrmiller | 2016-12-21T01:08:58+00:00
Yes works now thanks. I like to keep luigi1111 busy.

## danrmiller | 2017-09-05T16:41:21+00:00
+resolved

# Action History
- Created by: radfish | 2016-09-17T20:32:08+00:00
- Closed at: 2017-09-05T16:42:24+00:00
