---
title: 'Win_10_64bit synchronization messing with sound '
source_url: https://github.com/monero-project/monero/issues/1333
author: Comodore125
assignees: []
labels: []
created_at: '2016-11-12T21:18:45+00:00'
updated_at: '2021-08-13T04:03:11+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:03:11+00:00'
---

# Original Description
Having monerod.exe started and working, this program is messing with sound on my system without going over 60% on CPU neither doing some problems with HDD. 

This issue is pretty strange. 

The problems it does with sounds is when I am listening to some podcast on Soundcloud it is interfering with the process like every 30 seconds sound output feels like shaking (or like it freezes) and then it moves on for another tens of seconds. 

# Discussion History
## moneromooo-monero | 2016-11-12T21:39:12+00:00
Seems like the OS is a bit bad at I/O scheduling. The heavy load is there only while syncing, it should be gone once you're up to date and getting only new blocks. A workaround might be to set a download rate limit, which will, if small enough for your system, also keep CPU and disj I/O usage lower.


## Comodore125 | 2016-11-12T21:51:36+00:00
It might be bad at I/o scheduling, but it makes little sense when this issue is hapening only with monerod.exe. Bitcoin Core is causing no problems as well as other cryptos I tried. And nothing else is causing me problems. 


## anonimal | 2016-11-12T22:38:24+00:00
> it makes little sense when this issue is hapening only with monerod.exe

Unless you've produced a reliable [scientific control](https://en.wikipedia.org/wiki/Scientific_control), [deductive reasoning](https://en.wikipedia.org/wiki/Deductive_reasoning) without proper [scientific method](https://en.wikipedia.org/wiki/Scientific_method) can be misleading (e.g., are all conditions the same?).

Can you produce video/audio recording snapshots of all instances or provide another form of verifiable measurement? These types of symptoms with heavy I/O are usually indicative of low-resources, old hardware, and/or a bad operating systems (windows is inherently bad). 

I've noticed that syncing requires much I/O regardless of OS - and it is noticeable, so I think more info is needed.


## Comodore125 | 2016-11-12T23:20:33+00:00
Ok, guys, I will be testing this further


## Comodore125 | 2016-11-13T11:22:29+00:00
https://uloz.to/!V3XVCvx7Wxdx/monero-m4a

0:48 I started monerod.exe

When it start running on full speed the issue is happening more often. You can hear the problem after 2:00. 

You can see here that PC is not getting hit at all on resources side. 

![pc_detailsjpg](https://cloud.githubusercontent.com/assets/6156234/20245166/c7c315f0-a99b-11e6-95fc-3aa45010d7da.JPG)

I am going to test it on another win_10_64bit computer 


## iDunk5400 | 2016-11-13T12:58:15+00:00
https://www.google.com/#q=deferred+procedure+call


## Comodore125 | 2016-11-16T12:18:40+00:00
yes, it is likely related. on other PC with win_10 I did not have this issue. It is likely related to sound drivers.


## moneromooo-monero | 2017-10-02T19:30:58+00:00
It might be better now with current master, with 510d0d47.


## selsta | 2021-08-13T04:03:11+00:00
Closing as the issue appears to be unrelated to monero. 

# Action History
- Created by: Comodore125 | 2016-11-12T21:18:45+00:00
- Closed at: 2021-08-13T04:03:11+00:00
