---
title: Implement Masari's difficulty adjustment algorithm on Oct. 18th
source_url: https://github.com/monero-project/monero/issues/4483
author: MoneroCrusher
assignees: []
labels:
- invalid
created_at: '2018-10-01T14:28:10+00:00'
updated_at: '2019-01-18T14:49:02+00:00'
type: issue
status: closed
closed_at: '2018-10-06T18:48:53+00:00'
---

# Original Description
Hi there,

I think Monero should have a faster difficulty ajdustment algorithm because I think Monero is actively being exploited by large-scale GPU farms (and if Monero is not being exploited, it would be good measure to implement Masari's algo proactively because there's economic inventive to exploit the network and loyal miners).
https://www.coinwarz.com/difficulty-charts/monero-difficulty-chart
The difficulty very predictably varies from +-5 to +-15% within 48 hours.
After the miner leaves, the rest of the network has to deal with increased difficulty, slowly lowering it with time, at which point the big miner comes back to quickly mine some blocks.

If I had a 50-100 MH/s farm I would do exactly the same, bouncing around between different coins & algos to maximize profits at the cost of the rest of the network.
I think something should be done against it. Masari's difficulty adjusts after every block and the window is 60 blocks. I think that's a good approach.
In the face of the Oct. 18th fork where difficulty will stay very high for a couple days I think it's a good time to implement it.

# Discussion History
## SamsungGalaxyPlayer | 2018-10-01T15:00:42+00:00
Duplicate of #2887.

## MoneroCrusher | 2018-10-01T15:25:31+00:00
So it seems like nothing's in the way of implementing it! Or did I overlook something?

## ghost | 2018-10-01T15:49:39+00:00
@MoneroCrusher This is more of an issue for small networks. Monero's difficulty algorithm works all right the way it is.

## MoneroCrusher | 2018-10-01T16:01:48+00:00
@wowario Disagree. Monero's network is 1/12th of Ethereum's measured in absolute RX 570 capacity. As a rational GPU miner with a LARGE farm or pool it makes 100% sense to inflate the Monero network & mine blocks faster for a short period of time until the difficulty has adjusted and to then leave for another network letting loyal miners cope with the difficulty until it ajdusts again (which takes a long time with the Monero network).
This way you can consistently exploit loyal Monero miners & increase profits for you large scale GPU farm significantly. And I think it's actively happening.

Let me ask another question:
Is there a way Masari's difficulty adjustment would actively hurt Monero? I think it makes sense to implement this solely because there's significant economic incentive to exploit the Monero network this way and not patching this flaw is actively asking for it to be exploited.

## ghost | 2018-10-01T16:11:11+00:00
It is probably more profitable and easier to hash attack many shitcoins than a single large network. By the way is it not "Masari's" difficulty adjustment, it is [Zawy](https://github.com/zawy12)'s.

## pallas1 | 2018-10-01T16:12:17+00:00
I don't know masari algorithm, but I know that adjusting too fast up means that big farms go away quicker, leaving the network difficulty high and blocks start coming too slowly. Also be very careful which retargeting algorithm you use, because some coins where hit hard by hackers some months ago. I think the current algo is good and safe, it saved monero when some other coins where hacked.

## plavirudar | 2018-10-01T16:18:14+00:00
Furthermore, there's not been significant evidence that there has been excessive amounts of hash influx. With ASIC/FPGAs you'll expect an increase in hashrate, but hashrate has not changed significantly between the April fork to CNV1 and now. There is no reason to expect a massive hashrate drop. 

## MoneroCrusher | 2018-10-01T16:24:02+00:00
@wowario no it's not feasible to do those "hash attacks" on small networks if you own a large GPU farm. I'm talking about a large Ethereum GPU farm. In fact a 1.5% GPU farm on the Ethereum network is the equivalent of a 50 MH/s farm on Monero and I believe there's more than one 1.5% GPU farm on Ethereum. So why should they want to miss out on additional profits they could make by exploiting Monero's slow difficulty adjustment?
I'm sorry I didn't know it was @zawy12's
@pallas1 Was Masari's algo exploited too? It's been in the wild for quite some time now
>adjusting too fast up means that big farms go away quicker, leaving the network difficulty high and blocks start coming too slowly

The attacker could in fact continue doing a hash attack even with Masari's algo but the frequency would significantly increase. Increased frequency means more shares lost and other potential problems that surface with increased algo/pool/coin switching. It definitely makes hash attacks less attractive.
@plavirudar
I'm not talking about increased hashrate, I'm talking about the 10% increase every other day followed by a 10% decrease. It has been happening since months now and I don't think it's by chance and natural variation.

## pallas1 | 2018-10-01T16:26:00+00:00
Some variations of Zawy have been hacked. Don't know about Masari.

## MoneroCrusher | 2018-10-01T17:00:42+00:00
@pallas1 Thanks for the info, will look into it. By hacked do you mean the a super critical bug that allowed printing coins out of thin air or how exactly was it hacked?

Also this is not just about hashrate attacks, but since we agreed to fork Monero every 6 months, it makes sense to not brick the Monero network for 1 week every 24 weeks. The first ~~20~~ 75 blocks will probably take days again and until the network has equalized it will take a week again..which is not good for Monero. I don't want to send an XMR transaction and having to wait 1 day for it to go through (in the worst case in the first 24h).

## pallas1 | 2018-10-01T17:23:20+00:00
It was hacked by mining blocks faster and faster, but the difficulty didn't rise. It was achieved by playing with the block timestamp. Not exactly printing coins out of thin air, but the effect is similar. At intense coin (now lethean) we were hacked like this, but were quick enough to stop the exchanges and roll back the chain, but that is clearly not an option for a much bigger coin like monero.

## zawy12 | 2018-10-01T17:24:56+00:00
@pallas1  No coins following any variation of **[my LWMA](https://github.com/zawy12/difficulty-algorithms/issues/3)** have been hacked for profit, but  I did allow a change by a dev that resulted in two coins having their difficulty shoot way high from overflow. This occured about 7 months ago.  

But some variations of LWMA are vulnerable to either overflow or timestamp manipulation that results in difficulty being lowered.  

If monero uses LWMA, they should have N=300 instead of 60. This would give it the same stability and yet be 5x faster.  They needed it pretty bad last year when ASICS were a problem, but as long as ASICs aren't a problem the current one (that no clone has been able to tolerate) is good enough.


## moneromooo-monero | 2018-10-06T18:41:47+00:00
In all seriousness, we're not changing something dangerous like this just before the fork.

Later on, if you want to change difficulty algorithm, get a member of MRL to look at it in detail.

+invalid


## zawy12 | 2018-10-06T19:08:26+00:00
@moneromooo-monero in what sense do you consider it laughable and dangerous when almost all monero/cryptonote alts were forced to make this change?  I think it's sufficient to regard it as not needed for Monero, thanks to its size not resulting in the typical oscillation blow up.

## moneromooo-monero | 2019-01-18T14:49:02+00:00
"Dangerous" means "if it's broken, consensus can break down and it'll be pretty annoying to fix as we'll have several chains growing while we scramble". That would be the opposite of laughable.
If you want to comment on a closed bug/PR, better to do so on IRC or I probably will only see it if random chance :)

# Action History
- Created by: MoneroCrusher | 2018-10-01T14:28:10+00:00
- Closed at: 2018-10-06T18:48:53+00:00
