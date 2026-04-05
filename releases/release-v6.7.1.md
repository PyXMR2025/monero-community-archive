---
title: v6.7.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.7.1
author: xmrig
tag_name: v6.7.1
published_at: '2021-01-11T09:43:27+00:00'
---

# Version: v6.7.1

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.7.1
- [#1995](https://github.com/xmrig/xmrig/issues/1995) Fixed log initialization.
- [#1998](https://github.com/xmrig/xmrig/pull/1998) Added hashrate in the benchmark finished message.
- [#2009](https://github.com/xmrig/xmrig/pull/2009) AstroBWT OpenCL fixes.
- [#2028](https://github.com/xmrig/xmrig/pull/2028) RandomX x86 JIT: removed redundant `CFROUND`.

## SHA256SUMS
```
3e9cca28e4ff8c53eac9d8ccaf837bf015011a8a8087fb0cc90bcbccbdc6a072 *xmrig-6.7.1-bionic-x64.tar.gz
5bd0829604343eb283ac920bd60c326035ee69f58ee312e587f12058b889af38 *xmrig-6.7.1-focal-x64.tar.gz
f236d6904a41a4658a153b6fc43f8600be5428712bd0c1a1d2fdaa2a98026f51 *xmrig-6.7.1-freebsd-static-x64.tar.gz
96578f6bea774b84aba6f0e58394ce3dc8c1f8d1dae02640f3fc9bc230c64474 *xmrig-6.7.1-linux-static-x64.tar.gz
593cd74eeb4d6efd4f9bec146a0066efbc364e932385283cae52d2c31459b848 *xmrig-6.7.1-linux-x64.tar.gz
ded6f02c612baec038b15f01b941f1679fbe587d3e98e46bfe4dd8d57aa6d122 *xmrig-6.7.1-macos-arm64.tar.gz
ca49904775ef3c0e93582394610b1fe78e54cd7d83972226d9cee664a8eccd63 *xmrig-6.7.1-macos-x64.tar.gz
645117a9598802e7b545a3de82afda2fd07ce18cffc0fa88d20eae80ebbca1b5 *xmrig-6.7.1-gcc-win64.zip
4cec03ee16be7bbec5b9ecbdfd4f781eebda1b104cb4059aaa2cce535f4cf0db *xmrig-6.7.1-msvc-cuda10_2-win64.zip
b23c7967426c1e042435e6ed1a20431e6516c20739704405528a5dfd69bd04a5 *xmrig-6.7.1-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl/8G8gACgkQRGpTY4vp
RAkleQf/bEgloA9zbfpefqWdS36aJogDhur4EOhFMTPPYeLxI0jzyezZ4foSSg/x
DURKWOGe8UD7do0IQKPi7fuV80Xo90cFGN/Hbj5Xk+mPtkMqTtTpF8k6gjCjALrD
tZmPvZFLH2BJ2Pc0DJdXyVcszynQL92cxRxc8nCH6GBy/k5oMZcIgAX+VI2+KgdC
7CZmBVmQlokV2hmqhVb8wg6DpFbOOSxhwF0K6ZvBHAnYLKLIxg/qHrPexBONY+H8
rJTil0vysZ05GiSwz6DHdA6E2LVLpXdPPD7vOgjImD1CwauxyTGXzOOSjTHP/d3w
nq0F8xDUXCRAHg+gJpWvDSt25JIr8g==
=883x
-----END PGP SIGNATURE-----
```