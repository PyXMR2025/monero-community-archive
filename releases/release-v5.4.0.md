---
title: v5.4.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.4.0
author: xmrig
tag_name: v5.4.0
published_at: '2019-12-21T10:19:49+00:00'
---

# Version: v5.4.0

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.4.0
- [#1434](https://github.com/xmrig/xmrig/pull/1434) Added RandomSFX (`rx/sfx`) algorithm for Safex Cash.
- [#1445](https://github.com/xmrig/xmrig/pull/1445) Added RandomV (`rx/v`) algorithm for *new* MoneroV.
- [#1419](https://github.com/xmrig/xmrig/issues/1419) Added reverting MSR changes on miner exit, use `"rdmsr": false,` in `"randomx"` object to disable this feature.
- [#1423](https://github.com/xmrig/xmrig/issues/1423) Fixed conflicts with exists WinRing0 driver service.
- [#1425](https://github.com/xmrig/xmrig/issues/1425) Fixed crash on first generation Zen CPUs (MSR mod accidentally enable Opcache), additionally now you can disable Opcache and enable MSR mod via config `"wrmsr": ["0xc0011020:0x0", "0xc0011021:0x60", "0xc0011022:0x510000", "0xc001102b:0x1808cc16"],`.
- Added advanced usage for `wrmsr` option, for example: `"wrmsr": ["0x1a4:0x6"],` (Intel) and `"wrmsr": ["0xc0011020:0x0", "0xc0011021:0x40:0xffffffffffffffdf", "0xc0011022:0x510000", "0xc001102b:0x1808cc16"],` (Ryzen).
- Added new config option `"verbose"` and command line option `--verbose`.

## SHA256SUMS
```
b444329e6461c49db68d9d771b4445024405b404980f5b4f47f32e5277d4ef3e *xmrig-5.4.0-xenial-x64.tar.gz
00b7ace4f1c027aa22eca18f38e41e0635da2fb5681f570aaa9c329dcf382045 *xmrig-5.4.0-gcc-win64.zip
67fa8e81586e99d066d30f127c2767990c00b78e9e5d669caad567ecf148c26e *xmrig-5.4.0-msvc-cuda10_1-win64.zip
85301585e0942b16fa934f96381e1bc633ff33f37acaf90e73b5e986c00bfb93 *xmrig-5.4.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl397TUACgkQRGpTY4vp
RAlwWwgAjd3s35yc/NpHAKn/tZ7VDpFXWkYGFLUkrZMEu7PEThnZf12/782/U65G
txEehZO7RqndKtF6ee7lHKVOiHmspwk1znp+WWugzd7TUpCB9grojRO3fGaBdTgl
vonPyxEpkbgbnh722c0+qSPJ/w8mjtuOoFQIgkSlTaY1AYS3NX/baa9MHODNNBWN
5ScJEi1d4ZjxPOKyPLJBez1W9b8up42L22rly3ofF2A/3hpJmf5aIMdGqNojM1JO
BuCC1yOuBJceenSAk/jygfag6zk4LL69uDqXMTdWl+chdMFIdsMG4Bow67BUqFVj
iKjjexKf+vIuITVHLxd7qWHieauAkQ==
=mWu8
-----END PGP SIGNATURE-----
```