---
title: v6.26.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.26.0
author: xmrig
tag_name: v6.26.0
published_at: '2026-03-28T13:34:12+00:00'
---

# Version: v6.26.0

# Release Notes
## Notes
- **GhostRider algorithm (Raptoreum) [RELEASE NOTES](https://github.com/xmrig/xmrig/blob/master/src/crypto/ghostrider/README.md)  :new:**
- [RandomX Benchmark](https://xmrig.com/benchmark)
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on X https://x.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.26.0
- [#3769](https://github.com/xmrig/xmrig/pull/3769), [#3772](https://github.com/xmrig/xmrig/pull/3772), [#3774](https://github.com/xmrig/xmrig/pull/3774), [#3775](https://github.com/xmrig/xmrig/pull/3775), [#3776](https://github.com/xmrig/xmrig/pull/3776), [#3782](https://github.com/xmrig/xmrig/pull/3782), [#3783](https://github.com/xmrig/xmrig/pull/3783) **Added support for RandomX v2.**
- [#3746](https://github.com/xmrig/xmrig/pull/3746) RISC-V: vectorized RandomX main loop.
- [#3748](https://github.com/xmrig/xmrig/pull/3748) RISC-V: auto-detect and use vector code for all RandomX AES functions.
- [#3749](https://github.com/xmrig/xmrig/pull/3749) RISC-V: detect and use hardware AES.
- [#3750](https://github.com/xmrig/xmrig/pull/3750) RISC-V: use vector hardware AES instead of scalar.
- [#3757](https://github.com/xmrig/xmrig/pull/3757) RISC-V: Fixed scratchpad prefetch, removed an unnecessary instruction.
- [#3758](https://github.com/xmrig/xmrig/pull/3758) RandomX: added VAES-512 support for Zen5.
- [#3759](https://github.com/xmrig/xmrig/pull/3759) RandomX: Optimized VAES code.
- [#3762](https://github.com/xmrig/xmrig/pull/3762) Fixed keepalive timer logic.
- [#3778](https://github.com/xmrig/xmrig/pull/3778) RandomX: ARM64 fixes.
- [#3784](https://github.com/xmrig/xmrig/pull/3784) Fixed OpenCL address-space mismatch in `keccak_f800_round`.
- [#3785](https://github.com/xmrig/xmrig/pull/3785) Don't reset nonce during donation rounds.

## SHA256SUMS
```
a49c08f780484d0a50e18065132228556c64e857bb6783ebf1da3eec0beceee6 *xmrig-6.26.0-focal-x64.tar.gz
f766ec3ead48a21f9d478c309086b2fc4bd675747d91436d8ccf86d8fc57b18c *xmrig-6.26.0-freebsd-static-x64.tar.gz
ca82fc8426187880dffa502363849af6258e65fdb675a9cc9984a2b843854087 *xmrig-6.26.0-jammy-x64.tar.gz
fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5 *xmrig-6.26.0-linux-static-x64.tar.gz
6ae4eb4216e99a201ae9a3d2c3a7c275207c5165cfc25da1f3d735d6c4829c18 *xmrig-6.26.0-macos-arm64.tar.gz
1da924b358c0089e361540c4a9e6f8b09538b29efeafa2379590e0f6db358ff4 *xmrig-6.26.0-macos-x64.tar.gz
18198537f741405f569db0e6ecdc11c01f514aa861843b49bfa1ef60fe2877e7 *xmrig-6.26.0-noble-x64.tar.gz
958952de131c392a4e1e9656a1d70c3916d09d5a1f5e3f8c67dc0e6f35dbd76a *xmrig-6.26.0-windows-arm64.zip
2de2ae3c2d01e6245e41101571cf7bb83e9236e8361213026308228d227b16fb *xmrig-6.26.0-windows-gcc-x64.zip
bba8097cb37d9b458a1cb1137876b27cde6740d17fe4ccbc086ba07d87d9e147 *xmrig-6.26.0-windows-x64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmnH1jkACgkQRGpTY4vp
RAlokgf/QwXQe9DfrQdEtHCH8N821QEvol/iVMyeajsFRAVvw2Qxrfxcpvq50WqD
1DFt5yT4WZzuRC+SM/soXA6Xiq/v+/BeiN4dWoXBCtdMVwiP5oMRxlOBELXtCknW
5viL085uyvbGON5cFn/K0mcF1x7L0sH/yXX70UAbV1GI3wPwvKQ3n7EczdRYyjms
dic9seyPU3caorevYAvZm+4M5ufsh8L4r35MsCk5ildNW4Kn40qzm14DEUCvlOQq
NyagOwzH08F5RA2wzl0dMYZYzzWEqHYBJBUc6nBxZKvbBmMHyPzb36yp9yYRdiHv
fNYGuS+zQqoNM1G6Oc0hFwmcA9mtdA==
=oKx5
-----END PGP SIGNATURE-----
```