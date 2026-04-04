---
title: Default new wallet directory path on Linux
source_url: https://github.com/monero-project/monero-gui/issues/59
author: peronero
assignees: []
labels: []
created_at: '2016-10-13T20:59:13+00:00'
updated_at: '2016-11-13T17:59:28+00:00'
type: issue
status: closed
closed_at: '2016-11-13T17:59:28+00:00'
---

# Original Description
Currently, for Linux, the default new wallet directory is set to 'homedir/Monero Accounts', which is not ideal for many reasons - chiefly that it pollutes the user's home directory, that there is a space in the name, and perhaps even that it unnecessarily exposes sensitive files which would not be regularly used by the same typical novice user that also wouldn't choose a path other than the one set as default.

Suggest setting the default directory for new wallets to '$monerodir/wallet' where $monerodir is currently .bitmonero as first option, or where the GUI binary is located as a second option.

Further suggest looping into a greater discussion about the organization of .bitmonero, which is understood to be in the process of being renamed to .monero, particularly with regard to compartmentalizing/future-proofing the directory structure - currently it is devoted to containing blockchain-related files only, which could be moved to '.monero/blockchain' allowing for the wallets directory to neatly coexist, and also for a 'testnet' directory and whatever other needs arise down the road.

Unsure as to what the current or optimal behaviors are on other platforms but perhaps they should be reviewed as well.

Also, the default directory 'Monero Accounts'  seems to be created when monero-core is initialized and is not removed if a different location is chosen.


# Discussion History
## peronero | 2016-10-27T18:45:12+00:00
Paragraph appended about non-removal of 'Monero Accounts' directory.


## Jaqueeee | 2016-10-30T20:23:39+00:00
changed default location to $HOME/Monero/wallets and removed auto creation in https://github.com/monero-project/monero-core/pull/93
Each wallet will get an own subdir as before. 


## medusadigital | 2016-11-06T09:20:40+00:00
can be closed 


## fluffypony | 2016-11-13T17:59:28+00:00
Closing as fixed


# Action History
- Created by: peronero | 2016-10-13T20:59:13+00:00
- Closed at: 2016-11-13T17:59:28+00:00
