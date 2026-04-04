---
title: SSD Bottleneck and wear with monolithic file.
source_url: https://github.com/monero-project/monero/issues/8208
author: ThomasAn73
assignees: []
labels: []
created_at: '2022-03-05T13:49:50+00:00'
updated_at: '2022-03-05T19:14:36+00:00'
type: issue
status: closed
closed_at: '2022-03-05T17:30:10+00:00'
---

# Original Description
Currently the entire blockchain is saved on a single, monolithic file. Even a pruned chain is 40Gb.

During sync-ing or initial setup this huge file has to be written over and over again to disk. Adding a new block to the chain means the entire 40Gb file has to be re-written even though the last seven years of blockchain data has not changed.

As, such the wear on the SSD is exponential.

Would it make more sense to split the blockchain to multiple smaller data chunks on disk of no more than a Gb? The older data-chunks never change and don't need to waste SSD writes.

# Discussion History
## plowsof | 2022-03-05T15:44:52+00:00
Can you show how you came to this conclusion? Are you certain that's how things work? 

## ThomasAn73 | 2022-03-05T15:53:08+00:00
I am not seeing any arguments in you comment, so I will ignore it as irrelevant.

## rbrunner7 | 2022-03-05T16:40:35+00:00
After poor @plowsof just bounced off you, let me try:

> adding a new block to the chain means the entire 40Gb file has to be re-written even though the last seven years of blockchain data has not changed.

Frankly, that can't be true. Any database that would do that - write the whole DB file when small parts of the data change - would be immediately discarded as clearly not fit for purpose.

But anyway, maybe you have extraordinary proof for your extraordinary claim? Did you actually watch the monerod process write 40 GB, and if yes, with what kind of tool?

## ThomasAn73 | 2022-03-05T17:26:38+00:00
I see, the mdb file is seen as a single file by Windows. So the question becomes: if we append a mere 5bytes to the mdb does windows write 40Gb all over again ?

![Clipboard-2](https://user-images.githubusercontent.com/3271277/156892304-76bd13b5-4b93-4b88-8242-c58b59be1166.jpg)

The drive has been maxing out to 100% for seven days (day and night) during this initial sync. (With my connection at 60mbps I can download a 40Gb file in about 2hr). Even if the drive was a slow SD card it can still write a 40Gb file in about 5hr.
![Clipboard-1](https://user-images.githubusercontent.com/3271277/156892325-ec47e6a9-172c-4f7d-aa20-1e90131932ad.jpg)

The writing to disk is bottlenecking. What is it writing day and night ?




## selsta | 2022-03-05T17:30:10+00:00
> if we append a mere 5bytes to the mdb does windows write 40Gb all over again ?

No.

> The drive has been maxing out to 100% for seven days (day and night) during this initial sync. (With my connection at 60mbps I can download a 40Gb file in about 2hr). Even if the drive was a slow SD card it can still write a 40Gb file in about 5hr.

Syncing the blockchain does a lot more than just downloading blocks. It has to verify transactions and blocks which is extremely IO expensive.

> The writing to disk is bottlenecking.

That's why a fast SSD is recommend.
 

## nahuhh | 2022-03-05T17:30:27+00:00
@ThomasAn73 
No way. Trolling?

This should be closed. 
@selsta 

To give op benefit of doubt, im assuming
- op did initial sync
- op later checked and saw a larger than 40gb io or data download
- op doesnt understand how pruning works

Regardless, @hyc has noted that the DB sync mode does more than a 1:1 write.
Regardless, the whole blockchain isnt rewritten, ever.

Not even when switching from a full to a pruned node. 

## hyc | 2022-03-05T17:38:22+00:00
To be clear, the blockchain stored on disk isn't just a consecutive series of blocks. It's also a bunch of index tables to allow fast lookup by output ID, txn ID, block ID, key image, etc etc etc. Since these IDs are 32 byte hashes which are essentially random, that means creating (and referencing) these indices involves almost exclusively random I/O, which are slower than simple sequential I/Os, regardless of the type of storage device.

And yes, the default sync mode is fairly aggressive about flushing writes to disk precisely because Windows is such an unreliable OS that if we didn't do this, most system crashes would leave a corrupt DB. We've never needed to use such extreme measures on Linux systems but the default has been set that way across all platforms. I'm now thinking it only needs to be set this way on Windows, though.

## ThomasAn73 | 2022-03-05T17:46:39+00:00
Many thanks to @hyc @selsta (and @rbrunner7) for taking time to explain in a granular way and provide some in-depth insight about where my original assumptions could have been wrong; instead of assuming it was just a trolling attempt and be dismissive.

Coming from a Windows environment, I had some inherent mistrust to how the OS is handling write/append operations.

## nahuhh | 2022-03-05T18:37:32+00:00
> about where my original assumptions ~~could have been~~ _were_ wrong; instead of assuming it was just a trolling attempt and be dismissive.
> 

You mean, dismissive like this? 
>I am not seeing any arguments in you comment, so I will ignore it as irrelevant."
>

Look. You might not like the attitude but myself, plowsof and rb went out of our way to try to figure out what you were talking about.
Was obviously a troll job or a misunderstanding, and obviously not a code issue / bug (obviously not even possible )

If you had replied to plowsof with a proper response, by your standards, I wouldnt have called you a troll.

If you have future misunderstandings, GitHub issues isnt the place. 
Can ask questions in matrix.
Im sure hyc and selsta have more difficult problems to solve. 

Personally, if you don't have an ssd, but do have a spare android device, its way faster to sync on android sd card or internal.
1. Less intensive db writes (Linux)
2. Flash storage is way faster than HDD (micro sd or usd flash/ssd)


## ThomasAn73 | 2022-03-05T19:11:35+00:00
@nahuhh 

I have no reason to be snippy to strangers, but Plowsof telegraphic comment was offensive from the get go. It was not an argument and he came in hot with a condescending / elitist attitude. Socially the term "are you certain this is how things work" is tantamount to "are you certain you are not stupid"

He instigated it and you missed the instigation. Maybe you are both low on socialization skills, but I resent you defending it and you will both not receive any responses from me from now on. 

# Action History
- Created by: ThomasAn73 | 2022-03-05T13:49:50+00:00
- Closed at: 2022-03-05T17:30:10+00:00
