---
title: Mining with the daemon not working on Linux 64-bit VPS with 0.10.2.1
source_url: https://github.com/monero-project/monero/issues/1810
author: ghost
assignees: []
labels: []
created_at: '2017-02-26T21:12:37+00:00'
updated_at: '2017-11-27T19:50:16+00:00'
type: issue
status: closed
closed_at: '2017-11-27T19:50:16+00:00'
---

# Original Description
I tried both regular mining (start_mining [address] [threads] and background mining (adding [true/false] [true/false]) and the status will say "smart mining" or "mining" but it never changes from 0 hashes/sec and the VPS CPU utilization doesn't change either.

# Discussion History
## hyc | 2017-02-26T22:03:48+00:00
Works for me.
```
start_mining 47xxx... 4
2017-02-26 14:01:51.961     7fac45413700        WARN    miner   src/cryptonote_basic/miner.cpp:293      Mining has started with 4 threads, good luck!
2017-02-26 14:01:51.961     7fa79cff9700        INFO    global  src/cryptonote_basic/miner.cpp:399      Miner thread was started [0]
2017-02-26 14:01:51.962     7fa763fff700        INFO    global  src/cryptonote_basic/miner.cpp:399      Miner thread was started [1]
2017-02-26 14:01:51.962     7fa79d7fa700        INFO    global  src/cryptonote_basic/miner.cpp:399      Miner thread was started [2]
2017-02-26 14:01:51.962     7fa7637fe700        INFO    global  src/cryptonote_basic/miner.cpp:399      Miner thread was started [3]
show_hr
Hash rate logging is on
hashrate: 50.0000
hashrate: 52.0000
hashrate: 53.2500
hashrate: 53.8000
hashrate: 54.3333
```

## ghost | 2017-02-26T22:13:29+00:00
@xmr-eric have you tried telling it to ignore the battery status?

And could you mine on this system with version 0.10.1?


## ghost | 2017-02-26T22:38:35+00:00
@NanoAkron That isn't working either. And when I try to stop the smart miner it errors like this:

https://paste.fedoraproject.org/paste/ridvjJkmj7mCVu-hpqLB5F5M1UNdIGYhyRLivL9gydE=

Edit: I never tried mining with 0.10.1

## vtnerd | 2017-02-27T16:12:07+00:00
I see the offending spot in the code. It is triggered in `mining::stop` to "wake-up" the thread from sleeping. This is easy to fix, and I will issue a pull request for it.

And can you try this with debug logging? I am wondering about the target CPU rate calculation, which might telling the mining threads to sleep for an extended period of time resulting in effectively zero hash rate.

## vtnerd | 2017-02-27T16:14:18+00:00
Also tagging @revler1082 who might want to follow this.

## revler1082 | 2017-02-27T17:47:31+00:00
Apologies for the poopie code gents. I'd venture to guess that the more likely reason for the 0 H/s is that the background mining is never actually "starting" because some threshold isn't being met. I should update the status to be a little more verbose (about whether mining is currently paused, etc).

Does your system have the following path: "/sys/class/power_supply/AC/online"?
Assuming it's not the battery, in order for background mining to trigger, the cpu idle percentage has to be >= 90% (BACKGROUND_MINING_DEFAULT_IDLE_THRESHOLD_PERCENTAGE). Are you maybe running something else on the VPS?



## ghost | 2017-02-27T17:47:39+00:00
Here's log level 2. If you want level 3 or 4 let me know

https://paste.fedoraproject.org/paste/BhPvRwkj8T48WLy~ysuUkV5M1UNdIGYhyRLivL9gydE=

## ghost | 2017-02-27T17:48:45+00:00
@revler1082 It won't mine with normal mining or smart mining, so I'm not sure if the problem is just for background mining alone.

## ghost | 2017-02-27T17:55:12+00:00
@revler1082 The CPU utilization is hovering around 5% 24 hours a day with a few spikes to 10%. The only software running is the node and the pool software. And my Linux VPS doesn't have power_supply/AC/online. It has power_supply/ACAD/online. But I'm pretty sure I checked the option for ignore battery.

## revler1082 | 2017-02-27T17:58:32+00:00
@xmr-eric thanks for the info. That path works as well, so I don't think it's a battery issue. Just a side note, the ignore battery only kicks in if the code fails to find out about battery power, so because you have that path, it WILL find out whether you're plugged in or not, and it will have to be plugged in for mining to start.

There's definitely something more going on since mining normally should be exactly the same as before, I didn't mess with anything in there, but let me check it out.


## vtnerd | 2017-02-28T02:55:51+00:00
Is the VPS a container? How are you getting the CPU idle statistics (top, etc.)? Can you run `head - n 1 /proc/stat` - which just prints out the first line containing CPU statistics.

## doobilydo | 2017-03-01T01:21:41+00:00
So, this looks like it's certainly a defect in the code that is affecting the normal mining as well. I initially thought this was specific to @xmr-eric's setup.

I'm also, now, unable to establish any hashrate with mining, smart or regular, on **wallet-cli** and **monerod**. My issue for this is #1821, due to the previous uncertainty of this issue, and the fact that @hyc appears to not have problems.

## ghost | 2017-03-03T05:25:30+00:00
@vtnerd I don't know how to tell if it's a container. I assume you're asking if it's a dedicated machine, and I don't think it is. I get statistics of stuff like CPU load from the host website, which shows an image like this: https://i.imgur.com/VjFLqVS.png

If I run that `head` command it simply says "==> standard input <==" with nothing below that text. Instead if I run `top` it spits out this: https://paste.fedoraproject.org/paste/MmEgjKjeEJLC5vwX2SBNIl5M1UNdIGYhyRLivL9gydE=

Edit: this is with non-smart mining on 1 thread (0 h/s)

## vtnerd | 2017-03-03T06:09:53+00:00
Crap, earlier `head -n 1 /proc/stat` - no space after the dash. Could you run that instead? Top should be reading the same information, so this is unlikely to be the problem anyway.

## ghost | 2017-03-03T18:10:31+00:00
cpu  4036686 0 212138 81823600 319375 0 43104 0 0 0

## ghost | 2017-03-13T17:43:13+00:00
I wonder if this is a Linux specific bug, and that it's because I start the daemon inside Linux /etc/rc.local file. I am having trouble sending commands to a daemon started within /etc/rc.local (for example starting a testnet daemon process) when those commands are sent from within a logged in user and not the main OS itself.

## ghost | 2017-03-13T17:43:59+00:00
Basically, the daemon is started by the OS/root, but the commands are issued from a logged in user, so that may be the reason for the disconnect.

## doobilydo | 2017-04-14T16:19:24+00:00
I just found out that logging in remotely triggers the idle percentage to stay in the 80s. It never seems to reach 90, despite nothing running differently.The CPU was remaining the same.

The moment I logged in directly, not remotely, it went above 90% and began mining again.

I'm not sure why remote access is having this effect. Other than that, I can't duplicate the zero hash rate problem.

## revler1082 | 2017-04-14T16:25:17+00:00
Maybe the extra work required by whatever process is doing the remote work
is higher?

On Fri, Apr 14, 2017, 12:19 PM Jon <notifications@github.com> wrote:

> I just found out that logging in remotely triggers the idle percentage to
> stay in the 80s. It never seems to reach 90, despite nothing running
> differently.The CPU was remaining the same.
>
> The moment I logged in directly, not remotely, it went above 90% and began
> mining again.
>
> I'm not sure why remote access is having this effect. Other than that, I
> can't duplicate the zero hash rate problem.
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/1810#issuecomment-294183483>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AA0DGtxuG1D9zNBV2jKDpMpQPVnq0nFkks5rv5yPgaJpZM4MMhcM>
> .
>


## doobilydo | 2017-04-14T16:40:46+00:00
It didn't look that way. I mean sure, there is probably a little extra something running. I can't argue that. I was running it with low CPU usage to begin with, and it wouldn't kick in. Even now, My CPU usage is higher than that, but it is still producing a hashrate.

I just logged in remotely, with my CPU running higher, and the mining kept going, dropping only slightly. So now that remote bug is not consistent either. I'm not sure what's happening.

Perhaps we should keep the "remote" idea in the back of our heads, though.

## moneromooo-monero | 2017-09-21T08:58:37+00:00
Is this working now for those people for whom it wasn't ?

# Action History
- Created by: ghost | 2017-02-26T21:12:37+00:00
- Closed at: 2017-11-27T19:50:16+00:00
