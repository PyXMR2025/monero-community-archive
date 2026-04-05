---
title: v6.18.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.18.1
author: xmrig
tag_name: v6.18.1
published_at: '2022-10-23T11:21:01+00:00'
---

# Version: v6.18.1

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- VAES optimizations not supported by `xmrig-6.18.1-linux-x64.tar.gz` due old compiler, please use `xmrig-6.18.1-linux-static-x64.tar.gz` instead. :warning:
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.18.1
- [#3129](https://github.com/xmrig/xmrig/pull/3129) Fix: protectRX flushed CPU cache only on MacOS/iOS.
- [#3126](https://github.com/xmrig/xmrig/pull/3126) Don't reset when pool sends the same job blob.
- [#3120](https://github.com/xmrig/xmrig/pull/3120) RandomX: optimized `CFROUND` elimination.
- [#3109](https://github.com/xmrig/xmrig/pull/3109) RandomX: added Blake2 AVX2 version.
- [#3082](https://github.com/xmrig/xmrig/pull/3082) Fixed GCC 12 warnings.
- [#3075](https://github.com/xmrig/xmrig/pull/3075) Recognize `armv7ve` as valid ARMv7 target.
- [#3132](https://github.com/xmrig/xmrig/pull/3132) RandomX: added MSR mod for Zen 4.
- [#3134](https://github.com/xmrig/xmrig/pull/3134) Added Zen4 to `randomx_boost.sh`.

## SHA256SUMS
```
74eedd71adfd3bb42e2a8e69416f73d91a40be25301437220c5e098bfb72e7a1 *xmrig-6.18.1-bionic-x64.tar.gz
820618f9dde020591d811422fee9a980783073b4b42303a12d5756c147f7e7d6 *xmrig-6.18.1-focal-x64.tar.gz
2de993cee9f0ac4d7b6737634c886e3a0c272c950a25100595d2b95d8faee416 *xmrig-6.18.1-freebsd-static-x64.tar.gz
99a082f0d801be63e26bb96473409c2f9d98629b453d907554b3a107efd284fe *xmrig-6.18.1-linux-static-x64.tar.gz
e5c588f7cf9b177a58bb4dfc3410a984221d1cf2d95a1acc135e582020ac970e *xmrig-6.18.1-linux-x64.tar.gz
f3c7c3aa7ebb8b241e01250044b88e5b7e814723db2339a6226aa6370dddb976 *xmrig-6.18.1-macos-arm64.tar.gz
119c0c365697a98899493dc77dc6ea85b2ee6d08328845526f211a581f64b93b *xmrig-6.18.1-macos-x64.tar.gz
e12abacd392970ecd60e3ef32eaad5d17377b29be257ef2a2a1bd4cd2eda6176 *xmrig-6.18.1-gcc-win64.zip
8c231f2ebe719066ad3c85b8bea98e1a867af85643d4285c7d33f890d1d22338 *xmrig-6.18.1-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmNVIHcACgkQRGpTY4vp
RAnZwQf9FWbPSGA5p0f4mFYh4QChixOUiO5Z3MnwVP3+iC++EFmJoC1KvEK+DPwG
bfyTZ51AewK1wcXqiKnb+wwwbAJWbMN89lSMoGB34GDhY+TdqxMl60KuhVG4Uuqm
PFdxIM9DsPZI0m0XIK1TBWKuRUu3OFCsIKpUhpxJnfIEMg1hNR1y7clfuIjypjbB
qMv1fpUXv8/65efwMs9MIixgaJB9mFGZN1UnHzLoHMbAZo7v27vG77nAsNMxgGi4
nXGiMaCPXqLt64m7SEE+5lx1EToGqVXKSlT9fCeTu4ii0P8g8sQV3tvPucGDfnGc
v37KYifBlJesiMHgLgXjY01vwPgrBA==
=cYC9
-----END PGP SIGNATURE-----
```