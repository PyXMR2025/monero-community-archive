---
title: v6.4.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.4.0
author: xmrig
tag_name: v6.4.0
published_at: '2020-10-18T21:31:13+00:00'
---

# Version: v6.4.0

# Release Notes
## Notes
- **[KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915) :new:**
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.4.0
- [#1862](https://github.com/xmrig/xmrig/pull/1862) **RandomX: removed `rx/loki` algorithm.**
- [#1890](https://github.com/xmrig/xmrig/pull/1890) **Added `argon2/chukwav2` algorithm.**
- [#1895](https://github.com/xmrig/xmrig/pull/1895) [#1897](https://github.com/xmrig/xmrig/pull/1897) **Added [benchmark and stress test](https://github.com/xmrig/xmrig/blob/dev/doc/BENCHMARK.md).**
- [#1864](https://github.com/xmrig/xmrig/pull/1864) RandomX: improved software AES performance.
- [#1870](https://github.com/xmrig/xmrig/pull/1870) RandomX: fixed unexpected resume due to disconnect during dataset init.
- [#1872](https://github.com/xmrig/xmrig/pull/1872) RandomX: fixed `randomx_create_vm` call.
- [#1875](https://github.com/xmrig/xmrig/pull/1875) RandomX: fixed crash on x86.
- [#1876](https://github.com/xmrig/xmrig/pull/1876) RandomX: added `huge-pages-jit` config parameter.
- [#1881](https://github.com/xmrig/xmrig/pull/1881) Fixed possible race condition in hashrate counting code.
- [#1882](https://github.com/xmrig/xmrig/pull/1882) [#1886](https://github.com/xmrig/xmrig/pull/1886) [#1887](https://github.com/xmrig/xmrig/pull/1887) [#1893](https://github.com/xmrig/xmrig/pull/1893) General code improvements.
- [#1885](https://github.com/xmrig/xmrig/pull/1885) Added more precise hashrate calculation.
- [#1889](https://github.com/xmrig/xmrig/pull/1889) Fixed libuv performance issue on Linux.

## SHA256SUMS
```
d710f6305da414a2e697b4742ca8afdb8bacbd5c0827a668e014adbdae3860cf *xmrig-6.4.0-bionic-x64.tar.gz
724275f4b06a6dcb192425e4169a83d18d5149df210853bfcf08452983440ab1 *xmrig-6.4.0-focal-x64.tar.gz
164daa479c89bf0cbb36b0f819b615116f17b7fac82ff8021d521ec8267c469d *xmrig-6.4.0-freebsd-static-x64.tar.gz
4c0eb350c7aabd72020ca9874a5b0a65792d8bbf29a2e9365f92f6abe02f1d03 *xmrig-6.4.0-linux-static-x64.tar.gz
2dfe328387cc24e9c68e7e1f219f78df9a53fe0ade67266a2947cc4e45f3d346 *xmrig-6.4.0-linux-x64.tar.gz
169a72ec929ffefdbcf4a0de9d0364d8240e0a42b207f75a68bd6463263762d0 *xmrig-6.4.0-macos-x64.tar.gz
c12bbc7e3dbe27af675c3be3ccf989ce531a6c88b654d9ff8713caa26d2f3a1e *xmrig-6.4.0-gcc-win64.zip
bc8084ab0260ef08fbe7cd4c58efabb9200c981dc7b7be3d2c52dc3ad8aaaeb0 *xmrig-6.4.0-msvc-cuda10_2-win64.zip
fca96347ae588ef90252fd21b8c5c1eeb39fc4610e9575427e0b79a7c47a5c2f *xmrig-6.4.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl+MstwACgkQRGpTY4vp
RAlV1wgAuclZ1Fac08ra8GgNRmv7XO2egRkX+hMzVqGN9mJ+mn04YkyA1GL+WwUD
rG+WQmVQDEHMTwH3Y1NeYVsEKpZxYWZmMp6IWQlrhY2VkJkBj+e1wKZQzQUtC1Iq
q0rPR6cXsYn/l6BS+VKEDP+QxjwuHgOZe6rX8wDYovpj+4BTThzLvjsoCqnVY0Qz
Oh7hBgeNn417KqMdVMwN1yfTT2jxXbpfdTl39DKlRjBNVmWZDnwOzfxlPTbv1TLt
MTa5JccfoFyuarJZDZP5wlKHhI4LW1eO7fR+UdQkxhOYGftwExpMxA0gClAwbXEw
BgaHrIzprm/qwYbj/9bz6lR9dHgNeg==
=nWP5
-----END PGP SIGNATURE-----
```