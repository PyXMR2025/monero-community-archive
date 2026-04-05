---
title: Is huge pages working?
source_url: https://github.com/xmrig/xmrig/issues/2493
author: Joe23232
assignees: []
labels: []
created_at: '2021-07-24T12:45:48+00:00'
updated_at: '2021-07-27T10:39:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```cmd
[2021-07-24 22:42:27.166]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (6 ms)
[2021-07-24 22:42:30.826]  randomx  dataset ready (3660 ms)
[2021-07-24 22:42:30.826]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2021-07-24 22:42:30.850]  cpu      READY threads 4/4 (4) huge pages 0% 0/4 memory 8192 KB (23 ms)
```

Hi, I am a little concerned about this, I have enabled huge pages but it shows 0% over here, is this something bad or something? Is it still not working? I ran it as administrator and this is on Windows 10.

# Discussion History
## Spudz76 | 2021-07-24T18:35:55+00:00
Windows will fragment memory quickly after boot try running immediately/first thing after clean boot and it might camp the pages.

It cannot allocate 2MB pages if Windows already stuck 1KB of garbage within the range (must be 2MB contiguous, and 1168+4 of them)

## Joe23232 | 2021-07-25T06:41:39+00:00
@Spudz76 

> Windows will fragment memory quickly after boot try running immediately/first thing after clean boot and it might camp the pages.

Yeah I could try that.

> It cannot allocate 2MB pages if Windows already stuck 1KB of garbage within the range (must be 2MB contiguous, and 1168+4 of them)

Is there a way to some how fix this though other than a reboot?

## Spudz76 | 2021-07-27T02:56:45+00:00
Nope.  Possibly, with a Windows service that maybe could permanently hang on to allocations, made at boot, and never give them up except via API request to xmrig.  But process security might make that impossible (for a separate xmrig process to directly use allocation pointers made by a system service).

Or if you have like 128GB then Windows sort of can't possibly scatter junk everywhere, there is too much space for it to defile every 2MB.  But that isn't much of a solution, and huge RAM or lots of sticks tends to hurt latency or be terribly expensive (fast and huge, you pay both the fast premium and the huge premium).

I wish there was some registry key that made it spend more time keeping memory defragged, and not allocate where it would trash a 2MB zone if it doesn't have to.  But that also makes things launch slower (due to memory allocation looking at more things before it just picks somewhere randomly).  I think it also randomizes on purpose so that things won't be in predictable places in memory, that's more exploitable.

What I do is just always leave the xmrig window open and just hit P to pause.  Then it retains its allocations but stops chewing CPU so I can go do other things like play Warzone.  Then when I'm done with that I come back and hit R and it resumes without releasing any memory.  But since I run MoneroOcean autoswitching occasionally there is a CPU usage spike if it switches algos (even if paused it still does the prep phase on switch).  Sometimes that hurk-jerks my gaming but not really that often.  Pause stays connected to the pool but just stops doing any work.  Maybe there could be a deep-pause or disconnect-on-pause, that stops mining and also disconnects but stays around camping the memory...

## Joe23232 | 2021-07-27T10:39:12+00:00
Thanks mate sounds like a good idea mate.

# Action History
- Created by: Joe23232 | 2021-07-24T12:45:48+00:00
