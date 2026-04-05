---
title: v6.0.1-beta
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.0.1-beta
author: xmrig
tag_name: v6.0.1-beta
published_at: '2020-06-06T08:30:13+00:00'
---

# Version: v6.0.1-beta

# Release Notes
## Notes
- **[KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915) :new:**
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.0.1-beta
- [#1708](https://github.com/xmrig/xmrig/issues/1708) Added `title` option.
- [#1711](https://github.com/xmrig/xmrig/pull/1711) [cuda] Print errors from KawPow DAG initialization.
- [#1713](https://github.com/xmrig/xmrig/pull/1713) [cuda] Reduced memory usage for KawPow, minimum CUDA plugin version now is 6.1.0.

## SHA256SUMS
```
e96b33ec9b06790e4104cc26b667e592d4dc3283db35597a8deaad7a5acb9f12 *xmrig-6.0.1-beta-msvc-cuda10_1-win64.7z
b12f693b2b5ef2a6dca37f9c2562f02fa6e0bd9785c98227e8562330a4a8327c *xmrig-6.0.1-beta-xenial-x64.tar.gz
203a8593e5bbc0a67cb0a38e27ffe8c1ee0cb5bed295830b84bcf9a9c045391f *xmrig-6.0.1-beta-gcc-win64.zip
f93fa3a70719ee6fb9cde3df0f8087b6704a663bf10adbf44648d4622258f831 *xmrig-6.0.1-beta-msvc-cuda10_1-win64.zip
3efb1074c3b046863a481cf239f58f021d4671b2e3f299a691996aff144d4e50 *xmrig-6.0.1-beta-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl7bU1MACgkQRGpTY4vp
RAmOwQgAzbzGWgmCp4lADRxPIm9BFhzyoBvSqpfvA88hCUE6/3b2t0tTFw0hQJ7n
NqiLYXyJI6MBMTbbTYalBJwQ4sEtaom7MDTC/HUfTL32Xij/6+F0f5QjLQQtayhG
JeJC5Mtvn6ZEIOtMim4DJ7qNRW3R0uIbUw2cO9c3hyhSV1Zf2BedVx3Ua+5eqmKY
I3bBPqgdJtZ8wkvmLZc7t4/if1WpgIGHgls0GTJv0cSm0NWifxpXOcCFiRMY0yY6
yNGxNX0jjSKao38ALlwsgWzhiE3eQdRpwi9R6m0kKCzRrai1UfO3W2gr1aOiyph/
9Z6kYy1TNKuNPH6skIbB/w2S5xUoiQ==
=gY7c
-----END PGP SIGNATURE-----
```