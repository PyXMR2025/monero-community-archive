---
title: Compile Error
source_url: https://github.com/xmrig/xmrig/issues/1132
author: vergotle
assignees: []
labels:
- bug
created_at: '2019-08-21T11:34:46+00:00'
updated_at: '2019-12-21T20:11:59+00:00'
type: issue
status: closed
closed_at: '2019-12-21T20:11:59+00:00'
---

# Original Description
Hi

When compiling Xmrig 3.1.0 on Centos 7 using Cmake v3, the compiler exits with the following error

/tmp/xmrig-3.1.0/src/crypto/randomx/reciprocal.c: In function ‘randomx_reciprocal’:
/tmp/xmrig-3.1.0/src/crypto/randomx/reciprocal.c:57:2: error: ‘for’ loop initial declarations are only allowed in C99 mode
  for (uint64_t bit = divisor; bit > 0; bit >>= 1)
  ^
/tmp/xmrig-3.1.0/src/crypto/randomx/reciprocal.c:57:2: note: use option -std=c99 or -std=gnu99 to compile your code
/tmp/xmrig-3.1.0/src/crypto/randomx/reciprocal.c:60:2: error: ‘for’ loop initial declarations are only allowed in C99 mode
  for (unsigned shift = 0; shift < bsr; shift++)


# Discussion History
## TheCHIM | 2019-09-02T06:26:02+00:00
I confirm, I have the same error!

## srax47 | 2019-09-14T16:32:26+00:00
Same error here

## xmrig | 2019-09-14T17:14:34+00:00
Compiler version? `gcc -v`

## xmrig | 2019-09-15T06:27:06+00:00
Fixed in dev branch.

# Action History
- Created by: vergotle | 2019-08-21T11:34:46+00:00
- Closed at: 2019-12-21T20:11:59+00:00
