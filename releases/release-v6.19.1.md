---
title: v6.19.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.19.1
author: xmrig
tag_name: v6.19.1
published_at: '2023-03-23T13:29:55+00:00'
---

# Version: v6.19.1

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- VAES optimizations not supported by `xmrig-6.19.1-linux-x64.tar.gz` due old compiler, please use `xmrig-6.19.1-linux-static-x64.tar.gz` instead. :warning:
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.19.1
- Resolved deprecated methods warnings with OpenSSL 3.0.
- [#3213](https://github.com/xmrig/xmrig/pull/3213) Fixed build with 32-bit clang 15.
- [#3218](https://github.com/xmrig/xmrig/pull/3218) Fixed: `--randomx-wrmsr=-1` worked only on Intel.
- [#3228](https://github.com/xmrig/xmrig/pull/3228) Fixed build with gcc 13.

## SHA256SUMS
```
8ce330e614010ae30a2bf02b5055f98954f7ddbd05a1ba2a8ec4e7b62c27e82f *xmrig-6.19.1-bionic-x64.tar.gz
ef777c65249b183c28834cfbe4db2051be2d1e56f9c0f8087149a43afe678741 *xmrig-6.19.1-focal-x64.tar.gz
b7de51348bda79e0adea1fdc272a4746953e60bcb8111b79c90a2d94d7c55c02 *xmrig-6.19.1-freebsd-static-x64.tar.gz
297c25be307dec795a7d63bf7c220b81573e5096ebadc50faab6132f64cd2d71 *xmrig-6.19.1-linux-static-x64.tar.gz
32fcd2cc2e71abd5f10f3062281a1b3146d72f9678d3f75690cdbaf7ae641ca2 *xmrig-6.19.1-linux-x64.tar.gz
083cfcc0c09925c35861426b262a247d20d3478a1752461f6b39d750e1c32df2 *xmrig-6.19.1-macos-arm64.tar.gz
39bf18efa88beb2d07a12135528e4fa59bf7d961784a67c2ad72d8f1e9c90a9b *xmrig-6.19.1-macos-x64.tar.gz
2cdb1a42cd816f84cd00c36416e9746bd3bacc343062d742208b60fba6852f1f *xmrig-6.19.1-gcc-win64.zip
f90bdaf53b4ed92e27f28a34e22707208f896946b746d657549bff308212861b *xmrig-6.19.1-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmQcUmAACgkQRGpTY4vp
RAlQowf/Z2c1a/bmywRL3SVofrd5FQ4rzgm+NkeTUROd4UPW8ohyzDscJPHqVaGd
+69Wl7PvXAu7rIDN+YBLoZ0i7/bgTy3CrytKcTiK4MkxAR124KuENns/gkmKYmOY
Sv0tvyXPDeQZldIrmGOaEvB1sEW5Yl2gNqWEF5DO8S8gV8S2Qza3FfU30ApuG1rr
RwfcE/KYMU70mR5jm+gaR/i4QKRp1oVB+c4McuN39skBzRNLMz0yMOd9YKn9WWpT
5MhQjPnsziGqXALg46kEPqX1ZjVsRom76kfGjHx08J57CmwhbGx/oC45wZMhfg9o
L2NwyW6LIQKPmGvGhT82SMu+8Act0w==
=Rnm/
-----END PGP SIGNATURE-----
```