---
title: '[UI/UX] Settings "Blockchain location" and "Daemon startup flags" should reconcile
  use of data-dir flag'
source_url: https://github.com/monero-project/monero-gui/issues/1670
author: xbkingx
assignees: []
labels: []
created_at: '2018-10-16T20:32:14+00:00'
updated_at: '2020-06-14T22:44:11+00:00'
type: issue
status: closed
closed_at: '2020-06-14T22:44:11+00:00'
---

# Original Description
(on Windows, but may be a general issue) 

Current behavior: Setting the "Blockchain location" (BL) setting to a new directory while also changing "Daemon startup flags" (DSF) to include `--data-dir=<same directory>`  results in monero-gui failing to start monerod. The terminal appears briefly and closes (looks like it prints the help command briefly, but too fast for me to tell).

Windows specific sub-issue: The DSF converts Windows paths with spaces to the short/DOS/8.3 format, while BL doesn't. If this wasn't the case, you could just compare the two values to make sure they're equal and discard one as duplicate.

Desired behavior:  Two options to address this.

The easiest, least error-prone way to display this would be to hide the DSF setting behind a selectable UI element, like a checkbox or section fold, and when the "View DSF" option is enabled, the value from BL is copied to the DSF in the data-dir format, while disabling the BL editable section. If the checkbox is de-selected, check for the data-dir argument in DSF and if it exists, copy it back to BL. If it doesn't, clear BL.

Second possibility would be to remove the editable text field from BL and have 2 buttons: Set new location and Clear. Setting a new location adds the data-dir command/value to the DSF.


Edit: Forgot to add the current solution I'm using. Clear DSF and only use BL. 

Steps (if not run as admin): Change values in monero-gui, close monero-gui and any other monero wallet processes, open Regedit, search for `monero-core` should be  `HKEY_USERS\S-#-#-#-#######-########-########-####\Software\monero-project`, where # varies), delete the data from `daemonFlags`.

Note that the blockchainDataDir data will have the normal/long path format and no quotes.

# Discussion History
## selsta | 2020-06-14T22:44:11+00:00
AFAIK this is now resolved.

# Action History
- Created by: xbkingx | 2018-10-16T20:32:14+00:00
- Closed at: 2020-06-14T22:44:11+00:00
