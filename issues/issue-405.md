---
title: Can I run xmrig in my cluster?
source_url: https://github.com/xmrig/xmrig/issues/405
author: BeanSampa
assignees: []
labels: []
created_at: '2018-02-15T22:04:40+00:00'
updated_at: '2019-08-02T13:07:18+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:07:18+00:00'
---

# Original Description
Hi, 
I received error: Ilegal instruction

My config.json : http://prntscr.com/ifbgmr
The single command line (returns this same error).

See compile: http://prntscr.com/ifbfoe

I'm newbie, and I'm mounting a cluster with 6 RPI3, I used:
https://github.com/bamarni/pi64
https://packages.debian.org/jessie/arm64/yorick-mpy-mpich2/download

Note: I try to run on only one Rpi3 (not starting the cluster by master)
I have 10 more Rpi3 to add i my cluster.

Thnx




# Discussion History
## Zelecktor | 2018-02-16T03:47:38+00:00
Just for educational purposes, because each raspberry pi3 does about 8-12H/s
You need to mount as multi core server.

Your goal i think is to oppen only one instance in one pi and start mining with 7 (for example) which 1 is the main server and the others are only for resourses.
The main thing you need to consider is on that ARM works as quadcore, but practically is only one CPU and one socket, so threads must be in 1.
As you are mining with more than one, server pi must recognize others CPU and you need to play with the affinity.

I have understand that afinity works on the cpu where you want.
For example if you are working with one CPU with 4 cores but you want to use only the first two, you set threads 2 and afinity  0 0 1 1 on binary, on this case "0x3". if you want to use cpu0 and cpu2 0 1 0 1 so afinity will be "0x5"
As pi CPU work as quadcore, each raspberry have four slots but as you are working only with one thread, each raspberry pi should be 0 0 0 1 on afinity (because you only are mining with cpu0)
You need to setup for each rasberry pi.

For example if your cluster have 5 raspberry pi, set threads to 5.
Each one have 0 0 0 1 on afinity so

0 0 0 1 - 0 0 0 1 - 0 0 0 1 - 0 0 0 1 - 0 0 0 1 = so afinity "0x11111"

Obviusly check cpu listen with `lscpu` and CPU number to know which CPU correspond to each raspberry pi.
If rpi server listen the other cpu. Xmrig should detect others CPU but you need to define with afinity.

## BeanSampa | 2018-02-16T19:29:29+00:00
Thank you, Zelecktor, for your response.
I tried many combinations of Thread and Afinity, and I always got: Illegal Instruction

I'm trying to run a single rpi3.
I do not know what is happening. Maybe compilation is a problem?

## Zelecktor | 2018-02-16T19:42:45+00:00
did you tried run it with `sudo su` or maybe `chmod 777 /path folder`
Or maybe you are compiling with wrong libraries (libuv). linux raspbian have many issues when compining softwares with ARM because they are not optimized. Debian 8 is the most similar, maybe try to re-install packages from that source.

## BeanSampa | 2018-02-16T21:10:50+00:00
I tried both (sudo and chmod)

Distributor ID: Debian
Description:    Debian GNU/Linux 9.3 (stretch) Release:        9.3 - Codename:       stretch

libuv1_1.9.1-3_arm64 and libuv1-dev_1.9.1-3_arm64   Are files I found.

Thank you.



# Action History
- Created by: BeanSampa | 2018-02-15T22:04:40+00:00
- Closed at: 2019-08-02T13:07:18+00:00
