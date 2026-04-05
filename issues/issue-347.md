---
title: 4way for internal algos
source_url: https://github.com/xmrig/xmrig/issues/347
author: YetAnotherRussian
assignees: []
labels:
- enhancement
created_at: '2018-01-17T17:31:19+00:00'
updated_at: '2019-08-02T12:42:40+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:42:40+00:00'
---

# Original Description
Some algos used in cryptonight may benefit from 4way, example: 
https://github.com/JayDDee/cpuminer-opt/tree/master/algo/skein
https://github.com/JayDDee/cpuminer-opt/tree/master/algo/keccak
https://github.com/JayDDee/cpuminer-opt/tree/master/algo/blake
https://github.com/JayDDee/cpuminer-opt/tree/master/algo/jh

This cannot be ported directly, but you may take a look at possibilty to have a separate build of xmrig, or add some switches depending on CPU capabilities.

# Discussion History
## 2010phenix | 2018-01-21T20:10:43+00:00
and if already have example in clean C, maybe add this one to classic xmrig miner version too.

# Action History
- Created by: YetAnotherRussian | 2018-01-17T17:31:19+00:00
- Closed at: 2019-08-02T12:42:40+00:00
