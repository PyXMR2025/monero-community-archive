---
title: 'Unchecked malloc return NULL vulnerability '
source_url: https://github.com/xmrig/xmrig/issues/2152
author: vulnerabilitydetectionlearning
assignees: []
labels: []
created_at: '2021-03-02T17:52:41+00:00'
updated_at: '2021-04-12T14:08:23+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:08:23+00:00'
---

# Original Description
**Describe the bug**
Does not check for the return value of `_mm_malloc` in `CnCtx.cpp` which could return NULL if the memory allocation is unsuccessful. Operating on null pointers can cause unexpected behavior. See https://cwe.mitre.org/data/definitions/690.html for detail on the potential vulnerability. 

**Exact Location**
https://github.com/xmrig/xmrig/blob/4c5421b2bf3622e81971084cbe2bbfab23fc8208/src/crypto/cn/CnCtx.cpp#L36-L48

Line 39 is the memory allocation is question



# Discussion History
# Action History
- Created by: vulnerabilitydetectionlearning | 2021-03-02T17:52:41+00:00
- Closed at: 2021-04-12T14:08:23+00:00
