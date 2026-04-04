---
title: Monero GUI forgets some of its configuration
source_url: https://github.com/monero-project/monero-gui/issues/3948
author: usernamesaredumb2
assignees: []
labels: []
created_at: '2022-06-18T14:04:28+00:00'
updated_at: '2022-09-02T20:15:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Monero GUI v0.17.3.2 today greeted me with a dark theme (ouch!) and started to sync at block 0 (double ouch!).
I have used 0.17.3.2 before, so there shouldn't be any changes upon a restart.
It seems to have forgotten some configuration settings, but not all. The wallet location was still correct and it was properly opened. The blockchain location was reset to default, where it couldn't be found, obviously. I don't know if/what other settings were affected.
There's plenty of space left on the drive, so this shouldn't be the cause as suggested in issue #3929.
OS is Debian 11.

# Discussion History
## selsta | 2022-06-21T17:29:18+00:00
I need some more information. How did you install the GUI (website, flatpak, package manager)? Did you ever set it to portable mode?

## usernamesaredumb2 | 2022-06-24T06:54:20+00:00
I downloaded the tar from the website and the updates suggested by Monero GUI at startup from time to time. Just unpacked those tars in a local directory in user home and started the new binary. Never had any problems until the last update (and the settings were not forgotten upon the first start after the update, but upon a subsequent start).
I don't know about portable mode so no, probably haven't set it to.

## usernamesaredumb2 | 2022-09-02T05:53:36+00:00
It has just happened again in v0.18.1.0.

## rating89us | 2022-09-02T20:15:10+00:00
I also experienced this problem, but with v0.18.0.0, not yet with v0.18.1.0.
I opened Monero GUI, it opened correctly my previous wallet, but it had forgotten the custom blockchain location, so it started to sync it from scratch using the default blockchain folder. I then closed Monero GUI and opened it again, and strangely the custom blockchain location was now correct again.

# Action History
- Created by: usernamesaredumb2 | 2022-06-18T14:04:28+00:00
