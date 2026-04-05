---
title: Out-of-memory crash using default config for RX (RTX 2070 SUPER)
source_url: https://github.com/xmrig/xmrig/issues/1595
author: YetAnotherRussian
assignees: []
labels: []
created_at: '2020-03-13T13:37:56+00:00'
updated_at: '2021-04-12T14:59:26+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:59:26+00:00'
---

# Original Description
Default config (auto-generated):

"index": 0,
"threads": 32,
"blocks": 80,
"bfactor": 6,
"bsleep": 25,
"affinity": -1,
"dataset_host": false

nv   thread #0 failed with error <randomx_prepare>:43 "out of memory"

RTX 2070 SUPER
Shading Units: 2560
Mem: 8Gb
SMX count: 40 

Should be at least:

"index": 0,
"threads": 32,
"blocks": 40,
"bfactor": 6,
"bsleep": 25,
"affinity": -1,
"dataset_host": false

or (max performance):

"index": 0,
"threads": 16,
"blocks": 80,
"bfactor": 6,
"bsleep": 25,
"affinity": -1,
"dataset_host": false

# Discussion History
# Action History
- Created by: YetAnotherRussian | 2020-03-13T13:37:56+00:00
- Closed at: 2021-04-12T14:59:26+00:00
