---
title: Deprecating `-Ofast`
source_url: https://github.com/monero-project/monero/issues/9407
author: '0xFFFC0000'
assignees: []
labels:
- enhancement
- easy
- build system
created_at: '2024-07-27T08:44:07+00:00'
updated_at: '2026-05-26T00:37:16+00:00'
type: issue
status: closed
closed_at: '2026-05-26T00:37:16+00:00'
---

# Original Description
Clang merged a warning for `-Ofast` few days ago, and they are going to deprecate it. 

We need to disable and change our `-Ofast` flag. 

https://github.com/llvm/llvm-project/commit/2ef7cbf71c98


https://github.com/monero-project/monero/blob/caa62bc9ea1c5f2ffe3ffa440ad230e1de509bfd/CMakeLists.txt#L349


# Discussion History
## SpaceSleuth | 2024-07-28T02:06:10+00:00
Pull request: https://github.com/monero-project/monero/pull/9409

## selsta | 2026-05-26T00:37:11+00:00
#10312

# Action History
- Created by: 0xFFFC0000 | 2024-07-27T08:44:07+00:00
- Closed at: 2026-05-26T00:37:16+00:00
