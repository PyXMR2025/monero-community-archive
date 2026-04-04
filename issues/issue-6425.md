---
title: '"Out of memory: Killed process" on Raspberry Pi'
source_url: https://github.com/monero-project/monero/issues/6425
author: dfg3hz5zqtwz46hw6
assignees: []
labels: []
created_at: '2020-04-03T23:41:09+00:00'
updated_at: '2020-04-25T16:55:40+00:00'
type: issue
status: closed
closed_at: '2020-04-25T16:55:40+00:00'
---

# Original Description
Hello,

monerod is being closed frequently on my Raspberry Pi 3B+
I'm running Ubuntu 18.04
I reckon it is related to #4189

```
root@ubuntu:/var/log# grep -a 'monero' ./syslog
Apr  3 11:09:13 ubuntu kernel: [44783.754209] monerod invoked oom-killer: gfp_mask=0x100cca(GFP_HIGHUSER_MOVABLE), order=0, oom_score_adj=0
Apr  3 11:09:13 ubuntu kernel: [44783.754233] CPU: 1 PID: 3242 Comm: monerod Tainted: G         C  E     5.3.0-1021-raspi2 #23~18.04.1-Ubuntu
Apr  3 11:09:13 ubuntu kernel: [44783.755802] [   3238]     0  3238   245719   137010  1753088        0             0 monerod
Apr  3 11:09:13 ubuntu kernel: [44783.755878] oom-kill:constraint=CONSTRAINT_NONE,nodemask=(null),cpuset=/,mems_allowed=0,global_oom,task_memcg=/,task=monerod,pid=3238,uid=0
Apr  3 11:09:13 ubuntu kernel: [44783.756235] Out of memory: Killed process 3238 (monerod) total-vm:982876kB, anon-rss:548040kB, file-rss:0kB, shmem-rss:0kB
Apr  3 11:09:13 ubuntu kernel: [44784.105520] oom_reaper: reaped process 3238 (monerod), now anon-rss:8kB, file-rss:0kB, shmem-rss:0kB
```


# Discussion History
## sumogr | 2020-04-04T05:04:30+00:00
As far as i can remember there was a bug with oom killer going rogue on xenial with early kernels. Can you update your kernel to the latest available version and see if it persists?

## dfg3hz5zqtwz46hw6 | 2020-04-04T11:03:54+00:00
I ran apt update and apt upgrade. Everything should be up to date

`root@ubuntu:/home/ubuntu# lsb_release -a
LSB Version:    core-9.20170808ubuntu1-noarch:security-9.20170808ubuntu1-noarch
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.4 LTS
Release:        18.04
Codename:       bionic
`

## moneromooo-monero | 2020-04-04T15:16:15+00:00
Do you have some reason to think this is a monero bug ? If so, what are they ? You mention nothing of that in your report.

## dfg3hz5zqtwz46hw6 | 2020-04-04T16:04:24+00:00
Because I am on a clean install of Ubuntu and only monerod crashes while everything else is running fine? Crashing is probably not intended behavior?
Let me know if I can provide any additional information to help fix this problem.

![htop](https://user-images.githubusercontent.com/21203981/78455435-b31aa680-769e-11ea-94e7-f276652c9262.PNG)


## sumogr | 2020-04-04T17:09:26+00:00
on a pi with that setting on out and in peers what did you expect.
Reduce it

## ghost | 2020-04-04T18:07:18+00:00
add some swap

## dfg3hz5zqtwz46hw6 | 2020-04-04T19:16:14+00:00
What settings would you recommend?
How large should I make the swapfile? If I increase its size can I set more in and out peers?

## sumogr | 2020-04-04T19:21:35+00:00
yes you should be able to. play a bit with it allocate 1 Gb of swap and reduce it to 50 and 50. Why is it so important that you exceed the default settings of incoming and outgoing nodes number?  

## dfg3hz5zqtwz46hw6 | 2020-04-04T19:29:22+00:00
Thanks for the suggestions. I'll try it and will report back tomorrow if it doesn't crash again :)

I have a lot of bandwidth and I want to share as much as possible. Is there a better way to do it?

## moneromooo-monero | 2020-04-04T22:25:49+00:00
Your log does not show a crash. It shows the OOM killer killing monerod.
This means your OS is short of RAM is decided to kill monerod to get some (because monerod uses a fair bit of it).

## dfg3hz5zqtwz46hw6 | 2020-04-06T15:32:16+00:00
I guess that's true. But there should be some kind of countermeasures in place for this behavior?
Anyway, I found a workaround for now.
I added 4Gb swap and am running monerod and the xmrig-proxy as systemctl services now.

[Unit]
Description=Monerod
After=network.target
StartLimitIntervalSec=0

[Service]
Restart=always
RestartSec=30
User=root
Nice=19
ExecStart=/usr/bin/screen -DmS monero /home/ubuntu/monero/monerod --limit-rate 50 --in-peers 50 --out-peers 50

[Install]
WantedBy=multi-user.target

Alternatively the OOM killer could be disabled I guess.

# Action History
- Created by: dfg3hz5zqtwz46hw6 | 2020-04-03T23:41:09+00:00
- Closed at: 2020-04-25T16:55:40+00:00
