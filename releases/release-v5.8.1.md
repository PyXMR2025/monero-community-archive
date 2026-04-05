---
title: v5.8.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.8.1
author: xmrig
tag_name: v5.8.1
published_at: '2020-03-04T04:12:29+00:00'
---

# Version: v5.8.1

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.8.0
- [#1573](https://github.com/xmrig/xmrig/pull/1573) Added new AstroBWT algorithm for upcoming DERO fork, as `"algo": "astrobwt"` or `"coin": "dero"`.

## v5.8.1
- [#1575](https://github.com/xmrig/xmrig/pull/1575) Fixed new block detection for DERO solo mining.

## SHA256SUMS
```
3a154ffd01c9aeb1e85265b1c2bc357d9d813ad82f15e538407023cde72fbad7 *xmrig-5.8.1-xenial-x64.tar.gz
923c05a8cc0cc295a510ee0e116b88a50e1a3390a100ddcdc6a85d64c0956f49 *xmrig-5.8.1-gcc-win64.zip
58c91ef6d6c74c5f0037b8f0f2b925174f5ae8ead6ab08992297789c80fda059 *xmrig-5.8.1-msvc-cuda10_1-win64.zip
fe87bca4018565169bd8bf019d6694eb80ea2bdccce2f9ecbf61ed6b54c1c1e5 *xmrig-5.8.1-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl5fKK8ACgkQRGpTY4vp
RAmd1ggAm8TZFT+aw040h/xXN6UOHJQVcl5R8iVWLsDFOq7GMZxamVHSoWHRAgp4
XEjmIWD+P91U4aWwmGLi4H61XT15U4V3wBmPt8/jQ0PGFJwxZIBX39FmTpi0Ar5a
9fYsxmIU60+lP4xIAIOYslKPnGWovR97WKzLQ+8HVlYjHLgBPPNYqt4i+gnpKoHh
CgzFZgX9kF8eAd8vqV0tnX3Q+bsqU6z5xUuHAbG/m+CDDFJPYLMC9Z++Zs3j2t5Z
gYk1EJr6HW+2YHaWdIRwunFxz5O3NK0HsR+tZNzftDrAlCWuPX2Rz63dhMSQ0NaG
fnmastEcKMBmucR/6HL174kvNh3eSw==
=yv5G
-----END PGP SIGNATURE-----
```