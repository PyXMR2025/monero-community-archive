---
title: v6.12.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.12.0
author: xmrig
tag_name: v6.12.0
published_at: '2021-04-20T14:32:47+00:00'
---

# Version: v6.12.0

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.12.0
- [#2276](https://github.com/xmrig/xmrig/pull/2276) Added support for Uplexa (`cn/upx2` algorithm).
- [#2261](https://github.com/xmrig/xmrig/pull/2261) Show total hashrate if compiled without OpenCL.
- [#2289](https://github.com/xmrig/xmrig/pull/2289) RandomX: optimized `IMUL_RCP` instruction.
- Added support for `--user` command line option for online benchmark.


## SHA256SUMS
```
200fbc1e8d70c1a4e009dcff0b2ba5be691e63fb33074ee0a74730fde4b0a184 *xmrig-6.12.0-bionic-x64.tar.gz
3aaa436297ebf75b705f7eefb083b35ea9fa5ad2cf2a191bcf12f91a685106de *xmrig-6.12.0-focal-x64.tar.gz
6888fd699e3b2c2b22a46001a6aab244b10bf345bdf8c999328ca0a40e9a030f *xmrig-6.12.0-freebsd-static-x64.tar.gz
eb9257d141cdf3dc2d46c60fc4425ec4826105ec2c412d86cb3cf2df3a19edbc *xmrig-6.12.0-linux-static-x64.tar.gz
ec46ae1a3511a923ed0c74b4f0975726705b6b672672b61314deee8ef7b75341 *xmrig-6.12.0-linux-x64.tar.gz
bb6e5d8939c6d1bed90d62d1684b74892d1bd1d9b02d956bb530bff4a88158a9 *xmrig-6.12.0-macos-arm64.tar.gz
4ea11707dbc0a73c582270aad1a95386f6f343a249ee0524e301266f83a2bbdc *xmrig-6.12.0-macos-x64.tar.gz
b5fe47a4d93ebf085e4c8728426c776843044139efbb483cba73df2c4f37c3ea *xmrig-6.12.0-gcc-win64.zip
9fc1d1819761b8ef1909d1e05ffdf42ad17fa29cb4b97214e9abdb030347453b *xmrig-6.12.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmB+5OsACgkQRGpTY4vp
RAllDQgAoM0YUDACqB2gf69R5HkPGidGmNKQJrjFpUklcMXqnMZoBtsodwsTDuw/
ZuJ8mGOHwhLMEtpQfETHuNIinD1yE5V88jqVJJrOs0WhXkBgVQmuXPsdpMkx7i6p
nUHf5I5GYc7Qh+DJgHnm1IjtCcOFULNZ7D2XDIv5HMwey6kKyREXHtHp0ExwJ+H2
9iGNRfsl3hzuj2ZFaj3zSGFvRfyUTQtt4R2LzgkHh7/5b190o/CRwEJdMhME49Z8
Aw7Jzs2ieBxfj5y4D/rROfhN5WNdAZr224xaYSCMhQ9v0dXLdCYTqf281/cCajmf
NUV88RKx+9S3h84SUhjW58D++yny1A==
=anVH
-----END PGP SIGNATURE-----
```