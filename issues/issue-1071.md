---
title: GUI Wallet Feedback
source_url: https://github.com/monero-project/monero-gui/issues/1071
author: pseudopants
assignees: []
labels:
- enhancement
- proposal
created_at: '2018-01-10T23:01:16+00:00'
updated_at: '2018-03-30T01:47:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It was suggested on the Monero subreddit that I come here and post my feedback, so here goes (copied and pasted from my reddit comment):

I'm new to Monero, and tend to look at the world from a marketing/consulting perspective. That's been my world for twenty years, so I can't help but think about things from that framework.

Going off the assumption that the purpose of the GUI is to make Monero more accessible, to help take it from a smaller, command prompt audience, to the wider world, I'm guessing it's main job is knocking down technical barriers to entry. That's where my feedback concentrates.

First off, the GUI stalled out (repeatedly) upon first trying it. Had I not found one of the walk-throughs linked from this sub, that specifically mentioned running the "start-low-graphics-mode" version from the install directory, I would've been dead in the water, and would've moved on.

It's important to consider, because most of the wider world isn't going to find that walk-through.

IMO, the low graphics mode should run by default.

From a marketing perspective, it's a no brainer between one that works 99% of the time and one that doesn't work so often that the workaround is addressed in a walk-through.

Second, as I started typing this I was watching the GUI Wallet struggle to finish synchronizing the last few hundred blocks. 48 hours in, I am now finally connected.

That synch time is an incredible hurdle for the average user who isn't installing it on a dedicated miner, because the synch eats up so much working memory the computer becomes largely useless during the synch. Mine peaked around 3.5 gigs of working memory (that I saw), and I had to constantly stop and start the daemon to knock the usage down in order to be able to use my machine for basic tasks. The synch ran just as well with the lower memory footprint, so why was it hogging so much?

In any case, two days with a dysfunctional computer, in order to adopt Monero, is a big ask. Speeding up that synch, or at least minimizing the RAM usage, should be a priority, again, IMO. Obviously a better system would handle the load better, but most of the world is running on older computers.

Two points on mining: 1) until synched, the error message should really be more clear, perhaps something to the effect of, "Sorry, no mining until you're synched," and 2) this may already be in the works, but a GUI pool, or pools, would be a nice addition. There are better miners out there, but "accessibility" isn't about digging through github to find a command line solution.

Also, any miner on github may not be a dedicated Monero miner, and a dedicated miner today, may add other currencies in the future. There's a lot to be said for keeping your users on a dedicated platform that you control.

In any case, take this for what it's worth. Hope it helps.

EDIT: Also, on the mining, some indication that it's indeed running with my wallet as beneficiary would help with peace of mind.


# Discussion History
## snirp | 2018-01-10T23:26:43+00:00
Posted here at my request, feel free to label this as `won't fix`. I will run through the points one by one and add the individual issues after removing duplicates.

## sanderfoobar | 2018-01-11T13:04:01+00:00
Thanks for your critique/suggestions!

Ill give my 2 cents based on a summary of your post:

#### GUI should start in low graphics mode by default
Running the GUI in low graphics mode disables components related to visual effects, such as off-loading panel transitions to OpenGL with hardware accel. You describe the GUI 'stalling out', at which point you decided to turn these graphical effects off - which implies you either have an old video card, old drivers or integrated graphics. However, this does not influence the syncing of the blockchain.

A better solution would be to detect the graphical capabilities upon starting the GUI, instead of turning on low graphics mode by default. This way, the GUI can adapt to the system it is running on.

####  Sync time is too long
The GUI developers are planning to make it more clear you can choose to make use of a remote node, as opposed to syncing the blockchain locally. This greatly reduces the time it takes for a GUI to get up and running. Such an option would be presented in the welcome dialogs, during wallet creation. As far as I know, this was already being worked on - but don't take my word for it.

#### Mining with GUI
Whilst syncing, no mining. But that restraint can be communicated in a more descriptive error message, I agree. 

Thanks for your suggestions, Github is indeed the right place to make these :+1: 

## medusadigital | 2018-01-11T14:25:23+00:00
regarding 2d renderer as default: https://github.com/monero-project/monero-gui/issues/813



## pseudopants | 2018-01-11T20:05:15+00:00
@skftn, thank you.

> You describe the GUI 'stalling out', at which point you decided to turn these graphical effects off - which implies you either have an old video card, old drivers or integrated graphics.

The GUI starts, suggests turning off the firewall, and then the dialogs go away and nothing happens. You are correct in assuming the problem is with my graphics card, which is why I was attracted to CPU mining and Monero in the first place.

EDIT to add: Using the low graphics mode was a suggestion from a walkthrough linked from the Monero subreddit. Without the suggestion, I would've been stuck at the point of turning off the firewall and then nothing.

> A better solution would be to detect the graphical capabilities upon starting the GUI, instead of turning on low graphics mode by default.

Great solution!

> The GUI developers are planning to make it more clear you can choose to make use of a remote node, as opposed to syncing the blockchain locally.

Ahh, that would be a big improvement.

Any thoughts on a GUI pool/pools? I'm looking at xmr-stak right now, and researching different pools, but would much rather have a turn on and go solution all in GUI Wallet.  

> Thanks for your suggestions

Happy to help!

Also, my apologies for using "synching" instead of "syncing." I read over my own comments yesterday and was driven nuts by the error. That's the problem with Internet comments first thing in the morning...


## sanderfoobar | 2018-03-30T01:22:59+00:00
+enhancement

## sanderfoobar | 2018-03-30T01:23:03+00:00
+proposal

## sanderfoobar | 2018-03-30T01:47:22+00:00
#1071

# Action History
- Created by: pseudopants | 2018-01-10T23:01:16+00:00
