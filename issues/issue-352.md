---
title: Change display details
source_url: https://github.com/xmrig/xmrig/issues/352
author: Hardtack222
assignees: []
labels: []
created_at: '2018-01-19T09:59:45+00:00'
updated_at: '2018-11-05T12:46:34+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:46:34+00:00'
---

# Original Description
I would like to change my display to show all settings used.
Currently shows
* VERSION:
* HUGE PAGES:
* CPU:
* CPU L2/L3
* THREADS:
* POOL #1 
* COMMANDS:

What i would like to do is change it, so it shows all the current values of all the configurable options. 

I know its possible i just don't know how... if someone could guide me... or just point me into the right direction... THAT WOULD BE GREAT!


# Discussion History
## xmrig | 2018-01-19T18:41:26+00:00
All information located in one file https://github.com/xmrig/xmrig/blob/master/src/Summary.cpp several `print_*` functions. It can be extended.
Thank you.

# Action History
- Created by: Hardtack222 | 2018-01-19T09:59:45+00:00
- Closed at: 2018-11-05T12:46:34+00:00
