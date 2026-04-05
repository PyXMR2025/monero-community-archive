---
title: Sporadically slow FCMP++ verify
source_url: https://github.com/seraphis-migration/monero/issues/246
author: j-berman
assignees: []
labels: []
created_at: '2025-11-22T20:07:16+00:00'
updated_at: '2025-12-11T19:04:47+00:00'
type: issue
status: closed
closed_at: '2025-12-11T19:04:47+00:00'
---

# Original Description
u/Lyza reports sporadically slow time to verify FCMP++ txs on a machine with a good CPU (core i5 10300-H (10th gen)) using [this build](https://github.com/j-berman/monero/commits/test-fcmp%2B%2B-alpha-stressnet/). It's taking their machine up to 51s to verify 128-input FCMP++ txs. At other times, I've seen it take 12s in their logs.

# Discussion History
## j-berman | 2025-11-24T20:36:58+00:00
u/Lyza's machine has a low power mode that was apparently throttling the CPU. Running in "high performance mode" the time to verify 128-in FCMP++ txs is more consistently around 12s. That is still slower than expected.

## j-berman | 2025-11-25T19:19:43+00:00
TBC, I would think verifying a 128-in FCMP++ tx would be in the ballpark of 4-6s on u/Lyza's CPU (it's ~3s on my ryzen 7950X3D). That gap in expected perf is worth further investigation.

## j-berman | 2025-12-09T20:22:58+00:00
I had u/Lyza run some tests. It appears something is causing slow mulithreaded verification, and at first pass doesn't seem related to #228.

### 1) Benchmark 1-in, 2-in, 4-in, 8-in, 128-in with [this perf test](https://github.com/j-berman/monero/blob/525bf681afbf4aeff4f937349575400bdcf67225/tests/performance_tests/fcmp_pp.h).

Timings are expected.

```
test_fcmp_pp_verify<1> (1000 calls) - OK: 39416 µs/call
test_fcmp_pp_verify<2> (100 calls) - OK: 61690 µs/call
test_fcmp_pp_verify<4> (100 calls) - OK: 107 ms/call
test_fcmp_pp_verify<8> (100 calls) - OK: 199 ms/call
test_fcmp_pp_verify<128> (8 calls) - OK: 4181 ms/call
```

### 2) Benchmark multithreaded 128-in verification with [this unit test](https://github.com/j-berman/monero/blob/525bf681afbf4aeff4f937349575400bdcf67225/tests/unit_tests/fcmp_pp.cpp#L672-L740).

It takes ~8-9s to verify all the 128-in proofs.

<details>
<summary>Show results</summary>

```
$ ./unit_tests --log-level 2 --gtest_filter="fcmp_pp.batch_verify_from_file"
Note: Google Test filter = fcmp_pp.batch_verify_from_file
[==========] Running 1 test from 1 test suite.
[----------] Global test environment set-up.
[----------] 1 test from fcmp_pp
[ RUN      ] fcmp_pp.batch_verify_from_file
2025-12-09 19:39:09.400	D signable_tx_hash: <0000000000000000000000000000000000000000000000000000000000000000>, proof_size: 140672, n_layers: 7, tree_root_bytes: <91f2ca72cf566564776bb3165bd6c494539d5a5cee781a52e527dfd475280198>
2025-12-09 19:39:09.400	I Verifying (n_inputs=128)
2025-12-09 19:39:15.652	I Successfully verified (n_inputs=128)
2025-12-09 19:39:15.652	I Batch verifying 8 FCMP++ txs, attempt 1
2025-12-09 19:39:15.652	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:39:15.652	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:39:15.652	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:39:15.652	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:39:15.652	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:39:15.652	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:39:15.652	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:39:15.652	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:39:15.652	D Verifying FCMP++ batch 4
2025-12-09 19:39:15.652	D Verifying FCMP++ batch 8
2025-12-09 19:39:15.652	D Verifying FCMP++ batch 7
2025-12-09 19:39:15.652	D Verifying FCMP++ batch 5
2025-12-09 19:39:15.653	D Verifying FCMP++ batch 3
2025-12-09 19:39:15.653	D Verifying FCMP++ batch 6
2025-12-09 19:39:15.653	D Verifying FCMP++ batch 2
2025-12-09 19:39:15.654	D Verifying FCMP++ batch 1
2025-12-09 19:39:23.853	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:39:24.014	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:39:24.059	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:39:24.070	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:39:24.078	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:39:24.095	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:39:24.097	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:39:24.143	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:39:24.143	I Successfully batch verified 8 FCMP++ txs, attempt 1
2025-12-09 19:39:24.143	I Batch verifying 8 FCMP++ txs, attempt 2
2025-12-09 19:39:24.143	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:39:24.143	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:39:24.143	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:39:24.143	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:39:24.143	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:39:24.143	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:39:24.143	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:39:24.143	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:39:24.143	D Verifying FCMP++ batch 7
2025-12-09 19:39:24.143	D Verifying FCMP++ batch 8
2025-12-09 19:39:24.144	D Verifying FCMP++ batch 6
2025-12-09 19:39:24.144	D Verifying FCMP++ batch 5
2025-12-09 19:39:24.144	D Verifying FCMP++ batch 4
2025-12-09 19:39:24.144	D Verifying FCMP++ batch 3
2025-12-09 19:39:24.144	D Verifying FCMP++ batch 2
2025-12-09 19:39:24.144	D Verifying FCMP++ batch 1
2025-12-09 19:39:32.522	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:39:32.522	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:39:32.526	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:39:32.546	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:39:32.567	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:39:32.575	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:39:32.627	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:39:32.645	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:39:32.645	I Successfully batch verified 8 FCMP++ txs, attempt 2
2025-12-09 19:39:32.645	I Batch verifying 8 FCMP++ txs, attempt 3
2025-12-09 19:39:32.645	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:39:32.645	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:39:32.645	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:39:32.645	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:39:32.645	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:39:32.645	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:39:32.645	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:39:32.645	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:39:32.645	D Verifying FCMP++ batch 7
2025-12-09 19:39:32.645	D Verifying FCMP++ batch 4
2025-12-09 19:39:32.645	D Verifying FCMP++ batch 6
2025-12-09 19:39:32.645	D Verifying FCMP++ batch 3
2025-12-09 19:39:32.645	D Verifying FCMP++ batch 5
2025-12-09 19:39:32.645	D Verifying FCMP++ batch 8
2025-12-09 19:39:32.645	D Verifying FCMP++ batch 2
2025-12-09 19:39:32.645	D Verifying FCMP++ batch 1
2025-12-09 19:39:40.961	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:39:40.969	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:39:40.977	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:39:40.988	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:39:40.990	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:39:40.998	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:39:41.016	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:39:41.061	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:39:41.061	I Successfully batch verified 8 FCMP++ txs, attempt 3
2025-12-09 19:39:41.062	I Batch verifying 8 FCMP++ txs, attempt 4
2025-12-09 19:39:41.062	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:39:41.062	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:39:41.062	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:39:41.062	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:39:41.062	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:39:41.062	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:39:41.062	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:39:41.062	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:39:41.062	D Verifying FCMP++ batch 8
2025-12-09 19:39:41.062	D Verifying FCMP++ batch 7
2025-12-09 19:39:41.062	D Verifying FCMP++ batch 5
2025-12-09 19:39:41.062	D Verifying FCMP++ batch 6
2025-12-09 19:39:41.062	D Verifying FCMP++ batch 3
2025-12-09 19:39:41.062	D Verifying FCMP++ batch 4
2025-12-09 19:39:41.063	D Verifying FCMP++ batch 2
2025-12-09 19:39:41.063	D Verifying FCMP++ batch 1
2025-12-09 19:39:49.369	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:39:49.384	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:39:49.390	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:39:49.403	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:39:49.408	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:39:49.409	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:39:49.431	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:39:49.468	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:39:49.468	I Successfully batch verified 8 FCMP++ txs, attempt 4
2025-12-09 19:39:49.469	I Batch verifying 8 FCMP++ txs, attempt 5
2025-12-09 19:39:49.469	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:39:49.469	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:39:49.469	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:39:49.469	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:39:49.469	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:39:49.469	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:39:49.469	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:39:49.469	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:39:49.469	D Verifying FCMP++ batch 8
2025-12-09 19:39:49.469	D Verifying FCMP++ batch 4
2025-12-09 19:39:49.469	D Verifying FCMP++ batch 7
2025-12-09 19:39:49.469	D Verifying FCMP++ batch 5
2025-12-09 19:39:49.469	D Verifying FCMP++ batch 3
2025-12-09 19:39:49.469	D Verifying FCMP++ batch 6
2025-12-09 19:39:49.469	D Verifying FCMP++ batch 2
2025-12-09 19:39:49.469	D Verifying FCMP++ batch 1
2025-12-09 19:39:57.810	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:39:57.816	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:39:57.819	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:39:57.822	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:39:57.824	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:39:57.830	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:39:57.844	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:39:57.915	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:39:57.915	I Successfully batch verified 8 FCMP++ txs, attempt 5
2025-12-09 19:39:57.915	I Batch verifying 8 FCMP++ txs, attempt 6
2025-12-09 19:39:57.915	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:39:57.915	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:39:57.915	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:39:57.915	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:39:57.915	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:39:57.915	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:39:57.915	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:39:57.915	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:39:57.915	D Verifying FCMP++ batch 4
2025-12-09 19:39:57.915	D Verifying FCMP++ batch 3
2025-12-09 19:39:57.915	D Verifying FCMP++ batch 5
2025-12-09 19:39:57.915	D Verifying FCMP++ batch 8
2025-12-09 19:39:57.915	D Verifying FCMP++ batch 7
2025-12-09 19:39:57.916	D Verifying FCMP++ batch 6
2025-12-09 19:39:57.916	D Verifying FCMP++ batch 2
2025-12-09 19:39:57.917	D Verifying FCMP++ batch 1
2025-12-09 19:40:06.230	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:40:06.255	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:40:06.255	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:40:06.262	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:40:06.268	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:40:06.269	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:40:06.294	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:40:06.357	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:40:06.357	I Successfully batch verified 8 FCMP++ txs, attempt 6
2025-12-09 19:40:06.357	I Batch verifying 8 FCMP++ txs, attempt 7
2025-12-09 19:40:06.357	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:40:06.357	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:40:06.357	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:40:06.357	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:40:06.357	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:40:06.357	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:40:06.357	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:40:06.357	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:40:06.357	D Verifying FCMP++ batch 8
2025-12-09 19:40:06.357	D Verifying FCMP++ batch 1
2025-12-09 19:40:06.357	D Verifying FCMP++ batch 6
2025-12-09 19:40:06.358	D Verifying FCMP++ batch 5
2025-12-09 19:40:06.358	D Verifying FCMP++ batch 7
2025-12-09 19:40:06.358	D Verifying FCMP++ batch 3
2025-12-09 19:40:06.358	D Verifying FCMP++ batch 2
2025-12-09 19:40:06.359	D Verifying FCMP++ batch 4
2025-12-09 19:40:14.713	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:40:14.718	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:40:14.734	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:40:14.736	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:40:14.747	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:40:14.749	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:40:14.753	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:40:14.838	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:40:14.838	I Successfully batch verified 8 FCMP++ txs, attempt 7
2025-12-09 19:40:14.839	I Batch verifying 8 FCMP++ txs, attempt 8
2025-12-09 19:40:14.839	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:40:14.839	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:40:14.839	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:40:14.839	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:40:14.839	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:40:14.839	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:40:14.839	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:40:14.839	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:40:14.839	D Verifying FCMP++ batch 8
2025-12-09 19:40:14.839	D Verifying FCMP++ batch 1
2025-12-09 19:40:14.839	D Verifying FCMP++ batch 6
2025-12-09 19:40:14.839	D Verifying FCMP++ batch 5
2025-12-09 19:40:14.839	D Verifying FCMP++ batch 4
2025-12-09 19:40:14.839	D Verifying FCMP++ batch 3
2025-12-09 19:40:14.839	D Verifying FCMP++ batch 2
2025-12-09 19:40:14.839	D Verifying FCMP++ batch 7
2025-12-09 19:40:23.190	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:40:23.190	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:40:23.193	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:40:23.203	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:40:23.211	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:40:23.225	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:40:23.229	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:40:23.231	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:40:23.231	I Successfully batch verified 8 FCMP++ txs, attempt 8
2025-12-09 19:40:23.231	I Batch verifying 8 FCMP++ txs, attempt 9
2025-12-09 19:40:23.231	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:40:23.231	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:40:23.231	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:40:23.231	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:40:23.231	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:40:23.231	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:40:23.231	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:40:23.231	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:40:23.231	D Verifying FCMP++ batch 8
2025-12-09 19:40:23.231	D Verifying FCMP++ batch 7
2025-12-09 19:40:23.231	D Verifying FCMP++ batch 4
2025-12-09 19:40:23.231	D Verifying FCMP++ batch 6
2025-12-09 19:40:23.231	D Verifying FCMP++ batch 5
2025-12-09 19:40:23.231	D Verifying FCMP++ batch 2
2025-12-09 19:40:23.231	D Verifying FCMP++ batch 3
2025-12-09 19:40:23.232	D Verifying FCMP++ batch 1
2025-12-09 19:40:31.542	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:40:31.550	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:40:31.558	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:40:31.564	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:40:31.564	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:40:31.572	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:40:31.616	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:40:31.642	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:40:31.642	I Successfully batch verified 8 FCMP++ txs, attempt 9
2025-12-09 19:40:31.642	I Batch verifying 8 FCMP++ txs, attempt 10
2025-12-09 19:40:31.643	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:40:31.643	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:40:31.643	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:40:31.643	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:40:31.643	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:40:31.643	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:40:31.643	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:40:31.643	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:40:31.643	D Verifying FCMP++ batch 7
2025-12-09 19:40:31.643	D Verifying FCMP++ batch 6
2025-12-09 19:40:31.643	D Verifying FCMP++ batch 8
2025-12-09 19:40:31.643	D Verifying FCMP++ batch 4
2025-12-09 19:40:31.643	D Verifying FCMP++ batch 5
2025-12-09 19:40:31.643	D Verifying FCMP++ batch 2
2025-12-09 19:40:31.645	D Verifying FCMP++ batch 3
2025-12-09 19:40:31.645	D Verifying FCMP++ batch 1
2025-12-09 19:40:40.001	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:40:40.003	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:40:40.023	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:40:40.024	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:40:40.041	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:40:40.065	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:40:40.076	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:40:40.119	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:40:40.119	I Successfully batch verified 8 FCMP++ txs, attempt 10
[       OK ] fcmp_pp.batch_verify_from_file (90720 ms)
[----------] 1 test from fcmp_pp (90720 ms total)

[----------] Global test environment tear-down
[==========] 1 test from 1 test suite ran. (90720 ms total)
[  PASSED  ] 1 test.
```

</details>

### 3) Same as 2, but setting `MALLOC_ARENA_MAX=8`, since the machine has 8 threads.

Still takes ~8-9s to verify all the 128-in proofs.


<details>
<summary>Show results</summary>

```
$ MALLOC_ARENA_MAX=8 ./unit_tests --log-level 2 --gtest_filter="fcmp_pp.batch_verify_from_file"
Note: Google Test filter = fcmp_pp.batch_verify_from_file
[==========] Running 1 test from 1 test suite.
[----------] Global test environment set-up.
[----------] 1 test from fcmp_pp
[ RUN      ] fcmp_pp.batch_verify_from_file
2025-12-09 19:55:47.809	D signable_tx_hash: <0000000000000000000000000000000000000000000000000000000000000000>, proof_size: 140672, n_layers: 7, tree_root_bytes: <91f2ca72cf566564776bb3165bd6c494539d5a5cee781a52e527dfd475280198>
2025-12-09 19:55:47.809	I Verifying (n_inputs=128)
2025-12-09 19:55:53.878	I Successfully verified (n_inputs=128)
2025-12-09 19:55:53.878	I Batch verifying 8 FCMP++ txs, attempt 1
2025-12-09 19:55:53.878	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:55:53.878	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:55:53.878	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:55:53.878	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:55:53.878	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:55:53.879	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:55:53.879	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:55:53.879	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:55:53.879	D Verifying FCMP++ batch 8
2025-12-09 19:55:53.879	D Verifying FCMP++ batch 7
2025-12-09 19:55:53.879	D Verifying FCMP++ batch 2
2025-12-09 19:55:53.879	D Verifying FCMP++ batch 6
2025-12-09 19:55:53.879	D Verifying FCMP++ batch 5
2025-12-09 19:55:53.879	D Verifying FCMP++ batch 4
2025-12-09 19:55:53.879	D Verifying FCMP++ batch 1
2025-12-09 19:55:53.882	D Verifying FCMP++ batch 3
2025-12-09 19:56:02.184	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:56:02.204	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:56:02.273	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:56:02.278	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:56:02.290	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:56:02.291	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:56:02.319	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:56:02.324	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:56:02.324	I Successfully batch verified 8 FCMP++ txs, attempt 1
2025-12-09 19:56:02.325	I Batch verifying 8 FCMP++ txs, attempt 2
2025-12-09 19:56:02.325	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:56:02.325	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:56:02.325	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:56:02.325	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:56:02.325	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:56:02.325	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:56:02.325	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:56:02.325	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:56:02.325	D Verifying FCMP++ batch 8
2025-12-09 19:56:02.325	D Verifying FCMP++ batch 1
2025-12-09 19:56:02.325	D Verifying FCMP++ batch 5
2025-12-09 19:56:02.325	D Verifying FCMP++ batch 6
2025-12-09 19:56:02.325	D Verifying FCMP++ batch 4
2025-12-09 19:56:02.325	D Verifying FCMP++ batch 3
2025-12-09 19:56:02.325	D Verifying FCMP++ batch 2
2025-12-09 19:56:02.325	D Verifying FCMP++ batch 7
2025-12-09 19:56:10.682	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:56:10.693	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:56:10.698	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:56:10.704	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:56:10.717	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:56:10.717	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:56:10.756	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:56:10.765	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:56:10.765	I Successfully batch verified 8 FCMP++ txs, attempt 2
2025-12-09 19:56:10.766	I Batch verifying 8 FCMP++ txs, attempt 3
2025-12-09 19:56:10.766	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:56:10.766	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:56:10.766	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:56:10.766	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:56:10.766	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:56:10.766	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:56:10.766	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:56:10.766	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:56:10.766	D Verifying FCMP++ batch 6
2025-12-09 19:56:10.766	D Verifying FCMP++ batch 7
2025-12-09 19:56:10.766	D Verifying FCMP++ batch 2
2025-12-09 19:56:10.766	D Verifying FCMP++ batch 3
2025-12-09 19:56:10.766	D Verifying FCMP++ batch 4
2025-12-09 19:56:10.766	D Verifying FCMP++ batch 5
2025-12-09 19:56:10.766	D Verifying FCMP++ batch 8
2025-12-09 19:56:10.766	D Verifying FCMP++ batch 1
2025-12-09 19:56:19.096	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:56:19.097	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:56:19.123	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:56:19.123	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:56:19.129	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:56:19.129	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:56:19.130	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:56:19.194	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:56:19.194	I Successfully batch verified 8 FCMP++ txs, attempt 3
2025-12-09 19:56:19.195	I Batch verifying 8 FCMP++ txs, attempt 4
2025-12-09 19:56:19.195	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:56:19.195	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:56:19.195	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:56:19.195	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:56:19.195	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:56:19.195	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:56:19.195	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:56:19.195	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:56:19.195	D Verifying FCMP++ batch 8
2025-12-09 19:56:19.195	D Verifying FCMP++ batch 6
2025-12-09 19:56:19.195	D Verifying FCMP++ batch 7
2025-12-09 19:56:19.195	D Verifying FCMP++ batch 4
2025-12-09 19:56:19.195	D Verifying FCMP++ batch 5
2025-12-09 19:56:19.195	D Verifying FCMP++ batch 3
2025-12-09 19:56:19.195	D Verifying FCMP++ batch 2
2025-12-09 19:56:19.199	D Verifying FCMP++ batch 1
2025-12-09 19:56:27.510	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:56:27.525	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:56:27.534	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:56:27.534	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:56:27.548	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:56:27.560	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:56:27.576	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:56:27.631	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:56:27.631	I Successfully batch verified 8 FCMP++ txs, attempt 4
2025-12-09 19:56:27.631	I Batch verifying 8 FCMP++ txs, attempt 5
2025-12-09 19:56:27.631	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:56:27.631	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:56:27.631	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:56:27.631	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:56:27.631	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:56:27.631	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:56:27.631	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:56:27.631	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:56:27.631	D Verifying FCMP++ batch 5
2025-12-09 19:56:27.631	D Verifying FCMP++ batch 2
2025-12-09 19:56:27.631	D Verifying FCMP++ batch 4
2025-12-09 19:56:27.631	D Verifying FCMP++ batch 8
2025-12-09 19:56:27.631	D Verifying FCMP++ batch 3
2025-12-09 19:56:27.631	D Verifying FCMP++ batch 7
2025-12-09 19:56:27.631	D Verifying FCMP++ batch 1
2025-12-09 19:56:27.634	D Verifying FCMP++ batch 6
2025-12-09 19:56:35.966	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:56:35.974	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:56:35.979	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:56:35.979	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:56:35.987	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:56:36.001	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:56:36.033	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:56:36.037	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:56:36.037	I Successfully batch verified 8 FCMP++ txs, attempt 5
2025-12-09 19:56:36.037	I Batch verifying 8 FCMP++ txs, attempt 6
2025-12-09 19:56:36.037	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:56:36.037	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:56:36.037	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:56:36.037	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:56:36.037	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:56:36.037	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:56:36.037	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:56:36.037	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:56:36.037	D Verifying FCMP++ batch 8
2025-12-09 19:56:36.037	D Verifying FCMP++ batch 6
2025-12-09 19:56:36.037	D Verifying FCMP++ batch 5
2025-12-09 19:56:36.037	D Verifying FCMP++ batch 3
2025-12-09 19:56:36.037	D Verifying FCMP++ batch 4
2025-12-09 19:56:36.037	D Verifying FCMP++ batch 7
2025-12-09 19:56:36.037	D Verifying FCMP++ batch 2
2025-12-09 19:56:36.041	D Verifying FCMP++ batch 1
2025-12-09 19:56:44.369	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:56:44.379	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:56:44.380	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:56:44.397	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:56:44.429	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:56:44.434	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:56:44.456	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:56:44.465	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:56:44.465	I Successfully batch verified 8 FCMP++ txs, attempt 6
2025-12-09 19:56:44.465	I Batch verifying 8 FCMP++ txs, attempt 7
2025-12-09 19:56:44.466	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:56:44.466	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:56:44.466	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:56:44.466	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:56:44.466	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:56:44.466	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:56:44.466	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:56:44.466	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:56:44.466	D Verifying FCMP++ batch 8
2025-12-09 19:56:44.466	D Verifying FCMP++ batch 5
2025-12-09 19:56:44.466	D Verifying FCMP++ batch 6
2025-12-09 19:56:44.466	D Verifying FCMP++ batch 4
2025-12-09 19:56:44.466	D Verifying FCMP++ batch 3
2025-12-09 19:56:44.466	D Verifying FCMP++ batch 2
2025-12-09 19:56:44.466	D Verifying FCMP++ batch 1
2025-12-09 19:56:44.467	D Verifying FCMP++ batch 7
2025-12-09 19:56:52.783	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:56:52.796	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:56:52.797	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:56:52.805	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:56:52.818	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:56:52.832	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:56:52.865	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:56:52.885	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:56:52.886	I Successfully batch verified 8 FCMP++ txs, attempt 7
2025-12-09 19:56:52.886	I Batch verifying 8 FCMP++ txs, attempt 8
2025-12-09 19:56:52.886	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:56:52.886	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:56:52.886	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:56:52.886	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:56:52.886	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:56:52.886	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:56:52.886	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:56:52.886	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:56:52.886	D Verifying FCMP++ batch 8
2025-12-09 19:56:52.886	D Verifying FCMP++ batch 1
2025-12-09 19:56:52.886	D Verifying FCMP++ batch 6
2025-12-09 19:56:52.886	D Verifying FCMP++ batch 5
2025-12-09 19:56:52.886	D Verifying FCMP++ batch 2
2025-12-09 19:56:52.886	D Verifying FCMP++ batch 4
2025-12-09 19:56:52.886	D Verifying FCMP++ batch 7
2025-12-09 19:56:52.886	D Verifying FCMP++ batch 3
2025-12-09 19:57:01.237	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:57:01.237	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:57:01.241	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:57:01.242	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:57:01.244	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:57:01.245	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:57:01.255	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:57:01.326	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:57:01.326	I Successfully batch verified 8 FCMP++ txs, attempt 8
2025-12-09 19:57:01.326	I Batch verifying 8 FCMP++ txs, attempt 9
2025-12-09 19:57:01.326	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:57:01.326	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:57:01.326	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:57:01.326	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:57:01.326	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:57:01.326	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:57:01.326	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:57:01.326	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:57:01.326	D Verifying FCMP++ batch 8
2025-12-09 19:57:01.326	D Verifying FCMP++ batch 7
2025-12-09 19:57:01.327	D Verifying FCMP++ batch 4
2025-12-09 19:57:01.327	D Verifying FCMP++ batch 5
2025-12-09 19:57:01.327	D Verifying FCMP++ batch 6
2025-12-09 19:57:01.327	D Verifying FCMP++ batch 3
2025-12-09 19:57:01.327	D Verifying FCMP++ batch 2
2025-12-09 19:57:01.327	D Verifying FCMP++ batch 1
2025-12-09 19:57:09.658	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:57:09.663	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:57:09.666	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:57:09.669	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:57:09.675	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:57:09.679	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:57:09.695	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:57:09.762	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:57:09.762	I Successfully batch verified 8 FCMP++ txs, attempt 9
2025-12-09 19:57:09.762	I Batch verifying 8 FCMP++ txs, attempt 10
2025-12-09 19:57:09.762	D FCMP++ batch 1 has 128 total inputs across 1 txs
2025-12-09 19:57:09.762	D FCMP++ batch 2 has 128 total inputs across 1 txs
2025-12-09 19:57:09.762	D FCMP++ batch 3 has 128 total inputs across 1 txs
2025-12-09 19:57:09.762	D FCMP++ batch 4 has 128 total inputs across 1 txs
2025-12-09 19:57:09.762	D FCMP++ batch 5 has 128 total inputs across 1 txs
2025-12-09 19:57:09.762	D FCMP++ batch 6 has 128 total inputs across 1 txs
2025-12-09 19:57:09.762	D FCMP++ batch 7 has 128 total inputs across 1 txs
2025-12-09 19:57:09.762	D FCMP++ batch 8 has 128 total inputs across 1 txs
2025-12-09 19:57:09.762	D Verifying FCMP++ batch 8
2025-12-09 19:57:09.762	D Verifying FCMP++ batch 7
2025-12-09 19:57:09.762	D Verifying FCMP++ batch 6
2025-12-09 19:57:09.762	D Verifying FCMP++ batch 5
2025-12-09 19:57:09.762	D Verifying FCMP++ batch 3
2025-12-09 19:57:09.762	D Verifying FCMP++ batch 4
2025-12-09 19:57:09.762	D Verifying FCMP++ batch 2
2025-12-09 19:57:09.762	D Verifying FCMP++ batch 1
2025-12-09 19:57:18.087	D Finished verifying FCMP++ batch 5 / 8
2025-12-09 19:57:18.099	D Finished verifying FCMP++ batch 6 / 8
2025-12-09 19:57:18.102	D Finished verifying FCMP++ batch 4 / 8
2025-12-09 19:57:18.105	D Finished verifying FCMP++ batch 3 / 8
2025-12-09 19:57:18.122	D Finished verifying FCMP++ batch 8 / 8
2025-12-09 19:57:18.143	D Finished verifying FCMP++ batch 7 / 8
2025-12-09 19:57:18.160	D Finished verifying FCMP++ batch 1 / 8
2025-12-09 19:57:18.166	D Finished verifying FCMP++ batch 2 / 8
2025-12-09 19:57:18.166	I Successfully batch verified 8 FCMP++ txs, attempt 10
[       OK ] fcmp_pp.batch_verify_from_file (90358 ms)
[----------] 1 test from fcmp_pp (90358 ms total)

[----------] Global test environment tear-down
[==========] 1 test from 1 test suite ran. (90358 ms total)
[  PASSED  ] 1 test.
````

</details>


## j-berman | 2025-12-11T19:04:47+00:00
Confirmed u/Lyza's slowness was caused by the depends build. When using the GUIX build, their sync averaged an expected ~5s for 128-in verify.

See https://github.com/seraphis-migration/monero/issues/259#issuecomment-3643006549 for an explanation of why the depends build is slower than GUIX.

______

I do still note that it's unexpected how much slower 8-thread 8x 128-in parallel verify is, but that's a separate thing.

# Action History
- Created by: j-berman | 2025-11-22T20:07:16+00:00
- Closed at: 2025-12-11T19:04:47+00:00
