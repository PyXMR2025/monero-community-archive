---
title: Text alignment bug in the 'Change wallet' / 'Cancel' button with the password
  prompt
source_url: https://github.com/monero-project/monero-gui/issues/1924
author: tficharmers
assignees: []
labels:
- bug
- resolved
created_at: '2019-02-01T12:30:22+00:00'
updated_at: '2019-02-25T08:18:34+00:00'
type: issue
status: closed
closed_at: '2019-02-25T08:18:34+00:00'
---

# Original Description
The updated 'cancel' button in the password prompt overlay has some text rendering issues. I saw it in this build on macOS:

https://build.getmonero.org/builders/monero-gui-osx-10.11/builds/1344

![screen shot 2019-02-01 at 09 44 49](https://user-images.githubusercontent.com/23356013/52122983-b0e13600-261c-11e9-9313-a20bf06f1ee9.PNG)

![screen shot 2019-02-01 at 10 22 16](https://user-images.githubusercontent.com/23356013/52122997-b5a5ea00-261c-11e9-883f-6354fdcc5d7c.PNG)

When you select the button, on mousedown, the text slides back into a central/correct position in the button.

# Discussion History
## tficharmers | 2019-02-01T12:33:42+00:00
I have just noticed the same kind of issue in the 'Start daemon' button on the Settings page. Again, on mousedown, the text moves to the left to correctly align:

![screen shot 2019-02-01 at 12 31 44](https://user-images.githubusercontent.com/23356013/52123282-8643ad00-261d-11e9-9623-dbdef3566ea6.PNG)


## sanderfoobar | 2019-02-01T12:42:43+00:00
Thanks for reporting.

+bug

## selsta | 2019-02-03T20:33:25+00:00
This doesn’t happen on macOS with Qt 5.12.

## rbrunner7 | 2019-02-22T11:41:06+00:00
Happens on Windows as well, latest Buildbot build from today

## xiphon | 2019-02-22T11:59:53+00:00
Seems this is related to Qt version 5.7 installed on both the buildbots

## selsta | 2019-02-22T16:27:38+00:00
We should fix that before v0.14.

## mmbyday | 2019-02-25T00:22:40+00:00
Fixed nicely by https://github.com/monero-project/monero-gui/pull/1952

+resolved

## dEBRUYNE-1 | 2019-02-25T08:17:39+00:00
+resolved

# Action History
- Created by: tficharmers | 2019-02-01T12:30:22+00:00
- Closed at: 2019-02-25T08:18:34+00:00
