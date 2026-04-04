---
title: 'macOS: Show scroll bars if this is set system wide to "Always"'
source_url: https://github.com/monero-project/monero-gui/issues/4160
author: MikeRich88
assignees: []
labels: []
created_at: '2023-04-24T05:03:17+00:00'
updated_at: '2023-04-25T02:57:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
OS: macOS 13.3.1
Steps to reproduce: First, make sure that "Show scroll bars" is set to "Always" in the system settings.

![image](https://user-images.githubusercontent.com/7113073/233903736-ef3d811b-6840-471a-945f-6817a213cb23.png)

Now, load the monero-gui app and go to any area with scrolling. Such as transaction history, or you can go to Settings and click the Interface tab like I have done, because I did not want to show my transaction in a screenshot.

Because I made the window small not all of the settings can be seen, so it is a scrolling area - but as you can see, no scroll bar is shown despite being set to "Always".

![image](https://user-images.githubusercontent.com/7113073/233904120-774f9720-69d2-4bc4-80a6-598acc014c7d.png)

# Discussion History
## selsta | 2023-04-24T12:23:10+00:00
monero-gui is cross platform app that doesn't use the system settings for the scrollbar.

It's possible to use macOS system APIs to check whether "Show scroll bars" is set to "Always" on startup but it will be difficult to mimic exact behaviour of native macOS apps.

## MikeRich88 | 2023-04-25T02:57:58+00:00
> It's possible to use macOS system APIs to check whether "Show scroll bars" is set to "Always" on startup but it will be difficult to mimic exact behaviour of native macOS apps.

Here is the specific API to check: https://developer.apple.com/documentation/appkit/nsscroller/1523620-preferredscrollerstyle

This would go a long way to fit monero-gui better into the macOS interface.

# Action History
- Created by: MikeRich88 | 2023-04-24T05:03:17+00:00
