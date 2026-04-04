---
title: 'PR #3303 breaks build for non x86_64 architectures'
source_url: https://github.com/monero-project/monero/issues/3393
author: m2049r
assignees: []
labels: []
created_at: '2018-03-13T07:36:06+00:00'
updated_at: '2018-03-14T15:32:51+00:00'
type: issue
status: closed
closed_at: '2018-03-14T15:32:51+00:00'
---

# Original Description
```crypto/chacha.h``` calls ```cn_slow_hash_pre()``` from ```crypto/slow_hash.c``` but this method is only compiled for
```C
#if !defined NO_AES && (defined(__x86_64__) || (defined(_MSC_VER) && defined(_WIN64)))
```
and so, builds for arm & x86 fail with ```error: undefined reference to 'cn_slow_hash_pre'```

# Discussion History
## stoffu | 2018-03-13T07:52:38+00:00
#3350 

## moneromooo-monero | 2018-03-14T15:26:05+00:00
+resolved

# Action History
- Created by: m2049r | 2018-03-13T07:36:06+00:00
- Closed at: 2018-03-14T15:32:51+00:00
