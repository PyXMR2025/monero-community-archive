---
title: v5.11.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.11.1
author: xmrig
tag_name: v5.11.1
published_at: '2020-04-23T06:19:46+00:00'
---

# Version: v5.11.1

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.11.1
- [#1652](https://github.com/xmrig/xmrig/pull/1652) Up to 1% RandomX perfomance improvement on recent AMD CPUs.
- [#1306](https://github.com/xmrig/xmrig/issues/1306) Fixed possible double connection to a pool.
- [#1654](https://github.com/xmrig/xmrig/issues/1654) Fixed build with LibreSSL.

## SHA256SUMS
```
9fa2c7e94d333654b360d4b3c3d81b939a2c913e9d70e1525fa4499696c93879 *xmrig-5.11.1-xenial-x64.tar.gz
63ba3309048c2bf0b8c8022417876a7dbb3945bbc09f93bd82cfc3d5edb829b5 *xmrig-5.11.1-gcc-win64.zip
55612155abad338bfd94259f83adda9a128113893ae0a5d5c4e41fbb680d9e04 *xmrig-5.11.1-msvc-cuda10_1-win64.zip
cfea1eb1c63364d1d4ef13891da67eb96979ac255cd5576965afbdebd2a75091 *xmrig-5.11.1-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl6hMNcACgkQRGpTY4vp
RAnWuAf8CXBXuy9XZbtH+y8+OqRPzR/CWMn4as7dc+VvTuwwQ126aeIB1OmHNHal
PqV2LKmGDLjAEH1aLlfd/ikVN/YbPBHTJtQTO+b32PNoEIHJAo5T67QWCE1rrrf/
4jrxhgjqK+80yOdSGGNKHKT0PBwaCQ1YMF5pmlNFdDETYo/sgdWBMogBjDjUBAOe
G+noS66PUdfF+TNGZUTE7OR2Kzc9jRE6ydNK+BkWkcgAcFSzNBTzgDAFLZwRLNSn
cRRkjbunwg/z6rpCWTg3xZWxY0vOHOmY8o4NI6wjNukefABgU2fpa/7HucQvOXRW
/Jh0SzRFtstSbophGT9jPHrldYtupQ==
=z+pC
-----END PGP SIGNATURE-----
```