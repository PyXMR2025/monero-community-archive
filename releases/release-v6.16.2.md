---
title: v6.16.2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.16.2
author: xmrig
tag_name: v6.16.2
published_at: '2021-12-02T15:03:20+00:00'
---

# Version: v6.16.2

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- VAES optimizations not supported by `xmrig-6.16.2-linux-x64.tar.gz` due old compiler, please use `xmrig-6.16.2-linux-static-x64.tar.gz` instead. :warning:
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.16.2
- [#2751](https://github.com/xmrig/xmrig/pull/2751) Fixed crash on CPUs supporting VAES and running GCC-compiled xmrig.
- [#2761](https://github.com/xmrig/xmrig/pull/2761) Fixed broken auto-tuning in GCC Windows build.
- [#2771](https://github.com/xmrig/xmrig/issues/2771) Fixed environment variables support for GhostRider and KawPow. 
- [#2769](https://github.com/xmrig/xmrig/pull/2769) Performance fixes:
  - Fixed several performance bottlenecks introduced in v6.16.1.
  - Fixed overall GCC-compiled build performance, it's the same speed as MSVC build now.
  - **Linux builds are up to 10% faster now compared to v6.16.0 GCC build.**
  - **Windows builds are up to 5% faster now compared to v6.16.0 MSVC build.**

## SHA256SUMS
```
2a24a7e7dadda1fa2a50b34ce1983ea1a36140e7659b8f62efb93d0b832ed0d1 *xmrig-6.16.2-bionic-x64.tar.gz
a94013acaeab84beb04dd510099e7fa40a5da82788ab73049a51f5b927a8ecca *xmrig-6.16.2-focal-x64.tar.gz
4ff682c950176026911b5a57301e1e771d9be79db994c89dc34a6667de678773 *xmrig-6.16.2-freebsd-static-x64.tar.gz
8e6d16e0f48ab916d52f3e064b3152b74742d45825e720884d8c11d8f12c7c5a *xmrig-6.16.2-linux-static-x64.tar.gz
5474cfa13ba16bb38b57d85e4f6fd4a07d1d904f59dd8caf7529a82455b262b7 *xmrig-6.16.2-linux-x64.tar.gz
1e0669e77e8788493a7ddbe2c54146d184810038f08b9df3158db83555125183 *xmrig-6.16.2-macos-arm64.tar.gz
a2d546e5ad9689b95a1f179978d790b8a9edd033bbc6e22453d4d7f60f33c6db *xmrig-6.16.2-macos-x64.tar.gz
9a9b5cce347113e7d5fef8988c1cdcd6d36820bc2cec8b2db57983d6f474ef09 *xmrig-6.16.2-gcc-win64.zip
e1af6aa7fc50beca52136e477294c440548432fc659fa164d22e67bf36d5ce18 *xmrig-6.16.2-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmGo30EACgkQRGpTY4vp
RAmc6Qf+IXz/HDUuD/0TGmVjw/SNx0pG4T/CJQ9d8QYVzBcQURmb7V1dTZsapMj4
WHFUrTJ8J+Nexsf4OJguHYDCjpSmmk+dX1db1IgM/0z4D+9RCDKhodcIVwMY5laN
bFp5ZoFYysQnxzusTcrkMy6HNauKlZWFwfoRUEncPXA0umrezjoxnTZZlNBuUFuV
WCmWY9pGCmxxDYNJlHIzoYtigKOjOE7LnaXeQ77skDZjti0gZt7IMiJQpKoiLt13
Y1dEnGsjdTki+ff1hV8lpzwfRmJ7eSDWfyMG7zplgjCT+hVIy84mY+cQyKgCCEy5
dZJPCZYw2ZTARGEQB6TowLuyXsTf0Q==
=hT+l
-----END PGP SIGNATURE-----
```