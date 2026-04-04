---
title: Issues on high DPI screens
source_url: https://github.com/monero-project/monero-gui/issues/343
author: Jaqueeee
assignees: []
labels:
- resolved
created_at: '2016-12-22T21:05:20+00:00'
updated_at: '2017-08-07T17:45:09+00:00'
type: issue
status: closed
closed_at: '2017-08-07T17:45:09+00:00'
---

# Original Description
resolution: 3840x2160

![image](https://cloud.githubusercontent.com/assets/5909557/21440277/812b36b6-c892-11e6-9f42-ff1fa8736239.jpg)

elements without fixed pixels looks ok:
![image 1](https://cloud.githubusercontent.com/assets/5909557/21440298/a1d2eaee-c892-11e6-92af-ae5db169d3fd.jpg)

Reported by N-rG

# Discussion History
## rlittlefield | 2017-01-11T04:42:52+00:00
Can confirm on surface book (~271 DPI, 3000x2000)

## taoteh1221 | 2017-01-11T20:20:38+00:00
Same on 4k res on win10.

## Jaqueeee | 2017-03-01T16:22:13+00:00
hi @rlittlefield and @taoteh1221 
Can you try if PR #514 solves this?
Windows binary:
https://build.getmonero.org/downloads/monero-core-f094ffc-win64.zip
Linux:
https://build.getmonero.org/downloads/monero-core-f094ffc-linux-amd64.tar.gz

## rlittlefield | 2017-03-01T16:51:30+00:00
I've tested the windows binary you linked, and it works great. I might recommend an adjustment to the "network status" area to prevent it from overlapping when the "advanced" accordion is open. I don't know if this affects other DPIs.

![monero-overlap](https://cloud.githubusercontent.com/assets/290970/23470734/6b49dbce-fe64-11e6-9749-4c887b038baf.PNG)


## medusadigital | 2017-03-01T17:18:43+00:00
Hei @rlittlefield , unfortunately we needd to make the defualt size that small becasue of mac users. but you should be able to extend the window on the bottom right corner, which will prevetnt the overlap 

## rlittlefield | 2017-03-01T17:48:20+00:00
Yeah, that was just a suggestion. Potentially the accordion could be scrollable? It is easy enough to solve I don't think it is a big issue.

## rlittlefield | 2017-03-01T19:47:10+00:00
Thanks for the fix!

## Jaqueeee | 2017-03-01T21:51:22+00:00
@rlittlefield you're welcome. Thanks for testing. Will fix the the overlapping left menu one day. Probably gonna need to add scrolling to the mobile version anyway. 

## amiuhle | 2017-03-11T17:17:35+00:00
Don't know if it's related, but I thought I'll just reuse this issue since it's still open. This is my wallet on a 3200x1800 resolution on a 13" screen on Ubuntu 16.10. Built from b757cc28b8055c7811769c80fcbda569a66750d7

Also, no asterisks are shown in the password prompt.

![screenshot from 2017-03-11 17-41-01](https://cloud.githubusercontent.com/assets/460091/23825214/f6bb0952-0685-11e7-9356-b22cece734e1.png)


## dEBRUYNE-1 | 2017-08-07T17:44:49+00:00
+resolved

# Action History
- Created by: Jaqueeee | 2016-12-22T21:05:20+00:00
- Closed at: 2017-08-07T17:45:09+00:00
