---
title: v5.3.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.3.0
author: xmrig
tag_name: v5.3.0
published_at: '2019-12-15T09:46:07+00:00'
---

# Version: v5.3.0

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.3.0
- [#1414](https://github.com/xmrig/xmrig/pull/1414) Added native MSR support for Windows, by using signed **WinRing0 driver** (© 2007-2009 OpenLibSys.org).
- Added new [MSR documentation](https://xmrig.com/docs/miner/randomx-optimization-guide/msr).
- [#1418](https://github.com/xmrig/xmrig/pull/1418) Increased stratum send buffer size.

## SHA256SUMS
```
77f74cf93865b93c40ec556baef2c7e166c1e19bd7af44b1d0ed24cad14bc8ef *xmrig-5.3.0-xenial-x64.tar.gz
b811354ce8da6511734380cce329103a45df8d47b970a28ae5672f7b8bf7ee47 *xmrig-5.3.0-gcc-win64.zip
856521124ef403b01df6e6df4826570d917c93a073fe4ea910f77e4b8867aa7f *xmrig-5.3.0-msvc-cuda10_1-win64.zip
d719d5f6697e19ec3c0f9067241d331f1ea3210a6570c148e71bb2ed7bfbf3a6 *xmrig-5.3.0-msvc-win64.zip
```

## SHA256SUMS.sig

GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl31/44ACgkQRGpTY4vp
RAl8wAgAm2EQ5HHcAxTdi4LuuYUQvhS1WYx2Sn84zZfhCOhSkO3KqvGuYgcfZER3
A8mMSmvOmdgCBMYM6ZWI1npLAbF4xemxGdeQtWdBfzCpK+T/claTNBjfs9x//l3y
6PHF9WiUryZAO9AiaFD0YwnxGywetfN5+yBMFqSmIpqU+NMVmw/Vv5VXatPFcKf5
duR7bkc4PAcFEu9oEcOUVyEH5B+S9wFvBw20WugrUUnnDWRCO5Ps8ngrZmePUKxf
xhpvPwgl/qKnwYvWEoP3jeSye0+iAyCvHqS1+9jkVc+Kg+XW3yq6wV9z3htD+Cap
7vhSX6KWoRd88pcrWUp1UFyNKiPtlw==
=H+CB
-----END PGP SIGNATURE-----
```