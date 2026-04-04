---
title: Reddit icon messed up on Hangouts page.
source_url: https://github.com/monero-project/monero-site/issues/411
author: applebaum
assignees: []
labels: []
created_at: '2017-09-22T13:12:40+00:00'
updated_at: '2017-10-24T19:40:42+00:00'
type: issue
status: closed
closed_at: '2017-10-24T19:40:42+00:00'
---

# Original Description
Noticed that in Firefox and Chrome reddit social icon is displaying incorrectly on https://getmonero.org/community/hangouts/.
![getmonero-hangouts](https://user-images.githubusercontent.com/26916516/30745934-a78c3bc0-9fb0-11e7-97c8-fe7f643ef9c3.png).

 

# Discussion History
## mattcode55 | 2017-09-22T13:18:43+00:00
How long has it been like that? [Git blame shows that this stuff hasn't been touched for a few months](https://github.com/monero-project/monero-site/blame/master/css/custom.css#L3232).

## applebaum | 2017-09-22T13:20:07+00:00
@mattcode55 can't say, first time I've visited that page.

## rehrar | 2017-09-22T14:06:26+00:00
Everything was working correctly when I put it up the first time. I am aware of the issue, and I've fixed it. I will be putting out a Spring Cleaning patch in a couple days or so. It will address this. 

## erciccione | 2017-10-22T12:04:09+00:00
+bug

# Action History
- Created by: applebaum | 2017-09-22T13:12:40+00:00
- Closed at: 2017-10-24T19:40:42+00:00
