---
title: v6.2.2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.2.2
author: xmrig
tag_name: v6.2.2
published_at: '2020-06-23T09:35:11+00:00'
---

# Version: v6.2.2

# Release Notes
## Notes
- **[KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915) :new:**
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.2.1
- [#1726](https://github.com/xmrig/xmrig/issues/1726) Fixed detection of AVX2/AVX512.
- [#1728](https://github.com/xmrig/xmrig/issues/1728) Fixed, 32 bit Windows builds was crash on start.
- [#1729](https://github.com/xmrig/xmrig/pull/1729) Fixed KawPow crash on old CPUs.
- [#1730](https://github.com/xmrig/xmrig/pull/1730) Improved displaying information for compute errors on GPUs.
- [#1732](https://github.com/xmrig/xmrig/pull/1732) Fixed NiceHash disconnects for KawPow.
- Fixed AMD GPU health (temperatures/power/clocks/fans) readings on Linux.

## v6.2.2
- [#1742](https://github.com/xmrig/xmrig/issues/1742) Fixed crash when use HTTP API.

## SHA256SUMS
```
832949916736e98081608c3dc67a9e91e22ca6f31964daa3c317e5c71e971b68 *xmrig-6.2.2-msvc-cuda10_2-win64.7z
fc1c1809bc8dd175e2d694e1e8729bf700be8b2fbd2b499a7def3af3ade84640 *xmrig-6.2.2-xenial-x64.tar.gz
9cd1e53385ab8fdc67413fccd0c5a17187192e34530f42352041c9c348e17893 *xmrig-6.2.2-gcc-win64.zip
94b9271d8a945e4a46c1322badc4ec5097090b534119ffc7e111333ce13c398f *xmrig-6.2.2-msvc-cuda10_2-win64.zip
e1ac6263a7740f95cd573670db511d5b52d7e67e85fc1b74f4c9201c5924a398 *xmrig-6.2.2-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl7xy5gACgkQRGpTY4vp
RAmTSwgA2YUiVlT0bOZUtjDALk7Luw67AJ+PPRFuafuMGEQvnlsTE32pdrUI25ZF
NumyzWJJR1bxQDRinXPYjsxC2bV4WNYbTBZKpjKFP6jVI9ReU8jcYyMg+0zQcNMA
dfDLLDHmdCS+OhiaRGjs00Ii9UAS6IIaFiOml4FMrn3t4+QEW1qxQEq10tbcMxnK
cIrJE0w0nfGU2CzJdUaSRGZkq0hWd88qKiZ35+plXTaOf7GIG48TaEZQ3CHbUnx8
ysUuTJc+4OX5aIqTBUAvcJFV2DgRs9Bl4p2P+ySzwIpdvNy1pTM7jTA+VF15l949
SRsvlJ7hUjRegm5ksaloVKSdu9kbPw==
=ed9B
-----END PGP SIGNATURE-----
```