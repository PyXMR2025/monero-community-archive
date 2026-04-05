---
title: v6.5.1
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.5.1
author: xmrig
tag_name: v6.5.1
published_at: '2020-11-08T09:30:02+00:00'
---

# Version: v6.5.1

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.5.1
- [#1932](https://github.com/xmrig/xmrig/pull/1932) New MSR mod for Ryzen, up to +3.5% on Zen2 and +1-2% on Zen3.
- [#1918](https://github.com/xmrig/xmrig/issues/1918) Fixed 1GB huge pages support on ARMv8.
- [#1926](https://github.com/xmrig/xmrig/pull/1926) Fixed compilation on ARMv8 with GCC 9.3.0.
- [#1929](https://github.com/xmrig/xmrig/issues/1929) Fixed build without HTTP.

## SHA256SUMS
```
1d4e898295e0721fdd89a996fe4624537af4001fe1075a8fb203dee11d96c85d *xmrig-6.5.1-bionic-x64.tar.gz
9a93a4504aa3622a86ddbf6051d163d873067dd951301af5162ddb72dfd13af2 *xmrig-6.5.1-focal-x64.tar.gz
21a5bcb53c79faa7959efd77afb57b2014c0f06448f5e8513e85dc78cc71edbf *xmrig-6.5.1-freebsd-static-x64.tar.gz
029c7187ddba34fb22cc9fe1bb021c9233d4a01a6ee3760adebe4cc153caee2d *xmrig-6.5.1-linux-static-x64.tar.gz
2e9fc6a4caa688ead9629e2f63bb043125a7759ab0f5e361424993a5b8cfed30 *xmrig-6.5.1-linux-x64.tar.gz
4cf812a0fa25f3e36b602515543471aa7abe231e2699b89c8ddcaae4a21f3614 *xmrig-6.5.1-macos-x64.tar.gz
d99c9631015ec0f2754fe3e614a15b0b19bc8087861bb795346ac8cd9541da08 *xmrig-6.5.1-gcc-win64.zip
4b8f9dc5c4db4bad5aa712b8f3dd29543376c5e71e42e8d0990dda954074ab98 *xmrig-6.5.1-msvc-cuda10_2-win64.zip
c3a6766f262576d0e91b1f6d666cab74ade0ade78ef5f184fed6e297e4836d1e *xmrig-6.5.1-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAl+nuN8ACgkQRGpTY4vp
RAnH/wf+O03Tusapon685ylcb1BiHvrJkn+TyJTU2szqjy684JzKK1ZS7hWbVt5Y
OUzpOtYSFkiaqfes4inROP10MGZkqXs3tgDKiVBzdrHfkR3hYUIcp2+qo/e7Isi0
DEdiTAtNUBjtAEEnoN196agrgxk95QDcQbxshp0N3KSev4lqfle5+0Gubgk1DBw9
Fd8brNylguENDv7/8ylMCARrYcJsk9T/OazDGrekNzvdPGR/YoZBaVarLQLBpMuh
nMurDo0bvWGTymLrMyQW5/dPzArlKpaZ47GjME8qDrEc/heJdgbKFtoEfOAke0YR
+kCmyXyyVkBV2e1DnfXxdlIGIH18EQ==
=MuWL
-----END PGP SIGNATURE-----
```