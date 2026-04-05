---
title: maximum cpu usage can not be lower to 50%?
source_url: https://github.com/xmrig/xmrig/issues/366
author: axe-usat
assignees: []
labels: []
created_at: '2018-01-27T21:38:43+00:00'
updated_at: '2018-01-31T08:41:25+00:00'
type: issue
status: closed
closed_at: '2018-01-31T08:41:25+00:00'
---

# Original Description
i tried with two cores and always take me 50% of my pc. can not put in a lower limit modifying the code?

# Discussion History
## ondradus | 2018-01-28T16:48:05+00:00
First of all, how many threads in total do you have ? 2 ? 
What CPU do you have ? There is a chance you have 2 physical cores + 2 more threads if you have a newer Intel CPU. (Which would make 4 threads in total, but you only tried to use 2 threads).

You can actually modify the maximum CPU usage in the code.

## axe-usat | 2018-01-29T00:49:57+00:00
in which part in the configuration or in which part of code? i have 2 cores so the minimum is 50%. but i want to put it in a lower limit. 

## xmrig | 2018-01-31T08:41:25+00:00
With 2 cores minimum is 50% (1 core of 2).
Thank you.

# Action History
- Created by: axe-usat | 2018-01-27T21:38:43+00:00
- Closed at: 2018-01-31T08:41:25+00:00
