---
title: Duplicate port displayed
source_url: https://github.com/monero-project/monero/issues/3867
author: muff1nman
assignees: []
labels:
- invalid
created_at: '2018-05-26T21:18:56+00:00'
updated_at: '2018-05-27T10:56:52+00:00'
type: issue
status: closed
closed_at: '2018-05-27T10:56:52+00:00'
---

# Original Description
```
$ ../../0.12.1.0/monero-wallet-cli --daemon-host hostname:18081
2018-05-26 21:15:41.077	    7ffbf9acf100	WARN 	global	src/common/util.cpp:611	Running with glibc 2.25, hangs may occur - change glibc version if possible
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on an another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Lithium Luna' (v0.12.1.0-master-release)
Logging to ../../0.12.1.0/monero-wallet-cli.log
Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
Wallet file name (or Ctrl-C to quit): local
Wallet and key files found, loading...
Wallet password: 
Opened wallet: XXX
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Warning: using an untrusted daemon at http://hostname:18081:18081, privacy will be lessened
Starting refresh...
```

Note that the port is shown twice - the refresh still works fine however.

# Discussion History
## stoffu | 2018-05-27T04:18:23+00:00
The `--daemon-host` option is supposed to be given only the host name, like node.moneroworld.com. The port number should be given via `--daemon-port`. Or use `--daemon-address` if you want to use the `<hostname>:<port>` format.


## dEBRUYNE-1 | 2018-05-27T10:50:20+00:00
+invalid 

# Action History
- Created by: muff1nman | 2018-05-26T21:18:56+00:00
- Closed at: 2018-05-27T10:56:52+00:00
