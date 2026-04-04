---
title: possible speed up for HDDs initial sync, pre-sizing database to the current
  size of the database instead of constant resizing
source_url: https://github.com/monero-project/monero/issues/9822
author: Gingeropolous
assignees: []
labels: []
created_at: '2025-02-26T12:09:15+00:00'
updated_at: '2025-03-28T15:37:44+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
So when testing the new 2for1 writes patches on HDDs, I often noticed that I would find monerod stuck. I thought I would dive into the logs for the "time gaps" that would appear. I turned to claude for a [python script to grab these time jumps](https://github.com/Gingeropolous/timejump/tree/main): 

It turns out its LMDB resizing. 

here's an example:

```
2025-02-24 00:33:24.103	[P2P0]	DEBUG	net.cn	src/cryptonote_protocol/cryptonote_protocol_handler.inl:2781	get_next_needed_pruning_stripe: want height 2137588 (2135448 from blockchain, 2137588 from block queue), stripe 2 (10/12 on it and 2 on 3, 0 others) -> 2 (+0), current peers 118? 118? 110 115 115 115 115 115 110 115 115 115
================================================================================ 154.8 seconds 
2025-02-24 00:35:58.868	[P2P7]	INFO	global	src/blockchain_db/lmdb/db_lmdb.cpp:616	LMDB Mapsize increased.  Old: 94870MiB, New: 95894MiB
```

so just grepping and cutting the output file of part of my sync (i was using a high log level, so i don't have the entire sync in logs), i got 2.7 hours of database resizing. 

now, this is where my computer science knowledge limits and understanding of LMDB starts to show, and those that hate AI will want to bludgeon me. But in conversations with claude, it might be that pre-allocating the space on a spinny HDD could reduce fragmentation, placing all the blockchain data closer to each other. But apparently, ext4 should be doing this itself to a degree, but perhaps windows users don't get to experience that. And of course there would be a massive amount of time spent at the beginning of sync allocating 230 GB or whatever. 

This would also cause an immediate failure if the user doesn't have enough space for this initial allocation. Which would be good info for the user, and get them to use --prune mode off the bat, instead of waiting for an error and having to resync because you can't prune an existing when you have no space left. 

anyhoo, just musing about . Perhaps we don't need to worry about spinny HDDs for much longer.... but plenty of folks still have them. 

# Discussion History
## hyc | 2025-02-28T18:00:39+00:00
As you may (or may not) recall, LMDB was designed to have applications set a single maximum size at the time a DB is created and never bother with it again. Yes, resizing incrementally is a major waste of time. But ignorant whiners complained about dedicating all that disk space to the blockchain and so we had to write the resizing capability.

Another thing to note - on most Linux filesystems, setting a large size on a file doesn't actually allocate the space for the requested size. It's only Windows and some Apple filesystems that don't support sparse files that require all of the space to allocated immediately.

Yes, ext4fs uses extent-based allocation and so should be able to grow files more quickly than older filesystem designs. Some other high performance filesystems like XFS and JFS do as well. Regardless, none of these filesystems will force preallocation of the requested space, so there's no performance impact at creation time for setting a large size.

IMO any fresh run of monerod should just check the amount of free space on the blockchain storage device and set the DB size to "all available space" and be done with it. This question is not specific to HDDs, it should just be the standard operating procedure, always.

## Gingeropolous | 2025-02-28T18:28:40+00:00
>  But ignorant whiners complained about dedicating all that disk space to the blockchain and so we had to write the resizing capability.

well this seems absolutely foolish. The blockchain will eventually take up all that space, so doing it incrementally doesn't provide any benefit for those whiners. 

## hyc | 2025-03-01T09:41:48+00:00
> > But ignorant whiners complained about dedicating all that disk space to the blockchain and so we had to write the resizing capability.
> 
> well this seems absolutely foolish. The blockchain will eventually take up all that space, so doing it incrementally doesn't provide any benefit for those whiners.

Correct. It was never a good idea, but it's hard to go against user perception.

There's a lot of added locking code in the DB driver now just to enable online resizing. Multithread concurrency would improve if all that overhead was removed. Probably the best approach would be to have the DB use all available space by default, with a commandline option to set a specific smaller size limit if the space needs to be shared with other programs.

## Gingeropolous | 2025-03-02T05:29:59+00:00
> There's a lot of added locking code in the DB driver now just to enable online resizing. 

well for the initial sync, the resizing doesn't make any sense. But we still need all that for the constant growth of the DB right?

## hyc | 2025-03-02T13:07:59+00:00
> > There's a lot of added locking code in the DB driver now just to enable online resizing.
> 
> well for the initial sync, the resizing doesn't make any sense. But we still need all that for the constant growth of the DB right?

If you've already allocated as much space as is available, then the only time you'll be resizing is when you've upgraded to larger storage. At that point, I don't think it's unreasonable to stop monerod and restart it with a new, larger size specified on the commandline. I don't see why it needs to be an automatic online operation. It makes no sense to constantly pay the overhead cost of supporting that, when it should be an extremely infrequent event.

## Gingeropolous | 2025-03-02T13:23:30+00:00
gotcha. I guess I don't understand resizing then. I was thinking that as you are getting new blocks from the network after initial sync, then you would need to resize the database. 

My point with this issue is that at the time of a release, we could hard code the current size of the monero database, so that during initial sync, there are no resizing events. As the node continues to remain syncd with the network after initial sync, the database would need resizing (this im not sure on based on what you said). 

Sure, if the release has been sitting out for a while (2 years), then a new user would end up "non-resize synchronizing" to the database size upon release, but then encountering resize events for the blocks that formed after release. 

Or we could get fancy and incorporate current database size into the seed node information / DNS info so that users always experience "non-resize synchronizing" for the initial sync. 

## Gingeropolous | 2025-03-02T13:25:37+00:00
edited title to be more specific, and get rid of "LMDB database" (lightning memory mapped database database)

## jeffro256 | 2025-03-03T06:13:29+00:00
Built into the checkpoint system, we list specific blocks. Given that we mainly have one database scheme (whatever is in `BlockchainLMDB`), every release we could adjust the baseline map size based on those two factors and then include that value in the release code. We could add some code in the `open()` method like:

```
if (first_time_opening)
    do_resize(LMDB_CHECKPOINT_MAPSIZE);
``` 

That at least eliminates most runtime overhead without requiring users to re-run `monerod` with a different mapsize. On Apple and Windows that also doesn't cause as big a spike in upfront allocation of a non-sparse file. 

## hyc | 2025-03-03T17:42:50+00:00
> gotcha. I guess I don't understand resizing then. I was thinking that as you are getting new blocks from the network after initial sync, then you would need to resize the database.

Again, that's wasted work.

1. Give monerod some disk space for storing the blockchain. (E.g., 500GB)
2. Tell monerod to use 500GB.
3. Forget about it until the disk space is full.

It is pointless and stupid to try to track the currently used amount of space since a blockchain always grows.
Just decide how much space you're willing to give to it and be done with it.


## Gingeropolous | 2025-03-03T19:34:38+00:00
> Forget about it until the disk space is full.

If the online resizing isn't active, would monerod just crash out when the 500 GB is hit? Or would the behavior be something like it throwing an error message that says "allocated database space full, please restart with new database size indicated" ?

## hyc | 2025-03-06T14:54:38+00:00
> > Forget about it until the disk space is full.
> 
> If the online resizing isn't active, would monerod just crash out when the 500 GB is hit? Or would the behavior be something like it throwing an error message that says "allocated database space full, please restart with new database size indicated" ?

If the online resizing *was* active, would monerod just crash out when the disk space limit was hit?


## nahuhh | 2025-03-28T15:36:52+00:00
> > > Forget about it until the disk space is full.
> > 
> > If the online resizing isn't active, would monerod just crash out when the 500 GB is hit? Or would the behavior be something like it throwing an error message that says "allocated database space full, please restart with new database size indicated" ?
> 
> If the online resizing *was* active, would monerod just crash out when the disk space limit was hit?
> 

Not sure if sarcasm, but it prints "less than 1gb remaining" and eventually stops being able to sync. Then the downloaded queue grows
(it doesnt crash. Perhaps would eventually OOM if unattended for too long)

# Action History
- Created by: Gingeropolous | 2025-02-26T12:09:15+00:00
