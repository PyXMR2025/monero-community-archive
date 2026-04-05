---
title: v6.0.0-beta
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.0.0-beta
author: xmrig
tag_name: v6.0.0-beta
published_at: '2020-06-03T16:46:46+00:00'
---

# Version: v6.0.0-beta

# Release Notes
## Notes
- **[KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915) :new:**
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.0.0-beta
- [#1694](https://github.com/xmrig/xmrig/pull/1694) Added support for KawPow algorithm (Ravencoin) on AMD/NVIDIA.
- Removed previously deprecated `cn/gpu` algorithm.
- Default donation level reduced to 1% but you still can increase it if you like.

## SHA256SUMS
```
ed176b4ed6bfd90a42986c5a0d2fdf98c6d83774de4560733502f331812eb5ce *xmrig-6.0.0-beta-msvc-cuda10_1-win64.7z
044f9059c9d07a101fb79d5c97e06b66bd9ae57e74a62cbcd01e4eff81c5a5cf *xmrig-6.0.0-beta-xenial-x64.tar.gz
394b4bd58f4b0cd342a30974134bf765488b241d697a91fcbc41453082250baa *xmrig-6.0.0-beta-gcc-win64.zip
054c352e42a6e27938a6ee613db91d385509c67e118edbd8943e06858b787694 *xmrig-6.0.0-beta-msvc-cuda10_1-win64.zip
d51dfb7fbf20ca0781d7838a7c7575ba143e6308e2201fd8f7c305a5879c637e *xmrig-6.0.0-beta-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl7X0UcACgkQRGpTY4vp
RAk0dgf9EZsBIxhkcVpyqamUBhKWEYStepBgWbIXCbZ3t3282Ye+KVc6r09bir1Q
HKJRpGaFmMdihIhHC6PtYWi6ce7XrcCjJfVxz/+TSE+V6zau32w6QcayVzCxQKJm
A9QBpxA4wLTkzdGjAtuHTWfsPW5OkPDVplttaN8CP92Xj+QUgokAMxbjfHmXXcyD
lyL9yxwsFYHjnZv6I5ye4cbJxDxuucL4P6olyL5L9qtTKXAwFucmANCfZRCGWSBX
qmWhFV+UuZszbuj1DE8KZSowgcL8URm+jqegXXnoC4BgkagCMKMwei+fce+dcNam
KskWerZRlglWjZi5B2QG6bfZEcVl5A==
=ftjt
-----END PGP SIGNATURE-----
```