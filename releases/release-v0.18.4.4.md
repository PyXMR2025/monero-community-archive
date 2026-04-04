---
title: Fluorine Fermi, Point Release 4.4
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.18.4.4
author: binaryFate
tag_name: v0.18.4.4
published_at: '2025-11-19T10:37:04+00:00'
---

# Version: v0.18.4.4

# Release Notes
# Overview

This is the v0.18.4.4 release of the Monero software. This is a recommended release that fixes a bug with Ledger hardware wallet when rejecting secret view key export.

Some highlights of this release are:

- Ledger: make secret view key export mandatory (#10195)
- Wallet: identify spends in pool when scanning (#10153)
- Daemon: relay empty fluffy block on found block (#10206)
- Daemon: correct txpool weight miscalculation in edge case (#10204)
- Daemon: refine sync height selection logic (#10202)
- Additional logging deadlock fixes (#10194)
- Minor bug fixes and improvements

# Contributors for this Release

This release was the direct result of 4 people who worked to put out 14 commits containing 286 new lines of code. We'd like to thank them very much for their time and effort. In no particular order, they are:

- tobtoht
- 0xFFFC0000
- selsta
- j-berman

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.18.4.4.zip)
[Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.18.4.4.zip)
[macOS, Intel](https://downloads.getmonero.org/cli/monero-mac-x64-v0.18.4.4.tar.bz2)
[macOS, ARM](https://downloads.getmonero.org/cli/monero-mac-armv8-v0.18.4.4.tar.bz2)
[Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.18.4.4.tar.bz2)
[Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.18.4.4.tar.bz2)
[Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.18.4.4.tar.bz2)
[Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.18.4.4.tar.bz2)
[Linux, riscv64](https://downloads.getmonero.org/cli/monero-linux-riscv64-v0.18.4.4.tar.bz2)
[Android, armv7](https://downloads.getmonero.org/cli/monero-android-armv7-v0.18.4.4.tar.bz2)
[Android, armv8](https://downloads.getmonero.org/cli/monero-android-armv8-v0.18.4.4.tar.bz2)
[FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.18.4.4.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-win-x64-v0.18.4.4.zip, 7eb3b87a105b3711361dd2b3e492ad14219d21ed8fd3dd726573a6cbd96e83a6
monero-win-x86-v0.18.4.4.zip, a148a2bd2b14183fb36e2cf917fce6f33fb687564db2ed53193b8432097ab398
monero-mac-x64-v0.18.4.4.tar.bz2, af3d98f09da94632db3e2f53c62cc612e70bf94aa5942d2a5200b4393cd9c842
monero-mac-armv8-v0.18.4.4.tar.bz2, 645e9bbae0275f555b2d72a9aa30d5f382df787ca9528d531521750ce2da9768
monero-linux-x64-v0.18.4.4.tar.bz2, 7fe45ee9aade429ccdcfcad93b905ba45da5d3b46d2dc8c6d5afc48bd9e7f108
monero-linux-x86-v0.18.4.4.tar.bz2, 8c174b756e104534f3d3a69fe68af66d6dc4d66afa97dfe31735f8d069d20570
monero-linux-armv8-v0.18.4.4.tar.bz2, b9daede195a24bdd05bba68cb5cb21e42c2e18b82d4d134850408078a44231c5
monero-linux-armv7-v0.18.4.4.tar.bz2, 2040dc22748ef39ed8a755324d2515261b65315c67b91f449fa1617c5978910b
monero-linux-riscv64-v0.18.4.4.tar.bz2 c939ea6e8002798f24a56ac03cbfc4ff586f70d7d9c3321b7794b3bcd1fa4c45
monero-android-armv8-v0.18.4.4.tar.bz2, eb81b71f029884ab5fec76597be583982c95fd7dc3fc5f5083a422669cee311e
monero-android-armv7-v0.18.4.4.tar.bz2, 7c2ad18ca3a1ad5bc603630ca935a753537a38a803e98d645edd6a3b94a5f036
monero-freebsd-x64-v0.18.4.4.tar.bz2, bc539178df23d1ae8b69569d9c328b5438ae585c0aacbebe12d8e7d387a745b0
monero-source-v0.18.4.4.tar.bz2, 84570eee26238d8f686605b5e31d59569488a3406f32e7045852de91f35508a2
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys). To ensure that the files you download are those originally posted by the maintainers, you should both check that the hashes of your files match those on the signed list, and that the signature on the list is valid.