---
title: Some UI/UX improvements for the 'Welcome to Monero!' page.
source_url: https://github.com/monero-project/monero-gui/issues/1518
author: ghost
assignees: []
labels:
- enhancement
- resolved
created_at: '2018-07-20T07:28:56+00:00'
updated_at: '2019-09-05T01:54:31+00:00'
type: issue
status: closed
closed_at: '2019-09-05T01:54:31+00:00'
---

# Original Description
![monero_gui](https://user-images.githubusercontent.com/32292415/42988755-62c3e8c2-8c30-11e8-9572-ea1414381119.png)

Hey guys, had some spare time today and made some quick UI/UX changes to the GUI 'Welcome to Monero!' page when launching the GUI.

I get that some people may not like the improvements, i'm not suggesting that all of them should be included but imo they are some additions that enhance the UI/UX of the wallet.  Below I've outlined the changes. I am using the windows version of the GUI fyi. 

1) Changed 'Please select one of the following options:' to 'What would you like to do?' Posing a question creates a more user orientated experience.

2) Add a close window X on top right, this applies to all the GUI startup pages. I often have to right click the tray icon to close the GUI which is frustrating. 

3) The window is not movable (on windows anyways). The user should be able to hold click and drag the window on their screen. This is only apparent on the launching of the GUI, once using the wallet the screen is draggable. 

4) Slight design changes. 

- Used a lighter orange (#f4815b) which I think has a more material design feel to it. 
- Changed the font weight of the chevron arrow and rounded the edges.
- Changed the icons and the circle background colors. 

5) Hid the testnet and stagenet options in a collapsed section which can be shown by clicking advanced option. This has already been suggested in issue #1436. 

If people like these additions I'd be happy to do other GUI pages over the weekend. 


# Discussion History
## dginovker | 2018-07-24T16:41:35+00:00
> Changed 'Please select one of the following options:' to 'What would you like to do?' Posing a question creates a more user orientated experience.

Incredible support on this

> Add a close window X on top right, this applies to all the GUI startup pages. I often have to right click the tray icon to close the GUI which is frustrating.

Great change

> The window is not movable (on windows anyways). The user should be able to hold click and drag the window on their screen. This is only apparent on the launching of the GUI, once using the wallet the screen is draggable.

Might be a qt thing

> Used a lighter orange (#f4815b) which I think has a more material design feel to it.

I like it. The Monero logo is very hard-hitting, we don't have to always use those colors

> Hid the testnet and stagenet options in a collapsed section which can be shown by clicking advanced option. This has already been suggested in issue #1436.

An unbelievably good change.

Do you have the code for this or was it a paint mock-up?

## sanderfoobar | 2018-07-24T18:51:51+00:00
I've actually started redesigning the wizard screens in #1513 

This screen will probably be replaced by something that looks like:

![](https://i.imgur.com/uQYcgef.png)

Nothing is set in stone though. 

@Electricsheep01 Any chance you could join `#monero-gui` on freenode?

## ghost | 2018-07-25T04:10:09+00:00
@dginovker It is just a AI mock up for now. I just wanted some initial feedback to see if its worth doing some more pages.

@skftn ahh crap sorry I should have did some browsing in the issues, just joined on freenode. 

## sanderfoobar | 2018-07-26T10:15:10+00:00
+enhancement

## selsta | 2019-09-05T01:45:30+00:00
Thanks for the suggestions, I’m closing this because a lot has changed in the last year and I think your suggestions have been integrated :)

+resolved

# Action History
- Created by: ghost | 2018-07-20T07:28:56+00:00
- Closed at: 2019-09-05T01:54:31+00:00
