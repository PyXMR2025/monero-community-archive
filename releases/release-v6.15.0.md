---
title: v6.15.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.15.0
author: xmrig
tag_name: v6.15.0
published_at: '2021-08-31T08:29:01+00:00'
---

# Version: v6.15.0

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.15.0
- [#2548](https://github.com/xmrig/xmrig/pull/2548) Added automatic coin detection for daemon mining.
- [#2563](https://github.com/xmrig/xmrig/pull/2563) Added new algorithm RandomX Graft (`rx/graft`).
- [#2565](https://github.com/xmrig/xmrig/pull/2565) AstroBWT: added AVX2 Salsa20 implementation.
- Added support for new CUDA plugin API (previous API still supported).

## SHA256SUMS
```
c4181288118f484eefd65c260e6337c80c4d3f5746b259c4f57820d878b3de80 *xmrig-6.15.0-bionic-x64.tar.gz
5362aff4860d670898a6a892465a71e907025f61fffe9b48ed394d130d23b0fa *xmrig-6.15.0-focal-x64.tar.gz
26a9a6aaea6362362c80fd3f1bc4e999e117bad30a9e3a988db940d5383ee7a7 *xmrig-6.15.0-freebsd-static-x64.tar.gz
607c3d7071ea2914f5bfc3c76f71cab425ca1a2611ac69fd12dccf057a62ad5b *xmrig-6.15.0-linux-static-x64.tar.gz
126ff0caaa90adb114b0928db32a70b7938ef7a5a9689c352a6d434bfd0486f5 *xmrig-6.15.0-linux-x64.tar.gz
0167140edc1cf8d2e7867ef896b2829b515c813ddd80e8f58633407e87e3851e *xmrig-6.15.0-macos-arm64.tar.gz
f6248c6a0f5859bc40cf08416442b27bf770c60444f936d156789d74894f1479 *xmrig-6.15.0-macos-x64.tar.gz
159730c8aaba9d79634475a669cc31854bd7b9b62b1ec33b21a0493074e0ab9f *xmrig-6.15.0-gcc-win64.zip
298ef5f7b29b08fe590ba3f8375d89c9da5a3eb3812983f18fe7e29348f2fe6b *xmrig-6.15.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmEt4/QACgkQRGpTY4vp
RAmVDggA3qi6Acu/FYd1HdloQ84CQlEUvp7DgFLWVM1nSlGlHfe55u/AvWdiWoH0
ukpnzdlfKM6GZYFyXbPlsBaalsoVOhKJh9dkyZacHlS1gSd9yi5oBUHkJM93Cn2P
4ioOQgGtNgOspggvvzQ9Cs39VpDWHjVD6MLnq8yHEJrOx2M7uceEG/L2PKXZDOfC
ZbMD9FhcMjis3+xf82mYYHp+0svtbDbbVr/GXMDeie3H3vNDamTKotaJf1A5bNQi
CEep/Y3e4lyaxTSgg1odz8FaKUqmH/tTXifIU8lenAeSK6buWAHv5eiZ3+3MbIUE
Njl3eUpxer9eWkmGx9v/CJz1JM3ILQ==
=PRbh
-----END PGP SIGNATURE-----
```