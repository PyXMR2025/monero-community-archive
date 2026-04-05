---
title: Compiling STATIC=ON doesn't produce a static binary -- dep on glibc
source_url: https://github.com/xmrig/xmrig/issues/2902
author: lfaoro
assignees: []
labels:
- question
created_at: '2022-01-26T10:34:09+00:00'
updated_at: '2022-04-03T08:10:03+00:00'
type: issue
status: closed
closed_at: '2022-04-03T08:10:03+00:00'
---

# Original Description
the compiler warns us:
```../scripts/deps/lib/libcrypto.a(b_sock.o): In function `BIO_gethostbyname':
b_sock.c:(.text+0x71): warning: Using 'gethostbyname' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking```

On older systems the static binary which is not really static may throw errors e.g. `/lib64/libc.so.6: version `GLIBC_2.25'`

# Discussion History
## Spudz76 | 2022-01-26T11:00:29+00:00
Static builds use non-glibc library that does support full static compilation, like uClibc or such

# Action History
- Created by: lfaoro | 2022-01-26T10:34:09+00:00
- Closed at: 2022-04-03T08:10:03+00:00
