---
title: v6.25.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.25.0
author: xmrig
tag_name: v6.25.0
published_at: '2025-12-23T13:18:44+00:00'
---

# Version: v6.25.0

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on X https://x.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.25.0
- [#3680](https://github.com/xmrig/xmrig/pull/3680) Added `armv8l` to the list of 32-bit ARM targets.
- [#3708](https://github.com/xmrig/xmrig/pull/3708) Minor Aarch64 JIT changes (better instruction selection, don't emit instructions that add 0, etc).
- [#3718](https://github.com/xmrig/xmrig/pull/3718) Solo mining: added support for FCMP++ hardfork.
- [#3722](https://github.com/xmrig/xmrig/pull/3722) Added Zen4 (Hawk Point) CPUs detection.
- [#3725](https://github.com/xmrig/xmrig/pull/3725) Added **RISC-V** support with JIT compiler.
- [#3731](https://github.com/xmrig/xmrig/pull/3731) Added initial Haiku OS support.
- [#3733](https://github.com/xmrig/xmrig/pull/3733) Added detection for MSVC/2026.
- [#3736](https://github.com/xmrig/xmrig/pull/3736) RISC-V: added vectorized dataset init.
- [#3740](https://github.com/xmrig/xmrig/pull/3740) RISC-V: added vectorized soft AES.
- [#3743](https://github.com/xmrig/xmrig/pull/3743) Linux: added support for transparent huge pages.
- Improved LibreSSL support.
- Improved compatibility for automatically enabling huge pages on Linux systems without NUMA support.

## SHA256SUMS
```
1673bfa501aeac47217f6a786da5e9da9f12c831c932e667316f8e49ad0318c1 *xmrig-6.25.0-focal-x64.tar.gz
6ce9151b33b0a2c625fc0e2371efc836f04fa214efaf287646a4c6356a7a860c *xmrig-6.25.0-freebsd-static-x64.tar.gz
8e6d7445ae9e79d430b9b491af601070f84728cce68db0c181b1dad4edae1f2e *xmrig-6.25.0-jammy-x64.tar.gz
4732cee4ffad920392fa35e432b77294f2cdf69fbb73491a7dff8b649336f888 *xmrig-6.25.0-linux-static-x64.tar.gz
a8ae95752b16084f3dd70d82db7030a7ad234a1c015a8aef9cdd3eb4877ac849 *xmrig-6.25.0-macos-arm64.tar.gz
4704aad2f9f6fd70d6a2f3cd6a7eaa04b0869daac0a35e40ee9fcd4e0c43fa8b *xmrig-6.25.0-macos-x64.tar.gz
55a2535031c3bafa5cd98028ea40791e9a68e36918929f1ec6e5146c65dab207 *xmrig-6.25.0-noble-x64.tar.gz
d2efa485c7959971203ebc1f93e962331831139272ad00ef18e4a55312a27e46 *xmrig-6.25.0-windows-arm64.zip
3d4b59dafc50900414aa93cdba7cd7f929137ee58e3e8285f7db1c05d1ac327c *xmrig-6.25.0-windows-gcc-x64.zip
1ad8694c8b94a923be6056a58c896f872c5bbfa3b8c26f3f31d601615f3fdc90 *xmrig-6.25.0-windows-x64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmlKlM0ACgkQRGpTY4vp
RAl2Vwf9GxUDl/qz8BBCB8PeOk1Qmv6ga7ZCBWj/7JehIJ+a8cOoNSu3hNMt+l8u
ZmzvfqdoKd2utrt91Sxi+uQHuEBhKO2SzqHOngdnJE/pmmi3JXKn7rgVKL4EWmSd
1maD6QevDrE7iGAhQv4bYdXSb8A4ivGuVIaKEKYZMNhmmPT2bxXM3L7cGjHyL42I
chmbaHGvpiNq3ZHYEM7yiud8I6NYyEhaj1hnEgtV6Lw4jxrCOUdkwZDDZXDwTGaB
PtKbBd8LtlH7gz+M3R68iR16kZYF4pGEChb59SVIviz3i5QCNijvOyPcGK+mCcLh
cSg7wN6SAcJCfEa9Lvz5Q8V7RF5GFQ==
=Cv9k
-----END PGP SIGNATURE-----
```