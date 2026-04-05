---
title: v6.9.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v6.9.0
author: xmrig
tag_name: v6.9.0
published_at: '2021-02-21T15:06:44+00:00'
---

# Version: v6.9.0

# Release Notes
## Notes
- **[RandomX Benchmark](https://xmrig.com/benchmark) :new:**
- [KawPow release notes](https://github.com/xmrig/xmrig/pull/1694#issuecomment-638310915)
- Stay tuned about updates, follow me on twitter https://twitter.com/xmrig_dev
- [Configuration wizard](https://xmrig.com/wizard)
- [Management panel for miners](http://workers.xmrig.info/)
- For NVIDIA CUDA mining support, use version with `cuda10_2` suffix or any regular version with [CUDA plugin](https://github.com/xmrig/xmrig-cuda).

## v6.9.0
- [#2104](https://github.com/xmrig/xmrig/pull/2104) Added [pause-on-active](https://xmrig.com/docs/miner/config/misc#pause-on-active) config option and `--pause-on-active=N` command line option.
- [#2112](https://github.com/xmrig/xmrig/pull/2112) Added support for [Tari merge mining](https://github.com/tari-project/tari/blob/development/README.md#tari-merge-mining).
- [#2117](https://github.com/xmrig/xmrig/pull/2117) Fixed crash when GPU mining `cn-heavy` on Zen3 system.

## SHA256SUMS
```
f7cbfeff9d27fc15dab5cfced5ea72b57ebc51000ee8105b891373051cf3f4ff *xmrig-6.9.0-bionic-x64.tar.gz
2d67dd33adeb42ee4aa467d5638b0809b6ab1e0f88180e67bcc97a4fe21aa822 *xmrig-6.9.0-focal-x64.tar.gz
42e22b1484fb8bd2d73e5089bcc4c9de6b5fd4c57af1943a7ec3aafa2525a852 *xmrig-6.9.0-freebsd-static-x64.tar.gz
c9d02f9f094006ac56f800281f7e3fc875619675431af5a32d81dfef1da0f9f0 *xmrig-6.9.0-linux-static-x64.tar.gz
3dc6ca4c6c40d00850182616d2f7834b2b9d2dcda0619611c2612cead8d39a92 *xmrig-6.9.0-linux-x64.tar.gz
c86f9a9c225e1a4b77587b2cccbcb8453966bd730b65ed8759de7538d56f3d1a *xmrig-6.9.0-macos-arm64.tar.gz
d795141adaca612354939b6aa80b4404aa42864600e63b68b868e0dbe4fdab62 *xmrig-6.9.0-macos-x64.tar.gz
a4aad44ab9cadacb38e231527b94a29864fdfa858878b4fe0ad82f6fe6340d61 *xmrig-6.9.0-gcc-win64.zip
d6b7d6ebdbe02d36b91611a54e3d47215bb36db341e04c45f7e134a62ad1eb97 *xmrig-6.9.0-msvc-cuda10_2-win64.zip
5bbc7bc6f1b3914b4873c87870ad37898b8c8430c2808e0d637b729c9d1d958d *xmrig-6.9.0-msvc-win64.zip
```

## SHA256SUMS.sig

**GPG public key: [xmrig.com](https://xmrig.com/docs/gpg-key) + [github]( https://github.com/xmrig/xmrig/blob/master/doc/gpg_keys/xmrig.asc)**

```
-----BEGIN PGP SIGNATURE-----

iQEzBAABCgAdFiEEmsTOqOZuNaXHzdwbRGpTY4vpRAkFAmAydHcACgkQRGpTY4vp
RAm/mQf/Re1fZ1OiKfhI2VQshuJ5Rstt/8dOtaefEeNoQLN86xPyrLNr60vwAjX1
nZLAFiDrcQopo9da7qJKJAZOwTC3H2NFX3rHi8nLuA1RSbX+pnw8aK7UMNv5ibKy
79Jc7SBTKsOFPnmh1yjvwp4tquXkBbD7bn5hK2BDgqRD2yHLTf+WBvJKK4522k5Z
gcGmZEFtGW9PpgwmLJCwzpMEaf4Ke/EBkc6eEstuQyq6LLdJWjMBk3Ada94DYiFJ
zEvMirEmJP7HUuDFoztokN6itrTZ2MV5nA9BjSeDZzL0SrdkssnqnBjZcbKJPvgk
A5w0B26r/250tp4DMRq6VdWh6NZ5kg==
=P6+H
-----END PGP SIGNATURE-----
```