---
title: 'monerod: [windows] Mysterious "disk leak," while Monero daemon is running'
source_url: https://github.com/monero-project/monero/issues/8742
author: opportunistic
assignees: []
labels:
- bug
- low priority
created_at: '2023-02-15T20:32:42+00:00'
updated_at: '2023-12-09T12:17:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This is driving me absolutely crazy, whenever I have monerod.exe running (after fully syncing), Windows begins to report disk free space decreasing at a pretty alarming rate, around 15GB every hour.  However, there is are not actually any new data being written to the disk...

WinDirStat reports the proper free space after fully scanning all files, and Windows only recognizes that this space is not actually allocated to any files after a full restart.

Something potentially worth noting is that this is being performed on an SSD with the operating system installed on it and also Veracrypt full disk encryption.

Please let me know if anyone has a solution or if more information is needed, this is driving me absolutely crazy.

# Discussion History
## selsta | 2023-02-15T20:38:46+00:00
Could you post your monerod config?

## opportunistic | 2023-02-15T20:59:25+00:00
> Could you post your monerod config?

I do not believe I have one, I'm using Monero GUI wallet and I have not changed anything besides `--out-peers=512`

## selsta | 2023-02-15T21:19:05+00:00
I'd recommend against setting such a high number of out peers but that's unrelated to your issue.

We have never received a similar report before so I suspect it's related to Veracrypt. Can you copy the blockchain to an external unencrypted drive and see if you can reproduce the issue?

## hyc | 2023-02-15T21:23:33+00:00
> copy the blockchain to an external unencrypted drive

Move the entire bitmonero folder and tell monerod where to find it. I'm suspecting logfile activity, not database activity.

## opportunistic | 2023-02-15T22:33:21+00:00
> > copy the blockchain to an external unencrypted drive
> 
> Move the entire bitmonero folder and tell monerod where to find it. I'm suspecting logfile activity, not database activity.

Watching the process with Process Monitor, there's not really any log file activity... mostly just ReadFile and WriteFile on the database.

## opportunistic | 2023-02-16T17:33:21+00:00
Update!

After disabling this option on my blockchain folder (Windows seems to turn it on automatically sometimes), it seems like the "leak" has stopped!

![image](https://user-images.githubusercontent.com/109391343/219443146-60b2f6a2-32cf-46ba-a967-398d4664209e.png)

I'm not sure why this interaction occurs, would be worth fixing or warning the user about, though.


## selsta | 2023-09-21T17:30:14+00:00
@hyc do you know anything about how this Windows option interacts with LMDB?

# Action History
- Created by: opportunistic | 2023-02-15T20:32:42+00:00
