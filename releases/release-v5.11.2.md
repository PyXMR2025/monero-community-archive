---
title: v5.11.2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.11.2
author: xmrig
tag_name: v5.11.2
published_at: '2020-05-23T04:50:12+00:00'
---

# Version: v5.11.2

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.11.2
- [#1664](https://github.com/xmrig/xmrig/pull/1664) Improved JSON config error reporting.
- [#1668](https://github.com/xmrig/xmrig/pull/1668) Optimized RandomX dataset initialization.
- [#1675](https://github.com/xmrig/xmrig/pull/1675) Fixed cross-compiling on Linux.
- Fixed memory leak in HTTP client.
- Build [dependencies](https://github.com/xmrig/xmrig-deps/releases/tag/v4.1) updated to recent versions.
- Compiler for Windows gcc builds updated to v10.1.

## SHA256SUMS
```
e8412a9f6db5032cb15d4735e9233c2f22e08a79f6c80c12f53d3d89d6b4a5d2 *xmrig-5.11.2-msvc-cuda10_1-win64.7z
0c6227efbcf49a8ccda6ac49691c0dfc959315c2d2742ec9ef990a2f6fa5186e *xmrig-5.11.2-xenial-x64.tar.gz
c3f518e8b9216bb58f62d566f620b7cfa3454328dfdbc72c7b7c834fe7e43c7b *xmrig-5.11.2-gcc-win64.zip
d7d5fdb83cad86ec481f02a5fb9a1ecb3ed700727f0c78290564b1dca84f69af *xmrig-5.11.2-msvc-cuda10_1-win64.zip
cfdd425ad2533820fab5f11fd8a6b3fb7ddb37b2be74a905bc116f6718dcec19 *xmrig-5.11.2-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl7IqhcACgkQRGpTY4vp
RAmImwf/QXUE8q4psoALxKlVfsye6mQFibSzDJlnhUVZ4g6Dd/kVRJ8ZopPU+d5/
Skr97Yh9/pf5FakVcRWyGb5tv07yxxsaD6sXMcFHxVd5M3lO9JAo/95rHVriYhs8
YePOmHZgyFTsTVZH1d8Vh+/Aku02MFlxRMt4ZvhUEdj1W/eus7+r1ZrQqggkPTjP
i4xKhYma3Lp36P0YsaiEEeiefO47uJqMQgX0cjiOmav5oGb/QirZcHho9/JDqs+h
9fJbAPzdWyFczFgEfKCElD6INsHMdBWCxTE0NzDVcWdROkc3TvqELx6Tsx9w4P2N
f561gaM9e82Z6JFPvDj3Znw7yzlk5w==
=DpyX
-----END PGP SIGNATURE-----
```