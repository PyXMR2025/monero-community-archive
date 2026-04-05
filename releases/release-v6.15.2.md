---
title: v6.15.2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.15.2
author: xmrig
tag_name: v6.15.2
published_at: '2021-10-05T17:31:34+00:00'
---

# Version: v6.15.2

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.15.2
- [#2606](https://github.com/xmrig/xmrig/pull/2606) Fixed: AstroBWT auto-config ignored `max-threads-hint`.
- Fixed possible crash on Windows (regression in v6.15.1).

## SHA256SUMS
```
26377757c0f4ec623284c545c4e82b6c89cdc2576a9aac73f540ec9e15c4fd60 *xmrig-6.15.2-bionic-x64.tar.gz
029ac9411d8f22305f9e0637f0fc270f1f873962c0a1fcee9f6bb8ce586920e5 *xmrig-6.15.2-focal-x64.tar.gz
c049d86ef7a70b9b405c8415b95a8c797d2b703455c9916c0cbb36db52d11cba *xmrig-6.15.2-freebsd-static-x64.tar.gz
96b24035af7fd5b72a9728075b0dde95d0c704b09d168e15837ff2f86932a357 *xmrig-6.15.2-linux-static-x64.tar.gz
52b8a63e074be5d53445238379b590ecb9177274e45794d1ad4adf6a6bdc971e *xmrig-6.15.2-linux-x64.tar.gz
30fcdec4b8b8ad6a9bd015a4c8b5f60ca40ed2fd9e7a47a1eebd74ad639c6b0c *xmrig-6.15.2-macos-arm64.tar.gz
21606d4f99e5b36839ca185606ae11d0a783b3e4ddfc1257a7cc5f7e0779fcab *xmrig-6.15.2-macos-x64.tar.gz
78bc17bb8b7d2c59076240b48299a11c17d0d024d8db2405826b1ecb9a79dbb4 *xmrig-6.15.2-gcc-win64.zip
c6493b04ce06f618e6ade2b9a7c14e507562aebdc6bf7ca7f804615bf8b5d50a *xmrig-6.15.2-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmFcihkACgkQRGpTY4vp
RAmdIAgAtvKuuvUFEphOQotcagml2Ch1OM2WjG+PoTgUdrNLRZRrHv792Bm43QUW
aYfAa77+OIEQEqruiS4GznBzjTBLxW19rogLaqYe7SK81fBzZVtMdNRd64m4TMwz
xnKdHH8CIAIjkU8exBpyRztTcoCbEBXtbsosrfUZBibSEIWXKW6LoQwKTeHvUth2
4tQprKooJN6FYCNat1taCP2YSd4bb7J2HHWaTuBChq/ZKsF6AvK8livfZLIGWWRP
K3mB/d97szvy/yDxg25B3uKv5+gjLo+XT5uS21Y9YK64OEKR7Hk65clAIVUHwoTG
0n4TJvqXgCoXM0iDIw5JidOYVmhb3g==
=aKXQ
-----END PGP SIGNATURE-----
```