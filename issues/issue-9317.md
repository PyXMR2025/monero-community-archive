---
title: A lot of 150/2 transactions in the txpool causes memory spike / OOM
source_url: https://github.com/monero-project/monero/issues/9317
author: selsta
assignees: []
labels:
- daemon
created_at: '2024-05-03T02:48:23+00:00'
updated_at: '2024-05-18T02:53:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have noticed this a couple times now that monerod gets OOMd when there are a lot of 150/2 transactions in the txpool. This happened on VPS with both 8GB and 16GB RAM.

# Discussion History
## thilool | 2024-05-03T15:44:43+00:00
I had a similar issue which happened now the second time after I upgraded from v0.18.3.2 to v0.18.3.3 (looks more like issue #9315)
I run a 32GB RAM standalone server on a fiber connection and an SSD so I would rule out any hardware limitations. 

here is what monerod shows:
_2024-04-28 14:51:07.835	I [batch] DB resize needed
2024-04-28 14:51:08.435	I LMDB Mapsize increased.  Old: 215675MiB, New: 216699MiB
2024-04-28 15:23:50.517	I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3137335
2024-04-28 15:23:50.518	I id:	<13f334bd761b12b8d382c7a9f2fed8708c198270906ba82621ee990740245fa6>
2024-04-28 15:23:50.518	I PoW:	<20a551bdbc8ac6a1744da38033033e53e6fd297915c9bd77845e940200000000>
2024-04-28 15:23:50.518	I difficulty:	257613739237
2024-04-29 08:17:34.150	I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3137818
2024-04-29 08:17:34.154	I id:	<6d056d352284efea4a3f21a46d6fbcb98194fc0ab994c470626cfd9737e6b946>
2024-04-29 08:17:34.154	I PoW:	<d29f1a21e03620870b6d80ad191bffc035eab9e16d9cfc5b525e750400000000>
2024-04-29 08:17:34.155	I difficulty:	239388303636
2024-04-29 14:21:49.674	E Failed to parse transaction from blob
2024-04-29 18:05:08.287	E Failed to parse transaction from blob
2024-04-30 06:11:25.791	I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3138489
2024-04-30 06:11:25.797	I id:	<c25b108d08fec0651faa8475ab24e7f99243d29a70561d4ae06f9ba7a6617f81>
2024-04-30 06:11:25.797	I PoW:	<3fa592639c5da5a00ce082f0bb99efaa33a4e819db90a9994587e30100000000>
2024-04-30 06:11:25.797	I difficulty:	253900650451
2024-05-01 04:07:39.429	W ge_frombytes_vartime failed at 457
2024-05-01 08:55:18.591	I [69.234.65.55:46556 INC] Sync data returned a new top block candidate: 3139275 -> 3139276 [Your node is 1 blocks (2.0 minutes) behind] 
2024-05-01 08:55:18.593	I SYNCHRONIZATION started
2024-05-01 13:31:16.704	W ge_frombytes_vartime failed at 457
2024-05-01 19:51:21.045	I Recalculating difficulties from height 3102800 to height 3139634
2024-05-02 05:34:52.597	E Failed to parse transaction from blob
2024-05-02 05:58:59.706	E Failed to parse transaction from blob
2024-05-02 05:59:21.923	E Failed to parse transaction from blob
2024-05-02 06:01:45.093	W ge_frombytes_vartime failed at 457
2024-05-02 06:05:17.435	E Failed to parse transaction from blob
Killed_

Hope fully this helps. Something in the latest version seems to cause this issue.
The version v0.18.3.2 was running for months straight. This is now the second crash within a week.

Greetings!







## selsta | 2024-05-03T15:50:25+00:00
>  Something in the latest version seems to cause this issue. The version v0.18.3.2 was running for months straight. This is now the second crash within a week.

This is not related to the latest version, the reason why this only happened in the last week is because before that no one ever added a ton of 150/2 transactions into the txpool.

## thilool | 2024-05-03T15:59:29+00:00
What exactly are 150/2 transactions?

Can you point me to any documentation?

Thanks!






## selsta | 2024-05-03T16:02:50+00:00
150/2 means transactions with 150 inputs and 2 outputs. It's basically someone consolidating a lot of inputs. Such transactions are large and take a while to verify. Someone has transacted a lot of these at the same time which caused the tx pool to fill up.

## thilool | 2024-05-03T16:12:22+00:00
when you say 'takes time to verify' would a server being used as well for mining benefit from leaving a few threads extra available for such transactions spikes? Or is the CPU not really the bottleneck but rather RAM or SSD?

interesting to see is that a manual restart of monerod always works without any problems. it syncs back up and runs as nothing ever happened. 
Is there an option to execute an automated restart in case it crashed?

## Column01 | 2024-05-03T16:27:02+00:00
I just checked my node today and it reported being 2 months ahead after the issue I had that was linked here.

```
2024-05-03 01:14:10.069	    7ed3293fe6c0	INFO	msgwriter	src/common/scoped_message_writer.h:102	Height: 3140496/3140496 (100.0%) on mainnet, not mining, net hash 2.03 GH/s, v16, 32(out)+63(in) connections, uptime 0d 5h 30m 27s
2024-05-03 03:20:49.070	[P2P9]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:409	[94.16.112.22:45386 INC] Sync data returned a new top block candidate: 3140561 -> 3097104 [Your node is 43457 blocks (2.0 months) ahead] 
```

This is the output of diff
```
2024-05-03 16:23:55.530	    7ed3293fe6c0	INFO	msgwriter	src/common/scoped_message_writer.h:102	BH: 3140966, TH: bfe1f2f2add49f50204d41ec0c9aa55d12d52fbfc7dd651f9e54071c5f76dd77, DIFF: 246857749344, CUM_DIFF: 350313291089291902, HR: 2057147911 H/s
```


## selsta | 2024-05-03T16:30:00+00:00
@Column01 you can ignore that message, it means a different peer claimed that 3097104 is the correct height which isn't true. Your node doesn't have any issues.

## selsta | 2024-05-03T16:35:10+00:00
> when you say 'takes time to verify' would a server being used as well for mining benefit from leaving a few threads extra available for such transactions spikes? Or is the CPU not really the bottleneck but rather RAM or SSD?

Leaving a couple threads available is recommended for good node performance, but I don't think it would have helped in this specific case.

> Is there an option to execute an automated restart in case it crashed?

Nothing built in but you can use for example systemd for this.

## HardenedSteel | 2024-05-03T23:32:30+00:00
Some people reported same issue on [Reddit](https://reddit.com/r/Monero/comments/1ci9l7g/in_todays_flood_attack_on_the_network/l27ty5w/), copy & pasting to here:
> During this attack that has been going on for about 3 hours, my node (v0.18.3.3) has been killed twice by Linux OOM killer, due to too high memory usage.
> 
> It seems someone has found out how to make nodes use massive amounts of memory.During this attack that has been going on for about 3 hours, my node (v0.18.3.3) has been killed twice by Linux OOM killer, due to too high memory usage.
> 
> It seems someone has found out how to make nodes use massive amounts of memory. 
> > can you make a bug report? https://github.com/monero-project/monero
> > > I have nothing concrete to write in a bug report, other than the fact that my node consumed ~14GB more memory than usual, was killed by Linux OOM-killer and then was restarted by systemd, due to my unit being configured with "Restart=always".
I have no idea how it was triggered or if it would've even been a problem on a host with more memory available.
> 
> > Mine was killed last night too

## Column01 | 2024-05-03T23:36:14+00:00
> Someone reported same issue on [Reddit](https://reddit.com/r/Monero/comments/1ci9l7g/in_todays_flood_attack_on_the_network/l27ty5w/)

That is very interesting indeed. I do not think this is a coincidence, then

## thilool | 2024-05-04T09:36:30+00:00
I will adjust the monerod process priority based on this documentation and see what happens.

https://www.baeldung.com/linux/memory-overcommitment-oom-killer



## thilool | 2024-05-04T10:25:50+00:00
Most of my processes are running with an oom_score of '666' 
monerod was running above 700 so it was one of the first candidates to be killed.

I adjusted the oom_score_adj to -700 (sudo choom -p MONEROD_PROCESSID -n 700) which made it the number 2 in line after the unkillable processes with an oom_score of 0.

If it gets killed now with 32GB of RAM we have a much bigger issue concerning this attack vector.

I still cannot grasp how so much memory can be used in this case. Can anyone point me to some simple math how we get in the 10+GB range of memory usage?
Thanks!

## Boog900 | 2024-05-05T17:15:38+00:00
This could be because of how txs are relayed.

When we receive txs in the fluff stage, we add them to our fluff queue and set a timer on each connection except the one that sent the txs to us. Then when the timer is up we make a message and the txs get sent on that connection:

https://github.com/monero-project/monero/blob/c8214782fb2a769c57382a999eaf099691c836e7/src/cryptonote_protocol/levin_notify.cpp#L396-L400

https://github.com/monero-project/monero/blob/c8214782fb2a769c57382a999eaf099691c836e7/src/cryptonote_protocol/levin_notify.cpp#L203-L207

So it seems for every tx thats broadcasted the bytes of the tx are copied for each connection that receives the tx. So if we have [96 connections](https://github.com/monero-project/monero/issues/9315#issuecomment-2091001070), then each tx will be fluffed to 95 peers (1 of them sent the tx to us).

It's easy to see how this can add up: 10GB / 95 = ~108MB which means we only need around 108MB of txs for this to potentially use 10GB with 96 connections (I don't know how big the tx pool was when the crashes happened). 

It's more nuanced than I laid out there, each connection has a randomized timer so not all 95 will fluff at once for example and I haven't actually tested this so I might be missing something.

@vtnerd what do you think?

## selsta | 2024-05-06T02:39:28+00:00
@Boog900 The txpool reached around 100MB, but those transactions got propagated over the time of like an hour, they didn't get submitted all at once.

## Jayd603 | 2024-05-07T13:46:20+00:00
[1842267.939549] Out of memory: Killed process 37137 (monerod) total-vm:292086252kB, anon-rss:57011624kB, file-rss:0kB, shmem-rss:0kB, UID:0 pgtables:507476kB oom_score_adj:0

How much memory do I need?  sheesh.   : - )



## thilool | 2024-05-08T17:15:16+00:00
Do I see correct that your VM killed the process with 292GB available? Or did monerod use that much memory? 
Did you run other memory intensive processes and monerod was just the first to be killed?

Obviously seems to be a more widespread issue. 

Is there anything I can do to help? Logging certain processes for example which helps to isolate the problem or helps to find a fix?

## selsta | 2024-05-08T23:36:22+00:00
@thilool @Jayd603 how many incoming / outgoing connections to you approximately have?

I'm curious if there was anyone who had this issue with no incoming connections.

## thilool | 2024-05-09T08:22:01+00:00
currently I am running around 40-60(out) and 100-150(in).
my OOM_adj seems to have worked so far and now I see monerod sitting at 10.2GB of memory usage. I'll keep you posted on that.

monerod managed to get through 2 failed 'parse transaction from blob' which before was often the trigger to a OOM kill.

see the status below:

_2024-05-06 21:42:51.443	I difficulty:	271257517664
2024-05-06 21:42:51.499	I ###### REORGANIZE on height: 3143297 of 3143297 with cum_difficulty 350902947730358755
2024-05-06 21:42:51.499	I  alternative blockchain size: 2 with cum_difficulty 350903219324713192
2024-05-06 21:42:52.986	I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3143297
2024-05-06 21:42:52.986	I id:	<7a53b19e2e794c2d012cbfb5e7ee79830668d893c9f4fe660065c76f5fd8cae8>
2024-05-06 21:42:52.986	I PoW:	<fbc1390c1cadf1212c609b4fe14c475f0055c3201aa08b79f3b2f60100000000>
2024-05-06 21:42:52.986	I difficulty:	271257517664
2024-05-06 21:42:54.319	I REORGANIZE SUCCESS! on height: 3143297, new blockchain size: 3143299
2024-05-06 21:42:54.372	I Synced 3143299/3143299
2024-05-06 22:27:54.860	I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3143314
2024-05-06 22:27:54.860	I id:	<74b6e103c62b0c44389a2c175fbc8cd9b31b33f3d692930963e883197d0d7814>
2024-05-06 22:27:54.860	I PoW:	<eb3b097dca0d3e031a012ae418669e5c6ee26d6b34706f43e652bd0100000000>
2024-05-06 22:27:54.860	I difficulty:	266444980508
2024-05-07 10:47:23.348	E Failed to parse transaction from blob
2024-05-07 15:19:42.640	E Failed to parse transaction from blob
2024-05-07 23:42:56.943	I [batch] DB resize needed
2024-05-07 23:42:57.534	I LMDB Mapsize increased.  Old: 216699MiB, New: 217723MiB
2024-05-08 14:42:51.569	I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3144474
2024-05-08 14:42:51.575	I id:	<dfb7d2f8c5ed5586afc1f534f83847f9ce08c2e51ab9890bcca8831f39a2d0f8>
2024-05-08 14:42:51.575	I PoW:	<cc1604d8023648b5230bf7c0e4aebbc4ef7ee5c96b2db2472f42860400000000>
2024-05-08 14:42:51.575	I difficulty:	235033673331
2024-05-08 14:44:57.949	I ###### REORGANIZE on height: 3144474 of 3144474 with cum_difficulty 351195806642158375
2024-05-08 14:44:57.949	I  alternative blockchain size: 2 with cum_difficulty 351196041538715801
2024-05-08 14:44:58.442	I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3144474
2024-05-08 14:44:58.442	I id:	<15d5f24014d151a542c2b27c5a78d0d89bb853a06aeabc23c7a042593d990dc0>
2024-05-08 14:44:58.442	I PoW:	<8d2495dd5ba535538b17c3ced5b515ea43737744285ce21cbeaae00200000000>
2024-05-08 14:44:58.442	I difficulty:	235033673331
2024-05-08 14:44:59.533	I REORGANIZE SUCCESS! on height: 3144474, new blockchain size: 3144476
2024-05-09 01:21:02.822	W Attempt to get block from height 3144803 failed -- block not in db
2024-05-09 06:47:44.252	E Transaction not found in pool
status
Height: 3145017/3145017 (100.0%) on mainnet, smart mining at 0 H/s, net hash 1.98 GH/s, v16, 43(out)+112(in) connections, uptime 5d 16h 18m 6s_




## selsta | 2024-05-09T14:11:02+00:00
> monerod managed to get through 2 failed 'parse transaction from blob' which before was often the trigger to a OOM kill.

"parse transaction from blob" is unrelated

## Jayd603 | 2024-05-09T14:12:50+00:00
I had 64GB RAM in a VM, monerod was running under Docker, got OOM, docker container wasn't set to auto restart.  Now it is, so at least when it crashes it can restart itself.



## Jayd603 | 2024-05-10T17:47:54+00:00
> @thilool @Jayd603 how many incoming / outgoing connections to you approximately have?
> 
> I'm curious if there was anyone who had this issue with no incoming connections.

root@ce015ec34800:~/xmr# netstat -na | egrep -c EST  
1224

I've seen it a good amount higher.   

## chaserene | 2024-05-11T16:04:45+00:00
> I'm curious if there was anyone who had this issue with no incoming connections.

@selsta I had an unusually low number of incoming connections during the May 2 consolidation flood, which couldn't be helped even with multiple restarts and a good number of `--add-priority-node`s. my node was syncing so slowly that it looked like it had stopped syncing. meanwhile, monerod's resource utilization was ridiculously low (350 MB ram, 0-1% CPU), so it's possible that for some reason I couldn't connect to any good peers. some people suggested that my node may have been stuck on a bad block, so I popped the height back to before the flood, but this didn't help either. so I just waited and eventually it synced. once it was syncing properly, peer count was also healthy again.

while stalled, my txpool was empty all the time and the best known height alternated between my local height and the actual height I saw on block explorers.

## selsta | 2024-05-11T16:09:25+00:00
@chaserene What about the amount of incoming and outgoing connections before your node "crashed" / got killed for the first time, not afterwards?

## spackle-xmr | 2024-05-11T23:54:05+00:00
Is limiting in/out peers the best potential recommendation for node operators at this time? 
On that topic, can anyone confirm that lowering --max-txpool-weight from the default will cause disconnections?

## selsta | 2024-05-11T23:56:20+00:00
@spackle-xmr limiting in / out is currently a theory, it hasn't been confirmed to work yet.

>On that topic, can anyone confirm that lowering --max-txpool-weight from the default will cause disconnections?

I have seen that behaviour, yes. I had troubles getting incoming connections.

## Boog900 | 2024-05-12T11:36:47+00:00
> The txpool reached around 100MB, but those transactions got propagated over the time of like an hour, they didn't get submitted all at once.

Ah ok, transactions are periodically re-broadcasted after being in the txpool for too long, so this could still happen if a lot of txs re-broadcasts line up.

> >    On that topic, can anyone confirm that lowering --max-txpool-weight from the default will cause disconnections?

> I have seen that behaviour, yes. I had troubles getting incoming connections.

I mentioned this is -dev a while ago but I'll put it here again for visibility. I think this is also because of how txs are relayed.

If you receive a tx, add it to your fluff queue, drop the tx from the txpool, then receive it again, it is added to the fluff queue a second time. When the fluff timer fires we would then broadcast a message with the same tx twice causing the peer to disconnect.

I have tested this and I have managed to make monerod broadcast a message with the same tx twice.

It makes sense that incoming connections are effected more as they have a longer average fluff timer, 5 seconds instead of 2.5 seconds for outbound. Longer time to receive the tx again and add it to the queue. 


## selsta | 2024-05-12T12:16:04+00:00
@Boog900

> Ah ok, transactions are periodically re-broadcasted after being in the txpool for too long, so this could still happen if a lot of txs re-broadcasts line up.

The txpool was empty again after around 12h, would you hat cause re-broadcasts? Also any ideas to improve efficiency here?

> If you receive a tx, add it to your fluff queue, drop the tx from the txpool, then receive it again, it is added to the fluff queue a second time. When the fluff timer fires we would then broadcast a message with the same tx twice causing the peer to disconnect.

Would it be possible to add some check to the fluff queue to disallow duplicate transactions?

> It makes sense that incoming connections are effected more as they have a longer average fluff timer, 5 seconds instead of 2.5 seconds for outbound. Longer time to receive the tx again and add it to the queue.

I had troubles keeping both outgoing and incoming connections, I'm not sure if incoming had more issues but what you are saying seems plausible.

## Boog900 | 2024-05-12T13:40:52+00:00
> The txpool was empty again after around 12h, would you hat cause re-broadcasts?

sorry, I don't know what you mean.

> Also any ideas to improve efficiency here?

Yes, changing how txs are broadcasted around the network. Instead of sending the whole tx blob to every connection (except the one that sent the tx to us first) send the tx hash and the peer can send a request for that tx if it doesn't already have it.

This would require a couple new p2p messages, adding support for these can be done before the changes to how txs are broadcasted, which is how I would recommend doing it.

I am planning to make a proposal for this in a separate issue as I am pretty sure this would significantly reduce the amount of bandwidth used for nodes but I want to test the amount of bandwidth wasted first to see just how much we can save before I do.

For people interested, the way I am planning to test to see how much bandwidth is wasted is by recording data sent and received by monerod in a fully synced state. Then for each link I will monitor the txs sent along it, if the same tx is sent twice (in either direction), both the tx messages will count as wasted as it means the first message of the 2 was not the first time the node received that tx.

> Would it be possible to add some check to the fluff queue to disallow duplicate transactions?

Probably but the queue is kept as raw bytes so we would need to keep a separate list of tx ids in the queue or compare the raw bytes of every tx in the queue to the one we are about to broadcast.

If we adopted the new way to broadcast then this would be a lot easier as the queue would be tx ids not raw bytes.



## selsta | 2024-05-12T13:51:48+00:00
> sorry, I don't know what you mean.

Sorry I mistyped and didn't proofread. I wanted to ask if transactions are typically re-broadcasted within the first 12h of being in the txpool, because that's usually the timeframe of the txpool clearing up again.

> I am planning to make a proposal for this in a separate issue as I am pretty sure this would significantly reduce the amount of bandwidth used for nodes but I want to test the amount of bandwidth wasted first to see just how much we can save before I do.

That sounds like a good idea!

----

Also regarding the drop peer issue with `--max-txpool-weight`, is https://github.com/monero-project/monero/pull/8916 related? Because the change was only done recently, maybe it makes sense to revert it?

## Boog900 | 2024-05-12T14:19:37+00:00
> I wanted to ask if transactions are typically re-broadcasted within the first 12h of being in the txpool, because that's usually the timeframe of the txpool clearing up again.

Yes, txs are rebroadcasted after 5 mins, then 10, then 15, so after every broadcast the wait between them increases 5 mins, up to 4 hours where it is capped.

> Also regarding the drop peer issue with --max-txpool-weight, is https://github.com/monero-project/monero/pull/8916 related? Because the change was only done recently, maybe it makes sense to revert it?

If people have a need to have an extremely low txpool we could temporarily, but we would need people to update to fix this issue, not just the people actually having the issue. I think it makes more sense to just recommend people not set the txpool weight too low, until we fix monerod sending duplicate txs.


## chaserene | 2024-05-12T15:04:08+00:00
> @chaserene What about the amount of incoming and outgoing connections before your node "crashed" / got killed for the first time, not afterwards?

@selsta I don't remember how many connections my monerod had before I first restarted it, but I checked my logs and I see quite a few of the following around that time:

* `monerod is now disconnected from the network`
* `There were 0 blocks in the last 90 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack, or your computer's time is off. Or it could be just sheer bad luck.`
* `Host _._._._ blocked.`

## selsta | 2024-05-13T00:42:24+00:00
@chaserene I'm not sure if your issue is the same as the issue I opened here. I did not see any of these messages on my nodes. I only had issues with high RAM usage.

What kind of hardware do you have? What daemon config do you use?

## vtnerd | 2024-05-17T04:36:47+00:00
> If you receive a tx, add it to your fluff queue, **drop the tx from the txpool**, then receive it again, it is added to the fluff queue a second time. When the fluff timer fires we would then broadcast a message with the same tx twice causing the peer to disconnect.

Is it possible to trigger this (the bolded part) remotely, or do you have to manually drop the tx from the txpool?

## selsta | 2024-05-17T11:24:13+00:00
@vtnerd for this to happen there has to be a large txpool backlog (for example 1MB) and the node has to be set to a smaller txpool limit with `--max-txpool-weight`. Then the node drops / prunes transactions once the limit is reached.

# Action History
- Created by: selsta | 2024-05-03T02:48:23+00:00
