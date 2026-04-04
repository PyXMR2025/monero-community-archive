---
title: UI Labels were mangled until creating another wallet
source_url: https://github.com/monero-project/monero-gui/issues/2826
author: jcalfee
assignees: []
labels: []
created_at: '2020-04-08T14:45:21+00:00'
updated_at: '2020-04-08T16:15:10+00:00'
type: issue
status: closed
closed_at: '2020-04-08T15:04:00+00:00'
---

# Original Description
After creating a new "Simple mode (bootstrap)" wallet and letting it running over night I re-started the app.  Upon UI restart, the labels appeared manged (screen shot below).  I can re-start and open the same wallet and the labels are still manged (repeatable).

![image](https://user-images.githubusercontent.com/204121/78789209-6d95fc00-7972-11ea-9def-e5f6785317d5.png)

If I use the same installation to create and open a new "Simple mode" wallet with a new name then open that wallet, the UI is fine again. I can re-open the original wallet (in the same run) and the labels are fine.  I can restart and open either wallet and the labels both wallets are fine.  So not the issue it not repeatable unless perhaps I start from scratch.

On each test, I let the app stop and start the daemon.

monero-gui-linux-x64-v0.15.0.4.tar.bz2

There is one persistent error but it does not appear to have anything to do with the labels:
`2020-04-08 14:38:53.825	E No message store file found: /home/user/Monero/wallets/word/word.mms`

I have mounted the entire Moneor folder on an external USB hard drive.

I'm running in docker `debian:10` on a  4.9.0-11-amd64 x86_64 debian 9 (stretch) host.

# Discussion History
## selsta | 2020-04-08T14:48:54+00:00
Can you try starting with `QMLSCENE_DEVICE=softwarecontext` env var?

## jcalfee | 2020-04-08T14:56:52+00:00
The labels are fine, but recall the issue seemed to have disappeared.  Here is the log with `QMLSCENE_DEVICE=softwarecontext`

```bash
~$ /monero-gui-v0.15.0.4/monero-wallet-gui
xkbcommon: ERROR: failed to add default include path /usr/share/X11/xkb
Qt: Failed to create XKB context!
Use QT_XKB_CONFIG_ROOT environmental variable to provide an additional search path, add ':' as separator to provide several search paths and/or make sure that XKB configuration data directory contains recent enough contents, to update please see http://cgit.freedesktop.org/xkeyboard-config/ .
2020-04-08 14:52:51.953 W app startd (log: /home/james/.bitmonero/monero-wallet-gui.log)
2020-04-08 14:52:51.953 W Qt:5.9.7 GUI:v0.15.0.4 | screen: 1920x1080 - dpi: 96.1263 - ratio:1.10899
libGL error: MESA-LOADER: failed to retrieve device information
libGL error: Version 4 or later of flush extension not found
libGL error: failed to load driver: i915
libGL error: failed to open drm device: No such file or directory
libGL error: failed to load driver: i965
2020-04-08 14:52:52.595 W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"
2020-04-08 14:53:06.809 I Generating SSL certificate
2020-04-08 14:53:06.938 W Loaded wallet keys file, with public address: 468k6...5JVq7N6J7jzyEXpt7j5
2020-04-08 14:53:07.029 E No message store file found: /home/home/Monero/wallets/james/james.mms
2020-04-08 14:53:07.032 I Generating SSL certificate
2020-04-08 14:53:11.830 I Monero 'Carbon Chamaeleon' (v0.15.0.1-release)
Forking to background...
```
and without `QMLSCENE_DEVICE=softwarecontext`
```bash
$ /monero-gui-v0.15.0.4/monero-wallet-gui
xkbcommon: ERROR: failed to add default include path /usr/share/X11/xkb
Qt: Failed to create XKB context!
Use QT_XKB_CONFIG_ROOT environmental variable to provide an additional search path, add ':' as separator to provide several search paths and/or make sure that XKB configuration data directory contains recent enough contents, to update please see http://cgit.freedesktop.org/xkeyboard-config/ .
2020-04-08 14:54:37.944 W app startd (log: /home/james/.bitmonero/monero-wallet-gui.log)
2020-04-08 14:54:37.945 W Qt:5.9.7 GUI:v0.15.0.4 | screen: 1920x1080 - dpi: 96.1263 - ratio:1.10899
libGL error: MESA-LOADER: failed to retrieve device information
libGL error: Version 4 or later of flush extension not found
libGL error: failed to load driver: i915
libGL error: failed to open drm device: No such file or directory
libGL error: failed to load driver: i965
2020-04-08 14:54:38.590 W qrc:/qt-project.org/imports/QtQuick/Controls/ApplicationWindow.qml:240:9: QML ContentItem: Binding loop detected for property "implicitWidth"

2020-04-08 14:54:49.759 I Generating SSL certificate
2020-04-08 14:54:49.885 W Loaded wallet keys file, with public address: 468...7j5
2020-04-08 14:54:50.020 E No message store file found: /home/james/Monero/wallets/james/james.mms
2020-04-08 14:54:50.047 I Generating SSL certificate
2020-04-08 14:54:54.812 I Monero 'Carbon Chamaeleon' (v0.15.0.1-release)
Forking to background...
```

I'll save that ENV incase it happens again.


## selsta | 2020-04-08T15:01:03+00:00
I think the problem is related to graphic drivers and using docker, as you can see with the libgl error messages.

## jcalfee | 2020-04-08T15:04:00+00:00
Thanks, I'll look into it.  Interesting that the password prompt always worked but it was only the labels.  Guess that uses different UI components.

## jcalfee | 2020-04-08T16:15:10+00:00
Looks like the container needed "gpu" support.  The error did disappear.

There is still this:
`2020-04-08 15:45:44.845	E No message store file found: /home/james/Monero/wallets/james/james.mms`

 All seems well though.

# Action History
- Created by: jcalfee | 2020-04-08T14:45:21+00:00
- Closed at: 2020-04-08T15:04:00+00:00
