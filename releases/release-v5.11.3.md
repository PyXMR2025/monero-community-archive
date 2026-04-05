---
title: v5.11.3
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.11.3
author: xmrig
tag_name: v5.11.3
published_at: '2020-06-08T19:05:39+00:00'
---

# Version: v5.11.3

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.11.3
- [#1718](https://github.com/xmrig/xmrig/pull/1718) Fixed, linker on Linux was marking entire executable as having an executable stack.
- [#1720](https://github.com/xmrig/xmrig/pull/1720) Fixed broken CryptoNight algorithms family with gcc 10.1.

## SHA256SUMS
```
829aa923d9ee7831e3fa08b09d71149fe3a85dc83d01ef456d8362e2d4d6ba0c *xmrig-5.11.3-msvc-cuda10_2-win64.7z
06cf5de0b7fd53ab5a0c056e5425535b9741defbfa7ada302765b2ae0eecc4cd *xmrig-5.11.3-xenial-x64.tar.gz
c904db76d159e2d15095842042b7f81fbd744a2bb6bae4ed1ae145b8e4fe2647 *xmrig-5.11.3-gcc-win64.zip
1e51d727655dce9694f4893a64156a77b6c527ef1926455db4e7a75ebed0e8b9 *xmrig-5.11.3-msvc-cuda10_2-win64.zip
968b06d007f218f8e3c882b3b6d76293fa2533f282bcffc9b727c36ca31e5db5 *xmrig-5.11.3-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl7eh+gACgkQRGpTY4vp
RAnCqAgAxR/+AkZxMFC1RB4NsY6787IQk40MrG3lqVXtvE4U19dodS3tMdq7bY7b
FrwWA8ggqMOpoDEfsXXtyObGI6NRSbdF8T1UmFhHERzvDDGTl91N7OxMJtZanWAd
TeLvoONMdqAUDMRVogPUyVS/LbAHM8ToEvnoI1SG8vfYlVB82Uo10NNLGupzjRiY
QZhRjpb9IP+UvpeUuqU2mRM9R2WFNgGuodQnVEZ3AN94KkLUgNLFYhBM8C+5++gi
KOS2ODXtgUUAz27kshp1AKUtph9J/WyQQFDZIoeCdcCmhisbxP0Fwb8qZRlD4Ctb
Ve5/9IoaaymnoM7WcNqUCKMgxjRsrw==
=saJz
-----END PGP SIGNATURE-----
```