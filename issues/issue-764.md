---
title: '[Feature Request] Auto-populate ideal mining threads in GUI'
source_url: https://github.com/monero-project/monero-gui/issues/764
author: SamsungGalaxyPlayer
assignees: []
labels:
- resolved
created_at: '2017-06-13T19:04:45+00:00'
updated_at: '2018-11-18T13:45:28+00:00'
type: issue
status: closed
closed_at: '2018-11-18T13:45:28+00:00'
---

# Original Description
Would it be possible to automatically populate the number of CPU mining threads in the GUI? I was looking around and there seem to be ways in several systems to check the size of the L3 cache. How difficult would this be to implement?

Windows example:

`wmic cpu get L3CacheSize`

I believe this will help new users, who can help the network in an ideal way without needing to look up the specs for their processor.

# Discussion History
## jonathancross | 2017-06-16T20:38:23+00:00
I'd recommend against making the default anything more than 1 thread.

My reasoning is:
1. Noobs trying to "help the network" should not have a degraded experience with their computer slowing down, getting hot, etc.
2. If they are curious about mining, they can at least learn a bit about their own system so they are making a _decision_ about the resources being allocated.
3. Users who are really interested in mining should probably be using an optimized miner like 
`xmr-stak-cpu`.

The current input field is not ideal, but unless we can easily and reliably determine how many threads are available, I think this is fine for now.  If we can get CPU info without wasting a lot of dev time or introducing cross-platform bugs / flakey behavior (I'm skeptical) --  a dropdown would be preferable to prevent mistakes and give users a sense for how much of their overall CPU cycles are being allocated.

## medusadigital | 2017-08-07T19:05:49+00:00
i tend to agree with @jonathancross.

however, leaving it open a few more days before closing

## doobilydo | 2017-08-22T22:56:50+00:00
I believe this is causing the threads to reset back to 1 if the application is restarted. I changed it to 4, but it didn't save that setting. Is this the desired functionality? 

## erciccione | 2018-11-18T13:43:42+00:00
Few days have passed

+resolved

# Action History
- Created by: SamsungGalaxyPlayer | 2017-06-13T19:04:45+00:00
- Closed at: 2018-11-18T13:45:28+00:00
