---
title: monerod stuck on RPi3
source_url: https://github.com/monero-project/monero/issues/4466
author: dawiepoolman
assignees: []
labels: []
created_at: '2018-09-29T05:43:44+00:00'
updated_at: '2018-10-01T20:53:05+00:00'
type: issue
status: closed
closed_at: '2018-10-01T20:28:12+00:00'
---

# Original Description
Hi guys

My RPi3 has been progressing nicely syncing up with he network for about a week now but it started giving some errors then I rebooted.  Now monerod seems to be stuck 12hrs on startup:

![image](https://user-images.githubusercontent.com/2351212/46241509-46449300-c3bb-11e8-8546-ca128a108e07.png)

anything I can validate for corruption?

# Discussion History
## moneromooo-monero | 2018-09-29T08:49:15+00:00
Please provide those error messages, and anything relevant that happened shortly before (eg, did it crash, did you do something unuual, etc). This goes for any bug you report in the future, whether to monero or other software.

If it's not stuck, start it with "--log-level 1", wait for it to be stuck again, then paste those logs too.

When done, you can try starting it with "--db-salvage", which might get past the corruption.

## dawiepoolman | 2018-10-01T18:59:36+00:00
Hi moneromoo

Apologies, I was away for the weekend.  Thx for the guidance.
I ran the log and got a bus error:

<img width="1106" alt="monerod-bus-error" src="https://user-images.githubusercontent.com/2351212/46309454-b1a98300-c5bc-11e8-996e-b8c257e746bd.PNG">

and then when starting with --db-salvage it just hangs again

![image](https://user-images.githubusercontent.com/2351212/46309507-d140ab80-c5bc-11e8-93ef-791512014039.png)

I take the dbse is corrupt?

## moneromooo-monero | 2018-10-01T20:24:48+00:00
Probably. LMDB tends to bus error a lot in that case.

## dawiepoolman | 2018-10-01T20:28:01+00:00
no worries, I will try and re-download from scratch  

## hyc | 2018-10-01T20:47:17+00:00
Actually Bus error is pretty rare, it typically only occurs on misaligned data accesses. Usually a corrupted DB will cause a SIGSEGV. And I know of no situations where a corrupted DB can cause a startup hang.

## dawiepoolman | 2018-10-01T20:53:05+00:00
thx for the pop in hyc
I do recall some blocks seemed to being downloaded and then a few blocks later it looped back and re-downloaded again

# Action History
- Created by: dawiepoolman | 2018-09-29T05:43:44+00:00
- Closed at: 2018-10-01T20:28:12+00:00
