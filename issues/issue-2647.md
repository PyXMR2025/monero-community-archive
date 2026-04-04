---
title: 'Settings: too much text in Settings > Wallet'
source_url: https://github.com/monero-project/monero-gui/issues/2647
author: rating89us
assignees: []
labels: []
created_at: '2019-12-20T13:26:43+00:00'
updated_at: '2020-04-16T11:48:00+00:00'
type: issue
status: closed
closed_at: '2020-04-16T11:47:59+00:00'
---

# Original Description
We should remove buttons with repeated text and add some nice icons (similiar to Settings > Node page):
![image](https://user-images.githubusercontent.com/45968869/71263273-5c23d800-2320-11ea-902b-2cbc59e41518.png)

Current Settings > Node page:
![image](https://user-images.githubusercontent.com/45968869/71263308-68a83080-2320-11ea-8d8f-ec88a8af8270.png)

Current Settings > Wallet page:
![image](https://user-images.githubusercontent.com/45968869/71257651-0ac11c00-2313-11ea-96f5-2bfb697d1dbd.png)

See also issue #2652

# Discussion History
## tobtoht | 2019-12-20T14:47:00+00:00
This is great. Can you share the icons?

## tobtoht | 2019-12-20T16:01:10+00:00

![image](https://user-images.githubusercontent.com/41021257/71266295-07905500-2340-11ea-9d74-3f654ddaa3b1.png)


How does this look? I feel like I need to play around with the margins a bit more.

## rating89us | 2019-12-20T16:38:35+00:00
Icons' vertical alignment isn't centered in the row (see Node page)

## rating89us | 2019-12-20T16:39:23+00:00
Can you make the whole row clickable (like Node page rows)?

## tobtoht | 2019-12-20T16:40:46+00:00
Yes, it is like that now. Should I highlight the row on mouseover?

## tobtoht | 2019-12-20T16:57:30+00:00
![cut](https://user-images.githubusercontent.com/41021257/71271103-16303980-234b-11ea-8e60-5bc7ef2aa4a2.gif)

What do you think?

## rating89us | 2019-12-20T17:13:37+00:00
I think it's fine highlighting. But we should also highlight items in Settings>Node for consistency. 

## rating89us | 2019-12-20T17:15:50+00:00
And I would change the locker icon in `Change wallet password` to a *** icon, because a locker icon will be used in Lock wallet function (issue #2656)

## SamsungGalaxyPlayer | 2019-12-20T18:26:24+00:00
Reference #2654. I like the proposed changes here with icons. If these are added, we should not change #2654 to keep both pages consistent.

## rating89us | 2019-12-21T03:36:30+00:00
Too much vertical margins. This could be more compact:
![image](https://user-images.githubusercontent.com/45968869/71302462-e05e7580-2389-11ea-917b-42cdc203cc9b.png)


## selsta | 2019-12-21T03:37:55+00:00
Vertical margin helps with make the page feel less cluttered and overwhelming.

## GBKS | 2020-01-20T16:09:08+00:00
I would recommend keeping the buttons. Otherwise we are confusing two different types of interaction models ("choose one from a list of options" vs. "a series of independent actions"). Without buttons, there is not visual indication how these items work.

An easy to keep spacing consistent is what I had setup with the original (orange/white) icons. Each icon is centered in a  60x60px frame. The whole item has top and bottom padding of 16px either from the icon frame or the text content, whichever one is taller.

## rating89us | 2020-04-16T11:47:59+00:00
Closed with PR #2821

# Action History
- Created by: rating89us | 2019-12-20T13:26:43+00:00
- Closed at: 2020-04-16T11:47:59+00:00
