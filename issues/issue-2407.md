---
title: Failed to compile on Centos 6.9
source_url: https://github.com/monero-project/monero/issues/2407
author: bvort
assignees: []
labels: []
created_at: '2017-09-07T07:17:56+00:00'
updated_at: '2017-09-08T01:55:03+00:00'
type: issue
status: closed
closed_at: '2017-09-08T01:55:03+00:00'
---

# Original Description
[ 92%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/epee_utils.cpp.o
In file included from /opt/monero/tests/gtest/include/gtest/gtest.h:1878:0,
                 from /opt/monero/tests/unit_tests/epee_utils.cpp:33:
/opt/monero/tests/unit_tests/epee_utils.cpp: In member function ‘virtual void StringTools_GetIpInt32_Test::TestBody()’:
/opt/monero/tests/unit_tests/epee_utils.cpp:392:13: error: statement-expressions are not allowed outside functions nor in template-argument lists
   EXPECT_EQ(htonl(1), ip);
             ^
/opt/monero/tests/unit_tests/epee_utils.cpp:392:3: error: template argument 1 is invalid
   EXPECT_EQ(htonl(1), ip);
   ^
/opt/monero/tests/unit_tests/epee_utils.cpp:395:13: error: statement-expressions are not allowed outside functions nor in template-argument lists
   EXPECT_EQ(htonl(0x1000001), ip);
             ^
/opt/monero/tests/unit_tests/epee_utils.cpp:395:3: error: template argument 1 is invalid
   EXPECT_EQ(htonl(0x1000001), ip);
   ^
/opt/monero/tests/unit_tests/epee_utils.cpp:398:13: error: statement-expressions are not allowed outside functions nor in template-argument lists
   EXPECT_EQ(htonl(0x1010001), ip);
             ^
/opt/monero/tests/unit_tests/epee_utils.cpp:398:3: error: template argument 1 is invalid
   EXPECT_EQ(htonl(0x1010001), ip);
   ^
/opt/monero/tests/unit_tests/epee_utils.cpp:404:13: error: statement-expressions are not allowed outside functions nor in template-argument lists
   EXPECT_EQ(htonl(0x01010101), ip);
             ^
/opt/monero/tests/unit_tests/epee_utils.cpp:404:3: error: template argument 1 is invalid
   EXPECT_EQ(htonl(0x01010101), ip);
   ^
/opt/monero/tests/unit_tests/epee_utils.cpp:416:13: error: statement-expressions are not allowed outside functions nor in template-argument lists
   EXPECT_EQ(htonl(0xaff00ff), ip);
             ^
/opt/monero/tests/unit_tests/epee_utils.cpp:416:3: error: template argument 1 is invalid
   EXPECT_EQ(htonl(0xaff00ff), ip);
   ^
/opt/monero/tests/unit_tests/epee_utils.cpp:419:13: error: statement-expressions are not allowed outside functions nor in template-argument lists
   EXPECT_EQ(htonl(0xff0aff00), ip);
             ^
/opt/monero/tests/unit_tests/epee_utils.cpp:419:3: error: template argument 1 is invalid
   EXPECT_EQ(htonl(0xff0aff00), ip);
   ^
make[3]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/epee_utils.cpp.o] Error 1
make[3]: Leaving directory `/opt/monero/build/release'
make[2]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory `/opt/monero/build/release'
make[1]: *** [all] Error 2
make[1]: Leaving directory `/opt/monero/build/release'
make: *** [release-all] Error 2

# Discussion History
## moneromooo-monero | 2017-09-07T10:06:54+00:00
htonl might be declared in some other header on your OS maybe. Find out which, and include it at the top of the file, and see if that helps.

## bvort | 2017-09-08T01:55:03+00:00
I found a solution, just run cmake before running make

# Action History
- Created by: bvort | 2017-09-07T07:17:56+00:00
- Closed at: 2017-09-08T01:55:03+00:00
