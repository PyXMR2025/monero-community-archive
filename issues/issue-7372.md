---
title: Prevent randomx from polluting monerod log.
source_url: https://github.com/monero-project/monero/issues/7372
author: crocket
assignees: []
labels: []
created_at: '2021-02-11T14:31:19+00:00'
updated_at: '2022-07-19T20:21:48+00:00'
type: issue
status: closed
closed_at: '2022-07-19T20:18:54+00:00'
---

# Original Description
Unless huge pages are enabled by a command like `sysctl vm.nr_hugepages=1280`, randomx large page allocator keeps printing exceptions in monerod log.

It occupies almost 100% of monerod log. I can't analyze monerod log at all because of the large page allocator exceptions.

This problem should be documented or fixed properly.

# Discussion History
## selsta | 2022-07-19T20:19:24+00:00
Fixed in https://github.com/tevador/RandomX/pull/241

## hyc | 2022-07-19T20:21:48+00:00
Fixed by #8312

# Action History
- Created by: crocket | 2021-02-11T14:31:19+00:00
- Closed at: 2022-07-19T20:18:54+00:00
