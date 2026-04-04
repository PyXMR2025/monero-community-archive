---
title: MacOS build require high performance graphics.
source_url: https://github.com/monero-project/monero-gui/issues/1301
author: Axam
assignees: []
labels:
- enhancement
- easy
created_at: '2018-04-09T06:36:34+00:00'
updated_at: '2018-05-07T20:53:22+00:00'
type: issue
status: closed
closed_at: '2018-05-07T20:53:22+00:00'
---

# Original Description
On Mac with 2 graphics cards GUI require high performance graphics.

Fix: include in Info.plist this option:
```
	<key>NSSupportsAutomaticGraphicsSwitching</key>
	<true/>
```

# Discussion History
## sanderfoobar | 2018-04-09T08:10:00+00:00
Nice one! Will test this later.

## sanderfoobar | 2018-04-09T08:11:54+00:00
+enhancement

## sanderfoobar | 2018-04-09T08:13:55+00:00
+easy

## sanderfoobar | 2018-04-28T17:19:22+00:00
Duplicate of #829

## pazos | 2018-05-02T17:44:28+00:00
@Axam : could you check if https://build.getmonero.org/downloads/monero-wallet-gui-894b10e-osx-10.11.zip fix your problem? thanks

# Action History
- Created by: Axam | 2018-04-09T06:36:34+00:00
- Closed at: 2018-05-07T20:53:22+00:00
