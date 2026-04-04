---
title: 'Daemon error: Failed to update txpool transaction metadata: Error finding
  txpool tx meta: MDB_NOTFOUND: No matching key/data pair found'
source_url: https://github.com/monero-project/monero/issues/2921
author: sleever
assignees: []
labels: []
created_at: '2017-12-14T09:42:40+00:00'
updated_at: '2018-01-30T10:16:37+00:00'
type: issue
status: closed
closed_at: '2018-01-30T10:16:37+00:00'
---

# Original Description
Hello,

Because the Electroneum wallet is a fork of Monero, I would like to raise this issue here as well.

I  hope you can help us out. We're running a pool at https://etnpool.net and are, as of last friday morning (8th of December), experiencing the error in the attached file concerning:

2017-12-14 08:26:29.870	[P2P4]	ERROR	txpool	src/cryptonote_core/tx_pool.cpp:516	Failed to update txpool transaction metadata: Error finding txpool tx meta: MDB_NOTFOUND: No matching key/data pair found

We've tried everything to resolve this, and with everything I mean:

1. Rebuilding the blockchain from scratch (miners were still connected during this process).
2. Rebuilding the block externally, uploading it to the server while miners were not connected.
3. Updating the wallet to the latest version & rebuilding the blockchain, again, externally.
4. Completely reinstalling the server by reinstalling the OS and start off new. We've also changed the ports to mine on to make sure no miner is submitting corrupt shares from before the crash. The blockchain has also been rebuild on this system from scratch.

As you might understand we're quite lost here and would like to know what might cause this issue and, of course, how to solve it. We're under the assumption that due to this error our pool is not possible to correctly talk with the blockchain and thus is not able to submit blocks to the chain (not finding blocks). This issue has currently caused our pool to run dry so this is our last resort.

Additional details:

- We're running our Redis server separately from our main pool server to maintain stats, I am under the assumption that this should not be a problem as the daemon doesn't talk with Redis.

I thank everybody very much in advance for looking into this and helping us out as we really want to start mining again and be of service to our miners.

Best regards,
Stefan

[20171214-MDB_NOTFOUND_no_matching_key_data_pair.txt](https://github.com/monero-project/monero/files/1558594/20171214-MDB_NOTFOUND_no_matching_key_data_pair.txt)


# Discussion History
## moneromooo-monero | 2017-12-14T13:23:24+00:00
I suspect a bug in how monero creates db transactions, but I have no idea what now.

## sleever | 2017-12-14T13:29:21+00:00
Could it affect the possibility to find a block, for a pool?

## moneromooo-monero | 2017-12-14T16:38:35+00:00
I don't think so. I'll have a patch for testing soon I think.

## moneromooo-monero | 2017-12-14T17:11:33+00:00
Try https://github.com/moneromooo-monero/bitmonero/tree/txprel

## sleever | 2017-12-14T21:42:16+00:00
Thanks a lot!

As I mentioned in my initial post, i'm using the Electroneum fork of the Monero wallet, can this patch work for that version too?

Next to that: What does the functionality do and what causes the error message?

The reason why I ask is because after our crash we experienced these errors for the first time and weren't able to find a block for five days while the the hashrate should've been enough (or we were on our way to find a very, very bad block, but that would'be been more than 100% eventually).

I'm concerned this IS actually causing a block to not be found so I would like to exclude that option and why this shouldn't/couldn't be the case.

Again, thank you very much!

## moneromooo-monero | 2017-12-14T22:14:13+00:00
AFAIK they didn't fork that long ago. You'll have to adapt, most likely, but it should be pretty similar. The patch does not try to update the txpool for txes already in a block. If you still get those errors, or similar ones, send another log please.

## sleever | 2017-12-15T08:53:12+00:00
Thanks again for getting back on such short notice. I will look into applying the patch today.

However I would still like to know how to this problem could occur while it first was not an issue. We experienced this issue after we've had a crash and the problem persisted after rebuilding the blockchain several times and even reinstalling the whole server.

Am I understanding it right that the error originates from an effort the transaction pool from an existing block (and upcoming)? If this is the case, couldn't that also be the reason why we're not finding/are able to submit a block and thus that this patch could fix that?

I'm hammering on why this is happening because running a pool and keeping your miners happy is a hard thing to do that's why I would like to know whether this is not able to block our mining efforts to find a block.

Thank you very much in advance again!

I will keep you posted.

## ddvs1 | 2017-12-15T11:03:06+00:00
Hi Sleever, 
I'm getting the same issue in our pool, what path are you going to apply ?

Luis

## sleever | 2017-12-15T11:34:06+00:00
Hi @ddvs1 ,

Are you on Telegram? You can find me at https://t.me/etnpool. I'm currently comparing log files of other pools to determine whether this really is an issue. 

Would you happen to have your electroneum.log file with data all the way back before the 8th of December where you still found blocks?

If you could reach out through Telegram, that would be great.

Best regards,

## phil2cr | 2017-12-21T21:46:56+00:00
Hi,

I got the exactly the same problem (with electroneum), somebody did davance on the problem ? found a solution ?
Now i have delected the data.mdb and lock.mdb file to resync all the block chain

## phil2cr | 2017-12-21T22:05:22+00:00
To add more info i use : 
./electroneumd --db-salvage
(from monero)
The program seems to work but take 3 or 4 second to finish. I didn't check the result.

## phil2cr | 2017-12-21T22:18:55+00:00
Maybe i should have begin with that:
I think i don't found block in the same way @sleever  did describe.
But as the pool begin after the 10 of december is see the error message "Daemon error: Failed to update txpool transaction metadata: Error finding txpool tx meta: MDB_NOTFOUND: No matching key/data pair found" from that time (i have no thing before).

I have Ubuntu 14.4.05
the daemon is linux-x64-0.11.0.0 (from linux-x64-0.11.0.0.zip)
nodejs: node-v0.10.48-linux-x64.tar.gz
db: redis-2.6.14.tar.gz
pool: github.com/fancoder/cryptonote-universal-pool.git

I didn't start the RPC wallet. Only the daemon is ruuning.

## moneromooo-monero | 2017-12-21T22:32:12+00:00
Try the patch linked above.

## phil2cr | 2017-12-21T22:39:23+00:00
OK thanks, i will try when i finish to sync the blockchain and do some tests.

## phil2cr | 2017-12-21T23:22:05+00:00
I would like to have the feeling of everybody.
I did see in the code the result of the function was changed from the return value to a boolean value. I think that is to check the validity of the block.
The problem that happend with the block is coming (from your point of vue) more probably from:
- a pbm in a node of the pool (so all pools have the same problem) ?
- a pbm on the local node (only one pool have a probleme from time to time) ?
- it was caused by the dameon of the blockchain ?
- it was caused by a mining software ?
- it is a glitch in the transmit of the blockchain ?

## phil2cr | 2017-12-22T01:42:41+00:00
I have an other question related to this problem:

To check every thing is fine, how can we know the pool had success mining a block by looking at the logs ? 
- of the deamon
- of the pool
?

## phil2cr | 2017-12-22T01:46:14+00:00
@sleever "from an effort the transaction pool from an existing block (and upcoming)" i don't understand what you mean by that ? (why an "effort" ) ?

Thank you

## phil2cr | 2017-12-22T03:07:14+00:00
hi @moneromooo-monero 

When you say "Try the patch" , you mean it as worked for @sleever or it is the solution to that problem ?

- i am on electroneum (before i hope going to monero) do i have to use the package like that or modify line by line the source of the electroneumd . IF it is this solution, somebody can give the good link for the most stable version of electroneumd (i am using linux 0.11.0.0 x64 ) so i can apply the changes.
- Somebody did have the same problem with monerod ?

thanks


## moneromooo-monero | 2017-12-22T11:57:36+00:00
I mean apply the patch in my comment above. You might or might not have to do that manually, depending on whether electronium made changes to that part of the code.

## phil2cr | 2017-12-22T12:22:27+00:00
Ok, thank you very much.I understand.

But does that mean the bug is because the blockchain is corrupted ? Permanently ?

## phil2cr | 2017-12-22T14:54:51+00:00
Is it a problem with the data from the pool transmited to the daemon ?
 or is it a problem with the data going from the daemon to the blockchain ?
 or is it a problem with the data from the blockchain ?

## moneromooo-monero | 2017-12-22T15:24:26+00:00
It should not be corrupted. Just applying the patch should be enough.

## phil2cr | 2017-12-22T15:41:22+00:00
Ok, Thank you for your answer.
but i must say i didn't find out where to search in the electroneum project to fix this. And they updates are not as often as yours. so maybe the fork is not uptodate ?
I wonder if it is possible to use your monero deamon instead of they fork in a mining pool for electroneum ?

## moneromooo-monero | 2017-12-22T17:53:29+00:00
You can't use a monero daemon to mine electroneum. You'd be mining monero. This bug is not a bad bug anyway, I don't think it's related to not finding blocks.

## phil2cr | 2017-12-22T20:34:54+00:00
Thank you for your answer.

- I asked the question because, i didn't see much difference since the fork.
- If you told me it is not related to not finding blocks i belive you

Have a good day.


## moneromooo-monero | 2018-01-30T09:48:33+00:00
+resolved

# Action History
- Created by: sleever | 2017-12-14T09:42:40+00:00
- Closed at: 2018-01-30T10:16:37+00:00
