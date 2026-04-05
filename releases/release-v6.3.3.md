---
title: v6.3.3
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.3.3
author: xmrig
tag_name: v6.3.3
published_at: '2020-08-28T15:07:47+00:00'
---

# Version: v6.3.3

# Release Notes
## Notes
- **[KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915) :new:**
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.3.3
- [#1817](https://github.com/xmrig/xmrig/pull/1817) Fixed self-select login sequence.
- Added brand new [build from source](https://xmrig.com/docs/miner/build) documentation.
- New binary downloads for macOS (`macos-x64`), FreeBSD (`freebsd-static-x64`), Linux (`linux-static-x64`), Ubuntu 18.04 (`bionic-x64`), Ubuntu 20.04 (`focal-x64`).
- Generic Linux download `xenial-x64` renamed to `linux-x64`.
- Builds without SSL/TLS support are no longer provided.
- Improved CUDA loader error reporting and fixed plugin load on Linux.
- Fixed build warnings with Clang compiler.
- Fixed colors on macOS.

## SHA256SUMS
```
bc3b0f4b3442b5159b57510d44123e96618caef637bc2202633cafa33d75ae02 *xmrig-6.3.3-bionic-x64.tar.gz
0bfb7ba998e5f70682cb3ee5332269a06b86f7884e98588014aec179f5b4f988 *xmrig-6.3.3-focal-x64.tar.gz
cfda6309ed0ce7ad0529500a78eac2112a47f79796a8d0ed4fee72211bcb168f *xmrig-6.3.3-freebsd-static-x64.tar.gz
ad1133cdcb486bab2368347b3ab35e83e5cd492c4bc6bfcb11a4b4c99d2c8014 *xmrig-6.3.3-linux-static-x64.tar.gz
8572c53b8085f5f269aa1070db460c5c5d6f79cfd8a211f74a54aa0841e4543f *xmrig-6.3.3-linux-x64.tar.gz
e9882f125c5b8c3740e82e916b0c4363572923b8e6eff1e89c52f153f6d70559 *xmrig-6.3.3-macos-x64.tar.gz
f13410f88d35cfe09c76efd75d55e9445c718f069e97858a261450af212ba641 *xmrig-6.3.3-gcc-win64.zip
0c227d4876456601ab966a386ab360cfbc957b7ff4ccc4d7944f25d49975c6bf *xmrig-6.3.3-msvc-cuda10_2-win64.zip
98f370f87b75e9d2718837c91746a0e6e04d292f4a348bc3fc457c5abdbc94e5 *xmrig-6.3.3-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl9JGuQACgkQRGpTY4vp
RAnKQQgA0mBMkVJO3d7rq7OxbI73j6E0Jsnse0Homv7Wt+ypCL7SWVRfxmzxjNdy
o301JfnCGRtHHo55CjELU84AkGiUTwpWQa2J4HWIpuKp+ALvbJPJ3WVKdGXTHLJ0
Yyk3CJ7nQ61yocDh+jiGtiXmP7EmkeM8ksLzFceoCFcTEkpMSWvrcY56LrZikSR+
r0kgXh9YbeQ1A/TR4pzX6aHMelgw7zf5mWgMm6/czZXIND4L8WTUXB3OuruduJHo
ZppV5S844DX+z2ji/9Oh6WoODzsVCvINhlSTWknEe3g1KmSlWdEJTJZoShMSHOOH
qx1ynvEkDEnb9RP7a8Gs41EWT2LPzA==
=8VQz
-----END PGP SIGNATURE-----
```