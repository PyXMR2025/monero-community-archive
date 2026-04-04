---
title: Application uses too many Unix sockets on Linux, causing issues with X11
source_url: https://github.com/monero-project/monero-gui/issues/3324
author: Wyatt915
assignees: []
labels: []
created_at: '2021-02-02T00:05:02+00:00'
updated_at: '2021-03-05T18:58:10+00:00'
type: issue
status: closed
closed_at: '2021-03-05T18:58:10+00:00'
---

# Original Description
Every time `monero-gui` locks after a period of inactivity, it uses an additional 2 Unix sockets. When a password is entered to unlock the gui, an additional 32 sockets are used. This will continue until no more sockets can be opened, causing other apps (especially X11, resulting in the message `cannot open display: :0.0 Maximum number of clients reached`) to misbehave if a socket is needed.

This can be tested by running `lsof -U +c 15 | cut -f1 -d' ' | uniq -c | grep monero-wallet` while the app is open. Each time an unlock is required, run the command and it will show an increase of 32 open sockets.

I am running Arch Linux (kernel 5.10.11), and have installed monero-wallet-gui from the default repos.

GUI version: 0.17.1.9-3ca5f10f (Qt 5.15.2)
Embedded Monero version: 0.17.1.9-release
Wallet mode: Advanced mode (Local node)OpenGL

# Discussion History
## selsta | 2021-02-02T00:06:29+00:00
Please test if you have the same behavior with the getmonero.org binaries.

## Wyatt915 | 2021-02-02T00:34:53+00:00
Just tested it with the `monero-wallet-gui` binary and found it to have the same issue. I did not try the AppImage.

## xiphon | 2021-02-03T11:15:15+00:00
Located the issue. Will submit a fix in a few.

## Wyatt915 | 2021-02-03T16:23:21+00:00
Gotta love a one-line fix :)

# Action History
- Created by: Wyatt915 | 2021-02-02T00:05:02+00:00
- Closed at: 2021-03-05T18:58:10+00:00
