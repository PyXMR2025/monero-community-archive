---
title: v6.8.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.8.0
author: xmrig
tag_name: v6.8.0
published_at: '2021-01-26T09:09:24+00:00'
---

# Version: v6.8.0

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.8.0
- [#2052](https://github.com/xmrig/xmrig/pull/2052) Added DMI/SMBIOS reader.
  - Added information about memory modules on the miner startup and for online benchmark.
  - Added new HTTP API endpoint: `GET /2/dmi`.
  - Added new command line option `--no-dmi` or config option `"dmi"`.
  - Added new CMake option `-DWITH_DMI=OFF`.
- [#2057](https://github.com/xmrig/xmrig/pull/2057) Improved MSR subsystem code quality.
- [#2058](https://github.com/xmrig/xmrig/pull/2058) RandomX JIT x86: removed unnecessary instructions.

## SHA256SUMS
```
cb3cb7fc2b45bcf7f2c129dcbefa732f561fa6c0825b4bf612a1947a0ba26e8b *xmrig-6.8.0-bionic-x64.tar.gz
22d953f930ef069a9b19b96ff1052fc4598d9b1e8265434026f4ff5f45dee0e9 *xmrig-6.8.0-focal-x64.tar.gz
0f2c92288b054bb1af107f34ccc07e94b800380045906871a8098228cfb665bf *xmrig-6.8.0-freebsd-static-x64.tar.gz
9109826b274bb611710446a7f600e11a236119063767307ff9a8a1ce9cadc93f *xmrig-6.8.0-linux-static-x64.tar.gz
0613b50a2f6d6e768c40c23093bb403f67f88a1aca26f164e129eb57533f966f *xmrig-6.8.0-linux-x64.tar.gz
f870c64095cc469225ab0258360dee9acdb72b7c8fae13846476b7b5f4f9e0f9 *xmrig-6.8.0-macos-arm64.tar.gz
75d01da83f6a295a4fba3cf119a0749e9754a8f4c4b85dd5432734f67e14a666 *xmrig-6.8.0-macos-x64.tar.gz
bb919bb794875e8c2320efd5b9ccb774d577d0faa1cfa2a7c89e9f4e2841c597 *xmrig-6.8.0-gcc-win64.zip
3692d4844a00a26e49ee75b751d17f65e8ac2dd65a375942f14566d664f5bd5c *xmrig-6.8.0-msvc-cuda10_2-win64.zip
087210ca3f5dfe324730e68eb27419bce79688a29164c7711af6ec4c681a8506 *xmrig-6.8.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmAP23AACgkQRGpTY4vp
RAnkrggAmPP7AGlUr4iSHHuRdapb3JrfwKnDwgYN+WFcnzIUhQAnLuvIiw+ujvmN
OVN0OT0ymEMV7k83V3z8xbkhoYttrXpWqiohUW0Sj3UwcejLs+6oDT7U5oo1FzY4
NKUFIYt/qTaPgxtl5QDNwB8wRf0dr+l8sXiTIu9+FoCACRTJhRDU6y0Mnmwuhqw2
XQZWUuWvCwyLf17wlzIZuqr5CkFdZDi/YDKXilca/3mqr2Of/fq0U8mBH6Fef8ox
McQ8TJuDmYPuBxcC5BzBcXdWXsRFqdejdckL3DNWSI8Ta5kXpwYUvtIAyeinhMSy
F9EB7xJJe3tF/kLa4oTL1WGTtZBBAw==
=McdT
-----END PGP SIGNATURE-----
```