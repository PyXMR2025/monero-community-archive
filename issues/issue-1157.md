---
title: Sync throttle flags
source_url: https://github.com/monero-project/monero/issues/1157
author: Gingeropolous
assignees: []
labels:
- proposal
created_at: '2016-10-01T03:52:12+00:00'
updated_at: '2025-12-19T15:21:17+00:00'
type: issue
status: closed
closed_at: '2025-12-19T15:21:17+00:00'
---

# Original Description
Sorry if I beat you to posting this @fluffypony , but I wanted to expand on the idea.

New Feature - Initial Synchronization (or heavy synch) throttling flag with different levels, or just a general throttling flag. 

Goal - gets at decreasing the Cost of Node metric. 

Rambling thoughts: 

in general, perhaps the "throttle while syncing" should be a flag with different levels. I just had a VPS provider shutdown my service because the initial sync was gobbling the CPU too much and who knows how many other resources. Yeah, I know, this could be addressed with "nice" or whatever, but having it built in might make it function better? I dunno. The bastards could've charged me 15 bucks just to release the server from its banished state. Luckily, they were nice. 

So, if a 5 point scale, 

0 = no throttle 
1 = limit number of incoming connections that can use you to sync during initial sync (default)
2 = no incoming connections during initial sync
3 = no incoming connections keep CPU below 75%
4 = no inc and keep CPU < 50%

Now I have five points. 


# Discussion History
## moneromooo-monero | 2016-10-01T08:35:47+00:00
You have 6 points.


## Gingeropolous | 2016-10-01T14:27:12+00:00
Now I have 5 points. 


## moneromooo-monero | 2016-10-01T16:06:38+00:00
I can't argue with that.


## ghost | 2016-10-02T17:50:27+00:00
Perhaps your node could run a local function such as 'time to validate x signatures' or 'time to fetch x bytes from peers' and use these as internal metrics against which to drive the CPU usage whilst keeping the initial sync time as low as possible?


## ghost | 2016-10-02T17:50:51+00:00
Local *calibration function


## dEBRUYNE-1 | 2018-01-08T12:36:00+00:00
+proposal

## selsta | 2025-12-19T15:21:06+00:00
While explicit CPU percentage limits could be useful in some environments, they're better handled by the runtime or container rather than inside the application. Given the existing resource controls and the long inactivity of this issue, I'm closing this as not planned.

# Action History
- Created by: Gingeropolous | 2016-10-01T03:52:12+00:00
- Closed at: 2025-12-19T15:21:17+00:00
