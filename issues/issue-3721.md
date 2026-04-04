---
title: 'Makefile:138: recipe for target ''all'' failed'
source_url: https://github.com/monero-project/monero/issues/3721
author: quantumproducer
assignees: []
labels: []
created_at: '2018-04-28T19:01:06+00:00'
updated_at: '2018-05-01T21:37:37+00:00'
type: issue
status: closed
closed_at: '2018-04-28T21:48:43+00:00'
---

# Original Description
Ubuntu. I started by installing all dependencies with apt-get, then cloned recursively & ran the submodule init & update recursive.

```
[ 94%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/hardfork.cpp.o
/root/monero/tests/unit_tests/hardfork.cpp: In member function ‘virtual void major_Only_Test::TestBody()’:
/root/monero/tests/unit_tests/hardfork.cpp:171:10: error: cannot declare variable ‘db’ to be of abstract type ‘TestDB’
   TestDB db;
          ^~
/root/monero/tests/unit_tests/hardfork.cpp:44:7: note:   because the following virtual functions are pure within ‘TestDB’:
 class TestDB: public BlockchainDB {
       ^~~~~~
In file included from /root/monero/tests/unit_tests/hardfork.cpp:34:0:
/root/monero/src/blockchain_db/blockchain_db.h:1497:72: note: 	virtual std::map<long unsigned int, std::tuple<long unsigned int, long unsigned int, long unsigned int> > cryptonote::BlockchainDB::get_output_histogram(const std::vector<long unsigned int>&, bool, uint64_t, uint64_t) const
   virtual std::map<uint64_t, std::tuple<uint64_t, uint64_t, uint64_t>> get_output_histogram(const std::vector<uint64_t> &amounts, bool unlocked, uint64_t recent_cutoff, uint64_t min_count) const = 0;
                                                                        ^~~~~~~~~~~~~~~~~~~~
/root/monero/tests/unit_tests/hardfork.cpp: In member function ‘virtual void empty_hardforks_Success_Test::TestBody()’:
/root/monero/tests/unit_tests/hardfork.cpp:201:10: error: cannot declare variable ‘db’ to be of abstract type ‘TestDB’
   TestDB db;
          ^~
/root/monero/tests/unit_tests/hardfork.cpp: In member function ‘virtual void ordering_Success_Test::TestBody()’:
/root/monero/tests/unit_tests/hardfork.cpp:220:10: error: cannot declare variable ‘db’ to be of abstract type ‘TestDB’
   TestDB db;
          ^~
/root/monero/tests/unit_tests/hardfork.cpp: In member function ‘virtual void states_Success_Test::TestBody()’:
/root/monero/tests/unit_tests/hardfork.cpp:234:10: error: cannot declare variable ‘db’ to be of abstract type ‘TestDB’
   TestDB db;
          ^~
/root/monero/tests/unit_tests/hardfork.cpp: In member function ‘virtual void steps_asap_Success_Test::TestBody()’:
/root/monero/tests/unit_tests/hardfork.cpp:257:10: error: cannot declare variable ‘db’ to be of abstract type ‘TestDB’
   TestDB db;
          ^~
/root/monero/tests/unit_tests/hardfork.cpp: In member function ‘virtual void steps_1_Success_Test::TestBody()’:
/root/monero/tests/unit_tests/hardfork.cpp:286:10: error: cannot declare variable ‘db’ to be of abstract type ‘TestDB’
   TestDB db;
          ^~
/root/monero/tests/unit_tests/hardfork.cpp: In member function ‘virtual void reorganize_Same_Test::TestBody()’:
/root/monero/tests/unit_tests/hardfork.cpp:307:12: error: cannot declare variable ‘db’ to be of abstract type ‘TestDB’
     TestDB db;
            ^~
/root/monero/tests/unit_tests/hardfork.cpp: In member function ‘virtual void reorganize_Changed_Test::TestBody()’:
/root/monero/tests/unit_tests/hardfork.cpp:336:10: error: cannot declare variable ‘db’ to be of abstract type ‘TestDB’
   TestDB db;
          ^~
/root/monero/tests/unit_tests/hardfork.cpp: In member function ‘virtual void voting_threshold_Test::TestBody()’:
/root/monero/tests/unit_tests/hardfork.cpp:385:12: error: cannot declare variable ‘db’ to be of abstract type ‘TestDB’
     TestDB db;
            ^~
/root/monero/tests/unit_tests/hardfork.cpp: In member function ‘virtual void voting_different_thresholds_Test::TestBody()’:
/root/monero/tests/unit_tests/hardfork.cpp:414:12: error: cannot declare variable ‘db’ to be of abstract type ‘TestDB’
     TestDB db;
            ^~
/root/monero/tests/unit_tests/hardfork.cpp: In member function ‘virtual void new_blocks_denied_Test::TestBody()’:
/root/monero/tests/unit_tests/hardfork.cpp:441:12: error: cannot declare variable ‘db’ to be of abstract type ‘TestDB’
     TestDB db;
            ^~
/root/monero/tests/unit_tests/hardfork.cpp: In member function ‘virtual void new_version_early_Test::TestBody()’:
/root/monero/tests/unit_tests/hardfork.cpp:464:12: error: cannot declare variable ‘db’ to be of abstract type ‘TestDB’
     TestDB db;
            ^~
/root/monero/tests/unit_tests/hardfork.cpp: In member function ‘virtual void reorganize_changed_Test::TestBody()’:
/root/monero/tests/unit_tests/hardfork.cpp:484:12: error: cannot declare variable ‘db’ to be of abstract type ‘TestDB’
     TestDB db;
            ^~
/root/monero/tests/unit_tests/hardfork.cpp: In member function ‘virtual void get_higher_Test::TestBody()’:
/root/monero/tests/unit_tests/hardfork.cpp:535:12: error: cannot declare variable ‘db’ to be of abstract type ‘TestDB’
     TestDB db;
            ^~
tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:902: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/hardfork.cpp.o' failed
make[3]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/hardfork.cpp.o] Error 1
make[3]: Leaving directory '/root/monero/build/release'
CMakeFiles/Makefile2:4465: recipe for target 'tests/unit_tests/CMakeFiles/unit_tests.dir/all' failed
make[2]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[2]: Leaving directory '/root/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/root/monero/build/release'
Makefile:64: recipe for target 'release-all' failed
make: *** [release-all] Error 2
```

# Discussion History
## moneromooo-monero | 2018-04-28T21:40:58+00:00
https://github.com/monero-project/monero/pull/3720 (already merged)

## moneromooo-monero | 2018-04-28T21:41:10+00:00
+resolved

## quantumproducer | 2018-05-01T21:37:37+00:00
Thank you

# Action History
- Created by: quantumproducer | 2018-04-28T19:01:06+00:00
- Closed at: 2018-04-28T21:48:43+00:00
