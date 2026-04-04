---
title: Open Source ASIC
source_url: https://github.com/monero-project/monero/issues/4533
author: timolson
assignees: []
labels: []
created_at: '2018-10-08T19:52:00+00:00'
updated_at: '2022-07-20T20:24:43+00:00'
type: issue
status: closed
closed_at: '2022-07-20T20:24:43+00:00'
---

# Original Description
We have posted an [open source CryptoNight ASIC](https://github.com/altASIC/Open-CryptoNight-ASIC) design which is 5x better than the Bitmain X3.

We believe specialized mining hardware is inevitable for any proof-of-work and that long term, the CN tweak schedule and creative new PoWs will be defeated. We love Monero and want a future where the Monero chain is always free of threat, instead of hoping that a new PoW approach is working.

We ask the Monero community to consider embracing an open-source ASIC design, possibly with a community-owned co-op manufacturer.  See our README for some of our thoughts about open source and community backed ASICs.

Is there a way to bring commodity ASICs with fair manufacturing to the cryptocurrency world and Monero specifically?


# Discussion History
## bitlamas | 2018-10-10T17:30:16+00:00
I feel like unless a lot of manufacturers from all over the world get on board with this, it will be a very centralized process with maybe 2 or 3 companies manufacturing and controlling the supply of all the ASICs out there.

Honest question: wouldn't just be easier to wait SHA256 ASICs to become somewhat commoditized? I've read somewhere that manufacturers are getting to the limit of how much it can be improved, so I'd say that we're getting near the _perfect_ ASIC.

One of the things that I imagine on a CN ASIC is that it's like a "new" field, so even if everyone decides to embrace this open source ASIC there's still the chance that some random manufacturer finds a way to do it 10x better and keep the secret to themselves.

I have no idea if my concerns are valid or not, but I feel that the whole scene is not mature yet to manufacture and provide components in a fair way to all over the globe, considering logistics, etc.

## timolson | 2018-10-10T18:15:03+00:00
I absolutely agree that CryptoNight should _not_ be used if you want commodity hardware with lots of competition!

If you want commoditization with lots of manufacturers, you need a PoW which is _simple_ and ideally has a _proven optimal_ implementation.  Even SHA is too complex, and we've seen large variance in implementations, as well as hacks such as ASIC Boost.

IMO, a good candidate for an easily-commoditized PoW would be a simple ARX-based hash, the simpler the better.  The most complex part of an ARX hash is the adder, which has been well-studied in hardware for decades.  Of course, proprietary adder implementations are the fastest...

RandomJS is heinously complex and has none of the features you'd want for a commoditized PoW.  There's a very high barrier to entry for implementing it, and enormous scope for clever optimizations.

## BigslimVdub | 2018-10-10T18:34:13+00:00
Cryptocurrency has not evolved enough yet for fair co-op asic practices. We may still be 5-10 years from cooperative implementation of our ecosystem. Right now, the current process works just fine for the average Monero blockchain miner with the support available. Heck the underlying CN code hasn’t even reached its full potential yet. 

## jq8778 | 2018-10-18T02:00:02+00:00
Obviously, the problem is not only the manufacturing side. ASIC algo makes an unnecessary "step", which is to purchase  pro equipment(ASIC mining rigs), for people who want to join monero mining. This kind of "step" may keep people out from joining our community. Also, ASIC miner make hashpower be centralized. It will make a small group of people control a lot of hashpower.  Btc is the best example for ASIC with multi-manufacturers but hashpower is centralized. So i don't think being ASIC/FPGA friendly will be a good choose for our community.

## Cactii1 | 2022-07-20T20:23:27+00:00
Monero now uses RandomX,

Propose to close.

# Action History
- Created by: timolson | 2018-10-08T19:52:00+00:00
- Closed at: 2022-07-20T20:24:43+00:00
