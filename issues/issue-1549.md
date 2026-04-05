---
title: Max Cpu Usage
source_url: https://github.com/xmrig/xmrig/issues/1549
author: DogeZillaMeme
assignees: []
labels:
- question
created_at: '2020-02-12T13:09:36+00:00'
updated_at: '2020-08-28T16:41:44+00:00'
type: issue
status: closed
closed_at: '2020-08-28T16:41:44+00:00'
---

# Original Description
Hello,i have 200 Servers and i waint to put all to mine monere,but i want to make this option to work , Max Cpu Usage 10% ,i want to user only 10 procent of CPU
Is posible to make this on curent version?
Thank you

# Discussion History
## xmrig | 2020-02-12T16:23:24+00:00
https://github.com/xmrig/xmrig/blob/master/doc/CPU_MAX_USAGE.md

## DogeZillaMeme | 2020-02-13T14:24:56+00:00
I see that,but i want to know if is posible to put this option Max Cpu Usage 10% 

## bruto786 | 2020-03-04T13:39:22+00:00
https://scoutapm.com/blog/restricting-process-cpu-usage-using-nice-cpulimit-and-cgroups
use cpu limit

## Spudz76 | 2020-03-22T02:05:39+00:00
The max cpu usage controls how many threads the auto-configuring will decide to use.
If you have four cores then your minimum "cpu usage" would be 25% (one core) and "10%" would be essentially ignored (you get whatever is greater than zero but still allows any work to occur).
xmrig does no throttling, use cpulimits for that as suggested

I run xmrig on servers too and they don't even notice it as long as it's process priority (nice level) is set high enough (5 at least, 15 if that's not enough, 19 is max which is least important).  The scheduler will put it on the back burner whenever anything else wants CPU.  The `priority` setting in the config will select various nice levels but I forget how they map to exact nice levels.

# Action History
- Created by: DogeZillaMeme | 2020-02-12T13:09:36+00:00
- Closed at: 2020-08-28T16:41:44+00:00
