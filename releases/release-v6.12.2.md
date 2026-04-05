---
title: v6.12.2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.12.2
author: xmrig
tag_name: v6.12.2
published_at: '2021-05-31T06:32:11+00:00'
---

# Version: v6.12.2

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.12.2
- [#2280](https://github.com/xmrig/xmrig/issues/2280) GPU backends are now disabled in benchmark mode.
- [#2322](https://github.com/xmrig/xmrig/pull/2322) Improved MSR compatibility with recent Linux kernels and updated `randomx_boost.sh`.
- [#2340](https://github.com/xmrig/xmrig/pull/2340) Fixed AES detection on FreeBSD on ARM.
- [#2341](https://github.com/xmrig/xmrig/pull/2341) `sse2neon` updated to the latest version.
- [#2351](https://github.com/xmrig/xmrig/issues/2351) Fixed help output for `--cpu-priority` and `--cpu-affinity` option.
- [#2375](https://github.com/xmrig/xmrig/pull/2375) Fixed macOS CUDA backend default loader name.
- [#2378](https://github.com/xmrig/xmrig/pull/2378) Fixed broken light mode mining on x86.
- [#2379](https://github.com/xmrig/xmrig/pull/2379) Fixed CL code for KawPow where it assumes everything is AMD.
- [#2386](https://github.com/xmrig/xmrig/pull/2386) RandomX: enabled `IMUL_RCP` optimization for light mode mining.
- [#2393](https://github.com/xmrig/xmrig/pull/2393) RandomX: added BMI2 version for scratchpad prefetch.
- [#2395](https://github.com/xmrig/xmrig/pull/2395) RandomX: rewrote dataset read code.
- [#2398](https://github.com/xmrig/xmrig/pull/2398) RandomX: optimized ARMv8 dataset read.
- Added `argon2/ninja` alias for `argon2/wrkz` algorithm.

## SHA256SUMS
```
e125dc6c936f31b492ef3af56eb64d3df2867ccac80536b8f1549045ce27e73c *xmrig-6.12.2-bionic-x64.tar.gz
7d149468f36de8ddb859d4aabd2f4efc529f295035ffec568bcd1e8aba10e93a *xmrig-6.12.2-focal-x64.tar.gz
4746dc5af22785aa215fbe53f9ed338a274cf330b3010d3be3a9489c29ff5242 *xmrig-6.12.2-freebsd-static-x64.tar.gz
8eb8d0d54d893b1eaeeb20c0d55189a04a41732ebac4d0dba8c958c8ac5ec08a *xmrig-6.12.2-linux-static-x64.tar.gz
b5a10747af28e8c1363f2a56137e55d7af6ce64b2f2bca943eb91792eb655b5f *xmrig-6.12.2-linux-x64.tar.gz
790d09999e2e547c44882f9ea31072b087d83f13e85f1ac6e0f4f5ede6a85262 *xmrig-6.12.2-macos-arm64.tar.gz
132b1ca2a0dd4a6e85691615fc596fce2e1f14dcb2f4b044bed243fc4613ebc5 *xmrig-6.12.2-macos-x64.tar.gz
b3dfbd80ab446e1e44fc508a0fab0bd7ad4bf03668d3ed65a82e3075e94b46e5 *xmrig-6.12.2-gcc-win64.zip
c082043a1fdfc35e92361c7053b2e310f07b3e0904d3ecedd19441389dfdc374 *xmrig-6.12.2-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmC0ghUACgkQRGpTY4vp
RAngfwgAvOtXv8YValfYO94v3dLdWWoNG/oI0CtojK3cHs0B21p+K+tNEMmKCw+e
etzzN0A5lrlOFA8CmtdGzWRbqlM6xll08NBKgfvyc1PnjWjjOfV0KNKkk/jAFCmd
Wp7FPEW+E7kzxMDHhr6vH0Vi+C6LV13bAbiXJGejj+n5FWP/VwO6an5n3VX+GiET
gx27yXm2Rt3++7S8ZSWtLhBbWVpc4ypksqhe2aRcVuNgpg60+Y+Jp5419t5jehLH
16za4sz4/c90bO/jmB/eaejuvoNqHN210B9LlcJrfTGx8tbsnGyMyTopCu/Y+QUW
fKmt2WBC2rtgLw8TatDV9AVE3FbYAw==
=fH7s
-----END PGP SIGNATURE-----
```