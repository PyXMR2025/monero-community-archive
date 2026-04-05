---
title: Warnings while compile on CentOS 8
source_url: https://github.com/xmrig/xmrig/issues/2043
author: xsistema
assignees: []
labels: []
created_at: '2021-01-17T00:15:43+00:00'
updated_at: '2021-04-12T14:24:19+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:24:19+00:00'
---

# Original Description
Nothing critical, but I see some warnings when launching `make` on CentOS 8:

```
~/xmrig/src/crypto/randomx/aes_hash.cpp: In lambda function:
~/xmrig/src/crypto/randomx/aes_hash.cpp:396:62: warning: comparison of integer expressions of different signedness: ‘uint64_t’ {aka ‘long unsigned int’} and ‘const int’ [-Wsign-compare]
           } while (xmrig::Chrono::highResolutionMSecs() - t1 < test_length_ms);
```

Perhaps it is worth to do some changes?

# Discussion History
## xmrig | 2021-01-17T10:49:25+00:00
Should be fixed in dev branch.
Thank you.

# Action History
- Created by: xsistema | 2021-01-17T00:15:43+00:00
- Closed at: 2021-04-12T14:24:19+00:00
