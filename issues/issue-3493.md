---
title: 'Monero GUI (Android) UI Bugs '
source_url: https://github.com/monero-project/monero-gui/issues/3493
author: ghost
assignees: []
labels: []
created_at: '2021-05-21T02:41:18+00:00'
updated_at: '2021-05-24T19:35:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I was pleasantly surprised at how well the GUI wallet works on an Android phone, and I would say it's 95% of the way to being really quite usable for an intermediate Monero user (at least when the phone is in landscape mode).  

UI Bugs that were spotted:

Bug 1: 
Everything in the 'Advanced' section is too wide for the screen and doesn't wrap correctly including the section buttons at the top (Mining, Prove/Check' etc).  It should look and behave more like the 'Settings' section.
![image](https://user-images.githubusercontent.com/84093240/119071818-1e612e00-b9b0-11eb-8d98-2af1b845e06f.png)

What it should look like: 
![image](https://user-images.githubusercontent.com/84093240/119072965-0c808a80-b9b2-11eb-80bc-2c8a2b2fb728.png)

Bug 2: 
Hostname/Port input fields have cutoff text, maybe could be more responsive or stack?
![image](https://user-images.githubusercontent.com/84093240/119072164-acd5af80-b9b0-11eb-8173-5a79382e15c8.png)

Bug 3:
Sidebar scrolling.  The only 'scrollable' spot in the sidebar on a small screen is the tiny little sliver where the 'Accounts' text is in the photo below- the node area and account info really take up a ton of space and it would be cool to see these shrink to a 'minified' version on smaller screens that allows more visibility and scrollability of sidebar items.  
![image](https://user-images.githubusercontent.com/84093240/119072362-f4f4d200-b9b0-11eb-89b7-c3f1d8deeaed.png)

Bug 4:
If at all possible, it would be great to see 'custom decorations' unchecked by default for the Android build.  It takes up a lot of screen area and is just an awkward experience as no other Android apps have desktop-style close buttons/title bars.  

Bug 5: 
There is a white pixelish-wide border that sporadically happens on different sides of the app- usually on the right and bottom sides.  Full length.  
![image](https://user-images.githubusercontent.com/84093240/119072747-a4ca3f80-b9b1-11eb-9694-c5bf32539347.png)

Bug 6:
Text Centering/Wrapping Bug in Portrait Mode
![image](https://user-images.githubusercontent.com/84093240/119072869-df33dc80-b9b1-11eb-8854-e9da4f9c7787.png)

Bug 7:
Portrait mode.  I'm adding this as a bug, but it's probably more of a feature request.  The Monero GUI is basically impossible to use in portrait mode on an Android phone because the sidebar doesn't collapse or have a minified mode.  Adding a responsive sidebar (or just a total rethink) that can collapse and look something like MyMonero would be beneficial for the desktop wallet and it would definitely help make portrait mode 'more possible' on Android.
![image](https://user-images.githubusercontent.com/84093240/119073283-9892b200-b9b2-11eb-8000-134fb97179cd.png)



  

# Discussion History
## rating89us | 2021-05-24T19:35:10+00:00
I'm starting to work on this. Please check PR #3500

# Action History
- Created by: ghost | 2021-05-21T02:41:18+00:00
