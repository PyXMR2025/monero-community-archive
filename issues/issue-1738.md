---
title: Error opening wallet in Windows GUI
source_url: https://github.com/monero-project/monero-gui/issues/1738
author: G-Bigo
assignees: []
labels:
- resolved
created_at: '2018-11-12T13:15:22+00:00'
updated_at: '2018-11-18T12:36:22+00:00'
type: issue
status: closed
closed_at: '2018-11-18T12:36:22+00:00'
---

# Original Description
The Windows x64 GUI wallet contains a massive bug. It is impossible to re-open a wallet.

Situation: 
• Open program first time
• Choose language (German for me)
• Create a wallet
• Choose a password (in my case containing spaces)
• Start service
• Sync blockchain
  (Everything standard up to here)
• Close program
• Re-open program
• Enter password
• Wallet couldn't be opened: basic_string::_M_replace_aus

The same happens when trying to open the (definitely existing) wallet from a file.

When restarting the whole process and creating a new wallet the wallet specs show a possible reason:
The alleged location (on a windows system!) alway ends with something like (without quotation marks)
'/username/username'
I.e. the windows path contains slashes (instead of backslashes), which of course must evoke an error. Seems like some Linux code splashed over unaltered.

I don't know whether the slashes within the wallet file path actually are the reason for the described bug. Anyway, the procedure described above reproducible yields the wallet open error.

# Discussion History
## dEBRUYNE-1 | 2018-11-13T18:25:32+00:00
Which version are you using? Because this particular bug is supposedly fixed in GUI v0.13.0.4, which can be found here:

https://www.reddit.com/r/Monero/comments/9ti2on/gui_v01304_beryllium_bullet_released/

## G-Bigo | 2018-11-13T21:21:09+00:00
I first run into this issue with version 0.13.0.3, then downloaded 0.13.0.4 to see whether it works. And no, nothing is fixed in v0.13.0.4 — exactly the 'Can't open wallet' error described above.

## dEBRUYNE-1 | 2018-11-14T08:52:03+00:00
@G-Bigo - You will, after upgrading to GUI v0.13.0.4, still have to remove the wallet cache once. Thereafter it should work properly though. 

## dEBRUYNE-1 | 2018-11-18T11:11:21+00:00
Ping @G-Bigo - Did you manage to resolve your issue?

## G-Bigo | 2018-11-18T11:14:58+00:00
Yepp, deleting old wallet, restoring (aka recreating) it with mnemonic phrase, re-synching wallet. No it works as expected. Thanks.

## erciccione | 2018-11-18T12:35:22+00:00
+resolved

# Action History
- Created by: G-Bigo | 2018-11-12T13:15:22+00:00
- Closed at: 2018-11-18T12:36:22+00:00
