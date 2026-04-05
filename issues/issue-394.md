---
title: Is it possible to lower processor time usage?
source_url: https://github.com/xmrig/xmrig/issues/394
author: rtpoz
assignees: []
labels: []
created_at: '2018-02-09T11:15:39+00:00'
updated_at: '2018-02-11T15:54:45+00:00'
type: issue
status: closed
closed_at: '2018-02-11T15:54:45+00:00'
---

# Original Description
I bought some VPS with 2 core, but I can use only 86400 seconds per day.
Is it possible to change code to lower processor usage to about 90% on one core?

# Discussion History
## 2010phenix | 2018-02-09T21:51:38+00:00
yes 50%, use option -t 1

## rtpoz | 2018-02-09T23:19:15+00:00
It's not working. I already running only one thread.
Thanks for your answer.

## xuxuedong | 2018-02-11T01:26:59+00:00
"but I can use only 86400 seconds per day", are you kidding, it's 24 hours per day?

## xuxuedong | 2018-02-11T01:35:08+00:00
what's meaning of "to about 90% on one core", you want only one core or each core to about 90% cpu usage? if the latter, you can try option "--max-cpu-usage=N    maximum CPU usage for automatic threads mode (default 75)", if the former, it's a little difficult to use only one core to about 90% cpu usage

## xuxuedong | 2018-02-11T01:36:34+00:00
and the title "processor time usage", what's meaing of it?

## rtpoz | 2018-02-11T15:51:14+00:00
The VPS administrator wrote to me that I exceeded the consumption of time (processor time usage). Theoretically it is possible to use 2x86400 s on two cores but I can use only 1 core on 90% of power :(. 

I already found a solution. I'm using 
`cpulimit -l 87 -e xmrig > /dev/null  2>&1 &`

# Action History
- Created by: rtpoz | 2018-02-09T11:15:39+00:00
- Closed at: 2018-02-11T15:54:45+00:00
