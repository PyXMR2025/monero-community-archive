---
title: Windows x64 Beta 2 GUI missing November 1, 2015
source_url: https://github.com/monero-project/monero-gui/issues/789
author: robricc
assignees: []
labels:
- bug
- resolved
created_at: '2017-07-07T17:45:57+00:00'
updated_at: '2019-04-27T00:00:39+00:00'
type: issue
status: closed
closed_at: '2019-04-27T00:00:39+00:00'
---

# Original Description
The date selector in the History tab for November 2015 starts at November 2nd.

![monero_nov2015](https://user-images.githubusercontent.com/29985373/27969809-6ae82cf6-631a-11e7-9927-753040add784.png)
 

# Discussion History
## MaxXor | 2017-07-09T12:36:12+00:00
For me it's showing the dates correctly on Windows 7 x64. Can you provide more information on how to reproduce this?

![history](https://user-images.githubusercontent.com/7271470/27993952-6de2cd86-64b3-11e7-915c-bee045b7e5f2.png)


## robricc | 2017-07-10T13:55:01+00:00
I am only trying out the GUI because it's easier to pinpoint what transactions happen on what date. So, the wallet I have open is a view-only wallet that has been functioning fine via CLI for years. I'm also connecting to a remote node. I don't think that these factors are likely to contribute to the issue I'm seeing.

I do notice that your week starts on Monday. Since I'm am in the US, my week starts on Sunday. Other than that, I just unzipped the current GUI binary linked from Reddit and restored a wallet from keys (view-only). Once it was done syncing the wallet, I then noticed this issue.

## jonathancross | 2017-07-16T20:21:04+00:00
The date picker is a bit wonky.  Although there is no reason the first of any month should be missing, I did notice that your start date is _after_ your end date (and the end date is December).  Even though it seems as though you can type in dates, I cannot (on a mac).  I had to use the mouse and click back through all months, then select a specific day.  Please try that and see what happens.

## medusadigital | 2017-08-07T19:48:54+00:00
would consider this as a bug, even if exotic. 

+bug

## Jaqueeee | 2017-08-21T06:58:15+00:00
I can't reproduce this. Seems to be related to the locale setting since OP's week starts on a Sunday. Can anyone else confirm this? Haven't found any reported Qt bugs regarding this. 

## jonathancross | 2017-08-23T19:31:36+00:00
I changed my "Language & Region" settings here on my mac to make Sunday the first day of the week, but could not reproduce the bug.

Interesting to note that October seems to just be shifted one day forward, deleting Nov 1. (November 2nd, 2015 being Monday is correct).

## selsta | 2019-04-26T23:52:53+00:00
This was most likely a bug in an older Qt version. We require Qt 5.9 now.

+resolved

# Action History
- Created by: robricc | 2017-07-07T17:45:57+00:00
- Closed at: 2019-04-27T00:00:39+00:00
