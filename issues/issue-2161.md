---
title: 'Fail to start with error: cannot register existing type ''GtkIMContext'''
source_url: https://github.com/monero-project/monero-gui/issues/2161
author: Lafudoci
assignees: []
labels: []
created_at: '2019-05-05T12:37:07+00:00'
updated_at: '2019-05-15T14:51:39+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
OS: elementary os juno (based on ubuntu 18.04)
Wallet version: v0.14.0.0
IM: [HIME](https://github.com/hime-ime/hime)
```
(monero-wallet-gui:6557): GLib-GObject-WARNING **: 19:44:00.522: cannot register existing type 'GtkIMContext'

(monero-wallet-gui:6557): GLib-CRITICAL **: 19:44:00.522: g_once_init_leave: assertion 'result != 0' failed

(monero-wallet-gui:6557): GLib-GObject-CRITICAL **: 19:44:00.522: g_type_register_dynamic: assertion 'parent_type > 0' failed

(monero-wallet-gui:6557): GLib-GObject-CRITICAL **: 19:44:00.522: g_object_new_with_properties: assertion 'G_TYPE_IS_OBJECT (object_type)' failed
```
It seems related to the input method, but I haven't figured out.

# Discussion History
## Lafudoci | 2019-05-10T12:17:50+00:00
I found it works if I build from master
`v0.14.0.0-110-ge81cb7e (Qt 5.9.5)`

## sanderfoobar | 2019-05-10T21:35:44+00:00
To confirm; you downloaded [latest release binary](https://github.com/monero-project/monero-gui/releases/tag/v0.14.0.0) and it error'd with `GtkIMContext` ?

## sanderfoobar | 2019-05-10T21:36:58+00:00
Do you have a `QT_STYLE_OVERRIDE` set in your environment?

## Lafudoci | 2019-05-11T01:48:19+00:00
> To confirm; you downloaded [latest release binary](https://github.com/monero-project/monero-gui/releases/tag/v0.14.0.0) and it error'd with `GtkIMContext` ?

Oh, the official build could start without such error, but I still can't enable my input method to type Chinese characters in app though.

The error reported in this issue is from my build with tag v0.14, Qt 5.95

> Do you have a `QT_STYLE_OVERRIDE` set in your environment?

Yes, it is `QT_STYLE_OVERRIDE=adwaita`

Also provide all others QT env FYI
```
QT_STYLE_OVERRIDE=adwaita
QT4_IM_MODULE=hime
QT_QPA_PLATFORMTHEME=gtk3
QT_ACCESSIBILITY=1
QT_IM_MODULE=hime
```

## sanderfoobar | 2019-05-11T03:24:45+00:00
Thanks for the information. Ill see if I can test in a virtual machine at a later point in time.

## Lafudoci | 2019-05-11T13:10:10+00:00
Thank you @xmrdsc. But I guess if it works fine with master build, then it should be resolved in next release as well?

## sanderfoobar | 2019-05-11T14:01:08+00:00
Release builds are statically compiled (`./build.sh release-static`). It will use an embedded Qt. In your case, you most likely compiled with just `./build.sh` or `./build.sh debug`. This will use your local Qt, that may or may not differ from ours.

In any case ill try out a VM. I take it you installed Qt dependencies via `apt` ?

## Lafudoci | 2019-05-11T14:09:42+00:00
Yes, you're right. I built with `QT_SELECT=5 ./build.sh` which is described in readme. And indeed my Qt is from apt.

## Lafudoci | 2019-05-15T14:51:19+00:00
I found the same issue still appears in master build, but not at launch, instead, it occurs when I click `Browse filesystem` button in `open wallet from file`
```
(monero-wallet-gui:7542): GLib-GObject-WARNING **: 22:46:25.527: cannot register existing type 'GtkIMContext'

(monero-wallet-gui:7542): GLib-CRITICAL **: 22:46:25.527: g_once_init_leave: assertion 'result != 0' failed

(monero-wallet-gui:7542): GLib-GObject-CRITICAL **: 22:46:25.527: g_type_register_dynamic: assertion 'parent_type > 0' failed

(monero-wallet-gui:7542): GLib-GObject-CRITICAL **: 22:46:25.527: g_object_new_with_properties: assertion 'G_TYPE_IS_OBJECT (object_type)' failed

```

# Action History
- Created by: Lafudoci | 2019-05-05T12:37:07+00:00
