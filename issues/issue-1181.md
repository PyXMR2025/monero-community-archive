---
title: Standard log location (Linux & Android)
source_url: https://github.com/monero-project/monero-gui/issues/1181
author: pazos
assignees: []
labels:
- feature
created_at: '2018-03-14T18:01:54+00:00'
updated_at: '2018-05-11T21:58:16+00:00'
type: issue
status: closed
closed_at: '2018-05-11T21:58:16+00:00'
---

# Original Description
For monero-wallet-gui the logfile is in the same folder as the binary. This is great when running the GUI from its folder (ie: static build) but a bad choice If I want to run the GUI from /usr/bin, /usr/local/bin, where the user running the binary doesn't have permissions to write at those folders.

Using a standard location, like $HOME/.monero/monero-wallet-gui.log as a fallback would be great.

# Discussion History
## pazos | 2018-03-14T20:18:07+00:00
About android I'm not sure if the log should be saved in AppDataLocation (/data/data/monero..) or somewhere in external storage, like DocumentsLocation  /storage/emulated/0/Documents..)

The latter requires request for permission WRITE_EXTERNAL_STORAGE.

The former doesn't require permissions and it is compatible with IOS. 

## sanderfoobar | 2018-03-29T23:15:16+00:00
+feature

## pazos | 2018-04-01T20:50:21+00:00
It seems that changing Wallet::getWalletLogPath() in src/libwalletqt/Wallet.cpp don't make any difference and the log is still created in the same dir as the binary.

@skftn: any hint on this?

## sanderfoobar | 2018-04-01T21:42:24+00:00
No clue, unfortunately. Perhaps try in #monero-dev or the GUI channel on Freenode.

# Action History
- Created by: pazos | 2018-03-14T18:01:54+00:00
- Closed at: 2018-05-11T21:58:16+00:00
