---
title: Ryzen 7 1700x Crach/freeze
source_url: https://github.com/xmrig/xmrig/issues/1588
author: Advantage1
assignees: []
labels:
- stability
created_at: '2020-03-08T12:27:55+00:00'
updated_at: '2020-08-31T05:47:26+00:00'
type: issue
status: closed
closed_at: '2020-08-31T05:47:26+00:00'
---

# Original Description
**Describe the bug**
When diff is grow more when 90k
ver 5.3.0-msvc is crached
ver 5.4+-msvc is freezed, speed down to 10-12 on each core

ver 5.8.2-gcc - work stable

**Required data**
 - xmrig.exe -o gulf.moneroocean.stream:10016 -u *** -p **:**@**.** --donate-level=1
 - Windows 10
 - Ryzen 7 1700x


# Discussion History
## cryptonius | 2020-03-20T14:28:31+00:00
I've noticed the app closing on me out of a sudden. Ryzen 3600 here.

## Spudz76 | 2020-03-23T06:22:40+00:00
#1506 probably related / caused by new Win10 19xx patch cpu scheduler changes

Set threads to `-1` all the way across (no hard binding to cores) and don't use `priority` setting

## xmrig | 2020-08-31T05:47:26+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

# Action History
- Created by: Advantage1 | 2020-03-08T12:27:55+00:00
- Closed at: 2020-08-31T05:47:26+00:00
