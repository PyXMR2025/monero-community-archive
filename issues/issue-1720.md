---
title: Compiler warning in cn_slow_hash - nested externs
source_url: https://github.com/monero-project/monero/issues/1720
author: ghost
assignees: []
labels: []
created_at: '2017-02-12T23:03:31+00:00'
updated_at: '2017-02-24T06:06:02+00:00'
type: issue
status: closed
closed_at: '2017-02-24T06:06:02+00:00'
---

# Original Description
It's been around for quite a while now. Pretty sure it's nothing but should be reported nonetheless.

Ubuntu 16.04. GCC 5.4.1. ARMv8

@hyc any simple fixes?

```
/home/nodey/monero/src/crypto/slow-hash.c: In function ‘cn_slow_hash’:
/home/nodey/monero/src/crypto/slow-hash.c:1090:13: warning: implicit declaration of function ‘aesb_pseudo_round’ [-Wimplicit-function-declaration]
             aesb_pseudo_round(&text[AES_BLOCK_SIZE * j], &text[AES_BLOCK_SIZE * j], expandedKey);
             ^
/home/nodey/monero/src/crypto/slow-hash.c:1090:13: warning: nested extern declaration of ‘aesb_pseudo_round’ [-Wnested-externs]
/home/nodey/monero/src/crypto/slow-hash.c:1106:7: warning: implicit declaration of function ‘aesb_single_round’ [-Wimplicit-function-declaration]
       aesb_single_round(p, p, a);
       ^
/home/nodey/monero/src/crypto/slow-hash.c:1106:7: warning: nested extern declaration of ‘aesb_single_round’ [-Wnested-externs]
```

# Discussion History
## hyc | 2017-02-12T23:34:55+00:00
Probably just move the declarations from lines 141-142 to outside of whatever ifdef, so they're present for both x86 and ARM builds.

## ghost | 2017-02-24T06:06:02+00:00
Closing

# Action History
- Created by: ghost | 2017-02-12T23:03:31+00:00
- Closed at: 2017-02-24T06:06:02+00:00
