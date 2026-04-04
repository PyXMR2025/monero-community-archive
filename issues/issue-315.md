---
title: Unit Tests failure at v0.8.8.6
source_url: https://github.com/monero-project/monero/issues/315
author: shawnpringle
assignees: []
labels: []
created_at: '2015-06-09T21:40:35+00:00'
updated_at: '2016-01-25T18:11:36+00:00'
type: issue
status: closed
closed_at: '2016-01-25T18:11:36+00:00'
---

# Original Description
``` sh
bash-4.2$ make test
Running tests...
Test project /home/shawn/development/pkg/bitmonero/build/release/tests
      Start  1: hash-target
 1/12 Test  #1: hash-target ......................   Passed    0.99 sec
      Start  2: coretests
 2/12 Test  #2: coretests ........................***Exception: SegFault  4.75 sec
      Start  3: crypto
 3/12 Test  #3: crypto ...........................   Passed  189.66 sec
      Start  4: unit_tests
 4/12 Test  #4: unit_tests .......................***Failed   52.97 sec
      Start  5: difficulty
 5/12 Test  #5: difficulty .......................   Passed    1.18 sec
      Start  6: hash-fast
 6/12 Test  #6: hash-fast ........................   Passed    0.50 sec
      Start  7: hash-slow
 7/12 Test  #7: hash-slow ........................***Exception: SegFault  0.38 sec
      Start  8: hash-tree
 8/12 Test  #8: hash-tree ........................   Passed    0.15 sec
      Start  9: hash-extra-blake
 9/12 Test  #9: hash-extra-blake .................   Passed    0.53 sec
      Start 10: hash-extra-groestl
10/12 Test #10: hash-extra-groestl ...............   Passed    0.50 sec
      Start 11: hash-extra-jh
11/12 Test #11: hash-extra-jh ....................   Passed    2.25 sec
      Start 12: hash-extra-skein
12/12 Test #12: hash-extra-skein .................   Passed    2.23 sec

75% tests passed, 3 tests failed out of 12

Total Test time (real) = 259.56 sec

The following tests FAILED:
          2 - coretests (SEGFAULT)
          4 - unit_tests (Failed)
          7 - hash-slow (SEGFAULT)
Errors while running CTest
```

I am using Linux/32bit
# 

``` sh
git diff | tee /dev/null:
```

``` diff
diff --git a/src/cryptonote_core/difficulty.cpp b/src/cryptonote_core/difficulty.cpp
index d4d733e..25c0f84 100644
--- a/src/cryptonote_core/difficulty.cpp
+++ b/src/cryptonote_core/difficulty.cpp
@@ -45,9 +45,13 @@ namespace cryptonote {
   using std::uint64_t;
   using std::vector;

-#if defined(_MSC_VER) || defined(__MINGW32__)
+// Any 32-bit on MSC, or GNUC
+#if defined(_MSC_VER) || \
+       (defined(__GNUC__) && __SIZEOF_POINTER__ == 4)
+#ifdef _WIN32 
 #include <windows.h>
 #include <winnt.h>
+#endif

   static inline void mul(uint64_t a, uint64_t b, uint64_t &low, uint64_t &high) {
     low = mul128(a, b, &high);
```
# 


# Discussion History
## fluffypony | 2016-01-25T18:11:36+00:00
Fixed in 0.9


# Action History
- Created by: shawnpringle | 2015-06-09T21:40:35+00:00
- Closed at: 2016-01-25T18:11:36+00:00
