---
title: Wallet "invalid password" after changing initial block height
source_url: https://github.com/monero-project/monero-gui/issues/1081
author: Neozaru
assignees: []
labels:
- resolved
created_at: '2018-01-16T13:41:35+00:00'
updated_at: '2018-03-30T00:54:20+00:00'
type: issue
status: closed
closed_at: '2018-03-30T00:54:20+00:00'
---

# Original Description
**OS :** Archlinux x86_64
**Kernel :** 4.13.8-1-ARCH
**Branch** : master (3b069ec04908f76b8244a96124ce9619c0b0300d)

Summary : Error message "Could open wallet, invalid password" after changing wallet initial block height and closing/reopening.


Steps to reproduce :
- Create new wallet with name "neozaru5".
- Set password "barbarbar".
- Choose to connect to a remote node.
- Wait for connect and quick sync.
- Go Settings > Change creation block to "1" (should freeze some seconds before going back to wallet view)
- Close the window (should freeze some seconds before actually closing)
- Open again, and enter the password for your wallet
--> You get "wrong password" error message

EDIT : I didn't investigate technically speaking but entering no password seems to do the trick. So I assume that when *wallet creation height* is edited, a new wallet file is created, but not encrypted again (which would make sense since the GUI doesn't ask for any password before changing this parameter). 
EEDIT : Finally investigated.

Wallet files after create, after changing height, and after closing the GUI :
[debugNeozaruAfterClosing.zip](https://github.com/monero-project/monero-gui/files/1635279/debugNeozaruAfterClosing.zip)

Full console log : https://pastebin.com/2dkDYQF6

# Discussion History
## sanderfoobar | 2018-03-30T00:17:42+00:00
Assuming resolved, as there was a PR. If not, please re-open. (and thanks for reporting!)

## sanderfoobar | 2018-03-30T00:17:47+00:00
+resolved

# Action History
- Created by: Neozaru | 2018-01-16T13:41:35+00:00
- Closed at: 2018-03-30T00:54:20+00:00
