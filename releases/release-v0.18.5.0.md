---
title: Fluorine Fermi, Major Point Release 5
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.18.5.0
author: binaryFate
tag_name: v0.18.5.0
published_at: '2026-05-12T18:45:06+00:00'
---

# Version: v0.18.5.0

# Release Notes
# Overview

This is the v0.18.5.0 release of the Monero software. This recommended release adds SOCKS v5 support, removes UPnP support, and includes a large number of bug fixes.

Some highlights of this release are:

- Add SOCKS v5 support to daemon and wallet (#10411)
- Daemon: remove UPnP support (#10465)
- Daemon: fix shutdown hangs (#10494, #10401, #10489)
- Daemon: improve exception handling (#10437, #10373)
- Daemon: speed up transaction pool `get_complement()` for large requests (#10377)
- Daemon: restrict `add_aux_pow` RPC (#10409)
- ZMQ: add restricted RPC mode (#10389, #10420, #10425, #10469, #10504)
- ZMQ: fix txpool transaction reporting for stem-phase transactions (#10399)
- ZMQ: notify txpool event when stem transaction bumps to fluff (#10453)
- Wallet: improve proof validation (#10480, #10471, #10481, #10473)
- Wallet: add option to skip refresh after multisig import (#10402)
- Wallet: add change address sanity check (#10431)
- Wallet RPC: add source info to `describe_transfer` (#10380)
- Wallet RPC: fix `set_daemon` allowed SSL fingerprints parsing (#10433)
- Wallet RPC: restrict sensitive methods in `--restricted-rpc` mode (#10379, #10435)
- Harden HTTP client authentication handling (#10364)
- Add LoongArch build support (#10400)
- Various bug fixes and improvements

# Contributors for this Release

This release was the direct result of 12 people who worked to put out 96 commits containing 2786 new lines of code. We'd like to thank them very much for their time and effort. In no particular order, they are:

- tobtoht
- selsta
- hinto-janai
- jeetrex17
- lschomaker1
- nahuhh
- fangyaling
- SNeedlewoods
- jeffro256
- vtnerd
- woodser
- j-berman

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.18.5.0.zip)
[Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.18.5.0.zip)
[macOS, Intel](https://downloads.getmonero.org/cli/monero-mac-x64-v0.18.5.0.tar.bz2)
[macOS, ARM](https://downloads.getmonero.org/cli/monero-mac-armv8-v0.18.5.0.tar.bz2)
[Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.18.5.0.tar.bz2)
[Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.18.5.0.tar.bz2)
[Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.18.5.0.tar.bz2)
[Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.18.5.0.tar.bz2)
[Linux, riscv64](https://downloads.getmonero.org/cli/monero-linux-riscv64-v0.18.5.0.tar.bz2)
[Android, armv7](https://downloads.getmonero.org/cli/monero-android-armv7-v0.18.5.0.tar.bz2)
[Android, armv8](https://downloads.getmonero.org/cli/monero-android-armv8-v0.18.5.0.tar.bz2)
[FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.18.5.0.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-win-x64-v0.18.5.0.zip, 027d96a72d36663b6f5cbcc5b1564c65c628a9f8f2bb9b4d9859c03f741cabc4
monero-win-x86-v0.18.5.0.zip, ce0210583b1b4113d709bb432dde72c55b76c40ebbc7b5b4d4ae862b507632a1
monero-mac-x64-v0.18.5.0.tar.bz2, 79e03406046255d0f6a47e1fdcbbe677ab11ef7d9fcc4481252235361769292c
monero-mac-armv8-v0.18.5.0.tar.bz2, fb48fcef9302bf2f97821498ec791b4f693af4984702e72e588ce02209f8960d
monero-linux-x64-v0.18.5.0.tar.bz2, 166ad93036f95f5abeba24c8670061be022c9238dba2e6a7587611a1d759e294
monero-linux-x86-v0.18.5.0.tar.bz2, 57c63e067d7aefa69f74f44ef7f46091251512aba39570a7c8e26644d298eeb5
monero-linux-armv8-v0.18.5.0.tar.bz2, d8f19b947ce46d468615bb7331962d4ca732e79b1ac6c5128fa509df3f6cc487
monero-linux-armv7-v0.18.5.0.tar.bz2, dedaf94b765c428040f1b64e580e389206141fa2be72fd1394be0a8614f04f40
monero-linux-riscv64-v0.18.5.0.tar.bz2, 219112ffac9af48226dc6ec1fadc8a210a5876eeb7f3a32f3d3cbae842b52bf9
monero-android-armv8-v0.18.5.0.tar.bz2, 7321662959f917db85c3da1c0a37530d21fb5c25e2c9a2dc0490486842dec974
monero-android-armv7-v0.18.5.0.tar.bz2, ab5ab33899c5ac6806a0c1a24a3b01d46c291142f0983a8a184f93c8a3baca9f
monero-freebsd-x64-v0.18.5.0.tar.bz2, 0beb34bac944fdf02e2939fe320b9a6a5b26910cbf0a1a629b26be2aad50bace
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in `/utils/gpg_keys`). To ensure that the files you download are those originally posted by the maintainers, you should both check that the hashes of your files match those on the signed list, and that the signature on the list is valid.
