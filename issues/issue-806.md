---
title: Command line option for -l, --log-file=FILE donesn't work after 2.5
source_url: https://github.com/xmrig/xmrig/issues/806
author: JustHoldit
assignees: []
labels:
- bug
created_at: '2018-10-16T13:57:44+00:00'
updated_at: '2024-04-02T18:30:47+00:00'
type: issue
status: closed
closed_at: '2018-11-05T14:44:09+00:00'
---

# Original Description
The command line option for log to file does not work in the last few releases. I have not tested all versions but it looks to have appeared in 2.6.

-l, --log-file=FILE      log all output to a file

xmrrig seems to ignore it

# Discussion History
## welj | 2018-10-16T14:04:59+00:00
works that me  -lstats.log 

## JustHoldit | 2018-10-16T17:29:11+00:00
does:   --log-file=lstats.log work for you?

## JustHoldit | 2018-10-16T17:38:39+00:00
I have confirmed that:  /usr/rig/xmrig -l/path/to/filename.log  --background 
works for me. 

This however does not work
/usr/rig/xmrig --log-file=/path/to/filename.log --background

## xmrig | 2018-10-17T02:34:28+00:00
`./xmrig --url donate.v2.xmrig.com:3333 --log-file=xmrig.log --background` works fine for me, however mixed configuration config file + command line seems broken.
Thank you.

## snipeTR | 2018-10-17T07:40:32+00:00
./xmrig --url donate.v2.xmrig.com:3333 --log-file=./xmrig.log --background

## maravento | 2024-04-02T18:30:45+00:00
https://github.com/xmrig/xmrig/issues/3455

# Action History
- Created by: JustHoldit | 2018-10-16T13:57:44+00:00
- Closed at: 2018-11-05T14:44:09+00:00
