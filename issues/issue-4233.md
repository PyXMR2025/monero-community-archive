---
title: start of monerod gives "Segmentation fault (core dumped)" on Archlinux
source_url: https://github.com/monero-project/monero-gui/issues/4233
author: ZombB
assignees: []
labels: []
created_at: '2023-10-22T10:41:28+00:00'
updated_at: '2023-11-04T20:08:51+00:00'
type: issue
status: closed
closed_at: '2023-11-04T20:08:51+00:00'
---

# Original Description
When the monerod daemon is started on Archlinux it segfaults every time. I have attached the shelloutput when trying to start the daemon manually and the logfile that is produced.

[monero.log](https://github.com/monero-project/monero-gui/files/13062957/monero.log)
[shelloutput.log](https://github.com/monero-project/monero-gui/files/13062958/shelloutput.log)

This bug first appeared on Monero 'Fluorine Fermi' (v0.18.2.2-release)

This is my Linux kernel version: 6.5.8-arch1-1

# Discussion History
## selsta | 2023-10-22T13:03:43+00:00
How did you install monerod? Package manager or binary from the website?

What is /mnt/ ? A network drive or an external HDD? Did you sync up partially before it started to segfault?

## ZombB | 2023-10-22T20:20:31+00:00
Hi selsta,

monerod was installed using the package manager which is pacman on Archlinux. So this affects the official monero Archlinux package: https://archlinux.org/packages/extra/x86_64/monero/

/mnt/ is a local harddrive on the PC. Precisely it is an ext4 filesystem on a raid 5 array.

## selsta | 2023-10-22T20:22:22+00:00
Did you sync up partially before it started to segfault? Or did this segfault show up instantly on first start and monerod never worked before?

## ZombB | 2023-10-23T12:58:36+00:00
Hi selsta,

yes, I synced up before. I ran monero as a full node since 2017 on this machine and the node was fully synced up. Then suddenly the daemon did not get started during boot. 

So it was synced up before.
I then updated to Monero 'Fluorine Fermi' (v0.18.2.2-release) using the regular Archlinux updates with the distros standard package manager pacman. And it synced up again.
Then from one day to another it stopped working. The daemon did not start. This problem persists also with the succeeding updates of the package.

## ZombB | 2023-11-04T20:08:51+00:00
duplicate of #9055 https://github.com/monero-project/monero/issues/9055

# Action History
- Created by: ZombB | 2023-10-22T10:41:28+00:00
- Closed at: 2023-11-04T20:08:51+00:00
