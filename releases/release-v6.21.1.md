---
title: v6.21.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.21.1
author: xmrig
tag_name: v6.21.1
published_at: '2024-02-25T15:55:41+00:00'
---

# Version: v6.21.1

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- VAES optimizations not supported by `xmrig-6.21.1-linux-x64.tar.gz` due old compiler, please use `xmrig-6.21.1-linux-static-x64.tar.gz` instead. :warning:
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.21.1
- [#3391](https://github.com/xmrig/xmrig/pull/3391) Added support for townforge (monero fork using randomx).
- [#3399](https://github.com/xmrig/xmrig/pull/3399) Fixed Zephyr mining (OpenCL).
- [#3420](https://github.com/xmrig/xmrig/pull/3420) Fixed segfault in HTTP API rebind.

## SHA256SUMS
```
1005ec64558a16b5a4638629ca512d20b9d64079b43592679c33697b4a388a20 *xmrig-6.21.1-bionic-x64.tar.gz
5ec2dfef44bc46694309a9a3b9c5ff41b425771e11df39c49f2c8eb8d72f050f *xmrig-6.21.1-focal-x64.tar.gz
46faa339f9a5889226940b1a523b4f8679affd4993d4d8b6863ee7bf20665f7f *xmrig-6.21.1-freebsd-static-x64.tar.gz
d41502a3caaa9ed3e4bfb4c2ccabba0d7225be4b87361329fc5db0349c67777a *xmrig-6.21.1-linux-static-x64.tar.gz
8dafcfa9ccaf2b717f3dbbccfbb746a22db11ac38bc2e14448f084ce9c7258cd *xmrig-6.21.1-linux-x64.tar.gz
6ab24cb0b5061992c76c458c75f48cd296d25c935601d7e0b7b0c462714295a1 *xmrig-6.21.1-macos-arm64.tar.gz
6213c8f08c738a9268ee04fe85a4bbadfa8fa202a8bec7c846aa5f55a739a395 *xmrig-6.21.1-macos-x64.tar.gz
fa6214ad822c6a70ee064de975608438a55eac4de41a5bb20f7180895e0524f9 *xmrig-6.21.1-gcc-win64.zip
65f378d0c6868212f611bd94514f32674d795719880e0aa95e5b3c8a211b38cf *xmrig-6.21.1-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmXbYa8ACgkQRGpTY4vp
RAn7Rgf7BtJ2KvyBSskrNcBxrVcqpsMbAddN3F0u+Qph6nXj697+aKmJcQpzUHcQ
HBE76xZPdwHvSp9zgu1mvWgjpXcuMyvI7S95MuX+Gy1GNyVHfG3FrylMPHiDayJQ
qDpSRhyVcQhC2t11nfBHQys3FxPKBAbg/yPw65SxKzN1I0Ep13ApcEQcQZHGc9cu
cUL8y0LlUKzUeq46Tpl6VvNOi6vvxTcFRTPCM1Amsa45nK9Hi/NT/DUBb83VEL/z
R1ooc297ZhwOqSnsTRWnnQ+Bt/ajSLeQlbT8nNWNkxI5SoDhosstNJXozAs/ZVyz
VktK77k/f8cx5YOJYsPE5B5NQi0sKw==
=JHeS
-----END PGP SIGNATURE-----
```