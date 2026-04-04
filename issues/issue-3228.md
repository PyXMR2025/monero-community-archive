---
title: monero-gui 'Daemon log' not using remote node (ever)
source_url: https://github.com/monero-project/monero-gui/issues/3228
author: alberto-fc
assignees: []
labels: []
created_at: '2020-11-12T00:51:34+00:00'
updated_at: '2021-01-24T12:01:32+00:00'
type: issue
status: closed
closed_at: '2021-01-22T04:42:00+00:00'
---

# Original Description
monero-wallet-gui configured to use a remote node (outside the LAN network) didn't route the commands to the remote node.

You can see that every command entered in the GUI is pushed to the monerod binary (```<monerod binary> <command>```):

```
DEBUG	frontend	src/wallet/api/wallet.cpp:404	sending external cmd:  ("status")
DEBUG	frontend	src/wallet/api/wallet.cpp:404	showing status message
```

```
>>> status
[12/11/2020 1:30] 2020-11-12 00:30:22.809 I Monero 'Oxygen Orion' (v0.17.1.3-release) 
Error: Couldn't connect to daemon: 127.0.0.1:18081
```

As far as I can see, there is no way to command monerod (using arguments nor the config file) to use a remote node for the RPC callings (or anything else, aka ZMQ). So even passing arguments to the monerod binary, the GUI will never read (nor show) the responses from the remote node in the 'Daemon log' dialog.

Another parallel consequence of this, you can delete the monerod binary from the GUI folder (at least using the Window version), the GUI will never show a message about the missing file, just timeout the external command without any trace about the missing binary.

![image](https://user-images.githubusercontent.com/5665863/98880994-4ca60400-2489-11eb-8283-9b56cf6a70e5.png)



# Discussion History
## xiphon | 2021-01-15T11:27:01+00:00
`Log` tab is not meant to be used in Remote Node mode, Will be fixed via https://github.com/monero-project/monero-gui/pull/3309 PR.

## alberto-fc | 2021-01-24T12:01:32+00:00
Mice job @luigi1111, simple and elegant. Like it.

Sorry for the extra work but Thank you.

# Action History
- Created by: alberto-fc | 2020-11-12T00:51:34+00:00
- Closed at: 2021-01-22T04:42:00+00:00
