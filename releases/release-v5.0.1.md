---
title: v5.0.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.0.1
author: xmrig
tag_name: v5.0.1
published_at: '2019-11-18T15:21:41+00:00'
---

# Version: v5.0.1

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.0.1
- [#1234](https://github.com/xmrig/xmrig/issues/1234) Fixed compatibility with some AMD GPUs.
- [#1284](https://github.com/xmrig/xmrig/issues/1284) Fixed build without RandomX.
- [#1285](https://github.com/xmrig/xmrig/issues/1285) Added command line options `--cuda-bfactor-hint` and `--cuda-bsleep-hint`.
- [#1290](https://github.com/xmrig/xmrig/pull/1290) Fixed 32-bit ARM compilation.

## SHA256SUMS
```
6bb1a2e3a0fbca5195be6022f2a9fbff8a353c37c7542e7ab89420cb45b64505  xmrig-5.0.1-gcc-win32.zip
24dba9ec281acfb2ea2c401ebd0e4e2d1f1ee5fd557da5ff3c7049020c1f78b6  xmrig-5.0.1-gcc-win64.zip
86d65c6693ec9e35cd7547329580638b85c9eb0cf8383892a1c15199de5b556f  xmrig-5.0.1-msvc-cuda10_1-win64.zip
0fbfe518b1c4b6993b0f66ff01302626375b15620ccf8f64d6fb97845068ffca  xmrig-5.0.1-msvc-win64.zip
aa34890738a3494de2fa0e44db346937fea7339852f5f10b5d4655f95e2d8f1f  xmrig-5.0.1-xenial-x64.tar.gz
```

## SHA256SUMS.sig

GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl3VcsoACgkQRGpTY4vp
RAm9vQgA1MyTUU2jley2TCYLUzQy2Fffc8fbXYv64r44jbWOjC/6qo2iIlRgPhIc
oVyPKr5TYS3QjDzCEm8IvozS0YudS6soESbPzqDonboK8pd0K4bsML9TQY2feV7A
NL5vln0rfVHp1wxLLrQpfBqAgvJUXEyaHece6gFQN79JOGhEo2bHL2NyrOl+FViS
b2BaMtXq410Fh+XT6ShnOaG/2EuO8ZqSGdCO6A/2LHQw1UY+mZiCvue6P6B06HmB
WD/urOv38V389v+V+Sp4UlEW6VpBOOjvtChoVWtLt+tKzydrnt2EmoWWWg475pka
4G6whHuMWS8CTt5/PDhJpvVXNQTIOw==
=C764
-----END PGP SIGNATURE-----
```