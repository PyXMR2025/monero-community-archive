---
title: Unified Code Issue with German seed letters on Windows
source_url: https://github.com/monero-project/monero/issues/938
author: Milaui
assignees: []
labels:
- bug
created_at: '2016-07-27T19:13:39+00:00'
updated_at: '2018-05-10T17:32:52+00:00'
type: issue
status: closed
closed_at: '2018-05-10T17:32:52+00:00'
---

# Original Description
Hi,
I found an issue that occurs only on Windows. If a seed is created with German word that contain ä/ü/ö then, the letters are appear as ä=├ñ, ö= ├Â, ü= ├╝. There is no problem with that on Linux. 
So if you try to import a wallet created on Linux with a seed word "Müll" then "Müll" won't work on Windows and you must use "M├╝ll"
Good Luck!


# Discussion History
## moneromooo-monero | 2016-07-31T16:53:00+00:00
Looks like 6 extra bytes, assuming copy/pasting did not lose any information. Do you know if your terminal supports UTF-8 ? IIRC, Windows uses UTF-16 by default (and lower endian to boot).


## Milaui | 2016-09-05T20:55:16+00:00
I am sorry, not an expert. I just used the standard Windows "cmd" terminal. Don't know wether it supports UTF-8 or 16... What I know is that I did copy and past my seed. I typed every single letter ;-).


## dEBRUYNE-1 | 2018-01-08T12:28:32+00:00
+bug

## dEBRUYNE-1 | 2018-05-10T17:20:33+00:00
+resolved

# Action History
- Created by: Milaui | 2016-07-27T19:13:39+00:00
- Closed at: 2018-05-10T17:32:52+00:00
