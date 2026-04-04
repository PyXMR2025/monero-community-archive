---
title: start of monerod gives "Segmentation fault (core dumped)" on Archlinux
source_url: https://github.com/monero-project/monero/issues/9055
author: ZombB
assignees: []
labels: []
created_at: '2023-11-04T20:07:12+00:00'
updated_at: '2023-11-11T14:22:04+00:00'
type: issue
status: closed
closed_at: '2023-11-11T14:20:55+00:00'
---

# Original Description
When the monerod daemon is started on Archlinux it segfaults every time. I have attached the shelloutput when trying to start the daemon manually and the logfile that is produced.

[monero.log](https://github.com/monero-project/monero/files/13257610/monero.log)
[shelloutput.log](https://github.com/monero-project/monero/files/13257611/shelloutput.log)

This bug first appeared on Monero 'Fluorine Fermi' (v0.18.2.2-release)

This is my Linux kernel version: 6.5.8-arch1-1

monerod was installed using the package manager which is pacman on Archlinux. So this affects the official monero Archlinux package: https://archlinux.org/packages/extra/x86_64/monero/

/mnt/ is a local harddrive on the PC. Precisely it is an ext4 filesystem on a raid 5 array.

I ran monero as a full node since 2017 on this machine and the node was fully synced up. Then suddenly the daemon did not get started during boot.

When I  updated to Monero 'Fluorine Fermi' (v0.18.2.2-release) using the regular Archlinux updates with the distros standard package manager pacman. And it synced up again.
Then from one day to another it stopped working. The daemon did not start. This problem persists also with the succeeding updates of the package.

@ketiv17 has recently filed a similar bug https://github.com/monero-project/monero/issues/9054

_*** by mistake this issue was initially filed under monero-gui, see https://github.com/monero-project/monero-gui/issues/4233 but actually it is not monero-gui instead it is the monero package and I am using monero-cli ***_


# Discussion History
## selsta | 2023-11-05T01:21:59+00:00
Did you lose access to the storage at some point during sync? E.g. power outtage or other reason it would unmount?

Do you have a backup of the blockchain or file are you able to sync up from scratch again? To me it looks like a corrupted blockchain but it's difficult to say why it happened.

## LevitatingBusinessMan | 2023-11-11T01:47:28+00:00
I have had this issue occur with a corrupted blockchain.

## ZombB | 2023-11-11T14:22:04+00:00
Thank you for the hint. I synced up from scratch again and now everything works again. Closing this issue.

# Action History
- Created by: ZombB | 2023-11-04T20:07:12+00:00
- Closed at: 2023-11-11T14:20:55+00:00
