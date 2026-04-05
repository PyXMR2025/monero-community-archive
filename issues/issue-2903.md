---
title: Compilation on Alpine 3.15 fails on building openssl dependency
source_url: https://github.com/xmrig/xmrig/issues/2903
author: lfaoro
assignees: []
labels: []
created_at: '2022-01-26T10:39:19+00:00'
updated_at: '2022-01-26T10:39:47+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
openssl 1.1.1l fails compiling on alpine linux 3.15 (latest)

```ui_openssl.c:(.text+0x531): undefined reference to `__fprintf_chk'
/usr/lib/gcc/x86_64-alpine-linux-musl/10.3.1/../../../../x86_64-alpine-linux-musl/bin/ld: ./libcrypto.a(p5_scrypt.o): in function `PKCS5_pbe2_set_scrypt':
p5_scrypt.c:(.text+0x131): undefined reference to `__memcpy_chk'
collect2: error: ld returned 1 exit status
make[1]: *** [Makefile:6554: fuzz/asn1-test] Error 1
make[1]: *** Waiting for unfinished jobs....
make[1]: Leaving directory '/build/scripts/build/openssl-1.1.1l'
make: *** [Makefile:174: all] Error 2```

I resolved by editing `build.openssl.sh` and editing the version from `1.1.1l` to `1.1.1m`.

# Discussion History
# Action History
- Created by: lfaoro | 2022-01-26T10:39:19+00:00
