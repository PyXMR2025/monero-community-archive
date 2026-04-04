---
title: ' Oxygen Orion, Point Release 3.2'
type: release
source_url: https://github.com/monero-project/monero/releases/tag/v0.17.3.2
author: binaryFate
tag_name: v0.17.3.2
published_at: '2022-04-29T19:17:10+00:00'
---

# Version: v0.17.3.2

# Release Notes
# Overview

This is the v0.17.3.2 point release of the Monero software. This release adds support for Ledger Nano S Plus.

Some highlights of this point release are:

- Wallet: add support for Ledger Nano S Plus (#8239)
- Wallet: balance includes unconfirmed payments (#8154, #8159)
- Wallet: rename duplicate amount headers in CSV export (#8177)
- Wallet: multisig key exchange update and code refactor (#8190)
- Wallet: fix stagenet restore height estimation (#8196)
- Daemon: replace outdated seed nodes (#8222, #8131)
- Daemon: don't require `--rpc-login` with `--rpc-access-control-origins` (#8227)
- Daemon: add a sanity check to RPC input data size (#8276) [Reported by m31007]
- RPC: support authentication with `set_daemon` command (#8166)
- Fix compilation on OpenBSD RISC-V (#8241)
- Minor bug fixes

# Contributors for this Release

This release was the direct result of 10 people who worked, largely unpaid and altruistically, to put out 28 commits containing 2294 new lines of code. We'd like to thank them very much for their time and effort. In no particular order they are:

- luigi1111
- Gingeropolous
- woodser
- jeffro256
- hbs
- moneromooo
- reemuru
- UkoeHB
- erciccione
- selsta

# Official Download Links

[Windows, 64-bit](https://downloads.getmonero.org/cli/monero-win-x64-v0.17.3.2.zip)
[Windows, 32-bit](https://downloads.getmonero.org/cli/monero-win-x86-v0.17.3.2.zip)
[macOS, 64-bit](https://downloads.getmonero.org/cli/monero-mac-x64-v0.17.3.2.tar.bz2)
[Linux, 64-bit](https://downloads.getmonero.org/cli/monero-linux-x64-v0.17.3.2.tar.bz2)
[Linux, 32-bit](https://downloads.getmonero.org/cli/monero-linux-x86-v0.17.3.2.tar.bz2)
[Linux, armv7](https://downloads.getmonero.org/cli/monero-linux-armv7-v0.17.3.2.tar.bz2)
[Linux, armv8](https://downloads.getmonero.org/cli/monero-linux-armv8-v0.17.3.2.tar.bz2)
[Android, armv7](https://downloads.getmonero.org/cli/monero-android-armv7-v0.17.3.2.tar.bz2)
[Android, armv8](https://downloads.getmonero.org/cli/monero-android-armv8-v0.17.3.2.tar.bz2)
[FreeBSD, 64-bit](https://downloads.getmonero.org/cli/monero-freebsd-x64-v0.17.3.2.tar.bz2)

# Download Hashes

If you would like to verify that you have downloaded the correct file, please use the following SHA256 hashes:

```
monero-win-x64-v0.17.3.2.zip, 4912d97040af32c14a99e3db1357fc2516e4ed9a8bbf828fc636bcf558b03a65
monero-win-x86-v0.17.3.2.zip, d2a2475943f75d33ec448844166a2cefe4b5fbbec63d3662682491fc32b2257b
monero-mac-x64-v0.17.3.2.tar.bz2, 3631f84739ef73d0105d902639c75d66921da6c8dff5487e01a11bf523dd0cae
monero-linux-x64-v0.17.3.2.tar.bz2, 1e54acd749265d9439d3733441c645d9b058316283c8f21cca2a333c1238cd16
monero-linux-x86-v0.17.3.2.tar.bz2, 2b3365b740b5f35a42db1b032e9401b5e2ed4e6d9266eea4f5e01ea747952cb5
monero-linux-armv8-v0.17.3.2.tar.bz2, 8e311714e97f2ac87bfd818abd5c4c605ca19ebda84a1edea93ec00a89d07e2e
monero-linux-armv7-v0.17.3.2.tar.bz2, 76c101db6df7d923ab4cff074a0368e41dbc532b65f99ac983da2f1a199b4423
monero-android-armv8-v0.17.3.2.tar.bz2, c9cfb2eaace60a2436f9b8db8a0fa6f2ae4318016d4e3fce1bd7ba5def2aeb97
monero-android-armv7-v0.17.3.2.tar.bz2, 4dab5307d4635d2f18278fff09e54c24d89f5e4582fb77a2e5dea9733868c092
monero-freebsd-x64-v0.17.3.2.tar.bz2, 097e72be2eca2944414ee0551ae9d9b560605ce208cd016cc3db24944407db91
```

A GPG-signed list of the hashes is at [https://getmonero.org/downloads/hashes.txt](https://getmonero.org/downloads/hashes.txt) and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys). To ensure that the files you download are those originally posted by the maintainers, you should both check that the hashes of your files match those on the signed list, and that the signature on the list is valid.