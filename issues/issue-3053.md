---
title: '[Feature Request] KAWPOW OpenCL Benchmark'
source_url: https://github.com/xmrig/xmrig/issues/3053
author: iamhumanipromise
assignees: []
labels: []
created_at: '2022-05-20T06:28:22+00:00'
updated_at: '2025-06-28T10:35:41+00:00'
type: issue
status: closed
closed_at: '2025-06-28T10:35:41+00:00'
---

# Original Description
Requesting a benchmark mode for the KAWPOW algorithm to just run a benchmark to simulate OpenCL hashrate, similar to the existing benchmarks. 

Would also be a great way to test that all headers are correctly configured, etc, without messing with a config file. 



# Discussion History
## Spudz76 | 2022-05-21T03:18:11+00:00
You can (ab)use [`meta-miner`](https://github.com/MoneroOcean/meta-miner) to benchmark things.  It normally functions as a proxy but in the setup phases it benchmarks all configured algorithms with canned jobs which I have used as a test-harness before.

EDIT: to note, using the MO fork of xmrig with its internal benchmarking, does not work for OpenCL anyway (never returns / doesn't sense "ready").  So don't bother with that as a benchmarking hack unless you're testing CPU or CUDA.

# Action History
- Created by: iamhumanipromise | 2022-05-20T06:28:22+00:00
- Closed at: 2025-06-28T10:35:41+00:00
