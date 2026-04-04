---
title: monerod excessive hard drive writes
source_url: https://github.com/monero-project/monero/issues/8189
author: undeath
assignees: []
labels: []
created_at: '2022-02-21T14:37:01+00:00'
updated_at: '2022-03-27T16:01:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I noticed that monerod writes a lot of data to my drives, a lot more than what would be expected from keeping the blockchain database up to date.

Within 120h (5d) of running my monerod IO stats (reported by systemd) are: IO: 204.7G read, 407.2G written

That's an average of almost 1mb/s. Those statistics only include keeping up to date with an already synced blockchain. This does not look right.

I'm running v0.17.3.0.

# Discussion History
## moneromooo-monero | 2022-03-21T16:35:18+00:00
Is this while syncing historical blocks or just keeping up with new blocks after initial sync ?

## undeath | 2022-03-21T16:40:40+00:00
just keeping up with new blocks

## moneromooo-monero | 2022-03-21T17:45:51+00:00
Thanks. It does seem excessive then.

## moneromooo-monero | 2022-03-21T18:21:21+00:00
Here's something you can try, to see if it changes the write amount:

<+moneromooo> OK. Do you have a setting suggestion for --db-mode to see if that is the reason for the high usage ?
< hyc> I usually suggest fast:async:1000000
< hyc> but it also won't make much difference if there's not enough RAM to cache more dirty pages
< hyc> if they can run with `/usr/bin/time -v` that will give full stats from getrusage()
< hyc> you'd be looking for the pagefault counts to decrease with a looser sync-mode

So: --db-sync-mode fast:async:1000000


## undeath | 2022-03-22T17:26:02+00:00
Looking much better with that setting. Node has been running for 22h now and current stats are `IO: 33.9G read, 8.4G written`. Also RAM consumption is lower (now 3.7gb, before 5gb).

## moneromooo-monero | 2022-03-27T07:50:07+00:00
Still the same after a similar time from what you originally reported ?

## undeath | 2022-03-27T10:54:03+00:00
Yes, significantly less writes with same amount of reads. After 137h (5.7d) the process is at `IO: 212.7G read, 61.9G written`. RAM consumption went up again  and is now at 6.1gb.

## XfedeX | 2022-03-27T15:56:54+00:00
Shouldn't the default DB config be changed?

## selsta | 2022-03-27T15:58:40+00:00
@XfedeX then we get countless complaints again that the DB corrupts on Windows.. that's why it got changed in the first place.

## hyc | 2022-03-27T16:01:04+00:00
Have considered changing the default back for everything except Windows...

# Action History
- Created by: undeath | 2022-02-21T14:37:01+00:00
