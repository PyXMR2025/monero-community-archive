---
title: v5.10.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.10.0
author: xmrig
tag_name: v5.10.0
published_at: '2020-03-22T23:19:09+00:00'
---

# Version: v5.10.0

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.10.0
- [#1602](https://github.com/xmrig/xmrig/pull/1602) Added AMD GPUs support for AstroBWT algorithm.
- [#1590](https://github.com/xmrig/xmrig/pull/1590) MSR mod automatically deactivated after switching from RandomX algorithms.
- [#1592](https://github.com/xmrig/xmrig/pull/1592) Added AVX2 optimized code for AstroBWT algorithm.
  - Added new config option `astrobwt-avx2` in `cpu` object and command line option `--astrobwt-avx2`.
- [#1596](https://github.com/xmrig/xmrig/issues/1596) Major TLS (Transport Layer Security) subsystem update.
  - Added new TLS options, please check [xmrig-proxy documentation](https://xmrig.com/docs/proxy/tls) for details.
- `cn/gpu` algorithm now disabled by default and will be removed in next major (v6.x.x) release, no ETA for it right now.
- Added command line option `--data-dir`.

## SHA256SUMS
```
38732737e839d782abb4a8b5f7b6d93991fbbf7507edeb8c6f6bd1f400d8f078 *xmrig-5.10.0-xenial-x64.tar.gz
295938c0b4af8887459206c5212a1ee8afd95c4d555b4d068bae5bbfa032b5fc *xmrig-5.10.0-gcc-win64.zip
b8100ca2263d8c55226a424f84dcc15c62456880ac963577ccb7f381cb51c6ea *xmrig-5.10.0-msvc-cuda10_1-win64.zip
5eb87869bf7fbec451673010196c2be3a534a757b7c01aecc2e8da3c9805a3c5 *xmrig-5.10.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl537e4ACgkQRGpTY4vp
RAkUlAf/afrdyvhvhx+K/sXbuwK1FFP5+j4AahSr0ZLRDy6pWuQCtNDQ2D/4PDsd
/xecV63DTLgy+0jjuWymb+rUQakd383cYb1pmnB+XvQSiGHcZQBGUTuEQ2zMy7Q7
7unUU6muxTe1cRTdFGNA6jXncwQWQS+M7y18Sr8xJoH9KqvohlxWNjzWy5SbOJn7
C+eT+bZsZUrD8TRd22u01Wdx7wRtmVSbF18mUNJ+QyJRA5PTPjpMjHsFrBrFgAMY
xZRrb2EyVauZxI1m0ClsTJW4+7x0ocNtkMK09xLMiBsm3OEDoiGHryCK9wKS97RM
gBQ3EdS0sLtkj5RltnVyW6qaKajahw==
=TbNa
-----END PGP SIGNATURE-----
```