---
title: v6.8.2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.8.2
author: xmrig
tag_name: v6.8.2
published_at: '2021-02-12T12:51:43+00:00'
---

# Version: v6.8.2

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.8.2
- [#2080](https://github.com/xmrig/xmrig/pull/2080) Fixed compile error in Termux.
- [#2089](https://github.com/xmrig/xmrig/pull/2089) Optimized CryptoNight-Heavy for Zen3, 7-8% speedup.

## SHA256SUMS
```
38c869c91f5fe06f997977ffbb6df220828463055c42a5ef9519b99f2953131d *xmrig-6.8.2-bionic-x64.tar.gz
64fb7321781c1b3809f92b5095176c9de959dec948f616b0efdb2c5d5e099851 *xmrig-6.8.2-focal-x64.tar.gz
af17de4b6a479d271d2a76a01344769eebd41f404854f5a78d3be9fdef164cf7 *xmrig-6.8.2-freebsd-static-x64.tar.gz
3f28dbe972e60fff3818e0049434c04439150eec76dbdbde7642908eb1e895d3 *xmrig-6.8.2-linux-static-x64.tar.gz
34493f89e1394c76e8f610469aca8cde3f137aec4f57dfe2bd9f134bd167a162 *xmrig-6.8.2-linux-x64.tar.gz
16320598005c287e64b880785d9512900991246a669e900a1e13d0f653eadd02 *xmrig-6.8.2-macos-arm64.tar.gz
48df3e816c9afff41b1001b23d81ec7fba94158f7227aab236ebe8c9476f78c3 *xmrig-6.8.2-macos-x64.tar.gz
becc260c081325c4d548e7c6db36a6bc9bb5df2d34fd526bcf6a072e651d4562 *xmrig-6.8.2-gcc-win64.zip
462c28b66be220953e4775b8f560d1e4a18674087b8c8dbbaa4f8a792c152d72 *xmrig-6.8.2-msvc-cuda10_2-win64.zip
7a9517faf46b4603f4a063c57146563e07c52549323d99b37dd2b9709685ecf5 *xmrig-6.8.2-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmAmeJQACgkQRGpTY4vp
RAkHQwgAsSokhkldepIkTxHwh5mJkrC/aUN+t4hfCSpOe8tmCYq7TLW28FiUoESh
2oaBd9DW2oJXtkKFLjZJa39yAopO/WFq/sOp9W87DXYioG9mf9n8ovqzHX1w6EA7
lRH4Fpz4cY2gGPNLPhmSuQdYrhKPsVZzAIOR92kCW32sLN1F1z+IQ6FKW3WiVnYn
87Fbk4Zx1ffSVJJiiG9hhB10/f4KPUCXRQNcAfu4WvOIuIDv9S7Sk1Y0OsV5hFds
rmPIHH3qBj6+n9cSl3b7FjA5KxrazjOyoRmLbGGHCOFq9gwmTDMrk2flQdQTnnoR
U7UzRTLDjjQ3Y+NtIO7MGJ4eF6tQCA==
=AXLt
-----END PGP SIGNATURE-----
```