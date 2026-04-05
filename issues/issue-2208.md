---
title: Add memory specifications to workers web interface
source_url: https://github.com/xmrig/xmrig/issues/2208
author: BillGatesIII
assignees: []
labels:
- review later
created_at: '2021-03-25T10:43:26+00:00'
updated_at: '2021-04-12T13:48:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
You already added memory info to the benchmark results which I very like.

[Add memory specifications to benchmark information](https://github.com/xmrig/xmrig/issues/2038)

Can you also add it to the workers web interface? So I can test different memory layouts and dimms without having to submit a benchmark.

Thank you.

# Discussion History
## Spudz76 | 2021-03-28T06:59:38+00:00
Already available at `/2/dmi` is that sufficient?

EDIT: oops you might mean http://workers.xmrig.info/ which I didn't even know existed

## BillGatesIII | 2021-03-28T07:27:04+00:00
That will do, thanks. I indeed mean the workers page and there you can create an API request.

Where do I find the API documentation?

## Spudz76 | 2021-03-29T21:01:32+00:00
[Here](https://github.com/xmrig/xmrig/blob/master/doc/API.md#endpoints) however there have been some added but not yet documented (such as the `/2/dmi')

# Action History
- Created by: BillGatesIII | 2021-03-25T10:43:26+00:00
