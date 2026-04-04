---
title: Graphical glitch
source_url: https://github.com/monero-project/monero-site/issues/336
author: binaryFate
assignees: []
labels: []
created_at: '2017-07-21T17:40:39+00:00'
updated_at: '2017-10-20T22:13:05+00:00'
type: issue
status: closed
closed_at: '2017-08-31T09:25:12+00:00'
---

# Original Description
Buttons are too far up, on top of text.
See screenshot: http://i.imgur.com/zRwVo35.jpeg

Config: Firefox 54, linux Ubuntu 16.04 64bits


# Discussion History
## erciccione | 2017-07-21T17:54:37+00:00
I have the same problem. I opened an issue [on rehrar 's fork](https://github.com/rehrar/monero-site-new/issues/3) weeks ago, but it probably got lost after the merge

## MaxXor | 2017-07-26T12:45:38+00:00
I can't reproduce this. For me it's looking fine on Windows 7 with Firefox 54.0.1 (on 1920x1080). Maybe this is related to screen resolution or OS?

edit: I think it's the font which Ubuntu uses.

## binaryFate | 2017-07-26T13:40:01+00:00
I'm on 1920x1080 too

## erciccione | 2017-07-26T13:40:21+00:00
@MaxXor I think is the font aswell, but  the fix suggested in #342 play around the problem increasing the height of that section of .5
This will fix the problem for Ubuntu users but shouldn't affect in a relevant way windows users

## jrob-io | 2017-07-27T16:39:18+00:00
@binaryFate @erciccione Since this might be a font issue, can anyone test to see if #315 would fix this?

In Firefox, go to Developer Tools > Style Editor > `custom.css`
In Chrome, Developer Tools > Sources > `custom.css` via the file picker on the left
Delete `sans-serif` from lines 32 and 46.

Edit: Confirming that **the font is the problem**. Ubuntu uses **Deja Vu Sans** for `sans-serif`, which has a very wide glyphs. You can reproduce this issue on any OS by downloading it and forcing `font-family: "DejaVu Sans"` via Dev Tools. #315 allows OpenSans to be displayed so it should fix this.

## erciccione | 2017-07-27T18:01:07+00:00
@jrob-io Tested. I can confirm, #315 will fix this issue

# Action History
- Created by: binaryFate | 2017-07-21T17:40:39+00:00
- Closed at: 2017-08-31T09:25:12+00:00
