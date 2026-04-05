---
title: v5.5.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.5.0
author: xmrig
tag_name: v5.5.0
published_at: '2019-12-29T15:38:54+00:00'
---

# Version: v5.5.0

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.5.0
- [#179](https://github.com/xmrig/xmrig/issues/179) Added support for [environment variables](https://xmrig.com/docs/miner/environment-variables) in config file.
- [#1445](https://github.com/xmrig/xmrig/pull/1445) Removed `rx/v` algorithm.
- [#1453](https://github.com/xmrig/xmrig/issues/1453) Fixed crash on 32bit systems.
- [#1459](https://github.com/xmrig/xmrig/issues/1459) Fixed crash on very low memory systems.
- [#1465](https://github.com/xmrig/xmrig/pull/1465) Added fix for 1st-gen Ryzen crashes.
- [#1466](https://github.com/xmrig/xmrig/pull/1466) Added `cn-pico/tlo` algorithm.
- Added `--randomx-no-rdmsr` command line option.
- Added console title for Windows with miner name and version.
- On Windows `priority` option now also change base priority.

## SHA256SUMS
```
89c5246df9de4373568b11c195711a7756429c9cc451aa00e57612dc55c8509c *xmrig-5.5.0-xenial-x64.tar.gz
21a17555446ce6e92f2cae8a5b4bf2bb71331e036e1aca9c7644381b2b42edc5 *xmrig-5.5.0-gcc-win32.zip
c236556adaa53df6cd8109429b515e0ae4dde1efa95f52738b9315aad542586d *xmrig-5.5.0-gcc-win64.zip
4c70c016ae849482055e7ed03f245bad54126a52ff377d55171d1a57f6e3fffb *xmrig-5.5.0-msvc-cuda10_1-win64.zip
6fe1ad5593977e43f333c769d66d7d611e4712493e0a2cc985cacd63b5dd424a *xmrig-5.5.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl4IxNUACgkQRGpTY4vp
RAkCvAgAmyGlV6tyQJ4mdv7wu/JFqCMMF/gbbzh3hZx8u8Vh9LnGOf5nle+BwmX9
aU5MML1n368+Noy6ZNHMijLPBufCLz9mCIkr1tbQoLUOfOtPtSe+fWfMOc3kmj3r
wYeweq4CLH4qO24kbiqsEvpM+Zjoo5ZqFtA6B8pjz0A0Ej9bKhFRUL/p+K3WpjnL
nfHaz7dXKVxio+2YWt8T5ATLVcOEIA8P2hvUAgTu4IS5xAFfFgc6QX47srrPviRD
fmSRZKss3RiIidHkyAeMsiAp8EMdtM8tzzr5vfvC7IF4aRY5RiMjhPayK0rqQ0dt
MXyjdHw5lfnSnPjoPXy3EDydyAUjtg==
=waXx
-----END PGP SIGNATURE-----
```