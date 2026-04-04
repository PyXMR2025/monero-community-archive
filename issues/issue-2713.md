---
title: Better display of daemon sync progress
source_url: https://github.com/monero-project/monero-gui/issues/2713
author: rbrunner7
assignees: []
labels: []
created_at: '2020-01-10T07:19:03+00:00'
updated_at: '2020-06-29T22:24:11+00:00'
type: issue
status: closed
closed_at: '2020-06-29T22:24:10+00:00'
---

# Original Description
This is about the daemon sync progress bar, lower left of the GUI wallet main window.

It seems that currently for this progress bar the 100% value is always current blockchain top, which therefore now means a large number of over 2,000,000.

If my daemon needs to sync e.g. 20,000 blocks, which means it's behind almost a full month, even that relatively large sync distance is a mere single percent of the whole blockchain. Sync progress display will therefore happen in the last few pixels to the far right of the progress bar.

If I sync a typical 1,000 blocks "from overnight" the progress bar will probably always fully show, not being able to show progress over syncing a mere 0.05% of the whole blockchain.

This is not very useful :)

What would be a better daemon sync progress display with this progress bar?

My proposal: 100% for the progress bar is the total amount of blocks to sync, which means the very first number of "Daemon blocks remaining" that the GUI wallet was able to calculate after starting sync.

Example: If the wallet finds out right after starting sync that e.g. 1600 blocks are to sync until current blockchain top, it should display the progress through syncing those 1600 blocks. After syncing 800 blocks the progress bar would show 50%. With 160 blocks remaining the progress bar would stand at 90%.

If somebody has to sync from scratch and needs to fetch over 2,000,000 blocks, with that logic the progress bar would work like it does now and correctly show progress over syncing those 2,000,000+ blocks.

Of course "blockchain top" is a moving target, and blocks will be added while the daemon syncs, but it's trivial to periodically adjust the 100% percent value for the progress bar, e.g. from 1600 to 1605.

# Discussion History
## GBKS | 2020-01-16T17:21:19+00:00
Totally agree with this change.

Would also be nice to show the estimated sync time remaining (could be calculated by numberOfBlocksToSync / averageBlockSyncTimeInTheLastTenMinutes or something like that). Clicking could maybe switch back and forth between estimated time left and blocks remaining. I bet that a time indicator would be more helpful to most users.

## rbrunner7 | 2020-01-16T18:17:56+00:00
> Would also be nice to show the estimated sync time remaining

I just programmed this for the daemon console log, it's waiting as a PR [here](https://github.com/monero-project/monero/pull/6278). It's not trivial to arrive at useful estimates, but doable.

But just changing the 100% value of that sync bar might be piece of cake for somebody that knows their way around that QML / C++ code mix, a very low-hanging fruit so to say.

## ghost | 2020-04-04T13:37:36+00:00
Some guy already showed how your ideas could look like (#2304):

![image](https://user-images.githubusercontent.com/46682965/78452139-d2f39f80-7689-11ea-9d92-cbc9da6b7b89.png)

As described in detail in #2304, there's a lot more to consider when fixing the status bars. 

## selsta | 2020-06-29T22:24:10+00:00
#2881

# Action History
- Created by: rbrunner7 | 2020-01-10T07:19:03+00:00
- Closed at: 2020-06-29T22:24:10+00:00
