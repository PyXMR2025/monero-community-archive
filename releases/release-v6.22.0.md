---
title: v6.22.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.22.0
author: xmrig
tag_name: v6.22.0
published_at: '2024-08-11T18:42:33+00:00'
---

# Version: v6.22.0

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on X https://x.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.22.0
- [#2411](https://github.com/xmrig/xmrig/pull/2411) Added support for [Yada](https://yadacoin.io/) (`rx/yada` algorithm).
- [#3492](https://github.com/xmrig/xmrig/pull/3492) Fixed `--background` option on Unix systems.
- [#3518](https://github.com/xmrig/xmrig/pull/3518) Possible fix for corrupted API output in rare cases.
- [#3522](https://github.com/xmrig/xmrig/pull/3522) Removed `rx/keva` algorithm.
- [#3525](https://github.com/xmrig/xmrig/pull/3525) Added Zen5 detection.
- [#3528](https://github.com/xmrig/xmrig/pull/3528) Added `rx/yada` OpenCL support.

## SHA256SUMS
```
f69df25232d4ec437bb614d2b2a57309deb5be598adc65e89ebed2300c711586 *xmrig-6.22.0-focal-x64.tar.gz
23090c2deb2a3518dc181f656a1885cbc15524fef7cba7b7ed3a4ba38a02e181 *xmrig-6.22.0-freebsd-static-x64.tar.gz
2bc9c20980b36686f0a55da2e0d0209d3a7545a2eb545f29549d44ad4aabe8d9 *xmrig-6.22.0-jammy-x64.tar.gz
cb49ae0793b257fd95892cb5eb777b9fe0d61a4015c7926cb68a3d353ed6accd *xmrig-6.22.0-linux-static-x64.tar.gz
01fc3b9733bdd4dd1bab53b5a963b40292a292db3857ebd91b3f6078beffd286 *xmrig-6.22.0-macos-arm64.tar.gz
2ca9612975255c71925fbc976cb64d7b46355b9dd301b9084b4725a7f4513e43 *xmrig-6.22.0-macos-x64.tar.gz
0d2333e5169e5ddf527d9d1f307ccb1845c943ef0057f14e16723e8b5179c08a *xmrig-6.22.0-noble-x64.tar.gz
6a543eaa9cca4909099db2d0a277d2cb970feeba7630ce5310c92be1a4ab240c *xmrig-6.22.0-gcc-win64.zip
b980b17ef632506ad6747f813572058698e9da843f008c8d395c7f2afc31ebea *xmrig-6.22.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAma5A+wACgkQRGpTY4vp
RAmNMwgA13OTEyM2DVLovKTG5d+BoJPyMmJdV/1B7Y8nJzaegQjRzwroiox4HX2g
oqXUDjJgFukqulwaLond+PVGABWTML/C20MJwemvmy9vRzVuvC10zXhEtAWh/7JO
mLpNeNoKK5qx++wKi0BqPLxrBvXE1d4RNweDU5sP8cTQvpYh0Txako2ZIOMqvR7b
S65U7mKJUrja93+LuURuo/udbfZnP72DSyq6qQHi7TpKCk7OUSvdfgdvrvNNyUDQ
HAHahKr/z3QC49r2NgW+TJTLXuvTH0vo9KC0aFKGKDE4vZIg1/13gquh4FbFyCef
Fy3W/q0VR3bMo6x4P5BlvF+oVYNmTQ==
=/JbE
-----END PGP SIGNATURE-----
```