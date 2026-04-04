---
title: Can't run Linux x64 binaries on Arch Linux x64
source_url: https://github.com/monero-project/monero-gui/issues/1253
author: MaxXor
assignees: []
labels: []
created_at: '2018-04-04T06:38:05+00:00'
updated_at: '2018-07-12T01:49:31+00:00'
type: issue
status: closed
closed_at: '2018-04-22T13:24:59+00:00'
---

# Original Description
Trying to run `monero-wallet-gui` fails with:
> ./monero-wallet-gui: error while loading shared libraries: **libpcsclite.so.1**: cannot open shared object file: No such file or directory

GUI v0.11.1.0 was working fine, seems like some dependency is messed up.

I'm using the binaries from here: https://github.com/monero-project/monero-gui/tree/v0.12.0.0

# Discussion History
## stevesbrain | 2018-04-04T06:46:03+00:00
Does it change if you install pcsclite?

## MaxXor | 2018-04-04T06:49:01+00:00
Yes, then it is starting. Why this new dependency on "PC/SC Architecture smartcard middleware library"?

## stevesbrain | 2018-04-04T06:50:40+00:00
@MaxXor My expectation would be possible use with the Ledger Nano S when it comes about, but I don't know if this is why or not. Glad to hear that resolves it :) P.S. you can always build from [the AUR package](https://aur.archlinux.org/packages/monero-gui-bin/) if that helps :)

## MaxXor | 2018-04-04T06:54:09+00:00
Ah, that seems to be the reason for the new dependency.

## tumbi-j | 2018-07-05T05:49:43+00:00
@stevesbrain Hi i am having this issue as well. How do i install the pcsclite you talked about

## stevesbrain | 2018-07-12T01:49:30+00:00
@tummybos Should just be a case of `pacman -S pcsclite` - let us know if you have issues beyond that :)

# Action History
- Created by: MaxXor | 2018-04-04T06:38:05+00:00
- Closed at: 2018-04-22T13:24:59+00:00
