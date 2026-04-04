---
title: We need a note on spinning drives
source_url: https://github.com/monero-project/monero/issues/3996
author: littleblackfish
assignees: []
labels: []
created_at: '2018-06-12T16:53:54+00:00'
updated_at: '2026-03-07T17:53:55+00:00'
type: issue
status: closed
closed_at: '2022-04-08T14:51:42+00:00'
---

# Original Description
So I've been running a full node for a month or two and things have been extremely unreliable. I've reported here on some weird intermittent failure modes which were really hard to trace. Last night I threw on a SSD on that same potato and copied the the blockchain over, and poof! all my problems went away. It was the spinning drive choking all along. 

Sync works on a spinning drive, but wallet really doesn't. Not reliably anyways. I think that might be ok but I haven't been able to find any advice against using a spinning drive. Granted this can be very disheartening to an unsuspecting beginner, I think it is reasonable that we put a very visible advice against spinning drives. 

I guess the alternative is to have conservative enough timeout limits to allow for the drive to do its thing. Maybe a command line option for 'patient mode'?

Where would be the appropriate place to put the notice and should I do it? I am also willing to implement the command line switch as I've been aching to dig into the code and contribute, but is this is a good idea?

# Discussion History
## SRCoughlin | 2018-06-12T17:36:00+00:00
This is not an issue with the code _per se_ but with the requirements of the LMDB database: https://symas.com/anticipating-future-lmdb/   Since most/all new computers have SSD drives the need to support older 'spinning' HDDs will consistently decrease. Whether or not to give some special warning now is debatable, but there no need for a long-term resolution.

## littleblackfish | 2018-06-12T17:39:49+00:00
I agree that is is ok not to 'support' spinning hdds. It is however conceivable that people will experiment with low end hardware and we should let them know they should expect issues with spinning drives. I got no warning and took me a while to figure out why it was choking. 

## moneromooo-monero | 2018-06-12T18:13:49+00:00
There is such a warning in master (on Linux anyway, patches welcome for Windows or Mac). Also, it might work better with a larger C in --db-sync-mode A:B:C.

## littleblackfish | 2018-06-12T18:18:57+00:00
For what its worth, I was looking for it and still did not find it. Now that you told me there is a warning, I still can't find it. :) Where is it? 

## littleblackfish | 2018-06-12T18:20:07+00:00
Oh you meant like a runtime warning, I was thinking more like README level warning. 


## moneromooo-monero | 2018-06-12T18:34:55+00:00
Ah, feel free to add a README one, yes.

## hyc | 2018-06-12T20:17:14+00:00
Not sure I understand this ticket, since it says the daemon syncs fine, and the wallet chokes - but the wallet doesn't use LMDB.

## littleblackfish | 2018-06-12T20:27:54+00:00
When I say syncing I mean daemon syncing the chain to peers, when it chokes is the refresh operation of the wallet (also called sync?). 

I'm pretty new at this but my understanding is that a wallet refresh is pretty heavy on the daemon side LMDB operations, no? Whenever I attempt to refresh my wallet for ~ a weeks worth of blocks the daemon would be unresponsive and drop out after each 1000 blocks or so. It would be like 'no daemon found' but I could trigger another refresh after a few seconds. It would take several cycles of this to get the wallet to refresh to the top block. 

I could see full on IO utilization on iotop while this was going on, and it was immediately resolved with the SSD in there. 

## hyc | 2018-06-12T21:15:50+00:00
OK, that's more clear. And yes, you're forcing the daemon to reread block data off the drive since it's old enough that it's no longer cached in RAM. Seems like a pretty slow drive though, 5400rpm maybe? Also sounds like you have very little RAM on that box, if the most recent blocks were already flushed out of RAM while reading back the old ones.

## hyc | 2018-06-12T21:19:53+00:00
> This is not an issue with the code per se but with the requirements of the LMDB database: 

Actually this is just a matter of physics. You either need larger RAM for caching, or you need to be able to handle a lot of IOPS to retrieve all of the relevant data. Every other database technology that exists is multiple times more resource intensive and slower than LMDB for this type of task.
(e.g., for a DB 5x larger than RAM, LMDB vs LevelDB http://www.lmdb.tech/bench/hyperdex/ )

## littleblackfish | 2018-06-12T21:44:08+00:00
I understand the limitations and don't think there is an actual issue with the code or the db being used. Few months back when I got into monero I put the daemon on my little box that is essentially scavenged parts. This is usually how I get into things and I think this is not uncommon with tinkerers in general. 

A brief search on google suggests that monero is pretty resource friendly compared to, say eth, and so I figured it would play well with my setup. There are instructions for a raspberry in the readme, and this is running on an atom processor with 2 gb ram, mind you, and it runs fine, for the most part. It is just not reliable and when it does fail it does not behave well.  

My point is that the spinning hdd was the deal breaker in this case and this does not surprise anybody including me now that I know what's going on. If we had a note on that, it would have saved me a lot of time fiddling with the thing and trying to figure out why its acting up. You are on point that it could have been remedied with additional memory, so maybe there is some value in posting overall minimum system requirements to inform newcomers. Since it might not be feasible to define absolute minimums, I think a friendly warning about spinning drives should suffice for now. Moneromoo says there already is one on runtime but I have not seen it all this time. 

I prepare bioinformatics workflows for biologists; sometimes when I neglect to tell them the thing will need 2 tb scratch space for intermediate output, the biologist does not know where to start looking when the pipeline fails. Its just lost time. Not everybody that wants to run a node knows LMDB's demands on hardware by heart. Especially with monero where we encourage everyone to run their own nodes. 

Perhaps there is a better platform to discuss this. As it stands now, I'll try to put a gentle warning in the readme and do a pull request. 

## selsta | 2022-04-08T14:51:42+00:00
```
The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
```

This warning shows up when syncing on HDD.

## CocolinoFan | 2026-03-07T17:53:55+00:00
Please make `monerod` work on spinning HDD. Blockchains are big and I want to put on HDD.
Make command line option for starting `monerod` on spinning hard drive and put that in the message that shows when HDD is detected.
As long as HDDs exist and they are widely used, as they are (I'm not asking you to support running `monerod` from an optical DVD), it should work, obviously.
Running `monerod` right now on a HDD is so painful. 

# Action History
- Created by: littleblackfish | 2018-06-12T16:53:54+00:00
- Closed at: 2022-04-08T14:51:42+00:00
