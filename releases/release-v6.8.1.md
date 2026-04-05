---
title: v6.8.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.8.1
author: xmrig
tag_name: v6.8.1
published_at: '2021-02-03T00:58:04+00:00'
---

# Version: v6.8.1

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.8.1
- [#2064](https://github.com/xmrig/xmrig/pull/2064) Added documentation for config.json CPU options.
- [#2066](https://github.com/xmrig/xmrig/issues/2066) Fixed AMD GPUs health data readings on Linux.
- [#2067](https://github.com/xmrig/xmrig/pull/2067) Fixed compilation error when RandomX and Argon2 are disabled.
- [#2076](https://github.com/xmrig/xmrig/pull/2076) Added support for flexible huge page sizes on Linux.
- [#2077](https://github.com/xmrig/xmrig/pull/2077) Fixed `illegal instruction` crash on ARM.

## SHA256SUMS
```
da74367329a8cfbcd85a02c8928e94694dc0f64c59def929c62152606ed99afe *xmrig-6.8.1-bionic-x64.tar.gz
1013e174b0c6531cad1c0bce414aec5a8e53e766a5374f3c380b5ff545abf318 *xmrig-6.8.1-focal-x64.tar.gz
c879e0a715e7206cf57edabd8d425b1547b8a6f7168d9f40f06937a0963afe93 *xmrig-6.8.1-freebsd-static-x64.tar.gz
825c60dd1bb32cd6b7e6686f425c461532093b1e9f6ca662c1ea9b07ec7e470b *xmrig-6.8.1-linux-static-x64.tar.gz
187088d2785cbcb19e2998f8aa3a88c7c43f69117359f7155e3dcde8e004fa7d *xmrig-6.8.1-linux-x64.tar.gz
f42dbea05f40f1af3e75373b05e5021259dd78306f13fadaa70ceeb16e107900 *xmrig-6.8.1-macos-arm64.tar.gz
6d2241e7f2b9d0b6f42f1f2d18293dc3c132750f2137da716358a3883796d240 *xmrig-6.8.1-macos-x64.tar.gz
a4836f5b0c54a40d479967efca7387d487b4394904667ee316e39cb124056f18 *xmrig-6.8.1-gcc-win64.zip
279f242e54ebd90da8dbeef1a1b4a3f78fa4fb033dabe2031e7e9d108ea8d4be *xmrig-6.8.1-msvc-cuda10_2-win64.zip
03c21c80852f088d5afe28de2838a49b63f45e217b6b7087417771851a197293 *xmrig-6.8.1-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmAZ850ACgkQRGpTY4vp
RAkCkAf/Y8arP3kmGHI4/3vQILmQA8k6dj9oxNCzjX9jDsNxP89v6zzZvl/tQEVa
fVy7NEWUEMPEvVUu1IiR5AsEu2T51lXsFpqC/shV+qR71gB5sMXi2Gpjxztoczji
5ozSYCtntve3/nHxoCCsTmfKzuaKqEzvz/V77yiUog+Ied2nvzZhlXqtUGINC7xi
74axiYSxjtyPB/IL29IHVtiOvH5gmqP7fsTtBl2qmhYfImcwMOchBN+6poRKpwEL
rFqMQyBDlKq9dGW26Tsc5ge2J8aMoaXv6DkSo6coPivLJ8Kzg6lxtEweOrAPlBWb
GDYqZeZ0vkUYT6/SsyRjwIYsTAJ2tg==
=GnaJ
-----END PGP SIGNATURE-----
```