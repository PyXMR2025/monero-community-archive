---
title: Build error when disable WITH_AEON (dev branch)
source_url: https://github.com/xmrig/xmrig/issues/111
author: yoyohip
assignees: []
labels:
- bug
created_at: '2017-09-16T09:22:39+00:00'
updated_at: '2017-09-16T13:48:31+00:00'
type: issue
status: closed
closed_at: '2017-09-16T13:48:31+00:00'
---

# Original Description
Hi,
error occured.
    return memcmp(output, algo == Options::ALGO_CRYPTONIGHT_LITE ? test_output1 : test_output0, (Options::i()->doubleHash() ? 64 : 32)) == 0;

Thank you.

# Discussion History
## xmrig | 2017-09-16T12:21:10+00:00
I fixed it. Thank you.

## yoyohip | 2017-09-16T13:22:32+00:00
Thank you!

# Action History
- Created by: yoyohip | 2017-09-16T09:22:39+00:00
- Closed at: 2017-09-16T13:48:31+00:00
