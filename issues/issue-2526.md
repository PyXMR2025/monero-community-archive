---
title: randomx; change Fast to Slow after multiple failed attempts
source_url: https://github.com/xmrig/xmrig/issues/2526
author: APT-ZERO
assignees: []
labels: []
created_at: '2021-08-09T15:34:57+00:00'
updated_at: '2021-08-20T08:53:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi
when ram is enough but other programs don't allow xmrig process to use ram, xmrig will exit (i tried it in last ver)
it's good if you add ability to change randomx fast mode to slow mode after multiple failed attempts to use ram
also please add a parameter for it that we can use in xmrig parameters in cmd

# Discussion History
## Spudz76 | 2021-08-09T17:07:14+00:00
Most users would rather have it be obviously broken, than wasting energy in slow mode automatically.

Imagine all the users that would flood these Issues with "why is this so slow?" when it shouldn't have worked at all because it couldn't use fast mode?  And they only have 8GB and 5GB of bloatware camping memory they won't bother to go clean up (or get more memory, really) unless they literally have to.

Although I could agree with on/off/auto instead of on/off, where auto is not the default.  Then if you choose this fallback mode you'd have to manually set "auto" (default still "on").

## APT-ZERO | 2021-08-09T22:29:47+00:00
@Spudz76 
add feature to change to slow mode after multiple fails, and set this feature 'disabled' by default
then no one will ask "why is this so slow?"

also add another ability to check for free memory each N seconds/minutes, and if enough ram was empty, change to fast mode (exactly how --retries=N and  --retry-pause=N works, but i think it's better to not try filling ram each time to see it's free enough or not, just check if free ram each time and if it was free enough, then stop slow mode and change to fast mode)

it would be something like this :
--randomx-fast-mode-retries=N [Default = 0/disabled] (time that xmrig will try to fill ram)
--randomx-fast-mode-retries-pause=N [Default = ? sec/min] (time to check if enough free mem is available)

## DeeDeeRanged | 2021-08-20T08:53:15+00:00
Another solution is not to have so many processes running in the background if you are memory constrained. I would evaluate the programs needing so much memory. I mine and play games at the same time, mind you I have 16GB and 32GB memory.

# Action History
- Created by: APT-ZERO | 2021-08-09T15:34:57+00:00
