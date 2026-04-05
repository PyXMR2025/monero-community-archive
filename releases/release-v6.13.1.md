---
title: v6.13.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.13.1
author: xmrig
tag_name: v6.13.1
published_at: '2021-07-03T08:56:21+00:00'
---

# Version: v6.13.1

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.13.1
- [#2468](https://github.com/xmrig/xmrig/pull/2468) Fixed regression in previous version: don't send miner signature during regular mining.

## v6.13.0
- [#2445](https://github.com/xmrig/xmrig/pull/2445) Added support for solo mining with miner signatures for the upcoming Wownero fork.

## SHA256SUMS
```
09315a793b1d516109a012fcf4f2822acf6e072e5d0e5418e2888d01859c90f6 *xmrig-6.13.1-bionic-x64.tar.gz
3759f692f90b99628f25613742e3fbd5151441e32406bf6dc338871e3f73649d *xmrig-6.13.1-focal-x64.tar.gz
e9a9d90a24a525353d75308f2016df2b0ba9eb07f91b5bade36b52ef295ffd88 *xmrig-6.13.1-freebsd-static-x64.tar.gz
be225e89211a3667e758a133bf75270daf1bb000672b5b4ba7b6337166e1c6f7 *xmrig-6.13.1-linux-static-x64.tar.gz
f28da17dec2b5949fd2b113be3a3746e1bbb6e1cc591631d0150084b00e0d3ad *xmrig-6.13.1-linux-x64.tar.gz
5a1e5fa66a25796d8b03a40c96ed9d2eb968f7ba3604321f29940e9363fae3e8 *xmrig-6.13.1-macos-arm64.tar.gz
c4a008a5ef6c00d44802b9ee973863bb634cc580a792067f1f04337ccbb57a5c *xmrig-6.13.1-macos-x64.tar.gz
7097dc8a4bbef4341d6e112e6c5906c9c849c246deba429735da02493e15e54f *xmrig-6.13.1-gcc-win64.zip
79bb16aa326a401e9cd1716d0ea1d6e1fdfdac945a7b4f4f4480be3a1e77cdd3 *xmrig-6.13.1-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmDgJU4ACgkQRGpTY4vp
RAl+AAf+MK9sj9D+hHBIUAmlhF8EdSHTXZubf9QH4fXhjCadaducGqZVVNufgWx4
LOyD7ril/u4h76x8yyMBq6dOCXx6rK+HNu1gRmQX9qeceVH8rTAzOBwSmq56yMyH
zDRC9j3b5tpgZAlhREgvU5EwFGPoqJ7C8XQNahTn/HFkkZRfkO2J+1A4Z5+8r11R
KILMIXBVQlW8CyKQtt6rnh4qILiKvcfDemoS04cP1bwA+hq+odBgwkmZPHMg3d/j
BozbYZPiHIcv2JzL9EKhADF452YELXyBfet/MX0hyd1gaUH9j/RE3uN399XgCcK/
wMuXTeDQTTr6M2f+KNudzd/dpkgMxg==
=IMZq
-----END PGP SIGNATURE-----
```