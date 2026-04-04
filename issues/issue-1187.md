---
title: Improve visibility of the videos in the "What is Monero?" page
source_url: https://github.com/monero-project/monero-site/issues/1187
author: erciccione
assignees:
- erciccione
labels:
- enhancement
- UX
created_at: '2020-09-14T08:01:50+00:00'
updated_at: '2020-11-10T19:26:23+00:00'
type: issue
status: closed
closed_at: '2020-11-10T19:26:23+00:00'
---

# Original Description
Some [users report](https://www.reddit.com/r/Monero/comments/iaww0p/getmoneroorg_updated_improved_rss_feed_new/g57j2xq/) they are easy to miss. We could move them somewhere else or make them more visible.

# Discussion History
## erciccione | 2020-09-16T10:18:33+00:00
#1190 

Note that 1190 doesn't address the problems reported in the reddit post about videos not playing. I tried to reproduce but i wasn't able to. The structure of our videos should be supported by all browsers. @selsta reported he doesn't have any problems with Chrome, but i am having issues playing videos on chromium. I couldn't find an obvious explanation. I'm creating a dedicated Windows system to test this and will keep inspecting the issue.

## selsta | 2020-09-16T10:20:10+00:00
It does also not show up with Chrome, I didn’t understand the issue initially. There is still the problems that videos keep playing if you click on next.

## erciccione | 2020-09-16T10:25:34+00:00
> It does also not show up with Chrome

I created #1191 to keep track of the problem.

> There is still the problems that videos keep playing if you click on next.

That's related to the way the videos are displayed (the carousel thing), which is removed by #1190.

# Action History
- Created by: erciccione | 2020-09-14T08:01:50+00:00
- Closed at: 2020-11-10T19:26:23+00:00
