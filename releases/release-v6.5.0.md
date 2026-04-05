---
title: v6.5.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.5.0
author: xmrig
tag_name: v6.5.0
published_at: '2020-11-02T08:27:32+00:00'
---

# Version: v6.5.0

# Release Notes
## Notes
- **[Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.5.0
- **Added [online benchmark](https://xmrig.com/benchmark) mode for sharing results.**
  - Added new command line options: `--submit`,  `--verify=ID`,  `--seed=SEED`,  `--hash=HASH`.
- [#1912](https://github.com/xmrig/xmrig/pull/1912) Fixed MSR kernel module warning with new Linux kernels.
- [#1925](https://github.com/xmrig/xmrig/pull/1925) Add checking for config files in user home directory.
- Added vendor to ARM CPUs name and added `"arch"` field to API.
- Removed legacy CUDA plugin API.

## SHA256SUMS
```
6e58d598c9730cc26be43b3473ebef4a20c7935c6a962c7194fd28e47b06c338 *xmrig-6.5.0-bionic-x64.tar.gz
24b7e9beb0a19951cbbe181146bb795544ba2506f3a97cbf1dd20a22ffe3131d *xmrig-6.5.0-focal-x64.tar.gz
b60de58bc915aab119f3a6085354630d21123500d85897c519681d4c562d8593 *xmrig-6.5.0-freebsd-static-x64.tar.gz
f146c527c42e049f5ff1d906d9edab27b0e42bd5ba548b4aea34de821f3c2b2e *xmrig-6.5.0-linux-static-x64.tar.gz
0f4f2e22e0a240fe298816817f727e8ac0919a1e7db65d88c1ea3beb397ad1b7 *xmrig-6.5.0-linux-x64.tar.gz
e89b08c2b374f5ae2dbe927bd422cfb1a209ec4a245e7737303f6a6fc32cf350 *xmrig-6.5.0-macos-x64.tar.gz
83b331bc8efebb72e44c83cda0302754ab2ee4368bd4509f7b09726a312a45a0 *xmrig-6.5.0-gcc-win64.zip
b55a68f0c6e19138d92bc519354f12db7d411670da478622e9ac2ba25c6c40d8 *xmrig-6.5.0-msvc-cuda10_2-win64.zip
4816a80da1cfad581203cd38c0d07bf693ca05f02e7ea01b87aa3aadde27fa70 *xmrig-6.5.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl+fwXwACgkQRGpTY4vp
RAlNFwf/fGizmkQxeq/fH/ZEJsYdiNraMUmNeOqC3mP7j2sWnB8towyWgG0WC1gN
QDl/u5/zdEtbpSAqVTKJ2Qf49Q2VCTiZi+OziErkFTsDVVNR8zeVqVmbYCh5O7ES
HaNmM1dj7jnLPN01PjyEZfcG4fgjn6RBNoNSOCGRL7iNeVIiVHPfDoVOPmi+iobK
YUnT1Duj86vVuXlwb3mPia5NaLzq80oL/TyZQmbbNMO1BW5rXD4jFWjk6jYoee47
AUuDCfIJcWmWjbdhWmbgMsfwdQq4ANc0RFiDQBEy85s7f+sZhwr5oFIc2v+CrJO3
AjbfluAp1uuft0TA6EABKHuCaAwsFA==
=ACWL
-----END PGP SIGNATURE-----
```