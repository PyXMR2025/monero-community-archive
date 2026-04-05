---
title: v6.21.2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.21.2
author: xmrig
tag_name: v6.21.2
published_at: '2024-03-23T06:53:55+00:00'
---

# Version: v6.21.2

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned for updates, and follow me on X https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.21.2
- The dependencies of all prebuilt releases have been updated. Support for old Ubuntu releases has been dropped.
- [#2800](https://github.com/xmrig/xmrig/issues/2800) Fixed donation with GhostRider algorithm for builds without KawPow algorithm.
- [#3436](https://github.com/xmrig/xmrig/pull/3436) Fixed, the file log writer was not thread-safe.
- [#3450](https://github.com/xmrig/xmrig/pull/3450) Fixed RandomX crash when compiled with fortify_source.

## SHA256SUMS
```
c9101b0bffe94e14660ce76983536aba4986148f65552970d05283e644c923db *xmrig-6.21.2-focal-x64.tar.gz
c14410e8bce94936f4dcef0a5272e0f23f79bf84064eadfd4b6dd9aec7dfe1f3 *xmrig-6.21.2-freebsd-static-x64.tar.gz
3e13d84f3fd6fc72bc76cd67a4e2f635ac8905eb987dbae442c91838d1ee015f *xmrig-6.21.2-jammy-x64.tar.gz
e7321ed45e4b1f58e9b2ab46b08becabe8ea4b1dce39ca621a500bd04977da1e *xmrig-6.21.2-linux-static-x64.tar.gz
ac71a8d0b7aafa19d283a11aa23b8a7a0bc51f3f5711c080c07e3e3a9dd1b3c3 *xmrig-6.21.2-macos-arm64.tar.gz
4f94e4587d5214e49a36c4fa6818ae0c345b172829116e315ab63b124b4192d6 *xmrig-6.21.2-macos-x64.tar.gz
61150c72c3cdc121a2bcd0e13aed45ea7a1059e21563888af1fe2710f7883db6 *xmrig-6.21.2-noble-x64.tar.gz
a55fd7f703fe907d0409dfa81a5b66e7a6259143f50897a96b52d7b8bfde9cd6 *xmrig-6.21.2-gcc-win64.zip
ac442c192a538aceb2802adb3c72d4e7fe781f84f8b21adf0f9d87f0314bae98 *xmrig-6.21.2-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmX+ew4ACgkQRGpTY4vp
RAlG4gf/RqBsKR9+QcXbyeQkPgzrlq/bt6nTgPIZxgTlkmAkkJsoBPu0twgY8qGR
+MEAFkcYsLAhwnczLTwE7vfzQWm9qPDn7WhncWzSnc5IoDUONszgPR6ukFz7VmIL
Ac4w4K0Mv2SHVSMpN1ZQYW20ErrShPZw1z8RZPFWqgSSWKcoPgL/i2ig+OoZZeu3
2avbbtpMtV/8ZPVo9EuUxs7NuMlTHEKHM1uKl/EhhYbKvCzNpGMgAYBO8pOMeg2I
iOZnGUEXhPiI2Z7zJz0IawqfbQ+cPbukEpGn2Gs1y96/nqYtYgh9iLvfehziYeqo
2xOfgY7R7OVe8V01DWXhKNP5kSFueg==
=kHVU
-----END PGP SIGNATURE-----
```