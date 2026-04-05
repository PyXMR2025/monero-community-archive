---
title: v5.7.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.7.0
author: xmrig
tag_name: v5.7.0
published_at: '2020-02-24T23:33:04+00:00'
---

# Version: v5.7.0

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.7.0
- **Added SOCKS5 proxies support for Tor https://xmrig.com/docs/miner/tor.**
- [#377](https://github.com/xmrig/xmrig-proxy/issues/377) Fixed duplicate jobs in daemon (solo) mining client.
- [#1560](https://github.com/xmrig/xmrig/pull/1560) RandomX 0.3-0.4% speedup depending on CPU.
- Fixed possible crashes in HTTP client.

## SHA256SUMS
```
c05613910ddb42f468bed10634c5cb74d562cf00093424955f1486f6f4c5cb6f *xmrig-5.7.0-xenial-x64.tar.gz
6d81a1be4da3f89f336f6207aec9e02ba432d3c7c171c917a045f05203990a35 *xmrig-5.7.0-gcc-win64.zip
488254c512e2edcbb4407455bef37301a88bb39658681d7a65cfbf113625479e *xmrig-5.7.0-msvc-cuda10_1-win64.zip
1522415404f0cbbc56db4c3f6226721b16fbe0bc0974da8fb0d6c2842feaf3b4 *xmrig-5.7.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl5UWWMACgkQRGpTY4vp
RAl7CAf/ThMCp9WbzZS0GG5EzbPokX0R8OZPsAXAmSbUy7ukQPrYe5qeA715L5GE
6X25J3j0721yqFrna3xVDguZdaiButLUkFJMgm8Yi1/BjM6kuRG+9rqv4EDTeq69
gMf5+9gIon3XkCdN9RoQoAqUaiKe4ltTgbq2799NIjZ5cVj6fJKuXM/G/QmSUZJA
S9v53yNiAEaRU2UpSfKOEtCpoVZOIkk7kL4c3spkSsajiXAfh9hDDARnZ9tlG02z
HEYbkyLcqn3Cc6ORS2sZY5xARJO9L2+K3OmjDXFmzrT+XbafpFPksgRO/pa1HzGu
FHpkyIRkpDR6i8YHS161F3bbZGTdWg==
=tVCa
-----END PGP SIGNATURE-----
```