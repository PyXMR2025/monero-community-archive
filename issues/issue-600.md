---
title: How to change default CPU usage
source_url: https://github.com/xmrig/xmrig/issues/600
author: zyjsuper
assignees: []
labels:
- question
created_at: '2018-05-03T08:50:13+00:00'
updated_at: '2018-06-17T18:05:44+00:00'
type: issue
status: closed
closed_at: '2018-06-17T18:05:44+00:00'
---

# Original Description
Please tell me,Thx.

# Discussion History
## zyjsuper | 2018-05-03T09:10:37+00:00
I set m_maxCpuUsage(25) 
but it run use 100% of cpu usage always.
how to solve it.


## BearBang7 | 2018-05-03T12:16:24+00:00
@zyjsuper how many core have your cpu ?

## ghost | 2018-05-03T12:24:50+00:00
maxCpuUsage - this option only to set how miner can use one CPU in percent from 1% to 100%.
If you need usage of CPU not at full capacity just don`t use all threads.
"max-cpu-usage": 75 - load one CPU in percent
"threads": - loading of CPU (simple if have 4 CPUs and use 4 -> get 100% loading.)

## zyjsuper | 2018-05-03T12:29:19+00:00
1core and 2core,all have 

## Meyer01 | 2018-05-04T12:51:42+00:00
As i know, if you set "threads": 0 than xmrig will calculate the optimal number of cores for use based on CPU cache. 
You can manualy set number of cores for mining by set the number in "threads": 
Xmrig cant use percents of core. If you have 1 core it would be 100% always. If you have 4 cores for example you can choose 25%,50%.75% and 100% of CPU. If 2 cores you have only 50% or 100% options.

# Action History
- Created by: zyjsuper | 2018-05-03T08:50:13+00:00
- Closed at: 2018-06-17T18:05:44+00:00
