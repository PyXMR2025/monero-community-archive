---
title: Build failed - cannot declare variable 'db' to be of abstract type 'TestDB'
source_url: https://github.com/monero-project/monero/issues/3747
author: khelle
assignees: []
labels: []
created_at: '2018-05-02T14:06:15+00:00'
updated_at: '2018-05-16T10:24:56+00:00'
type: issue
status: closed
closed_at: '2018-05-16T10:24:56+00:00'
---

# Original Description
Hi, because of bug related to #3734 I am rebuilding the monero using release-v0.12 branch which incorporates fix #3723 and #3730 .

I downloaded all dependencies and am buliding using command:

```
make CXXFLAGS=-fPIC CFLAGS=-fPIC
```

I get following compilation errors:

```
/home/xmr/node/tests/unit_tests/hardfork.cpp: In member function 'virtual void major_Only_Test::TestBody()':
/home/xmr/node/tests/unit_tests/hardfork.cpp:171:10: error: cannot declare variable 'db' to be of abstract type 'TestDB'
   TestDB db;
          ^
/home/xmr/node/tests/unit_tests/hardfork.cpp:44:7: note:   because the following virtual functions are pure within 'TestDB':
 class TestDB: public BlockchainDB {
       ^
In file included from /home/xmr/node/tests/unit_tests/hardfork.cpp:34:0:
/home/xmr/node/src/blockchain_db/blockchain_db.h:1497:72: note: 	virtual std::map<long unsigned int, std::tuple<long unsigned int, long unsigned int, long unsigned int> > cryptonote::BlockchainDB::get_output_histogram(const std::vector<long unsigned int>&, bool, uint64_t, uint64_t) const
   virtual std::map<uint64_t, std::tuple<uint64_t, uint64_t, uint64_t>> get_output_histogram(const std::vector<uint64_t> &amounts, bool unlocked, uint64_t recent_cutoff, uint64_t min_count) const = 0;
                                                                        ^
/home/xmr/node/tests/unit_tests/hardfork.cpp: In member function 'virtual void empty_hardforks_Success_Test::TestBody()':
/home/xmr/node/tests/unit_tests/hardfork.cpp:201:10: error: cannot declare variable 'db' to be of abstract type 'TestDB'
   TestDB db;
          ^
/home/xmr/node/tests/unit_tests/hardfork.cpp: In member function 'virtual void ordering_Success_Test::TestBody()':
/home/xmr/node/tests/unit_tests/hardfork.cpp:220:10: error: cannot declare variable 'db' to be of abstract type 'TestDB'
   TestDB db;
          ^
/home/xmr/node/tests/unit_tests/hardfork.cpp: In member function 'virtual void states_Success_Test::TestBody()':
/home/xmr/node/tests/unit_tests/hardfork.cpp:234:10: error: cannot declare variable 'db' to be of abstract type 'TestDB'
   TestDB db;
          ^
/home/xmr/node/tests/unit_tests/hardfork.cpp: In member function 'virtual void steps_asap_Success_Test::TestBody()':
/home/xmr/node/tests/unit_tests/hardfork.cpp:257:10: error: cannot declare variable 'db' to be of abstract type 'TestDB'
   TestDB db;
          ^
/home/xmr/node/tests/unit_tests/hardfork.cpp: In member function 'virtual void steps_1_Success_Test::TestBody()':
/home/xmr/node/tests/unit_tests/hardfork.cpp:286:10: error: cannot declare variable 'db' to be of abstract type 'TestDB'
   TestDB db;
          ^
/home/xmr/node/tests/unit_tests/hardfork.cpp: In member function 'virtual void reorganize_Same_Test::TestBody()':
/home/xmr/node/tests/unit_tests/hardfork.cpp:307:12: error: cannot declare variable 'db' to be of abstract type 'TestDB'
     TestDB db;
            ^
/home/xmr/node/tests/unit_tests/hardfork.cpp: In member function 'virtual void reorganize_Changed_Test::TestBody()':
/home/xmr/node/tests/unit_tests/hardfork.cpp:336:10: error: cannot declare variable 'db' to be of abstract type 'TestDB'
   TestDB db;
          ^
/home/xmr/node/tests/unit_tests/hardfork.cpp: In member function 'virtual void voting_threshold_Test::TestBody()':
/home/xmr/node/tests/unit_tests/hardfork.cpp:385:12: error: cannot declare variable 'db' to be of abstract type 'TestDB'
     TestDB db;
            ^
/home/xmr/node/tests/unit_tests/hardfork.cpp: In member function 'virtual void voting_different_thresholds_Test::TestBody()':
/home/xmr/node/tests/unit_tests/hardfork.cpp:414:12: error: cannot declare variable 'db' to be of abstract type 'TestDB'
     TestDB db;
            ^
/home/xmr/node/tests/unit_tests/hardfork.cpp: In member function 'virtual void new_blocks_denied_Test::TestBody()':
/home/xmr/node/tests/unit_tests/hardfork.cpp:441:12: error: cannot declare variable 'db' to be of abstract type 'TestDB'
     TestDB db;
            ^
/home/xmr/node/tests/unit_tests/hardfork.cpp: In member function 'virtual void new_version_early_Test::TestBody()':
/home/xmr/node/tests/unit_tests/hardfork.cpp:464:12: error: cannot declare variable 'db' to be of abstract type 'TestDB'
     TestDB db;
            ^
/home/xmr/node/tests/unit_tests/hardfork.cpp: In member function 'virtual void reorganize_changed_Test::TestBody()':
/home/xmr/node/tests/unit_tests/hardfork.cpp:484:12: error: cannot declare variable 'db' to be of abstract type 'TestDB'
     TestDB db;
            ^
/home/xmr/node/tests/unit_tests/hardfork.cpp: In member function 'virtual void get_higher_Test::TestBody()':
/home/xmr/node/tests/unit_tests/hardfork.cpp:535:12: error: cannot declare variable 'db' to be of abstract type 'TestDB'
     TestDB db;
            ^
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:902: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/hardfork.cpp.o' failed
make[3]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/hardfork.cpp.o] Error 1
make[3]: Leaving directory '/home/xmr/node/build/release'
CMakeFiles/Makefile2:4465: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/all' failed
make[2]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/home/xmr/node/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/xmr/node/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2
```

How can I fix the problem?

# Discussion History
## moneromooo-monero | 2018-05-02T14:52:12+00:00
That's fixed in 3741.


## khelle | 2018-05-07T08:49:14+00:00
Is there anything I can do to make it work on my machine? I waited for few days, but still #3741 was not merged. I cannot wait more, as the users I provide monero payments for are getting impatient and I am being scolded.

## moneromooo-monero | 2018-05-07T10:39:59+00:00
That's the tests that are failing to build fwiw. Wallet and daemon are already built at that point.

## moneromooo-monero | 2018-05-16T10:22:24+00:00
It's been merged for a few days now.

+resolved


# Action History
- Created by: khelle | 2018-05-02T14:06:15+00:00
- Closed at: 2018-05-16T10:24:56+00:00
