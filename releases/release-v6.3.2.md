---
title: v6.3.2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.3.2
author: xmrig
tag_name: v6.3.2
published_at: '2020-08-20T06:42:35+00:00'
---

# Version: v6.3.2

# Release Notes
## Notes
- **[KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915) :new:**
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.3.2
- [#1794](https://github.com/xmrig/xmrig/pull/1794) More robust 1 GB pages handling.
  - Don't allocate 1 GB per thread if 1 GB is the default huge page size.
  - Try to allocate scratchpad from dataset's 1 GB huge pages, if normal huge pages are not available.
  - Correctly initialize RandomX cache if 1 GB pages fail to allocate on a first NUMA node.
- [#1806](https://github.com/xmrig/xmrig/pull/1806) Fixed macOS battery detection.
- [#1809](https://github.com/xmrig/xmrig/issues/1809) Improved auto configuration on ARM CPUs.
  - Added retrieving ARM CPU names, based on lscpu code and database.

## SHA256SUMS
```
31354cbf619e77696bb752b9fc9a69df153537c2eb4e01e23ff472a7dad3c903 *xmrig-6.3.2-msvc-cuda10_2-win64.7z
c0a5af6f241efad1145f8a4a970db6446ad8065c08c87742026a336a3ed44053 *xmrig-6.3.2-xenial-x64.tar.gz
b8a270e985c6bbf0785be23a6d1d94d0d31e2d24075ee4dd1cb84a236cfb91f8 *xmrig-6.3.2-gcc-win64.zip
7fb7609e3d6d4303dc034f8126df57d1f090f5f7a1fed6837aa66d83ad145c4b *xmrig-6.3.2-msvc-cuda10_2-win64.zip
cd2393f2d8d77fbe358ef9a95c641558c562a1db9fad2411e3dbfcffeace6c09 *xmrig-6.3.2-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl8+Gg0ACgkQRGpTY4vp
RAnBuQgAoXcGLKYYrb9DHjM8nqyZdHubRoiRMu2WzxrAizWshkIg88ktepZl2R+4
UMs6S46enE3ZjFa4ibqLer+PvoLrkUDqbcHIqNEcGffeflKBVucCs8gJPmjYEoJw
1HCSQw3Qu5ZvhFGkneTKHJKH8jqH2rtlgNGF1MkgLK99c0o1iZzafCGQ7hRZjGMz
RKYBYkK9k7nC2Q8bGCwCNyzmjPJTJ8CAAh2EWe4os0JqJeM1qrmDiiBzXBIQ1HdH
Ze58xTYiHhtp48oPKmho57zjTECVAXmU3U8BlP5ZrXaW3McpdP6ndurMn84R1afA
mop6q3IsY4kG0ZEOqBhoNG7++AzTxw==
=ImnR
-----END PGP SIGNATURE-----
```