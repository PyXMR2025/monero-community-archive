---
title: Why no colors if log file is not null?
source_url: https://github.com/xmrig/xmrig/issues/103
author: Balzhur
assignees: []
labels:
- wontfix
created_at: '2017-09-08T10:39:05+00:00'
updated_at: '2018-03-14T22:55:55+00:00'
type: issue
status: closed
closed_at: '2018-03-14T22:55:55+00:00'
---

# Original Description
Why? Because you do not know how to strip colors before logging?

# Discussion History
## mnik247 | 2017-09-08T11:12:10+00:00
+1

## xmrig | 2017-09-08T11:51:56+00:00
That right, you know nice and safe code to strip ANSI color escape?
Thank you.

## Balzhur | 2017-09-08T12:07:08+00:00
Not really, bu I'm not a programmer.
This is the way I do it in bash:

> debug() {
> 	[ "${DEBUG}" = "1" ] && echo -en "Debug: [\e[0;32m${@}\e[0m]\n"
> 	echo "`LANG=C /bin/date +'%b %e %H:%M:%S'` `/bin/hostname -s` ${@}" >> ${LOG}
> }

e.g. you print output using some function which duplicates the output to screen with colors and to log in plain text adding regular 'unix style' timestamping. Hope this helps.

## merdecas | 2018-02-28T22:24:46+00:00
+1

# Action History
- Created by: Balzhur | 2017-09-08T10:39:05+00:00
- Closed at: 2018-03-14T22:55:55+00:00
