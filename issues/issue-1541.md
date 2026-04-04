---
title: Mac can't open monero-wallet-gui
source_url: https://github.com/monero-project/monero-gui/issues/1541
author: KPWorkspace
assignees: []
labels: []
created_at: '2018-08-16T09:41:03+00:00'
updated_at: '2018-08-22T07:38:06+00:00'
type: issue
status: closed
closed_at: '2018-08-22T07:38:06+00:00'
---

# Original Description
Mac ： 10.12.6
monero-wallet-gui ： 0.12.3.0 Lithium Luna.
![image](https://user-images.githubusercontent.com/19641227/44201306-8210f980-a17b-11e8-8439-46942ecd92f1.png)

The prompt for console is
```
com.apple.xpc.launchd.oneshot.0x10000013.monero-wallet-gui[14784]): Could not find and/or execute program specified by service: 2: No such file or directory: /private/var/folders/fr/0sn549vn75zgbwc7y0rjlg400000gp/T/AppTranslocation/B3601126-6939-41B1-929B-D757D1C57EBD/d/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
```

# Discussion History
## sanderfoobar | 2018-08-16T13:11:42+00:00
Try

`defaults write com.apple.LaunchServices LSQuarantine -bool true`

Be aware I found this online - I don't know the exact implications of running this command.

## KPWorkspace | 2018-08-17T01:58:42+00:00
@skftn Thank you, I tried this method, but it seems to be useless.
I solved this exception.
```
com.apple.xpc.launchd.oneshot.0x10000013.monero-wallet-gui[14784]): Could not find and/or execute program specified by service: 2: No such file or directory: /private/var/folders/fr/0sn549vn75zgbwc7y0rjlg400000gp/T/AppTranslocation/B3601126-6939-41B1-929B-D757D1C57EBD/d/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
```
This method is used
```
$ chmod -R 755 monero-wallet-gui.app/
$ ls -l
drwxr-xr-x@ 3 xxx  staff  102  7 26 17:55 monero-wallet-gui.app
```
Now, The prompt for console is
```
com.apple.xpc.launchd[1] (com.apple.xpc.launchd.oneshot.0x1000000c.monero-wallet-gui[3589]): Service could not initialize: 16G29: xpcproxy + 11769 [1505][1E2A2740-D4E5-342E-A502-4792BD02598D]: 0xd
```
I am trying to solve this problem.

## pazos | 2018-08-17T15:37:22+00:00
@KPWorkspace: please run from terminal:
`./monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui`

## KPWorkspace | 2018-08-20T01:27:21+00:00
@pazos Thank you,I think it may be a problem with this computer, my private Mac can run GUI.
This public computer can run cli but can't run GUI

# Action History
- Created by: KPWorkspace | 2018-08-16T09:41:03+00:00
- Closed at: 2018-08-22T07:38:06+00:00
