---
title: v6.19.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.19.0
author: xmrig
tag_name: v6.19.0
published_at: '2023-02-02T05:22:21+00:00'
---

# Version: v6.19.0

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- VAES optimizations not supported by `xmrig-6.19.0-linux-x64.tar.gz` due old compiler, please use `xmrig-6.19.0-linux-static-x64.tar.gz` instead. :warning:
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.19.0
- [#3144](https://github.com/xmrig/xmrig/pull/3144) Update to latest `sse2neon.h`.
- [#3161](https://github.com/xmrig/xmrig/pull/3161) MSVC build: enabled parallel compilation.
- [#3163](https://github.com/xmrig/xmrig/pull/3163) Improved Zen 3 MSR mod.
- [#3176](https://github.com/xmrig/xmrig/pull/3176) Update cmake required version to 3.1.
- [#3182](https://github.com/xmrig/xmrig/pull/3182) DragonflyBSD compilation fixes.
- [#3196](https://github.com/xmrig/xmrig/pull/3196) Show IP address for failed connections.
- [#3185](https://github.com/xmrig/xmrig/issues/3185) Fixed macOS DMI reader.
- [#3198](https://github.com/xmrig/xmrig/pull/3198) Fixed broken RandomX light mode mining.
- [#3202](https://github.com/xmrig/xmrig/pull/3202) Solo mining: added job timeout (default is 15 seconds).

## SHA256SUMS
```
ba841674d35e6e6b3b1118fa8cecced3044cee40cea5d5bac079678cfb36604c *xmrig-6.19.0-bionic-x64.tar.gz
550414f0e102ec89fe0482a095867c5069a6eee3900027397a556dd47dc6a7f3 *xmrig-6.19.0-focal-x64.tar.gz
12260288e789d947cd23a5b354d2ad4e159e07d63b533248aba0979c90744043 *xmrig-6.19.0-freebsd-static-x64.tar.gz
f10c3084797f942f4c3895f345b12f6e554158863d96d30167acd4d203e52c9f *xmrig-6.19.0-linux-static-x64.tar.gz
9ed5a3b5be3393b8231ce42a73e39433b5822ff8ba7ebe0c6786f0505e89a11a *xmrig-6.19.0-linux-x64.tar.gz
82f499ca17668bed0332857f636014d7f772785da34cf2cd2839f17fc970dba0 *xmrig-6.19.0-macos-arm64.tar.gz
3e133785aac1d0ade268f1d8e55febf7e059f31b0987456d135ca37c851d2f73 *xmrig-6.19.0-macos-x64.tar.gz
a1a17ca76ebf8063837b0c02450e660e7ea7bdf822c841234cc2aaa571e82850 *xmrig-6.19.0-gcc-win64.zip
0e828b9de94058b0a96c32818f341268d67634f7ce55be675bfa37484ad38950 *xmrig-6.19.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmPbxv8ACgkQRGpTY4vp
RAl0bwf/VizYn39rISQzbVMWNfxR1dOP7xoss7bwozob3wswNl77gj7tS3gkYgKM
qvG0V7k1Tf8xcXS9AtVVG32B13JcAMfWnde/WcdKLFELVLp+FRD2RLQZaxHAKDLt
tCxu5OHFUEXOU6VtTl7+d/QAlCgONdEc4NY5oUE4brEoVtPMMTzK400ERfWTrCOD
/uCHz1ZAiD8VlMWS6tGNO0+yesj+V/VCJq4oeo9mCVzgjON58AuTe0eHcjsXgeeS
gGA/44lx6vZfWpka4RWtdgsqxJGBnX7sqxqd3WS9C2PeNIQPI/kXtsNj6BGu/r3R
9Oowah6TMKDicl/MqqrRRoQvelwP4w==
=8LIF
-----END PGP SIGNATURE-----
```