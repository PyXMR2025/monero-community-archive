---
title: Benchmark mode should filter VM's / database needs cleanup
source_url: https://github.com/xmrig/xmrig/issues/2997
author: Spudz76
assignees: []
labels:
- review later
created_at: '2022-03-28T23:49:09+00:00'
updated_at: '2025-06-18T22:58:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Benchmark submit should refuse when in any sort of VM machine.

Please mass-delete any existing results with VMWare in the machine name, it will only cause confusion and is not a benchmark of the hardware in question.

Such as:

https://xmrig.com/benchmark/2Q8u4v
https://xmrig.com/benchmark/6FJber

There is only one of three benchmarks on a real baremetal [EPYC 7313](https://xmrig.com/benchmark?cpu=AMD+EPYC+7313+16-Core+Processor)

# Discussion History
# Action History
- Created by: Spudz76 | 2022-03-28T23:49:09+00:00
