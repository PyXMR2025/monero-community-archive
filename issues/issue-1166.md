---
title: Document how to uninstall the GUI on Linux
source_url: https://github.com/monero-project/monero-gui/issues/1166
author: Bomper
assignees: []
labels:
- help wanted
created_at: '2018-03-06T11:47:09+00:00'
updated_at: '2018-04-07T12:06:30+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I see a [Windows installer README](https://github.com/monero-project/monero-gui/blob/master/installers/windows/README.md), but nothing for Linux. Is it sufficient to delete `~/.bitmonero` in addition to the `monero-gui-vx.x.x.x` directory?

# Discussion History
## sanderfoobar | 2018-03-29T23:26:21+00:00
For those that come here via Google, the relevant paths are:

- `~/.bitmonero/` - blockchain
- `~/.config/monero-project/` - GUI config
- `~/Monero/` - default wallet location (careful)

Please note that when creating a wallet from the CLI, it'll be saved in the same folder as the binary.

## sanderfoobar | 2018-03-29T23:27:23+00:00
+help wanted

## ghost | 2018-04-07T04:06:30+00:00
I am new to Monero but I think ~/.Monero/ is meant to be ~/Monero/ for the default wallet location (for monero-gui-v0.12.0.0 at least)

If a Linux user is unsure (for now) then running the following command in terminal should find any directories with a max depth of 2 that contain the string "monero"

`find . -maxdepth 2 -type d -iname "*monero*" -print`

Outputs the following

- ~/monero-gui-vx.xx.x.x - Monero downloaded package location
- ~/Monero/ - default wallet location (careful)
- ~/.config/monero-project/ - GUI config
- ~/.bitmonero/ - default blockchain location

# Action History
- Created by: Bomper | 2018-03-06T11:47:09+00:00
