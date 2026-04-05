---
title: v6.14.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.14.0
author: xmrig
tag_name: v6.14.0
published_at: '2021-08-09T10:19:21+00:00'
---

# Version: v6.14.0

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.14.0
- [#2484](https://github.com/xmrig/xmrig/pull/2484) Added ZeroMQ support for solo mining.
- [#2476](https://github.com/xmrig/xmrig/issues/2476) Fixed crash in DMI memory reader.
- [#2492](https://github.com/xmrig/xmrig/issues/2492) Added missing `--huge-pages-jit` command line option.
- [#2512](https://github.com/xmrig/xmrig/pull/2512) Added show the number of transactions in pool job.

## SHA256SUMS
```
ddc2d233a3c53cb612c6c9327de7fe7f38aeeba3b8ce8e14f0fd8f42b01e3180 *xmrig-6.14.0-bionic-x64.tar.gz
18c4f3588ec6342e2e7e1cc42439a7246861c0368966336be07c4bda4f756207 *xmrig-6.14.0-focal-x64.tar.gz
d232b4b69de6463090b24464d8c11ee173c496120dcd1341232fa52b276f99f7 *xmrig-6.14.0-freebsd-static-x64.tar.gz
e84096d042f78610fc7b1a873aa203d9e89fee0666a3e115da311367cac941d1 *xmrig-6.14.0-linux-static-x64.tar.gz
f0272b96fed6ab74925944a1cb4b0f951dd1a6c956d073f62ce0eba28fbb0a43 *xmrig-6.14.0-linux-x64.tar.gz
7f6430ed1251b0fbde799263e15cb4821b1f63de23121db7c48a6b510fec33df *xmrig-6.14.0-macos-arm64.tar.gz
47a3e77573043e1ff114793887d677c2ec759e0c1654ed0e75ba093d457407f5 *xmrig-6.14.0-macos-x64.tar.gz
1faa98f3fb514e0592e2e5840a566fe084b4bc1741ea65ee6b637d0f913ae215 *xmrig-6.14.0-gcc-win64.zip
d3d91686e7b1d3a780c300d5da632a5c6c1a41d9b4792b0f0cc041e02b6ac675 *xmrig-6.14.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmEQ+nAACgkQRGpTY4vp
RAntbgf/XG8st5avkpgP0MUhQJACHqKH9+mWWAXDer9/w8cP0kI3JkD3O9YW5RHJ
n5t/K6QxWVoPUTW9zXpfftkxBeMJ+ApGOW+MV76IcTPg4Nd5vGTOqyZGKpE23yja
cinFEHwr9cIAd45VWyasXSxTyva9ZNmJFBrL7/8zGYLHMfM9EKbMmYFCo6bPwOgT
8SkRuXY3P9YGbrmHRMVgTnSanV/qn/ADe3A3G+QEVfQbd9KFKsNY1o4/Zsfzpa9/
49be5wfpDALHjA6VrOB2ztt+5tPfEqx7nuxkoV+XusGixTxE5LuejF1wWXU94tjd
ijXmm+WJhfp20VqQPy1kke1tjH+btw==
=Y87K
-----END PGP SIGNATURE-----
```