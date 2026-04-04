---
title: Oxygen Orion, Major Point Release 1
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.17.1.0
author: luigi1111
tag_name: v0.17.1.0
published_at: '2020-10-14T16:29:14+00:00'
---

# Version: v0.17.1.0

# Release Notes
# Overview

This is the v0.17.1.0 point release of the Monero software.

Some highlights of this release are:

- Dandelion++: skip desynced peers in stem phase, reducing transaction timeouts
- Fix a bug in wallet serialization that could lead to inaccurate display balance
- Silence spammy "failed to find tx meta" warning message
- Fix next_seed_height in get_block_template RPC
- Fix empty RPATH token issue (Linux / FreeBSD)
- Reduce minimum required glibc from 2.23 to 2.17 (Linux)
- Minor bug fixes

# Contributors for this Release

This release was the direct result of 6 people who worked, largely unpaid and altruistically, to put out 20 commits containing 135 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- luigi1111
- selsta
- xnbya
- moneromooo-monero
- hyc
- xiphon

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.17.1.0.zip)
[Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.17.1.0.zip)
[macOS, 64-bit](https://downloads.getmonero.org/cli/monero-mac-x64-v0.17.1.0.tar.bz2)
[Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.17.1.0.tar.bz2)
[Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.17.1.0.tar.bz2)
[Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.17.1.0.tar.bz2)
[Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.17.1.0.tar.bz2)
[Android, armv7](https://downloads.getmonero.org/cli/monero-android-armv7-v0.17.1.0.tar.bz2)
[Android, armv8](https://downloads.getmonero.org/cli/monero-android-armv8-v0.17.1.0.tar.bz2)
[FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.17.1.0.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-win-x64-v0.17.1.0.zip, b942b584601faa504ed2eb5c6d7bdf62740826cbef63d33d35b48e414dd48f5d
monero-win-x86-v0.17.1.0.zip, d438ce08ebce2705b1de8469833ccda47c76401887751972086246cb3c59f041
monero-mac-x64-v0.17.1.0.tar.bz2, 3e9cefcb02e0fd5f4c720165bf1621ccda48f18eda1f63f207f29a2549658620
monero-linux-x64-v0.17.1.0.tar.bz2, b7b573ff3d2013527fce47643a6738eaf55f10894fa5b2cb364ba5cd937af92e
monero-linux-x86-v0.17.1.0.tar.bz2, e58e1f60120cc9a3be1f6bad95d4605843608630437794c56d705547db2bfd69
monero-linux-armv8-v0.17.1.0.tar.bz2, 487011bc1bdaa9bcc276cdbee0930c2289b317c752a99a38d98c0ad13324a612
monero-linux-armv7-v0.17.1.0.tar.bz2, 2ad46e3834a25f78f1c070220dd1b907200abe57246a7b0cc410b998174e5ed2
monero-android-armv8-v0.17.1.0.tar.bz2, a758c81dfe177c74567e9793e1332adc3e2ce9ae71addb81f1e7f5fcce4303f7
monero-android-armv7-v0.17.1.0.tar.bz2, e0234000ee183656092621066658bece27a49442101755b565f190d4e0d29314
monero-freebsd-x64-v0.17.1.0.tar.bz2, 11577db88edf29d5a09c45599cb43c1da568f63a1303322bf0aecabfaffd48a7
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys). To ensure that the files you download are those originally posted by the maintainers, you should both check that the hashes of your files match those on the signed list, and that the signature on the list is valid.