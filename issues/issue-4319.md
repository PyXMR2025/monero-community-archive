---
title: error on gtest after 100%
source_url: https://github.com/monero-project/monero/issues/4319
author: kenken64
assignees: []
labels: []
created_at: '2018-08-31T08:03:53+00:00'
updated_at: '2018-09-09T17:10:49+00:00'
type: issue
status: closed
closed_at: '2018-09-09T17:10:49+00:00'
---

# Original Description
[ 98%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/vercmp.cpp.o
[ 98%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/ringdb.cpp.o
[100%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/wipeable_string.cpp.o
In file included from /usr/include/gtest/gtest.h:58:0,
                 from /media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/tests/unit_tests/wipeable_string.cpp:31:
/media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/tests/unit_tests/wipeable_string.cpp: In member function ‘virtual void wipeable_string_parse_hexstr_Test::TestBody()’:
/media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/tests/unit_tests/wipeable_string.cpp:196:3: error: no matching function for call to ‘testing::AssertionResult::AssertionResult(boost::optional<epee::wipeable_string>&)’
   ASSERT_TRUE((s = epee::wipeable_string("").parse_hexstr()));
   ^
In file included from /media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/tests/unit_tests/wipeable_string.cpp:31:0:
/usr/include/gtest/gtest.h:262:12: note: candidate: testing::AssertionResult::AssertionResult(bool)
   explicit AssertionResult(bool success) : success_(success) {}
            ^
/usr/include/gtest/gtest.h:262:12: note:   no known conversion for argument 1 from ‘boost::optional<epee::wipeable_string>’ to ‘bool’
/usr/include/gtest/gtest.h:260:3: note: candidate: testing::AssertionResult::AssertionResult(const testing::AssertionResult&)
   AssertionResult(const AssertionResult& other);
   ^
/usr/include/gtest/gtest.h:260:3: note:   no known conversion for argument 1 from ‘boost::optional<epee::wipeable_string>’ to ‘const testing::AssertionResult&’
In file included from /usr/include/gtest/gtest.h:58:0,
                 from /media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/tests/unit_tests/wipeable_string.cpp:31:
/media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/tests/unit_tests/wipeable_string.cpp:198:3: error: no matching function for call to ‘testing::AssertionResult::AssertionResult(boost::optional<epee::wipeable_string>&)’
   ASSERT_TRUE((s = epee::wipeable_string("00").parse_hexstr()));
   ^
In file included from /media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/tests/unit_tests/wipeable_string.cpp:31:0:
/usr/include/gtest/gtest.h:262:12: note: candidate: testing::AssertionResult::AssertionResult(bool)
   explicit AssertionResult(bool success) : success_(success) {}
            ^
/usr/include/gtest/gtest.h:262:12: note:   no known conversion for argument 1 from ‘boost::optional<epee::wipeable_string>’ to ‘bool’
/usr/include/gtest/gtest.h:260:3: note: candidate: testing::AssertionResult::AssertionResult(const testing::AssertionResult&)
   AssertionResult(const AssertionResult& other);
   ^
/usr/include/gtest/gtest.h:260:3: note:   no known conversion for argument 1 from ‘boost::optional<epee::wipeable_string>’ to ‘const testing::AssertionResult&’
In file included from /usr/include/gtest/gtest.h:58:0,
                 from /media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/tests/unit_tests/wipeable_string.cpp:31:
/media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/tests/unit_tests/wipeable_string.cpp:200:3: error: no matching function for call to ‘testing::AssertionResult::AssertionResult(boost::optional<epee::wipeable_string>&)’
   ASSERT_TRUE((s = epee::wipeable_string("41").parse_hexstr()));
   ^
In file included from /media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/tests/unit_tests/wipeable_string.cpp:31:0:
/usr/include/gtest/gtest.h:262:12: note: candidate: testing::AssertionResult::AssertionResult(bool)
   explicit AssertionResult(bool success) : success_(success) {}
            ^
/usr/include/gtest/gtest.h:262:12: note:   no known conversion for argument 1 from ‘boost::optional<epee::wipeable_string>’ to ‘bool’
/usr/include/gtest/gtest.h:260:3: note: candidate: testing::AssertionResult::AssertionResult(const testing::AssertionResult&)
   AssertionResult(const AssertionResult& other);
   ^
/usr/include/gtest/gtest.h:260:3: note:   no known conversion for argument 1 from ‘boost::optional<epee::wipeable_string>’ to ‘const testing::AssertionResult&’
In file included from /usr/include/gtest/gtest.h:58:0,
                 from /media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/tests/unit_tests/wipeable_string.cpp:31:
/media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/tests/unit_tests/wipeable_string.cpp:202:3: error: no matching function for call to ‘testing::AssertionResult::AssertionResult(boost::optional<epee::wipeable_string>&)’
   ASSERT_TRUE((s = epee::wipeable_string("414243").parse_hexstr()));
   ^
In file included from /media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/tests/unit_tests/wipeable_string.cpp:31:0:
/usr/include/gtest/gtest.h:262:12: note: candidate: testing::AssertionResult::AssertionResult(bool)
   explicit AssertionResult(bool success) : success_(success) {}
            ^
/usr/include/gtest/gtest.h:262:12: note:   no known conversion for argument 1 from ‘boost::optional<epee::wipeable_string>’ to ‘bool’
/usr/include/gtest/gtest.h:260:3: note: candidate: testing::AssertionResult::AssertionResult(const testing::AssertionResult&)
   AssertionResult(const AssertionResult& other);
   ^
/usr/include/gtest/gtest.h:260:3: note:   no known conversion for argument 1 from ‘boost::optional<epee::wipeable_string>’ to ‘const testing::AssertionResult&’
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:1238: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/wipeable_string.cpp.o' failed
make[3]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/wipeable_string.cpp.o] Error 1
make[3]: *** Waiting for unfinished jobs....
make[3]: Leaving directory '/media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/build/release'
CMakeFiles/Makefile2:4418: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/all' failed
make[2]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/media/kenneth/b13ae9f7-5727-4bc0-94fe-77d72079f2ee/monero/build/release'
Makefile:72: recipe for target 'release-all' failed
make: *** [release-all] Error 2


# Discussion History
## moneromooo-monero | 2018-08-31T09:20:31+00:00
What compiler, and does this patch work ?
Save to a file, then: patch -p1 < filenameyousaveditas
When you've tested, undo it with: patch -p1 -R < filenameyousaveditas

```
diff --git a/tests/unit_tests/wipeable_string.cpp b/tests/unit_tests/wipeable_string.cpp
index 5ea1c17..2450118 100644
--- a/tests/unit_tests/wipeable_string.cpp
+++ b/tests/unit_tests/wipeable_string.cpp
@@ -193,12 +193,12 @@ TEST(wipeable_string, parse_hexstr)
   ASSERT_EQ(boost::none, epee::wipeable_string("0").parse_hexstr());
   ASSERT_EQ(boost::none, epee::wipeable_string("000").parse_hexstr());
 
-  ASSERT_TRUE((s = epee::wipeable_string("").parse_hexstr()));
+  ASSERT_TRUE((s = epee::wipeable_string("").parse_hexstr()) != boost::none);
   ASSERT_EQ(*s, "");
-  ASSERT_TRUE((s = epee::wipeable_string("00").parse_hexstr()));
+  ASSERT_TRUE((s = epee::wipeable_string("00").parse_hexstr()) != boost::none);
   ASSERT_EQ(*s, epee::wipeable_string("", 1));
-  ASSERT_TRUE((s = epee::wipeable_string("41").parse_hexstr()));
+  ASSERT_TRUE((s = epee::wipeable_string("41").parse_hexstr()) != boost::none);
   ASSERT_EQ(*s, epee::wipeable_string("A"));
-  ASSERT_TRUE((s = epee::wipeable_string("414243").parse_hexstr()));
+  ASSERT_TRUE((s = epee::wipeable_string("414243").parse_hexstr()) != boost::none);
   ASSERT_EQ(*s, epee::wipeable_string("ABC"));
 }

```

## moneromooo-monero | 2018-09-09T12:40:21+00:00
ping

## kenken64 | 2018-09-09T17:10:49+00:00
no luck i tried using diff branch 

# Action History
- Created by: kenken64 | 2018-08-31T08:03:53+00:00
- Closed at: 2018-09-09T17:10:49+00:00
