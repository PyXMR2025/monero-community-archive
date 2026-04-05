---
title: v6.3.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.3.1
author: xmrig
tag_name: v6.3.1
published_at: '2020-07-31T07:08:34+00:00'
---

# Version: v6.3.1

# Release Notes
## Notes
- **[KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915) :new:**
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.3.1
- [#1786](https://github.com/xmrig/xmrig/pull/1786) Added `pause-on-battery` option, supported on Windows and Linux.
- Added command line options `--randomx-cache-qos` and `--argon2-impl`.

## SHA256SUMS
```
f801adf9520f57dcf57c06504869f80b149af25a3bd697c34c57572817f5bd0f *xmrig-6.3.1-msvc-cuda10_2-win64.7z
0a8fa17e619a978bd59a2d5133c1820d74931435eddbb4d4e4e3d99f8ccff685 *xmrig-6.3.1-xenial-x64.tar.gz
9a8981f4dddde01dfe26b78254d6d950bf4b03b4a491368ec048f60adc08c082 *xmrig-6.3.1-gcc-win64.zip
92b72ff8571b7d0c9b0c90b3ae19c6e7e9a9d171201da4f255f6e6d5962a3232 *xmrig-6.3.1-msvc-cuda10_2-win64.zip
e93540a4e2bd033ee4bc1394d4a2af77e701bb14724983893849a34dfce3ee21 *xmrig-6.3.1-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl8jwYkACgkQRGpTY4vp
RAk5FwgAoa5uTVKhJ+Xx5csZHFyWFoKuuzQvPX1Zn6Nir0UTtTBzQ7hKw76YIXoE
0RB7tzF6y/y6XQwI3yrM7rgsJ8YFlZpcu21v1io7FeglT0Oe2vgmYxk95G9Spbvs
Jom53IAKryaKQBiqCpu2Hq3Z7PpxLnhoH60uUk4PpCz4JYQ4HskHAX206dTwM26r
hU853yUfXa49EojJvV0JD3wh8H2V/pTBrUGgbKWi6p2FazZ3BuRZ/TBOFiDuz2yU
v2XQCt8+g8tGNZo00jHy+uTxIbzTdV1tk/DyKaq1tze5CnfAfRA3HStEfMHRAAk5
RgHj+VqC6T46tu3eHn4Zb9g4oQUjeg==
=Ej9c
-----END PGP SIGNATURE-----
```