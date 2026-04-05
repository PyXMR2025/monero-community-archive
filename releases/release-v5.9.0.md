---
title: v5.9.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.9.0
author: xmrig
tag_name: v5.9.0
published_at: '2020-03-08T08:00:17+00:00'
---

# Version: v5.9.0

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.9.0
- [#1578](https://github.com/xmrig/xmrig/pull/1578) Added new RandomKEVA algorithm for upcoming Kevacoin fork, as `"algo": "rx/keva"` or `"coin": "keva"`.
- [#1584](https://github.com/xmrig/xmrig/pull/1584) Fixed invalid AstroBWT hashes after algorithm switching.
- [#1585](https://github.com/xmrig/xmrig/issues/1585) Fixed build without HTTP support.
- Added command line option `--astrobwt-max-size`.

## SHA256SUMS
```
1727449ec2da2ff7c52651d67e188f6bf1d6803a22890de3a539a324df960b68 *xmrig-5.9.0-xenial-x64.tar.gz
5fe8757435a5775f6c0b782f625603641f57e780776370ad68623a5c61731147 *xmrig-5.9.0-gcc-win64.zip
6a46e7ce2a8f094f14317fb9e423cd8783a54d4f4414d6ad6d47277cf0cb9a9f *xmrig-5.9.0-msvc-cuda10_1-win64.zip
5f620fa3164a88980c1807a4a6ce48e151fbae79f8c268984191c8a939aaec2f *xmrig-5.9.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl5kohwACgkQRGpTY4vp
RAlhBQf/eb3FluAT0wki0NyoBAMmqepxAiNg9RTNo+EMrQqdgpVE35bkkynn1Q9N
tIUTRpPO05s1cTzidhHye29nBlydHHnK7f88pbtZ+jxIOD23pBehv9km/0G4Hfy9
9fEWSBAwELexNAhA87zu42hbvX6+hgatYjJIdYbicau7M6bhrHnQbGcampERWZP6
jwKN+yuMO/wIJIIP+9tPfLkM62DdWkiFUH4lvO5UwFYWUwhLLn40HiqMD5bydYR2
7v2urYYKm3ywz3pWsaZcfgn11t77pqS4HFzF8uycn4+czzbjWGAqa+Sno46yljh3
TBqlWNXXPdz/knXhhttVZ1Hf9te5jQ==
=RwHH
-----END PGP SIGNATURE-----
```