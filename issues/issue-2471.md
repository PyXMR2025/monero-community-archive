---
title: Unnecessary scroll bar in many pages
source_url: https://github.com/monero-project/monero-gui/issues/2471
author: rating89us
assignees: []
labels: []
created_at: '2019-11-23T23:23:57+00:00'
updated_at: '2019-12-21T23:10:02+00:00'
type: issue
status: closed
closed_at: '2019-12-21T23:10:02+00:00'
---

# Original Description
Many pages (see Settings) are displaying an unnecessary scroll bar when the content is being completely displayed in the window. 

This seems to happen because the scroll bar is always enabled, unless the window height is at least 
~970 px.

# Discussion History
## selsta | 2019-11-24T00:20:50+00:00
Many pages? Can you check to see if this happens in other places apart from settings? The height is dynamic on the other pages so it should not happen.

## rating89us | 2019-11-24T00:55:26+00:00
I think there are two different problems:

Problem 1: all pages of Settings have a large scroll bar, even when the content fits in the window.

![5](https://user-images.githubusercontent.com/45968869/69581600-143abb00-0fd7-11ea-9525-8a4fb1ee2b64.gif)

Problem 2: in the remaining pages (not in Settings), it seems that there is a black bar at bottom that is being considered as part of the content. Because of this black bar the scroll bar is appearing even when all content is being displayed. See below:

![image](https://user-images.githubusercontent.com/45968869/69487553-58558080-0e5c-11ea-8d3d-3ad99aafc749.png)

For example, see the send page below. All content is being displayed, and a scroll bar shouldn't appear:
![image](https://user-images.githubusercontent.com/45968869/69487539-1c222000-0e5c-11ea-8725-dceff6f37214.png)

This problem of the black bar at bottom seems to be worse in Transactions page, which is dynamic, and because of this it almost always display the scroll bar.

# Action History
- Created by: rating89us | 2019-11-23T23:23:57+00:00
- Closed at: 2019-12-21T23:10:02+00:00
