---
title: v6.22.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.22.1
author: xmrig
tag_name: v6.22.1
published_at: '2024-10-23T06:26:24+00:00'
---

# Version: v6.22.1

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on X https://x.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.22.1
- [#3531](https://github.com/xmrig/xmrig/pull/3531) Always reset nonce on RandomX dataset change.
- [#3534](https://github.com/xmrig/xmrig/pull/3534) Fixed threads auto-config on Zen5.
- [#3535](https://github.com/xmrig/xmrig/pull/3535) RandomX: tweaks for Zen5.
- [#3539](https://github.com/xmrig/xmrig/pull/3539) Added Zen5 to `randomx_boost.sh`.
- [#3540](https://github.com/xmrig/xmrig/pull/3540) Detect AMD engineering samples in `randomx_boost.sh`.

## SHA256SUMS
```
79fab61f3b6e94653cc5b7381ae24d2b9358c35365b7cf47e4eabf966aed2eb1 *xmrig-6.22.1-focal-x64.tar.gz
17573e51fbbe5c8012baa90127158655aa62418a027474375ba3e27bbe40cacf *xmrig-6.22.1-freebsd-static-x64.tar.gz
ae421bf7663a34df042ca2e6e5357d3cdaeb40aa2928078b2a5511a16cc3f6f9 *xmrig-6.22.1-jammy-x64.tar.gz
df7d249d768b5bf71b6b4399cd1061713c74c5c1fbc98c5ed9dcb4e4323b4b96 *xmrig-6.22.1-linux-static-x64.tar.gz
e204e795f6215e5d1102c8a252e0fbd4d8db4a36940cded7f9138923928a17ec *xmrig-6.22.1-macos-arm64.tar.gz
3e56ce1ff0c5f2bfae7bb2981880ef36f8ad0a2718823d17fca3afd5ccb5dd36 *xmrig-6.22.1-macos-x64.tar.gz
76684cf3f2f71d5d3632bad597ef82069dfe6b8702650f2a6e7f44c56d489f91 *xmrig-6.22.1-noble-x64.tar.gz
7084964c61c889fac649d695427f214d8b99fe8b719d2e9b3fbf6e72f1d2f470 *xmrig-6.22.1-gcc-win64.zip
1d8060ce86b65e0eb489ead196660ba8064f711beca612551d40e94a46d8e628 *xmrig-6.22.1-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmcYlOYACgkQRGpTY4vp
RAlNRQf9EzULa525ntth3do7besx+ieJfzpqs3jjatOVtPqvozS8C089gvfUFgIE
R4Bjv7kPe+iJKt+dziiVDxO9QzTRKV3Dxd+4aVvgI4RWVkwwzmfhXHnq931RmnWK
XHqqtV2hDkkmWqQOhLOWj5ZU61tOWRsU22EWZVn0VeGAPhRIr9EvBJCliRsBbso7
vLXveRKh3v8XD1tgX2UkL1z49DJsS8hydXBUjFPvn5WcbQ1/HSAMBbzBR6nCCbZ8
DNQqbEeZebCixMoML1IBBza2MhkwhiHZQ3Va81yiT2WH0p1tlAc5AaQ92mj3Evnr
WAMBew+q8DYvrzQUExsj1jzpwyM5Eg==
=xzXR
-----END PGP SIGNATURE-----
```