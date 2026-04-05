---
title: v5.1.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.1.0
author: xmrig
tag_name: v5.1.0
published_at: '2019-12-01T08:54:49+00:00'
---

# Version: v5.1.0

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.1.0
- [#1351](https://github.com/xmrig/xmrig/pull/1351) RandomX optimizations and fixes.
  - **Improved RandomX performance (up to +6-7% on Intel CPUs, +2-3% on Ryzen CPUs)**
  - Added workaround for Intel JCC erratum bug see https://www.phoronix.com/scan.php?page=article&item=intel-jcc-microcode&num=1 for details.
  - Note! Always disable "Hardware prefetcher" and "Adjacent cacheline prefetch" in BIOS for Intel CPUs to get the optimal RandomX performance.
- [#1307](https://github.com/xmrig/xmrig/issues/1307) Fixed mining resume after donation round for pools with `self-select` feature.
- [#1318](https://github.com/xmrig/xmrig/issues/1318#issuecomment-559676080) Added option `"mode"` (or `--randomx-mode`) for RandomX.
  - Added memory information on miner startup.
  - Added `resources` field to summary API with memory information and load average.

## SHA256SUMS
```
536aac41864f0078849fea8dad039efac9fb6234d60554aa751991d802117625 *xmrig-5.1.0-xenial-x64.tar.gz
d87ad21033b5a8550816e282d6c158cb8d316cc7f5f5b054ec127f3b7974580f *xmrig-5.1.0-gcc-win32.zip
2fc54d97e58b64cbb710e7bb192c43ff60c30ecb15d43e4555383655a9379a4d *xmrig-5.1.0-gcc-win64.zip
b5b1044b18cb4981f6a6cda9c02c8d776484db2091e292af1f4cd6c2529cfdd6 *xmrig-5.1.0-msvc-cuda10_1-win64.zip
b463d80da09c5c6c244e81b47be89fb30fbdb59beeb91029c41c14c93951a36d *xmrig-5.1.0-msvc-win64.zip
```

## SHA256SUMS.sig

GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl3jfmsACgkQRGpTY4vp
RAkcGwf/afzoEBNolI7cpudiHWHrhH+w7g60tbhc4cf6oRhdoFdWQDX+ZHPElAS0
CH0050ONPC61VgHTQrBdFuRPVy3wjHCLv7fvsA8Nd1za+xC5mnDkcEWpnpxeUqAD
DrpJzUkjVjdhbTsSWozvJ6N7PEwmS7ErZKwzk/JQMTlMz5gLwPiqquTX1LXsxBO0
kcCS5DmcB+iAUavyj8OaAqNMIkkFvGKCSyTK636DoJh2RVXrO/d8LwdRM2J3zO3p
r2S2rLf341jEm5E1ptYBIIKisshoi5N1T/9vnJtOQjbp7JFTJAc1uSJIB0QA4AXB
IJchcTA1Kdq3rBMlzCHftwjo/V+OcQ==
=f7DM
-----END PGP SIGNATURE-----

```