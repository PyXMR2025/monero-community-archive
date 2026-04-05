---
title: v5.8.2
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v5.8.2
author: xmrig
tag_name: v5.8.2
published_at: '2020-03-06T07:31:43+00:00'
---

# Version: v5.8.2

# Release Notes
## Notes
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_1` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v5.8.0
- [#1573](https://github.com/xmrig/xmrig/pull/1573) Added new AstroBWT algorithm for upcoming DERO fork, as `"algo": "astrobwt"` or `"coin": "dero"`.

## v5.8.1
- [#1575](https://github.com/xmrig/xmrig/pull/1575) Fixed new block detection for DERO solo mining.

## v5.8.2
- [#1580](https://github.com/xmrig/xmrig/pull/1580) AstroBWT algorithm 20-50% speedup.
  - Added new option `astrobwt-max-size`.
- [#1581](https://github.com/xmrig/xmrig/issues/1581) Fixed macOS build.

## SHA256SUMS
```
082c6960317f60e852363e4e1fa96cb213a80d66da48aeef5e99762aee00c3af *xmrig-5.8.2-xenial-x64.tar.gz
0ce10d0fd4322d2327d4a92b38cf40b2aa97240a876f6faa61c3b7a8e8f4e5e6 *xmrig-5.8.2-gcc-win64.zip
9a4936032d0c7bdf6a6d585fa22aa88ec0cf5b7a88de5a6b9812c691444342ba *xmrig-5.8.2-msvc-cuda10_1-win64.zip
c38f2745cd559c9d7cb8b8401929e460d66d1fd0b2d1ba03357ac3f1655b46fb *xmrig-5.8.2-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl5h+5gACgkQRGpTY4vp
RAntzAgA0AAWSUO19g8aP5g/x1nNt+lzqNitIG18g9ypEt5vLDclzMQmpNPDglAL
q4I0PdAuNmVyXWkeX4ubixdWx/X3ybzP0q+kbKTIQKxPJ3/O1/zTLkB67PDO0c1S
RaDaBe9uFQ1g189WBoHnxeoqABplie91cnuyKAvoQ/hu0QybBLDXy0s1MOTVQ+9T
vtrDSK8pLwdJA9AObKzpXFuNG6W1VzLZn55535tez+dTnpIEiC2Y/D6PK4ksLsFS
WID/Kmn9PzPsXhKz+UMe6lnsw4uVHaj6SR2bJriD+i20VLXi4knWyWJKYkfVKjhI
YSBfAcqoG7yey62lJ8lnv6joP9HK8Q==
=sS1Z
-----END PGP SIGNATURE-----
```