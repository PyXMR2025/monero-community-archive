---
title: '[6.16.2] Ghostrider auxiliary threads do not follow "priority" setting'
source_url: https://github.com/xmrig/xmrig/issues/2825
author: electroape
assignees: []
labels:
- bug
created_at: '2021-12-20T09:10:43+00:00'
updated_at: '2022-01-25T14:54:00+00:00'
type: issue
status: closed
closed_at: '2022-01-25T14:54:00+00:00'
---

# Original Description
So Ghostrider has additional threads equal to the amount of 'usual' threads. These threads do not follow priority set by "priority" setting. I.e if i set it to 0, i.e idle, i can see that auxiliary threads are set to normal priority. It probably makes sense to set their priority one level higher than for main threads, but not 'normal' as this may interfere with foreground tasks the "priority" setting is supposed to address. Although personally haven't observed such cases.

# Discussion History
# Action History
- Created by: electroape | 2021-12-20T09:10:43+00:00
- Closed at: 2022-01-25T14:54:00+00:00
