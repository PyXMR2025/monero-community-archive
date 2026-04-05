---
title: v5.2.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.2.1
author: xmrig
tag_name: v5.2.1
published_at: '2019-12-14T07:23:27+00:00'
---

# Version: v5.2.1

# Release Notes
## Notes
- **[Release notes](https://github.com/xmrig/xmrig/issues/1403)**
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.2.1
- [#1408](https://github.com/xmrig/xmrig/pull/1408) Added RandomX boost script for Linux (if you don't like run miner with root privileges).
- Added support for [AMD Ryzen MSR registers](https://www.reddit.com/r/MoneroMining/comments/e962fu/9526_hs_on_ryzen_7_3700x_xmrig_520_1gb_pages_msr/) (Linux only).
- Fixed command line option `--randomx-wrmsr` option without parameters.

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
b8ffbeb544fc00b93e47f280a972075f3b9215d9d76cda5a13ae3e0f38fb1b25 *xmrig-5.2.1-xenial-x64.tar.gz
8ac944a7e43af665415b0b4f4ed3e5569ccb48992965ae4c39f976666404e5a5 *xmrig-5.2.1-gcc-win64.zip
a396401c6a9d2ecbfd3bf7ee5c2aa85bd64b7520a0235ecc5cad94597306f1ed *xmrig-5.2.1-msvc-cuda10_1-win64.zip
a9aa1b4f8a9a75cddffa3aa6b84d7b8d314755a78d997c9f759d407edaf37b37 *xmrig-5.2.1-msvc-win64.zip
```

## SHA256SUMS.sig

GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl30iGoACgkQRGpTY4vp
RAkS3AgAz8cWVNe4+35+bTlFuLzJiE8uaRiNoqeskyk4hScPQPngfqd1qmER5Xi+
ntA9Lj7tkaAX/MmDTGc5UrkmYOAltR0JYQU5NqZX9ZcELIzxMWHwDr7xJL5p2roz
jhf/9NhZVV0s31BCXv+7iFTJ3/JS3fSEIW6tN/2fkVg3Mwsw/lzfsHEM1GaWWaEs
u/qcp4MSGDY1mU9ZjRFRxtdguFbXEy9f6ZVjplXfjnhoTvdkI+Pey3o0SP3rGyrg
jb2oE0w+vOFpgTMYZVB0gCOEqc+vSLJtZrU44n7vBmbptaYBnb8JII/u29qwaC/2
cS6VDK6yEZ5DJaBhw/w6fosmf4dN/g==
=MQLM
-----END PGP SIGNATURE-----
```