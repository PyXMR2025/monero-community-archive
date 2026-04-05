---
title: '[Idea] additional setting for pause-on-active'
source_url: https://github.com/xmrig/xmrig/issues/2131
author: moorer2k
assignees: []
labels:
- question
- wontfix
created_at: '2021-02-26T02:37:38+00:00'
updated_at: '2021-04-12T14:10:09+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:10:09+00:00'
---

# Original Description
I was about to write a windows service that did this. Very happy to see it native, however, I don’t pause all together. I just set threads to a lower number while active. Maybe have this as an additional parameter?  

# Discussion History
## xmrig | 2021-02-27T07:08:34+00:00
Hard to implement, threads is not just a number, it is a much more complicated thing with binding to specific cores. Yes it can be a number on single socket CPUs with simple topology, but it is not universal.
Thank you.

## moorer2k | 2021-02-27T09:14:37+00:00
What I was thinking is that, for example, my 3950x is set to 30 threads from my config. When I am doing some programming or playing a game I set it to 20-25 threads, save and then just bump it back up when I’m done. Can the config itself not just be modified and re-saved for the user if that options specified?

## waltzforvenus | 2021-03-03T01:46:27+00:00
what about not automatically calculating the thread number and binding them to the cores but putting an option to switch between a pre configured (lower amount of) threads when there is load on the cpu? There also could be additional settings for different loads and different configurations like a 10% load and a 20% load (arbitrary numbers) option that you can write a parser for e.g. I think that would be useful for people who are mining on their main rigs as I don't really use all my cpu cores all the time and I would rather to utilize them as much as possible.

# Action History
- Created by: moorer2k | 2021-02-26T02:37:38+00:00
- Closed at: 2021-04-12T14:10:09+00:00
