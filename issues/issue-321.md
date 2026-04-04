---
title: 'Discussion of the future of the PoW algorithm #2'
source_url: https://github.com/monero-project/meta/issues/321
author: dEBRUYNE-1
assignees: []
labels: []
created_at: '2019-03-25T15:55:29+00:00'
updated_at: '2020-06-05T15:25:49+00:00'
type: issue
status: closed
closed_at: '2020-06-05T15:25:49+00:00'
---

# Original Description
A productive meeting about the future of the PoW algorithm took place yesterday (logs can be found [here](https://repo.getmonero.org/monero-project/monero-site/blob/b87354501b6343f9146f331805ddadc45696f728/_posts/2019-03-24-logs-for-the-dev-meeting-held-on-2019-03-24.md)). Furthermore, common ground was found as well. That is, rough consensus was that: 

(i) RandomX, if ready, would be preferred over another tweak in October. 

(ii) The path of least resistance seems to be a course of action where RandomX is adopted in October and a switch to an ASIC friendly algorithm (such as SHA3) is made in case of a RandomX failure. This path was preferred over precommiting to a set date for a switch to an ASIC friendly algorithm. 

I'd like to use this issue to further discuss a few things that were brought up in the meeting. The most salient point of discussion is how to qualify failure of RandomX. I personally mentioned ASIC miners driving out all other miners, thereby showing a significant efficiency advantage. sech1's comments are consistent with this notion:

>**<sech1>** steep increase in hashrate (and profitability drop) without price changing is a strong indicator of more efficient hardware (ASICs)

And:

>**<sech1>** I think "RandomX failed" condition comes true only when there is no debate about it in the community at all. Like when hashrate spiked so much and for so long time that everyone gets 20% (at best) from money spent on electricity.

Other aspects we can use to gauge failure (though they are more prone to manipulation / gaming):

- Mining profitability compared to other coins. 

- Reports of miners leaving the network. 

- Efficiency statistics in case an ASIC manufacturer creates an ASIC for RandomX and publicly sells it. 

Some other points of discussion:

- How to find capable reviewers that can check the degree of ASIC resistance for RandomX?

- In case of a RandomX failure, should we switch to SHA3 immediately or allow a bit of a grace time (e.g. 3 months after RandomX is qualified as failure)?

Lastly, I'd like to kindly ask anyone to stay on topic and ensure this issue retains a high signal to noise ratio. The previous issue got kind of cluttered when people digressed. 



# Discussion History
## SamsungGalaxyPlayer | 2019-03-25T17:40:09+00:00
I believe the best way to gauge failure is the presence of private ASICs that a) control a majority of network hashrate, or b) are expected to control a majority of the hashrate within 3 months. I use 3 months as a benchmark for a quick switch to SHA3 (or other similarly ASIC-friendly algorithm), since most manufacturers and expects say that this time is appropriate.

For a) and b), Monero should evaluate RandomX to see if a fatal, patchable flaw is known. If there is a patch that will improve RandomX and remove this flaw, it should be considered instead of SHA3. If, however, no flaw is known and any tweaks would just break the current round of ASICs, this option should not be considered.

Then, under a), Monero needs to either a1) wait it out until SHA3 is implemented, or a2) emergency fork with a tweak until SHA3 will be implemented 3 months later. I think this is a good point of discussion. Both have pros and cons.

Under b), Monero still has the same two options, but the community may decide to prefer the former over the latter to avoid an emergency hardfork. This may be especially the case if ASICs are expected to threaten the network near the end of the 3 month window.

Some of the other mentioned measurements are indicators that ASICs may be present, but I would not commit us to using one of those at certain thresholds. I would instead say that people should make the case for network issues using whatever indicators are sensible. Ultimately, a call will need to be made at that time, and it could be controversial. I believe an expressed intent to follow the actions outlined above is enough.

## tevador | 2019-03-25T17:43:27+00:00
I'm reposting the overview of RandomX performance compared to CryptoNight (CNv0 = original CryptoNight, CNv4 = current PoW).

These 4 machines were used as the testing sample, representing low-end, mid-range and high-end systems:

|CPU|Architecture|RAM|OS|AES|
|---|------------|---|--|---|
AMD Ryzen 7 1700|x86_64|16 GB DDR4|Ubuntu 16.04|HW|
Intel Core i7-8550U|x86_64|16 GB DDR4|Windows 10|HW|
Intel Core i3-3220|x86_64|2 GB DDR3|Ubuntu 16.04|software|
Raspberry Pi 3|armv7l|1 GB DDR2|Ubuntu 16.04|software|

Software used:

RandomX 0.3.3: https://github.com/tevador/RandomX
xmrig version 2.14.1 (CNv0 and CNv4): https://github.com/xmrig/xmrig

RandomX has 2 modes: "light" mode requiring 256 MiB of memory and "full" mode, which requires 2 GiB of memory.

### Single threaded performance

Table lists the performance using 1 CPU thread.

|CPU|CNv0|CNv4|RandomX (light)|RandomX (full)|
|---|----|----|---------------|--------------|
AMD Ryzen 7 1700|70 H/s|68 H/s|68 H/s|590 H/s|
Intel Core i7-8550U|79 H/s|74 H/s|94 H/s|770 H/s|
Intel Core i3-3220|29 H/s|26 H/s|78 H/s|-|
Raspberry Pi 3|3.1 H/s|1.0 H/s|3.2 H/s|-|

### Multi-threaded performance

The number of threads was selected for maximum performance.

|CPU|CNv0|CNv4|RandomX (light)|RandomX (full)|
|---|----|----|---------------|--------------|
AMD Ryzen 7 1700|536 H/s (8T)|522 H/s (8T)|640 H/s (16T)|4250 H/s (8T)|
Intel Core i7-8550U|255 H/s (4T)|198 H/s (4T)|128 H/s (4T)|1660 H/s (4T)|
Intel Core i3-3220|42 H/s (4T)|42 H/s (4T)|187 H/s (4T)|-|
Raspberry Pi 3|10.7 H/s (4T)|3.5 H/s (4T)|12.3 H/s (4T)|-|

### RandomX initialization times

For fair comparison, it should be noted that RandomX needs to be reinitialized every 2048 blocks. The table lists this initialization time in seconds using the optimal number of CPU threads:

|CPU|RandomX 256 MiB|RandomX 2 GiB|
|---|-------------------|-----------------|
AMD Ryzen 7 1700|0.61 s|3.0 s|
Intel Core i7-8550U|0.55 s|3.5 s|
Intel Core i3-3220|0.75 s|-|
Raspberry Pi 3|8.3 s|-|

### Time to verify 1000000 consecutive blocks

This simulates the time of initial blockchain download, assuming inifinite download speed and no other verification except PoW. In reality, the differences will be smaller. For RandomX, the times include reinitialization every 2048 blocks.

|CPU|CNv0|CNv4|RandomX (light)|RandomX (full)|
|---|----|----|-----------|--------------|
AMD Ryzen 7 1700|31 minutes|32 minutes|31 minutes|28 minutes|
Intel Core i7-8550U|65 minutes|84 minutes|135 minutes|38 minutes|
Intel Core i3-3220|400 minutes|400 minutes|95 minutes|-
Raspberry Pi 3|26 hours|79 hours|24 hours|-|

In this case, there is a large difference especially for low-end machines without hardware AES, where RandomX is much faster than CN/R even in "light" mode.

### Time to verify a new incoming block

This is important for block propagation, DoS attack resistant and also for pools, which have to verify a large number of hashes.

|CPU|CNv0|CNv4|RandomX (light)|RandomX (full)|
|---|----|----|-----------|--------------|
AMD Ryzen 7 1700|14.3 ms|14.7 ms|14.7 ms|1.7 ms|
Intel Core i7-8550U|12.7 ms|13.5 ms|10.6 ms|1.3 ms|
Intel Core i3-3220|34.0 ms|38.2 ms|12.8 ms|-|
Raspberry Pi 3|320 ms|1000 ms|310 ms|-|

In this case, RandomX is faster across the board, allowing much faster verification for higher-end systems and systems without hardware AES.


## needmoney90 | 2019-03-25T17:58:18+00:00
Here we go again

## OrvilleRed | 2019-03-25T18:13:35+00:00
From yesterday's meeting, the specific ASIC-friendly algorithm to use (should one be needed) seems to warrant further discussion.
To avoid confusion, I would suggest referring to "an ASIC-friendly algorithm" rather than specifically "SHA3" until there's consensus on that point.

## dEBRUYNE-1 | 2019-03-25T18:16:54+00:00
@sgp:

>b), Monero should evaluate RandomX to see if a fatal, patchable flaw is known. If there is a patch that will improve RandomX and remove this flaw,

I'd be strongly opposed to trying to patch RandomX for the following reasons:

- We cannot know with certainty what to patch unless we have access to the device that is enjoying the significant efficiency advantage. Put differently, patching is conjecturing unless we're in possession of the ASIC (i.e. how do we know the exploit we're trying to patch is actually the exploit used to gain a significant efficiency advantage?).

- A patch may well introduce another efficiency advantage that can later be exploited.

- Patching is essentially tweaking and thus reintroduces the risks associated with tweaking listed here:

https://github.com/monero-project/monero/issues/3387

- Patching once is going to open the door to continue a strategy of tweaking, a course of action we're seeking to discontinue. 

In my opinion, patching should not be considered. History has proven that the tweaks are ineffective, inherently centralizing, and potentially dangerous. In my opinion, it would be foolish and irresponsible to continue them in any kind of form. If RandomX fails, we should not try to apply band-aid, but rather switch to an ASIC friendly algorithm such as SHA3. Arguably, the risks of switching, at that point, are significantly less than the risks of trying to patch a failed algorithm. 

## SamsungGalaxyPlayer | 2019-03-25T19:28:02+00:00
@dEBRUYNE-1 in my opinion, your hard line against all forms of patching is not appropriate. Is SHA3 has a fatal flaw for example, it's likely a patch would be implemented. To take such a firm line against all forms of improvement is far too aggressive.

> In my opinion, patching should not be considered. History has proven that the tweaks are ineffective, inherently centralizing, and potentially dangerous. In my opinion, it would be foolish and irresponsible to continue them in any kind of form. If RandomX fails, we should not try to apply band-aid, but rather switch to an ASIC friendly algorithm such as SHA3. Arguably, the risks of switching, at that point, are significantly less than the risks of trying to patch a failed algorithm.

I still believe you are not understanding my point, or at least you are taking the impact of a completely different type of patch and claiming it will have the same impact in this other case. I ***do not*** advocate for RandomX patches that would merely break existing ASICs, *except* as a potential short-term measure as Monero transitions to SHA3. This would only occur if the network is already in a severely vulnerable state as I outlined in a) in the previous comment. And even so, Monero would need to evaluate in the moment if it would be worth doing this instead of waiting it out or immediately transitioning to SHA3 without any established resources and a nonexistent market.

***I instead advocate*** for RandomX patches in the case some vulnerability is discovered or exploited. This is not merely the case that someone made something more efficient. It's the case that the audits overlooked some critical vulnerability that can be patched. This may or may not happen with ASICs having substantial control over the network.

Only in this case do I recommend a patch to update RandomX to be useful again. I feel that this action will have fewer consequences than another "tweak" in the sense we experience them now. Most notably, we are not committing ourselves to "tweak" it again in the future. It instead falls in line with any other critical vulnerability patch, including any needed patches for SHA3, RingCT, or anything else related to Monero. If Monero switches to SHA3, for example, we should expect that Monero will patch any related vulnerabilities if they arise.

## dEBRUYNE-1 | 2019-03-25T20:06:34+00:00
Your initial comment was rather ambiguous with respect to what a patch meant. In light of this debate, it was logical to assume it meant another tweak to the RandomX to either curb ASICs or to further try to strengthen (emphasis on try) ASIC resistance. My previous comment was a response to that notion. If you want to properly discuss this, you should be more clear. 

Code bugs should be patched, sure, but I don't think they are particularly relevant in this discussion. 

## stoffu | 2019-03-26T01:54:58+00:00
I imagine that when RandomX ASICs finally appear and dominate mining, someone will start claiming "RandomX was missing XYZ (e.g. IO-hard) aspect which is essential for beating ASICs. We should try RandomX 2.0 with XYZ!", to which the community would respond "We're sold, why not give it a try."

ASIC resistance is such a pipe dream that is hard to give up. Let's see if my prediction becomes true.


## OrvilleRed | 2019-03-26T02:12:59+00:00
The PoW algo is just a subsystem, like other subsystems.

Incremental improvements to RX would presumably be dealt with in the same way as other non-critical enhancements, and bundled in the next (semi-yearly or less) release.

Similarly, critical flaws or vulns should be patched at the earliest opportunity. This would equally be the case for a SHA3 or EthHash implementation (even the reference ones...)

That is very different from a reactive "ZOMG! Make a random RandomX tweak to brick the ASICs!"

## dEBRUYNE-1 | 2019-03-26T07:47:34+00:00
@denisgoddard 

>Incremental improvements to RX 

"Improvements". They are simply tweaks and my previous post fully applies here:

https://github.com/monero-project/meta/issues/321#issuecomment-476318615

>would presumably be dealt with in the same way as other non-critical enhancements, and bundled in the next (semi-yearly or less) release.

They are vastly different. We cannot deal with them similarly than normal code improvements that require a consensus change. 

We've got to get off this crazy train of thought where tweaks are seen as a viable strategy. I instigated this debate to get away from them and seek common ground on a long-term solution. To reiterate, history has proven that the tweaks are ineffective, inherently centralizing, and potentially dangerous. 

On an administrative note, discussion regarding this subject (i.e. tweaks) is, in my opinion, already cluttering this ticket and it's merely a day old. 

----------------------

@stoffu:

The idea is to find a course of action (currently RandomX in October -> switch to an ASIC friendly algorithm (such as SHA3) in case of failure seems to be the path of least resistance) we can all reasonably agree on and to stick to that as to avoid the scenario you described. 

## hyc | 2019-03-26T17:25:46+00:00
@stoffu with respect, you have no idea what you're talking about. You might get a better understanding of what makes single-purpose hardware fast by reading other articles on the subject, like this one http://yosefk.com/blog/its-done-in-hardware-so-its-cheap.html

Key points:
* specialization lets you gain efficiency from removing the overhead of generic control flow
* parallelization lets you gain performance - but not efficiency

You've been spouting your skepticism for a while now, but at this point it's irresponsible of you to continue to do so without actually educating yourself on the topic.

## timolson | 2019-03-26T23:47:51+00:00
@hyc
> @stoffu with respect, you have no idea what you're talking about.

If we are slinging ad hominem attacks, then maybe YOU don’t know what you’re talking about. How many ASIC’s have you designed, hyc?

Recently an actual hardware designer (from Linzhi) showed up in the RandomX technical thread with some criticism of RandomX, so maybe we should listen to her not you.

Stoffu has every right to express his concerns, especially in light of recent tweaks not living up to their anti-ASIC claims. 

## WhyIsThisSoSlow | 2019-03-27T00:01:00+00:00
@dEBRUYNE-1 @stoffu @timolson 
I do understand that you guys may be ASIC advocates that really want to see RandomX fail, and see ASIC adoption ASAP, but let's put preference aside for a moment and think logically. 

There will be a need for Tweeks or Improvements to the RandomX algo, as nothing is perfect and everything can be improved. 
These updates (there was one a few days ago) will make the algo function better and can be done once an year or whenever the rest of the updates go in. 
In this sense when it comes to the ASIC part we should be ok with improvements that may reduce ASIC performance but do not brick them entirely.

On the other hand, critical bugs may be discovered and need to be patched ASAP. Bugs can occur on any algo, no matter if its ASIC friendly or not.

We all understand that an ASIC dominated network is the goal when they become commodity but let's not destroy years of work by rushing into it for no good reason. 
There is no long-term solution when it comes to technology like there is no BAD ASIC,there is just monopoly and centralisation,thus we need to adapt and improve.

And to get back on topic i believe that if we can analyze the pattern of new HR/DAY or WEEK and compare it to profitability we for sure have valuable data. No one likes to mine at a loss for a long period of time.
There is also always the nonce analysis that can verify if the hash analysis is correct.

## timolson | 2019-03-27T00:50:04+00:00
Profitability may not be a good metric. IMO, botnets will mine RandomX at a loss to their victims, regardless of the 2GB table. 

## WhyIsThisSoSlow | 2019-03-27T01:07:25+00:00
> Profitability may not be a good metric. IMO, botnets will mine RandomX at a loss to their victims, regardless of the 2GB table.

That is a valid point but for example, IF I had a botnet i would mine a coin that has more profitability and make twice the money. Most botnet infections tend to be created on open source code of popular multi algo miner software. If you invest time in creating and spreading a botnet would you not want to be as profitable as possible? There is a very small chance that these botnets would be created for unattended use.

## stoffu | 2019-03-27T01:29:39+00:00
@WhyIsThisSoSlow 
> On the other hand, critical bugs may be discovered and need to be patched ASAP. Bugs can occur on any algo, no matter if its ASIC friendly or not.

Patching critical bugs (e.g. [the key image subgroup bug](https://src.getmonero.org/2017/05/17/disclosure-of-a-major-bug-in-cryptonote-based-currencies.html)) and "improving" the PoW algorithm are two entirely different things. The former is expected to happen rather rarely thanks to public scrutiny, while the latter is expected to happen rather frequently thanks to the market growth. The most serious drawback of ASIC resistance is that every sudden spike in hashrate forces an emergency PoW change hard fork which makes the protocol very unstable and centralized.


## stoffu | 2019-03-27T03:02:59+00:00
@hyc
> You've been spouting your skepticism for a while now, but at this point it's irresponsible of you to continue to do so without actually educating yourself on the topic.

Your overconfidence seems irresponsible to me. My confidence in the healthy growth of the ASIC market is based on what Bitcoin has gone through. I feel much more comfortable betting on that rather than your wishful thinking which solely is backed by the technical knowledge of just *three* people (you, @tevador and @SChernykh).

You are the most technically knowledgeable person among all the Monero contributors opting for ASIC resistance, so if Monero dies (i.e. price drops to zero and stays there indefinitely and no one runs full node) because of this, you will be primarily responsible for the consequence. I'm not sure if this matters to you, though.


## dEBRUYNE-1 | 2019-03-27T07:34:16+00:00
@WhyIsThisSoSlow 

>that really want to see RandomX fail,

I've never stated that I want to see RandomX fail. I stated that I have doubts about the proclaimed theoretical maximum efficiency advantage of 2x. My intention to have a solid back up plan (i.e. switching to an ASIC friendly algorithm) in place in case RandomX fails. 

>Improvements 

"Improvements". My previous post fully applies here:

https://github.com/monero-project/meta/issues/321#issuecomment-476510926

Why anyone even wants to discuss a strategy of performing tweaks whilst the vast majority agrees it is not viable is beyond me. Besides, I consider it off-topic for this ticket and would like to focus on the discussion posts listed in the OP.

--------------------

@timolson 

>Profitability may not be a good metric. IMO, botnets will mine RandomX at a loss to their victims, regardless of the 2GB table.

Profitably figures will be somewhat skewed by botnets. However, I think we can still reasonably use profitability as metric (especially in comparison to other coins). The metric should not be used as stand alone metric though. 

## SChernykh | 2019-03-27T07:47:43+00:00
@stoffu @timolson Instead of going down to "you fool - no, you" level, I'd prefer to discuss technical details regarding RandomX weaknesses, if there are any.

## tarris034 | 2019-03-27T08:37:23+00:00
@dEBRUYNE-1 
>In my opinion, patching should not be considered. History has proven that the tweaks are ineffective, inherently centralizing, and potentially dangerous. In my opinion, it would be foolish and irresponsible to continue them in any kind of form. If RandomX fails, we should not try to apply band-aid, but rather switch to an ASIC friendly algorithm such as SHA3. Arguably, the risks of switching, at that point, are significantly less than the risks of trying to patch a failed algorithm.

I'm glad not all developers think this way, otherwise every OS would be full of holes.
Even FIAT banking systems needs worldwide update from time to time.

I see nothing wrong in patching, lets not confuse them with *tweaking*.
Nothing is perfect and I'm sure patches will be required. (at least in the first years)

@edit: sorry, just read your correction on the subject:https://github.com/monero-project/meta/issues/321#issuecomment-476356693

@timolson 
>Recently an actual hardware designer (from Linzhi) showed up in the RandomX technical thread with some criticism of RandomX, so maybe we should listen to her not you.

Yes, she showed up to discourage the development by bringing invalid points, doubt she is that dumb to make such invalid claims. She is too smart to make such stupid claims.
Even as an amateur I can see failed logic of her claims.

## dEBRUYNE-1 | 2019-03-27T08:43:26+00:00
@tarris034:

Did you even read my previous comment where I clarified that? 

>Your initial comment was rather ambiguous with respect to what a patch meant. In light of this debate, it was logical to assume it meant another tweak to the RandomX to either curb ASICs or to further try to strengthen (emphasis on try) ASIC resistance. My previous comment was a response to that notion. If you want to properly discuss this, you should be more clear.

>**Code bugs should be patched, sure, but I don't think they are particularly relevant in this discussion.**

https://github.com/monero-project/meta/issues/321#issuecomment-476356693

## MoneroCrusher | 2019-03-27T10:43:25+00:00
Good takeaway from @WhyIsThisSoSlow's post:

> On the other hand, critical bugs may be discovered and need to be patched ASAP. Bugs can occur on any algo, no matter if its ASIC friendly or not.

I agree it's very important to very clearly distinguish between an obvious flaw/bug of the future PoW algorithm or if the very nature of the algo is flawed beyond redemption, rather than just saying the algo failed let's move on to ASICs, as people like @dEBRUYNE-1 like to suggest.

So what if the ASIC algo has a flaw too? What's next, PoS?

## hyc | 2019-03-27T10:43:29+00:00
@timolson True, I have never designed a mining ASIC before. But I've designed digital hardware, including the audio/DSP subsystem for Xybernaut wearable computers and a digital voicemail system for Atari and Mac. @stoffu has already said he has no hardware expertise, so that was not an ad hominem, it was a prompt to get up to speed at at least a basic level. The technical reasons why the approach we're taking will work are clear, and the article I linked gives a pretty good basic explanation as to why. The only point that isn't clear is by what degree, and we can only get the answer to that when actual ASICs are built.

linzhi's post identifies a bunch of factors in isolation, e.g. "ASICs can run at 3 GHz" but what matters is how all the components fit together as a system. A randomX ASIC is probably not going to get anywhere near 3 GHz after timing closure is settled; not if it aims to get any efficiency and cost advantages.

## WhyIsThisSoSlow | 2019-03-27T11:04:45+00:00
> I've never stated that I want to see RandomX fail. I stated that I have doubts about the proclaimed theoretical maximum efficiency advantage of 2x. My intention to have a solid back up plan (i.e. switching to an ASIC friendly algorithm) in place in case RandomX fails.

@dEBRUYNE-1 

The 2x estimate is just that, an estimate. What RandomX seeks to achieve is not to brick ASIC but to make them as inefficient as possible so that mining equality is reached till they become a commodity. Like i said before we as a community should be ok with updates made to the algo that provide improvements to that goal with a definite intention of NOT bricking the ASIC. These will in no way be as frequent as before and should be treated as any other update to the code. We can not consider the need of improvement a point of RandomX failure as this is what we are discussing here. The updates will be made to reduce the gap between other miners and ASIC advantage while technology evolves.

To make this clear and TLDR, i am opposed to tweaking just for bricking ASIC, but i want the RandomX code to evolve and keep the performance gap between ASIC and commodity hardware, as low as possible.This should not be treated as a failure of the algo.





## stoffu | 2019-03-27T11:06:59+00:00
What changed my view toward ASIC resistance is a realization that *demand drives innovation, not the other way around*. A good example is Bulletproofs; it was invented only because there was a strong demand for it (CT having been invented and deployed in several protocols). It wouldn’t have been invented if no one was using CT.

The market growth will certainly give rise to a strong demand for mining ASICs which will drive new technical innovations not foreseen today. I can see this nature without having any expertise in hardware, and it seems much more plausible than any of your wishful “probably” and “hopefully”.

## MoneroCrusher | 2019-03-27T11:09:28+00:00
> To make this clear and TLDR, i am opposed to **twerking** just for bricking ASIC

😃 
proof of twerk wen (sorry for the shitpost, couldn't resist)

## tarris034 | 2019-03-27T11:28:57+00:00
@WhyIsThisSoSlow 
> To make this clear and TLDR, i am opposed to tweaking just for bricking ASIC, but i want the RandomX code to evolve and keep the performance gap between ASIC and commodity hardware, as low as possible.This should not be treated as a failure of the algo.

Same with privacy development, it must evolve or it won't stay private for long in this race, network will always be a bit centralized in that context.

If privacy can evolve, why PoW shouldn't evolve ? ASIC-friendly PoW like SHA-3 does not guarantee 100% safety, as seen with SHA-1 (SHA-2 shares the same mathematical flaws as SHA-1):
https://www.computerworld.com/article/3173616/the-sha1-hash-function-is-now-completely-unsafe.html

It's all a matter of time till something gets cracked, that's why we should forget about dream of having one perfect PoW that won't require any maintenance.

The plus side of having x86 PoW is that any future change won't brick any hardware that was using previous version of PoW, AKA Backward compatibility.

And we know those changes are inevitable.

It will make defense against cracking much easier as the network will have proper hardware already for the next fork and not having problems like this:


*Why didn’t we move to SHA-3?
The number one reason why the world didn’t move to SHA-3 is because almost none of the world’s software or hardware supported it. Even if you wanted to move to SHA-3, you couldn’t have, unless you wrote your own code and firmware for every device you owned or used.*
Source:https://www.csoonline.com/article/3256088/why-arent-we-using-sha3.html

History will repeat and the same problem will occur when SHA-3 gets cracked, can't move to SHA-4 because there is no hardware for it for the next X months... we're practically on the mercy of ASIC manufacturers, hoping one of them won't go rogue (or some other *investor*) and take over the whole network before other company releases new hardware.

Monero needs to stay crypto-agile

## hyc | 2019-03-27T17:43:44+00:00
@stoffu the technical basis for the RandomX approach has been spelled out. Can you provide technical reasons for why any of
* the overall goal of forcing ASICs to operate on CPU playing field
* the overall approach of using randomly generated code to rule out fixed function hardware
* the overall design of RandomX to use this approach to achieve this goal
* the overall implementation of RandomX that embodies the design

are incorrect? If not then you're merely spouting fear borne of ignorance. That combination never yields positive accomplishments.

## stoffu | 2019-03-28T01:01:02+00:00
@hyc 
> Can you provide technical reasons

Of course I cannot disprove your arguments _based on today's technology_. My point is that the strong demand for efficient ASICs will lead to technological breakthroughs in semiconductor and render RandomX obsolete and necessitate RandomX 2.0 and 3.0 and forever.

The fact that the non-technical Monero community is led by your leadership makes me think that Monero is practically dead already. I don't think I can save you from your psychological lockup, so just go on with your sweet dream of ASIC resistance. I'll just focus on Aeon.

Farewell Monero, rest in peace.

## ghost | 2019-03-28T03:41:13+00:00
@stoffu 

> makes me think that Monero is practically dead already

And you will now focus on aeon?  That coin has been dead for 2 years bruh.  Where you been?  The community hates the fact that their voice is never a concern.  Why do you think turtlecoin is more popular than aeon now?

## dEBRUYNE-1 | 2019-03-28T06:59:49+00:00
@stoffu:

If you read the logs of the PoW meeting, you'd see that @hyc is in favor of a path where Monero switches to an ASIC friendly algorithm in case of a failure of the first iteration of RandomX (thus, no more tweaks to the RandomX algorithm). Your comment assumes hyc wants to tweak RandomX indefinitely, which is erroneous. 

## hyc | 2019-03-28T07:06:37+00:00
@stoffu 
> Of course I cannot disprove your arguments based on today's technology. My point is that the strong demand for efficient ASICs will lead to technological breakthroughs in semiconductor and render RandomX obsolete

Ah right, because transistors will magically improve for ASICs only, and CPUs won't be able to avail of those improvements too.

Your argument is pure nonsense.

## stoffu | 2019-03-28T07:10:56+00:00
@dEBRUYNE-1 
> Your comment assumes hyc wants to tweak RandomX indefinitely, which is erroneous.

My only assumption/understanding is that @hyc never agrees to bind ourselves with our own precommitment and wants to leave the possibility of 'improving' (aka tweaking) RandomX when there seems like a hope. Isn't this the precise thing you wanted to get rid of with precommitment? That's why I believe the plan won't work. Either go with RandomX (and its further updates), or abandon ASIC resistance now. I don't see any middle ground.


## hyc | 2019-03-28T07:15:24+00:00
@stoffu You seem to be overlooking the part where I explicitly stated that because RandomX necessitates a fully programmable device, small tweaks like we used on CN will be ineffective and pointless. I have no interest in perpetual tweaking and I have been opposed to perpetual tweaking from day 1. The point to developing a long-term PoW was to get away from tweaks.

And yes, I object to precommiting to change something before we see how well it works. I also object to precommiting to an algorithm like SHA3 today when the landscape may change in 2 years and that chosen algorithm may be proven to be a poor choice in that intervening time.

## stoffu | 2019-03-28T07:27:04+00:00
@hyc 
> You seem to be overlooking the part where I explicitly stated that because RandomX necessitates a fully programmable device, small tweaks like we used on CN will be ineffective and pointless. I have no interest in perpetual tweaking and I have been opposed to perpetual tweaking from day 1. The point to developing a long-term PoW was to get away from tweaks.

Sorry for making you confused by my generalized use of the word 'tweak' which includes more substantial design changes such as incorporating the 'IO-hard' aspect as suggested by @Sonia-Chen. I consider *any* kind of 'improvements' for RandomX as a tweak in a general sense.

> And yes, I object to precommiting to change something before we see how well it works. I also object to precommiting to an algorithm like SHA3 today when the landscape may change in 2 years and that chosen algorithm may be proven to be a poor choice in that intervening time.

Exactly, this is why Monero is doomed.

## hyc | 2019-03-28T07:29:34+00:00
Sonia's suggestion of IO-hard was nonsense and already discarded. She herself has already backed away from it. Try again.

## stoffu | 2019-03-28T07:30:56+00:00
It's just an example. Also you never know it's nonsense or not many years into the future.

## hyc | 2019-03-28T07:33:51+00:00
Yes, we do know. IO-hard requires an external IO device to talk to. Which then devolves into something stupid like "Proof of Storage" or whatever, which can never actually be proven.

## dEBRUYNE-1 | 2019-03-28T07:36:00+00:00
>Exactly, this is why Monero is doomed.

I think you're still misunderstanding hyc. He's opposed to:

- Precommitting to a switch to an ASIC friendly algorithm on a set date.
- Precommitting to a switch to a *specific* ASIC friendly algorithm if RandomX fails.

Hyc is in favor of:

- Precommitting to a switch to an ASIC friendly algorithm if RandomX fails. 

## stoffu | 2019-03-28T07:40:18+00:00
@dEBRUYNE-1 
> Precommitting to a switch to an ASIC friendly algorithm after RandomX fails.

As I understand it, the above is to be corrected as follows:

- Precommitting to a switch to an ASIC friendly algorithm after RandomX fails _and there is absolutely no hope of fixing RandomX_.

If I'm correct here (please confirm), Monero is still doomed because one can always find false hopes.


## tarris034 | 2019-03-28T08:35:00+00:00
@stoffu from the history of your messages I can see you're here only to give bad advice's with no proofs or facts and to advertise aeon shitcoin.

You are doomed in this discussion for not being neutral.

## stoffu | 2019-03-28T10:25:52+00:00
Put differently, Monero is doomed if @hyc refuses to agree with the following precommitment:

- RandomX will stay the same forever until it's broken by ASICs and we switch to whichever ASIC friendly PoW.


## dEBRUYNE-1 | 2019-03-28T10:28:35+00:00
@stoffu:

He basically said that in his previous comment:

>You seem to be overlooking the part where I explicitly stated that because RandomX necessitates a fully programmable device, small tweaks like we used on CN will be ineffective and pointless. I have no interest in perpetual tweaking and I have been opposed to perpetual tweaking from day 1. The point to developing a long-term PoW was to get away from tweaks.

[Also:](https://www.reddit.com/r/Monero/comments/b5fe5j/psa_seeking_volunteer_reviewers_for_pow_randomx/ejd4u8g)

>Frequent forks are untenable, especially as the ecosystem grows.



## SChernykh | 2019-03-28T10:28:41+00:00
@stoffu I don't understand what you're trying to do, you don't add any value to the discussion. Either provide some meaningful arguments or get out already. How many times have you said "farewell", 3 or 4? I lost count.

## stoffu | 2019-03-28T10:30:13+00:00
@dEBRUYNE-1 
Please see my above comment https://github.com/monero-project/meta/issues/321#issuecomment-477480286

> Sorry for making you confused by my generalized use of the word 'tweak' which includes more substantial design changes such as incorporating the 'IO-hard' aspect as suggested by @Sonia-Chen. I consider any kind of 'improvements' for RandomX as a tweak in a general sense.


## MoneroCrusher | 2019-03-28T13:58:16+00:00
@johnny1021
> An ASIC designer's suggestion:
> 
> 11:
> 
> Moner community make following precommitment : Once ASIC miner were found on the net, community will do a hard fork immediately, new hard fork algorithm was already prepared. The new POW algorithm might be a change of Cryptonight or RandomX or Dual POW, but it is uncertain until the last minute.
> 
> This commitment will be like a sword of Damocles hanging over ASIC machine designer's head. In this way, no one will dare to design XMR ASIC chips anymore, because there's on way for ASIC miner to get back their investment in a few weeks.
> 
> In this way, cat & mouse game can be avoided and community can focus on the protocol.

So now 2 ASIC designers already agree with me that the only way to keep ASICs away indefinitely is with perpetual forks. Once per year should be enough with a reasonably hard algorithm like **for example** ethash and this could perfectly blend with the yearly fork we are planning to transition to.

Additional suggestion: Instead of switching to SHA-3 algo in case the future PoW algorithm fails and ASIC makers are still as shitty as they are today:
just switch to "Ethash-Monero" and stay on it forever. It would provide co-existence of ASICs, FPGAs and GPUs as we see on Ethereum today. Ethash exists since 5 years and hasn't seen a sigificantly more efficient ASIC in comparison to other algos.

**Let's switch this whole discussion around**
Imagine Monero were to fork/split into the following variants in October:
Monero-ASIC
Monero-CPU
Monero-GPU
Monero-CPU/GPU

IMO Monero-ASIC would instantly become a shitcoin and the others would depend on whether they have most developer support. IMO an algorithm that has both CPUs & GPUs will have the biggest community support.

So the most harmonious way forward is to select the path where most people's interests & beliefs are aligned in order to avoid a contentious HF.

@fluffypony I'm still trying to grasp the change of heart in your sudden(?) ASIC friendliness. In case Jihan is sending by Chinese mobsters please let us know.

## hyc | 2019-03-28T14:00:33+00:00
@MoneroCrusher sure dude, we've got an infinite supply of secure and unique algorithms to switch to in our pockets. We're just too lazy to deploy them.

Flat no.

## MoneroCrusher | 2019-03-28T14:02:56+00:00
@hyc In **the example** of ethash you could add unpredictable amounts of core computations (à la ProgPoW style) and change them on a random basis each year. This won't stop ASICs but it would require them to be considerably more flexible & therefore more expensive. I don't know in what capacity this would be possible in RandomX or CN-R-GPU.

A possible approach:
for the next 4 years introduce a stepper-like function that increases core computations/iteration count every quarter by 6.25% until after 4 years 100% core computation/full specification is reached, naturally this will lead ASIC manufacturers to rather produce end-specification ASICs. Then after 4 years go away from stepper function to a random function that assigns random amounts of core iterations every quarter. This would mean that ASICs would get overengineered and then can't use their full potential. Naturally this would ofc also lead to more modular ASICs, which in turn likely would also add cost.
This could all be easily achieved without a HF.

I mean the goal is to reduce commodity HW/ASIC gap, there are many possible ways to achieve this and I especially like economical approaches.

Just bringing in possible ideas. I don't like your hostile-ish approach tbh.

## fluffypony | 2019-03-28T14:51:20+00:00
@MoneroCrusher there is no change of heart, I've been consistent from before the first PoW tweak to now.

https://twitter.com/fluffypony/status/975326973840019458

https://twitter.com/fluffypony/status/975342955811823616

https://twitter.com/fluffypony/status/976532977051226112

https://twitter.com/fluffypony/status/1026758221602742272

https://twitter.com/fluffypony/status/1036923704121417729

https://twitter.com/fluffypony/status/1086261753892229121

https://twitter.com/fluffypony/status/1093949707754315779

## MoneroCrusher | 2019-03-28T14:53:49+00:00
I know that, but you said switching to SHA-3 ASICs only makes sense until they are commoditized and you can buy them everywhere. This will likely not be the case in October 2019, nor in October 2021.
IMO switching to ASICs only makes sense once we see large scale adoption of cryptocurrency as a whole, as then people are more aware and more likely to get a device _just_ for that.

## fluffypony | 2019-03-28T14:56:06+00:00
@MoneroCrusher I realised that nobody was going to work on SHA3 ASICs without a financial incentive to do so; waiting for them to be commoditised is putting the cart before the horse.

## MoneroCrusher | 2019-03-28T15:09:19+00:00
@fluffypony So after Bitcoin existing for 10 years there's still not a single SHA-256 ASIC by a reputable producer, despite a $100B+ market cap. What makes you believe it'll be any different for SHA-3 ASICs?
And there's also the legal/KYC/import problem with ASICs that you will never have with commodity hardware.

Let's say many governments, maybe even the EU or the US deem Monero illegal tender and it's mined by SHA-3 ASICs. What makes you believe they wouldn't ban the import of devices that enable Monero to have a functioning network?
Nobody can forbid commodity HW.

Once there's widespread adoption & acceptance of cryptocurrency the situation might look different.

## fluffypony | 2019-03-28T15:13:24+00:00
@MoneroCrusher there are several high profile, reliable manufacturers, including GMO (Japan), Halong (China), Obelisk (USA), and BitFury (UK). If the US *and* the EU ban Monero ASICs it won't make a single bit of difference, Monero can still be mined in several hundred other countries.

Besides, it would literally be the most pointless against Monero - if they want to get rid of it why would regulators not just ban it outright? Make it illegal to use, hold, mine, or run a node. Then it wouldn't matter WHAT PoW algorithm Monero is using.

## hyc | 2019-03-28T15:17:35+00:00
* Obelisk is not reliable. https://www.grin-forum.org/t/obelisk-grn1-chip-details/4571/36

## MoneroCrusher | 2019-03-28T15:18:20+00:00
You mean the same BitFury as in 2013 that scammed customers left and right?
Order in March
Supposed to receive in April
Actually receive brick in October

By reputable manufacturer I mean a manufacturer that is only in business for selling hardware, and not using their customers mainly as a risk buffer for their mining operations.

I won't buy any fixed-function ASICs unless I can buy them from: Samsung, Intel, AMD, Nvidia, ARM, Qualcomm, IBM and some others.
With 3 years (extendable up to 10 years) warranty, actual real customer & warranty service and 30 days return policies as a consumer.

## fluffypony | 2019-03-28T15:25:44+00:00
Thank goodness we're focusing on reliable companies that never have delays!

https://www.theinquirer.net/inquirer/news/3070793/amd-7nm-navi-delayed

https://www.theinquirer.net/inquirer/news/3036660/intel-10nm-cannon-lake-processors-delayed-again-until-late-2019

https://www.techpowerup.com/247962/nvidia-rtx-2080-ti-delivery-delayed-again-to-be-sent-october-5th-9th

https://www.techpowerup.com/247055/nvidias-bfgd-solutions-delayed-to-q1-2019-will-cost-an-awful-penny

https://www.computerworld.com/article/2573484/intel-to-ring-in-2004-with-delayed-prescott-launch.html

https://fudzilla.com/news/graphics/43781-vega-gpu-coming-at-siggraph

## hyc | 2019-03-28T15:31:26+00:00
Delays are part of life. Taking money in pre-orders, promising they're refundable, and reneging on refunds shouldn't be. ASIC builders have a long long way to go before anyone can consider them reputable.

## MoneroCrusher | 2019-03-28T15:31:28+00:00
The difference is:
Their delays cost them money (AMD, Intel, Nvidia etc) because they're in business to sell as much hardware as possible.
ASIC manufacturers are mainly miners, they delay on purpose in order to self-mine some more. They don't lose, they win by delaying as long as possible, then selling quasi-bricks to customers. Just to announce a "new" miner 2 months later.
Reference: see every single altcoin ASIC _ever_

There's a fundamental flaw in the ASIC manufacturer/customer relationship as it stands today, and it can very easily be expressed in one graph:
![image](https://user-images.githubusercontent.com/32360383/55170944-c33ca380-5177-11e9-825a-a83ad6f66f00.png)


## tarris034 | 2019-03-28T15:35:58+00:00
Lets all agree here that ASIC manufacturers got **very** bad reputation, [including 51% attacks on known coins](https://bravenewcoin.com/insights/etc-51-attack-what-happened-and-how-it-was-stopped), and all of the above problems mentioned by others.



## fluffypony | 2019-03-28T15:46:50+00:00
Regardless, ASICs are the lesser of two evils in the scenario where RandomX fails. Tweaking is not an option, and will do more damage and put Monero's contributors at more risk than any bad ASIC manufacturer ever could. I have no problem with RandomX being the next step, but the step thereafter simply cannot be yet-another-supposedly-ASIC-resistant-algorithm, or tweaks every 3 months.

## tarris034 | 2019-03-28T15:49:23+00:00
@fluffypony 
>If the US and the EU ban Monero ASICs it won't make a single bit of difference

You can't ban something that is decentralized, you can have nodes over VPN and mine over encrypted connection no problem.

## fluffypony | 2019-03-28T15:50:48+00:00
@tarris034 that link doesn't demonstrate an ASIC manufacturer 51% attacked a coin. The only relevant thing is a *claim* by ETC developers that an ASIC manufacturer was testing ethash machines.

Regarding your second comment, I fail to see how that is at all relevant. Miners do not need to be in the country you're in for Monero to work.

## tarris034 | 2019-03-28T15:57:16+00:00
@fluffypony 
Monero and many other coins was in the beginning all about being free of regulations, government and other control, we shouldn't be afraid of any bans, the network will work regardless as it's not centralized.

Situation complicates when the government can ban the production of required hardware for the network, and that can't happen with Intel/AMD/IBM as it's not job specific. 

## fluffypony | 2019-03-28T16:04:32+00:00
@tarris034 I don't think you understand. If Monero is banned in a country then it will be relegated to a handful of individuals who are essentially operating criminally. If a large number of countries ban Monero then it is as good as dead - people do NOT want sound, private money enough to overcome such regulation. The PoW choice has NOTHING to do with this scenario - it neither helps nor hinders it. And, frankly, there simply does not exist a scenario where a large country bans Monero ASICs but doesn't ban Monero's use.

## MoneroCrusher | 2019-03-28T16:08:00+00:00
It's easier to ban imports & hardware and introduce KYC to ASIC miners.
It's virtually impossible to stop Monero mining from a software/internet traffic perspective.

## tarris034 | 2019-03-28T16:13:09+00:00
@fluffypony I agree with the first part what you said about Monero being too hot to use by normal people but I will disagree with the statement that PoW has nothing to do with it, I think due to the hardware assimilation we are being in more danger of getting banned worldwide (due to the lack of mining hardware) just because one or two governments decided it's illegal to produce mining equipment for it.  

## fluffypony | 2019-03-28T16:17:44+00:00
> It's easier to ban imports & hardware and introduce KYC to ASIC miners.
> It's virtually impossible to stop Monero mining from a software/internet traffic perspective.

That's not how regulation works. You don't need to take action against everyone, you just need to pick 3 people at random and throw them in jail for 10 years and everyone else will be too afraid to use it.

## tarris034 | 2019-03-28T16:18:46+00:00
> > It's easier to ban imports & hardware and introduce KYC to ASIC miners.
> > It's virtually impossible to stop Monero mining from a software/internet traffic perspective.
> 
> That's not how regulation works. You don't need to take action against everyone, you just need to pick 3 people at random and throw them in jail for 10 years and everyone else will be too afraid to use it.

Yet P2P piracy still exists, stronger than ever. No ones afraid of downloading or uploading movies/music/games.

## fluffypony | 2019-03-28T16:25:51+00:00
> @fluffypony I agree with the first part what you said about Monero being too hot to use by normal people but I will disagree with the statement that PoW has nothing to do with it, I think due to the hardware assimilation we are being in more danger of getting banned worldwide (due to the lack of mining hardware) just because one or two governments decided it's illegal to produce mining equipment for it.

@tarris034 again - there is never going to be a scenario where creating Monero via mining is banned, but using it is not. There's no legal precedent for something like that. If Monero is viewed as problematic it will be because of fear of abuse by users, not fear of miners.

The scenario you're suggesting is the equivalent of a government saying that it's totally fine for citizens to snort copious amounts of cocaine, but nobody in the country is allowed to manufacture cocaine, nor can anyone import cocaine. But if you happen to have some then sure, go wild.

> Yet P2P piracy still exists, stronger than ever. No ones afraid of downloading or uploading movies/music/games.

Actually P2P piracy has taken a MAJOR beating, in part because of Netflix / Spotify etc., and in part because of enforcement. Here's a good article on it: https://www.plagiarismtoday.com/2017/06/01/the-long-slow-decline-of-bittorrent/

## MoneroCrusher | 2019-03-28T16:27:54+00:00
Then why even invest energy in Kovri/Sekreta if you say it's a lost cause anyway, in case it gets banned?

## fluffypony | 2019-03-28T16:29:21+00:00
> Then why even invest energy in Kovri/Sekreta if you say it's a lost cause anyway, in case it gets banned?

It has nothing to do with being banned, not sure how you imagined that?? It has to do with the risk of passive analysis being used to weaken Monero's privacy enhancing systems. Defending against that is one of the 5 pillars of financial privacy.

## MoneroCrusher | 2019-03-28T16:31:24+00:00
Of course, but it being able to hide the fact that you're using Monero at all can also be used for the fact you're mining Monero at all, shall it become forbidden to mine, which is simply impossible to enforce.
Banning imports of fixed-function hardware and enforcing wrongdoers is very easily done though.
Not imaginable, nor enforcable on commodity hardware like CPUs & GPUs.

Nothing against fixed function hardware directly, but there needs to be groundwork done for that: adoption of ASIC production by the big guys and widespread adoption and acceptance of CC as whole.

## tarris034 | 2019-03-28T16:33:42+00:00
@fluffypony  > Actually P2P piracy has taken a MAJOR beating, in part because of Netflix / Spotify etc., and in part because of enforcement. Here's a good article on it

Yes P2P took a hit from Netflix but the new wave of streaming sites is taking it over again.

The scenario may seem unrealistic for the moment but there's always a chance of it happening, I'm not saying whole world will ban production ASIC for Monero, and surely it would spawn new ASIC companies in USA or other parts of the world.

But we are greatly dependent of those companies nevertheless, and those are not big companies like Intel/etc, they may decide other coin has more demand for hardware or any other aspect of investment will take a role.

## fluffypony | 2019-03-28T16:34:54+00:00
> Of course, but it being able to hide the fact that you're using Monero at all can also be used for the fact you're mining Monero at all, shall it become forbidden to mine, which is simply impossible to enforce.
> Banning imports of fixed-function hardware and enforcing wrongdoers is very easily done though.
> Not imaginable, nor enforcable on commodity hardware like CPUs & GPUs.

Not true. The design is such that transactions flow over hidden services, and blocks flow over IPv4, to prevent isolation / partitioning attacks. It will be trivial to determine that you're using Monero even when you're using this additional privacy enhancement.

## MoneroCrusher | 2019-03-28T16:37:03+00:00
@fluffypony hypothetical scenario:
we switch to SHA-3 ASICs and 1 year later the US and EU consider Monero a criminal currency and ban all imports on SHA-3 ASICs.
What next? Just let it sit & outsource mining to the Cayman Islands?

This would never even be a possibility on commodity hardware.

## fluffypony | 2019-03-28T16:37:38+00:00
@tarris034 Supporting "big companies" seems an even worse value proposition, if you're concerned about regulatory risk. Large multinationals like Intel and AMD are far, far more likely to put a backdoor in their hardware to remain in regulator's good books. They are global, and their business would be devastated if regulators came after them, which means that regulators have them by the proverbial balls. There is a rising suspicion that Intel and AMD have such a backdoor in their Management Engine already.

## tarris034 | 2019-03-28T16:38:32+00:00
@fluffypony lets put this subject into our conspiracy collection.

## fluffypony | 2019-03-28T16:40:29+00:00
> @fluffypony hypothetical scenario:
> we switch to SHA-3 ASICs and 1 year later the US and EU consider Monero a criminal currency and ban all imports on SHA-3 ASICs.
> What next? Just let it sit & outsource mining to the Cayman Islands?

You realise there are other parts of the world besides the US and the EU? In fact, most mining farms are located in other parts of the world, including the Baltic states and Asia. I think it's totally fine for mining to continue in those many countries if the US and the EU bans it.

## MoneroCrusher | 2019-03-28T16:43:57+00:00
@fluffypony if US & EU ban anything it's a nice precedent for every other country to follow suit with some exceptions.
I know it's ~~improbable~~ I changed my mind, I think sooner or later we might see a concentrated crackdown on private cryptocurrencies as a whole.

That's one of the many merits of commoditized hardware (avoiding regulatory problems).

## tarris034 | 2019-03-28T17:10:26+00:00
Lets get this straight, specialized ASIC hardware has no pros, we are discussing it only because we are forced by ASIC manufacturers.

Otherwise we would still use old PoW.

## MoneroCrusher | 2019-03-28T17:13:48+00:00
IMO it actually has pros:
1. Faster verification times
2. Better protection against state actors and big corps with huge CPU & GPU farms, but only if said ASIC is commoditized, otherwise this effect becomes the opposite.

## tarris034 | 2019-03-28T17:14:29+00:00
@MoneroCrusher isn't Diff in charge of how fast we are working ? ~2min block times, regardless of network hashrate.

Your second statement is as well wrong, show me farm/supercomputer/company that is capable of 150 MH/s mining or even half of this.
It's far from reality to come with that huge hashrate on commodity hardware to make a successful 51% attack.

Summit, fastest supercomputer in the world currently got *only* 9,216 POWER9 22-core CPUs

One of this CPUs is about the AMD EPYC 7401P 24-CORE performance, something around ~1800 H/s on CN/R according to some monero benchmarks.

That's *only* ~16.5 MH/s (could be little faster but for sure not capable of 51% attack, not even close)

It also got GPU's, 1789,75 H/s per one  Nvidia Tesla V100 x 27,648 = 49,5 MH/s on CN/r
Too small, and RandomX will kill the GPU part in significant part.


## hyc | 2019-03-28T17:16:00+00:00
Commoditization isn't even enough. Even if ASICs were available in every electronics shop in the world tomorrow, only a small minority of people would know what they are or be interested in buying them. Market penetration matters, and ASICs will never compete with CPUs on that score.

## MoneroCrusher | 2019-03-28T17:46:00+00:00
@tarris034 
1. Point: I'm not talking about block time, I'm talking about the time it takes to verify a block by a CPU.
2. Point: I said ASIC would provide better security against state actors and big corps because they wouldn't own any hardware and the rest of the network is absolutely not incentivized to attack it's own network, especially if the ASIC is commoditized and widespread. **If** the last 2 points are not given, then yes we are much better off with GPUs and CPUs.

## tarris034 | 2019-03-28T17:47:46+00:00
@MoneroCrusher 1. I'm still correct, diff is in charge how long it will take to find you a block.

>the rest of the network is absolutely not incentivized to attack it's own network

So you believe that there are only good people in the world with no bad intentions.
If someone bad could financially do 51% attack, he would do it. ROI is great on 51 street.

## MoneroCrusher | 2019-03-28T17:50:17+00:00
Let me put it another way:
Do you think the speed of synchronization of the Monero blockchain on your computer has anything to do with block time? I'm talking about syncing speed, but I'm not even entirely sure about that since CPUs don't natively support SHA-3, so I'll let an expert answer that one for me.

## WhyIsThisSoSlow | 2019-03-28T17:50:17+00:00
> Commoditization isn't even enough. Even if ASICs were available in every electronics shop in the world tomorrow, only a small minority of people would know what they are or be interested in buying them. Market penetration matters, and ASICs will never compete with CPUs on that score.

This is why i truly do not understand why we still consider ASIC as a valid change option for RandomX in the near future.

It has no chance of working out. Just wishing it will work out before Monero dies, defies all logic in my book.

## fluffypony | 2019-03-28T17:50:18+00:00
> Commoditization isn't even enough. Even if ASICs were available in every electronics shop in the world tomorrow, only a small minority of people would know what they are or be interested in buying them. Market penetration matters, and ASICs will never compete with CPUs on that score.

Literally makes no difference. The small minority who would buy ASICs are ~the same small minority who will mine on their commodity hardware. Both small minorities are going to also be a small minority of the Monero hashrate, which will always be dominated by large, professional mining farms. If RandomX fails, then why would we try to find a solution for 10% of the hashrate when we’d just be overcomplicating the at-scale efforts of the 90%??

## tarris034 | 2019-03-28T17:56:22+00:00
How it worked out for Bitcoin ? not so good.... 
https://bitcoinmagazine.com/articles/report-links-74-bitcoin-mining-china-sees-threat-network/

Only big players move out to cheap energy zones and to bypass import tax, that's why we see centralization of hashrate for bitcoin.

Government can take their hardware and never give it back, they are known for worst things than that. (taking and crashing homes because they wanted to build something there and so on)
Of course they are smarter than that and rather control Bitcoin than just stop the mining.

*There was a documentary about it somewhere*
Can't find it but here are some facts about China government:
https://bitterwinter.org/government-destroys-the-homes-of-900-villagers-videos/

They do what they want. I think we agree we don't want majority of the hashrate being in China like our Bitcoin grandma has today.

## iamsmooth | 2019-03-28T20:47:57+00:00
@MoneroCrusher 
> CPUs don't natively support SHA-3 

Recent ARM has special instructions for more efficient SHA-3. However even without special instructions SHA-3 is quite efficient on any CPU, certainly compared to something like CN or RandomX.

## iamsmooth | 2019-03-28T20:59:12+00:00
@fluffypony 
> I think it's totally fine for mining to continue in those many countries if the US and the EU bans it.

Not ideal from any perspective though. At a minimum it means that mining will be more geographically concentrated, which is moving in a negative direction, and probably more organizationally concentrated too. It is a potential negative, even if not immediately fatal.

@tarris034 
> Lets get this straight, specialized ASIC hardware has no pros

That's not true. In addition to the factors already discussed such as faster verification (at least compared to CN or RX) and less of a global inventory of non-mining gear which can be brought to bear by an attacker, ASICs may contribute to another dimension of security since it more tightly aligns the value of the equipment with the health of the network. (Attacking the network in a highly-damaging way means the owner of the equipment is more likely to suffer a loss in rapid deprecation.)

@hyc 
> Commoditization isn't even enough. Even if ASICs were available in every electronics shop in the world tomorrow, only a small minority of people would know what they are or be interested in buying them. 

This seems to be moving the goal line a fair bit. Sure, the ideal from the perspective of broad participation is probably to be able to download a program and start mining without any additional equipment but realistically the biggest harm from ASICs comes from the control over the supply and supply chain. Anyone being able to buy GPUs and build a mining rig is far less problematic from a  concentration and control perspective than monopolized ASICs, even if it doesn't quite reach the download-and-go ideal, and anyone being able to buy ASICs from an electronics shop would be essentially the same as that.

@fluffypony 
> The design is such that transactions flow over hidden services, and blocks flow over IPv4, to prevent isolation / partitioning attacks

Okay but people who are motivated can still run blocks over a hidden network if they really need to, perhaps employ other measures to mitigate the risk of isolation such as trusting known block explorers/APIs or something.

## tarris034 | 2019-03-28T21:07:24+00:00
> @iamsmooth (Attacking the network in a highly-damaging way means the owner of the equipment is more likely to suffer a loss in rapid deprecation.)

How about the fact that this ASIC mining hardware gets bricked sometimes couple times a year because of new more efficient one coming in ? talking about losses...

> and less of a global inventory of non-mining gear which can be brought to bear by an attacker

That's unrealistic scenario as I described earlier. Unless you're talking about another attack from ASIC manufacturers and failure of RandomX.

>ASICs may contribute to another dimension of security

It does absolutely nothing to the security, you could add increased possibility of heading down the Bitcoin road of being controlled by China.

>faster verification (at least compared to CN or RX)

It doesn't matter, what matters is the decentralization. Diff will adjust according to the environment.

## iamsmooth | 2019-03-28T21:20:27+00:00
@tarris034
> How about the fact that this ASIC mining hardware gets bricked sometimes couple times a year because of new more efficient one coming in ? talking about losses...

That's a function of immaturity, not the technology itself. There is no sustained reason for ASICs to get obsolete any faster than CPUs or GPUs. 

The longer you wait to start the necessary maturation process the longer it will take to get there.

> [global inventory of non-mining gear] That's unrealistic scenario as I described earlier. 

I don't agree. You described a specific (single) supercomputer. I agree on that point as I have stated earlier. That's very different from the global inventory of CPUs and GPUs that exist and can be brought to bear. 

> It does absolutely nothing to the security

You either didn't read what I wrote or didn't understand it. Note: I did not say that it improves security _in every way_, only that it doesn't have "no pros". That's simply wrong.

> [faster verification] doesn't matter

It does indeed matter. Slower verifying of blocks increases instability of the network, necessitates a slower block time all else being equal, increases orphan (wasted hash) rate, increases sync time, increases power usage on mobile nodes or wallets (if the wallet wants to actually verify PoW and not blindly trust a remote node), and increases DoS vulnerability of both nodes and pools.

I suggest that you stop confusing "I don't think this is important (enough)" with "This doesn't matter".



## tarris034 | 2019-03-28T21:32:10+00:00
> @iamsmooth That's a function of immaturity, not the technology itself. There is no sustained reason for ASICs to get obsolete any faster than CPUs or GPUs.

We can't base our decision on speculations, I'm talking how it looks today.

>I don't agree. You described a specific (single) supercomputer. I agree on that point as I have stated earlier. That's very different from the global inventory of CPUs and GPUs that exist and can be brought to bear.

Unrealistic is the word here.

>You either didn't read what I wrote or didn't understand it. Note: I did not say that it improves security in **every way**, only that it doesn't have "no pros". That's simply wrong.

I just said it does not improve it in *any* way.

>It does indeed matter. 

Yes it does matter but the network overall speed has no impact on it due to difficulty adjustment.

>Recent ARM has special instructions for more efficient SHA-3. However even without special instructions SHA-3 is quite efficient on any CPU, certainly compared to something like CN or RandomX.

Efficiency gains on purpose built ASIC will destroy any slightest profitability on any general purpose CPU even with hardware instructions in place due to additional decoding steps and so on.
In short - No one will even try to use commodity hardware to mine using SHA-3 (or any other ASIC-friendly algorithm for that matter).

## iamsmooth | 2019-03-28T22:45:27+00:00
> I'm talking how it looks today

Yes and even today the mining ASIC industry has moved beyond miners being obsolete after a few months in general (it may happen if the coin price crashes, but that's not the technology's fault, and applies equally to CPUs/GPUs). 

Today there are still miners which are profitable at 13c/kwh despite being two years old. For example: https://www.asicminervalue.com/miners/baikal/miner-cube

Or even the workhorse original Bitmain S9 which is almost _three_ years old and is still profitable with 6c/kwh electricity (cheap, but exists some places even at residential rates).

> difficulty adjustment

Difficulty adjustment has nothing to do with verification, apart from the one aspect of wasted hashes due to orphans, but that is a small element of it. You're not understanding the issue.

> Efficiency gains on purpose built ASIC will destroy any slightest profitability on any general purpose CPU 

Again, you are not understanding. The issue here is verification, not mining.


## stoffu | 2019-03-29T00:24:44+00:00
@hyc 
> Commoditization isn't even enough. Even if ASICs were available in every electronics shop in the world tomorrow, only a small minority of people would know what they are or be interested in buying them. Market penetration matters, and ASICs will never compete with CPUs on that score.

Commoditization happens _only because everyone wants the product_. Your biggest weakness is your poor understanding of economics.

## hyc | 2019-03-29T00:51:42+00:00
@stoffu You realize of course you're only weakening your own argument. People keep assuming that with multiple ASIC manufacturers, these chips will be commoditized. Clearly that won't happen in 2 years. Probably not even in 20 years.

## iamsmooth | 2019-03-29T01:33:02+00:00
@hyc I don't know why you think it is clear there won't be multiple ASIC manufacturers in two years. There were multiple manufacturers of Cryponight ASICs (likely harder, especially considering there are already open source SHA-3 hardware designs) and that happened in less than two years. I'm assuming here that no one cared to even try until the price took off, which is likely correct.

Clearly it won't happen if prices are low, but apart from that any predictions seem like little more than guesswork at best.

## hyc | 2019-03-29T01:40:48+00:00
@iamsmooth That is not what I said. There are multiple ASIC manufacturers today, but commoditization still has not happened. Nor is it likely to happen in 2 years.

## stoffu | 2019-03-29T01:48:35+00:00
Commoditization having happened (i.e. every electronic store in town selling it) means that the said cryptocurrency has already achieved its mission of global adoption; everyone understands what that cryptocurrency is and what mining means.

ASIC commoditization is not a precondition for switching to ASIC friendliness, it's an ultimate ideal state that we aim for.


## iamsmooth | 2019-03-29T03:19:06+00:00
Well I don't really agree that every store in town needing to sell it is necessary for a useful degree of "commoditization" though clearly if every store did sell them, that would qualify. There is a wide range of market conditions that would broadly qualify as having minimal harmful monopolization and considering that none of these solutions are perfect or easy, the degree matters a great deal. 

I would also agree with what @fluffypony stated earlier. The only way that conditions progress toward a better degree of commoditization (as they have in Bitcoinland, and yes while it is certainly not perfect, it is far better than it was in years past and continuing to get even better) is if there is a first a clear market for people to enter, compete, and become more commoditized over time. As long as ASIC-resistance is pursued, that market and process is smothered in the cradle. 

What Grin is doing makes a lot more sense long term than what is going on here.


## tarris034 | 2019-03-29T07:44:19+00:00
@iamsmooth 
> 
> Again, you are not understanding. The issue here is verification, not mining.

ok misunderstood you, so how it will impact the network ? post some numbers and how it will affect the pools / nodes hardware requirement.

Rented dedicated servers are cheap, got one that could handle the job with easy today and it's the cheapest one.
So in that respect I don't see any problem today and no gains from ASIC in this subject.

And don't come at me with DDoS as this kind of attack will stop any pool / node regardless of PoW used.

BTW, we have gone way too far from what we considered "commodization", it was about everyone having required hardware **already** in home because of other uses, specific ASIC hardware will never be a common hardware, that's just a dream.

Is Bitcoin ASIC miner a commodity ? no.
Is it profitable to mine Bitcoin using ASIC outside of China or some third world country with cheap energy ? no.
Is it centralized ? yes.

If you really insist you can find pros in everything but lets just look at Bitcoin and think about it, do we really want Monero going the same path ?

Anyway, I think @stoffu & @iamsmooth are both advocating for ASIC-friendly PoW on monero thread just because they want some major coin to start the movement so their aeon coin can utilize it.
Right now your community is even considering taking RandomX from what I see in other threads on the web but you both are trying to convince on SHA-3 path.

You are not neutral in this discussion.

## hyc | 2019-03-29T08:05:43+00:00
@stoffu 
> ASIC commoditization is not a precondition for switching to ASIC friendliness, it's an ultimate ideal state that we aim for.

You keep digging a deeper and deeper hole. By calling this an ultimate ideal you've just admitted it can never actually be achieved.

But ASIC-resistance is not just an ultimate ideal, it can be easily demonstrated to be attainable. For example - use gcc or MySQL as the target algorithm. While an ASIC might be able to accelerate a tiny portion of either of those systems, hardwiring 100% of gcc or MySQL is completely intractable. The complexity of these tasks would require far more logic gates than even the most expensive CPU in the world. So whenever someone says "nothing is ASIC-proof" or "ASICs are inevitable" it's easy to show this is totally false.

At a fundamental level it's clear as well. You can hardwire logic in lookup tables, of course. But the space needed for such lookup tables grows exponentially. Another simple example - converting a binary byte to hexadecimal - you could create a single lookup table with 256 values, and just output a result for the exact byte value. But that would be an unnecessary waste of space; so you add a little bit of compute overhead and only use a table of 16 values, and perform a shift and two lookups instead. It's always *possible* to hardwire a very complex algorithm, but without programmable logic it gets infeasible as the complexity grows. There's no wishful thinking here, no hopium, no "probably" - this is plain truth.


@iamsmooth 
> The only way that conditions progress toward a better degree of commoditization (as they have in Bitcoinland, and yes while it is certainly not perfect, it is far better than it was in years past and continuing to get even better) is if there is a first a clear market for people to enter, compete, and become more commoditized over time. As long as ASIC-resistance is pursued, that market and process is smothered in the cradle.

*This* is a lot of wishful thinking. Clearly the market for ASICs already exists, and it has arisen despite our previous ASIC-resistance attempts. But the market is *not* a reputable one. ASICs are being built because the "customers" are the ASIC-makers themselves, not the general public. In fact if anyone from the general public tries to order an ASIC chances are high they're simply going to be scammed and lose all their money. Or even if they receive a product, it will be previous generation and obsolete. This is the market that has existed for years and that *hasn't* improved, even if monopolization isn't as much of a factor now. Yes there are more fish in the pond today but they're all still playing the game for themselves only, not for the benefit of consumers. Why anyone would voluntarily choose to hang the fate of their ecosystem on this gang is beyond me.

The ASIC market is developing independently of what we do; it is beyond our influence or control. Whether it "gets better" or not, no one can say. One can only hope. 

What can usefully be done with an ASIC on our network, however, is completely under our control. IMO it's foolish to give up that control so willingly.


## fluffypony | 2019-03-29T08:11:56+00:00
> IMO it's foolish to give up that control so willingly.

@hyc this is where I think we're talking cross-purposes. Nobody is suggesting that we give anything up, and there is broad support for RandomX. Stupid ideas like dual PoW have already been shot down and won't be revisited. We are *purely* talking about the action to take if / when RandomX fails.

I, for one, do not support "tweaks" or further attempts at preventing ASICs, and in that eventuality I would support a switch to SHA3 because it levels the playing field among manufacturers and makes it harder for any one of them to have a massively competitive edge for very long.

But, between now and then, nobody is suggesting that we relinquish anything.

## stoffu | 2019-03-29T08:54:51+00:00
@hyc 
Can you please confirm my assumptions below which I posted earlier?

https://github.com/monero-project/meta/issues/321#issuecomment-477483721

> @dEBRUYNE-1 
> > Precommitting to a switch to an ASIC friendly algorithm after RandomX fails.
> 
> As I understand it, the above is to be corrected as follows:
> 
> - Precommitting to a switch to an ASIC friendly algorithm after RandomX fails _and there is absolutely no hope of fixing RandomX_.
> 
> If I'm correct here (**please confirm**), Monero is still doomed because one can always find false hopes.

https://github.com/monero-project/meta/issues/321#issuecomment-477536323

> Put differently, Monero is doomed if @hyc refuses to agree with the following precommitment:
> 
> - RandomX will stay the same forever until it's broken by ASICs and we switch to whichever ASIC friendly PoW.

I guess this is somewhat rephrasing what @fluffypony said above.


## tarris034 | 2019-03-29T08:56:11+00:00
@stoffu no, we are talking about *tweaks* and failure.

Evolution of RandomX in future is not considered failure or a *tweak*.

## MoneroCrusher | 2019-03-29T10:33:54+00:00
> > IMO it's foolish to give up that control so willingly.
> 
> @hyc this is where I think we're talking cross-purposes. Nobody is suggesting that we give anything up, and there is broad support for RandomX. **Stupid ideas like dual PoW have already been shot down and won't be revisited.** We are _purely_ talking about the action to take if / when RandomX fails.
> 

Nice how you can speak for everyone.
The discussion group in here is an extremely small drop on the big hot stone that is the Monero community. Do you think all people that bought **GPUs specifically for mining Monero** will just be fine and OK if their hardware lands in the trash can?

I can speak as a mid-sized 1-man GPU operation of low end Polaris cards that I specifically and only bought with mining Monero in mind (around 1.5 MH/s):
Before adoption of RandomX there must be an efficient implementation of RandomX in a GPU miner or there needs to be another solution like a dual PoW.
Why do you think dual PoW is a stupid idea? Zcash failing at evaluating and constructing a theoretical concept for it to work doesn't mean it doesn't work.

@dEBRUYNE-1 by the way, it has still not been added in the original thread, not that it matters now.

I think you are vastly underestimating the current underlying Monero GPU community and 90%+ of hashrate coming from their investments.
If you simply dismiss them, I think a contentious hardfork is quite likely, and no, this is not a threat, just an observation.

Re: ASICs

I think we should postpone ASICs _to a much later date_ when cryptocurrency sees large scale adoption and therefore natural commoditization of all aspects of the underlying blockchain occurs, by a large amount of **reputable** companies. Believing that incentivizing commoditization of SHA-3 ASICs with daily emission of around $130k is a pipe-dream at best, and a dangerous and scam-ridden path at worst.

## tarris034 | 2019-03-29T10:37:15+00:00
@MoneroCrusher Miners will adjust as always and this was already discussed.

You are again bragging, adding nothing to the discussion we already had.

We should create another thread for beggars like you.

## MoneroCrusher | 2019-03-29T10:41:25+00:00
I think it would vastly increase the quality of this thread if you stopped shitposting, I'm not saying I'm an expert in hardware, nor software but I do understand some stuff.
However, you on the other hand you don't know the difference between verification time and block time and _other basic facts of Monero and blockchain in general_.

So I suggest you reading up on some stuff and making more concentrated and effortful posts.

## tarris034 | 2019-03-29T10:42:24+00:00
@MoneroCrusher I have corrected my self on this subject, and this is not the place to fight so i drop the mic right here.

## dEBRUYNE-1 | 2019-03-29T10:49:41+00:00
>@dEBRUYNE-1 by the way, it has still not been added in the original thread, not that it matters now.

@MoneroCrusher 

My apologies, I forgot to update it. It has been updated now. 

--------------

@tarris034 

>Evolution of RandomX in future is not considered failure or a tweak.

Let's not fool ourselves here, evolution of RandomX or trying to improve it somehow is tweaking and aforementioned risks apply:

https://github.com/monero-project/meta/issues/321#issuecomment-476318615

Furthermore, if you had read the meeting logs, you would've seen that the majority is in favor of this path:

>The path of least resistance seems to be a course of action where RandomX is adopted in October and a switch to an ASIC friendly algorithm (such as SHA3) is made in case of a RandomX failure.

Which does not include tweaking of RandomX. 

## iamsmooth | 2019-03-29T11:10:30+00:00
@fluffypony 
> We are purely talking about the action to take if / when RandomX fails

Which will not only be likely ambiguous and contentious (people won't agree on whether it has in fact failed given ambiguous data from observation, as well as further disagreements on whether it failed or merely needs to be "upgraded") but also means that any hope of an orderly and safe transition to ASICs will be lost. 

I can't support this slippery "if/when it fails" notion and I view it as very dangerous.

If we want to be responsible about it, and do something reasonably sound, it would be to pick a time period over which we are reasonably confident (say 90%+) that RandomX will hold up, and then switch to ASICs at that point (or at least be clear that we would be switching to something else, whatever that might be) _because by that point the confidence will have fallen sufficiently to still be considered safe_ even if it hasn't failed _yet_. Waiting for it to _actually fail_ on a live network is irresponsible and dumb.

## fluffypony | 2019-03-29T11:21:42+00:00
@iamsmooth oh I totally agree, and my preference is also to pick a date and algorithm now and stick to it. Perhaps some who disagree can explain why.

## WhyIsThisSoSlow | 2019-03-29T11:57:55+00:00
I can explain why.

Because unless RandomX fails and we have no other solution, ASIC is a very bad idea. There is no point in selecting a date for a bad idea unless all else is known to fail.

If the ASIC agenda will somehow be forced until all else fails, there is a very big chance of a split, where the current (at that time) working and improvable PoW, will be used by the majority and a new ASIC only chain will emerge as well, but struggling to exist and make sense, as it will be centralised and will not represent the core of Monero in any way, no matter what name it has.





## fluffypony | 2019-03-29T12:01:47+00:00
> Because unless RandomX fails and we have no other solution, ASIC is a very bad idea. There is no point in selecting a date for a bad idea unless all else is known to fail.

Why is it a worse idea than constantly tweaking the algorithm on a live network? So many people in this thread are just incredibly selfish - the PoW changes don't put YOU at risk, they put the DEVELOPERS at very real risk! The PoW changes are a highly centralised process, and this provides a clear path for regulators to target the developers as a centralised force exerting control over the network.

> If the ASIC agenda will somehow be forced until all else fails, there is a very big chance of a split, where the current (at that time) working and improvable PoW, will be used by the majority and a new ASIC only chain will emerge as well, but struggling to exist and make sense, as it will be centralised and will not represent the core of Monero in any way, no matter what name it has.

I can assure you that only one chain will have any real developer support, and it will be the one that doesn't resort to centralisation as a means of control. If you want centralised control you're better off using Ripple.

## MoneroCrusher | 2019-03-29T12:07:24+00:00
@fluffypony all contributions are quite centralized in their very nature. The important differentiation is that everyone is allowed to participate. Nobody is stopping more people from entering the PoW development stage.

Would you consider Kovri/Sekreta a decentralized development?

The decentralization and trust comes from being open source and being publicly reviewable.

## fluffypony | 2019-03-29T12:08:34+00:00
Are you trying to argue that hard forks every 6 months where the PoW is tweaked is somehow decentralised? Let's not kid ourselves.

## MoneroCrusher | 2019-03-29T12:09:55+00:00
I'm arguing that nothing in Monero's developments truly is. It's always one or few people coming up with great ideas and developing them. Then they get reviewed by a larger audience.
RandomX is extremely centralized in its development, or would you say it's not? With a handful of people developing it?

## fluffypony | 2019-03-29T12:10:33+00:00
*The development isn't the issue*, it's the act of thrusting it on the network that is.

## MoneroCrusher | 2019-03-29T12:17:40+00:00
I don't like quick and reactionary forks either, like the last one.
That's why I proposed [this](https://github.com/monero-project/meta/issues/316#issuecomment-472677985) in the previous thread. There's a very distinct difference in the approach Monero has taken and the approach that I proposed there.

While I do believe a 4 month pseudo fork might be too frequent, I also believe with ASIC-hard algorithms like CN-R-GPU, Ethash and RandomX **a _pseudo_ tweak once a year would be enough** to economically disincentivize ASICs already. This would perfectly blend in with the yearly hardfork that Monero plans to switch to.

So take that approach but do a **planned 12 month pseudo fork** instead of 4 months.

Then we still have the problem of CPU/GPU-only. And there likely can't exist an algo that satisfies that requirement, hence I proposed dual PoW to satisfy both the CPU and the GPU community.

I would then suggest taking such an approach and doing it as long as the ASIC market hasn't changed their practices. Once they finally mature and become reputable (which is an undefined amount of time away), switch to something more simple, like SHA-3.

## WhyIsThisSoSlow | 2019-03-29T12:27:02+00:00
> Why is it a worse idea than constantly tweaking the algorithm on a live network? 

Do i really need to make a huge list of CONS for ASIC? They have been said already. Constantly tweaking is not a proposition as i said before, the tweeks will not be made with an intent to brick ASIC, but will be made to improve the algo in any way that will bring an efficiency advantage or fix any bug. These tweeks will happen once every 12 months if we really want to again predefine dates or they can happen the same as any other code change.


>So many people in this thread are just incredibly selfish - the PoW changes don't put YOU at risk, they put the DEVELOPERS at very real risk! The PoW changes are a highly centralised process, and this provides a clear path for regulators to target the developers as a centralised force exerting control over the network.

So by the same logic, any developer is at risk here with any change of code. Funny you would think like that. How about if we treat the damn PoW improvements as normal code and we just call it development towards the goal of this coin? 

> I can assure you that only one chain will have any real developer support, and it will be the one that doesn't resort to centralisation as a means of control. If you want centralised control you're better off using Ripple.

I think most of the community would want the money they have invested in this chain to be safe from being handled by just a few centralised miners.

The only ones on the ASIC chain will be the ones that already support ASIC as an idea but do not have big investments in the coin. Oh and the ASIC companies because there would still be some profits to be made until they decided to bail for a better coin. They won't even bother to sell the ASIC as no one will want them after that.

## fluffypony | 2019-03-29T12:39:57+00:00
@MoneroCrusher what on earth is a “pseudo tweak”?! Please use precise terms that actually mean something instead of making stuff up.

@WhyIsThisSoSlow every 12 months is insufficient, as you well know and has been evidenced just a few months back.

Developers are indeed at risk currently, which is why some of them are pseudonymous. The PoW tweaks put them at greater risk, which is undesireable. Again: it’s not about writing code, it’s about forcing things on a network. Monero’s forks do *not* have any sort of voting. They are flag-day forks, and entirely centralised. These can and should move to every year, and eventually every few years, and then rarely in some distant future.

Choosing to be anti-ASIC means that once a year is insufficient, but also that the centralised cabal of developers has to make a determination as to whether ASICs exist, and then force a reactionary fork. This is not only undesireable, it’s entirely untenable.

“Just a few centralised miners” is hardly the case - we’ve already seen 3 manufacturers develop ASICs for CryptoNight, which is a legitimately hard algorithm for it. How many more manufacturers will there be with a simple algorithm like SHA3?

If you want to fight against miner centralisation then where are your diatribes fighting against mining pools? What effort have you personally made to make p2pool a reality? And how are you not fighting against the fact that virtually every miner uses a closed-source piece of software that could have a backdoor in it? Seems to me you’re pretty disingenuous.

## MoneroCrusher | 2019-03-29T12:49:53+00:00
> @MoneroCrusher what on earth is a “pseudo tweak”?! Please use precise terms that actually mean something instead of making stuff up.

In a way it's a Schroedinger's cat scenario for ASICs, but instead of their ASICs having a 50% chance of blowing up, upon opening the box, they have a 100% chance. So they'd rather not open the box, aka, not produce the ASICs in that approach.

Read the post I linked, I explained it in there.

> @WhyIsThisSoSlow every 12 months is insufficient, as you well know and has been evidenced just a few months back.

That was with 200x efficiency gain possibilities and 20x efficiency gain possibilities. The whole thing changes once it becomes 2-3x efficiency gain possibility and a 1 year tweak likely is enough.
But that's why I proposed a 4 month pseudo tweak scheme in the earlier thread because as evidenced that is the hard time for ASICs to leave the production bands and entering facilities (But I'd prefer a 12 month pseudo fork schedule with an ASIC-hard algo to a 4 month pseudo fork schedule with an ASIC weak algo)

## WhyIsThisSoSlow | 2019-03-29T12:57:00+00:00
> If you want to fight against miner centralisation then where are your diatribes fighting against mining pools? What effort have you personally made to make p2pool a reality? And how are you not fighting against the fact that virtually every miner uses a closed-source piece of software that could have a backdoor in it? Seems to me you’re pretty disingenuous.

I`m really sorry, i had no idea i had to be the messiah of decentralisation in order to be taken seriously and not appear disingenuous. My valid points still stand, and you are well aware of this. Attempting to weaken the importance of such valid points is again a low blow from such a _respected_ member of this community, as everyone here can read what was said. There is no point in me providing a reply to people that use personal attacks when they fail an argument. Thus i will not reply to you after this, as your intentions are now clear and everyone can see them.


## fluffypony | 2019-03-29T13:00:03+00:00
You don’t have to be the messiah of anything, but you also don’t get to say that ASICs are bad whilst ignoring all the problems with the status quo.

## MoneroCrusher | 2019-03-29T13:06:07+00:00
> If you want to fight against miner centralisation then where are your diatribes fighting against mining pools? What effort have you personally made to make p2pool a reality? And how are you not fighting against the fact that virtually every miner uses a closed-source piece of software that could have a backdoor in it? Seems to me you’re pretty disingenuous.

Surely, the status quo isn't ideal with pools, that's why I run my own node and pool on my local LAN. But it's a completely false equivalence.
Are you suggesting solving that problem by adding more problems ontop (ASIC centralization/mining hardware ownership/geo-centralization)?

It seems like you are not here to discuss and open to absorbing good arguments, but that you already made your decision with regards to ASICs.

As I said earlier, I have absolutely nothing against ASICs if I and everyone else can buy them from reputable sources with extendable warranties of up to 10 years (standard for CPUs & GPUs) and strict consumer protection policies.
Before that happens, I don't consider ASICs a solution at all and hoping that pre-commiting to an ASIC algo somehow will create a different fair market (which has absolutely and utterly failed in Bitcoin so far **in 10 years time** despite having 80x the market capitalization of XMR and about 83x more daily emission (Mint BTC blocks go for 30% more)) is absolutely unrealistic in my opinion. 

So from my perspective:
At this point in time, ASIC talk seems like a big waste of time because I only consider it a viable solution once commoditization has kicked in (which implies widespread adoption of cryptocurrency). That won't happen for years. And since we don't know how those algos will look like in 5 to 10 years and how good and secure they are in 5 to 10 years I think it's best to discuss ASIC adoption when the time is right to do so. I don't believe that time is now.

However, I can understand that the time might **seem** right to pre-commit now, but the mature and fair ASIC market is just not there yet, otherwise I would likely support it. An ASIC network does have some pros if the environmental variables are right, which again, they are not.

## tarris034 | 2019-03-29T14:54:26+00:00
> @tarris034
Evolution of RandomX in future is not considered failure or a tweak.
> @dEBRUYNE-1 
Let's not fool ourselves here, evolution of RandomX or trying to improve it somehow is tweaking and aforementioned risks apply.

Lets assume some better PoW emerged or RandomX idea is reworked from ground up and that the network is hard forking because of other updates, regardless of PoW change or not all nodes and pools will have to update.

So why can't we change PoW at that time ? it would not disrupt the network, it would not add to the centralization.

If you gonna put a sunshine date for ASIC-friendliness, lets put another in the way if ASIC-friendliness won't return the same feelings and becomes a coffin like for Bitcoin.

Or are we afraid that this additional sunshine date may hurt feelings of the ASIC manufacturers who raped our network couple times ? at least they could take us to dinner... buy some flowers... nope. straight out rape.

> @fluffypony Choosing to be anti-ASIC means that once a year is insufficient

This is not a fact.
>, but also that the centralised cabal of developers has to make a determination as to whether ASICs exist, and then force a reactionary fork. 

Who puts pressure on devs ? who did discover the last ASICs ? not monero devs but some guy who analyzed nonce distribution. (sorry, can't remember who)

>This is not only undesireable, it’s entirely untenable.

Agreed. But only in the scenario you described which is false.

>And how are you not fighting against the **fact** that virtually every miner uses a closed-source piece of software that could have a backdoor in it? 

That's not a fact.
At least miners have choice to use open/closed source software (I'm against using any closed), and it's way easier to check for backdoors in software miners even the closed ones than in hardware miners.

>How many more manufacturers will there be with a simple algorithm like SHA3?

or how less ? it's all speculations, could be 0 could be 100. I wouldn't gamble with the fate of Monero in this Chinese casino with worst reputation on the planet.

## MoneroCrusher | 2019-03-29T15:14:35+00:00
Should be an interesting read for "RandomX-Pure" proponents:
https://www.technologyreview.com/s/613163/a-multi-million-dollar-criminal-crypto-mining-ecosystem-has-been-uncovered/

Conveniently both my suggestions destroy and make such schemes less attractive:
eternal 12 month forks + keeping GPU miners in the game via dual PoW

And no @hyc GPU miners don't get hijacked nearly as often. Nobody's gonna hijack my GPU miners since they're not even connected to the internet. And even if it happens, dedicated GPU miners will notice very very quickly since their income will vanish and they check it daily if not several times per day.

@tarris034 you think people with gaming machines won't notice when they start gaming or watching 4K videos and their computers start crashing? CPU hijacking is so much easier to implement since you don't have to deal with graphics drivers and it's not as easily detectable

Your arguments so far don't convince me at all. Show me some reports of those AV firms you mention. Wondering what the rate is.
https://arstechnica.com/information-technology/2018/01/in-the-wild-malware-preys-on-computers-dedicated-to-mining-cryptocurrency/
LOL 1 ETH.
I think it's fair to say that CPU botnets are much more rampant than any GPU botnet could ever be.
For sure there would be unvoluntary mining on both sides, just by a multitude more rampant on CPUs.

## tarris034 | 2019-03-29T15:18:24+00:00
GPU can be utilized as well on infected machines, if you're gonna fight malware the only solution is ASIC-friendly PoW which also suffers from malware as recent posts on the interwebs shows.

@MoneroCrusher It's not dedicated miners who usually get infected (they are too smart) but dumb Internet users with their gaming machines. As described by AV companies in their reports, many infected machines mined ETH with GPU's.

> you think dumb internet users with Gaming machines won't notice when they start gaming or watching 4K videos and their computers start crashing? 

They mine in idle, gaming / watching is not affected.

> CPU hijacking is so much easier to implement since you don't have to deal with graphics drivers

It's very easy to implement IF/ELSE routine that will use appropriate miner according to readings.

>Your arguments so far don't convince me at all. Show me some reports of those AV firms you mention. Wondering what the rate is.

I've read plenty of them, just google and read by yourself - you will get **plenty** of results.

>I think it's fair to say that CPU botnets are much more rampant than any GPU botnet could ever be.

Malware writers will always try to utilize **everything** possible on the machine, they will even infect your fridge just to mine 1 H/s more. Of course they will not run at 100% or mine when you're gaming because it would shorten their life in the infected system.

But you can be sure that if we had dual PoW, infected machines would mine both of them.

>For sure there would be unvoluntary mining on both sides, just by a multitude more rampant on CPUs.

So by incorporating dual PoW you agree that there would be more infected machines / more hashrate coming from infected machines. Basically, dual PoW will increase revenue for malware writers.

## MoneroCrusher | 2019-03-29T16:05:38+00:00
Absolutely not.
If involuntary CPU mining is 100x higher than involuntary GPU mining, then a dual PoW will decrease involuntary mining if comparing to a CPU-only mining network.

## tarris034 | 2019-03-29T16:33:26+00:00
@MoneroCrusher 

Explain how dual PoW can **decrease** revenue for malware writers ? It does exactly the opposite, you are giving them another part of computer to use more efficiently.

I find this discussion about dual PoW and malware pointless, malware writers will always use everything they can, regardless if it's CPU only PoW / GPU only / Dual. With Dual PoW you will just increase their income.

Would like to note one thing:
>Do you think all people that bought GPUs specifically for mining Monero will just be fine and OK if their hardware lands in the trash can?

GPU's will not be bricked, miners can sell them to gamers or other miners who mine other coins.
But lets not continue this discussion here as this thread is about security of the network and not about investments.

## MoneroCrusher | 2019-03-29T17:01:48+00:00
> Explain how dual PoW can decrease revenue for malware writers ? It does exactly the opposite, you are giving them another part of computer to use more efficiently.

I literally just explained above how it reduces relative involuntary mining on the network.

For anyone interested, the full in-depth study PDF:
https://arxiv.org/pdf/1901.00846.pdf

From this we can conclude:
Currently we have and we had botnets and they increasingly ceased to exists with the introduction of PoW changes and they were also not as incentivized monetarily because of vast amounts of GPU miners.

What RandomX suggests is kicking off all GPU miners (Ryzen 5 2600: 3x more hashrate, 3x less power and 3x less expensive than Vega 64 in RandomX and it'll be worse for Polaris cards) and taking away the PoW tweaks completely (not even once a year).

This is the absolute dream and perfect breeding ground for any botnet owner.
That's why we need a dual PoW as well, not only to keep community peace, but also to not become a network mainly dominated by large botnets.

## MoneroCrusher | 2019-03-29T17:06:52+00:00
Interesting Excerpt:
![image](https://user-images.githubusercontent.com/32360383/55249887-67dce500-524d-11e9-929e-6dda4adc4153.png)
![image](https://user-images.githubusercontent.com/32360383/55252737-da50c380-5253-11e9-8c38-67dd0f460864.png)
![image](https://user-images.githubusercontent.com/32360383/55250616-e38b6180-524e-11e9-87f8-fbd4cb121ed8.png)
![image](https://user-images.githubusercontent.com/32360383/55250644-f736c800-524e-11e9-84cd-b167d3bdabfb.png)

Edit:  @tarris034 Has got to be kidding me. There are the hard numbers and he simply claims they are not true. Guess you already made your mind up.


## tarris034 | 2019-03-29T18:24:34+00:00
@MoneroCrusher 
>Currently we have and we had botnets and they increasingly ceased to exists with the introduction of PoW changes and they were also not as incentivized monetarily because of vast amounts of GPU miners.

That is simply untrue. Botnets can update miners and no amount of GPU will hold them down, they pay 0 electricity, they don't care it's less profitable.

And no fancy article will change my mind on this subject.

>This is the absolute dream and perfect breeding ground for any botnet owner.

Again, you are wrong.
Perfect dream would be having dual PoW to get most out of the infected machines.

I don't know why you keep talking about dual PoW when we already established there's too many problems with it.
@edit: I know why.

## danrmiller | 2019-03-29T18:28:45+00:00
> But ASIC-resistance is not just an ultimate ideal, it can be easily demonstrated to be attainable. For example - use gcc or MySQL as the target algorithm. While an ASIC might be able to accelerate a tiny portion of either of those systems, hardwiring 100% of gcc or MySQL is completely intractable. The complexity of these tasks would require far more logic gates than even the most expensive CPU in the world. So whenever someone says "nothing is ASIC-proof" or "ASICs are inevitable" it's easy to show this is totally false.

Being hard to accelerate via hardwiring is not sufficient. If an ASIC is a little more energy efficient, at scale this will run everyone else out (I know there are people saying it hasn't yet happened to ethereum). Also if you design a system that cannot be made significantly faster with custom hardware, but the work can be easily parallelized or the verification is slow enough to cause issues with orphans/propogation/reorgs, or other things like that, its still not suitable.

## tarris034 | 2019-03-29T18:37:42+00:00
@danrmiller if the efficiency isn't far off of regular CPU's, bigger scale of operation of those ASIC will not harm the network. ASIC manufacturers will profit a little more than others, that's it.

I could be wrong on this, would be easier with actual numbers because this are only theories based on speculations.

Investors can scale as well with CPU's. Already made some calculations in the previous thread for amateur miners without special/server grade equipment.

If there will be demand for motherboards with more CPU sockets, I'm sure some of the big players like ASUS or others will come with one, as they did with PCI-E when the demand for GPU's was high.
Shouldn't be too high price considering CPU's don't have to work in parallel like in server motherboards meant for Xeon multiprocessing (just my guess).

With today's multicore CPU's where one CPU can have 20+ cores, having one motherboard for each is not so bad. With server grade mobo meant for multiple xeon's we are already nicely set, used ones aren't so expensive.

This scenario is much more probable than wishing ASIC manufacturers will create and start selling SHA3 miners for masses without any delays.


## hyc | 2019-03-29T19:47:05+00:00
@MoneroCrusher the article was interesting but I think you missed an important detail. Botnet owners/operators can automatically deploy updates to their botnets. But with PPI Pay-Per-Install they charge the botnet renters for that service. So while botnet miners who are renting the nodes may get thrown off the network by a PoW change, the botnet owners make money regardless. I.e., frequent PoW changes have no effect on the botnet operators.

## SChernykh | 2019-03-29T20:49:58+00:00
> If there will be demand for motherboards with more CPU sockets, I'm sure some of the big players like ASUS or others will come with one, as they did with PCI-E when the demand for GPU's was high.

I think even PCI-e boards with CPU socket + 2 DIMM sockets will be made..

## bitlamas | 2019-03-29T22:21:26+00:00
> @fluffypony my preference is also to pick a date and algorithm now and stick to it. Perhaps some who disagree can explain why.

The reason is that there's a chance RandomX actually works as planned. It doesn't seem to me a complete impossibility that an algorithm be developed in a way that the specialized hardware has a limited advantage when compared to the top processor on the market.

The coexistence in mining of specialized hardware **and** extremely accessible hardware on the market (GPUs and CPUs) seems plausible to me. I don't really understand the technical reasons why this is completely impossible. I'm not convinced that such an algorithm is equivalent to a golden unicorn. If it's possible, it's worth investing in it because it's aligned with the current Monero ethos. There are very competent people currently working on it. Why would anyone abruptly stop such development by precommitting to an expire date is beyond me.

Based on that, I don't think there are any real, clear, science-based reasons for simply killing the RandomX project after a specific date.

**About adopting ASICs**

Much of this discussion is based on the human capacity to predict the future. No one here can confirm how the ASIC market will be developed for Monero, or for SHA-3. It is impossible. The best that can be done is to imagine based on the experiences we have had in the last 10 years, which by the way is not good. I understand the many arguments in favour of adopting ASICs, but it seems that some people are predicting a bright, good future, where the nirvana, perfect balance will be achieved when we migrate to SHA-3 and only a few GPU miners will be sad in their corner.

To believe that this will definitely be the case is very naïve. People promoting a quick and definite change to ASICs should be able to at least consider all the negative scenarios that can happen, in the same way that we are considering all the negative scenarios when migrating to RandomX.

It is therefore very important that the discussion focuses on deciding in the best possible way what would be the acceptable criteria for defining the **success** or **failure** of RandomX. These terms need to be defined in a solid way, very well articulated so that in an eventual failure of the algorithm, we won't have to deal with a large number of people insisting on tweaks and other undesirable solutions.

**About tweaks vs. improvements**

It must be immediately clear that any modification to the algorithm that has the sole purpose of "breaking" the _current_ ASICs is undesirable.

But I agree with @SamsungGalaxyPlayer that we cannot close ourselves off completely from any kind of organic evolution of the technology, or the discovery of an implementation bug. These factors should be considered real and valid for any technology developed in the universe. Even the implementation of an algorithm like SHA-3 may receive improvements or bug fixes in the future.

That is why I also believe that it is necessary to discuss specific terms on how to implement a new technology or improvements on RandomX. Although @dEBRUYNE-1 says this is vastly different from improvements in other pro-privacy technologies, I can't understand exactly why. In the same way that in the implementation of Bulletproofs we performed several audits by different companies to ensure that the code was as good as possible, why can't we perform a similar procedure with another piece of technology, in this case PoW?

From what I understand, every new implementation in Monero's code (including the use of Bulletproofs) increases the risk that something doesn't work properly and the protocol breaks down definitively. I agree that we should try to mitigate the risks as much as possible, but simply abandoning an integral part of Monero's soul (egalitarian mining) and exchanging it for the uncertain future that ASICs will bring does not seem to me to justify the abnormal fear of the possible technological evolution of the algorithm that, again, should be carried out in a professional manner and with well-articulated terms, definitions and audits.

## bitlamas | 2019-03-29T22:38:13+00:00
And finally, I would like to remind those who believe that resisting ASICs is literally impossible, that in this case you also have an interest in trying to clearly define the terms of success and failure of the algorithm, because according to your prophecy, there is no chance that RandomX will work, and consequently, as most of us already agree, we would then adopt an ASIC-friendly algorithm.

## BigslimVdub | 2019-03-30T04:08:14+00:00
Remember, Mining for profitability is not the *only* or *most important* part of a cryptocurrency project. Every time you fork there is a chance something will happen and everyone running a node needs to verify those possibilities. 

Originally I was against ASICS 100% since I got into the mining scene in 2016, mainly because of profitability reasons. Again and again, I was against ASICS because owners were not playing fair and I could not obtain one for myself. Then I started to educate myself on ASICS and their purpose and general use-case. In the end, I realized that using ASICS on cryptocurrency makes sense because they only have to do one task all day long and are far more efficient than any other hardware. I feel both sides of the discussion because I was (and still am) a hobby miner yet I also want to see long term use-case for every crypto project. If RandomX works out for Monero, that's fantastic! However, I still believe that if there is a chance for profit and a chance for innovation, that ASICS will still return at some point.

Keep in mind that if their hash power is greatly reduced, they may appear more slowly and "organically" on the network. One could still hold 85% of the total network hash rate but "hobby miners" may think it's just "normal adoption" or something of that sort since its not an obvious 200-300% net hash increase in a one-month time frame. 200-300% increase over 9 months may cause a need for additional research for those looking for ASICS on the network. Will net hash increase be expected after a fork to RandomX? I remember when Monero went from 75Mh to 250Mh and everyone pooped their pants because of profitability. It was just farms/botnets moving to Monero, because. 

That being said, what can the community agree on for Monero's "normal" network hash rate? 290Mh? 500Mh? 150Mh? Is there a normal hash rate? How can community members know if an increase in hash rate is normal or ASICS? Is Monero forever tarnished from the past 2 years of asic debacle that every miner that sees a 50Mh increase or decrease here or there will automatically think its ASICS on the network? Does the community believe that Monero should always and forever be 250Mh and the devs must try to keep the net hash here? Can Monero still organically grow with or without ASICS?

IMO it's an educational and lifestyle change that needs to happen for the greater community and developers to work in unison for the best long-term use-case for Monero. The next year will be an important year for Monero. 


@4chanStanMan 
> 
> And you will now focus on aeon? That coin has been dead for 2 years bruh. Where you been? The community hates the fact that their voice is never a concern. Why do you think turtlecoin is more popular than aeon now?

LoL Aeon dead..... 👋 

## tarris034 | 2019-03-30T08:30:30+00:00
@BigslimVdub There's not much chance any of the ASIC manufacturers would accomplish this, mainly because of financial advantages being too small compared to regular hardware.

With only x2 efficiency it would be very hard to generate that much hashrate, and why would they put money on it if they could just create ASIC for other coin and have much more profit.

Why would they invest in designing new ASIC millions of dollars for such small gain, I think they would be better off just buying regular CPU's and making boards for them, having in mind this investment won't be bricked and can be shifted to other coins or reselled.

Also please don't mention aeon shitcoin in this thread, unless it can add something to the discussion.
AFAIK they are another copy/paste clone without any development of their own.

Actually after thinking more about it:
>The community hates the fact that their voice is never a concern

This problem of theirs is what should be considered a centralization problem, when the devs do what they want.

In this light I don't think Monero is that much centralized by having trusted core team, as they make decisions with regards to the community.

I know it's not perfect, but at least we don't have the above problem of silence and "I do what I want" attitude.

(funny how more and more aeon users come here, is it because they can't discuss their problems with their devs or is it because only here we have devs that actually do something..)

## 420coupe | 2019-03-30T14:19:06+00:00
> With only x2 efficiency it would be very hard to generate that much hashrate, and why would they put money on it if they could just create ASIC for other coin and have much more profit.


This is an assumption that ASICs will only be capable of 2x; which cannot yet be proven as RandomX is not complete. 

## tarris034 | 2019-03-30T15:39:33+00:00
@420coupe 
Sure, in reality it will probably be smaller and maybe after time they will manage to get better if they even care to waste big amounts of money on such little gains while there are other coins with better profits.

Time will tell.

## 420coupe | 2019-03-30T16:56:32+00:00
> > > With only x2 efficiency it would be very hard to generate that much hashrate, and why would they put money on it if they could just create ASIC for other coin and have much more profit.
> > 
> > 
> > This is an assumption that ASICs will only be capable of 2x; which cannot yet be proven as RandomX is not complete.
> 
> Sure, in reality it will probably be smaller and maybe after time they will manage to get better if they even care to waste big amounts of money on such little gains while there are other coins with better profits.
> 
> Time will tell.

you're pulling numbers based on what?  

My point you cant say in reality it will be more or less; you dont know untill it's done and there's eyes reviewing a 'finished' code

## tarris034 | 2019-03-30T17:06:33+00:00
@420coupe This are the predicted efficiency numbers based on physics from what I've read. 

As I said, time will tell. From the financial perspective I don't see point on making ASIC just to prove a point it can be done and losing other, much better opportunities for returns of investment.

Unless they would make it public and sell to everyone, then even 1.1x / 1.2x better efficiency would be met with lot of orders from miners. But I don't see a scenario where they waste money just to mine for them self with this little efficiency gains over other miners.

In this perspective with RandomX we are closer to the situation where ASIC's become available for everyone.

With more efficiency gains like 50x / 100x they rather mine for them self and I don't blame them for that.
Only idiot would sell chicken that lays golden eggs.

## timolson | 2019-04-01T23:55:34+00:00
I did a technical review of RandomX along with [7400](https://www.7400.digital/), a top ASIC designer here in Silicon Valley, and posted a [few comments](https://github.com/tevador/RandomX/issues/31#issuecomment-478778652) in the technical thread.  

While the Monero PoW team is undoubtedly talented and hard-working, device-binding to a CPU is a very difficult problem.  RandomX does have a chance of working, but challenges such as the "branching problem" may be _insurmountable_.  Fundamentally, CPU's are designed to run fast first, and save energy second, while PoW's need to save energy first, and be fast second.  CPU's may simply be a hammer trying to drive a PoW screw.  Does the screw look enough like a nail to keep AMD and Intel CPU's within 2x of ASIC's?  It's an open question, and we won't know the answer until a RandomX ASIC is fully designed, ready for tapeout.

ASIC makers will definitely try.  Because of the complexity of both CPU's and of RandomX, there is enough wiggle room for ASICs to _potentially_ outperform.  Even between CPU's there's currently more than a 2x performance difference.  How does anyone expect to get tighter bounds than that?  With all respect to the PoW team, RandomX may be attempting the impossible.

If a RandomX ASIC is built, there may not be many manufacturers, either.  RandomX is complex and difficult by necessity, just like a CPU, so producing a fast RandomX ASIC may be a challenge that only a few (secretive) manufacturers take up.  Isn't that the worst of all outcomes?

Of course the community has to try RandomX.  There's a chance it works.  But that is _not clear_ and there is a _good probability_ that we ditch RandomX again by 2021.

## hyc | 2019-04-02T02:38:17+00:00
@timolson Thanks for the review, and your invaluable insights.

One comment - there's more to the CPU world than Intel and AMD. In particular "designed to save energy first, and be fast second" also applies to a vast world of *mobile* CPUs. And going forward, these may be the more important target as mobile device sales have far outstripped desktop/laptop sales for many years now.

## MoneroChan | 2019-04-04T05:43:56+00:00
Exploring Solutions to @fluffypony 's "Reactionary" Fork issue:

Since Hardforks occur "seamlessly" at a certain [Blockheight Value]

Q: Is it thus possible to pre-code RandomX PoW, but "Trigger that same seamless hardfork" based on Other [Values] instead? Example:

- [Value] of : [Average difficulty past 2 weeks > 125% Non-ASIC Baseline ] (ASIC on continuously), and
- [Value] of : [Cumulative number of abnormal 10% difficulty fluctuations < 1 month] (ASIC abuse of fluctuating difficulty)

Result:
- No Reactionary issues . No Dev intervention needed, pools and exchanges don't need to do anything when ASICs appear.
- ASIC manufacturers are forced to create and "Sacrifice a CNR ASIC" to trigger fork before they can use a RandomX ASIC, Increasing the cost of any RandomX ASIC, 
- Extended lifespan for both RandomX and CNR.
- Hardfork triggered by Decentralized Community Vote (Hashpower threshold)
- Bricks ASICs faster than a dev initiated hard fork
- Game Theory Benefits (nuclear stalemate) without Reactionary stress on Devs.

Can this work? 

## SChernykh | 2019-04-04T07:38:30+00:00
@MoneroChan No. They don't need to create CN/R ASIC to trigger any predefined values. They just need to rent some big GPU farm for a couple of weeks. Biggest ETH farms have 100k+ GPUs.

## MoneroChan | 2019-04-04T10:24:52+00:00
@SChernykh
Re: "They just need to rent some big GPU farm for a couple of weeks" 
- YES ! Isn't that good???? :) 
- ASIC manufacturers will be forced to Kneel and Beg and Pay GPU Miners for the right to LIVE !

- Why Give them RandomX Free of charge?........
- when we can FORCE the ASIC manufacturers to PAY for that priviledge!
- ASICs are the cause of the problem. This guarantees to make them Pay for it.

-No sudden hard fork,  Exchanges, Miners, Nodes, everything switches seamlessly, No Reactionary complaints to Devs. Only ASIC manufacturers suffer.

Wouldn't it be wonderful?

## SChernykh | 2019-04-04T10:31:25+00:00
Another problem is how to define these triggers. Sudden hashrate increase may happen because of price spike like the one happened this week. And no, we can't embed price tracking into blockchain consensus code.

## MoneroChan | 2019-04-04T10:55:15+00:00
@SChernykh

Trigger is simple to define, Thanks to Past ASICs we have a excellent baseline.
Here's a draft demonstration:

    Trigger 1: [Sum Difficulty] of [Past 10000 Blocks] is > "600,000,000,000,000" , ( Basically 60G Difficulty per block average over 2 weeks) then Set Pow = RandomX

    Trigger 2: [Sum Difficulty] of [Past 2000 Blocks] / 2000 is < [(Current difficulty / 9)] Then Add 1 to Abnormal_Fluctation_Count.value. ELSE Minus 1 from Abnormal_Fluctation_Count.value. Then if Abnormal_Fluctation_Count.value > 30 , Set Pow = RandomX

    Trigger 3: No price monitoring needed! If it switches, Monero must be doing VERY well, then let it switch to RandomX naturally. Remember, we're switching to RandomX anyway right? So no problems here.

:: Draft Algorithm: (not code)

IF POW_Algorithm.Value ="CryptonightR", THEN
:: Run Sensor 1 : ASICs continuously running
IF [Sum Difficulty] of [Past 10000 Blocks] is > "600,000,000,000,000" ::(60G /block average over 2 weeks)
THEN SET POW_Algorithm.Value = "RandomX"
END IF

:: Run Sensor 2 : ASIC Difficulty Abuse 

IF [Sum Difficulty] of [Past 2000 Blocks] / 2000 is > [(Current difficulty / 9)]  
	THEN SET [Abnormal_Fluctation_Count.value] = [Abnormal_Fluctation_Count.value] + 1
END IF

IF [Sum Difficulty] of [Past 2000 Blocks] / 2000 is < [(Current difficulty / 9)]  
	THEN SET [Abnormal_Fluctation_Count.value] = [Abnormal_Fluctation_Count.value] - 1
END IF

IF [Abnormal_Fluctation_Count.value] > 30 
	THEN SET POW_Algorithm.Value = "RandomX"

END IF
END IF

## SChernykh | 2019-04-04T11:05:47+00:00
I'm sorry to say, but this is just ridiculous to integrate some ad-hoc triggers into $1B market-cap coin based on past performance. They can be triggered by simple price fluctuations, sometimes even because of other coins (ETH miners moving). And it'll require another hard fork, which will change to RandomX anyway as was agreed before. CN/R is just not good enough for ASIC resistance. Switching from GPU to CPU algorithm will require huge preparations from pools and miners, it's better to do it during scheduled fork. 

## MoneroChan | 2019-04-04T11:56:45+00:00
@SChernykh
So the switch to RandomX is too great to be automated seamlessly by smart trigger mechanisms?
Oh well, Manually then it is.

## tarris034 | 2019-04-04T12:09:35+00:00
> @SChernykh No. They don't need to create CN/R ASIC to trigger any predefined values. They just need to rent some big GPU farm for a couple of weeks. Biggest ETH farms have 100k+ GPUs.

100k+ GPU Farm ? where ? any proof ?

The trigger would need to happen according to nonce distribution patterns but I think it brings too much complications and abuse possibilities.

Switching PoW back and forth is just a temporary (very short) defense anyway.

We could as well just go the easy way and use dual PoW but not simultaneous, and force switch from block to block or every X blocks from one PoW to another. ...it's stupid and would be abused.

## JustFranz | 2019-04-05T01:27:02+00:00
For a specific real world event (secret ASIC miner existence) you want to make a trigger that switches POW and that trigger could get flipped at any moment, flipping the network on its head. The trigger is not safe from manipulation or natural network growth either.

Even if by magic you could guarantee that it will only happen when the specific real world event happens, its still a bad idea. Things change - bugs are found in code, people change their minds, conditions change in the world. 

I do not want a bomb in my crypto, IMO each fork should be almost regarded as the last one. Maybe I don't want to go along with the next fork, or someone else doesn't. You shouldn't half ass anything, include experimental/untested/unvetted nonsense. I don't like hostage situations like these.


A question about the SHA-3 date. What is the date based off of? Do we predict the useful life of RandomX (based on audit?) and subtract from that to be safe? Are we giving ASIC companies time to prepare? Prepare for what? Are we just picking some future time and hope that by then something has happened? 

If we are going SHA-3, is it best to make the change as soon as possible or to wait as long as possible?

## tarris034 | 2019-04-05T10:39:11+00:00
I think ASIC companies have already proved them self to be worthless in the crypto space, just look at today's BTC problems.

It centralizes the network on so many levels I'm surprised we still even talk about it.

Forget about the dream of ASIC companies around the world producing most efficient chips available for masses, it didn't happen in the last decade when there was a crypto boom, and it won't magically happen now.

For short I will call ASIC companies GREED from now on. Way simpler and much more descriptive.

Just look at this known GREED website
https://shop.bitmain.com/?lang=en

SOLD OUT SOLD OUT SOLD OUT SOLD OUT

LOL you tell me that after all this years they still have logistical problems in the production department ?
I think we can call it B$.

Also you gotta love notices under their hardware when they were *available*:

> 8. If delivery to US, according to the NY ruling N297495 ,mining machine might be classified under 8543.70.9960 which contain with 2.6% of the import duty and tax plus additional 25% of the import duty due to country of origin made in China.
> 
> 9. For Germany shipments, please be aware about we have numbers of German customers met custom clearance problems when shipments arrange via DHL. You may wish to consider this piece of information before choosing shipping carrier. In the case of any custom delay or shipment return due to DHL shipping, Bitmain will not be held liable.
> 
> 10. Due to a delay in the supply of EU-Standard materials, for this batch, the shipment to EU countries will be suspended till further notice. 

Keep in mind that this units are ~10 KG each (without PSU), so the shipment alone can be very expensive.

love this one too:

> 3. To prevent hoarding and to ensure that more individual buyers can purchase miners in this batch, we have set a limit of 10 miner per user. 

Someone was talking about big scale operations ? yeah right.
This needs translation:

3. To prevent large scale operations other than ours and ensure more profitability for us, in this batch we have set a limit of 10 miner per user.

If they would sell them without limitations, no one would hoard them for resale in the first place.
Or do they call big mining investors - hoarders ? anyway, it's another B$, another lie.
BTW, 10 miner per user is always the limit, it's not "in this batch" only as they suggest in this notice.

For dessert lets read some of the customers comments: (scroll down mspain tutorial on how to order)
https://support.bitmain.com/hc/en-us/articles/221888028-Ordering-payment-process

We can speculate more about adoption but this is the grim reality BTC is living for many years now.
The diff is so high they seek for a new host, and I think they found the perfect one. Just needs some adjustment, that's all. SHA3 (or any other GREED-friendly PoW) would be perfect, for them. Of course they have many more greedy reasons.

"Cure worse than the disease" - Perfect analogy for going GREED-friendly to avoid centralization.

I encourage everyone to Google: **btc centralization china** and read couple articles
I would be afraid of having large amount of money in BTC, the day we go GREED-friendly will be the day I trade all my XMR to Gold as I will see the whole crypto scene as a failed project and a one big joke.

For more fun google **bitmain scam**
Some of the reviews:
https://www.trustpilot.com/review/bitmain.com

PS. I don't base my opinion on GREED after one single bad actor.
Lets view what's for sale on: https://whatsminer.net/shop/
...some power cords, PSU. Nothing.

https://halongmining.com/shop/dragonmint-16t-miner/
The only model they've got, unavailable with no estimated date of shipping.

baikalminer - need to contact via email to ask if I can buy, sent them message couple days ago, still no answer. But from reviews on facebook I can see it's another scam.
**UPDATE** answer that I got when I wanted to order 100 of them: https://pastebin.com/raw/0Ny8bYb5
I guess they have the same *policy* as bitmain, idk what he meant by "few" but you can surely forget about big scale operations (not that anyone would want to make business on big scale with a company that has such bad reviews)

Bitfury - have to ask, still no answer.
(love the mandatory "Information on existing bitcoin activity" field, like I have to explain my self before they consider selling it to me)
**UPDATE** No answer. And I doubt they will ever answer, guess I did not please them enough with my  "Private mining operation" answer to the above question in the message form.

I have also checked couple known resellers, they all stink. According to what people write they take money in advance then tell you manufacturer is out of stock and can send you newer version of miner when they release it but you'll have to wait 3-4 weeks, if asked for return of money - silence.

USB ASIC sticks don't count as a proper hardware for mining so I'm not even checking them.

This is ridiculous. Right now I can go to any online/stationary hardware store and buy as many CPU's my wallet will let me with at least 3 year warranty, proper service, and the same day or max second day of delivery time, which are **way** more difficult in production.

And I still don't blame them, if I could built a money printer, I would never sell it or sell it in low quantity or after new more efficient one is built so people think it's free market for them.
You could buy them easier in the past when the efficiency on new ones were much higher, now it slowed down to the point they just stopped selling altogether.

What we see here is the biggest scam in the history of mankind.

*In the perfect world, where there's no greed, hunger for control and world domination, I would be in favor of going SHA3 or any other hashing algo that could be easily hardware built. But who needs money in the perfect world..*

@update: whatsminer is now accepting pre-orders, you need to contact them for bigger orders and so I did:
https://i.imgur.com/0XuJzwL.png

They will happily take 2+ million $ order anonymously, don't expect to know the full name of the guy that will take your money. With no guarantee that you will receive anything and at the expected date, is this on purpose being made to discourage investors ?

This is not how business is done. They don't take any responsibility.
(half an hour later still no answer, so they rather pass big order than give any info that could help authority track them down)

Apparently his full name is matt justin: 
https://bitcointalk.org/index.php?topic=5028653.0

But he lied to me that he is **only** employee:
https://i.imgur.com/3rKeC2W.png

Another scammer.
(he closed and deleted my ticket after sending him bitcointalk link with proof that he is not only an employee)

## EnglishGentleman | 2019-11-07T14:19:27+00:00
**Questions about RandomX & LOKI Hash Rate.**

Actually RandomXL 

Loki hashrate on pool HeroMiners in early November 2019: see https://loki.herominers.com/

16 MHS from 25 workers solo mining=630 KH/S/worker equivalent to 48 Ryzen9 or 252 Opteron 6378 CPU. Pool mining 44 MH/S from 790 workers is 55 KH/S per worker => 4 Ryzen9 or 22 Opt6378. Why is hashrate so high? What is the investment case?

Loki is a great yet tiny coin with $14m cap & daily volume of $17k. Why would a solo miner invest $25k (48x$520) to get 31USD per day revenue? Hero is 87% of Loki hashrate.   What is the source of the hash? 

I think I know but tell me your view please?

![image](https://user-images.githubusercontent.com/57457499/68396518-97e85100-0169-11ea-86ae-00f640d2c534.png)



![image](https://user-images.githubusercontent.com/57457499/68396482-89019e80-0169-11ea-93d6-d90b304fa5c2.png)


![image](https://user-images.githubusercontent.com/57457499/68396446-7d15dc80-0169-11ea-8228-2c9e12516f35.png)


## SChernykh | 2019-11-07T14:22:37+00:00
There was no investment, these are CPU farms that existed before. They consist of mainly old decomissioned Xeons and Opterons.

## SamsungGalaxyPlayer | 2020-03-10T20:41:28+00:00
@dEBRUYNE-1 can you please close this? We can open a new discussion if we want to revisit this for a future upgrade imo.

# Action History
- Created by: dEBRUYNE-1 | 2019-03-25T15:55:29+00:00
- Closed at: 2020-06-05T15:25:49+00:00
