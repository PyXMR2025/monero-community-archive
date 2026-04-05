---
title: v5.5.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.5.1
author: xmrig
tag_name: v5.5.1
published_at: '2020-01-12T02:25:19+00:00'
---

# Version: v5.5.1

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.5.1
- [#1469](https://github.com/xmrig/xmrig/issues/1469) Fixed build with gcc 4.8.
- [#1473](https://github.com/xmrig/xmrig/pull/1473) Added RandomX auto-config for mobile Ryzen APUs.
- [#1477](https://github.com/xmrig/xmrig/pull/1477) Fixed build with Clang.
- [#1489](https://github.com/xmrig/xmrig/pull/1489) RandomX JIT compiler tweaks.
- [#1493](https://github.com/xmrig/xmrig/pull/1493) Default value for Intel MSR preset changed to `15`.
- Fixed unwanted resume after RandomX dataset change.

## SHA256SUMS
```
b6e506853319ed484c1f17ceb7b3329d31320ba020c3aeaa31f9f28b17e27f88 *xmrig-5.5.1-xenial-x64.tar.gz
bfefa819eff6088734cc7d4333392b489ea44d189211990a12d6dc30d03eb03d *xmrig-5.5.1-gcc-win64.zip
7b57144b8e5c8e9816ed74658d9a877654dbe64d33a4d9aa736750648c786fd3 *xmrig-5.5.1-msvc-cuda10_1-win64.zip
6df9967bae86dd1826bf3a1f9b5f3789d72b4b303aacb59ad696510015ad80ff *xmrig-5.5.1-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl4agEMACgkQRGpTY4vp
RAmPAwgAoDMS1q8R9AVy0qW68mmgYXFWxvTU2yukNYplTDizabEkzWMs0y+xv0L8
bSK4vJJuHatqsYc3qjnFQgdVZ7wtdd2Tjeu4gIET+0QeUklMLt7Xy2dtDlPVSfFV
0hzBtFmjpsMOWTY/7h2fSo207gf/xxOIRTTcjjOnJNqWVCrbJM2CM29YGb3ecPYy
AX7RcH7Zw3COI1xZJKMm6JHrEutyAwQk4gYUuf84wFa1v9h7CSZxYbmdokz9q6O8
KGnJLL44uXnewNrEozDOQyCewsuHRCEMFmiJP6ojbcirX9dKDTLfhgGgSUj/Xy+Q
rqrqQonEkDrdvQ2S+U6rvlSg5X95Wg==
=BhRJ
-----END PGP SIGNATURE-----
```