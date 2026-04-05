---
title: v5.11.4
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.11.4
author: xmrig
tag_name: v5.11.4
published_at: '2020-06-23T05:23:52+00:00'
---

# Version: v5.11.4

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.11.4
- [#1726](https://github.com/xmrig/xmrig/issues/1726) Fixed detection of AVX2/AVX512.
- [#1728](https://github.com/xmrig/xmrig/issues/1728) Fixed, 32 bit Windows builds was crash on start.
- Fixed AMD GPU health (temperatures/power/clocks/fans) readings on Linux.

## SHA256SUMS
```
621491b3f699dc5b8195fa25093a0ff669acd7231571294907173167995abd4b *xmrig-5.11.4-msvc-cuda10_2-win64.7z
d78a71eec49213b87a9150ef0b8ba196a6c79fd0f943f86b45f7a82d44a33db2 *xmrig-5.11.4-xenial-x64.tar.gz
5acdacb6b410afbea72973f7f41785ef5bc522f32c56e1df770a48f074ba68fc *xmrig-5.11.4-gcc-win64.zip
76888dbfd476ef1e8cf664da5c1ed1c4d5aaf0ef46b24014cf7fc9a3cd2ef269 *xmrig-5.11.4-msvc-cuda10_2-win64.zip
7c6b94ef415efb5e1524254c778831e0c72ef31e8ab88174471ae3f22b749c70 *xmrig-5.11.4-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl7xjQwACgkQRGpTY4vp
RAlxHQf/WIwiDEjgTls5mWIZTf9RQ/ZNX+Qd6v0QoPUmo5f5hWK8fOe48chxZdR8
f+Iqxbi/Eedt4LFpsFnrAaplElOK0tLZ/V9cbZxeFZpKslbJMonD/ysi4dOA63sZ
xyuVuyPo8GHLgcq4+KGSoer1l4mJW5M9tUdM8Fjy0nx2/XA8VMPfLk8i9ludAQ81
Q284f6o49Qh8CzgETDpJt6XBjXfTAySSKjBXOaK1tOdGz9W00qajA78Fpb83myGe
uqq35tGSVwkqalAsHyp8Q4SOkyvM04zWyzF+gnpJX6kai+dl8Ubp4xQ6gtR9ta3n
IfOBOzJwxYg0kWUaeR787RDV6TI70Q==
=bKIz
-----END PGP SIGNATURE-----
```