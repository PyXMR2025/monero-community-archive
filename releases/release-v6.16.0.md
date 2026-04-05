---
title: v6.16.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.16.0
author: xmrig
tag_name: v6.16.0
published_at: '2021-11-26T12:38:40+00:00'
---

# Version: v6.16.0

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.16.0
- [#2712](https://github.com/xmrig/xmrig/pull/2712) **GhostRider algorithm (Raptoreum) support**: read the [RELEASE NOTES](src/crypto/ghostrider/README.md) for quick start guide and performance comparisons.
- [#2682](https://github.com/xmrig/xmrig/pull/2682) Fixed: use cn-heavy optimization only for Vermeer CPUs.
- [#2684](https://github.com/xmrig/xmrig/pull/2684) MSR mod: fix for error 183.

## SHA256SUMS
```
7fce4f27d1b71b38b2245537e8a232276cc0efddbf37d8466c55d17e2939237d *xmrig-6.16.0-bionic-x64.tar.gz
18434beed1a9571315e6d05da586825353cb5854de10aedf692b10fd670b23ed *xmrig-6.16.0-focal-x64.tar.gz
3f30aa662f524b1dd50f3e3905fe0f629c255fc4183072d1a6fa9bad76ad2005 *xmrig-6.16.0-freebsd-static-x64.tar.gz
911d483a80ddc343873d55af9311d97342a1b7eaaec4d47196995d45a416a18d *xmrig-6.16.0-linux-static-x64.tar.gz
54021b711d193d0489e0d55e89c23ffdc10748d7a54ec79201a00dce3de4dbbe *xmrig-6.16.0-linux-x64.tar.gz
5e73f8851e43738ce4ae548e251d9b66f2e86a83df6ee364193ba6cc3ac03487 *xmrig-6.16.0-macos-arm64.tar.gz
8a2ca31c58ac4b759640952fd3cfea955ea82e0ebaa50815561166df8069b595 *xmrig-6.16.0-macos-x64.tar.gz
e5bf29dbfb4c0c64fed55bd41c5ede4e513822e0250b21b3a3bd51e2ac299acf *xmrig-6.16.0-gcc-win64.zip
cea9281aab2808583b1731a86093e3117d190b1caebbec0eabe5c53037a9f78f *xmrig-6.16.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmGg1DsACgkQRGpTY4vp
RAkvDAgAtx3HkmmllXKwvyGUAV/3BGV3O4VM7+KWxpRAy0N9Zt7GNMZOTgyq3+fH
1VQK1mHmy4T/UI+7aqvS1dFThWSgJiFsEYeUtY+gjUur4yHWdww1HPQgU+8CkEsD
hkL77yG3BWkV/1tidJ5hQmZLyiG3fg5PbD4Hf/n4GQ7odnDYyvyNE2ArHweWZxD+
TfHGpnmcq5yvBCKeOzNCEiKcsVGwMYutIOpJflBJnpcDY3dc7LvJJyN1t3gqk1bf
ZVumgpV+39r1lT8Q3iIjVp+0DCihJBnfiYSdaWmtsIDNfwqNAeVlhVkE0y2yPNIM
P2E7e4aOOUtxom0PQcyp84BEMJiVtw==
=Ld9i
-----END PGP SIGNATURE-----
```