---
title: GUI Calendar Incorrect dates
source_url: https://github.com/monero-project/monero-gui/issues/1723
author: keatond
assignees: []
labels:
- bug
- resolved
created_at: '2018-11-02T17:47:18+00:00'
updated_at: '2019-04-26T23:54:35+00:00'
type: issue
status: closed
closed_at: '2019-04-26T23:54:35+00:00'
---

# Original Description
![calendar](https://user-images.githubusercontent.com/428041/47931593-a42a3600-dea5-11e8-8df8-3f766d12bbab.PNG)

Good Afternoon All,

Calendar within the history tab appears to be showing the dates of the month on the incorrect day.

# Discussion History
## sanderfoobar | 2018-11-03T23:54:29+00:00
+bug

## mmbyday | 2018-11-28T23:42:58+00:00
A few observations to add...

Seems to affect Window operating system. Datepicker is correct on Linux.

Specifically, the off by one bug occurs on March 11, 2018, a day light time change issue.

related: https://stackoverflow.com/questions/1102240/jquery-datepicker-bug

![mar11](https://user-images.githubusercontent.com/40871101/49189675-2e8a7c00-f324-11e8-9fe5-672efc21f26b.PNG)


## mmbyday | 2018-12-06T21:29:47+00:00
It appears this is a bug in qt 5.7.

Can confirm in qt 5.9.5 and as far as 5.11.1, this issue no longer exists. 

Perhaps we should bump up the minimum required qt version? At least this is another reason to do so, sooner than later.

![2](https://user-images.githubusercontent.com/40871101/49612869-cf97b900-f95a-11e8-9dcd-479c253aea37.gif)
 

## mmbyday | 2018-12-07T20:24:00+00:00
https://github.com/monero-project/monero-gui/issues/1787

## sanderfoobar | 2018-12-18T09:24:13+00:00
Related #789

## selsta | 2019-04-26T23:49:52+00:00
Qt 5.9 is required now.

+resolved

# Action History
- Created by: keatond | 2018-11-02T17:47:18+00:00
- Closed at: 2019-04-26T23:54:35+00:00
