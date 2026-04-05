---
title: v6.20.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.20.0
author: xmrig
tag_name: v6.20.0
published_at: '2023-07-03T06:17:51+00:00'
---

# Version: v6.20.0

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- VAES optimizations not supported by `xmrig-6.20.0-linux-x64.tar.gz` due old compiler, please use `xmrig-6.20.0-linux-static-x64.tar.gz` instead. :warning:
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.20.0
- Added new ARM CPU names.
- [#2394](https://github.com/xmrig/xmrig/pull/2394) Added new CMake options `ARM_V8` and `ARM_V7`.
- [#2830](https://github.com/xmrig/xmrig/pull/2830) Added API rebind polling.
- [#2927](https://github.com/xmrig/xmrig/pull/2927) Fixed compatibility with hwloc 1.11.x.
- [#3060](https://github.com/xmrig/xmrig/pull/3060) Added x86 to `README.md`.
- [#3236](https://github.com/xmrig/xmrig/pull/3236) Fixed: receive CUDA loader error on Linux too.
- [#3290](https://github.com/xmrig/xmrig/pull/3290) Added [Zephyr](https://www.zephyrprotocol.com/) coin support for solo mining.

## SHA256SUMS
```
3b5cbf0dddc3ef7e3af7d783baef315bf47be6ce11ff83455a2165befe6711f5 *xmrig-6.20.0-bionic-x64.tar.gz
4fe9647d6a8bf4790df0277283f9874385e0cd05f3008406ca5624aba8d78924 *xmrig-6.20.0-focal-x64.tar.gz
e1ff2208b3786cac801ffb470b9475fbb3ced74eb503bfde7aa7f22af113989d *xmrig-6.20.0-freebsd-static-x64.tar.gz
ff6e67d725ee64b4607dc6490a706dc9234c708cff814477de52d3beb781c6a1 *xmrig-6.20.0-linux-static-x64.tar.gz
99e3e313b62bb8b55e2637fc14a78adb6f33632a3c722486416252e2630cfdf6 *xmrig-6.20.0-linux-x64.tar.gz
5575c76987333427f74263e090910eae45817f0ede6b452d645fd5f9951210c9 *xmrig-6.20.0-macos-arm64.tar.gz
5a6e7d5c10789763b0b06442dbc7f723f8ea9aec1402abedf439c6801a8d86f2 *xmrig-6.20.0-macos-x64.tar.gz
08384f3f05ad85b2aa935dbd2e46a053cb0001b28bbe593dde2a8c4b822c2a7d *xmrig-6.20.0-gcc-win64.zip
dd7fef5e3594eb18dd676e550e128d4b64cc5a469ff6954a677dc414265db468 *xmrig-6.20.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmSiZsQACgkQRGpTY4vp
RAnMaAgAwIYp7W2rqEDqxDFUySBcOsqDW4uyI6S/3IGxptpvQvffQPN9dSUyIB23
U6eMtm/aGDi7HrB0SCnC88WEB/sAa7s1F07Z8w0bBRA7pVOoM1/Y4LZVwqGIB/WQ
fg+fkaGt8nwe6SJ88dTjsvrydjp9yNPTXh2F+Q4m9n/ZFHN4dXz12wptTIzsIj+s
xHcm9p7Q8aqJD7mqy06OTXyGc11qPnamp3kWCMEXgqT9Yv4LHWZPtXC9oFHdg9v/
Dzu2oy4A3svDHg6hS44MlwpsqZ3Ng1n0Nrps7rzucdBR0LTJVIuORyuYbsrnAxOO
NRl8FBDXUy2m+/9IozzOXTGNhnIKUw==
=/tvI
-----END PGP SIGNATURE-----
```