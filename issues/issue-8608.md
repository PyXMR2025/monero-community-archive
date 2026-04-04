---
title: Error with shared libraries
source_url: https://github.com/monero-project/monero/issues/8608
author: ChervonaKomanda
assignees: []
labels: []
created_at: '2022-10-11T01:10:41+00:00'
updated_at: '2023-06-06T01:34:19+00:00'
type: issue
status: closed
closed_at: '2023-06-06T01:34:19+00:00'
---

# Original Description
Fresh install of Debian 11

> Downloaded the linux tar.bz2 from Monero website
` tar xf monero-gui-linux-x64-v0.18.1.2.tar.bz2`
` ./monero-wallet-gui`
` ./monero-wallet-gui: error while loading shared libraries: libxcb-icccm.so.4: cannot open shared object file: No such file or directory`

# Discussion History
## selsta | 2022-10-11T01:14:24+00:00
Try to install

```
libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-xkb1 libxcb-shape0 libxkbcommon-x11-0
```

These should come preinstalled unless you installed an OS without any graphical user interface.

## lispydev | 2023-05-02T11:48:17+00:00
I was able to reproduce the error with a Ubuntu 22 LTS minimal install, after extracting the .tar.bz2:
./monero-wallet-gui./monero-wallet-gui: error while loading shared libraries: libxcb-icccm.so.4: cannot open shared object file: No such file or directory

Installing the libraries fixed it. The missing libraries were:
libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 libxcb-xkb1 libxkbcommon-x11-0

# Action History
- Created by: ChervonaKomanda | 2022-10-11T01:10:41+00:00
- Closed at: 2023-06-06T01:34:19+00:00
