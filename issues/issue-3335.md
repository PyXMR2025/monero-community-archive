---
title: '[solved] Segmentation fault with monero-wallet-gui'
source_url: https://github.com/monero-project/monero-gui/issues/3335
author: HoverHalver
assignees: []
labels: []
created_at: '2021-02-11T09:53:59+00:00'
updated_at: '2021-02-12T11:03:34+00:00'
type: issue
status: closed
closed_at: '2021-02-12T11:03:33+00:00'
---

# Original Description
Hello,
I have downloaded and gpg verified Monero GUI wallet v0.17.1.9 linux 64 bits on a Debian Buster Gnome 3.30.2 machine.
`./monerod` is working fine.
But` ./monero-wallet-gui` provokes immediately a "segmentation fault" message.
And there is nothing in the log files (even in /var/log).
I suspect this may have to do with the screen used (the DPI ?).
Even  `./monero-wallet-gui --help` provokes immediately a "segmentation fault" message.
Could somebody please give me some hint or directions on what I could do to fix this ?
Thanks

edit :
I tried `gdb ./monero-wallet-gui`
and the answer is : `not in executable format: file truncated`
... it appears that there must have been an issue when copying the file on its place. It got indeed completely truncated.

Getting the right file, it works.
Apologies for the annoyance.

# Discussion History
## selsta | 2021-02-12T11:03:33+00:00
Seems resolved.

# Action History
- Created by: HoverHalver | 2021-02-11T09:53:59+00:00
- Closed at: 2021-02-12T11:03:33+00:00
