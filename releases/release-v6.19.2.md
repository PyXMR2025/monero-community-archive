---
title: v6.19.2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.19.2
author: xmrig
tag_name: v6.19.2
published_at: '2023-04-03T16:23:06+00:00'
---

# Version: v6.19.2

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- VAES optimizations not supported by `xmrig-6.19.2-linux-x64.tar.gz` due old compiler, please use `xmrig-6.19.2-linux-static-x64.tar.gz` instead. :warning:
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.19.2
- [#3230](https://github.com/xmrig/xmrig/pull/3230) Fixed parsing of `TX_EXTRA_MERGE_MINING_TAG`.
- [#3232](https://github.com/xmrig/xmrig/pull/3232) Added new `X-Hash-Difficulty` HTTP header.
- [#3240](https://github.com/xmrig/xmrig/pull/3240) Improved .cmd files when run by shortcuts on another drive.
- [#3241](https://github.com/xmrig/xmrig/pull/3241) Added view tag calculation (fixes Wownero solo mining issue).

## SHA256SUMS
```
bdc96b9dfc9bb3f8bc75dfff34ac6c90777ac6a50a617a9e7eb116b3ca2a7ae6 *xmrig-6.19.2-bionic-x64.tar.gz
b6c0ebf8af74adf1392be86ca68e8ade0f54d952f5c140e45b6ff76877004be6 *xmrig-6.19.2-focal-x64.tar.gz
84c458a10daa66fdb1dd89606c6ec01c928b638caa67274153c70699a74ecdc9 *xmrig-6.19.2-freebsd-static-x64.tar.gz
49d4592a26f5fec7e5381f6dedfff33a8d2c9d72ea5bf4ca9352000e78ebc069 *xmrig-6.19.2-linux-static-x64.tar.gz
cccfd056978d629958f74e5c701335bd7b9bbd92fddd0a6979cf423220bff242 *xmrig-6.19.2-linux-x64.tar.gz
861eee81618a6eac1ff916b15f9adacd3bb2df895c2290175b6b800a4d3361ce *xmrig-6.19.2-macos-arm64.tar.gz
c5a0ec9371887c8d669740e3026a4030753ed00df54abcc489593f0d13bf4405 *xmrig-6.19.2-macos-x64.tar.gz
74784e528285119f9db24f8da235a52db1d7819e5595dee3fb45850b719d6802 *xmrig-6.19.2-gcc-win64.zip
8e1da98e61660ab108d7475b0d2163687ec0a9df6b369bc682c6ea6de1524dbd *xmrig-6.19.2-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmQq+loACgkQRGpTY4vp
RAl9pQgAwoFJikD0sVaUuiAJNQcFIgSwDAIVEQ5GhqNCujr1/KeC3s065JR0pd+p
H97/Ne/HZTiDBeNET0gJ8rFPpcinxJ3RQuBNzkiFF8WXdUqLtSxKbfbfeophXAC9
U9s6Rjv543SqHWXNvl7oCQwWv1WsY+VTZPM3nZVj91TiWDXaqxvGvVTqOaJRmuEC
8QVDgWgy5vQhnG+ijhLmNVwDPLRjtNqCIXLsg+j0ZAm/Mdj5JImJsrP5E5AGg9nd
1KA/HF5AxaYHyvizZBSAUbxf9JEvekANDplH+HnJB6tH/EmnxxKJr/Og2g+vbHCf
18i/k2Wl0/zPDRFdSCRY3e96hsUMiA==
=B/Zy
-----END PGP SIGNATURE-----
```