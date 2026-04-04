---
title: Button becomes unusable after clicking
source_url: https://github.com/monero-project/monero-gui/issues/1548
author: stoffu
assignees: []
labels:
- resolved
created_at: '2018-08-23T14:24:48+00:00'
updated_at: '2018-12-17T08:27:31+00:00'
type: issue
status: closed
closed_at: '2018-12-17T08:27:31+00:00'
---

# Original Description
https://streamable.com/qy8da

Switching to a different tab and coming back to the Send tab makes the button enabled again.

# Discussion History
## stoffu | 2018-08-29T09:49:29+00:00
Hmm, looks like this issue applies to everywhere using StandardButton: https://streamable.com/8mqx4

And the cause seems to be on my side, because I get the same issue even when I checkout v0.12.3.0 tags on both monero-gui and monero. FWIW the release binary works just fine for me. I remember the binaries I built some time ago not having this issue. I must have done something to my build environment, but I don't know what...

> QMake version 3.1
Using Qt version 5.11.1 in /usr/local/Cellar/qt/5.11.1/lib


## mmbyday | 2018-12-17T08:08:35+00:00
+resolved
by #1791

## dEBRUYNE-1 | 2018-12-17T08:09:54+00:00
+resolved

# Action History
- Created by: stoffu | 2018-08-23T14:24:48+00:00
- Closed at: 2018-12-17T08:27:31+00:00
