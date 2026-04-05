---
title: v6.19.3
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.19.3
author: xmrig
tag_name: v6.19.3
published_at: '2023-06-03T13:33:49+00:00'
---

# Version: v6.19.3

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- VAES optimizations not supported by `xmrig-6.19.3-linux-x64.tar.gz` due old compiler, please use `xmrig-6.19.3-linux-static-x64.tar.gz` instead. :warning:
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.19.3
- [#3245](https://github.com/xmrig/xmrig/issues/3245) Improved algorithm negotiation for donation rounds by sending extra information about current mining job.
- [#3254](https://github.com/xmrig/xmrig/pull/3254) Tweaked auto-tuning for Intel CPUs.
- [#3271](https://github.com/xmrig/xmrig/pull/3271) RandomX: optimized program generation.
- [#3273](https://github.com/xmrig/xmrig/pull/3273) RandomX: fixed undefined behavior.
- [#3275](https://github.com/xmrig/xmrig/pull/3275) RandomX: fixed `jccErratum` list.
- [#3280](https://github.com/xmrig/xmrig/pull/3280) Updated example scripts.

## SHA256SUMS
```
4c97972d3a24638f2334544ff3f0735f7fb785a54b2bc51f8e178a721b7f1357 *xmrig-6.19.3-bionic-x64.tar.gz
619a3f0b2fa7451abbaa20d5608cbddd76784b92593a92ef840e00bc81f3d36a *xmrig-6.19.3-focal-x64.tar.gz
1644584a605b40cd570ff089004f7fc4d5cad0ef93a02b15498362a872895ffa *xmrig-6.19.3-freebsd-static-x64.tar.gz
d8de8bbb4f48caf9c2510f39c005ce63a198e21fcb2fa1520116759c6b6a3d70 *xmrig-6.19.3-linux-static-x64.tar.gz
e56d2dd09018e3dc9d8600e21706afbf546a634b529f77b9d81632ab8b66c51f *xmrig-6.19.3-linux-x64.tar.gz
12a331c33cb6a6a03c2ad0fdd29908bf1730fa2ce523b4b499459f4a581b2f51 *xmrig-6.19.3-macos-arm64.tar.gz
60235223534bbaa725f866c68650a4c333aca0b3e9422bd22dd5c4c383709d1a *xmrig-6.19.3-macos-x64.tar.gz
4477f2b99e1f2c973d68f05856226823887ec45f9a515923ff7849b26ad2b840 *xmrig-6.19.3-gcc-win64.zip
ce0c28e5c89c92baa26dd57ca157b4d58aad30ee1d2a5e0a39e6d0126318de2c *xmrig-6.19.3-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmR7QGcACgkQRGpTY4vp
RAnl1wf+P383uiyp4aewQa58zhjN/Sx1hor8+2AXdmeWL6ER7D72kDuS5LTcHVX8
JPbCcFTFQnP+4ILD5hGnWk/o2IN95FkYVTIKxP0g2nZM0r940I1B0/tugjTg3XnW
GRu/6LGYLq83JxOrNE3C6S4Gsdji4XFBF/nkzP0EosAFpYx6vc7HC6L3axgFuqNC
+DRijrwfJIk4kNpYh/7aPQxAFqw8fPFJcRkNd7Mwb4U+l5E4Ik1DZ34f9aveg8xO
+6+3fvF5c3IlnbHnLmkiwn/YCYwxaNS4WNFz+0u6uZzEECPravwMRD2erZMo07+B
aoHh1780lhLfyQ2hknfO9Symwn+NSw==
=23ka
-----END PGP SIGNATURE-----
```