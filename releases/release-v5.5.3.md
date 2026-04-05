---
title: v5.5.3
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.5.3
author: xmrig
tag_name: v5.5.3
published_at: '2020-02-02T17:02:48+00:00'
---

# Version: v5.5.3

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.5.3
- [#1529](https://github.com/xmrig/xmrig/pull/1529) Fixed crash on Bulldozer CPUs.

## v5.5.2
- [#1500](https://github.com/xmrig/xmrig/pull/1500) Removed unnecessary code from RandomX JIT compiler.
- [#1502](https://github.com/xmrig/xmrig/pull/1502) Optimizations for AMD Bulldozer.
- [#1508](https://github.com/xmrig/xmrig/pull/1508) Added support for BMI2 instructions.
- [#1510](https://github.com/xmrig/xmrig/pull/1510) Optimized `CFROUND` instruction for RandomX.
- [#1520](https://github.com/xmrig/xmrig/pull/1520) Fixed thread affinity.

## SHA256SUMS
```
739b107365cc18dbbabc4b312b39fe4675703f6a209ea8849576e2c0751650b8 *xmrig-5.5.3-xenial-x64.tar.gz
e9549ebe2ff59946e8d2462531e528459ead52ee4e311ffabec8ab892e7aa99c *xmrig-5.5.3-gcc-win64.zip
d388af7900f6b5fc18d0eff25bb7d173f66e5b20c7d77d2570f3484059d54afa *xmrig-5.5.3-msvc-cuda10_1-win64.zip
8261c67d4e4e5ca1759a16350b9f91b0f64a2266c5c3cb0086329bb2f1aba6c2 *xmrig-5.5.3-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl43AAIACgkQRGpTY4vp
RAlvqwf+KFnAkUkBYBxD5e9GghEPv9g5TmSTyqIcZvLXRr8Tqim4Uwc8TtDL6cBA
B3932tl1DRZRZRDPm0jmGETtd8UJzDrHe3s2sjK8nP0jSq3F+B+lG8BHE1IjKEIw
YKcu907u0WB6B+pdvzEGrygCrkMN2KD1CGZrGQJ81JKHbDrfqIoE0wwJcm9AV7vb
IFvOhw9WtqKyXkLxnYM3/F91wy2vkvpYWK16qGe/VnfnvJKnlNPBfzSVwTPlTBAf
Dv4xqWjAwyxOYXuwt9dPHp3D9TJoYPuWFxanV0TBR/mpREJ/pkN/O9Lyhb5wQdXn
Y6k5HHP+yTe7egmXUbINggBnb7UvFg==
=c7xx
-----END PGP SIGNATURE-----
```