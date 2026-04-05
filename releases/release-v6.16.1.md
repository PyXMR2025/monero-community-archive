---
title: v6.16.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.16.1
author: xmrig
tag_name: v6.16.1
published_at: '2021-11-29T14:15:50+00:00'
---

# Version: v6.16.1

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- VAES optimizations not supported by `xmrig-6.16.1-linux-x64.tar.gz` due old compiler, please use `xmrig-6.16.1-linux-static-x64.tar.gz` instead. :warning:
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.16.1
- [#2729](https://github.com/xmrig/xmrig/pull/2729) GhostRider fixes:
  - Added average hashrate display
  - Fixed the number of threads shown at startup
  - Fixed `--threads` or `-t` command line option (but `--cpu-max-threads-hint` is recommended to use)
- [#2738](https://github.com/xmrig/xmrig/pull/2738) GhostRider fixes:
  - Fixed "difficulty is not a number" error when diff is high on some pools
  - Fixed GhostRider compilation when WITH_KAWPOW=OFF
- [#2740](https://github.com/xmrig/xmrig/pull/2740) Added VAES support for Cryptonight variants **+4% speedup on Zen3**
  - VAES instructions are available on Intel Ice Lake/AMD Zen3 and newer CPUs.
  - +4% speedup on Ryzen 5 5600X.

## SHA256SUMS
```
de1577f7ca9ca2aa90b4528a5658d6f01df8195430b5b415805bf718a85a24b6 *xmrig-6.16.1-bionic-x64.tar.gz
f3d09354e71bb920ad43b028319ef5c2d46f4ffe4e5faccd1617815c7625a821 *xmrig-6.16.1-focal-x64.tar.gz
daac99d74857ed4bc6dde8dbe621a81d019cfd4b83d3b1dfbd82fd5eb42e5104 *xmrig-6.16.1-freebsd-static-x64.tar.gz
f637a3d39d0b01fe359fe51b1ed0af130c869a86b13bbc69b8a7b4553eac261c *xmrig-6.16.1-linux-static-x64.tar.gz
438ba0c4eb927dcaf5a35893a5ad74c5c416d1d51cf33fcc1716b341a9d5a469 *xmrig-6.16.1-linux-x64.tar.gz
31b0344b81a0d6c73e86d87221d41d5947a481860bf5a0185e0c74644fe8a304 *xmrig-6.16.1-macos-arm64.tar.gz
a4c06a437fc4e5d20d03dfa0be364ab16239d0386ee11b236f9d85dc65d6b232 *xmrig-6.16.1-macos-x64.tar.gz
f6929eb39474444792a2062c75aaa4c06c6e09ea4b7ae949064c7dd93447f409 *xmrig-6.16.1-gcc-win64.zip
4ba1de92c6fd6959a0a30091784d04b3eaabb44245009b92bcd8076579957ba4 *xmrig-6.16.1-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmGk3l0ACgkQRGpTY4vp
RAnbFwf7BVFCNP/UYAOUVaZiLVIF7Vp4KFOOaFoaeMfuWTBn/W1oCb3+vRdS9X3L
CU32rofXovUrTCrVy/U8sPOrfjaImxNFiyUiM4Dt7N8zVers5e6sRSR0K1QAiO+Y
wQlZ4kPj0BlGNjZEqsrQJd3fBLMcQv4/4dGGnxU/FxCgybyAH/bTFPpvomRfeIv1
Raw+R5NOvkOUDjE7Z5n7bIneiYhYi92onZAQ33b9mk1mO7vzXbG2gRcL352Yn23V
4ELJlXBrwUnyzIrp2Tk/Wfyb+ypWJ+hmymu2Ovc0nbiVEfSMtORywIuWuWsjIv+p
5+b8CoWumfi+I+e+4UE9SEMOVYR+hA==
=WFru
-----END PGP SIGNATURE-----
```