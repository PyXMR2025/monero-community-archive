---
title: 'monero-wallet-cli: using a config file with "password=" is causing inactivity
  lock to misbehave, unable to unlock'
source_url: https://github.com/monero-project/monero/issues/9258
author: Robert-Riedl
assignees: []
labels:
- invalid
- wontfix
- upstream bug
created_at: '2024-03-20T12:48:24+00:00'
updated_at: '2024-03-22T02:59:50+00:00'
type: issue
status: closed
closed_at: '2024-03-22T02:59:50+00:00'
---

# Original Description
v0.18.3.2 for armv7

reproduce :

`./monero-wallet-cli --config-file file.cfg`

`password=<password>` set in `file.cfg`

The wallet startup works fine but then, either wait for the inactivity lock or just type `lock`

Your console will be spammed endlessly, multiple times per second, no chance to input anything :

```
The wallet password is required to unlock the console.
Wallet password: Error: failed to read wallet password
```


# Discussion History
## Robert-Riedl | 2024-03-20T13:16:10+00:00
okay this is not a monero-wallet-cli bug, this is an issue with how SCREEN und bash are handeling things, especially `tty`

so instead of

```
/usr/bin/screen -S monero -dm /usr/bin/bash -c "./monero-wallet-cli --config-file file.cfg"
```

which doesn't get a `tty` because of `-c` we have to wrap the cli command in a script because  SCREEN can't parse arguments for the cli (this throws a "file not found" error)

so `script.sh` looks like

```
#!/bin/bash
/absolute/path/monero-wallet-cli --config-file /absolute/path/file.cfg
```
and is called like this

```
/usr/bin/screen -S monero -dm "/absolute/path/script.sh"
```

#5922 and #5719 pointed me in the right direction

## 0xFFFC0000 | 2024-03-22T02:59:44+00:00
Closing this issue as the original author states has found the root issue in another software. 

# Action History
- Created by: Robert-Riedl | 2024-03-20T12:48:24+00:00
- Closed at: 2024-03-22T02:59:50+00:00
