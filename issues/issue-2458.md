---
title: Expanded menu items are hidden with small window height
source_url: https://github.com/monero-project/monero-gui/issues/2458
author: rating89us
assignees: []
labels: []
created_at: '2019-11-23T21:19:40+00:00'
updated_at: '2019-12-08T22:44:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The menu section should be automatic scrolled down when user clicks a main menu item, because when the wallet isn't full screen, the user can't see the subitems of the main menu item without scrolling.

In the example below the user can't see the other subitems in Advanced (Prove/check, Shared RingDB, Sign/verify):

![image](https://user-images.githubusercontent.com/45968869/69485366-c8eda480-0e3e-11ea-8c69-6e2e70190459.png)

I suggest creating an anchor link to each item in menu.

Related to #2568

# Discussion History
## selsta | 2019-11-23T21:20:47+00:00
What is the size of your display?

## rating89us | 2019-11-23T21:38:10+00:00
27 inches in 1920 x 1080, but I don't maximize Monero GUI window.

# Action History
- Created by: rating89us | 2019-11-23T21:19:40+00:00
