---
title: FUTURE_TIME_LIMIT is too far into future.
source_url: https://github.com/monero-project/monero/issues/3367
author: zawy12
assignees: []
labels: []
created_at: '2018-03-07T12:11:23+00:00'
updated_at: '2018-03-17T22:33:45+00:00'
type: issue
status: closed
closed_at: '2018-03-17T18:04:02+00:00'
---

# Original Description
CRYPTONOTE_BLOCK_FUTURE_TIME_LIMIT = 7200 in Monero clones.  If the target solvetime is 120 seconds, an exploit in some difficulty algorithms is possible.  Bitcoin's limit is 7200 which is only 12 blocks into future because it has 10 minute solvetimes.  But with T=120 seconds, that's 60 blocks into future.  This variable should set to 12x the target solvetime, not a fixed value.  Zcash saw problems from not correcting this.

# Discussion History
## moneromooo-monero | 2018-03-07T14:26:32+00:00
Any exploit in particular, or... ? (if so, please use hackerone)

## zawy12 | 2018-03-10T15:24:12+00:00
They did not reply to me, so here goes.

The median of node times upper limit is 7200 seconds in Bitcoin and Monero. This is fine for bitcoin, but appears to be very risky for alts, especially if their target solvetime T is < 600 seconds. Such a large future limit allows can lower difficulty to (N-7200/T)/N of the initial difficulty by a large > 50% miner. For N<61 and T=120 for many clones, a large miner can drive difficulty to zero. N needs to be about 60 for alts.  The default N=720 provides protection against this exploit, but that's a disaster for Monero clones as they typically need to hard fork to reduce the N.  ( I know of 8 Monero clones switching to my algorithms because of this. There's a pull request from Masari using my algorithm that Monero is considering.  )

To do this exploit, a large miner would simply assign a large forward timestamp. But the number of blocks he can get at low difficulty is limited by how low he drives difficulty. He does not want to immediately drive difficulty down if he wants more than 2 blocks. To maximize the number of blocks he can get without difficulty rising, he assign to all his blocks
```timestamp = (HR+P)/P*T + previous_timestamp```
where P is his hashrate multiple of the network's hashrate HR before he came online. For example, if he has 2x network hashrate, he can assign 1.333xT plus previous timestamp for all his timestamps. This prevents difficulty from rising, keeping it the same value, maximizing the number of blocks he can get. With CRYPTONOTE_BLOCK_FUTURE_TIME_LIMIT=7200 and T=120 seconds, this would allow him to get 7200/120 = 60 blocks without the difficulty rising. He can't continue because he will have reached the future time limit that the nodes enforce. He then leaves and difficulty starts rising if negative solvetimes are allowed in the difficulty calculation. If negative solvetimes are not allowed (method 1 timestamp handling in my LWMA), he gets 60 blocks all the same over the course of 90 blocks that he and the rest of the network obtained. The average real solvetime for the 90 would be 1/3 of T (if he has 2x the network hashrate) without the difficulty rising. And when he leaves, difficulty will stay the same. So the algorithm will have issued blocks too quickly without penalizing other miners (except for coin inflation which also penalizes hodlers).

## moneromooo-monero | 2018-03-10T18:04:54+00:00
Sorry, I think I checked once some time after replying here, and then forgot :)

So your overall point is that the more blocks can be fit in the acceptable time window, the more wiggle room there is for someone to craft timestamps as needed for whatever nefarious purposes they have, right ? If so, it looks like shrinking that acceptable window as you suggest should have no adverse side effects.

I don't get this part:
>  The default N=720 provides protection against this exploit, but that's a disaster for Monero clones as they typically need to hard fork to reduce the N.

Why would using a large window to determine difficulty be good for Monero, but bad for clones ? Because clones can have a large variance in hash rate as they start their chain, and need to react faster to hash rate changes ?

I'll ping the MRL people to have a look at this.


## zawy12 | 2018-03-10T18:18:05+00:00
By "they did not reply" I meant hackerone.  I really didn't see too well how it would help.  I have not seen a clear example of this exploit being used, except for the Zcash testnet before they launched. Zcash mentioned they wished they had made the future time limit more like 1500 instead of 3600, so I believe they still saw some problems from not lowering it even further below BTC's 7200.

If Monero is not having problems with N=720, then it's fine for Monero.  But clones of it have to hard fork because, by being smaller, big miners (or pools) can jump on and off more often and more easily.  Also, alts' price can change more, motivating those big miners, pools, or a bunch of small miners.  Several devs have said nicehash caused this type of problem.  Same thing with Bitcoin as for Monero: the largest coin for a given proof of work does not have to worry too much about optimizing the difficulty algorithm. The big miners jumping on and off Monero and Bitcoin do not affect the coins much.  But they have a big effect on alts, forcing difficulty high, so they soon leave to go back to Monero or another alt, leaving dedicated miners stuck with a higher difficulty for at least half a day since N=720. 

## iamsmooth | 2018-03-12T08:56:18+00:00
The original reason for two hours is to be forgiving of incorrectly set clocks, including off-by-one time zone and/or summer time setting. In reality, the limit doesn't really matter for its main security purpose _as long as it is (meaningfully) finite_. Possibly it does matter on micro-hashrate coins, I don't know but for Monero I wouldn't be concerned about it at this point. (Though I would also say that the original reason for the two hour window is also perhaps not that important any more either.)

> For example, if he has 2x network hashrate

We generally don't consider 50% attacks as within the scope of meaningfully addressible problems. If someone has >50% and they want to mess with the network there is nothing we can really do other than change PoW or work to boost and decentralized the hash rate.

## zawy12 | 2018-03-12T10:31:08+00:00
Making it more strict to address a different problem is not a reason to not use it for the secondary problem. I take the position that having code that will be beneficial to clones when its effect is neutral to the master is being a good steward of what the master itself inherited.  I believe good clones are good for Monero if only by marketing.  It at least gives Monero's miners a place to turn if Monero's difficulty/(price+fees) ratio  goes too high. This enables a slightly higher hashrate by giving miner's a more stable difficulty which enables a more predictable profit.  I'm giving a weak argument to support strong zen and good karma. 
 
5x hashrate is a daily problem with small alts, although it is not often I've seen the fake timestamp aspect of that problem occur.  3x hashrate is a daily problem in Zcash.  They originally had problems with large forward timestamps such that they wished they had set it lower than 3600 seconds. As a 2nd example in a large coin, Bitcoin cash immediately experienced 3x hashrate when its difficulty/(price+fees) ratio dropped 30% twice during startup with the new difficulty algorithm.  

Miners seeking a lower difficulty to obtain coin who's value they do not wish to hurt are not going to hurt the network other than attempting to lower the difficulty while they're mining it, so it's meaningfully addressable.

## moneromooo-monero | 2018-03-12T11:48:50+00:00
I think the incorrectly set clock problem can be mostly fixed by printing a warning message if getting a block claiming to be > local + 30 minutes. Failure to sync should be seen quickly, and with 30 minutes, even an off by one (in the wrong direction) should be evident at the first synced block after initial sync.

## zawy12 | 2018-03-12T14:14:17+00:00
I don't know the consequences of changing this variable.  [This article](http://culubas.blogspot.com.es/2011/05/timejacking-bitcoin_802.html) gives details on how it works in bitcoin.  It says nodes revert to using their own clock time if the median of their peers is > 70 minutes wrong (this variable would also need reducing in Monero if FUTURE_TIME_LIMIT is reduced).  In this way they cast their vote for the correct time if the median seems very wrong.  If the median is 70 minutes wrong, then miners can still be 50 minutes wrong in the opposite direction and their block will be accepted (it's still < the 120 minute limit).  But it seems like a distant group of node peers could have a different conclusion as to what the median time is, so in this case, miners don't have the full 50 minutes of leeway for their block to be acceptde by the entire network (if I understand things correctly).  There's also block propagation time delay.

So I wonder if making it smaller than 1 hour greatly increases the risk of a split in the network (and thereby chain) due to time zones and daylight savings.  Can (and what if) 8 (?) nodes with 1 hour off due to daylight savings happen to get together and agree that the 1 hour error is the median and start rejecting all blocks due to the timestamp being > 7xT off?  

## iamsmooth | 2018-03-12T21:54:35+00:00
@moneromooo-monero There are two issues of incorrectly set clocks. One is for the node attempting to sync and the other is for the miner/pool who mined the block. This is particularly acute in the case of systemic errors which could potentially result in a split or at least instability as @zawy12 suggests. For example, on occasions the summer time rules are changed in various countries, and sometimes there are barely-maintained operating systems (e.g. non-current versions of Windows) which don't get proper updates, leading to the possibility of multiple independent mining or non-mining nodes with wrong timestamps by an hour or slightly more (the latter due to added actual inaccuracy).

Is this important? Probably not, but there is also no real reason to change the value either, on a non-microhash coin with a sound difficulty algorithm (Monero's is only mostly-sound, but not too bad). In the case of blocks with timestamps far in the future, the exceptionally long (incorrect) block duration will be balanced by a future (most likely within 1-2 blocks) exceptionally short duration when another block with a correct time is accepted. The only time this doesn't occur is when the miner using incorrect time has a very high hash rate, but even then, such a miner only gets one 'bite at the apple' (moving time 2 hours forward) within the entire difficulty adjustment window. This is one reason not to reduce (and potentially to increase) N: it increases the proportional impact of these one-time manipulations.

I also don't agree that Zcash had a real need to change it, even if they considered it or claimed to want to (or perhaps their difficulty algorithm is broken in some manner, I don't know). Frankly speaking, Zcash has proposed and, less often, done some really stupid things when it comes to blockchain engineering.


## iamsmooth | 2018-03-12T22:10:46+00:00
> I take the position that having code that will be beneficial to clones when its effect is neutral to the master is being a good steward of what the master itself inherited

I'm not against forks/clones (with their own genesis block, and absent some other reason to dislike them) but I don't agree with this at all. 1. It isn't neutral to Monero to be changing these parameters, particularly not without very careful _and correct_ analysis (which is very hard) 2. Forks are by definition trying to do something different than Monero. They can manage their own code changes to address their unique market niche needs (such as working a little "better", maybe, with very low hash rates).

This is also true to the extent that Monero inherited code. We have never expected, nor desired, that the improvements that we want to make to address our intended market to come from Cryptonote or Bytecoin. Of course they like anyone else are _welcome_ to contribute, but not out of expectation, and particularly not out of expectation that they modify their own code/coin to address our different needs.


## zawy12 | 2018-03-13T13:27:13+00:00
I do not disagree with anything you've said, but I still think the limit should be reduced. 

[The article I linked to](http://culubas.blogspot.com/2011/05/timejacking-bitcoin_802.html) describes an attack that is listed as one of [9 possible problems](https://en.bitcoin.it/wiki/Weaknesses#Forcing_clock_drift_against_a_target_node) in Bitcoin's wiki.  The attack depends on the degree to which the future limit is beyond the confirmation window. This indicates the attack is a greater risk for Monero (having the same future limit of 7200 but 3x faster confirmation window of 10x2 minutes instead of 6x10 minutes.)

## b-g-goodell | 2018-03-13T18:32:44+00:00
Can you explain how you derived (N-7200/T)/N? 

You say this (N-7200/T)/N is a bound on how much the attacker can reduce difficulty, but I don't see how this is true: if an attacker performs a clockdrift attack AND has >50% of hash rate, they can set "network time" at will after a sufficiently long clockdrift. But then: the only blocks that the network will accept have timestamps so different from UTC that honest blocks are rejected and the attacker ends up hijacking the whole network.

Why bother messing with difficulty as you describe if you can just kick everyone off the network and write whatever ledger you like? Please explain like I'm a precocious 11 year old.

## iamsmooth | 2018-03-13T18:55:43+00:00
@zawy12 Monero (as with all of the original cryptonote-based coins afaik) is not vulnerable to the described 'timejacking' attack since it does not use network time and nodes can not influence other nodes' clocks. The bitcoin wiki page you linked states:

> It can be fixed by changing how nodes calculate the current time

which is already the case here!

The other article proposes reducing the time window, but then states:

> Nodes with incorrect daylight savings handling might be left behind though.

Which is exactly the issue we have been discussing, and can lead to greater opportunities for network splits and double spend attacks (and unlike the "poison block" variant, these accidental network splits can be exploited without the attacker even needing to incur the cost/risk of mining a block).

So there is not a clear advantage to changing this from the sources cited (though it might possibly  be justified another way).



## iamsmooth | 2018-03-13T18:57:00+00:00
@b-g-goodell clock drift attacks (manipulating network time) and block timestamp manipulation (manipulating difficulty) are two different things. Clock drift attacks do not exist in Monero (but do in Bitcoin) because unlike bitcoin there is no such thing as network time. Monero nodes are responsible for their own clock settings.

## zawy12 | 2018-03-13T19:01:58+00:00
@b-g-goodell I made a mistake.  They can't reduce it by that factor with Monero's difficulty algorithm that subtracts beginning and ending timestamps.  It's only in other difficulty algorithms that attempt to take the slope of the sequence of difficulty/solvetime ratios into account in order to estimate current hashrate. (N-7200/T)/N applies to Moneo in only the block after the bad timestamp like @iamsmoooth said (I'm talking about timestamp manipulation).  The simple moving average that Monero uses gets the difficulty at N/2 blocks the past (as it was 12 hours ago).   

Clones of Monero have miners with 3x to 5x their network hashrate jumping on and off their network all the time, but they do not bother the chain.  They just come in when the difficulty/(price+fees) ratio is a little low and get N/3 blocks before the difficulty rises, then leave. So the dedicated miners will be stuck with about 2x difficulty for the next N/2 blocks. 

## zawy12 | 2018-03-13T19:08:59+00:00
I mean, if they bother the chain, the malicious activity is more clear and a revert to a previous state could cost them.  But if they only lower the difficulty 30% once every day on 10 different coins, there won't be a  hard fork to stop their cash cows.

## b-g-goodell | 2018-03-13T20:43:18+00:00
@smooth : Yes. However, looking at the median timestamp as a proxy for network time, the attacker during a timestamp/difficulty manipulation attack can still cause a drift of the proxy (especially with >50% hashpower as zawy12 assumed), and likewise attacking network time with a clockdrift when difficulty updates each block implies manipulated timestamps/difficulty. So in that sense they play off each other, although they are certainly distinct ideas. Unless I'm misunderstanding either or both of the fundamentals here?

## zawy12 | 2018-03-13T21:09:41+00:00
Yes, with > 50% hashrate more than half the blocks could have the difficulty lowered to (720-7200/T)/720. If he has 2x the baseline hashrate, then he has a 2/3 chance of getting the next block at the lower difficulty.   In that sense I wasn't wrong, but he can't make it slowly drift downward with 60% like I was thinking. 

Is the network time the median of a node's peers?  In that case, and ignoring network delays, if an attacker assigns exactly 7200 seconds ahead of real time, would half the network reject it?  (half think it's < 7200 and the other half think its >7200?)

## iamsmooth | 2018-03-13T21:14:39+00:00
@b-g-goodell Each node has its own notion of time which is used: a) to reject blocks that are too far in the future, and b) to apply timestamps when creating a new block (mining). 

In Bitcoin, the node-specific notion of time is determined via the p2p network by applying a median to other nodes' reported time (I think there might be some other rules, but I don't remember them). This is the so-called "network time". It can pretty obviously be manipulated by connecting to nodes (possibly multiple times) and sending them deliberately incorrect time, which then interferes with the functioning of the node (for example, causing them to reject blocks which they should accept, or accept blocks which they should reject).

In Monero the node-specific notion of time is determined by the node operator (often with ntp but not necessarily, I'd guess that a significant fraction of nodes run with just an approximate time setting and a (not very accurate) hardware clock. p2p nodes have no effect, nor do the timestamps on blocks. This isn't necessarily better, there are negative aspects of relying on a largely-centralized system like ntp (if important parts of the ntp network or common implement are compromised or malfunctions, it would probably mess up the Monero network more so than the Bitcoin network).

Timestamps on blocks are not assumed to be accurate, they are measured relative to each other other for purposes of adjusting difficulty and rejected if too far in the future which (along with guarding against other dumb errors, such as the fencepost error in Bitcoin's difficulty algorithm) protects against time warp attacks.

I don't believe that paying a lot of attention to what an attacker with >50% can do is very important here, apart from guarding against Bitcoin-style time warp attacks. Monero is not perfect in this sense, but it is mostly okay as @zawy12 noted earlier (since it uses a difference of timestamps across a reasonably-wide window, and a sliding window as used in Monero is immune to Bitcoin's fencepost error).

@zawy12 
> Is the network time the median of a node's peers?

In Bitcoin yes. Not in Monero.

> In that case, and ignoring network delays, if an attacker assigns exactly 7200 seconds ahead of real time, would half the network reject it? (half think it's < 7200 and the other half think its >7200?)

Yes that is a well known 'effect' of the rule, regardless of the number chosen, and regardless of whether the nodes use Bitcoin-style or Monero-style node clocks. Either way some nodes will reject the block and some will accept it. 

However, note that a block that is _just slightly_ too far in the future will become not-to-far soon. So if that block continues to get built upon and becomes the longest chain (because the majority of the hash rate did not reject it), even the nodes that considered it too far in the future will then accept it (with some small delay). Since a network split can only be accomplished (apart from for example by exploiting one-hour apart time-zone related issues) with a timestamp that is _very close_ to the limit (so some nodes reject and some accept given normal dispersion of clocks), the delay must be small.


## zawy12 | 2018-03-13T21:40:58+00:00
My understanding of "timewarp" attacks as described in an old bitcointalk post is not possible with rolling average difficulty algorithms. 

I think N=720 is way too big.  It's just so slow.  I want to check Monero's solvetimes to see how it's performing compared to other algorithms.  Where can I get monero's difficulty and timestamp data?  I tried running a node to get the data, but unlike the 10 monero clones I've installed without a hitch, I can't get monero installed (make craps out).

N=100 should be a lot better, but because of the 7200 future limit, you would need to loop over all the blocks to limit any large difference between timestamps to about 6xT instead of letting miners assign 60xT.  I'm getting monero clones to use N=60 to stop the N=720 disaster, and they're doing really well.  There are 4 different equally good ways of estimating current hashrate rather than N/2 blocks in the past that the simple average gives.  3 of them require a loop to get each block's apparent solvetime, which allows this attack, so timestamp handling has to be very careful if this limit is not reduced.

Trying to see if the 7200 can be lowered was a preliminary step to seeing if the N=720 can be lowered.

## zawy12 | 2018-03-14T10:58:08+00:00
A relevant factoid Vitalik tweeted today:

> Right now the time diff between US east coast and central Europe is down to 5 h for 2 weeks, as time changes on 3/11 in US/Can and on 3/25 in Europe. Then it's back to 6 h.

But timestamps are seconds since 1/1/1970, so I don't think that's a problem.

## moneromooo-monero | 2018-03-14T15:20:44+00:00
>  Where can I get monero's difficulty and timestamp data? I

getblockheaderbyheight RPC, you get timestamp and difficulty. getblockheadersrange for batching those.

## hyc | 2018-03-14T15:52:19+00:00
@zawy12 all network time is UTC, timezones and DST are irrelevant.

## iamsmooth | 2018-03-14T21:23:37+00:00
@hyc The issue is people having UTC set incorrectly on their computer, which is mostly equivalent to the wrong time zone/DST settings but correct local time. This is rare on well-maintained servers but definitely does happen in some cases especially desktops/laptops.

## iamsmooth | 2018-03-14T21:28:01+00:00
@zawy12 Speed of adjustment doesn't matter that much unless hash rate is changing so fast that it becomes extreme and therefore an actual problem (hours or longer for a block). Yes that happens on small, insecure coins. It should not and generally does not happen (there are rare exceptions such as during the BTC/BCH split) on coins with a meaningfully-secure mining network. Reducing the window and allowing faster adjustment increases the effectiveness and reduces the cost of any sort of hash rate manipulation attacks, introduces greater instabilities, and is not desirable. The slow adjustment in Bitcoin and somewhat faster but still moderately slow adjustment in Monero (probably faster than idea, though) is not a bug, it is a feature.

Small coins with weak mining networks have a distinct problem space they are trying to solve (or, at least, manage) and can adjust their own parameters accordingly.

I don't think this issue describes any real 'problem' that applies to Monero. It should perhaps be combined with a general 'enhancement' issue on longer term difficulty-adjustment improvements.

## zawy12 | 2018-03-14T21:29:43+00:00
@hyc It seems like if some number of node operators in central europe select some city in Africa that they know is in their time zone as their time zone when they installed the operating system, then their system will calculate the wrong UTC for 2 weeks.  Or maybe they install during the two weeks and select the wrong time zone in order to get the correct local time. Those nodes as a group would reject 50% of the blocks if the future time limit were reduced to 3600, subject to the caveat iamsmooth described.

## zawy12 | 2018-03-15T01:49:35+00:00
@iamsooth I have not yet reviewed Monero, but BCH with their new and improved simple moving average difficulty algorithm with N=144 is not performing as well as small coins using small N with a difficulty algorithm that estimates current hashrate (as opposed to N/2 in past).  By "performing as well" I mean it suffers from more instances of issuing groups of blocks too quickly as a result of the price+fees rising faster than the difficulty. Miners from other coins jump on, leaving dedicated miners with a slightly higher difficulty the rest of the day. Dedicated miners are losing about 2% of the block to this activity when it can be reduced to 0.5%, so it's not a big harm, but it's not nice or optimal.  There were also two unnecessary instances of BCH suffering abnormal delays in the past few months when price dropped.  

A smooth difficulty due to high N indicates a sub-optimal algorithm that poses a risk to the coin. It does not "stabilize" the network, but destabilizes miner profit motivations as price+fees change faster.  A constant ratio of  (price+fees)/difficulty is the feature that's needed (it will slowly drop as hardware efficiency improves or competition changes).  Unlike smooth difficulty, a smooth ratio prevents miners from being motivated to jump on and off as happens with smooth difficulty.  A faster difficulty encourages stability, but if it's made too fast, the ratio will get out of whack too often due to random variation. 

If Monero price dropped to 1/3 in a day, the delays would be terrible, at least if the miners have some place else to go.  The argument that Monero doesn't need to be nice to miners by keeping the ratio accurate is based on miners not having a choice.  I see no benefit to a smooth difficulty.  The small coins greatly preferring the faster difficulty (and finding N=720 totally unacceptable) is an indication that Monero is not playing it safe by sticking with N=720.  Monero has been remarkable in having only 1 instance (that I can see) where it dropped 50% in 2 days. N=720 is not completely safe for fast and persistent drops that could occur in the future, especially if the miners have alternative coins to mine.

N=100 that estimates current hashrate (via EMA, LWMA, least squares, or Digishield's method of tempering the SMA) would perform more optimally and be safer.  This has an expected random variation 
 of about 1/SQRT(N) = 10% every 3 hours (100 blocks) which makes it faster than the expected price+fee variation.  My intuition says random variation should equal expected price+fee variation over the same time period.  So N=200 might be better (for Monero). 

## zawy12 | 2018-03-15T18:54:37+00:00
[Zcash stated](https://github.com/mimblewimble/grin/issues/62#issuecomment-314996886):

> There is more that could be done to resist timewarp attacks. We retained the 1-hour limit on future-dated (relative to local clock) block times from Bitcoin, and should have decreased that significantly. We had a large miner exploit future-dating of timestamps right up to the 1-hour limit for a while; they stopped (I think because they realised it wasn't actually helping them much), but it is still undesirable to allow this if there are any features that expose timestamps.

By timewarp I believe she meant "timestamp manipulation".

I described BCH's N=144 SMA as not doing too badly, but not optimal.  Since their T=600, N=144 is the same as N=720 for T=120 coins, so I was not thinking Monero would do worse.  However, I finally got 73k blocks of difficulty data and it shows Monero is doing substantially worse than it small clones who upgrade the difficulty algorithm.  Here's is Monero compared to Masari, the one who has a pull request for Monero.  The problems at the beginning of Masari were because miners continued their old tricks for 2 days after the difficulty algorithm change, but then stopped because it was no longer profitable.  Notice Masari's metrics were as bad as Monero (3rd Masari chart) only when hashrate (and difficulty) rose a factor of 4 in a few days.

For some reason Monero's problem in this series (compared to BCH) is delays more than miners jumping on too suddenly.

My point is only to show Monero difficulty algorithm can be improved, which I'm saving for a future issue.

![masari_new](https://user-images.githubusercontent.com/18004719/37485024-a5ebb546-2860-11e8-8882-00f43bc9e4bd.gif)

![image](https://user-images.githubusercontent.com/18004719/37517336-71d1e8ac-28e7-11e8-8b65-5792ac855eb8.png)


## zawy12 | 2018-03-16T16:41:28+00:00
I corrected the scale in the above Monero difficulty chart and it shows the problems better. The data in the above chart was soon after the change to 2 minute blocks 2 years ago.  The newest difficulty data below does not show any problem.  The data above included blocks with timestamps that were older than 18 blocks in the past, so Monero was not using MTP like bitcoin, but the new data had only a few blocks that were off more than 100 seconds.

Has the difficulty algorithm or timestamp limits been changed since going to 2-minute blocks?

Here's the most recent data.

![image](https://user-images.githubusercontent.com/18004719/37532816-7e3d2eb0-2916-11e8-8b49-70b9e4a24c96.png)


## iamsmooth | 2018-03-16T20:53:17+00:00
@zawy12 

1. Nothing was changed in the algorithm
2. Timestamp manipulation (by a minority miner) is completely impossible in simple linear algorithms because any manipulation is precisely cancelled by its inverse once a block from a non-manipulating miner is received. Does Zcash use something non-linear? 
3. Non-linear algorithms are much harder to analyze in an adversarial sense, even though they can perform 'better' when block times are considered as a passive statistical process. Even Monero's algorithm which discards outliers (a seemingly reasonable thing to do) turned out to be subject to some manipulation (not seen much in practice AFAIK), probably unrecognized by the original designer. Getting rid of that 'feature' and replacing with a simple moving average would probably be an improvement. I've never seen a proper adversarial analysis of any of the non-linear algorithms (except Monero's outlier discarding, which turned out to be flawed).

## zawy12 | 2018-03-17T00:49:54+00:00
Linear algorithms are not ideal math for difficulty when N is finite (partly because the median of a Poisson is less than the mean). It persistently wants to overshoot which needs a correction factor to bring difficulty  down in order to get the correct average solvetime.  N=720 is so large, it's hard to see the error.  The apparently exact math (it does not need any adjustment in order to get the correct mean solvetime even down to N=1) is Jacob Eliosoff's EMA:
```next_difficulty = previous_difficulty*[ T/t * (1-e^(-t/T/N) + e^(-t/T/N) ]```
which finds [theoretical support from wiki.](https://en.wikipedia.org/wiki/Moving_average#Application_to_measuring_computer_performance)

N=720 SMA has repeatedly resulted in catastrophic failure, corrected by LWMA and SMA's as low as N=17.   I've tested LWMA and EMA to make sure they do not overshoot and to make sure there's no sign of oscillation (which would result from overshooting or not having symmetrical rises and falls as in BCH's EDA).  

An SMA that uses sum of individual solvetimes instead of ```timestamp.begin-timestamp.end``` and makes solvetimes < 0 changed to 0 or 1 leaves a big catastrophic exploit.  If this were the method of getting the sum of solvetimes, AND if a coin has future time limit = 7200, AND if reverse time limit were bitcoin's ~ -6xT, then a 3% hashrate miner could send difficulty to zero (if T=120). As you implied, attempting to apply a fix as a patch (throwing out outliers) rather than from mathematical first principles usually makes things worse.  BCH's EDA and Digishield v3 are other examples of where an attempted fix made things worse.

Zcash uses Digishield v3 which is an SMA like Monero's except their N=17 is "diluted" 75% like this: 
```next_target = sum(last 17 targets) / T / ( 0.75 + 0.25*(timestamp[-1] - timestamp[-17])/T )```
which is an SMA that has been "diluted" (aka "tempered" or "filtered") by the 0.75 and 0.25 factors to act 4x slower than SMA=17.  It takes N =  4x17 = 68 blocks to get the full correct difficulty, but it has a much faster initial small response like N=17.  It works a lot better than SMA, and I was unable to find a better choice for the 0.75 / 0.25 factors.   There are additional min and max limits on sum(last 17 targets) in Digishield which is a patch that makes things worse (for example, it takes 500 to 1000 blocks instead of 68 before it gets to the correct difficulty on startup.)

I went back to look at Zcash's history and did not see a problem from forwarded stamps on mainnet.  They had a large number of large reverse timestamps, that resulted in apparent negative solvetimes.   The blocks after them had large apparent solvetimes.  I did not see the reverse situation of a large solvetime coming before a negative solvetime that was trying to correct it.  The bad timestamp is the first very large or very small, and the one after it being the opposite sign is the evidence that the previous one was the bad timestamp.   I saw the same thing on Monero in 2016 data:  the primary errant timestamps are a reverse time instead of forward.  There are ways for negative stamps to lower difficulty, but the miners were not applying them in a way that tried to do this.  So Daira's comments might have been an error.  I know at least that bitcoin is 7200 and not the 3600 she implied.

I checked Monero's summer 2017 difficulty (before the recent rise of ASICs on it) and it did not have problems either. 

So from an experimental perspective of Monero's history, I can't say it needs to change the future limit or difficulty algorithm.  But I would, based mostly on just wanting something more accurate. The goal of difficulty is to match current hashrate (which I've expressed above indirectly as price+fees).  

I'll close this issue based on not having experimental evidence that future time limit =7200 has harmed coins.  Also because my primary concern about a slow downward drift does not apply to the way Monero gets the sum of solvetimes.

>Non-linear algorithms are much harder to analyze in an adversarial sense, even though they can perform 'better' when block times are considered as a passive statistical process. 

My testing used to center on modelling miner profit motivation with sudden on and off attacks.  I never blindly looked at the statistics.   I wanted the best stability during constant hashrate while keeping the fastest response to sudden increases in hashrate.   In the end I found out that I cuold identify the best algorithm in a simple way:  I throw various hashrate step functions of different strength and time-length, like I've seen on live coins.  Step functions are the hardest to deal with, unless the algorithm is trying to be predictive of the future hashrate and thereby prone to oscillation.  There's an "N" parameter in each one that I adjust to get the same speed of response in all of them.  Then I apply a constant hashrate and see which one has the lowest standard deviation.  That's the winner.  Then I can go back and confirm it with more modelling of different hashrate functions.

Does anyone know how far in the past Monero's timestamps can be?   It's interesting that it abandoned Bitcoin's MTP method.

## iamsmooth | 2018-03-17T03:31:09+00:00
@zawy12 Block solving is mostly poisson, but block _timestamps_ are not, when miners can manipulate them, which they can. By deviating from linear you are trading one set of weakness for others, and the ones you are trading for are much harder to analyze.

You seem to be assuming that the ideal is to track hash rate or solve time exactly but that is not really the case. That is one goal, but it has to be weighted against others, and for a coin with a high hash rate, good liquidity etc, it isn't really the most important within reason. _Approximately_ consistent solve times are perfectly okay as long as minority miners can't do much to manipulate it. 

What you are calling "ideal" math is just not necessary, or necessarily desirable, for this problem.

As for the past timestamps, afaik Monero uses the same method as Bitcoin but the window is larger. I don't remember the parameter.

## iamsmooth | 2018-03-17T03:47:31+00:00
@zawy12 Let me add a bit about what I mean by adversarial. I found the flaw in the Monero algorithm by implementing a multi-agent adversarial machine learning model that simulated miners trying to figure out how to game the timestamps to increase their return (approximately simultaneously, someone from MRL, I believe surae, discovered and described it through mathematical analysis). It was able to find the flaw experimentally and showed how a miner using the exploitive strategy was able to increase mining returns with no increase in mining cost (since adjusting timestamps is free). That said, I don't think this method was at all guaranteed that my method would be able to find the flaw, probably there was a degree of luck.

Another vulnerability concerns network splits or isolation/horizon attacks. If it is possible to reduce the difficulty too quickly (which, indeed, is precisely what you would do to be responsive to down-steps in hash rate), then an attacker who isolates some users can feed them an apparently-current but fake chain with relatively low cost (perhaps needing only to mine a few blocks a high difficulty before the difficulty drops radically). To avoid the adversarial vulnerability it is arguably okay to accept that hash down-steps will result in slow blocks for a while.

But anyway, if you want to analyze things adversarially, you have to consider the full range of strategies available to miners, including strategically lying about timestamps, withholding blocks, using mining attacks in combination with other attacks (or opportunistically to other abnormal conditions), etc. These are not exhaustive of the issues that need to be considered. This is a very complex multifaceted problem. 


## zawy12 | 2018-03-17T09:29:26+00:00
Putting bad timestamps and other attempted manipulation aside for a moment, our solvetimes are always following a Poisson, we just don't know what the current hashrate is.  That's why the math that objectively and correctly measures current hashrate is safer. Applying a linear equation to a non-linear process is not as safe as applying the non-linear EMA which matches the process.  In this way, the EMA makes the average solvetime rise and fall "linearly" rather than non-linearly overshooting like the SMA. Since the Poisson median is less than the mean, the SMA gives too much weight to the faster solvetimes for finite N, sending difficulty higher.  My reason for mentioning the accuracy of the EMA was not sourced in trying to get correct average solvetime as if it is the primary goal, but to provide observational evidence that EMA is the correct math.  I've recommended the LWMA over the EMA because in testing it works a little bit better.

As I said, the N=720 fails real world tests frequently while the others I've suggested do not.  

I immediately told Sumokoin about a year ago to get rid of that outlier rejection as soon as I heard about it.  It was easy to see it was a security risk unless it was done very carefully with non-linear math.  That's why the non-linear EMA beats SMA in estimating current hashrate and is safer: it softens the effect of both large and small "outliers" which are actually just part of the Poisson process.  It is only by accident that this also gives it more protection against timestamp manipulation.   

There is an underlying assumption that Monero's difficulty has been working fine (for Monero but not others) and therefore it is fine.  I support that view to an extent.  In a few months, the LWMA will have more total observational time than Monero in a variety of Monero clones under attack conditions far worse than what Monero sees.  All of them switched because of problems with N=720 SMA.  So in both theory (if estimating current hashrate is theory) and observation, the SMA is not as accurate and as safe.  Monero has had a remarkably smooth upward trend in price (compared to other coins) which has helped it avoid problems. The future could be different.  

>If it is possible to reduce the difficulty too quickly ... it is arguably okay to accept that hash down-steps will result in slow blocks for a while.

You're implying that there's a security improvement that can be gained by not setting difficulty to match the current hashrate as closely as possible.  Coins have shown that these kind of good intentions that go against the ideal math result in more problems than they solve.  Rejecting outliers, asymmetrical limits or filters on the difficulty's rise and fall, and large N in order to get smooth difficulty are examples of good intentions gone bad.

>You seem to be assuming that the ideal is to track hash rate or solve time exactly but that is not really the case. That is one goal, but it has to be weighted against others, and for a coin with a high hash rate, good liquidity etc, it isn't really the most important within reason. Approximately consistent solve times are perfectly okay as long as minority miners can't do much to manipulate it.

You're objecting to my implication that matching difficulty to current hashrate is the only goal.  You're implying that SMA somehow sacrifices accuracy for security.  I'm saying matching difficulty to current hashrate is also the most secure starting point.   

## iamsmooth | 2018-03-17T17:00:32+00:00
> Putting bad timestamps and other attempted manipulation aside for a moment 

No, that is very much a part of the problem space.

> You're objecting to my implication that matching difficulty to current hashrate is the only goal.

Yes I am. As long as you hold to that position we will not see eye to eye on this.

I gave to specific examples of how and why this is the case. I can't help that you refuse to let go of this notion that better tracking of wildly varying hash rates on small unstable networks is a good problem definition. It isn't. Those coins may be making the tradeoffs that make sense to their problem space but they are trading one set of problems for another. There is no reason to invite those new problems into Monero which does not need it.

Likewise, the original purpose of this issue was the claim that "FUTURE_TIME_LIMIT is too far into future". It isn't, given the nature of the algorithm (I can't speak for Zcash, BCH, or other tiny cryptonotes). In fact the number doesn't matter much as long as it is finite, and two hours seems to have some advantages in terms of avoiding misconfiguration-caused splits.

This whole issue is massive fail and basically wasting our time.

The one thing I will agree about is removing the outlier dropping. That should be done in Monero too, and we've known this for some time but apparently have never made a priority of actually doing it. That should happen in the next fork (six months from now, not several days from now).




## zawy12 | 2018-03-17T18:03:04+00:00
I've given the theoretical and observational data that show N=720 with SMA is not as secure or efficient as LWMA with N=60.  You have not provided any theoretical or observational evidence to the contrary.  That your A.I. has not been tested on other algorithms, "linearity", and vague references to undefined miner activity are just various boogie men you've presented to contradict world observation and theory.  If you wish to dispel the notion that your A.I. might find an exploit in EMA, LWMA, or Digishield, then you're welcome to try it.  Yes, we've side-tracked into difficulty off of the issue at hand, but I was trying to clear up your misunderstandings surrounding difficulty. Yes, it appears by not following the reasoning and evidence dispelling your boogie men, you've wasted my time.

## zawy12 | 2018-03-17T18:14:07+00:00
>Those coins may be making the tradeoffs that make sense to their problem space but they are trading one set of problems for another. 

What tradeoffs or problems are you suggesting? They track hashrate better, they have fewer delays, and they are not having to hard fork to fix anything that results from NOT matching difficulty to hashrate. 

In what way are you suggesting N=720 SMA is more secure?   

## iamsmooth | 2018-03-17T20:23:45+00:00
> What tradeoffs or problems are you suggesting?

I gave reasonably complete explanations above. I'm not going to repeat them.

## zawy12 | 2018-03-17T22:30:32+00:00
>Timestamp manipulation (by a minority miner) is completely impossible in simple linear algorithms because any manipulation is precisely cancelled by its inverse once a block from a non-manipulating miner is received. Does Zcash use something non-linear?

Good timestamps cancelling bad timestamps has nothing to do with linearity.  The algorithm only needs to be symmetrical in its effect, which is not the case with linear difficulty algorithms as I explained.

>Non-linear algorithms are much harder to analyze in an adversarial sense

This is not true because to analyze a system with feedback, you have to send it the possible extremes. You have to model a linear control (SMA or Digishield) just as much as a non-linear control because it is a feedback system involving a Poisson process with a non-linear driving force (miners being able to change hashrate and timestamps).   Linearity of just the controller does not simplify anything.  

>[concerning future tmie limit] .. two hours seems to have some advantages in terms of avoiding misconfiguration-caused splits.

This is a theoretical worry we've expressed. Three devs on 3 different coins have told me it's of no concern and Zcash has not had a problem.  It gives miners more leeway for timestamp manipulation, linear algorithm or not.

>I can't help that you refuse to let go of this notion that better tracking of wildly varying hash rates on small unstable networks is a good problem definition.

Assuming "unstable network" means wildly varying hashrate, slow difficulty is the biggest cause of wildly varying hashrate because it prevents difficulty from being able to change as fast as the price which is motivating the wildly varying hashrate.  Monero does not have wildly varying hashrate despite N=720, not because of it.  Monero network is stable despite it.

>Another vulnerability concerns network splits or isolation/horizon attacks. If it is possible to reduce the difficulty too quickly (which, indeed, is precisely what you would do to be responsive to down-steps in hash rate), then an attacker who isolates some users can feed them an apparently-current but fake chain with relatively low cost (perhaps needing only to mine a few blocks a high difficulty before the difficulty drops radically). To avoid the adversarial vulnerability it is arguably okay to accept that hash down-steps will result in slow blocks for a while.

I can't see how difficulty dropping to match hashrate to get the correct solvetime can make an attack easier.   Coins have been using N=17 SMA without noticing a problem like this, so I think the N=200 I suggested should be very palatable.  What is "too quickly"?  200% in a day?  In what way is N=720 optimal to prevent this theoretical vulnerability?  Should it be 7,000?  N=720 is a known danger to Monero if its price ever drops a lot in a day.  The danger increases as more and more GPUs are out there that can easily switch POW, jumping from coin to coin, assuming Monero gets around ASICs again. I would not so easily rule out Monero getting in the same position as its clones.  

If you prefer the SMA, N=200 will be a lot safer in it's ability to prevent Monero from being forced into a sudden hard fork.  Users and miners will be grateful for a better algorithm.

Getting the correct solvetime is the purpose of difficulty. Not doing it well is a hard fork risk and costly to dedicated miners and users who want confirmations to go through.  Being able to not let fake timestamps too strongly affect the hashrate calculation is an integral part of that goal.

# Action History
- Created by: zawy12 | 2018-03-07T12:11:23+00:00
- Closed at: 2018-03-17T18:04:02+00:00
