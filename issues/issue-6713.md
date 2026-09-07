---
title: Faulty behaviour with monero-wallet-cli in certain terminal emulators
source_url: https://github.com/monero-project/monero/issues/6713
author: Parckwart
assignees: []
labels: []
created_at: '2020-07-19T13:37:51+00:00'
updated_at: '2026-09-05T09:52:32+00:00'
type: issue
status: closed
closed_at: '2026-09-05T09:52:32+00:00'
---

# Original Description
When using monero-wallet-cli with certain terminal emulators such as urxvt or suckless' st, text formatting is all messed up. There's faulty whitespace all over the place, CTRL+L to clear the terminal doesn't work and you cannot delete characters using backspace either. This doesn't happen with xterm for example.

Screenshot:

![screenshot-2020-07-19-15-34-45](https://user-images.githubusercontent.com/8195243/87876066-eb7f8f80-c9c4-11ea-8841-a6fa1df83263.png)


# Discussion History
## moneromooo-monero | 2020-07-19T14:41:38+00:00
Do other readline using programs generally work ?

## Parckwart | 2020-07-19T16:38:12+00:00
Yes, I think so…

Things like bc and parted all work perfectly fine.

## Parckwart | 2021-03-05T22:47:56+00:00
Found a workaround: Setting $TERM to "xterm" did the trick.

## selsta | 2026-09-05T09:52:32+00:00
This might work better in the future once we move from readline to linenoise.

# Action History
- Created by: Parckwart | 2020-07-19T13:37:51+00:00
- Closed at: 2026-09-05T09:52:32+00:00
