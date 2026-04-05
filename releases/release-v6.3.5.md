---
title: v6.3.5
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.3.5
author: xmrig
tag_name: v6.3.5
published_at: '2020-10-03T05:21:38+00:00'
---

# Version: v6.3.5

# Release Notes
## Notes
- **[KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915) :new:**
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.3.5
- [#1845](https://github.com/xmrig/xmrig/pull/1845) [#1861](https://github.com/xmrig/xmrig/pull/1861) Fixed ARM build and added CMake option `WITH_SSE4_1`.
- [#1846](https://github.com/xmrig/xmrig/pull/1846) KawPow: fixed OpenCL memory leak.
- [#1849](https://github.com/xmrig/xmrig/pull/1849) [#1859](https://github.com/xmrig/xmrig/pull/1859) RandomX: optimized soft AES code.
- [#1850](https://github.com/xmrig/xmrig/pull/1850) [#1852](https://github.com/xmrig/xmrig/pull/1852) General code improvements.
- [#1853](https://github.com/xmrig/xmrig/issues/1853) [#1856](https://github.com/xmrig/xmrig/pull/1856) [#1857](https://github.com/xmrig/xmrig/pull/1857) Fixed crash on old CPUs.

## SHA256SUMS
```
a896166ca3ebfbcb6c8a7610cca74af2d9bcba443ad1969a3197b91f66a237b3 *xmrig-6.3.5-bionic-x64.tar.gz
98e1825d7f2ff5d51a6bc25df0c69992d4b9a1705b6b5f30bfad47cbb525761a *xmrig-6.3.5-focal-x64.tar.gz
66f40413d75e7e6321cc8de2db4e1f8533e49fa3bfd375a194d9c2f92bd39287 *xmrig-6.3.5-freebsd-static-x64.tar.gz
24d4f07cf5850f00ab513b228f95769a5a5ed68d35808d98f9959b58d97985a0 *xmrig-6.3.5-linux-static-x64.tar.gz
411c267f3446a961a682f8ff6c6d49ae7e4a6d7d894eff1cf01a321e0cd53c6d *xmrig-6.3.5-linux-x64.tar.gz
bf0a07d127c0b6f1c4a311fc28824bf6bb2eea2aa532c59efe8f41ec95af89c6 *xmrig-6.3.5-macos-x64.tar.gz
e45915ada7e6e30f6ab40abf33831056449d5914307d7706bb0ad439b6d64c12 *xmrig-6.3.5-gcc-win64.zip
9838d31f8ce5816dc928b24bcc6f9cff773cca7d0cba6fbd9936d4b3d4bae5b1 *xmrig-6.3.5-msvc-cuda10_2-win64.zip
e9760e18ef5f6a0c7f5437baf814f80eef90328cc47eff3e358372fbc731d98c *xmrig-6.3.5-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl94CCcACgkQRGpTY4vp
RAldPQf+PIapE0Wn/4TNIVLCC2paXByovuBp2XI448GY+Lb1wBq6DpttB1NnZ3Gr
ytot+RiqWdGktqzjNtSuELBk5GeTPfPR4BDsLdfYd3hYtigRZvY8EMqC29yWpNs7
5wJY5M7CCgemg+Wl+H9Uv92gXfXr45xChuSTZ+JMOFRiclQsgH0lqJqXPxb5h8Qt
T5SgrSKpUy8dFGPg/Zd/2y6vWp7KnNrGISDqJN8N7wVDm9WXDOpk9bG1swDRdZAI
hIJcnnp3x4uNAZoaTKh+lssY0ysPL3EwbSZffxCUR39NYqHObMkinaM7jlLqfGZp
Gagpf5/LryhpRLtRqM/M+N184ZTP1g==
=pWV0
-----END PGP SIGNATURE-----
```