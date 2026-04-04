---
title: Monero GUI Syncing process makes my Linux painfully slow and lagging
source_url: https://github.com/monero-project/monero-gui/issues/4259
author: F3llFr0mTh3Sky
assignees: []
labels: []
created_at: '2023-12-29T20:10:44+00:00'
updated_at: '2024-12-12T14:39:14+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
 Hello,
I'm using the Monero GUI v0.18.3.1 with a local node.
![image](https://github.com/monero-project/monero-gui/assets/142761866/ff4f0cbd-fd29-4c78-8cd6-9f1ba3595e72)

It was fully synced yesterday, but I kept my PC powered off during the night.
The first sync also took more than 24 hours, which downloaded about 170 Gb on my SSD.
So now, my node needs to sync again and like for the first time, it makes my Linux painfully slow.
By painfully slow, I mean it becomes randomly totally unusable during 1 to 2 minutes:
Unability to use, drag and switch between windows.
Unability to use the file manager.
Internet slowering down.
Moving the mouse cursor doesn't works or gets very slow.

It is very strange because I have a fast Samsung 2 Tb SSD, a 16 cores i7-10700K CPU and 32 Gb of Corsair DDR4 RAM.
I'm on Linux Kernel 6.1.67-rt20-xanmod1-dist (basically the XanMod kernel mixed with the Gentoo Dist Kernel patches).
The filesystem is EXT4 and again it's on a SATA 6 Gb/s Samsung SSD.
After the node was synced for the first time, I've been able to use the Monero miner and it didn't slows up my PC.

I think I know the root cause of the issue:
I've a 64 Gb SWAP and 32 Gb RAM, but it seems to me the Monero GUI uses ALL of it:
![image](https://github.com/monero-project/monero-gui/assets/142761866/3a8dbd83-43a8-4a0c-b19b-d8114fbb5f64)
![image](https://github.com/monero-project/monero-gui/assets/142761866/6d569f81-ba9d-431f-b565-fb7b2a1b9755)
![image](https://github.com/monero-project/monero-gui/assets/142761866/40340fbc-2cec-4003-81a9-a34cc73f1646)
![image](https://github.com/monero-project/monero-gui/assets/142761866/4cca9841-7c9e-48ff-90d7-5dbd0eb440a5)

**See that the VIRT usage reports 83 Gb, now its even ~~84~~ ~~85~~ ~~86~~ 87 Gb.**
I'll double check it but I think it also uses as much RAM after the sync is finished.
**So basically, memory leaking that fills my SWAP (so the SSD) with a lot of crap and slowering it?**
I already know that when my SSD is under heavy usage, for some reason it's slowering up a lot the whole OS.
This happened for example when I was downloading big files.

In order to help debugging, here's the source code of the install script that compiles the Monero GUI on Gentoo :
https://github.com/l29ah/booboo/blob/master/net-p2p/monero-gui/monero-gui-0.18.3.1.ebuild
And here's the one for Monero itself: 
https://github.com/gentoo/guru/blob/master/net-p2p/monero/monero-0.18.3.1.ebuild

Also, knowing my Internet connection is kinda slow:
![image](https://github.com/monero-project/monero-gui/assets/142761866/a9e0f422-83a5-4feb-a85d-f9e1c505edb6)
It is unlikely Monero syncing process should require 88 Gb of RAM and SWAP.

Here's the result of the memory usage of monerod:
[pmap.txt](https://github.com/monero-project/monero-gui/files/13796429/pmap.txt)

I'll need to sync my Monero Node every single day, and so, if the memory leaking bug doesn't fixed, I'll have to endure it and that it would cause a lot of frustration and loss of time.

So yeah, could you please fix your damn buggy software?

# Discussion History
## selsta | 2023-12-30T01:49:41+00:00
With your hardware it should take around 3 minutes to sync up after having your node offline for 24h. Does it take longer than that?

> See that the VIRT usage reports 83 Gb, now its even 84 85 86 87 Gb.

Monero uses LMDB, a memory mapped db, that's why it displays 83GB. This is not a memory leak, on my VPS with 16GB RAM it says 196GB VIRT usage, and I have no issues, no swap usage and lot of remaining free RAM.

## F3llFr0mTh3Sky | 2023-12-30T02:27:10+00:00
> With your hardware it should take around 3 minutes to sync up after having your node offline for 24h. Does it take longer than that?

I started the sync at 11:00 AM and at 21:00 PM I gave up because it still wasn't finished and it took way too much time.
I guess you proved my point, something wrong it happening on my side.
And knowing everything else on my PC runs just fine when MoneroD isn't running, then the issue is with MoneroD.

Also, as I explained MoneroD just does makes my PC unusable.
And according to the picture just under the "htop" one, the RAM usage of MoneroD is about 31 Gb.

## selsta | 2023-12-30T04:36:39+00:00
> And knowing everything else on my PC runs just fine when MoneroD isn't running, then the issue is with MoneroD.

You wrote the following which might be related, syncing the blockchain makes heavy use of random read / write on the SSD.

> I already know that when my SSD is under heavy usage, for some reason it's slowering up a lot the whole OS.

Did you look into what causes this?

## selsta | 2023-12-30T04:42:26+00:00
> And according to the picture just under the "htop" one, the RAM usage of MoneroD is about 31 Gb.

What does it show under MemAvailable?

## F3llFr0mTh3Sky | 2023-12-30T05:14:50+00:00
> > I already know that when my SSD is under heavy usage, for some reason it's slowering up a lot the whole OS.

> Did you look into what causes this?

No idea. The only thing I knew is that my SSD was limited to 3 Gb/s by the shit integrated SATA controller of my GigaByte motherboard. Then I moved it to my PCIe ASMedia 1066 SATA controller, which improved the speed up to 6 Gb/s but it didn't solve the issue.

> > And according to the picture just under the "htop" one, the RAM usage of MoneroD is about 31 Gb.

> What does it show under MemAvailable?

~~Sorry I don't know and I don't want to run MoneroD again until the issue is solved.
If I run it it will make my PC unstable.~~
The node has been running since less that 5 minutes and now I'll close it.
![image](https://github.com/monero-project/monero-gui/assets/142761866/86376b3f-0264-4d70-a592-03cd6320a442)


## F3llFr0mTh3Sky | 2023-12-30T05:20:23+00:00
Actually this time MoneroD strangely only had to sync around 700 blocks : 
![image](https://github.com/monero-project/monero-gui/assets/142761866/01bf291f-c618-4961-a812-a6e386221228)


## selsta | 2023-12-30T05:22:13+00:00
There are 720 blocks per day, so if you last opened it around 24h ago it's not strange.

## F3llFr0mTh3Sky | 2023-12-30T05:23:53+00:00
No it's strange, because earlier today, as you can see on the first picture it wanted to sync over 1 million blocks, but it was originally 2 millions before it started to progress. And that sync didn't finish. This was the second sync and the he first time, it was totally synced.

What I mean is that when a sync gets interrupted, the next time MoneroD is started, it should start to sync where it stopped the last time.

## jcassette | 2024-12-12T14:39:12+00:00
The monero daemon made my desktop freeze too. It was put to swap memory so I disabled the swap and now it's much better.

# Action History
- Created by: F3llFr0mTh3Sky | 2023-12-29T20:10:44+00:00
