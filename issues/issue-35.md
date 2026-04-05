---
title: Receiving funds using carrot lib fails on M1 Mac.
source_url: https://github.com/seraphis-migration/monero/issues/35
author: akildemir
assignees: []
labels: []
created_at: '2025-04-29T11:52:40+00:00'
updated_at: '2025-10-14T19:34:07+00:00'
type: issue
status: closed
closed_at: '2025-10-14T19:34:07+00:00'
---

# Original Description
Hello,

We realized the receiving funds using `try_scan_carrot_enote_external_receiver` function fails(it returns `false` for an enote that is supposed to return `true`) on M1 MacBook Pro while it passes in Linux x86 arch. To make sure of the issue I made a clean copy of `fcmp++-stage` branch and did `make debug-test -j4` and run the unit tests binary with `--gtest_filter="carrot_tx_builder.*"` argument. Sure enough 6 out of 14 tests in the failed, all with the same message; 
```
.../unit_tests/carrot_tx_builder.cpp:230: Failure
Expected equality of these values:
  1
  scan_results.size()
    Which is: 0
```

So tests expect to receive an output but they don't.  Here is the list of the tests that are failing;

```
[==========] 14 tests from 1 test suite ran. (1666 ms total)
[  PASSED  ] 8 tests.
[  FAILED  ] 6 tests, listed below:
[  FAILED  ] carrot_tx_builder.make_sal_proof_carrot_to_legacy_v1_mainaddr_normal
[  FAILED  ] carrot_tx_builder.make_sal_proof_carrot_to_legacy_v1_subaddr_normal
[  FAILED  ] carrot_tx_builder.make_sal_proof_carrot_to_carrot_v1_mainaddr_normal
[  FAILED  ] carrot_tx_builder.make_sal_proof_carrot_to_carrot_v1_subaddr_normal
[  FAILED  ] carrot_tx_builder.make_sal_proof_carrot_coinbase_to_legacy_v1
[  FAILED  ] carrot_tx_builder.make_sal_proof_carrot_coinbase_to_carrot_v1
```

Is this something you guys already aware of or Am I the first one who just stumble upon on this?

`MacOS Version: Sequoia 15.3.2` 

# Discussion History
## jeffro256 | 2025-04-29T20:33:40+00:00
Oh yes this is expected, and is on my [TODO list](https://github.com/monero-project/monero/pull/9559#issue-2645143517), but I kind of forgot about it ;). Currently, I haven't ported over the mx25519 modifications to ARM, since I don't know ARM assembly, so the X25519 key exchange is broken on ARM Macs. Perhaps I bump that up on my list so Mac-eans can test. 

## akildemir | 2025-04-30T09:30:21+00:00
@jeffro256 Thanks that is good to know. By the way, I realized there is some missing code/files in the [carrot_impl](https://github.com/jeffro256/monero/tree/carrot_impl/src/) repo(in unit_tests), which repo/branch should we track for the latest carrot code?

## jeffro256 | 2025-04-30T13:32:19+00:00
If you want the latest changes, the `fcmp++-stage` branch in this repository is where all most recent dev work happens. 

Also, just pushed commit(s) to `fcmp++-stage` which makes ARM machines use the portable implementation by default, so Carrot should work on ARM now. Don't mind the performance though, the actual ARM assembly implementations is much, much faster than the portable version. 

## jeffro256 | 2025-04-30T13:35:23+00:00
I'll leave this issue open until the ARM implementation is done correctly. See https://github.com/tevador/mx25519/issues/12 for more information. 

## jeffro256 | 2025-05-02T16:47:48+00:00
@akildemir Did you have any success with the latest version of the `fcmp++-stage` branch?

## akildemir | 2025-05-05T10:07:35+00:00
@jeffro256 yup all seems fine now 👍 

# Action History
- Created by: akildemir | 2025-04-29T11:52:40+00:00
- Closed at: 2025-10-14T19:34:07+00:00
