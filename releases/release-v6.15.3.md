---
title: v6.15.3
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.15.3
author: xmrig
tag_name: v6.15.3
published_at: '2021-11-01T13:51:27+00:00'
---

# Version: v6.15.3

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.15.3
- [#2614](https://github.com/xmrig/xmrig/pull/2614) OpenCL fixes for non-AMD platforms.
- [#2623](https://github.com/xmrig/xmrig/pull/2623) Fixed compiling without kawpow.
- [#2636](https://github.com/xmrig/xmrig/pull/2636) [#2639](https://github.com/xmrig/xmrig/pull/2639) AstroBWT speedup (up to +35%).
- [#2646](https://github.com/xmrig/xmrig/pull/2646) Fixed MSVC compilation error.

## SHA256SUMS
```
9ecad486d379fbe066acae4c96792d8c4cdf9315f0ef1484255116886f6a462d *xmrig-6.15.3-bionic-x64.tar.gz
c7b5b2c7ce0cb86e411ffcb3d54297bb327619c1f5ad7b9b35f3092c55a16e19 *xmrig-6.15.3-focal-x64.tar.gz
01919123e153f3068f0c00c012254be2ce0d4ea685e36d891b56d8ec0deab324 *xmrig-6.15.3-freebsd-static-x64.tar.gz
250c5249686f518ba3eb3691091958e2c26b1ad1910aabac7e891e3e99e5d525 *xmrig-6.15.3-linux-static-x64.tar.gz
5d1b2cf2db880c3e4c0e6f0c4a5cb336c3a50371b33297a4a4ce9674e04aa457 *xmrig-6.15.3-linux-x64.tar.gz
44d0bd8636cabd3c17d0f165431fef427f08d1ca30acc511437813d96bee0d8d *xmrig-6.15.3-macos-arm64.tar.gz
3f5231ee2d9fcb0f11547a7f5ec7d1d87f92cd2d6079bc34bae9efcaef35bf83 *xmrig-6.15.3-macos-x64.tar.gz
a85572959dd4536b487b372417338eb8e1b31cb034378cee9fb281f2b30d2cb8 *xmrig-6.15.3-gcc-win64.zip
abd3b672841a7dfe64c695f795d0a0813eb4811bdc08203dc50bfd752f8a61a3 *xmrig-6.15.3-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmF/778ACgkQRGpTY4vp
RAkJ6ggA0wpvsg7p085PbMAQCTuzfJ4FOf2EALCCbXghrlHh6byKX5/X4Dd2Yqli
Z2AUidCB4IWiCm68L0wv7J/xoBc+mYkBh2h2+feSm6BrC5N6EdZb9lwKO6+MrzUR
VDVllLKyp8GfUPXWE4G8A9BYXoADVltMl5FvQaC/btNE1+1hMIbt0DDoe0a+OPW0
165DHL1E2CZtuH+mEdzhUw/IiSJEUd+Ro9LH7OdKf9KncpsGEMVL7b6p6tsKEv7v
hZ0WrlyAnN/MYSYE80fFQ+uMdfmCC7SLi6OKDC21K8aJgib4fmIp4Lza7rGqiHM3
TCYpUHhGEREpdEt9ZEKTgVTsF/TYmw==
=KaQe
-----END PGP SIGNATURE-----
```