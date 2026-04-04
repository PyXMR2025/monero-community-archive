---
title: Lock wallet on inactivity time showing 14.7666666666666666666666 minutes
source_url: https://github.com/monero-project/monero-gui/issues/2006
author: rating89us
assignees: []
labels:
- bug
created_at: '2019-03-11T10:18:38+00:00'
updated_at: '2019-04-25T20:26:37+00:00'
type: issue
status: closed
closed_at: '2019-04-25T20:26:37+00:00'
---

# Original Description
On macOS Mojave v.10.14.3, when you select a time to lock wallet, it first rapidly displays a long number (like 14.7666666666666666666666 minutes), which is rapidly rounded (to 15 minutes).
![image](https://user-images.githubusercontent.com/45968869/54382132-a55b4300-468f-11e9-924f-28d803fc51a0.png)


# Discussion History
## sanderfoobar | 2019-03-11T11:42:30+00:00
+bug

## mmbyday | 2019-03-13T02:01:59+00:00
Might be a Mac specific bug. Can't replicate on Windoze.

## selsta | 2019-03-14T18:11:49+00:00
Can’t reproduce on macOS.

## apertamono | 2019-03-28T14:13:57+00:00
I get the same bug on Windows 10. It's also rounded down in the blink of an eye. Just managed to take a screenshot.

Maybe it's hardware-related and happens to fast to be visible on the shiny new gaming rigs used by devs?

![timer bug](https://user-images.githubusercontent.com/22837744/55164519-13156d80-516c-11e9-87ed-af3eadc52618.png)


## sanderfoobar | 2019-03-28T21:59:48+00:00
Thanks @ProkhorZ 

I looked some more at our implementation:

https://github.com/monero-project/monero-gui/blob/d4d8ff54e6c94f82de7eb012d7b310addeedcbb9/pages/settings/SettingsLayout.qml#L155-L164

It is due to how earlier versions of Qt lack a `Slider.onMoved` event, thus, we can't reliably update the minutes whilst the user is changing the value.

This will be fixed when we switch to Qt 5.9.7 - possibly next release.

# Action History
- Created by: rating89us | 2019-03-11T10:18:38+00:00
- Closed at: 2019-04-25T20:26:37+00:00
