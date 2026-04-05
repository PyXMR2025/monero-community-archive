---
title: v5.5.2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.5.2
author: xmrig
tag_name: v5.5.2
published_at: '2020-02-02T07:29:41+00:00'
---

# Version: v5.5.2

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.5.2
- [#1500](https://github.com/xmrig/xmrig/pull/1500) Removed unnecessary code from RandomX JIT compiler.
- [#1502](https://github.com/xmrig/xmrig/pull/1502) Optimizations for AMD Bulldozer.
- [#1508](https://github.com/xmrig/xmrig/pull/1508) Added support for BMI2 instructions.
- [#1510](https://github.com/xmrig/xmrig/pull/1510) Optimized `CFROUND` instruction for RandomX.
- [#1520](https://github.com/xmrig/xmrig/pull/1520) Fixed thread affinity.

## SHA256SUMS
```
eb9a223421c87a5a030a1848d2078ad60d4f5ef8847fa4761306875f6bd46ef9 *xmrig-5.5.2-xenial-x64.tar.gz
2225c4402042aa94a25e4d803c824c6dd4bacbe7c8e48ff2613b0fc974e56d37 *xmrig-5.5.2-gcc-win64.zip
a420a5f49ab05e9d9ff64aaffa93caa093d61f02260f8f37b61d21fe8f31cafd *xmrig-5.5.2-msvc-cuda10_1-win64.zip
3d8c5749077229bd2a1c2544588394a5b2d447b80034e55d47f4a220e67e3d24 *xmrig-5.5.2-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl42eDwACgkQRGpTY4vp
RAkXpgf+NThWBE3459lBZ9Vn8zHYIUJYPFJWQoY4Fg+E7GAMkBPAQxBxMQ4+hB5h
yijzWLxx8cyrQ9vlKHMLMNa9i7BGaaEcGxwoma75P2nQ2j2OBgEvHMAOJb7zDuSg
a84ulz1tmj6F6KrPj5aaukkdPuSTcivTyTSgePRc7JYsSy5pHayUbtcgMEDZ/sfV
f4FncTIJhgGUW2A8MeHXxMKzKNWw9tP9cWgDc/zT+DukE81eCYt0ekJZhFYcrrY3
FGVWhl+BOuaWJx8egEJcFgi0v7Dcv4pnCdTRWo5u4W3H0hvmgT8ypY9BPGB+QQYe
21OyMMm3y7hgXyoccg2zgV6HxP2bLg==
=Zfxs
-----END PGP SIGNATURE-----
```