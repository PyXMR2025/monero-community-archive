---
title: v6.16.3
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.16.3
author: xmrig
tag_name: v6.16.3
published_at: '2022-01-25T16:15:14+00:00'
---

# Version: v6.16.3

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- VAES optimizations not supported by `xmrig-6.16.3-linux-x64.tar.gz` due old compiler, please use `xmrig-6.16.3-linux-static-x64.tar.gz` instead. :warning:
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.16.3
- [#2778](https://github.com/xmrig/xmrig/pull/2778) Fixed `READY threads X/X` display after algorithm switching.
- [#2782](https://github.com/xmrig/xmrig/pull/2782) Updated GhostRider documentation.
- [#2815](https://github.com/xmrig/xmrig/pull/2815) Fixed `cn-heavy` in 32-bit builds.
- [#2827](https://github.com/xmrig/xmrig/pull/2827) GhostRider: set correct priority for helper threads.
- [#2837](https://github.com/xmrig/xmrig/pull/2837) RandomX: don't restart mining threads when the seed changes.
- [#2848](https://github.com/xmrig/xmrig/pull/2848) GhostRider: added support for `client.reconnect` method.
- [#2856](https://github.com/xmrig/xmrig/pull/2856) Fix for short responses from some Raptoreum pools.
- [#2873](https://github.com/xmrig/xmrig/pull/2873) Fixed GhostRider benchmark on single-core systems.
- [#2882](https://github.com/xmrig/xmrig/pull/2882) Fixed ARMv7 compilation.
- [#2893](https://github.com/xmrig/xmrig/pull/2893) KawPow OpenCL: use separate UV loop for building programs.

## SHA256SUMS
```
f06fbff701a1ca361c4b26fb2cf1795b2c31a92942c41d2d7451780bb664efbe *xmrig-6.16.3-bionic-x64.tar.gz
9cd105c0e11dff1268b587c01ae09f36fef26d5881fe6b9b0e6c8ccadbe9c9c6 *xmrig-6.16.3-focal-x64.tar.gz
a663d7fb9fd18124d95e46599ef45d56225e53733b0fbb83b9945c393eb3315a *xmrig-6.16.3-freebsd-static-x64.tar.gz
d716583849feded501fb3c30825d6b129b0c6a87db6688338b362a28996bdaf5 *xmrig-6.16.3-linux-static-x64.tar.gz
8a4120b4830b929f294501da44978e48ec90270ada6fa64a6d043523a1efd553 *xmrig-6.16.3-linux-x64.tar.gz
9894d00215aa6ef7eb9c066fcfb58b581ffdf13b70f9f2890d83147bfe8e0f98 *xmrig-6.16.3-macos-arm64.tar.gz
abc41118e228a17c2c898f2c6a25730bbf7afb6ae39f4e19c18983cfcc4beab3 *xmrig-6.16.3-macos-x64.tar.gz
70eca903689b502f01f7adf11e0e16d1e3e471a694a35a9cd7a3e48d89762871 *xmrig-6.16.3-gcc-win64.zip
63a2591d3a4b6dcb9c8e1b7fa2bc320a7a6843e6f69087a4111ae226b83b51b8 *xmrig-6.16.3-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmHwIO8ACgkQRGpTY4vp
RAm1Fwf/YP6h1qV7MNwIZ79XP11LQ8mHdwe/C/uZ/grOdyMpKSvbdJHVkesGlx4q
nBR0bn0wXiOcZnv+2fHnAkki7qQ3WUYQSnHhGNGdshbCcoABqMjVkTAYDwoHodeV
Mpb5xYdSfkvK1DoIx9JPBmDwIw9Mv0qbac60xokUzy1B2y7H1x1Ba41xFXZl0FaQ
OuQpxzBsyuv48f6a4eQlyllKNLtjgo/m6e4EUn693cOhC0uG5j8cEd9BlMn4GhMW
CNSuytFBrKRdsyk1TKAHbQU6pciSPsEX1VpuWYjCtDfF1EKC+bMf5ZNhz7JeGIKb
1KTZLJ5/nC4b9WO6M1Gug/t3kRxrDA==
=FAJt
-----END PGP SIGNATURE-----
```