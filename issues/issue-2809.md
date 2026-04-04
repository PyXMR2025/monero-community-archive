---
title: 'error: ''DIFFICULTY_TARGET_V1'' was not declared in this scope'
source_url: https://github.com/monero-project/monero/issues/2809
author: adelinvrd
assignees: []
labels:
- invalid
created_at: '2017-11-14T11:26:31+00:00'
updated_at: '2017-11-14T12:08:24+00:00'
type: issue
status: closed
closed_at: '2017-11-14T12:08:24+00:00'
---

# Original Description
How can i fix this?

`[ 56%] Building CXX object tests/core_tests/CMakeFiles/coretests.dir/block_validation.cpp.o
/root/git/tests/core_tests/block_validation.cpp: In function 'bool {anonymous}::lift_up_difficulty(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings> >&, std::vector<long unsigned int>&, std::vector<long unsigned int>&, test_generator&, size_t, cryptonote::block, const cryptonote::account_base&)':
/root/git/tests/core_tests/block_validation.cpp:48:85: error: 'DIFFICULTY_TARGET_V1' was not declared in this scope
       difficulty_type diffic = next_difficulty(timestamps, cummulative_difficulties,DIFFICULTY_TARGET_V1);
                                                                                     ^
/root/git/tests/core_tests/block_validation.cpp: In member function 'bool gen_block_invalid_nonce::generate(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings> >&) const':
/root/git/tests/core_tests/block_validation.cpp:178:81: error: 'DIFFICULTY_TARGET_V1' was not declared in this scope
   difficulty_type diffic = next_difficulty(timestamps, commulative_difficulties,DIFFICULTY_TARGET_V1);
                                                                                 ^
In file included from /root/git/src/cryptonote_basic/cryptonote_basic.h:47:0,
                 from /root/git/src/cryptonote_basic/account.h:33,
                 from /root/git/src/cryptonote_basic/account_boost_serialization.h:33,
                 from /root/git/tests/core_tests/chaingen.h:47,
                 from /root/git/tests/core_tests/block_validation.cpp:31:
/root/git/tests/core_tests/block_validation.cpp: In member function 'bool gen_block_unlock_time_is_timestamp_in_future::generate(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings> >&) const':
/root/git/src/cryptonote_config.h:85:57: error: 'DIFFICULTY_TARGET_V1' was not declared in this scope
 #define DIFFICULTY_BLOCKS_ESTIMATE_TIMESPAN             DIFFICULTY_TARGET_V1 //just alias; used by tests
                                                         ^
/root/git/tests/core_tests/block_validation.cpp:267:87: note: in expansion of macro 'DIFFICULTY_BLOCKS_ESTIMATE_TIMESPAN'
   miner_tx.unlock_time = blk_0.timestamp + 3 * CRYPTONOTE_MINED_MONEY_UNLOCK_WINDOW * DIFFICULTY_BLOCKS_ESTIMATE_TIMESPAN;
                                                                                       ^
/root/git/tests/core_tests/block_validation.cpp: In member function 'bool gen_block_invalid_binary_format::generate(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings> >&) const':
/root/git/tests/core_tests/block_validation.cpp:575:67: error: 'DIFFICULTY_TARGET_V1' was not declared in this scope
     diffic = next_difficulty(timestamps, cummulative_difficulties,DIFFICULTY_TARGET_V1);
                                                                   ^
/root/git/tests/core_tests/block_validation.cpp:590:65: error: 'DIFFICULTY_TARGET_V1' was not declared in this scope
   diffic = next_difficulty(timestamps, cummulative_difficulties,DIFFICULTY_TARGET_V1);
                                                                 ^
tests/core_tests/CMakeFiles/coretests.dir/build.make:86: recipe for target 'tests/core_tests/CMakeFiles/coretests.dir/block_validation.cpp.o' failed
make[3]: *** [tests/core_tests/CMakeFiles/coretests.dir/block_validation.cpp.o] Error 1
make[3]: Leaving directory '/root/git/build/release'
CMakeFiles/Makefile2:2157: recipe for target 'tests/core_tests/CMakeFiles/coretests.dir/all' failed
make[2]: *** [tests/core_tests/CMakeFiles/coretests.dir/all] Error 2
make[2]: Leaving directory '/root/git/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/root/git/build/release'
Makefile:62: recipe for target 'release-all' failed
make: *** [release-all] Error 2
`

# Discussion History
## moneromooo-monero | 2017-11-14T11:47:18+00:00
This is not monero, but a fork. They've changed the code, and apparently broken it. Ask them for how to fix it.

Alternatively, if you can reproduce this with Monero, please include your OS, compiler, and the commit hash you're building, and open a bug.

Also, where did you find a pointer to this repo ? It would be nice to get that fixed in the fork, unless they kept the URL on purpose to spam us :/

## moneromooo-monero | 2017-11-14T12:07:07+00:00
From another report, I've found the electroneum people have disabled their bug report page, so github sends you to us instead, since they copied our code. I suggest you find out how to contact them, and ask them to fix this, assuming they didn't do it on purpose.

Closing

+invalid

# Action History
- Created by: adelinvrd | 2017-11-14T11:26:31+00:00
- Closed at: 2017-11-14T12:08:24+00:00
