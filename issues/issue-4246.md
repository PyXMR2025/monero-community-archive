---
title: More flexible p2pool installation scenarios on Linux
source_url: https://github.com/monero-project/monero-gui/issues/4246
author: akiross
assignees: []
labels: []
created_at: '2023-11-18T16:07:16+00:00'
updated_at: '2024-03-29T10:47:55+00:00'
type: issue
status: closed
closed_at: '2024-03-29T10:47:55+00:00'
---

# Original Description
Hello,
I recently started exploring monero, got a GUI wallet working and I tried to mine using p2pool. I'm running NixOS (Linux), so I've got both monero-wallet-gui and p2pool nicely packaged in my distro's collection and I can have both of them working and available in my `PATH`.

I wanted to go on and use the nice GUI that is available in the wallet to start the miner, but it won't work. There are two issues:

1. monero-gui [will look](https://github.com/monero-project/monero-gui/blob/e9cd4588aef3f0808ce153957a504f43dcdbeb26/src/p2pool/P2PoolManager.cpp#L246) for p2pool in the same [directory of it's executable](https://doc.qt.io/qt-6/qcoreapplication.html#applicationDirPath), but it's not there
2. the root filesystem is read-only, so trying to install p2pool alongside the application executable will not work.

This could be fixed in a few ways:

1. search `p2pool` in the `PATH` and use that if present, before installing another one;
2. install p2pool in user's home directory (XDG_DATA_HOME or XDG_CACHE_HOME I think);
3. fallback to logging a message of the p2pool command to use, like
    > I failed to start p2pool, but you can run it by yourself using this command:
    > p2pool --host 127.0.0.1 ...

I think that looking for p2pool executable in `PATH` is the most idiomatic way to use an external executable and it's preferable to downloading it. What do you think? I'm familiar with Qt so I could even work on a small PR on this.

# Discussion History
## Rikj000 | 2023-11-20T19:58:54+00:00
Hi @akiross

I opened a possible duplicate a while ago, with a proposed fix written out here: https://github.com/monero-project/monero-gui/issues/4108#issuecomment-1416711920

# Action History
- Created by: akiross | 2023-11-18T16:07:16+00:00
- Closed at: 2024-03-29T10:47:55+00:00
