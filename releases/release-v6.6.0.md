---
title: v6.6.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.6.0
author: xmrig
tag_name: v6.6.0
published_at: '2020-11-24T02:46:03+00:00'
---

# Version: v6.6.0

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.6.0
- Online benchmark protocol upgraded to v2, validation not compatible with previous versions.
  - Single thread benchmark now is cheat-resistant, not possible speedup it with multiple threads.
  - RandomX dataset is now always initialized with static seed, to prevent time cheat by report slow dataset initialization.
  - Zero delay online submission, to make time validation much more precise and strict.
  - DNS cache for online benchmark to prevent unexpected delays.

## SHA256SUMS
```
0b75b763d191064d56e15cd64710a2a046dbd36c50fe72b5ced5e279843308af *xmrig-6.6.0-bionic-x64.tar.gz
14007bceee9f5284789a1be9b856414223557729468043ed578dbf9db6fe28ce *xmrig-6.6.0-focal-x64.tar.gz
75e88c3110a978a6f086fe249243539534b9b71b34ea86042e8cc5bce0b0c355 *xmrig-6.6.0-freebsd-static-x64.tar.gz
381b4c8b7b25855ec3a4884f8042113ff76e39551151e08ed4c56782ccce4ab0 *xmrig-6.6.0-linux-static-x64.tar.gz
c2112a2a82e4bfcaff9f5aa4e7276801fbe6796ec1d7d6adb796256272f3ad67 *xmrig-6.6.0-linux-x64.tar.gz
4e81dc47785682131b7dd860a230007214b21f9decaef8be21c72b0e0794595f *xmrig-6.6.0-macos-x64.tar.gz
0eec301097e0667c02eb7d10bd24e457908539442f15a4934571328a6396bf3b *xmrig-6.6.0-gcc-win64.zip
295484886dd8747304c9faaad196ccc5692e46342d70b037db98cb19390efa65 *xmrig-6.6.0-msvc-cuda10_2-win64.zip
0097f3e4e1c922a24cd87e4b8267d519c9f9fa13c2d9734a5b5e03aa3a2e92e1 *xmrig-6.6.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl+8cukACgkQRGpTY4vp
RAmQRAf+PsiCtSKGCi/74yOLUbxEpCKdxq6raqbumVJLqlnktya+V3GDVIYEDsk9
T0zC1RSeyRFUOLlNOydronARkKhc94FxAQfoca2XJNw2x4IrJZ54jwA7Hr5j6PuZ
Jf+I4tYJ81ij8aG7MrIwGlA9dm63lrvTUNk3lu86wvmQ/0TvWxDlR5p03Zk3UkLl
WLg/338bT/7SdWzQMMJwxcmGZVEIKuZmvT1NBmzZYDyeAka3m3V3/QNPSUHcuh6B
dvBL2vjGT4jPlOrwAQxcLAxqd7zHU2zL+28IWDRQstznfAPZD8YU42rBWvIn1hvP
01uklZaq5V3HJKi1lugUn45L0lDGVQ==
=1Jsf
-----END PGP SIGNATURE-----
```