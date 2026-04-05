---
title: v6.16.4
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.16.4
author: xmrig
tag_name: v6.16.4
published_at: '2022-02-04T10:36:56+00:00'
---

# Version: v6.16.4

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- VAES optimizations not supported by `xmrig-6.16.4-linux-x64.tar.gz` due old compiler, please use `xmrig-6.16.4-linux-static-x64.tar.gz` instead. :warning:
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.16.4
- [#2904](https://github.com/xmrig/xmrig/pull/2904) Fixed unaligned memory accesses.
- [#2908](https://github.com/xmrig/xmrig/pull/2908) Added MSVC/2022 to `version.h`.
- [#2910](https://github.com/xmrig/xmrig/issues/2910) Fixed donation for GhostRider/RTM.

## SHA256SUMS
```
5a96a942f7e85bd7bd16cb547257d546bec0c62dea98075e7a06d93d5c5f5a34 *xmrig-6.16.4-bionic-x64.tar.gz
f36dcc33ea955d53cc4f4665e5ddb0311b9cf592e3a2db4668a01fb5cca2f933 *xmrig-6.16.4-focal-x64.tar.gz
9d5c1d3c0a9fe2adbede5abacbd538cbdf824440555bd972131cc8c7f03866d5 *xmrig-6.16.4-freebsd-static-x64.tar.gz
bf1e10f389d119fe4f72950a6a59bc6a74ba99faa48e5c959edabcdc234ac457 *xmrig-6.16.4-linux-static-x64.tar.gz
25716d7d3a6e2d1028e2753f2fed229fe0ff3f57b9ff5b451a4b3f57f19a8678 *xmrig-6.16.4-linux-x64.tar.gz
9405a71971755660166ba32b2c34b546a29ac7e91b95a9e41da9f2fe8a8618c4 *xmrig-6.16.4-macos-arm64.tar.gz
f5c3dba40c3f96e86524a607f5b49eac5bda4a3d3e3a22a20ad23bec8e21488f *xmrig-6.16.4-macos-x64.tar.gz
a85955f1e36a152bec29140868f316bb89c7b279b3fb8feb470c72ad5c3641e8 *xmrig-6.16.4-gcc-win64.zip
556d1bb4897dc97eb458263158d480c8f93d443fc05808c05aaa9b17a0d6c379 *xmrig-6.16.4-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmH9AQIACgkQRGpTY4vp
RAnx+Af9FD+J2DfW/kfSpQLMZHqAXrK3q4RQZ6KCY0R949eANg1LIpvCTpK3ZV/a
bgytAaVVTWxg5RocuiayLiQkSaGXmbNBjzgRSNXNt0W87bk007P+Iy/Py6HHPl5S
imV1q9LEQ5DHsLCivxAEMk4V/YcpHRcAFQnU6M+qifVZ/Dg1Af/6A99tq3Uk/rZY
A0tUjhMi7rXlRQhtoRktAWRbzTQenIFEsKsTsHxNm4tPn+fVkzQdKCg1uo2uyTtn
tigfxHG9FgwcmRTsDe351rS5atkcTNTiuVoCnnCEi4wiiu46Wsu9ZKVxbUm14Blq
KdawYJLmPkWutUhyRGKBCKp2roDG4w==
=Dthi
-----END PGP SIGNATURE-----
```