---
title: v6.22.3
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.22.3
author: xmrig
tag_name: v6.22.3
published_at: '2025-06-04T11:46:58+00:00'
---

# Version: v6.22.3

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on X https://x.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.22.3
- [#3605](https://github.com/xmrig/xmrig/pull/3605) CUDA backend: added missing RandomX dataset update.
- [#3646](https://github.com/xmrig/xmrig/pull/3646) Optimized auto-config for AMD CPUs with less than 2 MB L3 cache per thread.
- [#3652](https://github.com/xmrig/xmrig/pull/3652) Fixed possible crash when submitting RandomX benchmark.
- [#3662](https://github.com/xmrig/xmrig/pull/3662) Fixed OpenCL kernel compilation error on some platforms.

## SHA256SUMS
```
c592b6b21a598ea05b2bb3742c2ef1939556b71d294ed6049c6700b6858047a2 *xmrig-6.22.3-focal-x64.tar.gz
9893d96337fc0dfa76938689710fe4237c5814eab89a11003f5c31f316b4e229 *xmrig-6.22.3-freebsd-static-x64.tar.gz
bab1fc66cea8738a9111cf730fce3118df44fe01b8ad10169ec84d3def5ccb65 *xmrig-6.22.3-gcc-win64.zip
9f2422b859a077a79ca4a78c883022e541ce184df6d8cd6c0513960db1b832c0 *xmrig-6.22.3-jammy-x64.tar.gz
1715856e020416dd8cca17f45eceb55a17bcff7388bac1bba4e2d1bd1c6f05b5 *xmrig-6.22.3-linux-static-x64.tar.gz
54f2cf48ad1ccb829dd06ede76e92120f40fe646b151e0d66b6d4e16f7b57816 *xmrig-6.22.3-macos-arm64.tar.gz
8aa7fcbaa8bc97b3f30267eae00ec966982733d88fd8c2b9e09126f5aabd4fd9 *xmrig-6.22.3-macos-x64.tar.gz
30ad4377f17ddd590837470279f28b02a0af035b7df0761aca24e4308d0dc125 *xmrig-6.22.3-msvc-win64.zip
d9d412bb83584b8ea1b02cb708967647c988b281004c038c7674570bb92e63d5 *xmrig-6.22.3-noble-x64.tar.gz
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmhALn4ACgkQRGpTY4vp
RAlMnwf/Rj8tQwrqG8Ia8RxcrJE0z3dpEicbwN+6/tAF1UpWbCMfA7nCJo58rEfb
h/oUMChmu4RcKTKKy801+VQfQQLaIas/IR6JDdJ2KoZwNoJskyNwx8PSAB+ptOI2
TJHu0olZQVRcQ9aeicarrUqXl/UjeiDZBpgndFWm0eR0XGcgg84m4+B8YabRsOvy
+IIF99bLPWMuTSJDooEn8kSU15gxABsN8YubJVNKbDk07DfGXMI6sHXicu6fBU43
FqTGPVXhSeVHXbUEWtWgEYwb1AMbuwfoCsrCG9+4e3EjUxsGRoZRS2JBhavFgJhF
eYtVn5kaxzt4c4d7ctDcrJ5NUUj99w==
=IHZY
-----END PGP SIGNATURE-----
```