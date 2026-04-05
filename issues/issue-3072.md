---
title: database de-initilization for saving memory during paused mining after a period
  of time
source_url: https://github.com/xmrig/xmrig/issues/3072
author: JacksonChen666
assignees: []
labels: []
created_at: '2022-06-16T21:12:50+00:00'
updated_at: '2022-06-17T04:34:02+00:00'
type: issue
status: closed
closed_at: '2022-06-17T04:34:02+00:00'
---

# Original Description
# the problem
when xmrig loads the randomx database, it uses quite a lot of memory (2GB+ memory).
sometimes, when not mining for long periods of time (like paused because running on battery for a long time now, like 30 minutes), it's not being used, and pretty much becomes wasted RAM that could be used for the rest of the system.

# the proposed solution
freeing up that used RAM (of randomx database, which is pretty much wasted RAM at that moment) could be helpful minimizing the use of RAM by the program when it isn't actively using it.
how about, a configuration option to say after how many seconds/minutes of paused mining should xmrig unload the randomx database.

# how it is applicable
well, on systems that gets used and not used for a long period of time and doesn't have as much RAM necessary for everything, RAM can become a pretty limited resource. or even more limited

# alternative solutions
- use `--light-mode`. but i'm pretty sure that's pretty detrimental to the hash rate.
- depending on the system to swap the memory instead of bothering with this issue at all (is it a good idea?)


# Discussion History
## Spudz76 | 2022-06-16T21:38:20+00:00
Since pausing stays connected and the state machine requires active dataset (algo "ready") to be connected, this would be extra complicated to implement.

Most users especially on windows would rather the hugepages stay allocated since releasing them could mean you never get them back until a reboot.  Otherwise they would quit and relaunch later (rather than pause, which again doesn't even disconnect).

I want it to disconnect while paused myself, so the autodiff doesn't fall to the minimum and then spam the server upon resume.  Even that seemed difficult to implement, the dataset is even deeper than that.

* yes that trashes hashrate and can't be changed on-the-fly
* no you can't "unlock" and allocation that was formed with "lock" to make it swappable on-the-fly

## JacksonChen666 | 2022-06-17T04:34:02+00:00
@Spudz76 thanks for the explanation.

will be closing. re-open if the plan could be feasible.

# Action History
- Created by: JacksonChen666 | 2022-06-16T21:12:50+00:00
- Closed at: 2022-06-17T04:34:02+00:00
