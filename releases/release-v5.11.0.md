---
title: v5.11.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.11.0
author: xmrig
tag_name: v5.11.0
published_at: '2020-04-13T14:07:39+00:00'
---

# Version: v5.11.0

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.11.0
- **[#1632](https://github.com/xmrig/xmrig/pull/1632) Added AstroBWT CUDA support ([CUDA plugin](https://github.com/xmrig/xmrig-cuda) v3.0.0 or newer required).**
- [#1605](https://github.com/xmrig/xmrig/pull/1605) Fixed AstroBWT OpenCL for NVIDIA GPUs.
- [#1635](https://github.com/xmrig/xmrig/pull/1635) Added pooled memory allocation of RandomX VMs (+0.5% speedup on Zen2).
- [#1641](https://github.com/xmrig/xmrig/pull/1641) RandomX JIT refactoring, smaller memory footprint and a bit faster overall.
- [#1643](https://github.com/xmrig/xmrig/issues/1643) Fixed build on CentOS 7.

## SHA256SUMS
```
c3d93065dca3139d99dfb05abad9c2e62b3637e2d60f35bca3fd845819427819 *xmrig-5.11.0-xenial-x64.tar.gz
a4c276a7db9135c9396cbcb5cd21ff91bf5b35508036590877906aaf24971b21 *xmrig-5.11.0-gcc-win64.zip
c4ffc7fbf20dfd0dbf9448883dd6ea3b7cb6ac1bff3ea1219dac9228b401af7d *xmrig-5.11.0-msvc-cuda10_1-win64.zip
cf2bb516ebf015290607da631c091c8f329293d88db27f8e766a4c0f19d7ec86 *xmrig-5.11.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl6UcK0ACgkQRGpTY4vp
RAkd5QgAq5tqscdTPHet1arOa0yomqU4jfZT+mi69tTTIXbQlN3UHcNQbVHsJk7q
jO0Fdhzyff1OaXh/iwfPb5x/RSLT8lBFN1rvVNg1Y590AFNmRskVLyCXdJlE1rI4
qqN14Ef/FdYIDJf92eAokC6cQz2pJU4uQ3uTOr7gIYAbBeQ8iUAwHr7lKlwUIcDu
arLZwvBgcod2NQVGMEbIDzId7bAq6/HZxcDoMj/zcccaHDuAQVzllwDME/Q/QcCH
qligSxrK15qqxIftEDOLr0gUTLRvcV3xp2T1nWsnE4+OLj3FxHyQbLMkxXmdhOz9
h4a5gcNao+Rco5OcS8eLnQkVj4uZrg==
=ZCrc
-----END PGP SIGNATURE-----
```