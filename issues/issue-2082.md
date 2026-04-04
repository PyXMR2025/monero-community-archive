---
title: 0.14 monero wallet gui install problem macosx mojave
source_url: https://github.com/monero-project/monero-gui/issues/2082
author: ebonit
assignees: []
labels: []
created_at: '2019-04-16T12:32:12+00:00'
updated_at: '2019-04-16T13:42:42+00:00'
type: issue
status: closed
closed_at: '2019-04-16T13:42:42+00:00'
---

# Original Description
I try to install the macosx gui from getmonero.org and also from https://github.com/monero-project/monero-gui/releases/download/v0.14.0.0/monero-gui-mac-x64-v0.14.0.0.tar.bz2

when I unpack the tar.bz2 then the app that I see shows this logo:
![Schermafbeelding 2019-04-16 om 14 23 23](https://user-images.githubusercontent.com/13302588/56209208-3d639800-6053-11e9-93c5-1c886d19ef1e.png)

when I try to open it it shows the following message:
![Schermafbeelding 2019-04-16 om 14 28 05](https://user-images.githubusercontent.com/13302588/56209451-e0b4ad00-6053-11e9-8f0d-afc574524259.png)

translated this says:
The monero-wallet-gui program cannot be opened because it may be damaged or incomplete.


# Discussion History
## ebonit | 2019-04-16T12:32:49+00:00
idid not try to compile myself yet. When I have time I will try to do that.

## selsta | 2019-04-16T12:34:02+00:00
Sounds like an anti-virus program blocking the GUI.

## sanderfoobar | 2019-04-16T13:00:34+00:00
If you're not running AV; are you certain the download was completed in full?

## dEBRUYNE-1 | 2019-04-16T13:18:51+00:00
If you are running AV software, please try this:

https://monero.stackexchange.com/questions/10798/my-antivirus-av-software-blocks-quarantines-the-monero-gui-wallet-is-there

## ebonit | 2019-04-16T13:42:37+00:00
AV was exactly what caused the problem. thanks for the replies.

# Action History
- Created by: ebonit | 2019-04-16T12:32:12+00:00
- Closed at: 2019-04-16T13:42:42+00:00
