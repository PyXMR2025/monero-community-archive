---
title: v6.7.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.7.0
author: xmrig
tag_name: v6.7.0
published_at: '2020-12-21T11:38:30+00:00'
---

# Version: v6.7.0

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.7.0
- **[#1991](https://github.com/xmrig/xmrig/issues/1991) Added Apple M1 processor support.**
- **[#1986](https://github.com/xmrig/xmrig/pull/1986) Up to 20-30% faster RandomX dataset initialization with AVX2 on some CPUs.**
- [#1964](https://github.com/xmrig/xmrig/pull/1964) Cleanup and refactoring.
- [#1966](https://github.com/xmrig/xmrig/pull/1966) Removed libcpuid support.
- [#1968](https://github.com/xmrig/xmrig/pull/1968) Added virtual machine detection.
- [#1969](https://github.com/xmrig/xmrig/pull/1969) [#1970](https://github.com/xmrig/xmrig/pull/1970) Fixed errors found by static analysis.
- [#1977](https://github.com/xmrig/xmrig/pull/1977) Fixed: secure JIT and huge pages are incompatible on Windows.
- [#1979](https://github.com/xmrig/xmrig/pull/1979) Term `x64` replaced to `64-bit`.
- [#1980](https://github.com/xmrig/xmrig/pull/1980) Fixed build on gcc 11.
- [#1989](https://github.com/xmrig/xmrig/pull/1989) Fixed broken Dero solo mining.

## SHA256SUMS
```
4538cbb07439a91d7d620a6bbdd49353952466df1e84cc52097052e93a97f9fd *xmrig-6.7.0-bionic-x64.tar.gz
2eafb6e3585669204667c3a7c824147f4d877f10d0c3bc63f3e0b7baf2152598 *xmrig-6.7.0-focal-x64.tar.gz
16871201fd67e99deecd07e6085895a2f2a98660d5fcb8001abe077a1f71ecba *xmrig-6.7.0-freebsd-static-x64.tar.gz
1dde3835123c451d1e3d666776bad4f5ec9fbf20c2b7a00094896edd39bb9d97 *xmrig-6.7.0-linux-static-x64.tar.gz
999cee31dfbea969747ed7fd2e8c0734eff9aeab84abbfd492ea7453ba0b506c *xmrig-6.7.0-linux-x64.tar.gz
98a08b2437a292310dbe7f254cba6e2b5f07b7cf0997f5d1f085475f073533fe *xmrig-6.7.0-macos-arm64.tar.gz
c6dd09c2d36a02af923c4064d593e7298d837d9e3f6b9f9edc21a5f4c6db60dd *xmrig-6.7.0-macos-x64.tar.gz
bd0e29ee5e71bc33367116fa7a709492afc2c1f0e1d77d186aa0f1a827f8ec00 *xmrig-6.7.0-gcc-win64.zip
8733802d51a57391d82095e2c9dc7cd35e2c87e22dff35ce7ab43b9bd7c57af8 *xmrig-6.7.0-msvc-cuda10_2-win64.zip
9312fcda72763da8af25c05d29cea6abe4941e3d1d31ddd17bd1acd7e2522e9e *xmrig-6.7.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl/gh1cACgkQRGpTY4vp
RAk26Qf/T10SAYCfpYRcovb5t7La1/6osWqEu3CzQ4HobbNn+zox1I/52BEUkgx5
eirLklhDLCf4eLDrHm+sTdiNg533BOCnkpf93bCJ+HbId8wwfbU2rBezpniAcPmW
Wvvcnq1CoU6Dxz4MQyUcByNYASqumhBvqxTVYnmCFLSwv3+8Bv1W8TpntwMA4nsl
A8rBqNlqDlK9QGs75SLcxJZJHPwz/QdqYEQGKn7LvFSmpIeqMnCW8PPykZ3LmU3+
ZBmOiazfFD8HndJrT1+HlkXrrVkSapMIihc0RqfJv4oJk36YqgQI7gEBfEHe1WyH
OeRvRuNUSLz5avVEW/ImO2xOlq0qjg==
=3hzK
-----END PGP SIGNATURE-----
```