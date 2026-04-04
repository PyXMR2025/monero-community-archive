---
title: Getting "E couldn't query power status from /sys/class/power_supply" in daemon
  when start mining
source_url: https://github.com/monero-project/monero/issues/9509
author: ludblom
assignees: []
labels:
- question
- linux
- reproduction needed
- more info needed
created_at: '2024-10-09T15:12:50+00:00'
updated_at: '2025-05-05T19:24:37+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
OS: Linux home 6.1.111-1-MANJARO #1 SMP PREEMPT_DYNAMIC Wed Sep 18 21:01:06 UTC 2024 x86_64 GNU/Linux
Monero version: 0.18.3.4-2

I am having the issue with not being able to start the mining because I get the error message `E couldn't query power status from /sys/class/power_supply`. I have seen other closed fault reports [here](https://github.com/monero-project/monero/issues?q=%2Fsys%2Fclass%2Fpower_supply) but most of them point to the [fix](https://github.com/monero-project/monero/issues/2614) that was made back in 2017, so the version I use should already have the fix included..

I run it on a stationary PC so I do not have anything in `/sys/class/power_supply`, so I understand why it complains, but have also tried to start the daemon with the flag `--bg-mining-ignore-battery`, but still give me the same error message.

Anyone who have an idea why?

# Discussion History
## 0xFFFC0000 | 2024-10-11T09:47:04+00:00
I have seen `E couldn't query power status from /sys/class/power_supply`.

I don't think that is a very serious issue. Of course there should be a way to fix it. But IIRC that is more like a warning. 

But the important thing is I don't think it is related to mining. I mean you should be able to easily start the mining without issues.

Can you invest your log and check why is not exactly possible to start mining? 

## gustavokennedy | 2024-11-13T20:00:46+00:00
Hi @ludblom!

Have you tried creating a dummy folder for the battery device?
```
mkdir -p /sys/class/power_supply/BAT0
```

## tankf33der | 2024-12-29T19:01:30+00:00
The same (?) issue on Alpine Linux 3.20, playing around.

## iamamyth | 2025-01-01T19:49:40+00:00
Duplicate of https://github.com/monero-project/monero/issues/9662. Linux fails to make power supply information available when there's trouble configuring the underlying device, typically due to driver/BIOS issues.

## ludblom | 2025-05-05T19:10:22+00:00
> Hi [@ludblom](https://github.com/ludblom)!
> 
> Have you tried creating a dummy folder for the battery device?
> 
> ```
> mkdir -p /sys/class/power_supply/BAT0
> ```

Sorry for late reply, but yes I have but my system do not permitt me to do that action, get:

```
sudo mkdir -p /sys/class/power_supply/BAT0
[sudo] password for ludblom:
mkdir: cannot create directory ‘/sys/class/power_supply/BAT0’: Operation not permitted
```

and do not feel confident with that kind of hot-fixes even though I maybe could do them as true root.

Regarding the conversation by @iamamyth and @tankf33der, I feel that the issue I am facing may be similar if not exactly the same.

# Action History
- Created by: ludblom | 2024-10-09T15:12:50+00:00
