---
title: Bulletproofs++
source_url: https://github.com/monero-project/research-lab/issues/101
author: selsta
assignees: []
labels: []
created_at: '2022-05-06T15:50:09+00:00'
updated_at: '2022-12-31T14:51:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
- Paper: https://eprint.iacr.org/2022/510.pdf
- Repository: https://github.com/Liam-Eagen/BulletproofsPP

```
test_bulletproof_3<true, 1> (100 calls) - OK: 1560 µs/call
test_bulletproof_3<false, 1> (20 calls) - OK: 5850 µs/call
test_bulletproof_3<true, 2> (50 calls) - OK: 2040 µs/call
test_bulletproof_3<false, 2> (10 calls) - OK: 8200 µs/call
test_bulletproof_3<true, 16> (10 calls) - OK: 9500 µs/call
test_bulletproof_3<false, 16> (2 calls) - OK: 73000 µs/call
test_aggregated_bulletproof_3<false, 2, 1, 1, 0, 64> (7 calls) - OK: 131428 µs/call
test_aggregated_bulletproof_3<true, 2, 1, 1, 0, 64> (7 calls) - OK: 52857 µs/call
test_bulletproof_plus<true, 1> (100 calls) - OK: 4360 µs/call
test_bulletproof_plus<false, 1> (20 calls) - OK: 26100 µs/call
test_bulletproof_plus<true, 2> (50 calls) - OK: 7360 µs/call
test_bulletproof_plus<false, 2> (10 calls) - OK: 50500 µs/call
test_bulletproof_plus<true, 16> (10 calls) - OK: 39200 µs/call
test_bulletproof_plus<false, 16> (2 calls) - OK: 343500 µs/call
test_aggregated_bulletproof_plus<false, 2, 1, 1, 0, 64> (7 calls) - OK: 466000 µs/call
test_aggregated_bulletproof_plus<true, 2, 1, 1, 0, 64> (7 calls) - OK: 56285 µs/call
test_bulletproof<true, 1> (100 calls) - OK: 4470 µs/call
test_bulletproof<false, 1> (20 calls) - OK: 28700 µs/call
test_bulletproof<true, 2> (50 calls) - OK: 7420 µs/call
test_bulletproof<false, 2> (10 calls) - OK: 56300 µs/call
test_bulletproof<true, 16> (10 calls) - OK: 39700 µs/call
test_bulletproof<false, 16> (2 calls) - OK: 384500 µs/call
test_aggregated_bulletproof<false, 2, 1, 1, 0, 64> (7 calls) - OK: 469714 µs/call
test_aggregated_bulletproof<true, 2, 1, 1, 0, 64> (7 calls) - OK: 61571 µs/call
Tests finished. Elapsed time: 75 sec
```

Verification speed in monero's performance tests.

# Discussion History
## plowsof | 2022-11-15T01:09:23+00:00
A draft proposal for getting the eprint paper audited https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/358

## UkoeHB | 2022-12-31T14:51:41+00:00
Note: this is how to read the test results

```
test_bulletproof<true, 1> (100 calls) - OK: 4470 µs/call
test_bulletproof<false, 1> (20 calls) - OK: 28700 µs/call
```

- true = proof verification perf; false = proof construction perf
- 1 = number of range proofs in one aggregate prof

```
test_aggregated_bulletproof<false, 2, 1, 1, 0, 64> (7 calls) - OK: 469714 µs/call
test_aggregated_bulletproof<true, 2, 1, 1, 0, 64> (7 calls) - OK: 61571 µs/call
```

- false = don't batch verify; true = batch verify
- 2, 1, 1, 0, 64 = 64 aggregate proofs, each with 2 range proofs

# Action History
- Created by: selsta | 2022-05-06T15:50:09+00:00
