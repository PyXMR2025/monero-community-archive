---
title: v6.11.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.11.0
author: xmrig
tag_name: v6.11.0
published_at: '2021-04-06T15:05:25+00:00'
---

# Version: v6.11.0

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.11.0
- [#2196](https://github.com/xmrig/xmrig/pull/2196) Improved DNS subsystem and added new DNS specific options.
- [#2172](https://github.com/xmrig/xmrig/pull/2172) Fixed build on Alpine 3.13.
- [#2177](https://github.com/xmrig/xmrig/pull/2177) Fixed ARM specific compilation error with GCC 10.2.
- [#2214](https://github.com/xmrig/xmrig/pull/2214) [#2216](https://github.com/xmrig/xmrig/pull/2216) [#2235](https://github.com/xmrig/xmrig/pull/2235) Optimized `cn-heavy` algorithm.
- [#2217](https://github.com/xmrig/xmrig/pull/2217) Fixed mining job creation sequence.
- [#2225](https://github.com/xmrig/xmrig/pull/2225) Fixed build without OpenCL support on some systems.
- [#2229](https://github.com/xmrig/xmrig/pull/2229) Don't use RandomX JIT if `WITH_ASM=OFF`.
- [#2228](https://github.com/xmrig/xmrig/pull/2228) Removed useless code for cryptonight algorithms.
- [#2234](https://github.com/xmrig/xmrig/pull/2234) Fixed build error on gcc 4.8.

## SHA256SUMS
```
ab186518bd344c00a7d87b71eae316ec33ae3b9ba70f44b085132f8dab1451a8 *xmrig-6.11.0-bionic-x64.tar.gz
2def22507a7f25c50a63af365f7d664e947f7ed63aed850a7b5bf91c2de55c44 *xmrig-6.11.0-focal-x64.tar.gz
e30e7d92ce59f1dcb80dcfdab46aa8c6b43de90372ed3cde58028f3f5323b614 *xmrig-6.11.0-freebsd-static-x64.tar.gz
d1f745790e60efd7234999eaccc1a9d211193ccda1dae357b726e5c4eb94917e *xmrig-6.11.0-linux-static-x64.tar.gz
63a60de9a8c1696ab136f7e9071fc7420b46067319d7ac535e8a2676ef170a58 *xmrig-6.11.0-linux-x64.tar.gz
c7513adbc6440ee1cf13da661abacf722dd497b3243b3edcf7392a39fd313101 *xmrig-6.11.0-macos-arm64.tar.gz
ca1fc78e0dca14740d4c33f7672d7247386542d3e2aee8b7f6b5f2f9d344677b *xmrig-6.11.0-macos-x64.tar.gz
1d0866b2e270eed8a3eba78b87c8a9ed00e461999908354e1280289f6aa6346a *xmrig-6.11.0-gcc-win64.zip
5a2b297b92196cd906af89a3779854ab48bb2092c29017b0249ff35d67a5c844 *xmrig-6.11.0-msvc-cuda10_2-win64.zip
c4466710d1386f964becd2c3202131c8de4818d768b9105c9bf76efb00282e30 *xmrig-6.11.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmBsdgEACgkQRGpTY4vp
RAkaqwf/byThY2TmDznYYfEAGRc9eTkkfon6lsCZmWnMQTykWwRiSuLGRQZAjQT0
1SP7E3b5p4aNS/9lhIIdRl72yLxegCET77I5KgB0pFs7v8IdgwM7sMXPj4SMJh9A
msshqjlYrE7rgyMe1O7FeGcX5Jvm7e5ReTwu08kPB/6MyYv7MW3Nv1ofmsm38B48
bgdvYhseLAGAOD2ypYL3fC8OVfl72jKwwrdeTDZOlGRyGUtN9JwoUYz5zxE5cR67
DfeTvM8AwoxyxCdFp3Cd+5yoLl/kS3+dlcvijf/f0W3ZE9zmW8edM+w5IsUsUt9B
Kug9QpA8fF1YUrgKGhibdYcmHicZoQ==
=KtOI
-----END PGP SIGNATURE-----
```