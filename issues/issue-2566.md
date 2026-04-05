---
title: 'Stupid question: how to disable 1gb hugepage'
source_url: https://github.com/xmrig/xmrig/issues/2566
author: SatoKentaNayoro
assignees: []
labels: []
created_at: '2021-08-29T16:08:57+00:00'
updated_at: '2021-11-18T12:41:32+00:00'
type: issue
status: closed
closed_at: '2021-11-18T12:41:32+00:00'
---

# Original Description
how to disable 1gb hugepage 0.0

# Discussion History
## DeeDeeRanged | 2021-09-03T10:03:19+00:00
In config.json file

    "cpu": {
        "enabled": true,
        "huge-pages": false,
        "huge-pages-jit": false,

"randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,


## chenjiaqi001 | 2021-09-24T03:44:16+00:00
好像只有Linux可以使用1GB-HUGEPAGE

## Spudz76 | 2021-09-24T12:43:12+00:00
正确的

# Action History
- Created by: SatoKentaNayoro | 2021-08-29T16:08:57+00:00
- Closed at: 2021-11-18T12:41:32+00:00
