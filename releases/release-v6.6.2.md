---
title: v6.6.2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.6.2
author: xmrig
tag_name: v6.6.2
published_at: '2020-12-01T14:22:17+00:00'
---

# Version: v6.6.2

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.6.2
- [#1958](https://github.com/xmrig/xmrig/pull/1958) Added example mining scripts to help new miners.
- [#1959](https://github.com/xmrig/xmrig/pull/1959) Optimized JIT compiler.
- [#1960](https://github.com/xmrig/xmrig/pull/1960) Fixed RandomX init when switching to other algo and back.

## SHA256SUMS
```
038e8bfc5278839f5abf1850aa91582fb6e5b93d64dbc64f0838c66e8ffad22c *xmrig-6.6.2-bionic-x64.tar.gz
d14321fdd4531d1a38ecc6c7f1b153cfa5be5e3daa75fddce2fa88c23e98c29b *xmrig-6.6.2-focal-x64.tar.gz
16083a8b2bb1686c75712721cf497b7775c1b34b3b8ec98060d9ae425a5c70ca *xmrig-6.6.2-freebsd-static-x64.tar.gz
bad174e0e2184910948ee87b3e7c4ea5fed35c597626a41d5cd6a5e4b3bc4d2c *xmrig-6.6.2-linux-static-x64.tar.gz
736c478a542c201cd614f1027a92e09bb453adfd9ef3e849eaf6d6a10c54e266 *xmrig-6.6.2-linux-x64.tar.gz
66daf3f0fd401832b965d349789c6f422cc7291f6bdc8b4af830b8a563354048 *xmrig-6.6.2-macos-x64.tar.gz
1b740cec9ab5febe89070c7ac9a18f77b982f367a9994f2a910e1d4a4e577d28 *xmrig-6.6.2-gcc-win64.zip
c7952481e996cb3edde5a097fcac3db0f8b04522817ee3c7aa7ca784a5f62fb8 *xmrig-6.6.2-msvc-cuda10_2-win64.zip
9b8b2b1d49b148d138776d25aa1d9586ae0f7d97a29ce2728a3f029deca499c8 *xmrig-6.6.2-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl/GT9cACgkQRGpTY4vp
RAnwOwf8DUpfYqCX44L0dZe789snehHOWr7og/0ydW8gmdUAgzrUoIgJn0VzrIIM
0o8WGAjhNoarKswnfpng4D2VzcYF/p4T+xESzyJqQAb8qDj2+y8cn7fgx9k/WK1k
eapF4nkiZ1KwqBEzb9hpjaB7cR7RD/h1uUYbHpXxcernvV5DvH34a/oTRuTBn8Cm
UgQ9Ws1F/ReaorQeN3gWodxL0oypDcLYp8tT6xcBkXLeFM1Bz/u5GIfrgMN0zBcQ
rC+WelNgmeSupAS+4+3hJcJi+wlVzq6eCjFOk2Q4MiZWdCqZHphyklazrZq668Nx
TPPY7rdQYv9Wos/2InlmMeNITTsCLQ==
=CrrW
-----END PGP SIGNATURE-----
```