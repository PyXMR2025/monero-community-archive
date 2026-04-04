---
title: Monerod getting OOM killed even with the block_tor.txt
source_url: https://github.com/monero-project/monero/issues/8830
author: Vbrawl
assignees: []
labels: []
created_at: '2023-04-24T21:58:44+00:00'
updated_at: '2023-04-25T14:28:54+00:00'
type: issue
status: closed
closed_at: '2023-04-25T14:28:54+00:00'
---

# Original Description
I was running monerod and I noticed that it got killed, I didn't kill it so I searched about it.

I found that there was an issue before about this, and it's some kind of vulnerability, I did what it said (downloading and including the block_tor.txt file) but that seems to be outdated since monerod got killed again.

If you need any other info don't hesitate to inform me.

I am currently addressing the problem by having a bash file with the following code, and running that:


    while :
    do
        ./monero/monerod --data-dir /mnt/block/monero_data/ --ban-list /mnt/block/monero_data/block_tor --prune-blockchain --in-peers 16 --out-peers 64
        echo >> MONERO_CRASHES

    done

and MONERO_CRASHES will have as many lines as the times it crashed.


Not sure if it's going to work though cause I haven't tested it.
I don't think that's a good practice but I'd like your opinion.

# Discussion History
## selsta | 2023-04-25T02:52:46+00:00
> I found that there was an issue before about this, and it's some kind of vulnerability, I did what it said (downloading and including the block_tor.txt file) but that seems to be outdated since monerod got killed again.

You don't have to add any block file, this is outdated information from years ago.

How much free RAM do you have?

## Vbrawl | 2023-04-25T04:58:06+00:00
I have 1GB of ram in the VM and I've read that monerod minimum requirements are indeed 1GB of ram

But I also found that in order for some people to get monerod to run on raspberry pi they modify a variable in the code, so I'll try that and see if that works.

## selsta | 2023-04-25T04:59:48+00:00
You will need swap if your VM only has 1GB.

## Vbrawl | 2023-04-25T05:00:54+00:00
I'll try that too then, thanks for the response, I'll be back with my results

## Vbrawl | 2023-04-25T14:28:46+00:00
@selsta 

That seemed to work, I added a 2GB swap (just to be sure)

And it hasn't crashed for about 2 hours now.

I'm closing the issue. Thanks for the help.

# Action History
- Created by: Vbrawl | 2023-04-24T21:58:44+00:00
- Closed at: 2023-04-25T14:28:54+00:00
