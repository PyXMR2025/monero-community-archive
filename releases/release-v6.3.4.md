---
title: v6.3.4
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.3.4
author: xmrig
tag_name: v6.3.4
published_at: '2020-09-22T23:39:25+00:00'
---

# Version: v6.3.4

# Release Notes
## Notes
- **[KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915) :new:**
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.3.4
- [#1823](https://github.com/xmrig/xmrig/pull/1823) RandomX: added new option `scratchpad_prefetch_mode`.
- [#1827](https://github.com/xmrig/xmrig/pull/1827) [#1831](https://github.com/xmrig/xmrig/pull/1831) Improved nonce iteration performance.
- [#1828](https://github.com/xmrig/xmrig/pull/1828) RandomX: added SSE4.1-optimized Blake2b.
- [#1830](https://github.com/xmrig/xmrig/pull/1830) RandomX: added performance profiler (for developers).
- [#1835](https://github.com/xmrig/xmrig/pull/1835) RandomX: returned old soft AES implementation and added auto-select between the two.
- [#1840](https://github.com/xmrig/xmrig/pull/1840) RandomX: moved more stuff to compile time, small x86 JIT compiler speedup.
- [#1841](https://github.com/xmrig/xmrig/pull/1841) Fixed Cryptonight OpenCL for AMD 20.7.2 drivers.
- [#1842](https://github.com/xmrig/xmrig/pull/1842) RandomX: AES improvements, a bit faster hardware AES code when compiled with MSVC.
- [#1843](https://github.com/xmrig/xmrig/pull/1843) RandomX: improved performance of GCC compiled binaries.

## SHA256SUMS
```
be454402c69ba3bd3cd0786c2257c06c7af7016ebc4981f74e59bfda3ef6f41d *xmrig-6.3.4-bionic-x64.tar.gz
f1a9c3e8d607f3cf2ac9c2866c8133f0ebff1dabee78c66203e4c28a3f7beea3 *xmrig-6.3.4-focal-x64.tar.gz
8936c9574a1ce319408f965d82fac216a8f933ee0e1a197a8f587fe8c9aef086 *xmrig-6.3.4-freebsd-static-x64.tar.gz
06bf41f7854fb7cfbc90c7a283fe5aefd9c273fd49c69d3946bb83500b22c0ec *xmrig-6.3.4-linux-static-x64.tar.gz
50da5d8bafe3f754fadd83063f53be69d28c62ed351d9bfc71b9b5dcb48a4e46 *xmrig-6.3.4-linux-x64.tar.gz
8ae5441571bd5978eecf82de2732ee516624390dcfc48e4e84abb22d0356c3dc *xmrig-6.3.4-macos-x64.tar.gz
38c4c99d927dc16ea22cdfe692a09151b3fb555c123cf88774ee373b9067952f *xmrig-6.3.4-gcc-win64.zip
86a48e71773071d945301d6de4b4c2303de8e82e728cde877cb9ae07cb373007 *xmrig-6.3.4-msvc-cuda10_2-win64.zip
344e738f9c4a8ea30f959ba410d5b27d3898d1e5c8f712377b1921ca30763a1c *xmrig-6.3.4-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl9qiAQACgkQRGpTY4vp
RAniKggAnbmIOTejqRLtVOxDH5fnTyTgfgB+O+9hcheoW2VTju+X1VjVi6vapCfM
KR0GU9M2Kg8O/ST50MTHXiLbDtyKVAhHx5Bvr7UFjQWbDC21/y5LMlbTMwlPImwa
7V+cmF41j1vHRzh6BiB06FvR+IfZmpUv+Hc1GQnzsp4t3w4DPRXBZUH27bKPLz8R
a9BeUcNq7ko1at30V4ltacg1sZhmYPTmXD8iTMHI0lBKyD/E4rkvrP9tBJryYlGh
BcVuXMYHhj9Zqap4BdI0r90yEAnBGEKkibrF1jVBEdw5qkkqwOH4J1ffZta80ylI
9da8FN9IqxpO1bu59JxGwo18nH9UQQ==
=vSrP
-----END PGP SIGNATURE-----
```