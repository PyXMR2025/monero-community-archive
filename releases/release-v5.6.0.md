---
title: v5.6.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.6.0
author: xmrig
tag_name: v5.6.0
published_at: '2020-02-15T16:08:49+00:00'
---

# Version: v5.6.0

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.6.0
- [#1536](https://github.com/xmrig/xmrig/pull/1536) Added workaround for new AMD GPU drivers.
- [#1546](https://github.com/xmrig/xmrig/pull/1546) Fixed generic OpenCL code for AMD Navi GPUs.
- [#1551](https://github.com/xmrig/xmrig/pull/1551) Added RandomX JIT for AMD Navi  GPUs.
- Added health information for AMD GPUs (clocks/power/fan/temperature) via ADL (Windows) and sysfs (Linux).
- Fixed possible nicehash nonce overflow in some conditions.
- Fixed wrong OpenCL platform on macOS, option `platform` now ignored on this OS.

## SHA256SUMS
```
181f21368c40f1b8c2a2b1b8d2e9cc70390cd4a7aea8ddb85ec2b3377543d0e9 *xmrig-5.6.0-xenial-x64.tar.gz
42b4cf2ba4c630b90106009f66ce547dd95d63921693df0e8d260b11e71b0c31 *xmrig-5.6.0-gcc-win64.zip
83fb9382216d86b4c44c406d09a941a717f554eefd6acbac508b3c85473c3661 *xmrig-5.6.0-msvc-cuda10_1-win64.zip
c8aa817f03a3e7db6c2d396a80e217715130806d5caa98a22d44ae9167d52ec7 *xmrig-5.6.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl5IBnkACgkQRGpTY4vp
RAmNqQf+JSuvH2EFNHYIvo4nlixYSbXSBNSLew4IbcWDE9dGnoNg9bJsHH/EsBHu
o3Fa0ORcMtptH/Fs1zsAx6t6MdhKKlM0EFVNhx6XUhCCAoZ1xpK9vAEtnUKbmU5k
hL3y+NQydMXiaRZ7el/Gv9kzpt5RNW9ZTuCSWMqN7RcrzlJa8k7NCXNjWE2jF4Eo
36f5hY5AlRMFPHbUSef/fC6wFFqCFlykmXDe4+dIMrnkSw5oe7Y59vYEJgFu0Wvq
zGoiA+7rMUzxrKzoIdPadjO4ZOkhof4StGB5lNEGwXEJj2BPMntIgOnwltMvXwbK
NznpAPwq0ouMjPAet0h5iPQCALoSvQ==
=RTAc
-----END PGP SIGNATURE-----
```