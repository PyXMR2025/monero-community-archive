---
title: Monerod and GUI monero not synced?
source_url: https://github.com/monero-project/monero-gui/issues/3274
author: IndustrialOne
assignees: []
labels: []
created_at: '2020-12-16T19:02:30+00:00'
updated_at: '2021-03-30T02:29:44+00:00'
type: issue
status: closed
closed_at: '2021-03-30T02:29:44+00:00'
---

# Original Description
Apologies if this is a dumb question but I just FINALLY finished syncing the blockchain and notice GUI Monero says I am disconnected from the network even though I'm not. Monerod is operational, GUI Monero started it after all and the log page confirms it is working.

The only thing from the gui monero log that sounds relevant is "wallet not initialized". What am I doing wrong?

# Discussion History
## selsta | 2020-12-28T21:39:19+00:00
Please go to Settings -> Log, type "status" and post the output here.

## IndustrialOne | 2021-01-04T12:36:56+00:00
Oh, didn't see this part.

[1/4/2021 5:15 AM] 2021-01-04 12:15:28.470 I Monero 'Oxygen Orion' (v0.17.1.5-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081

[1/4/2021 5:15 AM] 2021-01-04 12:15:44.505 I Monero 'Oxygen Orion' (v0.17.1.5-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081

[1/4/2021 5:15 AM] 2021-01-04 12:15:49.110 I Monero 'Oxygen Orion' (v0.17.1.5-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081

[1/4/2021 5:15 AM] 2021-01-04 12:15:53.768 I Monero 'Oxygen Orion' (v0.17.1.5-release)
Height: 2267019, target: 2267083 (99.9972%)
Downloading at 36 kB/s
4 peers
213.91.183.212:18080 0000000000000000 before_handshake 0 0 1 kB/s, 0 blocks / 0 MB queued
67.246.26.148:18080 80cb87adb0a46f6f synchronizing 0 2267083 8 kB/s, 20 blocks / 0 MB queued
185.141.60.7:18080 533030d8ea239596 synchronizing 0 2267083 26 kB/s, 20 blocks / 0 MB queued
54.37.172.36:10728 52205232dee3942d normal 0 2263958 1 kB/s, 0 blocks / 0 MB queued
2 spans, 0 MB
[..]
185.141.60.7:18080 20/181 (2267019 - 2267038) -
67.246.26.148:18080 20/181 (2267039 - 2267058) -

>>> status

[1/4/2021 5:35 AM] 2021-01-04 12:35:17.589 I Monero 'Oxygen Orion' (v0.17.1.5-release)
Height: 2267090/2267090 (100.0%) on mainnet, not mining, net hash 1.77 GH/s, v14, 12(out)+0(in) connections, uptime 0d 0h 19m 36s

The daemon btw synced it to full but the monero GUI doesn't seem to think so?

________________________________
From: selsta <notifications@github.com>
Sent: Monday, December 28, 2020 2:39 PM
To: monero-project/monero-gui <monero-gui@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero-gui] Monerod and GUI monero not synced? (#3274)


Please go to Settings -> Log, type "status" and post the output here.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero-gui/issues/3274#issuecomment-751872566>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4SCB76BZOJXCWEAEDDSXD3JJANCNFSM4U6OJCRA>.


## xiphon | 2021-01-15T10:58:11+00:00
Please post your Settings -> Info details.

## IndustrialOne | 2021-01-17T11:22:00+00:00
GUI version: 0.17.1.5-96f9c11 (Qt 5.9.9)
Embedded Monero version: 0.17.1.5-96f9c1132
Wallet path: C:\Users\Admin\Documents\Monero\wallets\Admin\Admin
Wallet restore height: 2207218
Wallet log path: C:\Users\Admin\AppData\Roaming\monero-wallet-gui\monero-wallet-gui.log
Wallet mode: Advanced mode (Local node)OpenGL

________________________________
From: xiphon <notifications@github.com>
Sent: Friday, January 15, 2021 3:58 AM
To: monero-project/monero-gui <monero-gui@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero-gui] Monerod and GUI monero not synced? (#3274)


Please post your Settings -> Info details.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero-gui/issues/3274#issuecomment-760865302>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4UR4UDICZE3AC2U5HTS2ANVFANCNFSM4U6OJCRA>.


## xiphon | 2021-01-17T11:29:39+00:00
Does updating to the latest Monero GUI v0.17.1.9 version resolve the issue?

## IndustrialOne | 2021-01-19T10:43:18+00:00
No.

________________________________
From: xiphon <notifications@github.com>
Sent: Sunday, January 17, 2021 4:29 AM
To: monero-project/monero-gui <monero-gui@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero-gui] Monerod and GUI monero not synced? (#3274)


Does updating to the latest Monero GUI v0.17.1.9 version resolve the issue?

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero-gui/issues/3274#issuecomment-761783598>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4TIKZRBO7XZ7GLYM2TS2LC27ANCNFSM4U6OJCRA>.


## IndustrialOne | 2021-01-19T16:14:29+00:00
More good news, here is what the latest version does:
2021-01-19 15:59:54.881 7764 ERROR console_handlercontrib/epee/include/console_handler.h:397 Failed to read line.

It spammed that a million times per second and filled my already-slow-as-shit thumb drive with 10 GB of log files consisting of just that line.

I just also restored a 3-week-old backup of the database file (which took over 4 hours) only to realize that it wasn't corrupted because monerod on its own doesn't spam log files with that error.

If I don't get an answer within a few days of what's going on then I'm dumping this program and seeking alternatives. It's really ridiculous that I've been waiting 2 months now. I want to start buying and spending monero already and I want to be a contributing node to the fucking network. Can we please make it more difficult?

________________________________
From: xiphon <notifications@github.com>
Sent: Sunday, January 17, 2021 4:29 AM
To: monero-project/monero-gui <monero-gui@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero-gui] Monerod and GUI monero not synced? (#3274)


Does updating to the latest Monero GUI v0.17.1.9 version resolve the issue?

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero-gui/issues/3274#issuecomment-761783598>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4TIKZRBO7XZ7GLYM2TS2LC27ANCNFSM4U6OJCRA>.


## xiphon | 2021-01-25T18:54:44+00:00
> If I don't get an answer within a few days of what's going on then I'm dumping this program and seeking alternatives. It's really ridiculous that I've been waiting 2 months now. I want to start buying and spending monero already and I want to be a contributing node to the fucking network. Can we please make it more difficult?

This attitude won't work, at least it definitely won't work the way you expect.

Given the information provided, right now it seems to me this might be some environment issue. We didn't see similar reports yet.

> GUI Monero says I am disconnected from the network

Just to clarify, you see `Disconnected` in the bottom left Monero GUI corner , right?

If so, please run Monero GUI, wait till it starts the daemon and run the following command and post the output (you might need to install wget beforehand `apt-get install wget`):
```
wget -O- http://127.0.0.1:18081/get_info
```



## IndustrialOne | 2021-01-30T18:31:41+00:00
Here's the thing, most people don't care to contribute a full node, they only want to trade crypto and forget about it. Don't tell me I have an attitude problem. I have patiently waited 2 months for answers, can you name a single dude with this kind of zen? You can't. I have moved on already, waiting to get my Trezor hardware wallet, but I will cooperate with the troubleshoot in the spirit of supporting free software.

"Just to clarify, you see Disconnected in the bottom left Monero GUI corner , right?" Correct. It starts the daemon, the daemon is obviously running and syncing but GUI says I'm disconnected.

C:\Users\Admin>wget -O- http://127.0.0.1:18081/get_info
--2021-01-30 19:29:37--  http://127.0.0.1:18081/get_info
Connecting to 127.0.0.1:18081... failed: Bad file descriptor.

________________________________
From: xiphon <notifications@github.com>
Sent: Monday, January 25, 2021 11:55 AM
To: monero-project/monero-gui <monero-gui@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero-gui] Monerod and GUI monero not synced? (#3274)


If I don't get an answer within a few days of what's going on then I'm dumping this program and seeking alternatives. It's really ridiculous that I've been waiting 2 months now. I want to start buying and spending monero already and I want to be a contributing node to the fucking network. Can we please make it more difficult?

This attitude won't work, at least it definitely won't work the way you expect.

Given the information provided, right now it seems to me this might be some environment issue. We didn't see similar reports yet.

GUI Monero says I am disconnected from the network

Just to clarify, you see Disconnected in the bottom left Monero GUI corner , right?

If so, please run Monero GUI, wait till it starts the daemon and run the following command and post the output (you might need to install wget beforehand apt-get install wget):

wget -O- http://127.0.0.1:18081/get_info


—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero-gui/issues/3274#issuecomment-767036569>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4T3VIMKUTUW5TQSUMTS3W5AJANCNFSM4U6OJCRA>.


## IndustrialOne | 2021-02-04T18:23:21+00:00
Update, my firewall had to be updated so it was temporarily off while I tried a few things including running GUI wallet to update the blockchain for this week and guess what? My wallet connected for the first time. So this was the mystery this whole time... I am dumbfounded. I would've known way better back in the day. This is the only application I know of thus far that my firewall had a problem with, tho. Maybe something to do with the 18081 port?

Anyway, what must I do to support the network and help others sync to it? Just load up the daemon and let it run in the background?

________________________________
From: xiphon <notifications@github.com>
Sent: Monday, January 25, 2021 11:55 AM
To: monero-project/monero-gui <monero-gui@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero-gui] Monerod and GUI monero not synced? (#3274)


If I don't get an answer within a few days of what's going on then I'm dumping this program and seeking alternatives. It's really ridiculous that I've been waiting 2 months now. I want to start buying and spending monero already and I want to be a contributing node to the fucking network. Can we please make it more difficult?

This attitude won't work, at least it definitely won't work the way you expect.

Given the information provided, right now it seems to me this might be some environment issue. We didn't see similar reports yet.

GUI Monero says I am disconnected from the network

Just to clarify, you see Disconnected in the bottom left Monero GUI corner , right?

If so, please run Monero GUI, wait till it starts the daemon and run the following command and post the output (you might need to install wget beforehand apt-get install wget):

wget -O- http://127.0.0.1:18081/get_info


—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero-gui/issues/3274#issuecomment-767036569>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4T3VIMKUTUW5TQSUMTS3W5AJANCNFSM4U6OJCRA>.


## xiphon | 2021-02-04T23:20:40+00:00
> Anyway, what must I do to support the network and help others sync to it? Just load up the daemon and let it run in the background?

Yep and optionally you can configure the firewall to allow incoming connections to tcp port 18080 (monero p2p port).


## IndustrialOne | 2021-02-06T20:08:54+00:00
I did that but I still get messages like these.
2021-02-06 18:37:45.905 [P2P6] WARNING global src/p2p/net_node.inl:2063 No incoming connections - check firewalls/routers allow port 18080

It seems to be syncing just fine and the wallet GUI now appears to work as well so not sure if that error message should concern me?

________________________________
From: xiphon <notifications@github.com>
Sent: Thursday, February 4, 2021 4:20 PM
To: monero-project/monero-gui <monero-gui@noreply.github.com>
Cc: IndustrialOne <industrial_one@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [monero-project/monero-gui] Monerod and GUI monero not synced? (#3274)


Anyway, what must I do to support the network and help others sync to it? Just load up the daemon and let it run in the background?

Yep and optionally you can configure the firewall to allow incoming connections to tcp port 18080 (monero p2p port).

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/monero-project/monero-gui/issues/3274#issuecomment-773667928>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFKNO4SVONNJWZ3IKGYVWVTS5MTVRANCNFSM4U6OJCRA>.


## selsta | 2021-03-30T02:28:39+00:00
> It seems to be syncing just fine and the wallet GUI now appears to work as well so not sure if that error message should concern me?

You can ignore it. If you manage to get incoming connections working your node will support the network more, but it is fine without it.

Closing as the issue seems resolved.

# Action History
- Created by: IndustrialOne | 2020-12-16T19:02:30+00:00
- Closed at: 2021-03-30T02:29:44+00:00
