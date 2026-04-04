---
title: Open a wallet from file displays Settings page in the background
source_url: https://github.com/monero-project/monero-gui/issues/1159
author: dEBRUYNE-1
assignees: []
labels:
- enhancement
- resolved
created_at: '2018-03-05T15:16:41+00:00'
updated_at: '2019-04-23T18:18:46+00:00'
type: issue
status: closed
closed_at: '2019-04-23T18:18:46+00:00'
---

# Original Description
Open a wallet from file -> It will display the settings page of the GUI in the background.

# Discussion History
## sanderfoobar | 2018-03-29T23:55:36+00:00
+enhancement

## sanderfoobar | 2018-12-17T18:10:44+00:00
@mmbyday mentioned:
> Whatever page, such as the setting page, was open previously, will show in the background. 

### Quick solution:

Programmatically switch to the transfer page before closing a wallet (and call [stackview.completeTransition()](http://doc.qt.io/qt-5/qml-qtquick-controls-stackview.html#completeTransition-method) to prevent panel animation).

### Better solution:

Find a way to properly construct and deconstruct QML components by utilizing `Component.onCompleted {`, etc, so a cleanup of text contents would happen automatically.

Just thinking out loud :-)

## mmbyday | 2018-12-17T20:59:43+00:00
I made a small, simple change. That'll fix this for now. #1837 , Keep thinking out loud @xmrdc . Rock on :-)

## dEBRUYNE-1 | 2018-12-18T08:08:51+00:00
Looks good. I'll close this issue when the PR gets merged. 

## dEBRUYNE-1 | 2019-04-23T18:15:02+00:00
+resolved

# Action History
- Created by: dEBRUYNE-1 | 2018-03-05T15:16:41+00:00
- Closed at: 2019-04-23T18:18:46+00:00
