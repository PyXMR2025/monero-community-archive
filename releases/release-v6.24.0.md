---
title: v6.24.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.24.0
author: xmrig
tag_name: v6.24.0
published_at: '2025-06-23T01:32:22+00:00'
---

# Version: v6.24.0

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on X https://x.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.24.0
- [#3671](https://github.com/xmrig/xmrig/pull/3671) Fixed detection of L2 cache size for some complex NUMA topologies.
- [#3674](https://github.com/xmrig/xmrig/pull/3674) Fixed ARMv7 build.
- [#3677](https://github.com/xmrig/xmrig/pull/3677) Fixed auto-config for AMD CPUs with less than 2 MB L3 cache per thread.
- [#3678](https://github.com/xmrig/xmrig/pull/3678) Improved IPv6 support: the new default settings use IPv6 equally with IPv4.

## SHA256SUMS
```
23b4e8788c92c9b628feda74cb20b9e7afeea2ac6c2202f282c05bd02192b74d *xmrig-6.24.0-focal-x64.tar.gz
a8685ca003fa7d3a23e8748b72cede8e78a970efd8dc64dc8af46c86f445a6fd *xmrig-6.24.0-freebsd-static-x64.tar.gz
58d9658ac6e85bb6336b4e4ff3dee011cc6457cf99050cbcd67de10093149770 *xmrig-6.24.0-jammy-x64.tar.gz
129cfbfbe4c37a970abab20202639c1481ed0674ff9420d507f6ca4f2ed7796a *xmrig-6.24.0-linux-static-x64.tar.gz
fd41f8936c391a668fff282ba8a348d5722f98e1c70d30c5428559787b99348a *xmrig-6.24.0-macos-arm64.tar.gz
cd3026587f710aaa44d58dffeeb7f40cb5acc9d51bebc56f74a578c7fa3d088d *xmrig-6.24.0-macos-x64.tar.gz
2f223420661789e9ddc263ddbc288366ced5ce1d9184d60d7d2d2468d54df40a *xmrig-6.24.0-noble-x64.tar.gz
f211aabe350d7e77866720cbf1bd12d8cc6ce544c15572fbf2fa46a10df30f5d *xmrig-6.24.0-windows-arm64.zip
c7714b0ecbcc5ffb79b6bf0f5f8dd846b757004b69885e4ec2fee85ca958ae37 *xmrig-6.24.0-windows-gcc-x64.zip
d0d751a3bc265db85a7bc351a7792068a8c46a002b703624b64b77920f869350 *xmrig-6.24.0-windows-x64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmhYrV0ACgkQRGpTY4vp
RAlBKAf/al12PPCYn3S9nCedYZ7A7rKXYrg+ogUVaeE+t9yvev4O90caGvXJSnEr
vi5Vy5r+Q/f0B80Iu4FBGwa5RNvIZozqDOi47Xn+lNT5OIw8mDbbFPqcBJB3o0G6
cl/4KsrCHRuZAqLnqlEudlKd/Xlz1BtcinHfvINM39+oN1ddm+nyg611DaaPmdKU
AOn1YgQAZCzb4nqe69c45oavDxxXmWwDUY+Mbs7WOmQuvKFZIvwye/iSAM3oofqV
ShnHAEffgA1LTFfNq7c6SI5mcC/KCBRUeZkrP7j+Abz/00S7OB/0a2QDgG1uV7KJ
krTKcbY/Z3ew+PyI5QvcRWCuosp8Bg==
=jLpg
-----END PGP SIGNATURE-----
```