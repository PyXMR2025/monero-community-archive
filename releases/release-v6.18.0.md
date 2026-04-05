---
title: v6.18.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.18.0
author: xmrig
tag_name: v6.18.0
published_at: '2022-06-23T13:55:45+00:00'
---

# Version: v6.18.0

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- VAES optimizations not supported by `xmrig-6.18.0-linux-x64.tar.gz` due old compiler, please use `xmrig-6.18.0-linux-static-x64.tar.gz` instead. :warning:
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.18.0
- [#3067](https://github.com/xmrig/xmrig/pull/3067) Monero v15 network upgrade support and more house keeping.
  - Removed deprecated AstroBWTv1 and v2.
  - Fixed debug GhostRider build.
  - Monero v15 network upgrade support.
  - Fixed ZMQ debug log.
  - Improved daemon ZMQ mining stability.
- [#3054](https://github.com/xmrig/xmrig/pull/3054) Fixes for 32-bit ARM.
- [#3042](https://github.com/xmrig/xmrig/pull/3042) Fixed being unable to resume from `pause-on-battery`.
- [#3031](https://github.com/xmrig/xmrig/pull/3031) Fixed `--cpu-priority` not working sometimes.
- [#3020](https://github.com/xmrig/xmrig/pull/3020) Removed old AstroBWT algorithm.

## SHA256SUMS
```
b177a458a71393384b1ad1f1129b6aedb581c23d17f878351e96f3480de313ba *xmrig-6.18.0-bionic-x64.tar.gz
4520448ae9ae681cfbeb6d08db9868211789038ddf5cdafe991685e3cf8eb752 *xmrig-6.18.0-focal-x64.tar.gz
4baba49a5b4e77a909d3a2c29aae9c9c25ba30c4f9b6c3d27cda6c8fc29b9aa4 *xmrig-6.18.0-freebsd-static-x64.tar.gz
8de5a261b1a90db90c6de3a20041863520afa536b019b08e9fc781cb7ef1fcc1 *xmrig-6.18.0-linux-static-x64.tar.gz
d84bcfd38f8f2a35702ed52ef90fe9bbe7f6a6fbbf2e05814ed4e137fc5730ca *xmrig-6.18.0-linux-x64.tar.gz
fd64cad3dc553b64626342c92f6c0d206015558e9fd6e4f9bf82c6c30da12530 *xmrig-6.18.0-macos-arm64.tar.gz
85f7b1c68be609309b32f449f92bf70b116ba0bf88f175fd3d25a5492c80b06e *xmrig-6.18.0-macos-x64.tar.gz
a37abd795444e9a1a576bb4d4131524363fc30b55088fc88dfe79689fbc2fda4 *xmrig-6.18.0-gcc-win64.zip
c0683e3fa96ae82000af40a08c50eaea0266d2b937c11455d5a3a2393aacd086 *xmrig-6.18.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmK0br0ACgkQRGpTY4vp
RAkyhAf/SBPYfroguaXGo035Ti4/YIa80x373g2Spgk78h9rqb1GfpsphMJ83J/d
NTs1zJDiv8LoM9yZs8A6bwIjDb2jzp28XpQ3SvDrl/8MWW8XjQRuh1EF4NGBOrpB
DRTYIaxGV6YsgSkG/bDPqvj7KYbqwelpYH04QnIQHt/MTbf1OejzWdLs0QPl3PxH
IbeV+hZ41JrcMPVV4aycOLSEMCXThDVUofihzqRrZkb55LnHj0f6dwJEgfpW91a4
F4MbT83QL9MItJ4zQm8OuEF1LDTlhE1iA+HPnfeat1rhmXmwkaE+6TRi2LqOEko7
d3Xvbe1BAE4jjCNysXjtRkfR1z2yLA==
=+XYP
-----END PGP SIGNATURE-----
```