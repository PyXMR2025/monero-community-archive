---
title: 'v0.13.0.1-RC1 + Whonix: sync stalls, need manual restart'
source_url: https://github.com/monero-project/monero/issues/4469
author: qubenix
assignees: []
labels: []
created_at: '2018-09-29T19:24:51+00:00'
updated_at: '2018-10-14T23:21:13+00:00'
type: issue
status: closed
closed_at: '2018-10-14T23:21:13+00:00'
---

# Original Description
OS: Qubes r4.0 + Whonix 14 (Debian Stretch)

Related: #4468

When using `torsocks` I get stacktrace spam and syncing will always quit at some point requiring a manual restart (even though outbound connections still exist).

Stacktrace spam is likely #4365. I'm pretty sure unrelated to the sudden stop in syncing since I've seen them happen independent each other, but I mention it just in case it's relevant.

log-level 1, quit syncing: http://termbin.com/3gxl
log-level 4, quit syncing: http://termbin.com/mutz

# Discussion History
## moneromooo-monero | 2018-09-30T08:53:15+00:00
Does 4469b0c41e8a2428cd2b5d34bd217d1ae339b096 make any difference ?

## qubenix | 2018-09-30T23:05:01+00:00
No, that commit was already in my build.

I've got another log here, not run by `systemd`, where even a stop signal is not recognized: http://termbin.com/nmyg.

Previous to this comment all my logs were run by `systemd` and always responded to a `systemctl stop/restart`.

## moneromooo-monero | 2018-09-30T23:07:50+00:00
So you tried with it, and... not without it ? Then you do not know if it makes a difference, right ?

## qubenix | 2018-09-30T23:13:15+00:00
Correct, I'll try without it and report back.

## qubenix | 2018-09-30T23:30:11+00:00
Without that commit I can't get any connections: http://termbin.com/jh1m.

## qubenix | 2018-10-14T23:21:13+00:00
I'm closing this because it was most likely an error on my part in the way I was running `monerod`. I'm able to run without stalling when using `monerod` the way mentioned in #4468.

# Action History
- Created by: qubenix | 2018-09-29T19:24:51+00:00
- Closed at: 2018-10-14T23:21:13+00:00
