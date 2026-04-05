---
title: v6.17.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.17.0
author: xmrig
tag_name: v6.17.0
published_at: '2022-04-05T16:24:54+00:00'
---

# Version: v6.17.0

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- VAES optimizations not supported by `xmrig-6.17.0-linux-x64.tar.gz` due old compiler, please use `xmrig-6.17.0-linux-static-x64.tar.gz` instead. :warning:
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.17.0
- [#2954](https://github.com/xmrig/xmrig/pull/2954) **Dero HE fork support (`astrobwt/v2` algorithm).**
  - [#2961](https://github.com/xmrig/xmrig/pull/2961) Dero HE (`astrobwt/v2`) CUDA config generator.
  - [#2969](https://github.com/xmrig/xmrig/pull/2969) Dero HE (`astrobwt/v2`) OpenCL support.
- Fixed displayed DMI memory information for empty slots.
- [#2932](https://github.com/xmrig/xmrig/pull/2932) Fixed GhostRider with hwloc disabled.

## SHA256SUMS
```
a09d55b6e4eadc8d5e02a29df34ea3e4f08004a790be54a32eec730618bbc0f9 *xmrig-6.17.0-bionic-x64.tar.gz
254b102ddb5f22a8ad11f76f13651f1ff94210e855a164f1f20589753532033b *xmrig-6.17.0-focal-x64.tar.gz
967e27b31305e6ab13173c0203ffa6cd974c82eeb2286b7bc9d3ae8014d3e8bb *xmrig-6.17.0-freebsd-static-x64.tar.gz
975b4f29621dcc67f531796d8b24826b361d2c1fd97193a9b5a80b5aad039eb3 *xmrig-6.17.0-linux-static-x64.tar.gz
75ce5d4d52c46a7c8c604e1de3549cba9dc4b07405d6598e12b6f21f50247739 *xmrig-6.17.0-linux-x64.tar.gz
b17f97f06e19023e1c1c5fbfb1536901de33dc29fdbf865ac4ef4873f67e4e08 *xmrig-6.17.0-macos-arm64.tar.gz
e08e7924248c953086ffb00b1be3e0c4e7a780859df2b344500d9f14e7d122cf *xmrig-6.17.0-macos-x64.tar.gz
0fc69e6c4316dab6a7de1b14700f75bbd37248aa6eab5c415fc86c1c774ccee3 *xmrig-6.17.0-gcc-win64.zip
50aeef5261daf0e0601693f427bf94f23aa285600a309e3c6b0ba0d5c3dd2331 *xmrig-6.17.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmJMa8MACgkQRGpTY4vp
RAmePAf/UkB3AqGRLO5MUnIzzpn6llw76ksG6iUYYDb2eeEjdluISkdOezjpbBG7
o7kR+++K4RHSEUdfDOEuKqAwvrP7VuvrQPMlYsIOUhM/Cy0/cfx9BghiCQp8aw+d
1ALoi/iJ/tgBklGa0RZrX5jvzN5AF50LSziPLJ/B2sqbWDQNwSYeTUkLzzHGXQpN
LxMI45nLGG2+I3VRhe7o1Pwq7mwm1aqIXHvUR+JpPCVZO9C/ICI5B/LmkQKJEe2x
MPnXSmdAkDTORDRMzu5/ZoSs2ZTgdV3Qzd67+eTH1ETwaq6zdg6f0MSyBgMg4Sl1
1a8rPmD1/VPBqycq945nMx9Kgm2zHA==
=1f4Q
-----END PGP SIGNATURE-----
```