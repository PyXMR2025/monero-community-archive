---
title: v6.21.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.21.0
author: xmrig
tag_name: v6.21.0
published_at: '2023-11-23T14:16:02+00:00'
---

# Version: v6.21.0

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- VAES optimizations not supported by `xmrig-6.21.0-linux-x64.tar.gz` due old compiler, please use `xmrig-6.21.0-linux-static-x64.tar.gz` instead. :warning:
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.21.0
- [#3302](https://github.com/xmrig/xmrig/pull/3302) [#3312](https://github.com/xmrig/xmrig/pull/3312) Enabled keepalive for Windows (>= Vista).
- [#3320](https://github.com/xmrig/xmrig/pull/3320) Added "built for OS/architecture/bits" to "ABOUT".
- [#3339](https://github.com/xmrig/xmrig/pull/3339) Added SNI option for TLS connections.
- [#3342](https://github.com/xmrig/xmrig/pull/3342) Update `cn_main_loop.asm`.
- [#3346](https://github.com/xmrig/xmrig/pull/3346) ARM64 JIT: don't use `x18` register.
- [#3348](https://github.com/xmrig/xmrig/pull/3348) Update to latest `sse2neon.h`.
- [#3356](https://github.com/xmrig/xmrig/pull/3356) Updated pricing record size for **Zephyr** solo mining.
- [#3358](https://github.com/xmrig/xmrig/pull/3358) **Zephyr** solo mining: handle multiple outputs.

## SHA256SUMS
```
d8c8c06ba31b56784b7305cd67d8c2f2642745a066aac13bf41003e9578a609d *xmrig-6.21.0-bionic-x64.tar.gz
bfa64cb89dfb08466f7e3f38b74f0b046ba6bf2cebdb5dea333198e7090dad33 *xmrig-6.21.0-focal-x64.tar.gz
596c89eb7497d80613a11fa4844cc355f9e72ae3477d47aa570d1c087ec411c5 *xmrig-6.21.0-freebsd-static-x64.tar.gz
c5dc12dbb9bb51ea8acf93d6349d5bc7fe5ee11b68d6371c1bbb098e21d0f685 *xmrig-6.21.0-linux-static-x64.tar.gz
7662ccbd97f0b579e9faf025b9872dc20759a791b572946aec247c12334e0d3f *xmrig-6.21.0-linux-x64.tar.gz
8d5c75d5e8ebf118cd0e1add533d9ff71f29ffa317a9e03c669779f61036cfd9 *xmrig-6.21.0-macos-arm64.tar.gz
ecd98acb25434368b076e915c7e0d4273f1817a08c09ba4fbfa4d93853b2bd21 *xmrig-6.21.0-macos-x64.tar.gz
4b8e7ff95e742973fb9c8c38ac68f6a1e692b05415036e1c92ee201b3b0e6699 *xmrig-6.21.0-gcc-win64.zip
4cf4198354abfee7e502c85f38e62dbb90fec976e4df38d0ecbfd811937c1981 *xmrig-6.21.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmVfXUUACgkQRGpTY4vp
RAkKhwgA3CtSDrnJLPxItHCPYGTnykCGsEstvEfrk1cxCWKWPKgRQymORzhR6p+7
QAekgZrr5MgpKPN4jM5mNbk2X+YU2w3ZBQbRtDVgYESmnGwWQb6nmSSBzPygfqpq
7fMdYnQhFXQKNzocsQUAnddL9QNufS7dpXhVrpenURTCHEnK7205qzrVwExp/PQS
ZinfGiLnfuq1YKQlctMLmtvTcwtSJCyqM5VLE3kh7RxFhGei8eV+BaazTphn0xSP
9xzDybPh2vd7uagwIBg6VA/4DZsuEfBUCaw4tbntoANt8D36WfWYGPw93OisZgMf
738z7++M4XFm7aaFuE+RCfjpEQA4bQ==
=zBo5
-----END PGP SIGNATURE-----
```