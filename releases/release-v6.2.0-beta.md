---
title: v6.2.0-beta
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.2.0-beta
author: xmrig
tag_name: v6.2.0-beta
published_at: '2020-06-08T19:09:41+00:00'
---

# Version: v6.2.0-beta

# Release Notes
## Notes
- **[KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915) :new:**
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.2.0-beta
- [#1717](https://github.com/xmrig/xmrig/pull/1717) Added new algorithm `cn/ccx` for Conceal.
- [#1718](https://github.com/xmrig/xmrig/pull/1718) Fixed, linker on Linux was marking entire executable as having an executable stack.
- [#1720](https://github.com/xmrig/xmrig/pull/1720) Fixed broken CryptoNight algorithms family with gcc 10.1

## SHA256SUMS
```
91ffb54cfcb0b21ad623acd66be4a37c31717cff3c1aa8340cc4a6cf047e0df0 *xmrig-6.2.0-beta-msvc-cuda10_2-win64.7z
b387e7831648aa6a24d6c8eebbe7d351e98ef066118584230c4f2cf3b91c33ef *xmrig-6.2.0-beta-xenial-x64.tar.gz
32af0158b43089dd1f79ddf36ae94c6a4ecf56f2817e10f80df01f4a9a8a7632 *xmrig-6.2.0-beta-gcc-win64.zip
81063507be6e6017bef90baa618dc3e4724cc7c3feb6b692ef51c7551751cc51 *xmrig-6.2.0-beta-msvc-cuda10_2-win64.zip
2a4666391f70706d88398c6bdb2d5439b36dc5d2438eefc051d430d889a821fa *xmrig-6.2.0-beta-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl7ehuEACgkQRGpTY4vp
RAkL6ggAy0b44X5wMSb0x3EwlRtAwWrzUS5cKVIz6JVEcYbNbydIlChvs+f53Nz4
4ODHwGBYuHlvL5XjH+OdQnzx8E2/1lhphRjAzYsHMYVrExApgSC4dbTG91ay+8en
Rk1OxqC9UVY/KuKirePY7/AIM2L9oOEoESQW9QtVuVXE5F5hE9cBSHX1xGLt3/21
u9hxbpUj9maZ5YdkT1K+eWM2X7Yw/jHhDi1Y0pwtx0MfIFG3dXRCUKCrkuvAcJw6
9NU4VZPq0pAMHbzMtprRFi2TRA9l0gjBOFU7MqqUDhUktds5HimzK7Lte4GJQ5R/
D++ZtPY6uvAThSidcEloMBaECoZADg==
=8wgC
-----END PGP SIGNATURE-----
```