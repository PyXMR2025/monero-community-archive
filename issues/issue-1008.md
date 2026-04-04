---
title: 'bitmonerod: armv7: some unittest tests fail in debug build'
source_url: https://github.com/monero-project/monero/issues/1008
author: radfish
assignees: []
labels: []
created_at: '2016-08-29T15:50:57+00:00'
updated_at: '2016-09-16T02:18:04+00:00'
type: issue
status: closed
closed_at: '2016-09-16T02:18:04+00:00'
---

# Original Description
Commit 16e9dbc
build with `cmake -DCMAKE_BUILD_TYPE=Debug`

```
[----------] 8 tests from block_reward_and_current_block_size
[ RUN      ] block_reward_and_current_block_size.handles_block_size_less_relevance_level
[       OK ] block_reward_and_current_block_size.handles_block_size_less_relevance_level (0 ms)
[ RUN      ] block_reward_and_current_block_size.handles_block_size_eq_relevance_level
[       OK ] block_reward_and_current_block_size.handles_block_size_eq_relevance_level (0 ms)
[ RUN      ] block_reward_and_current_block_size.handles_block_size_gt_relevance_level
[       OK ] block_reward_and_current_block_size.handles_block_size_gt_relevance_level (0 ms)
[ RUN      ] block_reward_and_current_block_size.handles_block_size_less_2_relevance_level
[       OK ] block_reward_and_current_block_size.handles_block_size_less_2_relevance_level (0 ms)
[ RUN      ] block_reward_and_current_block_size.handles_block_size_eq_2_relevance_level
[       OK ] block_reward_and_current_block_size.handles_block_size_eq_2_relevance_level (0 ms)
[ RUN      ] block_reward_and_current_block_size.handles_block_size_gt_2_relevance_level
[       OK ] block_reward_and_current_block_size.handles_block_size_gt_2_relevance_level (0 ms)
[ RUN      ] block_reward_and_current_block_size.fails_on_huge_median_size
/home/redfish/bitmonero-git-PKGBUILD/src/bitmonero/tests/unit_tests/block_reward.cpp:145: Failure
Death test: do_test(huge_size, huge_size + 1)
    Result: failed to die.
 Error msg:
[  DEATH   ]
[  FAILED  ] block_reward_and_current_block_size.fails_on_huge_median_size (6 ms)
[ RUN      ] block_reward_and_current_block_size.fails_on_huge_block_size
/home/redfish/bitmonero-git-PKGBUILD/src/bitmonero/tests/unit_tests/block_reward.cpp:153: Failure
Death test: do_test(huge_size - 2, huge_size)
    Result: failed to die.
 Error msg:
[  DEATH   ]
[  FAILED  ] block_reward_and_current_block_size.fails_on_huge_block_size (5 ms)
[----------] 8 tests from block_reward_and_current_block_size (12 ms total)
```

```
 [----------] Global test environment tear-down
[==========] 620 tests from 57 test cases ran. (357217 ms total)
[  PASSED  ] 618 tests.
[  FAILED  ] 2 tests, listed below:
[  FAILED  ] block_reward_and_current_block_size.fails_on_huge_median_size
[  FAILED  ] block_reward_and_current_block_size.fails_on_huge_block_size

 2 FAILED TESTS
```


# Discussion History
## moneromooo-monero | 2016-08-30T09:03:33+00:00
These tests should trigger asserts in src/cryptonote_core/cryptonote_basic_impl.cpp, get_block_reward. Do you have asserts disabled ?


## radfish | 2016-09-01T04:13:37+00:00
Asserts where enabled, I double checked by adding an assert(false).

I think the root cause is a few 32-bit problems:
https://github.com/radfish/bitmonero/commit/c0b5cc10e207a47bdc383fd0bba7901a12eeccf4

If that ^ looks good to you I will PR it. Tested that unit_tests passes on 32-bit armv7 and on x86_64.


## moneromooo-monero | 2016-09-02T12:31:59+00:00
I'm not sure that's a good idea. Since 32 bit systems are supposed to be able to process the blockchain, which uses some 64 bit operations in various places, I think they should be fixed where they do not handle 64 bit stuff properly. They do have uint64_t, right ? I'm pretty sure long long should be 64 bits on 32 bit platforms.


## radfish | 2016-09-02T23:28:21+00:00
@moneromooo-monero Agreed that changing `size_t` to `uint64_t` everywhere (at least in that functions's prototype and anywhere related) is another fix, but I was worried that the authors used `size_t` on purpose instead of `uint64_t` to match the word size on the machine (for efficiency reasons). Is it safe to assume that they did not? If so, do you want a PR with size_t->uint64_t change instead?


## moneromooo-monero | 2016-09-03T18:13:28+00:00
At first glance, I would not expect this to be a performance issue. I could make a patch for this, but I could not test whether it'd work. If you don't, I'll put that in my list of things to do.


## iamsmooth | 2016-09-04T06:23:24+00:00
32 bit systems should be able to process the blockchain, but processing blocks that are too large to fit in a 32 bit address space is unrealistic. If blocks ever get that large, with the current code, 32 bit systems will certainly fail. 

The first test is trying to observe correct behavior on blocks larger than 32 bits, which is incorrect expect to work on a 32 bit system. The second test is trying to observe correct behavior on a block which is exactly the size of a 32 bit address space, which is incorrect expect to work on a 32 bit system.

I think the correct fix is to disable both failing tests on a 32 bit platform.

If code is ever written which can process >4 GB blocks on 32-bit systems (seems highly unlikely), the tests can be reenabled.


## moneromooo-monero | 2016-09-04T06:53:48+00:00
Fair enough, but then the consensus code should be changed to cap block size at 32 bits.


## iamsmooth | 2016-09-04T07:43:44+00:00
@moneromooo-monero only if it is a requirement to support 32 bit platforms forever. I think it is reasonable that if blocks ever get to >32 bit, then 32 bit nodes become unsupported and fail (realistically before that)

Not unlike some nodes will have their disks fill up and fail once the blockchain grows sufficiently, others won't. We wouldn't cap blockchain size in consensus to prevent this.


## radfish | 2016-09-16T02:18:04+00:00
Merged in #1050


# Action History
- Created by: radfish | 2016-08-29T15:50:57+00:00
- Closed at: 2016-09-16T02:18:04+00:00
