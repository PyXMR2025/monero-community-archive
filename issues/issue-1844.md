---
title: '[Suggestion] Monero-GUI wallet settings add-ins/ons'
source_url: https://github.com/monero-project/monero-gui/issues/1844
author: SBSeed
assignees: []
labels:
- invalid
created_at: '2018-12-19T08:29:02+00:00'
updated_at: '2019-02-08T14:54:34+00:00'
type: issue
status: closed
closed_at: '2019-02-08T14:54:34+00:00'
---

# Original Description
support to use blockchain.raw from within the gui wallet, bypassing CMD/CLI
support to change blockchain saves minimum/maximum size files:
- set minimum size as 1gb or something as default...
- set maximum size as 10gb as default (higher/lower depending on if hard drive is SSD or HDD and max access run speeds)...

- support for deamon to run within Monero-GUI
- set optional start-up commands saved within the GUI

use of 'safe' - redesigned to use last good blockchain datapoint use save file for last datapoint verified and start point (if something does go wrong)...
in-program help database, potentially create as an addition to safe run commands to automatically save crash report or open ticket.

integration of all separate .exe files directly into the GUI so deamon (monerod.exe), and others, do not run separately from the monero application itself (probably not even remotely possible at this point but i thought i would throw this in here).

# Discussion History
## sanderfoobar | 2019-02-08T14:23:44+00:00
> support to use blockchain.raw from within the gui wallet

I do not understand what you mean.

> set maximum size as 10gb as default (higher/lower depending on if hard drive is SSD or HDD and max access run speeds).

Maximum size of what? The blockchain? No.

> support for deamon to run within Monero-GUI

'within' the GUI? I do not follow.

> set optional start-up commands saved within the GUI

This is possible, please consult Settings->Daemon to tweak `monerod` startup flags.

> use of 'safe' - redesigned to use last good blockchain datapoint use save file for last datapoint verified and start point (if something does go wrong)

This is a good suggestion, I tried adding this in #1920 but after talking about it with other developers, we concluded the performance impact would be too severe. It would take the 'l' out of [lmdb](https://en.wikipedia.org/wiki/Lightning_Memory-Mapped_Database), so to speak :-)

> integration of all separate .exe files directly into the GUI so deamon (monerod.exe), and others, do not run separately from the monero application itself

We do not have any plans on embedding multiple executables into one executable. We see no point.

+invalid

# Action History
- Created by: SBSeed | 2018-12-19T08:29:02+00:00
- Closed at: 2019-02-08T14:54:34+00:00
