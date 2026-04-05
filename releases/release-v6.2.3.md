---
title: v6.2.3
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.2.3
author: xmrig
tag_name: v6.2.3
published_at: '2020-07-09T16:24:06+00:00'
---

# Version: v6.2.3

# Release Notes
## Notes
- **[KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915) :new:**
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.2.3
- [#1745](https://github.com/xmrig/xmrig/pull/1745) AstroBWT: fixed OpenCL compilation on some systems.
- [#1749](https://github.com/xmrig/xmrig/pull/1749) KawPow: optimized CPU share verification.
- [#1752](https://github.com/xmrig/xmrig/pull/1752) RandomX: added error message when MSR mod fails.
- [#1754](https://github.com/xmrig/xmrig/issues/1754) Fixed GPU health readings for pre Vega GPUs on Linux.
- [#1756](https://github.com/xmrig/xmrig/issues/1756) Added results and connection reports.
- [#1759](https://github.com/xmrig/xmrig/pull/1759) KawPow: fixed DAG initialization on slower AMD GPUs.
- [#1763](https://github.com/xmrig/xmrig/pull/1763) KawPow: fixed rare duplicate share errors.
- [#1766](https://github.com/xmrig/xmrig/pull/1766) RandomX: small speedup on Ryzen CPUs.

## SHA256SUMS
```
1deb7d9f58348531e479cf1f9e3d0e18eacd0920f86b9d52ccab330f2907065f *xmrig-6.2.3-msvc-cuda10_2-win64.7z
a79d4f5633dbbe98842d5073b41cc25468679c46e011373587ffdbc544d1ea12 *xmrig-6.2.3-xenial-x64.tar.gz
33f13fe8a365842e10ce6a8f7f77defe4f8c75a05834d4d45e495b6f970811c5 *xmrig-6.2.3-gcc-win64.zip
7226caddebc9a10cca899de402bde3d3fc855e6c9268b0dd0c751af95f1f628b *xmrig-6.2.3-msvc-cuda10_2-win64.zip
5b795f39eae47242a8685970eaf0aa8e3267636fd0e3c2986f5c25000a6690d5 *xmrig-6.2.3-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl8HQdEACgkQRGpTY4vp
RAl9Rwf+IhU3EQb29Ru+XJoq+j9ojcQtTxYDmF4w/t/wrz9+VIyRX5N0Zd55wSuB
vFQD2fkfWnyuKCO4dZELcRBytH5Zc1ObsG2eVrQQlIyPllBHYMNKN9kuA1aoUvEq
NEfv18IF/FZU4jFKPc5/yRonXAL5owM0iBDH3l4b/M48/5IJSStdb80kyzBnuVqR
X9unGyCwBiNWRtvS4QwTDxsmMGqgQEFANFgUCuusesIHDBdWAll+g6vgxbpN58GL
abe0I7Mi2SCmtbpxRxCsSV5elk6IvtGSGJgC7Dwb3wpmQ4dEu8dBmUmxy3qBa4HU
4Ygza2R1x5UkbIp736D0QyxMv9SJIg==
=0brR
-----END PGP SIGNATURE-----
```