---
title: Automatic miner pause
source_url: https://github.com/xmrig/xmrig/issues/2559
author: AC1003
assignees: []
labels: []
created_at: '2021-08-25T08:59:45+00:00'
updated_at: '2025-06-16T20:51:05+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:51:05+00:00'
---

# Original Description
Hi there. I have installed and run the software, but after a few hours I get a sign that says "mining paused, press any key to resume." When I press a key the tab closes, and when I open it again the same poster appears that produces the same result.
I would like to know how I can fix this error and for what reason it occurs.
Thanks.


# Discussion History
## DeeDeeRanged | 2021-08-25T11:25:57+00:00
Linux/Windows?

## Spudz76 | 2021-08-25T19:48:38+00:00
Never heard of that message, the real Pause mode says:

```
[2021-08-25 13:47:03.539]  miner    paused, press  r  to resume
[2021-08-25 13:47:04.934]  miner    resumed
```

And it only accepts `r` to resume, not any-key.

So I'm guessing you're on Windows and using a BAT file which will say press any key after xmrig exits (if you put a `pause` shell command at the end of the BAT file)...

The only other automatic pause mode is from Battery detection, so is it a laptop and do you have `pause-on-battery` enabled?

## AC1003 | 2021-08-26T08:39:13+00:00
> Never heard of that message, the real Pause mode says:
> 
> ```
> [2021-08-25 13:47:03.539]  miner    paused, press  r  to resume
> [2021-08-25 13:47:04.934]  miner    resumed
> ```
> 
> And it only accepts `r` to resume, not any-key.
> 
> So I'm guessing you're on Windows and using a BAT file which will say press any key after xmrig exits (if you put a `pause` shell command at the end of the BAT file)...
> 
> The only other automatic pause mode is from Battery detection, so is it a laptop and do you have `pause-on-battery` enabled?

I use a battery-free hp desktop with windows 10 operating system.

# Action History
- Created by: AC1003 | 2021-08-25T08:59:45+00:00
- Closed at: 2025-06-16T20:51:05+00:00
