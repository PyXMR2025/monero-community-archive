---
title: --cpu-priority doesn't seem to do anything
source_url: https://github.com/xmrig/xmrig/issues/2505
author: Joe23232
assignees: []
labels: []
created_at: '2021-08-01T13:16:16+00:00'
updated_at: '2021-08-03T10:38:50+00:00'
type: issue
status: closed
closed_at: '2021-08-03T10:38:50+00:00'
---

# Original Description
When running `xmrig.exe -o qrl.miningocean.org:3333 -u <wallet_address> -p <worker_name> -a rx/0 -k --huge-pages-jit --cpu-priority 2`

it doesn't seem to make a difference if I set `--cpu-priority` to `1` `3` `4` etc. It all uses the same amount of processing power. Even if I set it to `0`.

I compiled `xmrig` from the `dev` branch.

# Discussion History
## Spudz76 | 2021-08-01T18:54:45+00:00
It sets the task priority but if the computer is doing nothing else then even lowest will just use everything.  More about how quick it gets put to the back-burner when other tasks are running.

You should note a different task priority in task manager for each of the numbers.

## Joe23232 | 2021-08-01T22:26:24+00:00
@Spudz76

> It sets the task priority but if the computer is doing nothing else then even lowest will just use everything. More about how quick it gets put to the back-burner when other tasks are running.

If i set it to `0`, then it is doing a lot, even if I am using my PC. 

> You should note a different task priority in task manager for each of the numbers.

Hmm can't quite seem to find that.

## Joe23232 | 2021-08-01T22:58:51+00:00
@Spudz76 Ah right I think I get what you mean like if I am using the computer but hardly anything is running then it sets the task prioriety accordingly. I see, thanks mate.

## Spudz76 | 2021-08-02T19:56:35+00:00
Well it's more that it sets xmrig to "Low" priority, but if there are no other things to do it will run as if it were "Highest" until something else with higher priority wants CPU then it will shelve xmrig.  But this occurs in microseconds so the other app will still lag (there is no "padding time" so the moment the higher priority app seems to be waiting for disk access or such xmrig takes back over instantly.  So it doesn't help with choppy response only ensures if the other app has a lot of CPU work to do then xmrig will be pushed away first.  So things should complete faster but while it's waiting for input or whatever, xmrig is going to run 100% as hard as it ever does.  It's a priority, not a limiter.

## Joe23232 | 2021-08-02T22:23:32+00:00
@Spudz76 Is there a limiter that can be set via flags?

## Spudz76 | 2021-08-03T10:07:03+00:00
No.  The only backend with any sort of throttling is the CUDA backend which has `bsleep` for doing nothing for N milliseconds between job fragments (of course reduces hashrate).  I have long wished the other backends also had `bsleep` for just this sort of thing.

## Joe23232 | 2021-08-03T10:38:43+00:00
THanks anyways mate @Spudz76 

# Action History
- Created by: Joe23232 | 2021-08-01T13:16:16+00:00
- Closed at: 2021-08-03T10:38:50+00:00
