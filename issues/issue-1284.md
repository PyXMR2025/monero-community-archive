---
title: Monero GUI 0.12.0.0 GUI blurred white typeface
source_url: https://github.com/monero-project/monero-gui/issues/1284
author: allegro101
assignees: []
labels:
- resolved
created_at: '2018-04-06T17:47:07+00:00'
updated_at: '2019-07-04T07:09:44+00:00'
type: issue
status: closed
closed_at: '2019-07-04T07:09:44+00:00'
---

# Original Description
Win 7 64 bit GUI works fine so far but white typeface against black background is blurred. Previous white background/black type was crystal clear. Is there an advanced setting which would make the type clearer?

![guinotclear](https://user-images.githubusercontent.com/24720449/38435843-ef712a24-39a0-11e8-812a-3627da153890.JPG)




# Discussion History
## dEBRUYNE-1 | 2018-04-06T19:22:22+00:00
Could you try launching GUI v0.12 via the `start-low-graphics-mode.bat` batch file that is included?

## allegro101 | 2018-04-08T01:43:56+00:00
Launching GUI by start-low-graphics-mode,bat batch file I notice no difference. Type still blurred.

## pazos | 2018-04-19T00:04:21+00:00
@allegro101: has your screen a resolution higher than 1920x1080?, which one? 

## allegro101 | 2018-04-19T03:23:45+00:00
Screen resolution is 1600x900

## dEBRUYNE-1 | 2018-07-04T08:37:05+00:00
This particular issue is supposedly resolved in GUI v0.12.2.0: 

https://www.reddit.com/r/Monero/comments/8vkx2g/gui_v01220_released/

Could you give it a try? 

## allegro101 | 2018-07-05T03:05:24+00:00
Tried GUI v0.12.2.0 issue still present as shown before.

## dEBRUYNE-1 | 2018-07-05T10:48:05+00:00
@allegro101 - Even with the `start-low-graphics-mode.bat` batch file? 

## allegro101 | 2018-07-05T13:38:52+00:00
@dEBRUYNE-1  - Yes even starting GUI with the start-low-graphics-mode.bat batch file:

![moneroscreenshot](https://user-images.githubusercontent.com/24720449/42326217-856e1f6a-8036-11e8-911b-55e989dd582a.PNG)

Slightly better perhaps this is as good as it gets? I preferred the older white background BTW.



## dEBRUYNE-1 | 2018-07-05T15:17:00+00:00
That looks slightly better indeed. 

>this is as good as it gets?

Probably :-P

>I preferred the older white background BTW.

There will, most likely, be a white theme in v0.13. 

## allegro101 | 2018-07-06T02:06:25+00:00
White theme option would be welcome as easier on the eyes. I also appreciate the separate command prompt window that GUI v0.12.2.0 launches by default.

## sanderfoobar | 2019-04-10T19:51:46+00:00
@allegro101 Is still an issue on the latest GUI version (0.14) for you?

## dEBRUYNE-1 | 2019-07-04T06:54:30+00:00
I am going to close this, as the author has not responded for several months. 

## dEBRUYNE-1 | 2019-07-04T06:54:34+00:00
+resolved

# Action History
- Created by: allegro101 | 2018-04-06T17:47:07+00:00
- Closed at: 2019-07-04T07:09:44+00:00
