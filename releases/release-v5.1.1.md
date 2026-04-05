---
title: v5.1.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.1.1
author: xmrig
tag_name: v5.1.1
published_at: '2019-12-04T10:31:41+00:00'
---

# Version: v5.1.1

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.1.1
- [#1365](https://github.com/xmrig/xmrig/issues/1365) Fixed various system response/stability issues.
  - Added new CPU option `yield` and command line equivalent `--cpu-no-yield`.
- [#1363](https://github.com/xmrig/xmrig/issues/1363) Fixed wrong priority of main miner thread.

## SHA256SUMS
```
533ab4efe855435fc7224a12b24114bb7aecd580a1f995d605bcc39de6fc3d72 *xmrig-5.1.1-xenial-x64.tar.gz
d80f25ba50b300552a9eac8dc31ff0df09de7f86936c4a77c548a508a87a1a03 *xmrig-5.1.1-gcc-win32.zip
7820b9ffa6f01e019898b9c97a28b321d0483e7727c2dfc2238e19ad0e713e48 *xmrig-5.1.1-gcc-win64.zip
13dbe288cf2a8ef4321dd62ba3369b6027d77bc33b6a5e4100cff892394b9244 *xmrig-5.1.1-msvc-cuda10_1-win64.zip
208b56b3e56aa835912ba672e2fa78e749d4979ae306119c09f79246c2bc7ed6 *xmrig-5.1.1-msvc-win64.zip
```

## SHA256SUMS.sig

GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl3niTgACgkQRGpTY4vp
RAkXAQf9FB4K4k49bhdumVMOkcB5fIvWV6vDhsFN8wkHLYxet/uFWM8Ac4LZCZWx
MyzWb+4Y5t9HQi0dybUN9EjVHyKRwiJpWY5G2dGUBk3m+yOTWHIlG8t+OKLNTko+
CD9i1uOiMSehgE0Oh9H0YK2jRIbj5q3yUVjbogbpZ5T2YEbSM+2cDxZwSp18rnij
s7QMZhTXOmBc64IegZaAS/ub/ESTSKyZqqB9mUVcRQK1AsGPSV3Gf9xQlEEJjGSr
unSZBSfpjEO1+cKPLq8gtAVCHQwuQsVdUzk+/gvJ2CDR7JhOnY2R/iaLA2OsCCgi
/8Js1b/lLtblFyvFMUAvLqWpSiG7Nw==
=jUJO
-----END PGP SIGNATURE-----
```