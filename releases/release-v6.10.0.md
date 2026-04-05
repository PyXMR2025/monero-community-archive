---
title: v6.10.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.10.0
author: xmrig
tag_name: v6.10.0
published_at: '2021-03-07T21:54:35+00:00'
---

# Version: v6.10.0

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.10.0
- [#2122](https://github.com/xmrig/xmrig/pull/2122) Fixed pause logic when both pause on battery and user activity are enabled.
- [#2123](https://github.com/xmrig/xmrig/issues/2123) Fixed compatibility with gcc 4.8.
- [#2147](https://github.com/xmrig/xmrig/pull/2147) Fixed many `new job` messages when solo mining.
- [#2150](https://github.com/xmrig/xmrig/pull/2150) Updated `sse2neon.h` to the latest master, fixes build on ARMv7.
- [#2157](https://github.com/xmrig/xmrig/pull/2157) Fixed crash in `cn-heavy` on Zen3 with manual thread count.
- Fixed possible out of order write to log file.
- [http-parser](https://github.com/nodejs/http-parser) replaced to [llhttp](https://github.com/nodejs/llhttp).
- For official builds: libuv, hwloc and OpenSSL updated to latest versions.

## SHA256SUMS
```
9f1b0acaaa8f4202c76be3e7263c68c8c3f68666b76aee0492742e77a0de56af *xmrig-6.10.0-bionic-x64.tar.gz
a43df8abe7b964973dfec08d6af7181232a9fdaa1e83f9125fcafc5a4e4c7852 *xmrig-6.10.0-focal-x64.tar.gz
1c198a8a449677aaa71ab927732d8198381f0b7a6cb596944a4e99e14d49bfc6 *xmrig-6.10.0-freebsd-static-x64.tar.gz
9cf853a49247acca754c25d21af5eb2c8ae079c658b89e752e7888aa64ba21e9 *xmrig-6.10.0-linux-static-x64.tar.gz
4079b3b34caa86dce0edc923a3292f5814dd555f28e8e6ec4c879a2c50a80787 *xmrig-6.10.0-linux-x64.tar.gz
d629e4e15df5504b47a5154399e8acb1b1dc838b555ea1675e99ef24b4496193 *xmrig-6.10.0-macos-arm64.tar.gz
5373e6eb3384075322e758dd8fb0f848f84e7a208eee67a967afbff6b593bb6d *xmrig-6.10.0-macos-x64.tar.gz
bece31a44a4c374de40b86f1883c9259c02b01c7da55c7c914297b8cbdae88ef *xmrig-6.10.0-gcc-win64.zip
5c51edc9032ae941046cd5f7718eae46436770199c21499d4e180777e78c6e41 *xmrig-6.10.0-msvc-cuda10_2-win64.zip
54251e6075d2d68f6505890c7c89825d56d7497fc6ccd688a41d9de7f1813440 *xmrig-6.10.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmBFSnwACgkQRGpTY4vp
RAltZQf/Ry8eqMFVUKIT1s9PzJv9q+MfzP8MaWGzkWvZQp/QHvy5olFu8KlExrhy
SG3nqDxd3f9e/5hRNYW44bZGb9yQjkC+w7ceMSigIOdHv+SWmScoD/Zi/UrqI2ht
NUBva8rldjLYDrt9agpL2CLyV2BWqt8kF0QYALgVtcqhCR8yTQKctzniFe0lVOqp
WzJL0Nx05NaeP04ggXCbmX/vZLYQkr0qMx9AnRK0F/cyBbalzCdbOhIA0RxCJkD9
4MQWP+AVeiC76ffPkE3CN8WuqSuTvUMSt5LOL0+h5LzygynMSy9wb42k3uZPEmRa
gaz4lmDAK/QWWTNkTNz4LeNXspikVQ==
=4D39
-----END PGP SIGNATURE-----
```