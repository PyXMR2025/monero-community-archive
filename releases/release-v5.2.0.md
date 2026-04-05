---
title: v5.2.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.2.0
author: xmrig
tag_name: v5.2.0
published_at: '2019-12-11T08:20:42+00:00'
---

# Version: v5.2.0

# Release Notes
## Notes
- **[Release notes](https://github.com/xmrig/xmrig/issues/1403)**
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.2.0
- **[#1388](https://github.com/xmrig/xmrig/pull/1388) Added [1GB huge pages support](https://xmrig.com/docs/miner/hugepages#onegb-huge-pages) for Linux.**
  - Added new option `1gb-pages` in `randomx` object with command line equivalent `--randomx-1gb-pages`.
  - Added automatic huge pages configuration on Linux if use the miner with root privileges.
- **Added [automatic Intel prefetchers configuration](https://xmrig.com/docs/miner/randomx-optimization-guide#intel-specific-optimizations) on Linux.**
   - Added new option `wrmsr` in `randomx` object with command line equivalent `--randomx-wrmsr=6`.
- [#1396](https://github.com/xmrig/xmrig/pull/1396) [#1401](https://github.com/xmrig/xmrig/pull/1401) New performance optimizations for Ryzen CPUs. 
- [#1385](https://github.com/xmrig/xmrig/issues/1385) Added `max-threads-hint` option support for RandomX dataset initialization threads.  
- [#1386](https://github.com/xmrig/xmrig/issues/1386) Added `priority` option support for RandomX dataset initialization threads. 
- For official builds all dependencies (libuv, hwloc, openssl) updated to recent versions.
- Windows `msvc` builds now use Visual Studio 2019 instead of 2017.

## SHA256SUMS
```
0b28f40459622899abc3a911b6ffa6ac1382ead65c8d54d0dc4b3705057b4fc4 *xmrig-5.2.0-xenial-x64.tar.gz
6a73e524f669625f52a5643cfb346c7a0b84a89a0e0b05fc4ad7a37c7ac4d301 *xmrig-5.2.0-gcc-win64.zip
a56f14a2dcb13e0d908d30c2d36ea56ca8d5291a74236f9ee14b6ee984e054c9 *xmrig-5.2.0-msvc-cuda10_1-win64.zip
90e0051ce71b07942aa00aa50b69d883885814430e0a37e1e386db57511685d9 *xmrig-5.2.0-msvc-win64.zip
```

## SHA256SUMS.sig

GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl3wn+YACgkQRGpTY4vp
RAmlYwgAo1dkkCz7+N5QD0IUb/xTQd2aJV7EDXZ6p+/WyFKchCzXtrfAgJHgpzQs
lJp0mOv12KMYErcNHoSa+dHZ2X18+syYhNG6HVMJ569VRuB1zt7xZ9iaLKQJu5fP
PL8kghfxcLdP2Ly8x/KGYzLBJSI7o7g9zaeypn0rEEJuHY29hPl6chiYqusBvmcp
YN7gp/PMgS26LfquX+Mwgdi5vqprDFdl/cWy6riObPUkJmjfcYss6b8MAhSE7enI
T2NVMM1na24pfVTk3ftzb+PJwWojR70oaphZwg+Zl/RCfN75nZtaddUiXFF+N1YD
5ECmtykFNeupWH+Z9j0GltAGbEd93w==
=ESr4
-----END PGP SIGNATURE-----
```