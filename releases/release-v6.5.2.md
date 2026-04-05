---
title: v6.5.2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.5.2
author: xmrig
tag_name: v6.5.2
published_at: '2020-11-13T19:12:57+00:00'
---

# Version: v6.5.2

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.5.2
- [#1935](https://github.com/xmrig/xmrig/pull/1935) Separate MSR mod for Zen/Zen2 and Zen3.
- [#1937](https://github.com/xmrig/xmrig/issues/1937) Print path to existing WinRing0 service without verbose option.
- [#1939](https://github.com/xmrig/xmrig/pull/1939) Fixed build with gcc 4.8.
- [#1941](https://github.com/xmrig/xmrig/pull/1941) Added CPUID info to JSON report.
- [#1941](https://github.com/xmrig/xmrig/pull/1942) Fixed alignment modification in memory pool.
- [#1944](https://github.com/xmrig/xmrig/pull/1944) Updated `randomx_boost.sh` with new MSR mod.
- Added `250K` and `500K` offline benchmarks.

## SHA256SUMS
```
23f8e45095db37378e016f8bdf77b99cb0d0c3f0f464a0ffb719e1ea46158257 *xmrig-6.5.2-bionic-x64.tar.gz
1f34755d45544e0d7384070a32630d7e2eacbae71e5bd23e9625a30350f30ea5 *xmrig-6.5.2-focal-x64.tar.gz
179f04dbfa3458f1a723cadada94202300c8441b02ad001927c204c933bc2965 *xmrig-6.5.2-freebsd-static-x64.tar.gz
2a55378dce34fee6e7f5424d6cd55679cee3d2d1ab47ba5a4b1b65e7a6d28495 *xmrig-6.5.2-linux-static-x64.tar.gz
5050d102e03103f444ea70576abaceb79afbff05d4414c98b530c3c5bbb11769 *xmrig-6.5.2-linux-x64.tar.gz
1beec682c874f8f1dc3efb4061e6fb4d08b5fe7450ca6dde87faf2a5d5f3c4b2 *xmrig-6.5.2-macos-x64.tar.gz
e965cfc423ea464b622d5b4c4ecc0134490dcbb09b632804de2de08aedd80c64 *xmrig-6.5.2-gcc-win64.zip
32f229ba9dc15c6f800994c9b1c8b38399697a33327365ef4018d41f24e9f2ef *xmrig-6.5.2-msvc-cuda10_2-win64.zip
ccd0967158fd32b6dbb4a8d0c477f1cebd5ac5b7a959ef5214c88a5324395739 *xmrig-6.5.2-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl+u2JoACgkQRGpTY4vp
RAnCEAf+NOET1z2/rYsWU5pJDY2tnuxxm63Kmj4YibYoVw2K0SxY2NFdgGavTet6
Mt8fbdgqlb3wPIhlmqJrGG7k/amRFBIswWxXPEoFY8iKLBOjrEPS8ztvNDc3kJsP
BDeGn0SQAaCF/TdIzBS/kmYhz6W609GYkjyWVc2MUicp5VbH3/RMCcD9LvmJBI70
J3vDd7iZPF4adGI40K0x943/lrpWLTlCAZ+tzOWW+xltTdG2lyFoYVcuiQSsJ9Xl
1/EMg+cl6yUJChXHxjZpzlby89DyFxbTpf0GZzcZWI7XlvgFuQCBD3DMS0tGZraM
PSGTtjsug5mSe7v4IUzID6pCepdM7g==
=kDxK
-----END PGP SIGNATURE-----
```