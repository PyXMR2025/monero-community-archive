---
title: v6.3.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.3.0
author: xmrig
tag_name: v6.3.0
published_at: '2020-07-16T18:23:03+00:00'
---

# Version: v6.3.0

# Release Notes
## Notes
- **[KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915) :new:**
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.3.0
- [#1771](https://github.com/xmrig/xmrig/pull/1771) Adopted new SSE2NEON and reduced ARM-specific changes.
- [#1774](https://github.com/xmrig/xmrig/pull/1774) RandomX: Added new option `cache_qos` in `randomx` object for cache QoS support.
- [#1777](https://github.com/xmrig/xmrig/pull/1777) Added support for upcoming Haven offshore fork.
  - [#1780](https://github.com/xmrig/xmrig/pull/1780) CryptoNight OpenCL: fix for long input data.

## SHA256SUMS
```
e35fb059b354a2eb6b21b0e76ea440868e043819b6fbbf47c402078ffd67358d *xmrig-6.3.0-msvc-cuda10_2-win64.7z
e4d9da8c9ae9640b447a701c8e21c7aeefad5ccd39bf72a4fb15f1709010cf8f *xmrig-6.3.0-xenial-x64.tar.gz
612cb7d848006b57538e6edf4f79e40645a8bdd4ec2a7eca7fa77d546a1d1e86 *xmrig-6.3.0-gcc-win64.zip
27c959d69bef79dc6e29779bb83e506a953df39315729483b56b9309388a56af *xmrig-6.3.0-msvc-cuda10_2-win64.zip
c8112fc1bc6b1d84c08b7457e9fdcf75c414c9f21fe194079c9e149a48d80759 *xmrig-6.3.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl8QlkgACgkQRGpTY4vp
RAlwZggAwR3JeJRElWb8/oxhD7fhHdVyB0bWOuHm7eNne/AJ4Eto0thOfY30mtjZ
Ldd9OJDMJYf9VNGNjSeaMpc4sWeWADbCc0X/s2b+L1BlPNh38P/naQZds6Dbj0U+
imjA8I7Nfj9vDCZjozWPvleFmS+OqGgEB7ztHTifa3lmD0jmD7VML+nSm8LVYKF9
6pTpTnKFTPBbn8GvC+WSc8DSs2YZwy5UnD8Tl5ta1AcwZqrBOk2637GXMRJ3yhQr
OEjsZAgNHSVt8bkXm6ZhZuHLEA7X3ZKgSqfOKC5P3vT6hT/8gLGp/vnpQdqtHegy
4GKySihffx99eB0WPxTY0xSqslr/qw==
=8ueV
-----END PGP SIGNATURE-----
```