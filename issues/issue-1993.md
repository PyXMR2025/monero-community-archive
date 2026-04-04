---
title: White fields in monero-wallet-qt 0.14.0.0-1
source_url: https://github.com/monero-project/monero-gui/issues/1993
author: brainscar
assignees: []
labels:
- invalid
created_at: '2019-03-03T02:33:16+00:00'
updated_at: '2020-01-16T02:45:51+00:00'
type: issue
status: closed
closed_at: '2020-01-16T02:45:51+00:00'
---

# Original Description
Hi,

I'm having this issue with this package:

https://aur.archlinux.org/packages/monero-wallet-qt

Some fields are white, which I think are supposed to be black, as such:

![1](https://user-images.githubusercontent.com/38463143/53690137-954f7500-3d19-11e9-9d23-636ecd8b9474.png)
![2](https://user-images.githubusercontent.com/38463143/53690138-954f7500-3d19-11e9-824d-9aceec7e8bd5.png)
![3](https://user-images.githubusercontent.com/38463143/53690139-95e80b80-3d19-11e9-861b-2310ada8269e.png)

Hope you can help. Thanks!

# Discussion History
## selsta | 2019-03-04T11:54:49+00:00
This is rather weird and seems to be related to your local setup. What Qt version did you use to build the GUI?

## brainscar | 2019-03-05T17:47:08+00:00
@selsta thank you so much for the response.

I hope I'm doing this right:

> $ qmake-qt5 --version

_QMake version 3.1
Using Qt version 5.12.1 in /usr/lib_

I tried different themes but it didn't change the white fields, except for 1 theme which made the fields a weird yellow.


## sanderfoobar | 2019-03-06T09:34:25+00:00
Maybe because we use `TextArea` without any background set;

https://github.com/monero-project/monero-gui/blob/02e16634716c6c9fa6bf0aa75928f0d698be7453/pages/settings/SettingsWallet.qml#L83-L105

It might be inheriting the background colors from OS/distro. That's probably why Qt's TextArea has [backgroundVisible](https://doc.qt.io/qt-5/qml-qtquick-controls-textarea.html#backgroundVisible-prop).

Just a thought.


## trulex | 2019-03-08T20:11:38+00:00
This happens when using Breeze theme. Workaround is to switch to Breeze Dark.

## brainscar | 2019-03-09T21:55:46+00:00
Thanks @trulex , but unfortunately that didn't work. I have since switched to the GUI binary and the issue has gone away.

## dEBRUYNE-1 | 2019-07-03T17:33:29+00:00
@brainscar - Is this still an issue with GUI v0.14.1.0?

## dEBRUYNE-1 | 2019-07-12T16:08:50+00:00
@brainscar - ping. 


## selsta | 2020-01-16T02:31:13+00:00
Closing due to inactivity.

+invalid

# Action History
- Created by: brainscar | 2019-03-03T02:33:16+00:00
- Closed at: 2020-01-16T02:45:51+00:00
