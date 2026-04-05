---
title: v5.8.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.8.0
author: xmrig
tag_name: v5.8.0
published_at: '2020-03-03T05:48:07+00:00'
---

# Version: v5.8.0

# Release Notes
# :warning: Use [v5.8.1](https://github.com/xmrig/xmrig/releases/tag/v5.8.1) instead of this version.

## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.8.0
- [#1573](https://github.com/xmrig/xmrig/pull/1573) Added new AstroBWT algorithm for upcoming DERO fork, as `"algo": "astrobwt"` or `"coin": "dero"`.

## SHA256SUMS
```
6763bba11b3e4ab25eb6387a9882bce02d88807b73691c0b58aa084f62feb761 *xmrig-5.8.0-xenial-x64.tar.gz
f77261e0edb0c6d6fb245437f98460e3729f96d8a4135a335817e964e9f4a703 *xmrig-5.8.0-gcc-win64.zip
16bbd66baa630de44160a4fac7963676831914686ed912ee30c912370f3f8c1f *xmrig-5.8.0-msvc-cuda10_1-win64.zip
5a0b2e03a964574f070f51707b5209bb4d08aaab39bda7d572ce07fa55459d88 *xmrig-5.8.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl5d7sMACgkQRGpTY4vp
RAl8Xwf+IWJVY0RigzIPX1Qhof/qvxoQRePeF3PdLEyIJmwL/Rbky0jQsYVh3Qx6
kinAJxZpJg4NoRRn57xGFnljiiSuTye03g/YXAzrKqOjG3OVoc+pg3Yg8pONj5eS
kR6YHPXfTlhjXdKINLFVlH5kWr+Q4eC5NOkUplwd0HNV/6uP8vEPGeNt3J2H3E27
TsmhbM7wXg78t/FIRX+UusTWXg0ESTTgX7wM9BZ/u6Dk9PnEk/pZob0hcWMibQxD
R/CoTo53crHTEWJKsHK4VxnjYCDBgIDeZ/n/ncJBhlWJLBlHjPmy6WbGIRmal+2p
ZC7Ef/cBf/A+OGA23Iy8an2E7XhX7A==
=XmT2
-----END PGP SIGNATURE-----
```