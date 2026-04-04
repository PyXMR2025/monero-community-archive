---
title: 'Dark theme: Can''t scroll History if mouse is over the transactions'
source_url: https://github.com/monero-project/monero-gui/issues/1209
author: tficharmers
assignees: []
labels:
- bug
- resolved
created_at: '2018-03-30T13:25:25+00:00'
updated_at: '2019-04-27T00:27:36+00:00'
type: issue
status: closed
closed_at: '2019-04-27T00:27:36+00:00'
---

# Original Description
Scrolling when the mouse cursor is over the transactions in History doesn't work. If you move the cursor to the left or right gutter, scrolling then works.

Mac OS
GUI version: v0.11.1.0-450-gb32b308

# Discussion History
## sanderfoobar | 2018-03-30T13:38:01+00:00
Interesting, scrolls work fine on Linux. How many items do you reckon you have in that table?

Ill test OSX at a later date.

## tficharmers | 2018-03-30T13:43:44+00:00
29 items.

Ah interesting. It doesn't scroll if I use an Apple magic mouse, but I just plugged in a cheap Microsoft mouse and it does scroll the transactions using the scroll wheel on that. 

Not so magic!

With the magic mouse though, I can click and hold on a transaction and then drag up/down and stop depressing the mouse, to make it scroll.

So, you also can't scroll the History using a Macbook Pro trackpad.

## sanderfoobar | 2018-03-30T14:19:17+00:00
Indeed, I can reproduce on macbook pro trackpad. 

## sanderfoobar | 2018-03-30T14:19:20+00:00
+bug

## peanutsformonkeys | 2018-04-03T22:27:18+00:00
Encountered the same issue when testing Aeon's pre-release 0.1.7.2. Scrolling with the mouse-wheel works, but two-finger swiping on the built-in trackpad doesn't work anymore. One has to click with the trackpad and then drag, which is a pain if you have hundreds of transactions to move through.

## Axam | 2018-04-10T01:08:40+00:00
Hold left mouse button to scroll as workaround. Mouse wheel and touchpad didn't work for me. 

## selsta | 2019-04-27T00:20:44+00:00
+resolved

# Action History
- Created by: tficharmers | 2018-03-30T13:25:25+00:00
- Closed at: 2019-04-27T00:27:36+00:00
