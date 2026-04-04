---
title: Daemon crashed last night with only a warning
source_url: https://github.com/monero-project/monero/issues/9315
author: Column01
assignees: []
labels: []
created_at: '2024-05-02T16:27:07+00:00'
updated_at: '2024-05-03T02:50:35+00:00'
type: issue
status: closed
closed_at: '2024-05-03T02:48:38+00:00'
---

# Original Description
Last night, my daemon crasged with only a warning saying the following:

```
2024-05-02 06:34:11.786	[P2P3]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1697	Synced 3139930/3139930
2024-05-02 06:53:10.124	[P2P4]	WARNING	ringct	src/ringct/rctOps.cpp:457	ge_frombytes_vartime failed at 457
```

Now when I try to launch the daemon, it just sits at the stage where it would be loading the blockchain for a long time.

`Monero 'Fluorine Fermi' (v0.18.3.3-release)` is the version I'm using

# Discussion History
## selsta | 2024-05-02T16:29:04+00:00
How long did you wait after launch?

The warning message you shared is likely unrelated to whatever freezing issue you had.

## Column01 | 2024-05-02T16:29:54+00:00
It's been almost 20 mins and the console has done nothing else other than warn me my blockchain is on an HDD (I know, bad practice), resource usage shows that it hasn't even tried to read the disk as far as I can really tell

## Column01 | 2024-05-02T16:30:40+00:00
The disk still works, I have media on there I can still stream just fine, its not an IO issue either as this machine has nothing else running at the moment

## Column01 | 2024-05-02T16:33:18+00:00
It's doing 400kb/s read but that's far slower than anything I've seen it do
![image](https://github.com/monero-project/monero/assets/26526649/8d1da0bc-43df-4a39-9fbe-94b3279ab2c0)


## selsta | 2024-05-02T16:35:03+00:00
It verifies the whole txpool on launch, which can take a while in some cases. Is there CPU usage?

Can you launch monerod with --log-level 2 and share the last couple messages?

## Column01 | 2024-05-02T16:36:59+00:00
OK it is verifying transactions. spamming the console with a lot of:

```
2024-05-02 16:36:42.734 I Transaction added to pool: txid <dd3fb300aa6ad4095319e1ce59b90b08c38a63ef4cd10cdefe9a2bc324e7fc3e> weight: 101187 fee/byte: 80000, count: 338
2024-05-02 16:36:42.773 D Removing tx <0f19390354b694ee7774356757f2b0f85f5af1ab838b07b141812290172a323f> from tx pool, but it was not found in the map of added txs
2024-05-02 16:36:42.773 D Transaction removed from pool: txid <0f19390354b694ee7774356757f2b0f85f5af1ab838b07b141812290172a323f>, total entries in removed list now 339
2024-05-02 16:36:42.773 D Using 0.000000019000/byte fee
2024-05-02 16:36:42.773 D Mixin: 15-15
```


## Column01 | 2024-05-02T16:37:38+00:00
Its using 250% CPU according to top so it is actually doing stuff

## Column01 | 2024-05-02T16:42:11+00:00
im gonna just let it do its thing for a few hours and see if it fixes itself, sorry to cause alarm. It appeared to be idle but that clearly is not the case. Patience it is :D thanks for your help

## Column01 | 2024-05-02T16:50:00+00:00
So I also mistitled it, I checked the log and it did close the daemon, not freeze. I also have ZMQ enabled for p2pool mining, I saw it mentioned here https://github.com/monero-project/monero/issues/8897, could it be related?

## selsta | 2024-05-02T16:51:35+00:00
How much RAM does your machine have? Did it get killed for OOM or crash?

## Column01 | 2024-05-02T16:52:15+00:00
16GB of RAM, wasn't anywhere close to full. My virtual memory was at 91% though since its only a gig, but it had been at 80%+ since I started mining so not sure

## Column01 | 2024-05-02T19:45:08+00:00
OK it was able to resync properly. I guess ill wait to see if it crashes again and try to get you more info if I can

## selsta | 2024-05-02T23:01:31+00:00
It's still not clear to me if it ran out of memory, or if it crashed. I have seen RAM usage spikes on my node in some specific situations that caused my node to OOM.

## selsta | 2024-05-02T23:03:29+00:00
Just checked one of my nodes, around the same time one of my nodes also ran out of memory. What you are reporting is not a crash, though it would be nice if someone could investigate what casues this RAM spike.

## Column01 | 2024-05-02T23:04:51+00:00
> Just checked one of my nodes, around the same time one of my nodes also ran out of memory. What you are reporting is not a crash, though it would be nice if someone could investigate what casues this RAM spike.

That is very odd indeed. No other processes were affected. I was running p2pool and xmrig on the server as well, if that is relevant. None of those crashed but were upset about the daemon dying

## selsta | 2024-05-03T02:48:38+00:00
Let's continue here #9315

## Column01 | 2024-05-03T02:49:47+00:00
The issue you linked is this one

## selsta | 2024-05-03T02:50:33+00:00
https://github.com/monero-project/monero/issues/9317

# Action History
- Created by: Column01 | 2024-05-02T16:27:07+00:00
- Closed at: 2024-05-03T02:48:38+00:00
