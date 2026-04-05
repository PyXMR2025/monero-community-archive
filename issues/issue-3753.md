---
title: build warning
source_url: https://github.com/xmrig/xmrig/issues/3753
author: bbbfkl
assignees: []
labels: []
created_at: '2026-01-08T05:03:36+00:00'
updated_at: '2026-01-08T11:20:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The following warning appears when static compiling: 

/usr/bin/ld: .. /scripts/deps/lib/libcrypto.a(libcrypto-lib-dso_dlfcn.o): in function `dlfcn_globallookup':
dso_dlfcn.c:(.text 0x17): warning: Using 'dlopen' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking
/usr/bin/ld: .. /scripts/deps/lib/libuv.a(libuv_la-core.o): in function `uv_os_get_group':
/home/cap/Desktop/xmrig-6.24.0/scripts/build/libuv-v1.51.0/src/unix/core.c:1381: warning: Using 'getgrgid_r' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking
/usr/bin/ld: .. /scripts/deps/lib/libuv.a(libuv_la-core.o): in function `uv__getpwuid_r':
/home/cap/Desktop/xmrig-6.24.0/scripts/build/libuv-v1.51.0/src/unix/core.c:1305: warning: Using 'getpwuid_r' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking
/usr/bin/ld: .. /scripts/deps/lib/libcrypto.a(libcrypto-lib-bio_addr.o): in function `BIO_lookup_ex':
bio_addr.c:(.text 0xd83): warning: Using 'getaddrinfo' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking
/usr/bin/ld: .. /scripts/deps/lib/libcrypto.a(libcrypto-lib-bio_sock.o): in function `BIO_gethostbyname':
bio_sock.c:(.text 0x75): warning: Using 'gethostbyname' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking 

How should I fix it thanks

# Discussion History
## SChernykh | 2026-01-08T11:20:00+00:00
Static compiling works in Alpine Linux which uses musl: https://xmrig.com/docs/miner/build/alpine

# Action History
- Created by: bbbfkl | 2026-01-08T05:03:36+00:00
