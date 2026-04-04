---
title: Discussion of the future of the PoW algorithm
source_url: https://github.com/monero-project/meta/issues/316
author: dEBRUYNE-1
assignees: []
labels: []
created_at: '2019-03-12T07:58:22+00:00'
updated_at: '2024-09-20T14:23:38+00:00'
type: issue
status: closed
closed_at: '2020-06-05T15:26:05+00:00'
---

# Original Description
This ticket is meant as supplement to #315 as well as a place where ideas can be discussed in more detail and outside of the scheduled meeting(s). As far as I can see, we basically have these options:

1. Maintain the current tweaking schedule. I think we can all agree this strategy has not worked and is potentially dangerous and should thus be abandoned. 

2. Expedite the current tweaking schedule (e.g. fork every 3-4 months). This would, in my opinion, be unsustainable and thus not feasible. Some services already deem our current 6 month schedule as aggressive. Expediting the schedule may even put us at risk of these services delisting us. We also have to keep in mind a future where the Monero ecosystem grows. The more the ecosystem grows, the more difficult forks will become to coordinate and execute. 

3. Switch to an ASIC friendly algorithm in the next scheduled protocol upgrade. Some people are worried the ASIC (manufacturer) ecosystem has not sufficiently matured yet. Presumably, it will mature further once time passes. Whether waiting is worth the incurred trade-offs is the question though.

4. Perform one more tweak and switch to an ASIC friendly algorithm thereafter. This would allow the current miners to achieve some ROI, which can presumably subsequently be used to invest in ASICs. 

5. Perform `x` more tweaks and switch to an ASIC friendly algorithm thereafter. This seems like an unwise strategy if we deem the tweaks as a failed strategy. 

6. Implement RandomX in October or April (in case it is not ready yet, though it would presumably mean one more tweak). Do not precommit to anything thereafter. I think this strategy would be susceptible to a lot of future controversy to the extent that there will be a contentious debate about the future of the PoW algorithm *if* specialized devices show up for RandomX. 

7. Implement RandomX in October or April (in case it is not ready yet, though it would presumably mean one more tweak). Precommit to an ASIC friendly algorithm after 1.5-2 years. This would enable ASIC manufacturers to already start designing devices. Furthermore, it would give us time to try to find a company that could publish an open-source design. Additionally, this removes future friction and allows us to focus on the protocol. 

8. Explore a GPU centric algorithm. 

9. Explore dual PoW: e.g. RandomX for CPUs, CryptonightR (with tweaks favoring GPUs) for GPUs. As far as I know Zcash investigated harmony mining and deemed it relatively unsafe insofar as that it would significant raise the attack surface and not add that much additional security.

10. [Game Theoretical approach to ASIC resistance (proposed by MoneroCrusher).](https://github.com/monero-project/meta/issues/316#issuecomment-472677985)

11. **Implement RandomX in October. Precommit to switching to an ASIC friendly algorithm (such as SHA3) in case of failure of RandomX. No further tweaks.** // Currently preferred path, as can be seen from [here](https://repo.getmonero.org/monero-project/monero-site/blob/b87354501b6343f9146f331805ddadc45696f728/_posts/2019-03-24-logs-for-the-dev-meeting-held-on-2019-03-24.md).

I'd personally be in favor of option 3, 4, or 7. I have some reservations about RandomX though, which are as follows:

- Fairly new and untested. It thus has not succeeded the test of time.
- Has to be audited, which is going to be costly (and will have to be funded by the community). By contrast, a well-known ASIC friendly algorithm would not require such an audit.
- ~~Increases verification time for nodes, especially for lower end devices. This is predominantly caused by 4GB memory requirement. That is, any device with less than 4GB RAM available will take a large verification performance hit. This, in my opinion, is paradoxical to our ethos where we want everyone to have access to Monero. It would, for instance, making running a node on a Raspberry Pi rather difficult if not completely unfeasible. Lowering the memory requirement significantly would resolve this issue as far as I can see. However, it would also make cryptojacking more attractive.~~ This has been addressed in the new version. Verification time is now approximately similar to earlier versions of CryptoNight. 
- ASIC resistance is basically a function of market cap. If Monero grows a lot, someone will inevitably create a specialized device for it that slowly drives out other miners. This would be significantly less of an issue, however, if we'd precommit to a switch to an ASIC friendly algorithm after say, 1.5-2 years. [Hyc responded to this with:](https://www.reddit.com/r/Monero/comments/azinzk/transcript_of_discussion_between_an_asic_designer/eia2nyi/)

>This is only true up to a limit. Everyone has access to the same transistor technology. Unbundling components that CPUs contain that the ASIC doesn't need can only yield so much power savings. Our pessimistic estimate is that ASICs can be 2x more power efficient than CPUs; best case is only 1.2x. These numbers are based on physics, not market cap.

- These numbers are theoretical and I am not entirely convinced they will hold up in practice / the real world as well. 
- May be met with a lot of opposition for the mining community, potentially causing a split. Same can be said for switching to ASICs I guess. Although, having one more tweak to allow current miners to achieve some ROI would somewhat mitigate this. 

To reiterate, the concept of ASIC resistance, in my opinion, better than ASICs. However, if we cannot viable attain it, the subject should be revisited. Some community members also seem to be venturing into an "at all costs" strategy to preserve ASIC resistance, which is potentially dangerous and may be a net negative for Monero. 


# Discussion History
## SChernykh | 2019-03-12T08:03:07+00:00
9. Explore dual PoW: RandomX for CPUs, CryptonightR (with tweaks favoring GPUs) for GPUs.

## dEBRUYNE-1 | 2019-03-12T08:06:54+00:00
@SChernykh - Will add that. Although, as far as I know Zcash investigated harmony mining and deemed it relatively unsafe insofar as that it would significant raise the attack surface and not add that much additional security.



## SChernykh | 2019-03-12T08:24:21+00:00
We need to re-evaluate what Zcash found. Maybe some new bright ideas will pop up.

GRIN uses dual PoW, so they seem to have resolved these issues.

## emesik | 2019-03-12T08:52:11+00:00
The 4GB memory requirement for RandomX worries me more than ASICs. It means hosting the node would cost me 88% more, and I guess I'm not the only one. That, together with elimination of local lightweight nodes, might be a harder blow to decentralization than allowing custom chips.

The dual PoW option sounds interesting but also opens a Pandora's box of further questions; especially how to keep the ratio of different blocks.

## tevador | 2019-03-12T08:55:16+00:00
@dEBRUYNE-1 

> Fairly new and untested. It thus has not succeeded the test of time.

We are planning to implement it in Wownero first, which should provide some test data.

> Increases verification time for nodes, especially for lower end devices. This is predominantly caused by 4GB memory requirement. That is, any device with less than 4GB RAM available will take a large verification performance hit. This, in my opinion, is paradoxical to our ethos where we want everyone to have access to Monero. It would, for instance, making running a node on a Raspberry Pi rather difficult if not completely unfeasible. Lowering the memory requirement significantly would resolve this issue as far as I can see. However, it would also make cryptojacking more attractive.

The slow verification mode of RandomX is about 3x slower than CNv2 on comparable hardware. CNv4 is also about 3x slower than CNv2 on all non-x86 platforms, including Raspberry Pi (due to missing JIT compiler). So there would be no practical difference between RandomX and CNv4 on ARM hardware.

Additionally, RandomX has a fast verification mode, which is about 7x faster than CryptoNight (but it's only usable in some cases).

> ASIC resistance is basically a function of market cap. If Monero grows a lot, someone will inevitably create a specialized device for it that slowly drives out other miners.

There is a significant difference between a 20x more efficient ASIC (like the recently bricked CNv2 ones) and a 2x more efficient ASIC. The latter has a much lower potential for attacking the network. For example, electricity prices across the world vary by more than a factor of 2, so there are already miners with this kind of advantage.

@emesik

> The 4GB memory requirement for RandomX worries me more than ASICs.

The slow verification mode of RandomX requires only 256 MB.


## SChernykh | 2019-03-12T09:03:08+00:00
2x more efficient ASIC is not as dangerous indeed. Just look at ETH which still stays the most profitable for most GPUs.

## antanst | 2019-03-12T09:20:12+00:00
>  1.Maintain the current tweaking schedule. I think we can all agree this strategy has not worked and is potentially dangerous and should thus be abandoned.

👍 
 
>  2.Expedite the current tweaking schedule (e.g. fork every 3-4 months). This would, in my opinion, be unsustainable and thus not feasible. Some services already deem our current 6 month schedule as aggressive. Expediting the schedule may even put us at risk of these services delisting us. We also have to keep in mind a future where the Monero ecosystem grows. The more the ecosystem grows, the more difficult forks will become to coordinate and execute.

100% agreed. This plan is infeasible, will damage Monero in the long term, and furthermore there's absolutely no guarantee that 3-4 months will be enough, if the price rises sufficiently. ASIC manufacturers are restless and always improving their methods. What if after a year or two we notice ASICs again, will we switch to a monthly PoW upgrade?

I'm actually quite astonished on the fact that this plan is even under consideration, does somebody really think that users/exchanges would like to update their software every 3 months, with a potential Ledger/exchange bug in between? **Users will either leave or switch to custodian wallets, leaving to somebody else to deal with the mess of running a full node/wallet; at this point we will ponder whether our "ASIC resistance battles" have led us to a far more centralized situation.**
 
>  3.Switch to an ASIC friendly algorithm in the next scheduled protocol upgrade. Some people are worried the ASIC (manufacturer) ecosystem has not sufficiently matured yet. Presumably, it will mature further once time passes. Whether waiting is worth the incurred trade-offs is the question though.

If ones make the assumption that we want ASICs to be introduced in Monero in an as fair way as possible, and avoiding the  "early-stage-monopoly" effect as much as possible, 3, 4 and 5 are not optimal:

- In case of 3, it's not enough time to announce the ASIC algorithm to give everybody a fair chance of building one.
- In case of 4 & 5, the miner ROI will only help the current ASIC miners that were already capable of producing an ASIC very fast.
- All cases will suffer from the "early-stage-monopoly" effect: Once the abrupt switch to 100% ASIC mining is made, the first to make an ASIC will have much more than 50% of mining power for a while.
- And, as you said, tweaks have already proved to be a failed strategy. No reason to plan them for the long term.

>  6.Implement RandomX in October or April (in case it is not ready yet, though it would presumably mean one more tweak). Do not precommit to anything thereafter. I think this strategy would be susceptible to a lot of future controversy to the extent that there will be a contentious debate about the future of the PoW algorithm _if_ specialized devices show up for RandomX.

I believe that will ultimately mean throwing away the big time window RandomX would've given us. The question is not _if_ someone gains an edge, it's when and how. After a year, or two, we'll be back to discussing frequent PoW changes again. Back to zero.

> 
>  7.Implement RandomX in October or April (in case it is not ready yet, though it would presumably mean one more tweak). Precommit to an ASIC friendly algorithm after 1.5-2 years. This would enable ASIC manufacturers to already start designing devices. Furthermore, it would give us time to try to find a company that could publish an open-source design. Additionally, this removes future friction and allows us to focus on the protocol.

Assuming that RandomX works and is tested for a while, that's the most sensible way to go for the long term, and the only way to take advantage of the (hopefully larger) time window that RandomX will give us if/when ready. Ideally, this time window will be used to gradually introduce the ASIC friendly PoW share to the network a-la Grin.

> I'd personally be in favor of option 3, 4, or 7. I have some reservations about RandomX though, which are as follows:
> <snip>

Many interesting points. I would gladly pitch in for a RandomX audit, and I suspect I'm not alone. If RandomX does not prove to be stable/optimal/whatever, things are more difficult; maybe we can make a few tweaks, all while precommiting to introducing ASICs gradually? Would something along these lines be sensible?

```
<pulls numbers out of ass>
Next PoW tweak (6m) , 10% SHA3
Next PoW tweak (1y), 45% SHA3
Next (and final) PoW tweak, 100% SHA3
```

## antanst | 2019-03-12T09:22:08+00:00
> GRIN uses dual PoW, so they seem to have resolved these issues.

Grin has resolved those issues not because they just use dual PoW, but because their (temporary) dual PoW system serves as only as a smooth and fair introduction to ASICs for the long term. To their credit, they immediatelly started thinking about this once it was clear that a Cuckatoo ASIC would be inevitable.

## emesik | 2019-03-12T09:46:35+00:00
> The slow verification mode of RandomX requires only 256 MB.

Sounds better.

How about committing to be ASIC-friendly with the block when tail emission kicks in? Approaching that goal in GRIN-like manner looks sensible, as we could watch the ASIC development during the transition time, instead of plunging into new world as proposed in point 7.

Of course, ASIC-dominated network in tail emission era brings different dangers than in mining era. Like purposeful withholding hashpower to trick people into higher fees. But there's plenty of time to spend on preparations for that moment, instead of adding another tweaks to PoW.

## umma08 | 2019-03-12T09:56:01+00:00
>7. Implement RandomX in October or April (in case it is not ready yet, though it would presumably mean one more tweak). Precommit to an ASIC friendly algorithm after 1.5-2 years. This would enable ASIC manufacturers to already start designing devices. Furthermore, it would give us time to try to find a company that could publish an open-source design. Additionally, this removes future friction and allows us to focus on the protocol.

i would be inclined to support this. with concerted effort (in the form of a funded workgroup) to find a manufacturer that would design and test an open hardware design.

## dEBRUYNE-1 | 2019-03-12T10:03:25+00:00
@tevador 

>We are planning to implement it in Wownero first, which should provide some test data.

That will certainly improve the situation, but we can't deny the concept is relatively new and largely untested. 

>So there would be no practical difference between RandomX and CNv4

The difference is that CNv4 is meant as temporary stop gap, whereas RandomX is meant as a long-term solution. Furthermore, as far as I know, enabling JIT is still possible for ARMv8, whereas ARMv8 devices would take a large verification performance hit with RandomX. We also have to account for other lower end 64-bit devices. 

>There is a significant difference between a 20x more efficient ASIC (like the recently bricked CNv2 ones) and a 2x more efficient ASIC.

I agree, but as I said, I have my doubts about whether the theoretically claimed 2x will work out in practice. 

## dEBRUYNE-1 | 2019-03-12T10:04:13+00:00
>I'm actually quite astonished on the fact that this plan is even under consideration

I think there is little support for that option, but as long as it remains an option we have to list it in my opinion. 

## iamsmooth | 2019-03-12T10:48:09+00:00
> There is a significant difference between a 20x more efficient ASIC (like the recently bricked CNv2 ones) and a 2x more efficient ASIC

Less than you might think. When joining a network at break even equilibrium, an ASIC with 20x efficiency gain has a 95% profit margin. At 2x, the profit margin drops to 50%. So the profit is about half, and the break even is almost twice as long. This is certainly significant, but not the 10x one might infer from the 20x vs 2x comparison.

The way the math works out the minimum efficiency improvement is far more significant than the maximum in these comparisons. As long as there is _any_ significant efficiency gain and sufficient revenue, ASICs become feasible. The difference in this equation between 20x and 2x is only a 2x increase in the XMR price.


## fluffypony | 2019-03-12T10:52:37+00:00
Just copying a comment I made on Reddit, to make my position clear:

I've said from the beginning that ASIC resistance is ultimately futile. As Monero grows bigger, ASIC manufacturers will get smarter and will indeed start to co-opt developers or slip their own developers into the fold. We have no way of telling if our reliance on vtnerd making changes at the last minute is at all meaningful.

There's also the very real risk of high-end FPGAs and similar (suggest you look at what NextSilicon and XTend Online are doing) which will make our changes meaningless.

I agree that geographical decentralisation is a desirable trait. So one way we can solve for this is by (1) choosing an algorithm where we can dominate the mining capacity; (2) choosing an algorithm that is easy to ASIC, is general purpose, and is easy to validate - I suggest SHA3; and (3) setting that fork date right now so that ASIC manufacturers have a few years to get their act together. By the time we go live there should be a plethora of ASICs available, and if it's something general purpose like SHA3 I can imagine motherboards building it in, CPU manufacturers adding support via an instruction set, and so on. This also gives existing miners enough time to sunset their hardware and make a profit on it, whilst pricing in new hardware, knowing that there's a time limit on how long they'll be able to run that hardware for.

We started this as a fight against Bitmain, against a single known-bad manufacturer dominating the mining space. I fully support that, but I do not support a futile attempt at evading ASICs forever, as that is impossible.

## iamsmooth | 2019-03-12T11:01:57+00:00
> setting that fork date right now so that ASIC manufacturers have a few years to get their act together

A few years means a few years of uncertainty as to the state of the network and having it get monopolized by secret ASICs, including potentially malicious ones (we seem to have lucked out this time, in that the apparent ASIC builder didn't feel like attacking the network when they controlled 80% of the hash rate, but we can't assume we will always be lucky).

RandomX might work out for a few years, in which case great. But it might not. What do we do if RandomX goes live and there are ASICs on the network within months? Continue a tweaking strategy that is actually working against the security of the network? Speed up the tweaking cycle, to which there are valid objections in terms of stability and frequent forks? Etc.

Given that we don't have a lot of good options left, I'm not sure a firm plan to wait a few years is really sensible.

To be clear on this, I would be perfectly happy waiting a few years _if_ what we do over the next few years actually works better than what we have been doing for the past year. Otherwise, I see dragging out the current state for another few years to be bordering on suicidal.

## fluffypony | 2019-03-12T11:06:55+00:00
@iamsmooth the alternative is to switch to SHA3 in the October fork, or to switch to RandomX in October followed by SHA3 in April 2020. This leads to two questions:

1. Is 6 months / 12 months enough time for existing miners to be profitable enough that they're fine with it?

2. Is 6 months / 12 months enough time for ASIC manufacturers to spin up and produce competitive miners?

## iamsmooth | 2019-03-12T11:15:01+00:00
@fluffypony I'm not necessarily saying to switch at a particular time, but I'm saying that if RandomX does not work out, then we must do something else, rather than committing to stick with a failed strategy for some set period of time (say, three years).

I don't believe we can make any promises to existing miners any more than we can make promises to the community of "egalitarian mining". If it isn't feasible to accomplish (without putting the network at great risk), then it simply _must_ be dropped out of necessity. It is a shame if this happens, but it is more of a shame if real world conditions require it, yet we deny that reality and make bad decisions as a result.


## ctrlshp | 2019-03-12T11:31:44+00:00
While there seems to be consensus on this conversation's primary goal being to find a way to free precious dev brain cycles from having to maintain PoW algorithm ASICs/FPGAs-resistance, thus embracing ASICs/FPGAs in the long run, the debate seems to rather be about how this is going to be done or transitionned into. And even then, regardless of the transition strategy (RandomX, etc.), I don't see two points of view being expressed here on the ASIC-embracing algorithm to be transitioned _into_, only one : that ultimately, the algorithm should be general/useful enough to ASAP 1) be easily implemented by large consumer motherboard/CPU manufacturers 2) be useful as to have the research in acceleration and optimization benefit the whole crypto ecosystem, not just the miners, and if possible, Monero specifically. And still, SHA3 is the only option being mentionned here, so is there consensus on that too or are there other options being investigated ? Should this conversation be divided into two indepentent ones: the first about the transition algorithm (RandomX, etc.) and another one about the algorithm that will ultimately and permanently be transitioned into (SHA3, etc.) ?

## fluffypony | 2019-03-12T11:41:40+00:00
@ctrlshp there aren't a lot of options when it comes to PoW algorithms that are (1) lightweight, (2) useful in other things, (3) proven, (4) not used in any other major cryptocurrency. I'm VERY keen on hearing suggestions from the MRL!

## ctrlshp | 2019-03-12T11:59:39+00:00
@fluffypony My point is similar to yours: I feel that the "ultimate" algo(s) is/are on a different timeframe than the "transition" one(s) and that by forking the conversation, we will give enough time to find a "ultimate" algo as groundbreaking as RandomX as a "transition" algo. I don't know, maybe BigNumber or ECC primitive arithmetics (mod, etc.) ? I'm just saying this on top of my head as examples of where this conversation should allow itself to thoroughly investigate, with the MRL and anybody who has an idea. I might be wrong too: maybe that it doesn't matter and SHA3 could be implemented first and then  there could be a permanently ongoing conversation on its eventual replacement. I don't kow for sure, I'm just suggesting. And I do think that "officially" taking the matter before the MRL and giving them enough time to think/research it through is a strict minimun.

**EDIT**: I just realized that I'm not assuming that it has to be a (known) hashing algo and that might not be a "natural" way to think about it. That should, IMHO, also be part of the conversation. I know that if it is not a hashing function per se, it breaks the "workflow", but can it be excluded now ? I don't know.

## fluffypony | 2019-03-12T12:16:49+00:00
@ctrlshp if we're looking for an ASIC-friendly algorithm I don't think we'd want to design something, we're not a group of seasoned cryptographers who should be doing so (see: Iota's hash function fail). We'd want something that has existed for some time, has strong pre-image resistance, and is unencumbered. SHA3 is specifically designed to be ASIC friendly, per the original paper:

> Its throughput for a given circuit area is an order of magnitude higher than SHA-2 or any of the SHA-3 finalists. And if you care beyond plain speed, note that it also consumes much less energy per bit. In this sense, Keccak is a green cryptographic primitive.

## SChernykh | 2019-03-12T12:19:03+00:00
I would say that throughput/energy per bit (aka absolute hashrate or hashrate per watt) are not important. What's important is that it must be easy to implement in ASIC, so easy that even a startup company could do it.

## antanst | 2019-03-12T12:22:46+00:00
> RandomX might work out for a few years, in which case great. But it might not. What do we do if RandomX goes live and there are ASICs on the network within months? Continue a tweaking strategy that is actually working against the security of the network? Speed up the tweaking cycle, to which there are valid objections in terms of stability and frequent forks? Etc.

If this happens, we'd be in a hole that we've dug ourselves into. So the question should be, what strategy will get us out of this hole in the long term? Not keep digging, that' for sure. If miners get an edge earlier than expected, which is entirely plausible, their reign in RandomX will end soon anyway. It's risky, sure, but it will be a one time thing instead of something that has a chance to happen every 6 months.

## ctrlshp | 2019-03-12T12:27:09+00:00
Guys, you are way ahead of me. I'm merely saying that for now, there should be two conversation spaces. Because the two conversations are independent and if done in the same space, they will phagocytize each other and confuse everybody. Can we do that now and then talk ?

## SamsungGalaxyPlayer | 2019-03-12T14:04:04+00:00
@SChernykh from what I can tell, GRIN did not resolve any of these issues. They had committed to a dual-PoW before Zcash began its testing. I personally do not feel confident in a dual-PoW _unless_ new research comes out suggesting it can be safer. Until then, I think we should consider it off the table for the reasons the Zcash team presented.

## dginovker | 2019-03-12T14:15:45+00:00
If one thing is certain about switching to an ASIC-friendly PoW, we should NOT choose one where our global hashrate is a minority (i.e. SHA256). This risks any sufficiently sized pool from the larger network to launch a 51 at any time, and defeats the decentralization aspect from a different angle.

## JustFranz | 2019-03-12T14:55:33+00:00
There are 2 separate issues. First, the quest for an ASIC inefficient POW - RandomX and what that means for the need to tweak the algorithm for ASIC bricking. How good is RandomX really?

Second, picking an ASIC friendly algo (which one?) and the conditions that need to be met for its orderly adoption. Are we OK with 1 or 2 companies mining Monero? Are we OK with them mining in china? Are we OK with an export ban on the ASICs? Mandatory KYC for ASIC buying? Import ban and confiscation in some countries?

What do we want the Monero ASIC manufacturing and mining landscape to look like?

There is a clear course of action for RandomX and a success condition, sort of. I don't know what success looks like for the ASIC route, seems like the current failure condition to me.

## dEBRUYNE-1 | 2019-03-12T15:07:51+00:00
One more option suggested by hyc on IRC. 

>Implement RandomX in October or April (in case it is not ready yet, though it would presumably mean one more tweak). Precommit to an ASIC friendly algorithm once ASICs appear on the network.

Trade-offs (personal addition):
- How do we reliably detect ASICs? 
- There will be contention in the community whether the new hashrate is coming from genuine miners or ASICs (remember the discussion threads when the hashrate started to increase recently? A lot of people were unconvinced it were ASICs). 
- Limited time for ASIC manufacturer to design and develop an ASIC. 
- The entity with the secret ASICs may temporarily reach a majority hashrate. 

## Gingeropolous | 2019-03-12T15:29:59+00:00
Firstly, I am disapointed to see what I view as myopicism, fatalism, and incongruence in the current discussion regarding the Monero PoW.

I guess I'll start with the incongruence. I know many people came to Monero for many different reasons, so its impossible to state what everyone thinks about this. However, a common starting point for all of us is the cryptonote whitepaper. And yes, there is plenty to question about the motives of
cryptonote, considering that bytecoin etc. was a bunch of scammers. Despite this visceral birthing of our beloved Monero, the people that got into Monero connected with the concepts presented in that paper.

So its important to note that even in the whitepaper, it is presented that "Our primary  goal is  to  close  the  gap  between  CPU  (majority)  and GPU/FPGA/ASIC  (minority)  miners." They go on to further expound that "It is appropriate  that  some  users  can  have  a  certain  advantage  over others,  but  their  investments should grow at least linearly with the power. More generally, producing special-purpose devices has to be as less profitable as possible".

Therefore, I view the notion that Monero will switch to an ASIC-only PoW as completely incongruent with what can be considered the gestalt of Monero.

I will then move to fatalism. Some view it as an inevitability that the only way for a PoW network to exist when the network has grown to a significant size is through ASICs.

And finally, myopicism. Being short-sighted. We don't know whats around the corner, and everyone seems to be talking about 1-2 year timelines.

OK, well, I guess framing this ramble in those three things wasn't ideal, because I want to get into some scenarios. ( And also using sublime text, because I apparently haven't install a spellcheck plugin. )

Imagine we somehow swallow this proposed inevitability that ASICs are the only way. We switch to SHA3. A handful of manufacturers are onboard. Everythings going grand for, I dunno, 2 years. And then.

Boom.

The hashrate quadruples. Not only does some entity have twice the network hashrate. They have twice the network hashrate of twice the the network hashrate.

What happens then? Do we just go forward with "Well.... uh, the network is clearly pwned, but... lets build some more ASICs I guess"

Because at that point, we're walled in. We're an ASIC coin, and everyones bunkered in. Changing the PoW at this point is as much as an option as is to choose to breathe air.

And then to top it off, nations start blocking shipments of SHA3 asics. Hrmmm. Whats happening? Well, the code is ossified and no one will change PoW so there goes any hope of cryptocurrencies doing anything to change the world.

I mean, the problem with ASIC manufacturers is they are entirely profit driven. If someone can prove otherwise, great. And do you know what could be the most profitable for an ASIC manufacturer? Providing control of the chain to an adversary.

Lets compare this the scenario where we settle on RandomX, or some variant of RandomX that we figure out over the next year or so. Monero network hashrate quadruples. People wanting to defend the network can rent server time from, yah know, anywhere. People wanting to get in can buy computers from, yah know, anywhere. People wanting to go all out and build their own ASICs can, yah know,
go ahead and do that.

I basically just can't get it through my head how a tool (cryptocurrency) that is supposed to be permissionless can have this huge gatekeeping mechanism of hardware production and distribution.

I mean, the revolution of cryptocurrency is that it enables monetary liberation dependent on ones ability to receive and transmit data. Walls for data are hard to build.

And I guess here its important to state that I feel mining decentralization is important not for some egalitarian rewards notion. I mean, yeah thats great, everyone should be able to get rewarded for contributing to the network if they want to. No, decentralized mining is more important for block creation
decentralization. As stated elsewhere, if we're moving towards a network with centralized block creation, we might as well just turn into a scamcoin and get the developers to sign the blocks.

Despite my strong stance against embracing ASICs, I do recognize that specialized hardware can be made to perform operations faster than general purpose hardware. However, I wish to propose a concept that may be more in line with the original concepts that we greater fools found attractive.

ASIC equivalence.

I ask the reader to ponder the possibility that RandomX performs really well, and that an ASIC developed for it is within 1 to 2x more efficient. Is this any different than AMD or NVIDIA making a new GPU in todays market? Perhaps there are some differences - an ASIC manufacturer won't have the same infrastructure to distribute as effectively as a GPU manufacturer. And there may not be an incentive to distribute, as the Monero mining market is miniscule compared to general purpose hardware.

However, now the ASIC manufacturer is directly competing with AMD, Intel, and NVIDIA. They will have to continue to increase their ASICs performance to be more efficient than whatever the leading computational developers are creating. This market force may incentivize them to distribute their hardware, or at the very least get to distribution more quickly than they would have otherwise.

And there are factors that can increase development costs for ASICs. For instance, a growing data size (the 4 gb thing) could force ASIC developers to include expandable memory, so the end user could upgrade their memory as time goes on.

Additionally, RandomX could lead to commoditization faster than an ASIC friendly PoW, as absurd as that may seem. Motherboard developers or processor developers could create RandomX co-processors. Presumably, AMD and Intel already *make* CPUs.... so they are already making hardware that is a bloated RandomX ASIC. they could probably make RandomX-ASICs at some ridiculous 
percentage of the cost of a CPU, and get themselves into the cryptocurrency mining market.

So in conclusion, I think that if RandomX works, we should stick with it. I think we also need to consider a reality of ASIC equivalence, where a RandomX ASIC does provide a competitive advantage, but it is an advantage that is market appropriate and is exposed to the existing market dynamics. I think we
need to focus on our network remaining borderless, and to do so, consider the hard truth that critical components may not exist in hardware-only forms.

Now is not the time to throw in the towel. 

For these reasons and many others stated elsewhere, and as lead troll developer of Monero, I hereby proclaim that Monero continue the fight against ASIC centralization and forever speculate bananas.

(edited to undo manual 80 char lines)

## fluffypony | 2019-03-12T15:32:31+00:00
@dginovker totally agreed - SHA3 is a good candidate for that, as the only coins using it are MaxCoin, SmartCash, and CreativeCoin.

@JustFranz the outcome would ideally be something like Bitcoin, where there are a host of manufacturers, and mining farms are [geographically widespread](https://cointelegraph.com/news/top-five-biggest-crypto-mining-areas-which-farms-are-pushing-forward-the-new-gold-rush). If we choose an algorithm that is WIDELY used on the Internet then there is the same chance of export bans and mandatory KYC as there is for GPUs. There's also a high likelihood that chip manufacturers will add support for the algorithm via an instruction set.

The alternative is that we keep coming up with "random tweaks" every 3 months, and ASIC manufacturers just co-opt a bunch of devs and/or insert their own devs who ingratiate themselves. The network becomes highly unstable, services like MyMonero and exchanges struggle to keep up with the changes, and people stop using Monero. We're fighting a losing game.

@dEBRUYNE-1 any strategy we come up can be gamed. ASIC manufacturers will just introduce it slowly, on public pools, spread out across individual "miners" so that it appears to just be GPUs. If we're going to precommit we need to precommit to a date so that ASIC manufacturers can work towards that. We need to stop being reactive, and be proactive instead.

## SChernykh | 2019-03-12T15:35:56+00:00
@dEBRUYNE-1 why not add:

10. Implement RandomX and proclaim it as the final PoW. If ASICs emerge, so be it, because they won't be much faster anyway and will be outperformed by future CPUs as @Gingeropolous said.

## dEBRUYNE-1 | 2019-03-12T15:40:38+00:00
>@dEBRUYNE-1 any strategy we come up can be gamed. ASIC manufacturers will just introduce it slowly, on public pools, spread out across individual "miners" so that it appears to just be GPUs. 

That is indeed a large drawback. Kind of falls under the "How do we reliably detect ASICs?" trade-off I listed.

>If we're going to precommit we need to precommit to a date so that ASIC manufacturers can work towards that. We need to stop being reactive, and be proactive instead.

Agree.

---------------------

>why not add

Sure, will add. I don't agree with "they won't be much faster anyway" though. As I said before:

>These numbers are theoretical and I am not entirely convinced they will hold up in practice / the real world as well.


## robodan918 | 2019-03-12T15:44:31+00:00
Committing to ASICs is capitulating to China & centralised wealth creation

Why would ASIC manufacturers EVER sell their hardware until they've mined all they can with them, until difficulty goes up enough to make their projected earnings less than the cost of the hardware+electricity?

From a game-theory perspective, the right decision is to shadowmine to maximise centralised wealth creation, then sell the hardware 'as new' when the profit projections switch from net positive to net negative, thus decentralising losses. If this sounds familiar, it's because that's basically what is happening in all modern banking and finance. Gains are centralised / privatized. Losses are decentralised / socialized.

This is the question that is at the heart of this debate: do we want to perpetuate a broken system that benefits the few, or (continue) to build a new one where the majority can participate and gain? You can tell which side I'm on, and which side the majority of the community (technical, miners, hodlers) are on.

For monero to last 5, 10, 20 years or more it must remain decentralised in wealth creation/mining, and (arguably, therefore) in wealth distribution

## SamsungGalaxyPlayer | 2019-03-12T15:53:45+00:00
@Gingeropolous makes a good point that if we move to ASIC-friendly, there probably isn't any going back. Monero's reputation will most likely be irreparably harmed if we expend a lot of effort working with manufacturers to make sure that several ASICs are available, only to switch to the new algorithm.

But if something goes awry, we don't have good short-term options. Are we going to brick the ASICs that we worked with the good actors to support? Do we then fund a new community design, knowing it will take months for R&D?

Sticking to a CPU-friendly algorithm gives Monero more flexibility. We can change the algorithm to harm any bad actors without severe community consequences.

I don't think our goal needs to be able to compete with all economies of scale. People can do this today by purchasing bulk GPUs or CPUs and cheap power. While mining is supposed to be boring, the market isn't completely efficient since there is a lot of volatility. Monero's price isn't known a year from now, so ASIC creators can't invest without sizeable risk. If we take these volatility risks into account, even 2x seems like a hard sell, at least for some profit-driven actor attempting to control the entire network. Even if they exist, the network can still be healthy. And if it's a malicious actor, they will have less relative advantage to normal hardware.

## el00ruobuob | 2019-03-12T16:04:29+00:00
I totally agree with @Gingeropolous  
He got all my concerns explained in a single post.

## moracha | 2019-03-12T16:04:52+00:00
@fluffypony Aren't FPGAs already rampant on SHA-3? I know this has been discussed heavily among the coins that have implemented Keccak. Is it a smart move to put the safety of Monero's network into the hands of FPGA owners? Is it not antithetical to Monero's original intention that one would need to acquire a $5,000 piece of equipment and pay a developer for a private bitstream, just for the opportunity to contribute to Monero's decentralization?

## fluffypony | 2019-03-12T16:14:02+00:00
@Gingeropolous I really don't think we should EVER claim "but the whitepaper says" unless we want a Bitcoin SV scenario. Let's PLEASE put that aside. We absolutely DO NOT need to do what the whitepaper says. There are multiple claims in the whitepaper that Monero has never had from its outset, and multiple claims that no longer apply to Monero.

I hear your concerns about possible outcomes, but it occurs to me that we'd already have seen this happen with Bitcoin ASICs in Venezuela and other parts of the world if this was a concern. I am also deeply concerned that we are largely unqualified to be designing our own hashing algorithms, and we're going to end up with egg on our proverbial faces.

If we end up committing to RandomX and then ASIC manufacturers are able to get significantly higher performance improvements than we expect, that is when "Monero's reputation will be irreparably harmed", to quote @SamsungGalaxyPlayer. Do we have any clue if RandomX is strongly resistant to pre-image attacks? I feel like we're playing in a pool reserved for very experienced cryptographers, and it's not going to end well. I'm concerned that the only reason we haven't had an incident thus far is because we change things too often for anyone to really be bothered to analyse the algorithms.

@moracha doesn't matter if they are, none of those coins are worth enough for an ASIC to be made. If ASIC manufacturers have a two year lead they will produce ASICs that are orders of magnitude better than existing ASICs. As mentioned, SHA3 is specifically designed to be easy to ASIC.

## dEBRUYNE-1 | 2019-03-12T16:28:29+00:00
>We can change the algorithm to harm any bad actors without severe community consequences.

I don't think we can realistically execute this strategy. You're essentially arguing for further tweaks, which has shown to be a rather futile and potentially dangerous strategy. 

> even 2x seems like a hard sell

To reiterate, I have my doubts about whether the theoretically claimed 2x will work out in practice.

>Even if they exist, the network can still be healthy.

Only for so long though. A miner with as significant advantage will eventually push out most other miners. 

## SamsungGalaxyPlayer | 2019-03-12T16:30:03+00:00
fwiw I also agree that we don't need to do something just because it's in the whitepaper. That's dangerous. However, I agree that CPU-friendly mining is an important part of the Monero ethos. This can change, but I understand why people (often myself included) like to hear about solutions that attempt to maintain this property.

## tevador | 2019-03-12T16:31:03+00:00
@iamsmooth 
> Less than you might think. When joining a network at break even equilibrium, an ASIC with 20x efficiency gain has a 95% profit margin. At 2x, the profit margin drops to 50%. So the profit is about half, and the break even is almost twice as long. This is certainly significant, but not the 10x one might infer from the 20x vs 2x comparison.

It's not so simple, you have to also include the R&D costs and the manufacturing cost per device. Price of electricity will be the smallest expense of these short ASIC runs.

@fluffypony 
> Do we have any clue if RandomX is strongly resistant to pre-image attacks?

RandomX is not a hashing algorithm. Internally, it uses a cryptographically secure hashing function (Blake2b), so unless that is broken, there is no doubt about pre-image resistance.
It's important to distinguish between the *work* and the *proof* that together make up a PoW algorithm. This was explained by hyc [here](https://www.reddit.com/r/Monero/comments/8bshrx/what_we_need_to_know_about_proof_of_work_pow/). RandomX is only the "work" part. The proof itself is given by a cryptographically secure hash.



## HuskarK | 2019-03-12T16:32:16+00:00
Hi there, sorry if I disturb. What if we try to think about the POW not as a formula, but as a task for AI. Like for exsample: win a game in GO or solve a riddle in a virtual world... 

## antanst | 2019-03-12T16:42:19+00:00
> SHA3 is a good candidate for that, as the only coins using it are MaxCoin, SmartCash, and CreativeCoin.

Pretty interesting. SHA3 looks like an ideal ASIC-friendly PoW. Standardized, high security margins, much more efficient than BLAKE2, Skein etc. in hardware. And not picked by a coin with substancial market cap, yet. What more to ask?

## Gingeropolous | 2019-03-12T17:04:28+00:00
@fluffypony , yeah I did not mean to do a "but the white paper said" thing. I tried to couch it appropriately, I guess I failed. And I don't want to do that either, because of the whole bitcoin SV type thing. 

I guess my point was is that what held 5 years ago also holds now. That this discussion is not new. Things, unfortunately, really haven't changed. There's no ASICs at my local bestbuy, there's not a healthy market of ASIC competition, etc. ASICS, IMO, have failed the cryptocurrency movement. 

It's true, we can say Monero has succeeded where others have failed (a functioning fungible currency network, shoe-string budget bootstrap development)... I just have real reservations about Monero's ability to single-handedly change the ASIC landscape. I feel that the machinery is different between these two things.

Maybe I'm wrong. Maybe the greater fool mentality can win in this arena as well. If we choose to go down this road, I sure hope it does. 

> I hear your concerns about possible outcomes, but it occurs to me that we'd already have seen this happen with Bitcoin ASICs in Venezuela and other parts of the world if this was a concern. 

I disagree. I think Monero creates a different scenario than Bitcoin.  

>  I am also deeply concerned that we are largely unqualified to be designing our own hashing algorithms, and we're going to end up with egg on our proverbial faces.

I'll admit that I'm no expert, but as stated by people that may be more expert than me, randomx doesn't fiddle much with cryptography. Though to your point, I agree that a lot more resources should be put towards RandomX development if this path is chosen. 

## dEBRUYNE-1 | 2019-03-12T17:14:45+00:00
>Things, unfortunately, really haven't changed.

I think that is myopic to say. Whilst ASICs have not been commoditized yet, the ASIC (manufacturer) ecosystem has vastly improved in comparison to a few years ago. A variety of manufacturers now exists including manufacturers not based in China. 

## Gingeropolous | 2019-03-12T17:17:27+00:00
> I think that is myopic to say. Whilst ASICs have not been commoditized yet, the ASIC (manufacturer) ecosystem has vastly improved in comparison to a few years ago. A variety of manufacturers now exists including manufacturers not based in China.

Has a single one of them ever put the network before their profits?

## dEBRUYNE-1 | 2019-03-12T17:25:00+00:00
What constitutes putting the network before their profits? 

## antanst | 2019-03-12T17:26:42+00:00
> Has a single one of them ever put the network before their profits?

PoW works because it gives economic incentives for actors to secure the chain and to compete while doing so. If cryptocurrencies relied on people's good will to burn electricity out of their pockets "for the good of the network", the whole thing would have died pretty soon, years ago.

## rw258906 | 2019-03-12T17:40:00+00:00
I have a few questions, I mentioned one on reddit, but maybe I can get a better answer here, I am sure there are good reasons you guys aren't discussing these but perhaps you could make it clear why these ideas wouldn't work. 

1) Why not do 2 algos 1st randomX and the 2nd ProgPow. While neither might be a perfect solution, having both and updating them from time to time seems like it would make it pretty hard to control 80%+ of the hashpower? 

2) If Monero were to use an algorithm designed to be optimized for specific consumer hardware such as RandomX or ProgPow, wouldn't it be easy to create an ASIC detection system using the profitability of the target hardware. For instance, instead of adjusting the algo every 6 months no matter what, why couldn't Monero adjust the algo every 6 months **if, and only if, they become unprofitable on their target hardware at $0.10/kWh**?

## hyc | 2019-03-12T17:40:36+00:00
@antanst the fact that Bitcoin survived its early years when it wasn't even worth 1 cent proves that statement false.

## Gingeropolous | 2019-03-12T17:42:27+00:00
> What constitutes putting the network before their profits?

I guess focusing on distribution of their product. Maybe making products that did more than just hash... like store the chain, speed up some other parts of the code, anything to actually support the infrastructure as opposed to just milk it. 

> If cryptocurrencies relied on people's good will to burn electricity out of their pockets "for the good of the network", the whole thing would have died pretty soon, years ago.

I guess all of the developers that aren't paid for their work on monero are just stupid then? Its OK to be goodwill driven for one aspect of network security, but not the other? And the first 3 years of monero mining was an illusion?

I gotta admit. I'm starting to feel this again

https://media.giphy.com/media/NPyHgTkMStCXC/giphy.gif

Call up Gordon Gekko. After 5 years of toiling, we've once against discovered that greed is good. 

I'm sorry. I've derailed this discussion. Lets get professional again. We got Billy in Marketing coming up with a whizbang promotion for Monero-sanctioned ASICs yesserreee boy, these bad boys are gonna be lickity split top-o-the line. Airdropped from moon hellicopters they'll be. 100% market driven, no hopium ever. Realistic, chart-proven market saturation ballistic humdingers they'll be. 

I think I'm sleep deprived. 

## dEBRUYNE-1 | 2019-03-12T17:48:50+00:00
>opposed to just milk it.

So you'd argue the current GPU and CPU miners are "just milking it" as well? 

## el00ruobuob | 2019-03-12T18:29:40+00:00
I guess, it's not the miners who milk it, but the manufacturers. If one creates a CPU miner and sell this software, it's milking.

## antanst | 2019-03-12T18:31:49+00:00
> @antanst the fact that Bitcoin survived its early years when it wasn't even worth 1 cent proves that statement false.

Not quite. The primary reason Bitcoin didn't have any huge reorg incidents or other attacks at that period is that nobody knew it, or nobody that knew it deemed worthy to attack it *precisely* because it was almost worthless. The network itself was incredibly vulnerable back then when just a few people were mining with their CPUs.

## el00ruobuob | 2019-03-12T18:36:45+00:00
@antanst I don't catch how it's linked to your statement who @hyc talked about, could you elaborate on it?

## antanst | 2019-03-12T18:45:18+00:00
@el00ruobuob I'm arguing that we can't compare the current situation to the very early days of Bitcoin that @hyc mentions, where Bitcoin was obscure and worthless enough not to attract malicious actors, despite being much more vulnerable due to the very small number of people mining it.

## Gingeropolous | 2019-03-12T18:45:20+00:00
> So you'd argue the current GPU and CPU miners are "just milking it" as well?

Some do, some don't. 

I don't see where your going though. An ASIC manufacturer is creating and building something. As @el00ruobuob just posted, its different. 

I mean, the problem is that the development space for mining is mostly populated by profiteers. There has been so little development of anything related to block generation in any cryptocurrency that its actually concerning. Its perhaps the *fundamental* aspect of this entire thing, and from top to bottom people are throwing in the towel. I mean, pooled mining? Still? Without co-operative generation of the block templates? 

No one talks about it. No one bats an eye that in most of these networks, there are 4-10 block producers. Everyone just says "well, if the pool operators starts publishing bad blocks, then the miners will move."

Except if the ASIC comes configured to only work on registered pools. But why would they do that? Well, why wouldn't they? They'd make more profit if they force their products to work on their pools, and greed is good, so... logic + logic = logic!

This problem is more than just the mining PoW, and no one cares. So, I guess I shouldn't either, right?

I think I want to sum up my distress with this. Creating an ASIC-dominated network feels like creating a backdoor. A weakness left in the code because it provides a benefit for something or other. Yeah, sure, it might not be a strict interpretation of backdoor but its something like that. And backdoors are bad, right? Yes, working on our own PoW may also create a backdoor. But that backdoor is still relatively under our control. Once the ASIC door is opened, I don't know how it can be closed. 

## hyc | 2019-03-12T18:50:16+00:00
@antanst to be clear
> If cryptocurrencies relied on people's good will to burn electricity out of their pockets "for the good of the network", the whole thing would have died pretty soon, years ago.

Clearly this statement is false.

## JohnnyMnemonic22 | 2019-03-12T19:28:35+00:00
I see lots of discussion about the technical consequences of certain decisions, but little of the social consequences. @fluffypony, if you don’t want a Bitcoin SV scenario, it may be wise to not forget what brought us together in the first place. I 100% disagree that we should not mention the whitepaper. Monero is a community first, NOT a technology first. We have a fiduciary responsibility to maintain the principles that created this community, and the whitepaper is our indenture.

It cannot be understated that Monero has an IDENTITY, and that is way more interesting and special than whatever the latest research or technical breakthrough happens to be (not that those things aren’t important, but they’re a result of who we are). The network can completely fall apart, but we will still be here because of what we stand for. But if we abandon our principles, it won’t matter how perfect or secure the network is. We will have failed in our trusteeship, and the community will be a hollow shell of what it once was.

## scottAnselmo | 2019-03-12T19:43:58+00:00
I agree with Gingeropolous. Hopefully I'm not oversimplifying, but it sounds like the options basically boil down to RandomX or ASIC friendly. My vote is with RandomX.

At the end of the day, the problem we're dealing with is general hardware vs specialized, and there's no realistic way for general hardware to win. If we go full ASIC friendly though we are arguably entirely reliant on the markets being competitive enough. While we can try to make it easy for startups, etc to manufacture there's no guarantee the markets will play out how we hope. The one positive is that we'd be using established crypto, but we as a community would be ceding a great deal of control over mining diversity security.

This [snippet](https://blog.sia.tech/the-state-of-cryptocurrency-mining-538004a37f9b) I think highlights the ongoing issues with ASIC's and why even when public sold, ASIC manufacturers still win big because they can buy 9 more for themselves every time someone buys one. It's the runaway leader problem on steroids:

> Our investigation into the mining equipment strongly suggests to us that the total manufacturing cost of the equipment is less than $1,000, meaning that anyone who paid $10,000 for it was paying a massive profit premium to the manufacturer, giving them the ability to make 9 more units for themselves. Beyond this, the buyer has no idea how many were sold nor where the difficulty would be when the units shipped. The manufacturer does know whether or not the buyer is going to be able to make a return, but the buyer does not. The buyer is trusting the manufacturer entirely. 

One of our goals is trying to make the Monero ecosystem as trustless as possible. Given all the bad behavior by BitMain and their continued dominance in the ASIC space, I don't see the prominent bad behavior in the ASIC space changing much, if at all and us trusting the markets is dangerous.

With RandomX while it does have a notable con of spinning our own crypto, we as a community are not ceding control to bad behavior markets. If the numbers are correct and ASIC's will have at most 2x, the runaway leader problem will still exist (manufacturers can still sell overpriced goods which we have no control over or otherwise not sell them, etc), but we still mitigate.

 To me the cons of going ASIC friendly and having to trust the markets far outweigh the cons of RandomX and paying for peer reviewed math. When we activate RandomX is a debate that is arguably secondary to that of ASIC vs RandomX.

## fluffypony | 2019-03-12T19:49:51+00:00
@JohnnyMnemonic22 Monero's identity is that it is a privacy-enhancing technology. People don't say: "oh yes, Monero, that ASIC resistant coin", they say "Monero, that privacy coin". The MRL's research has ENTIRELY been focused on privacy and scalability, and not on resisting ASICs.

Here's some of the negative things that resisting ASICs has accomplished:

- lots of criticism from highly technical people
- massive amounts of dev talent spent on PoW tweaks
- emergency, reactive hard forks
- terrible release engineering because we want to leave PoW tweaks until close to the fork
- a huge centralisation factor
- botnets
- the prevalence of Monero mining malware
- horrendous IBD & sync performance due to slow PoW validation

Let me be clear: it is **not possible** to avoid ASICs forever and retain our current properties. By pursuing that as a goal we are either going to end up being highly centralised, or we are going to open the door to ASIC manufacturers becoming significantly more sneaky than they have previously, or both.

I don't want to get too caught up in a back-and-forth on this. Suffice it to say that I will do whatever the community wants me to do and merge whatever PRs they want me to merge, but my strong preference is to commit to a hard date when we will switch to SHA3, even if it is 5 years out, and do whatever in-between: RandomX, ProgPoW, Cuckoo Cycle, whatever.

## JohnnyMnemonic22 | 2019-03-12T20:13:52+00:00
The people of this project have never been shy of adversity, which is essentially what all your negatives boil down to. Criticism? Botnets? Are you being serious?

> Let me be clear: it is not possible to avoid ASICs forever and retain our current properties.

That's an assumption that gets repeated a lot.

We DO need to get caught up in a back-and-forth on this. Otherwise we skip to the "solutions" without properly defining the boundaries and what is really at stake.

## fluffypony | 2019-03-12T20:28:11+00:00
@JohnnyMnemonic22 

> The people of this project have never been shy of adversity, which is essentially what all your negatives boil down to. Criticism? Botnets? Are you being serious?

You disagree that those are negatives? You think that Monero being identified as malware by antivirus companies *due to the mining code* is a good thing? You think that criticism from highly technical people should be ignored because *we know better*? Besides, you're cherry-picking two that you think aren't that bad - and I agree they're not - but that ignores the wood for the trees.

> That's an assumption that gets repeated a lot.

It's not an assumption. ASIC manufacturers will get faster and smarter, and companies like NextSilicon and XTend Online will eventually be able to manufacturer their FPGA-like equipment at scale. We're fighting a losing battle. If there is evidence that we can achieve resistance to specialised hardware without hard forks every 3 months I have yet to see it.

> We DO need to get caught up in a back-and-forth on this. Otherwise we skip to the "solutions" without properly defining the boundaries and what is really at stake.

Everyone else is welcome to have as many discussions about it as they need, nowhere in my comment did I imply otherwise? Not sure where you got that from.

## JustFranz | 2019-03-12T20:41:51+00:00
I feel that no matter what, we are going to have to switch to RandomX in the meantime and that is the immediate priority. The urgency of any move to SHA3 will depend on the results of the RandomX audit from an ASIC manufacturing and CPU internals POV. The possibility of a switch will depend on the overall crypto ASIC or custom ASIC manufacturing landscape.

## fluffypony | 2019-03-12T20:46:35+00:00
@JustFranz I totally agree - the only thing I'd add to that is that picking a date in the future for the switch will help existing miners figure out how and when to sunset their equipment, and will help ASIC manufacturers gear up. It doesn't have to be any time soon, it can even be 5 years out, but putting a peg in the ground would be useful.

## JohnnyMnemonic22 | 2019-03-12T20:48:40+00:00
> You think that criticism from highly technical people should be ignored because we know better?

Not at all. You listed it as a negative consequence, as if our goal should be to avoid criticism. And your mention of malware and botnets struck me similarly, like you think we need to suddenly start caring what everyone else in the world thinks about us. That was never what we were about.

> ASIC manufacturers will get faster and smarter, and companies like NextSilicon and XTend Online will eventually be able to manufacturer their FPGA-like equipment at scale. We're fighting a losing battle.

ASIC manufacturers are people. It's people vs. people. There's no winning or losing, but sometimes one side has an advantage.

You're probably correct in your assertions, and an ASIC-friendly PoW is probably the best technical solution. I'm suggesting it might not be the best solution FOR US. I'm only saying we need to consider who we are and the values we stand for before jumping into timelines.




## iamsmooth | 2019-03-12T20:51:58+00:00
@fluffypony 
> Monero's identity is that it is a privacy-enhancing technology. People don't say: "oh yes, Monero, that ASIC resistant coin", they say "Monero, that privacy coin".

Can't agree entirely. A lot of the exposure (in the sense of "no such thing as bad publicity" perhaps) has indeed been from mining malware. In fact I might venture to guess that there could be _more_ mainstream news mentions of Monero in that context vs. the privacy coverage, which seems more sporadic.

Within the crypto community, Monero is certainly known for privacy but also known for its mining properties, particularly once the population of large coins practically mineable without ASICs narrowed a lot (effectively to one). I've had people from other crypto projects entirely, bring up to me the idea of using (user-controllable; non-malware) Monero in-browser mining to pay for their web services, even though they have other use for Monero. This aspect of Monero is very well known.

> The MRL's research has ENTIRELY been focused on privacy and scalability, and not on resisting ASICs.

One could probably explain that to some extent as: the mining aspect fine as intended for the first three years and the privacy and scalability worked terribly.


## JohnnyMnemonic22 | 2019-03-12T20:56:53+00:00
Monero also has an underground, anti-establishment culture to it that I know you're aware of, @fluffypony, because you actively contributed to it. You may not see it as clearly now that the community has grown, but it's still there and, I'd argue, is the nucleus of what drives the project.

## bitlamas | 2019-03-12T20:58:33+00:00
> [...] picking a date in the future for the switch will help existing miners figure out how and when to sunset their equipment, and will help ASIC manufacturers gear up. It doesn't have to be any time soon, it can even be 5 years out, but putting a peg in the ground would be useful.

Instead of setting a definitive expire date to RandomX and **officially** accepting that Monero will change one of its core features that is arguably part of the social contract -- going 180° in something that has been defended by the vast majority since day 1 -- shouldn't we consider a middle ground? Like try to come up with parameters that would define either the _success_ or the _failure_ of the RandomX and then, in Z years as proposed, we can reevaluate using those parameters and then take a decision.

Precommitting to something that is clearly contentious so far ahead without really knowing what the future holds sounds dangerous.

## iamsmooth | 2019-03-12T20:59:27+00:00
@fluffypony 

> but it occurs to me that we'd already have seen this happen with Bitcoin ASICs in Venezuela and other parts of the world if this was a concern 

I'm not sure why you think we haven't. I've seen many stories about mining gear getting confiscated there, and a few specifically about how people there use can GPUs and mine Ethereum, Zcash or Monero instead of Bitcoin/ASIC coins (which can also be confiscated of course, but at least has a better chance to slip by). Of course like everything else that comes out of Venezuela or out of crypto 'press' you never quite know who to believe.

Here's one I pulled from the top of google, but one can easily find more

https://www.newsbtc.com/2018/05/31/officials-in-venezuela-begin-confiscating-imported-bitcoin-mining-hardware/

## JustFranz | 2019-03-12T21:09:33+00:00
@fluffypony
> @JustFranz I totally agree - the only thing I'd add to that is that picking a date in the future for the switch will help existing miners figure out how and when to sunset their equipment, and will help ASIC manufacturers gear up. It doesn't have to be any time soon, it can even be 5 years out, but putting a peg in the ground would be useful.

I'd like to account for a scenario where RandomX works really well and improving/tweaking it each release is enough to postpone a switch until the ASIC space is deemed sufficiently mature.

The main reason why the ASICs that are made right now are not sold is that they are too good compared to anything else out there, orders of magnitude better. Its just too easy to mine all of the coins yourself and mining all of the coins yourself is going to be maximum profit you can make, unless you sell so many ASICs that the buyers are forced to take a loss.

Perhaps closing the efficiency gap will change this behavior. 

## hyc | 2019-03-12T21:10:32+00:00
> It's not an assumption. ASIC manufacturers will get faster and smarter, and companies like NextSilicon and XTend Online will eventually be able to manufacturer their FPGA-like equipment at scale. We're fighting a losing battle. If there is evidence that we can achieve resistance to specialised hardware without hard forks every 3 months I have yet to see it.

Our previous PoW hard forks were just static targets. Sitting ducks, which is why they couldn't hold off ASICs for any long period of time. RandomX (and to a lesser extent, Cryptonight/R) is a moving target.

FPGAs are great for static algorithms but can't handle dynamic algorithms. When you use up FPGA resources to operate dynamically, you're building a softcore processor and these will always, necessarily due to machine architecture, run several times slower than for a static algorithm. These are simply not a threat. Not for RandomX anyway.

ASICs with an outsized efficiency advantage are not inevitable. That's not how hardware works. The more generalized they're required to be, the less efficient they become. This is unavoidable.


## iamsmooth | 2019-03-12T21:25:53+00:00
I tend to agree that RandomX and to an extent CN-R are new ground in that no other such algorithm has been deployed so there is no track record to say that it will absolutely be ASICd. 

However, I also tend to believe that it is largely a matter of (XMR) price, especially if the forking schedule is taken off the table. There are numerous obvious (and perhaps additional non-obvious) ways that a RandomX chip can be more efficient than general purpose processor (GPU or CPU), even if only by removing unused components. The degree of efficiency improvement won't and can't be arbitrary, but at some price and with a reasonably-long equipment lifetime, it still makes sense.

BTW, as I've noted elsewhere, the way the mining profitability math works out, the degree of advantage isn't that important, as long as there is (a significant) one.  A 10000x advantage gives near-100% profit margin against competing near-break-even miners. But dropping that down to 10x still gives 90% profit margin. Even a 2x advantage gives 50% profit margin, which is still extremely high and with a naive calculation (not quite accurate, but close enough for illustration) only _doubles_ the pay-back time compared with 10000x. I wouldn't rule out even 10-20% advantage being economically sufficient in some cases (with higher XMR price).

## tevador | 2019-03-12T21:34:59+00:00
@iamsmooth You can also get a 2-5x operational cost advantage by basing your mining farm in Iceland ($0.04/kWh). Capital costs will be probably much lower than designing an ASIC from scratch.

## iamsmooth | 2019-03-12T21:44:57+00:00
@tevador That's a nonsense argument. No one locates a mining farm in a high-electricity cost location. They're all in places with cheap electricity. The cost advantages from an ASIC are additive.

Now it is true there will be dorm miners with no direct electricity cost at all, and those will certainly not have to worry about competing. As well as people who mine for a hobby and don't care about profitability. But that's all kind of at the fringes. The bulk of the hash rate is going to end up in places with cheap electricity that is somewhat scalable.


## rw258906 | 2019-03-12T22:18:49+00:00
can someone please elaborate on why these options are off the table?

> I have a few questions, I mentioned one on reddit, but maybe I can get a better answer here, I am sure there are good reasons you guys aren't discussing these but perhaps you could make it clear why these ideas wouldn't work.
> 
>     Why not do 2 algos 1st randomX and the 2nd ProgPow. While neither might be a perfect solution, having both and updating them from time to time seems like it would make it pretty hard to control 80%+ of the hashpower?
> 
>     If Monero were to use an algorithm designed to be optimized for specific consumer hardware such as RandomX or ProgPow, wouldn't it be easy to create an ASIC detection system using the profitability of the target hardware. For instance, instead of adjusting the algo every 6 months no matter what, why couldn't Monero adjust the algo every 6 months if, and only if, they become unprofitable on their target hardware at $0.10/kWh?
> 

## tevador | 2019-03-12T22:25:20+00:00
@iamsmooth I would argue that a significant amount of hashrate are miners who pay residential rates for electricity. 

My point was that when you start talking about 10-50% advantage being significant, you have to consider that there are already differences of this magnitude between individual miners even without ASICs.

## SamsungGalaxyPlayer | 2019-03-12T22:28:22+00:00
@rw258906: please read this entire thread: https://github.com/zcash/zcash/issues/3672

## umma08 | 2019-03-12T22:33:21+00:00
> Firstly....

@Gingeropolous 

that was epic. fair play. ;-)

## iamsmooth | 2019-03-12T23:14:23+00:00
@tevador I'm going to disagree with you that a significant amount of hash rate are miners who pay _high_ residential rates for electricity. There are certainly places in the world that have low residential rates, some even lower than what you quoted, and people living in those place or in places at least with moderate rates may run large rigs, build mini farms, etc., people paying rates at the higher end of the range will not do this unless the plainly do not care about losing money (and there are indeed some, but even they have limits of how much they are willing to lose). 

And, again, it is additive. If the big farms in Iceland, China, NW US, etc. are using ASICs which give them an _additional_ 10-50% advantage then it is _that much harder_ for people with higher electricity rates to compete and many, most, or even all will be pushed out. 10-50% is a HUGE additional margin in terms of mining.

## ArticMine | 2019-03-12T23:56:24+00:00
I will start first with a question. Did we brick any ASICs this time around or did we simply just make GPU and CPU mining ~3.6 times harder? I actually just tried a little experiment. Mine Monero my my laptop and get ~10 H/s. mine MoneroV and get 36 H/s. MoneroV corresponds to V7 of Monero when it comes to mining and 36 H/s is close to what I was getting before all of this started last year.  My suspicion is that either there were no ASICs in the network or if there were any they has a minimal at most impact on the network. This also explains the fast recovery about 2 days, unlike what happened last spring and the fact that there was no impact in the 2018 fall fork.  Please prove me wrong with actual benchmarks on CPU and GPU mining that we actually killed  600-700 Mh/s worth of ASICs this time around. If what I suspect is true the it is very hard to argue that our current strategy has failed or that we need to hard fork every 3 months, when the reality has been no ASICs for close to a year. Even if I am proven wrong it is still 8 months before ASICs actually appeared on the network.  

I personally consider myself fairly neutral on the ASIC issue. The real threat here is proprietary mining. ASICs are only a threat in as much as they enable proprietary mining.  Realistically i do not believe that we can completely eliminate ASICs from the network even with something like RandomX. What I do believe is realistic to narrow down the ASIC advantage to the point where they can co-exist with GPU and CPU miners. This can easily happen with say a 2-3x ASIC advantage vs say 100x ASIC advantage. I also believe that if the ASIC is narrowed down to say 2x this will force the sale and commoditization of the ASIC. For this reason I would consider that moving to RandomX is the correct long term course of action. Furthermore POW changes should only be made it they significantly narrow the ASIC advantage. I do not see the need for "emergency" forks. The latest was in any case as much the result of paranoia over spam bloating attacks as it was over ASICs. I do believe we could  have easily have stayed  the course with our regular release schedule addressing for example a lot of  @fluffypony's concerns. As for a fixed schedule for a move to an ASIC friendly such as SHA-3 I an opposed; however there is nothing wrong with keeping this option were the RandomX approach fail. A little uncertainty here is a very good thing. 

On another note:  I believe we should strongly consider moving the mining aspects of Monero to a strong copyleft GPLV3+ software license. This is especially the case if we are considering a move to SHA-3 or have any concerns with respect to ASICs. There is simply way too much risk of  patents, ASIC boost comes to mind, kill switches powered by DRM, malware, application mining etc. to remain with our current license. We can of curse keep our current license for the rest of the project including basic wallet code which would address issues such as IOS, interactions with proprietary POS and shopping carts etc.    

Edit: @Gingeropolous pointed out to me that the is a configuration command to improve the CPU hashrate:
MONERO_USE_CNV4_JIT=1 ./monerod. This improved the hash rate from 10 H/s to 24 H/s which still implies a hit. Furthermore it will be interesting to monitor the hashrate during the next few days as people become aware of these configuration issues.

## iamsmooth | 2019-03-13T01:44:10+00:00
@ArticMine I'm not sure why your hash rate results are as they are on your hardware but as I understand it, during development one objective was to maintain relatively constant hash rate compared to previous versions on typical CPU and GPU hardware, and indeed this was confirmed through testing.

So I doubt that overall we made CPU and GPU mining 3.6x harder, but given your surprising test results, I guess we can't rule it out.

Interesting idea about licensing of the PoW algorithm. I'm not sure if that is actually possible (in that I don't know if the algorithm itself could be protected, and if not people could always reimplement it to avoid the license), but it is something that could be researched legally I suppose.

EDIT: I see from your edit that you were using the built-in miner, which indeed does not deploy by default in the most optimal configuration. However, standalone miners, which afaik, represents most of the hash rate, don't suffer from that issue. So I still doubt that the hit to the network hash rate due to the upgrade is anything close to 3.6x.

## Lafudoci | 2019-03-13T01:49:50+00:00
Will the ASIC friendly algo keep entity with more fund from producing more efficient miner? My pessimistic view of ASIC ecosystem is eventual annexation and monopoly no matter how we try to make it fair at the start. And this one way ticket will likely be hold in China makes me anxious. We should not ignore China politically fights against freedom and privacy at autocratic level. Profit-driven could always turn into political-driven at any time. "Monopoly miner is not necessary to be a bad actor" should be thought twice here.

I understand current strategy could put Monero in risk, but I don't see the risk is much big from the situation I mentioned above. So I believe we should at least put resource into RandomX. If it works (means reducing gap between ASIC and CPU/GPU, not eliminates ASIC), we should adopt it soon.

But I won't say then mission accomplished after RandomX. As I said, monopoly miner will always be the a potential threat to Monero due to nature of business world, no matter we choose anti- or pro-ASIC. So we should also put some thoughts on: How could we defend Monero properties like secure, privacy, fungible as much as possible in the worst scenario? After all, that's what we aim to build and why the community assemble since day one.

## iamsmooth | 2019-03-13T01:52:01+00:00
@ArticMine 
> I do not see the need for "emergency" forks. The latest was in any case as much the result of paranoia over spam bloating attacks as it was over ASICs

I can't agree with that. When it appears that one actor may control 80% of the hash rate, that is profoundly insecure, and is as worthy of an emergency fork as anything. Actually this is the main reason I'm very much concerned about the overall approach currently. The algorithm changing cycle is likely not fast enough to keep out _all_ ASICs, therefore we appear to be increasing the likelyhood of keeping out _all but one_, which is making the network less secure, potentially very insecure. 

This is an existential threat to Monero.

Previous double spend and hash rate attacks on coins such as ETC have not entirely destroyed the coin (though it is hard to measure the damage due to loss of reputation and confidence) but that does not guarantee that a major attack against Monero would not be devastating. As they say, past performance is no guarantee of future returns (or attacks).


## ArticMine | 2019-03-13T02:33:15+00:00
@iamsmooth I updated my post there is a configuration issue that improves the hashrate from 10 H/s to 24 H/s, but there is still a hit. Also there may be lack of awareness  of this which can impact the overall hashrate. My point is that we should properly quantify the threat and that means a proper evaluation of impact of the algo change on CPU and GPU hashrates, before jumping to conclusions.  My assumption of 3.6x change may be as bad as no change. 

I am not convinced that the ASIC threat this time was even close to what we say last year. 80% seems very high to me, this time around and I would not be surprised if a significant portion for the hashrate drop was mis configuration by miners and pools, apart from a harder algo. One reason is that the recovery this time around is both faster and smother.

Changing the license to GPL V3+ for the mining code will not protect the algorithm but will protect the code and consequently can mitigate against many attacks. 

I do agree that POW changes for the sole purpose of keeping ASIC manufacturers of balance is unsustainable. This does not mean that we are on the wrong course right now. If we narrow the ASIC advantage down to say well under 5x, this will mean much stronger protection than simply hoping that an "easy" ASIC algo is not going to be monopolized if for example a large player simply decide ti throw resource s at it. RandomX is looking very good and even it it develops an ASIC component may end up being  better than the alternatives. 

## JustFranz | 2019-03-13T03:04:23+00:00
The GUI/monerod miner is a joke miner. I'm getting 220 H/s with my 3770K on XMRig ( 4T x ~55 H/s) and Monero GUI is reporting 30-44 H/s total

1t - 11-14 H/s mostly stable at 14 
2t 21-28 H/s mostly stable at 27-28
3t 32-41 H/s seems to be mostly at 38-39, but unstable
4t 39-44 H/s unstable in that range, dips into mid 30s

## bitlamas | 2019-03-13T03:04:49+00:00
> The algorithm changing cycle is likely not fast enough to keep out _all_ ASICs, therefore we appear to be increasing the likelyhood of keeping out _all but one_, which is making the network less secure, potentially very insecure.

You're correct. There's a risk that _one_ unknown actor can dominate the majority of the network when secret ASICs are introduced. This is real and should not be taken lightly. But I don't think you can assume that this will happen, or that only _one_ unknown actor will join the network with secret ASICs for CryptoNight R or RandomX for that matter. The argument _"the risk is there anyway"_ is valid and I don't want to downplay that. I understand and accept that the risk is there.

But if we're going to put some arbitrary weight to that risk, I think it's only fair to also consider and put in balance other possibilities. The same way we cannot assume _one_ unknown actor will join the current network with secret ASICs, we cannot assume _any_ ASICs will join at all. In fact, if it makes sense to make a profit by taping out secret ASICs, maybe _more than one_ manufacturer will produce them, possibly mitigating the 51% attack possibility. Maybe FPGAs will join the network. Maybe more miners will join the network. This is all based in assumptions, because that's all we can do: make assumptions and projections about the future.

ETC recently suffered a 51% attack, but I think It's possible to argue that that specific chain is less relevant than Monero's. That argument can of course only happen if you consider that the attacker doesn't care about the future of Ethereum Classic, since Ethereum exists and is vastly bigger than the former. Monero in the other hand is not the same chain as Ethereum Classic and might be considered a chain with enough importance to not jeopardize its existence -- who knows, maybe this is the reason it wasn't attacked both times it was dominated by ASICs. This line of thinking might be supported by the very curious fact that Bitcoin Cash and Bitcoin SV both have chains that didn't suffer a 51% attack, albeit being extremely easy to attack them with existing specialized hardware currently mining Bitcoin. Let me remind you that all of this paragraph is purely based in assumptions, the same way the paragraph above this one is based on assumptions. I understand that the risk might be there anyway, and that's true.

I repeat: the possibility that _one_ unknown bad actor might dominate the network with secret ASICs and attack it is real and should not be taken lightly. I just disagree that the best (or only) solution is to accept ASICs and the plethora of problems and attack vectors they will ultimately bring.

To ignore or to believe that these problems and social implications don't exist is wrong. The same way you have a valid point by saying that **maybe** one unknown bad actor can dominate the network and this poses an existential threat to Monero, it wouldn't be that hard to argue that, **maybe**, the whole set of problems that effectively changing a core stance of this project will bring (by prematurely embracing ASICs) can pose an existential threat to Monero as well. 

## fluffypony | 2019-03-13T04:20:21+00:00
@JustFranz the GUI’s built-in solo miner is a CPU miner, not a GPU miner.

## iamsmooth | 2019-03-13T05:46:50+00:00
@fluffypony it sounds like he was using xmrig as a CPU miner. The problem is likely the same as what ArticMine encountered: The default mode for the built-in miner does not use JIT. This is probably dumb. Even if we don't want to use JIT for validation (which is debatable), the built-in miner should always use it. Worst case is that JIT gives the wrong results while mining and the "found" block is rejected.

## fluffypony | 2019-03-13T05:48:11+00:00
@iamsmooth at the very least the JIT should be enabled by a CLI flag and not by an environment variable... :)

## iamsmooth | 2019-03-13T05:48:30+00:00
@fluffypony That won't necessarily help with the GUI though

## iamsmooth | 2019-03-13T05:49:02+00:00
@JustFranz if you are on linux or mac try `export MONERO_USE_CNV4_JIT=1` before starting the GUI. If you are on Windows I have no idea.

## iamsmooth | 2019-03-13T05:58:45+00:00
@vp1111 
> But I don't think you can assume that this will happen, or that only one unknown actor will join the network with secret ASICs for CryptoNight R or RandomX for that matter

If multiple unknown actors join the network that is not quite as bad as only one, but it is still a failure of the approach and still likely leaves the network in a less secure state to the extent the approach has any 'successful' effect whatsoever in discouraging ASICs and reducing their development and availability.

> But if we're going to put some arbitrary weight to that risk, I think it's only fair to also consider and put in balance other possibilities

Yes, but the correct balance is the weight/probability that the strategy is _entirely_ successful and keeps _all_ ASICs off the network (the only possible way the approach is successful) vs. the strategy only being 'partially successful' (in fact this is better described as 'failure'), resulting in fewer or only one ASIC on the network, in which case it made matters worse. We do not absolutely _know_ these weights, but we can observe that the strategy has _repeatedly_ failed already, and virtually _no one_ actually expects it to reliably succeed in the future, the only question people are debating is whether ASICs will end up developed with a six month cycle, or whether they would perhaps need an eight or ten or twelve month cycle instead (and further these all change immediately if the XMR price goes up). _This is not a valid security model at all_.

RandomX raises even more problematic issues, because as @hyc points out, the 'tweaking' strategy basically goes away as an option. Any ASICs which do manage to implement it (and again, to the extent we 'succeed' in reducing the number but not to zero, this is actually a _failure_) will probably be flexible enough to adapt to modest changes. The only way to get rid of them at that point would be fork to a very different algorithm.


## SChernykh | 2019-03-13T06:39:47+00:00
@iamsmooth You seriously underestimate how hard would it be to create efficient RandomX ASIC. Yes, it can be 2x faster using the same process node but it _won't be the case_. RandomX ASICs will be most likely built on 16, 22 or 28 nm process node _and_ they won't use as efficient IPs as what AMD/Intel have. Either of these will immediately put them to disadvantage compared to newest 7 nm CPUs. You guys give up too early.

## iamsmooth | 2019-03-13T06:54:53+00:00
@SChernykh I haven't ruled out RandomX being a success. But I also think you have to recognize that the history of ASIC-resistant algorithms, including on Monero, has been overconfidence on the part of developers. Maybe RandomX would be different, maybe not.

Whether it does work is not the whole question though. Part of the question is what happens if it doesn't work, because I would argue we simply can not afford to be 100% or even nearly 100% confident that it will work. If it doesn't work, we are left in a nasty spot, with secret proprietary ASICs again dominating the network, no easy solution in terms of tweaking, and no preparation for an orderly switch to SHA3 (or anything else) because no one is going to build ASICs without knowing with some sort of confidence if and when they will go live.



## SChernykh | 2019-03-13T06:57:43+00:00
@iamsmooth We're _not_ overconfident, we _want_ independent reviews of RandomX from ASIC/FPGA designers. We also can't simply be binary "it works/it doesn't work". The main question is how efficient real RandomX ASIC could be. If it's really only 2x, it's not a 51% threat.

## iamsmooth | 2019-03-13T07:00:27+00:00
@SChernykh The only 'review' that counts is putting it live on a big network and having people attempt to attack its ASIC-resistance. Including when the network gets bigger because the price goes up. That's how these things work.

> We also can't simply be binary "it works/it doesn't work".

Yes we can, and not only can we, we must consider that because to fail to consider both possibilities leaves a gaping hole in any sort of plan.

> If it's really only 2x, it's not a 51% threat

I don't agree. Even a 2x advantage means ASICs can push out anyone with the same electricity costs and less than a 50% profit margin. That's most miners. If they are deployed in a location with cheap electricity, as they surely would be, they can easily push out just about everyone (apart from e.g dorm miners).

## SChernykh | 2019-03-13T07:06:12+00:00
> I don't agree. Even a 2x advantage means ASICs can push out anyone with the same electricity costs and less than a 50% profit margin. That's most miners. If they are deployed in a location with cheap electricity, as they surely would be, they can easily push out just about everyone (apart from e.g dorm miners).

I don't agree on that as well. 2x advantage means literally millions of ASIC chips need to be produced to 51%. And you'll have to organize _huge_ mining facilities for them if you don't sell them and mine in secret. This will cost a fortune. Add very high R&D costs to this. Also add botnets/office miners (arguably a significant part of network on CPU-favoring algorithm) with free electricity which will always be more efficient. Things aren't looking good for ASIC attacker anymore.

## iamsmooth | 2019-03-13T07:18:22+00:00
@SChernykh Production costs are often quite low once the chips are designed (and indeed producing more chips reduces by amortization the per-unit NRE). There are numerous reported cases where mining ASIC developers have way overproduced chips because it costs so little to do so. (They don't always turn them into working miners though, because of other-component and assembly costs.)

_Huge_ mining facilities are not a major obstacle. These already exist for Ethereum and Bitcoin, and some tiny fraction of them (which is all that would be needed for XMR at its current size) can easily be repurposed if there is a a higher-margin opportunity (any likely ASIC developer is probably already a big miner of other coins, or has close relationships with them).

At the current hash rate and assuming 10 H/W, XMR's total hash rate now rates about 30 MW, which is right about the size of the biggest _individual_ public mining farms.

That's not to say this sort of takeover would happen overnight, but it doesn't need to, as RandomX isn't intended as a temporary algorithm to be replaced with a fork after six months. If someone takes over the network over the course of a year, they've still taken it over, and likely in a stealthy gradual way that will avoid any sort of clear evidence that it has happened.

## SChernykh | 2019-03-13T07:23:20+00:00
> If someone takes over the network over the course of a year, they've still taken it over, and likely in a stealthy gradual way that will avoid any sort of clear evidence that it has happened.

That doesn't take into account that price/network can grow faster than they produce new chips. Too many unknowns. And if price doesn't grow, 51% attack will cost much more than it returns. So profit-driven 51% attacks are unlikely. Non-profit driven attacks could've happened long ago and can happen any moment, ASICs are not needed for this.

## iamsmooth | 2019-03-13T07:25:50+00:00
@SChernykh The "too many unknowns" work in the wrong direction for your argument. If you want to make a security case, you have to argue why something can't or won't happen, not that it isn't guaranteed to happen.

Someone taking over the bulk of the network _is already an attack_, regardless of what they do next, and exactly how they decide to make use of that position (a decision which can change over time). It undermines the purpose of a decentralized network.

## SChernykh | 2019-03-13T07:27:51+00:00
@iamsmooth You also can't prove that scheduled shift to ASIC-friendly algo won't result in 51% attack in the first few months of it. What's the point?

## iamsmooth | 2019-03-13T07:35:00+00:00
The case being made is the best argument available from the most people who have thought about the issue the most, and attempting to implement it in the safest way possible (for example, by some or all of: using the simplest available algorithm to encourage market entry, defining a clear fork/launch schedule to minimize cost-of-development and market risk, and actively engaging with ASIC developers to encourage support). 

On top of all that, a simpler and faster algorithm is inherently superior independent of mining marketplace and economy considerations, from the perspective of general resource usage, verification time and DoS concerns (also potentially unnecessary complexity and general attack surface considerations). For example, no need for 4 GB (or even 256 MB) of memory on smaller devices.

But you're right it still isn't a guarantee.

## JohnnyMnemonic22 | 2019-03-13T08:28:22+00:00
> If someone takes over the network over the course of a year, they've still taken it over, and likely in a stealthy gradual way that will avoid any sort of clear evidence that it has happened.

Don't forget that chip makers like Intel and AMD will continue to release faster chips, so even if ASICs had a 2x advantage, that gap would close considerably within a year, requiring new ASICs to be made in order to maintain their advantage. It doesn't seem likely that a stealth takeover would be feasible with only 2x advantage.

## iamsmooth | 2019-03-13T09:12:49+00:00
@JohnnyMnemonic22 Sure there is a trend, but not 2x per year. Even after a whole year, the (starting) 2x ASIC would still maintain some advantage, would have already banked a lot of profit whether or not completely dominant on the network (yet).

Also, the ASIC developer could also be making progress toward improved chips, too. I mean new chips aren't released continuously but looking at the bigger picture, everyone is pretty much on the same trajectory of improvements over time, including the ASICs.

Even if it takes multiple years and multiple chip generations, eventually 2x is still going push out anyone but hobby/dorm miners, botnets, etc. (and even give those some challenges in terms of reduced incentive to participate). Perhaps this takes a higher XMR price, but as long as overall revenue is enough to cover the ASIC development costs, it is inevitable. I really don't understand how anyone who understands mining economics and profit margins would think otherwise. 50% profit margins for mining are not the norm; they generally exist only during major pumps when the hash rate hasn't caught up yet.

## dEBRUYNE-1 | 2019-03-13T11:02:10+00:00
@vp1111 

>Like try to come up with parameters that would define either the success or the failure of the RandomX and then, in Z years as proposed, we can reevaluate using those parameters and then take a decision.

I'd strongly oppose such a course of action. I do agree that we ought to set up some rules to gauge whether RandomX is a failure or a success. However, in my opinion, we should also have a plan that outlines our course of action in case RandomX fails. Not committing to a plan will result in having to have this debate when Monero's ecosystem is significantly bigger. Should I remind you what happened when Bitcoin tried to come up with a plan for the block size? It effectively resulted in a large community split, where part now resides in Bitcoin Cash, Bitcoin SV, or even Bitcoin Gold. We also have to bear in mind that chain splits in Monero are arguably worse, as they have the potential to significantly weaken privacy. In sum, we should absolutely make this decision now and not in the future when Monero's ecosystem presumably is significantly bigger. Precommiting allows us to focus on the protocol and not waste time on endless debates in the future. Furthermore, it will substantially mitigate any future friction regarding this subject in the community.

>shouldn't we consider a middle ground?

I think most people can agree that switching to an ASIC friendly algorithm if RandomX fails is a reasonable middle ground. If RandomX fails, we've essentially exhausted all our options and should not venture into dangerous territory to further preserve ASIC resistance. 

------------------------

@JustFranz 

>I'd like to account for a scenario where RandomX works really well and improving/tweaking it each release is enough to postpone a switch until the ASIC space is deemed sufficiently mature.

Tweaking has proven to be a futile and potentially dangerous strategy. Why anyone would even consider to use it as strategy in the future is beyond me. 

## iamsmooth | 2019-03-13T11:08:57+00:00
@dEBRUYNE-1

> I think most people can agree that switching to an ASIC friendly algorithm if RandomX fails is a reasonable middle ground. If RandomX fails, we've essentially exhausted all our options and should not venture into dangerous territory to further preserve ASIC resistance.

I think it is quite plausible that it may be hard to tell if it fails and perhaps equally hard to define what "fails" even means in an objective way. Especially, as you say, that it may involve having the debate when Monero's ecosystem is significantly bigger and the issue is even more politicized (and perhaps more thoroughly infiltrated by people with a hidden narrow commercial interest).

When the vague claim of RandomX having failed is made at some point in the future, we're basically set back to the current state again of having a discussion of the future of the PoW algorithm, including a repeat of the current situation of people not agreeing whether the current strategy has failed.

> Tweaking has proven to be a futile and potentially dangerous strategy. Why anyone would even consider to use it as strategy in the future is beyond me

It has also been pointed out by @hyc that "tweaking" RandomX is even less likely to work at all.

## dEBRUYNE-1 | 2019-03-13T11:21:12+00:00
>I think it is quite plausible that it may be hard to tell if it fails and perhaps equally hard to define what "fails" even means in an objective way. Especially, as you say, that it may involve having the debate when Monero's ecosystem is significantly bigger and the issue is even more politicized (and perhaps more thoroughly infiltrated by people with a hidden narrow commercial interest).

I mentioned this earlier as well:

>There will be contention in the community whether the new hashrate is coming from genuine miners or ASICs (remember the discussion threads when the hashrate started to increase recently? A lot of people were unconvinced it were ASICs).

I think, however, this can mostly be mitigated by (i) setting up the parameters that define failure in advance and (ii) precomitting to switching to an ASIC friendly algorithm (chosen in advance). Do you think this would be a reasonable course of action?

- Switch to RandomX
- Set up parameters that would define failure of RandomX
- Switch to SHA3 once RandomX is classified as failed 

A heuristic to determine failure that I've seen discussed is looking at profitability figures of other CPU/GPU minable coins. Do you think that would be relatively reliable? 

## JustFranz | 2019-03-13T11:29:45+00:00
I have no idea how to enable the JIT for windows GUI/CLI miner. I am mining on a CPU. The GUI miner has 5.5x lower hashrate than XMRig. I'm going to open up a separate issue for this.

Regarding RandomX and its x86 instructions, what are the legal implications of implementing those instructions in hardware? Can you even sell those chips? Selling them outside of china? Would there be any hesitation from TSMC to produce those chips?

https://bitcoinmagazine.com/articles/bitmains-new-7nm-chip-miners-are-available-purchase-today/
The economics of other coins might force the chips onto older nodes. Bitmain are such scumbags, disabling ASIC boost for cutomers while mining with it themselves. Glad they impaled themselves on bitcoin cash.

CPU speed improvements will come from core count increase from Intel and core count and clock speed increase from AMD. Intels main strategy for performance increases since Sandy Bridge has been increasing the base clock, which they could have bumped by 500-600 Mhz way back then easily but they decided to spread it out. OC headroom for Intel chips has pretty much run out in the 9th gen chips. Before AMD got good with Zen, Intel was jacking up the prices and holding back performance.
AMD has 1 Ghz to catch up with intel and a little bit in IPC. Hopefully the core count race will continue.
Beyond that there are the increasingly smaller nodes, 5nm 2020 and 3nm 2022, for more transistors per area. After that, material change that will enable higher clocks?

RandomX needs to be run by some CPU guys too. When the documentation is finished we could start soliciting some first opinions.


## Gingeropolous | 2019-03-13T12:02:14+00:00
Despite my ramblings, I could get behind some sort of timeline on the scale of 5 to 10 years to throw in the towel. As others have mentioned though, these milestones are going to be difficult to measure. E.g, is RandomX doing what it needs to, do ASICs exist, etc. 

One option is to take the Obelisk approach and attempt to produce our own ASIC right from the start for RandomX. This does a lot of things. 1, it lets us know they exist. 2, it gives us a sense of their performance over commodity hardware. 3, it puts even more pressure on a secret asic manufacturer to distribute their product as oppose to secret mine. And 4, it forces the secret ASIC developer to have a significant efficiency gain over another ASIC as opposed to commodity hardware. So if RandomX is really going to hold is to, say, 1.5x commodity hardware,.... a secret asic manufacturer and miner may not make moves if all they can offer is 1.7x commodity hardware. 

Also, (and this may be a question for @tevador in the RandomX thread), but what happens if all the CPU manufacturers implement some new instruction sets? In general, is RandomX going to be modified as CPUs evolve? (because surely they will.)

## dEBRUYNE-1 | 2019-03-13T12:14:05+00:00
>ASIC right from the start for RandomX.

This is a bad idea. If you are going to allow ASICs, you'd want to adopt a simple algorithm that has the least possible amount of optimizations. This levels the playing ground and closes the gap between ASIC manufacturers. If you leave room for a lot of optimizations, you will probably end up with a single dominating manufacturer, which is potentially dangerous for the network. Hence, my suggestion to precommit to an ASIC friendly algorithm such as SHA3 in case RandomX fails. 

I should also note that SHA256 (which Bitcoin utilizes) can be considered as relatively complex (in comparison to for instance SHA3) and lots of optimizations have been 'exploited' by ASIC manufacturers. It may be one of the reasons why the playing field in Bitcoin has not leveled as much as we'd like. 

## bitlamas | 2019-03-13T13:20:38+00:00
Did we reach the peak of technology development? Who can guarantee that the moment we change to SHA3 there won't be one single manufacturer with one "creative" way to make a 4x better ASIC than all the others manufacturers? Why this risk has not the same weight as the _one single secret ASIC manufacturer_ who maybe will join the network and maybe will attack the chain? I can understand the argument that SHA3 is simplest algorithm to produce an ASIC, but does that mean that there are not further improvements possible? So did we finally reach the ultimate peak of technology development? If not immediately, what happens if in 1 year a single manufacturer comes up with such an improvement? As @Gingeropolous already said, if that happened we will be in a very bad situation because now we're officially ASICs-friendly and there would be nothing we could do about it. Should we just believe they will be benevolent dictators and offer the overpowered money printing machine to the society? I'd rather leave that such development to the computer processor industry so that we can all benefit from the future developments in many different ways, such as having better CPUs overall.

Do you really think it's worth to do such a **monumental** change in the protocol, social contract and project stance, just to _maybe_ have a well developed market? Anyone who believes the current SHA-256 ASIC market is well developed, just go to any country in South America and let me know how easy it is for you to buy one there.

@iamsmooth 
> I don't agree. Even a 2x advantage means ASICs can push out anyone with the same electricity costs and less than a 50% profit margin. That's most miners. If they are deployed in a location with cheap electricity, as they surely would be, they can easily push out just about everyone (apart from e.g dorm miners).

What about all the data centers that could be mining Monero? What about all the often ignored small and medium-sized business that could be mining Monero? They might not be right now, but that might be a question of education. Even if all the dorm miners + cheap/free electricity miners + ideology-driven miners + botnets + business mining with their desktops and servers count to up to 25% of the total network (compared to the hypothetical 2x ASICs), this level of decentralization is not wanted? It's not enough? How much would be enough? How can we know if we just want to get over with it and let the ASICs manufacturers run the show?

@dEBRUYNE-1 
> Not committing to a plan will result in having to have this debate when Monero's ecosystem is significantly bigger. Should I remind you what happened when Bitcoin tried to come up with a plan for the block size? It effectively resulted in a large community split, where part now resides in Bitcoin Cash, Bitcoin SV, or even Bitcoin Gold.

From what you're reading in Reddit you don't think there will be a large community split if we prematurely (imo) take the official stance to embrace ASICs when we just forked to remove them? Look at all the cheering over there. I think this is going to be a very hard sell and it doesn't matter if it happens now or in the future. But I get you, yes, of course it would be harder to have this debate if the community and ecosystem was significantly bigger. I agree. But if this current discussion is showing anything is that the pro-ASIC stance is not really unanimous, so such a split could happen anyway.

> I think most people can agree that switching to an ASIC friendly algorithm if RandomX fails is a reasonable middle ground. If RandomX fails, we've essentially exhausted all our options and should not venture into dangerous territory to further preserve ASIC resistance.

I don't fully agree with that, but I understand your point and could maybe accept this if the parameters were very well defined. In my previous comment when I said "reevaluate and take a decision" I meant to analyze the future state of the network against the set of parameters that would define it as success or failure, and if (and only if!) we state RandomX was a failure then we should proceed to a change. And I'm all for coming up with a very well defined set of parameters that don't open space for interpretation, because we will not want people saying _"I don't see this as a failure"_.


## tevador | 2019-03-13T13:33:04+00:00
@dEBRUYNE-1 
> we should absolutely make this decision now and not in the future when Monero's ecosystem presumably is significantly bigger

Even if we make a decision now that Monero will switch to SHA3 at block 2xxxxxx, it doesn't mean there won't be a split in the community when the fork date comes closer.

@JustFranz 
> Regarding RandomX and its x86 instructions, what are the legal implications of implementing those instructions in hardware?

RandomX has nothing to do with x86 and doesn't contain anything proprietary (as far as I'm aware). The RandomX VM is agnostic to the underlying platform and should run equally well on most 64-bit architectures, including x86-64, ARMv8 and RISC-V.

@Gingeropolous 
> what happens if all the CPU manufacturers implement some new instruction sets?

Normally it takes ages for new instruction sets to become widespread. For example AES-NI extension for x86 was created in 2008 and some Intel CPUs released in 2015 still didn't support it.

## dEBRUYNE-1 | 2019-03-13T13:57:40+00:00
>From what you're reading in Reddit you don't think there will be a large community split if we prematurely (imo) take the official stance to embrace ASICs when we just forked to remove them? Look at all the cheering over there. I think this is going to be a very hard sell and it doesn't matter if it happens now or in the future.

As far as I can see, the majority of the community currently envisions a foreseeable future that includes RandomX as PoW algorithm, hence the cheering. That being said, the community seems to understand that if RandomX fails, we've basically exhausted our options and the only logical next step is a ASIC friendly algorithm. I don't think this will be a particularly hard "sell". 

>Even if we make a decision now that Monero will switch to SHA3 at block 2xxxxxx, it doesn't mean there won't be a split in the community when the fork date comes closer.

Significantly less likely than a split occurring if we make a decision now. 

## Gingeropolous | 2019-03-13T15:07:12+00:00
>  If you are going to allow ASICs, you'd want to adopt a simple algorithm that has the least possible amount of optimizations. 

Yes, I understand that theory. However, I am countering with the idea that if there are no possible optimizations, or if a trusted entity (e.g., Monero) can push the optimizations to their known maximum, that leaves a nefarious ASIC entity less room for advances.

E.g., if commodity hardware does 100%, and if it is theoretically possible to produce an ASIC that does 200%, then an ASIC manufacturer gets all of that difference (100%). However, if Monero (or some known entity) does the work to push out an ASIC that does 180%, this shifts the playing field. 

So, if there is an actual limit to efficiency gains with RandomX at 200%, the secret ASIC manufacturer only has the remaining 20% of the original limit to play with, which is now 11% of the generally available hardware (including RandomX ASICs). 

> If you are going to allow ASICs, you'd want to adopt a simple algorithm that has the least possible amount of optimizations. This levels the playing ground and closes the gap between ASIC manufacturers. 

I think this theory holds true in a world where a PoW can't be developed that creates ASIC equivalence. That statement presumes that if an ASIC exists, it will dominate with ridiculous orders of magnitudes of efficiency. It does not take into account the possibility of parity. 

I'm not saying its a great idea, but something to kick around. 

## SamsungGalaxyPlayer | 2019-03-13T15:30:18+00:00
@Gingeropolous thanks for introducing the idea, but I would rather the Monero community develop a SHA3 ASIC with open hardware than to attempt a RandomX ASIC.

A competitive algorithm and the plans in place to move away from it if necessary in 1-2 months is perhaps the best chance we're going to get at discouraging ASICs from joining the RandomX network en masse for a long time.

## SamsungGalaxyPlayer | 2019-03-13T15:37:27+00:00
In reference to patching RandomX, I only am speaking to obvious discovered bugs. Suppose a manufacturer exploits a flaw that makes then 10x competitive, and we can patch it quickly. Those are the circumstances I'm speaking about when I say a RandomX patch may be preferable to committing to SHA3.

If the algorithm functions as expected and ASICs dominate the network nevertheless, then I agree small tweaks with the sole intent to break stuff aren't going to keep working.

## el00ruobuob | 2019-03-13T16:29:34+00:00
> I would rather the Monero community develop a SHA3 ASIC with open hardware than to attempt a RandomX ASIC.

Then it implies abandoning the idea of closing the gap between general purpose and specialized hardware. No CPU/GPU will be able to compete with those ASICs.  
I like the idea of an open hardware ASIC, but i don't like putting aside general purpose hardware.

## JustFranz | 2019-03-13T16:32:37+00:00
Thats what I meant with RandomX tweaks, patches for "bugs" and changes if new research has ways of making it better either by conforming to CPUs better, taking larger advantage of CPU features that are becoming more prevalent or introducing some other change that disproportionately hits ASIC manufacturing cost or power/hash efficiency.

@SamsungGalaxyPlayer 
>A competitive algorithm and the plans in place to move away from it if necessary in 1-2 months is perhaps the best chance we're going to get at discouraging ASICs from joining the RandomX network en masse for a long time.

A change like that must be kept secret but at the same time the community must know that it is being developed behind closed doors and accept that it will result in a hard fork as soon as ASICs appear. After the fork, then what? Its a decent deterrent if something like that materialized but with no followup we are caught with our pants down.

How much would it cost to outsource a SHA3 ASIC design? Seems to me that we need to pick a post RandomX POW ASAP and commit to it so that interested ASIC designers and manufacturers can start thinking about it. Commit in a sense that if we make a move to an ASIC POW, its going to be that one.

Should we have a reference design that established companies/startups can use as a base or for a production run?

I still think its too early to set a date. More like goals and conditions.


@el00ruobuob 
We must have something in case RandomX utterly fails.


https://i.imgur.com/MuMK6db.png how I see our options

## el00ruobuob | 2019-03-13T16:42:50+00:00
> We must have something in case RandomX utterly fails.

@JustFranz I do agree, but i am unconfortable with increasing the gap between ASICs and CPU/GPU.  
I do however understand how better a simple design as SHA3 would be to avoid risking a very optimised ASIC to emerge, as it could arise on RandomX ASIC.

## JohnnyMnemonic22 | 2019-03-13T18:01:48+00:00
> That being said, the community seems to understand that if RandomX fails, we've basically exhausted our options and the only logical next step is a ASIC friendly algorithm. I don't think this will be a particularly hard "sell".

That's a dangerous assertion because it's not really a "sell" as much as it's telling people how to think. People subscribe to a philosophy and it's our job (collectively) to uphold and facilitate it as best we can. It's not our place to _change_ the philosophy to whatever we want just because we think it's better that way. That is exactly the kind of behavior that leads to chain splits.

Monero's position has always been that of ASIC resistance. If embracing ASICS and adopting SHA3 is the goal, then the responsible course of action would be to fork the project and call it Monero-K (or whatever). Then you will really know how much support there is for such an endeavor.

## dEBRUYNE-1 | 2019-03-13T18:30:32+00:00
Being entrenched in a philosophy that is unviable to attain is also particularly dangerous. It results in venturing into "at all cost" strategies that are invariably a net negative for Monero. 

Arguably, if there's community consensus on switching to SHA3 *if* RandomX fails (as determined by some predefined rules), we should follow that path, even if it somewhat conflicts with our original philosophy. 

## antanst | 2019-03-13T18:51:22+00:00
> Arguably, if there's community consensus on switching to SHA3 if RandomX fails (as determined by some predefined rules), we should follow that path, even if it somewhat conflicts with our original philosophy.

What would those predefined rules like, and how is failure defined in the context and complexity of RandomX? Are we talking about definite, provable systemic failures (the equivalent in a hash based PoW would be the loss of preimage resistance, collisions etc)? What will we do if someone finds some case that could possibly give an edge to an ASIC manufacturer but we have no idea if someone has exploited or not yet?

Is there a point to keep following the current fuzzy "hmm that sudden rise in hash rate looks suspicious/scary/unfair, let's tweak and fork" style policy, after RandomX has been applied?

## JohnnyMnemonic22 | 2019-03-13T18:53:32+00:00
> Being entrenched in a philosophy that is unviable to attain is also particularly dangerous.

It _is_ dangerous. Switching to SHA3 would be the safest bet. I don't think Monero exists to play it safe or take the path of least resistance. This was a fight we all signed up for.

## geonic1 | 2019-03-13T18:56:13+00:00
> As far as I can see, the majority of the community currently envisions a foreseeable future that includes RandomX as PoW algorithm, hence the cheering. That being said, the community seems to understand that if RandomX fails, we've basically exhausted our options and the only logical next step is a ASIC friendly algorithm. 

@dEBRUYNE-1 That's a huge leap in reasoning to come to the conclusion you have. I would argue that very few people (measured as a percentage of the community) have made that leap in thinking that if RandomX fails, then ASIC friendliness is our only option. These people are technically-minded realists who are over represented in this thread. But a realist by definition can only work with currently available information. RandomX was thought up less than a year ago -- if it fails (again, there is no evidence it will), how can we be certain that a better ASIC-resistance mechanism will never be developed and that it doesn't deserve to be pursued?

Monero is a community of optimists who envision a fungible, decentralized, scalable currency. We've only (arguably) succeeded in the first and are fighting for the second. Forcing to precommit to a decision now will not only not avoid a split, but will make it certain when the time comes to carry out that commitment.

Precommitting to a contentious decision now achieves the following:
1) Deprives us of newly available information. This includes the future state of the ASIC industry, consumer hardware developments, RandomX's failure or success, the invention of other ASIC-resistance schemes that have not currently been thought up and the shifting incentives within the market as a whole.
2) Prevents the participation of wider group of people in the decision-making process. These people might be mercenaries or they might be meaningful contributors with abilities or knowledge that exceeds the current talent pool.
3) Makes certain a community split at a predefined future moment.

The best course of action is to make decisions about the present based on currently available information and to allow room for that information to change, not to make future decisions based on hypotheticals. As far as I'm aware, the most recently available information is that we bricked a bunch of ASICs -- why is this seen as such a failure?

## JohnnyMnemonic22 | 2019-03-13T19:09:06+00:00
Doctor: "Mrs. Brown, we've exhausted all known treatment options for your boy. The only logical next step is to embrace the infection, helping it spread through his body and killing him as quickly as possible."

On a more serious note, an ASIC-friendly fork would perhaps result in the least amount of friction, and if the community does sufficiently switch over, the fork could adopt the "Monero" name.

## fluffypony | 2019-03-13T19:09:13+00:00
> It is dangerous. Switching to SHA3 would be the safest bet. I don't think Monero exists to play it safe or take the path of least resistance. This was a fight we all signed up for.

On the contrary, as Monero is responsible for a greater & greater amount of people's money, we have to make the safer choices. I'd encourage everyone commenting in this thread to pretend that you are personally responsible for someone's life savings, and then act accordingly.

## antanst | 2019-03-13T19:16:59+00:00
> On a more serious note, an ASIC-friendly fork would perhaps result in the least amount of friction, and if the community does sufficiently switch over, the fork could adopt the "Monero" name.

The Monero developers have already proven in every hard fork so far that they take community consensus in serious consideration; therefore any fork so far that has been endorsed by the developers _de facto_ carried over the Monero name. This case is no different.

## JohnnyMnemonic22 | 2019-03-13T19:21:54+00:00
> therefore any fork so far that has been endorsed by the developers de facto carried over the Monero name. This case is no different.

This case is _very_ different. The trustees of the project are afforded all sorts of powers in order to carry out their objective. In this case, the trustees are proposing to _change_ the objective.

## geonic1 | 2019-03-13T19:22:51+00:00
> This case is very different. The trustees of this project are delegated all sorts of powers in order to achieve their objectives. In this case, the trustees wish to change the objective.

I would hold that judgment. Only two of the seven have voiced support for changing the objective.

## JohnnyMnemonic22 | 2019-03-13T19:26:50+00:00
I wasn't referring only to the core team. I consider everyone participating in this discussion effectively a trustee. We're all responsible here. I changed the wording of my statement slightly to make that more clear.

## fluffypony | 2019-03-13T19:28:41+00:00
@geonic1 the core team members ONLY responsibilities are around finalising the upload of releases, maintaining the GitHub and GitLab repos, and owning the domains. They are not responsible for decision making.

## geonic1 | 2019-03-13T19:33:59+00:00
@fluffypony Good! I'm glad to know that my opinion is weighted equally to that of any core team member.

## antanst | 2019-03-13T20:00:31+00:00
@JohnnyMnemonic22 Apparently we have different interpretations about "the objective". Fluffypony weighed on this as well above on a direct reply to you:

> Monero's identity is that it is a privacy-enhancing technology. People don't say: "oh yes, Monero, that ASIC resistant coin", they say "Monero, that privacy coin".

## JohnnyMnemonic22 | 2019-03-13T20:16:27+00:00
Privacy is a cornerstone of Monero's philosophy, no doubt. But are we pursuing privacy purely for the sake of it? I don't think so. It's a means to freedom, accessibility, decentralization.

Also, Monero has a very well known reputation as an ASIC resistant coin. The reason I cherry-picked fluffy's mention of "botnets" is because people have been trolling our community for years about how botnets would surely be the project's demise! Monero dared to be a CPU coin when everyone else was settling for ASICs! It's who we are, and it's been our position since day one.

## hyc | 2019-03-13T20:20:24+00:00
@geonic1 
> That's a huge leap in reasoning to come to the conclusion you have. I would argue that very few people (measured as a percentage of the community) have made that leap in thinking that if RandomX fails, then ASIC friendliness is our only option. These people are technically-minded realists who are over represented in this thread. But a realist by definition can only work with currently available information. RandomX was thought up less than a year ago -- if it fails (again, there is no evidence it will), how can we be certain that a better ASIC-resistance mechanism will never be developed and that it doesn't deserve to be pursued?

While it's true, we may learn new techniques along the way, the fundamentals aren't likely to change much. For the record, I wrote the first prototype "randprog" 1 year ago. A week or so later I wrote this description. https://www.reddit.com/r/Monero/comments/8bshrx/what_we_need_to_know_about_proof_of_work_pow/ which led to @tevador's RandomJS and subsequently RandomX. I started writing it while we were preparing for the CNv1 hardfork because it was obvious then that continual PoW tweaks were not going to work.

The fundamental principle is what I outlined above in my reply to @fluffypony https://github.com/monero-project/meta/issues/316#issuecomment-472182481

The only question (in my mind) is how much deadweight in a CPU can an ASIC maker avoid, to shave off inefficiencies. tevador's work on ensuring CPU computation units are fully utilized has been top notch. If we've botched this all up and a 10x ASIC shows up, I don't believe any other approach will have a better shot.

## SamsungGalaxyPlayer | 2019-03-13T20:20:59+00:00
@JustFranz sorry, but I can't read that. I made another one. I hope it can serve as a good summary of most ideas presented here:

![image](https://user-images.githubusercontent.com/12520755/54312282-86cc4d80-45a4-11e9-8a03-0f4491450d0e.png)


## JohnnyMnemonic22 | 2019-03-13T20:21:08+00:00
> Apparently we have different interpretations about "the objective".

Let me ask you this: would this discussion even be necessary if ASIC resistance wasn't an objective? I'm not suggesting the community hasn't discussed PoW changes in the past. But why the need to "agree" on timelines and dates and all this business? Why not just swap in SHA3 when the time is right?

## antanst | 2019-03-13T20:29:36+00:00
> Let me ask you this: would this discussion even be necessary if ASIC resistance wasn't an objective? I'm not suggesting the community hasn't discussed PoW changes in the past. But why the need to "agree" sooner than later on timelines and dates and all this business? Why not just swap in SHA3 when the time is right?

Ugh, we're here because the current approach is not working anymore and has taken a toll on our project. The very same post of Fluffypony's reply to you has a pretty nice summary of the specifics; I would kindly suggest you read it and with it as well the many previous discussions on the matter. Rehashing the same points all over again doesn't add anything to this conversation.

## floridahaunted | 2019-03-13T20:42:48+00:00
I strongly believe ASICs and FPGAs will always be very rare, narrow niche equipment. Consider Bitcoin with SHA2^2 algo: only 1 to 3 companies in the whole world do make ASICs for Bitcoin. Monero has much lesser market cap, so if you grant access to ASICs/FPGAs, they'll make hard mining equipment MONOPOLY on the Monero scene too (as it is in Bitcoin scene).

So I vote to fight against ASICs/FPGAs forever. Or, till they appear in EVERY local computer stores like Intel CPU/NVidia GPU do appear in EVERY local store.

What ways of fight do I consider?

Current mining algo, cn/r has two features against ASICs/FPGAs: basic level of virtualization and basic level of randomness. But the source of randomness in cn/r is just block height, so ASICs/FPGAs manufacturers can simply pre-compile programs for some 1000 nearest blocks and embed them into their ASICs/FPGAs
(see this discussion: https://www.reddit.com/r/Monero/comments/azinzk/transcript_of_discussion_between_an_asic_designer/).

To prevent that, we have to use source of TRUE randomness. This source may be some kind of oracles that being used in Ethereum contracts for example. Or... simple LONG hash (more than 256-bit) of last 100-1000 mined blocks in the past. We may then combine this advanced randomness with advanced virtualization of RandomX. I just vote to use lesser memory in RandomX - not 4Gb, but some 256Mb, to save Raspberry Pi-like devices in the game.

If we see that advanced randomness plus advanced virtualization is not sufficient, we may think further. For example we may introduce arbitrary precision floating point computations - solutions of arbitrary (or special kind) random differential/integral equations or symbolic mathematical tasks (symbolic computation or theorem proofs etc.).

But today we can think not too far: it is just current iteration. Let's first consider and implement advanced randomness and advanced virtualization described above.

## jwinterm | 2019-03-13T21:09:18+00:00
@floridahaunted I can name more than three active manufacturers of Bitcoin mining ASICs off the top of my head: Bitmain, Halong, Bitfury, Innosilicon, and Canaan. There's a somewhat comprehensive but out of date list here: https://en.bitcoin.it/wiki/List_of_Bitcoin_mining_ASICs

The notion that there is some very high barrier to new entrants to compete in the space of ASIC manufacturing for cryptocurrency mining does not seem supported by the facts.

## JustFranz | 2019-03-13T21:32:29+00:00
@SamsungGalaxyPlayer 

Pretty much that yes. 

What happens if the ASIC work in orange never happens or the results are dissatisfactory?
When we emergency fork and a move to ASICs after isn't possible/would lead to centralization like now, do we still do it? Do we keep having 3 month emergency forks? How many POW in parallel development do we need for that?

It seems to me that we must be as involved in the ASIC process as possible, we can't wait for someone else to do something that changes the semiconductor industry.

## JohnnyMnemonic22 | 2019-03-13T21:51:22+00:00
>Ugh, we're here because the current approach is not working anymore and has taken a toll on our project. The very same post of Fluffypony's reply to you has a pretty nice summary of the specifics; I would kindly suggest you read it and with it as well the many previous discussions on the matter. Rehashing the same points all over again doesn't add anything to this conversation.

I've read fluffy's reply quite thoroughly, thank you. It contained a list of "drawbacks", some of which were valid, while others seemed like a bit of a stretch. Likewise, I suggest you review the history of this project if you feel ASIC resistance has never been an important goal of this community. It cannot be dismissed or wished away just because it's not important to you individually.

I appreciate your patience in what may seem like a circular discussion. I assure you it's not. We continue to go back to examining the technical issues and ignoring the damage that may be caused to our community by giving up the spirit of the fight.

## iamsmooth | 2019-03-14T00:41:38+00:00
@JohnnyMnemonic22 I agree with you about ASIC-resistance being one of the objectives. Now look at the actual situation. People have been doing their best to accomplish the objective, incurring significant costs in doing so, and largely not succeeding. Now what? Do we throw all the _other_ objectives under the bus in order to relentlessly pursue this one particular objective, or maybe make a narrow tactical retreat on this one objective in order to better advance the objectives of the project in a broader sense?

This is a serious question BTW. I sincerely believe that we do not have infinite resources (in fact we don't even have comparable resources to other competing projects) and if we want to accomplish the most with what we have, we need to choose our battles not only carefully, but quite selectively. What do you think?



## jtgrassie | 2019-03-14T00:46:12+00:00
> What do we want the Monero ASIC manufacturing and mining landscape to look like?
> 
> There is a clear course of action for RandomX and a success condition, sort of. I don't know what success looks like for the ASIC route, seems like the current failure condition to me.

I tend to agree with this. 

It's simple to dismiss ASIC resistance by saying things like "they are inevitable" or "we have failed thus far", but I disagree with the premise. Firstly, technology is a constantly evolving. One of the pillars of CryptoNote is egalitarian mining - which cannot be achieved with ASICs now or any time soon. It is not just a case of concern over a one single ASIC manufacturer having dominance over the network. Even with several ASIC manufacturers, you still do not get egalitarian mining. ASICs would need to be at least commodity hardware, and at best dual purpose (which of course is highly unlikely by nature). The original PoW algorithm achieved this egalitarian goal for a period of time. But ASICs evolved and we have had to evolve the algorithm in response. To date, our changes have only ever been stop-gaps simply because we didn't have something better, more feasible, for the longer term. However, @hyc et al. have come up with something really promising, as a much longer term solution and I'm very surprised this hasn't been fully embraced by all - to the point of suggesting an ASIC friendly algorithm - breaking the original and continued to date social contract of egalitarian mining. Yes of course there are also other aspects of Monero, such as privacy, that people have embraced the technology, but to suggest egalitarian mining is less important seems amiss. In my mind, we should only consider embracing ASICs if a) we have no other option or b) they become commodity hardware. Neither of these points have yet been reached. 

I for one would wholeheartedly support some kind of funding proposal to further the RandomX developers, get some serious testing done on the algorithm and therefore hopefully get this into the next October or April upgrade. And I would plead with others to support this also.

One closing footnote on RandomX - GPUs. I know there is a good chunk of the mining community that may quite likely be affected by RandomX (I say quite likely because the current state pretty much obliterates GPUs). Let's not forget a couple of things though. 1) CryptoNight was originally designed to be CPU friendly. Everyone has a CPU, everyone can buy CPUs and anyone that has the capital to build a GPU farm can invest in a CPU farm. Yes it would rock the current status quo. Yes it would drive some miners away but yes it will also create profitable mining for others. Which of course leads to the another concern raised - security of the network. Our greatest security is having an algorithm that the many can mine, not the few.

## iamsmooth | 2019-03-14T01:06:25+00:00
@SamsungGalaxyPlayer 

> Are we going to brick the ASICs that we worked with the good actors to support?

In the case where some secret presumed-bad actor has taken over a dominant position, then a fork wouldn't be bricking the good actor's ASICs, the bad actor would have already effectively done it by rendering them uncompetitive and unprofitable. It would be up to the good actors to decide if they are willing and able to invest in getting back to a competitive position, or drop out.

Sia forked their ASIC network because it had been taken over by what they considered to be bad actor ASICs (one company who had monopolized the network and tightly controlled access to the miners, selling only small quantity at very high prices). Luke-Jr has repeatedly called for forking Bitcoin to change PoW, not to get rid of ASICs (he calls for a new ASIC-friendly algorithm, in fact usually SHA3), but to get rid of and punish the current ASIC industry which he considers to be bad actors. (Of course there is no consensus in Bitcoin for the latter, but it, like the previous example, illustrates the point that the concept of forking an ASIC network isn't equivalent to undermining those considered to be good actors.)

I should make clear that I'm not really an advocate for any of these forks and I think the concept of forking as framed in this discussion inherently centralizes the network and ensures that there is indeed a central authority/cabal making the decision. That may not exactly be the core team as @fluffypony  suggests, but it will still be a relatively small number of socially-prominent de facto decision makers (with probably some overlap with the core team, but not entirely).

## MoneroCrusher | 2019-03-14T02:18:23+00:00
I strongly believe the only way to fend ASICs off is by applying game theory. Monero has the whip hand and should use it to the full extend. ASIC manufacturers are in complete dependency of Monero, so it should be made as hard as possible for them economically and risk-wise.

By doing so, I believe we can achieve true ASIC resistance without actually applying one single hardfork.
It can be achieved by commiting to a pseudo 4 month fork schedule. Pseudo because the tweaks only get prepared, but actually won't be implemented.
This is similar to a nation-state's nuclear weapons arsenal. They're there to create "peace through strength". The very same can be applied to our situation, the PoW tweaks being the nukes that likely never get used.

Let me illustrate it:
![image](https://user-images.githubusercontent.com/32360383/54326435-a8f6b780-4606-11e9-9456-fcf51278dd85.png)

On a side note:
I'm quite surprised that nobody is talking about the elephant in the room: GPU miners.
From this conversation it looks like everyone's OK with RandomX. I believe a small amount of the participants in this discussion to actually be GPU miners.
By stabbing GPU miners (including me) in the back for years of providing security, I believe it will end up in a contentious hardfork if not adressed properly. And no, 10x less efficiency compared to CPUs will not count as a solution.

So I'm in favour of:
8. or 9.
Also please add my option to your list. "ASIC Resistance by applying game theory".

## Hueristic | 2019-03-14T02:25:33+00:00
Is there any reason when we fork to ASIC friendly that we cannot make it multi ASIC algo friendly and therefore allow all previous ASICs free reign as well? ALA Myriad for all, possibly phasing those in if stability of such a fork is an issue?

## jtgrassie | 2019-03-14T02:28:13+00:00
I welcome game theory ideas but..

> By stabbing GPU miners (including me) in the back for years of providing security,

GPU miners are largely in it for profit, not security. There was lots of talk from GPU miners switching to more profitable coins over the last few months, waiting for the CN tweak to kill off ASICs, then jumping back to Monero. Yes, there maybe some GPU miners that have just been in this for "security", but to suggest most are I find highly unlikely. If a CPU favored algorithm came out, those in it for security would sell their their GPUs and reinvest in CPUs. If they are in it for profit, they'll mine other more profitable currencies.

## jtgrassie | 2019-03-14T02:32:52+00:00
Following on from my last comment wrt GPUs. Even with a CPU friendly algo, GPU mining may still be very profitable. Just a new market opens up for everybody - CPU mining also becomes profitable (CPUs have unfortunately been less and less profitable for some time with CN, a change in their favor could tilt the balance to be fairer again).

## MoneroCrusher | 2019-03-14T02:37:01+00:00
@jtgrassie CPUs and GPUs have lost performance and gained power consumption in the same pace, so that is not an argument.

The problem I see with CPU mining is that hobby miners are at a great disadvantage to professional data-centers and botnets.
While with GPU mining hobby miners are in a very unique position in it that they actually have better cost-effectiveness than even the biggest data-centers you could imagine, like Google or Amazon. Reason being that GPUs are sold in two categories: Enterprise & Consumer. The consumer grade GPUs are not sold to big datacenters and they’d have no use for them. Thus hobby GPU miners have an enormous cost advantage because they get much more bang for the buck with regards to mining and they can absolutely cheap out on literally every other component:
- Gen1/2 x1 PCIE speed with cheap risers ($2 a pop)
- 2-core CPUs ($30)
- minimum RAM ($35)
- Cheap motherboards where you can stuff in 12/13 GPUs (-> you can’t cheaply do that with CPUs) ($70-100)
- Open air rigs ($30-40)
- Ignoring dust and cheaply cool rigs or even a farm with big industrial fans (also cheap)

12 RX 570 will cost you about $1800 (new with 3 years warranty). So we have a pure compute vs. rig cost ratio of about 10:1.
A professional data-center manager would find themself in fetal position if they had to work under such circumstances. The average hobby miner doesn’t care as long as the rig is producing cryptocurrency. That’s why GPU mining is the best shot we’ve got at preserving dedicated & decentralized hobby mining. But I would very much welcome a dual PoW mechanism that preserves both CPU & GPU mining in Monero with a dynamic block reward algorithm between CPUs & GPUs. Many people get into this space by trying for themselves and seeing the system work and a lot more people have CPUs to try it on, usually after getting a taste, most people want to build something dedicated to it and that’s much easier, cheaper & effectively done with GPUs.

## Lafudoci | 2019-03-14T02:47:05+00:00
> It can be achieved by commiting to a pseudo 4 month fork schedule. Pseudo because the tweaks only get prepared, but actually won't be implemented.

But is it technichally feasible? PoW change in every 4 months means it wont't be a big change even we have dev resource to do that. ASIC designer will find the way to include the variation range in programable ASIC/FPGA. Unless there is an pow change generater and it's random enough to keep programable chip away(or at least norrow down their performance). I'm not expert so hope somone could anwser it.

## SamsungGalaxyPlayer | 2019-03-14T02:47:33+00:00
@MoneroCrusher your proposed solution may benefit GPU miners, but it severely harms the rest of the ecosystem. Committing to a 3/year hardfork schedule is tremendously difficult. Who knows if we even have the expertise to make 3 solid algorithms each year. Any fewer than 3 is likely to mean the status quo.

Monero already threatens to hardfork whenever needed to break ASICs. Moving the update a month earlier, even when we had a month to prepare, wrecked havoc on the development and localization teams. We literally had 2 days to translate the GUI and CLI. Crazy. I don't believe it's in any way reasonable to shrink the gap shorter than about a month after ASICs are widely assumed, especially if you expect this to consistently occur.

I understand you claim that "game theory" will mean Monero will not need to actually go through these hardforks, but this is crazy in my opinion. ASIC manufacturers will still profit from the ramp up until detection, then they will have about a month of network dominance even in the best case. All the while this is wrecking havoc on all the other contributors. And the GPU miners will be severely unprofitable over this period of time, just as they were in February 2019.

RandomX is a compromise for GPU miners, yes. But they ultimately still have the following options:

1. Mine Monero at a lower relative profit

2. Mine something else

CPU and GPU mining is accessible to consumers, and the equipment is easily purchased and resold. Thus, the vast majority of miners are going to mine whatever is the most profitable. Every good-natured, idealistic Monero miner will drive away another profit-driven miner to reach rough equilibrium. I think it's unrealistic to assume enough idealism-driven miners exist to provide more network power than is otherwise profitable over a prolonged period of time.

Furthermore, GPU miners under RandomX are still better off than most options. They aren't as competitive as something built specifically for them of course, but they're better off than with SHA3. I don't think anyone other than GPU miners support constant hardforks to try and break ASICs. Furthermore, I think GPU miners will still benefit from the reliability of not having ASICs appear every so often, or at least that's our best guess. Are GPU miners really better off with frequent hardforks if they aren't competitive ~2-3 months of the year?

## jtgrassie | 2019-03-14T02:52:21+00:00
@MoneroCrusher 
> CPUs and GPUs have lost performance and gained power consumption in the same pace, so that is not an argument.

This is not strictly true if you go right back to the start. GPU mining quite quickly gained a large advantage over CPUs and you are not comparing back that early.

However, you raise valid points on hobby miners vs large data-centers. One cannot ignore the fact that CPU hobby miners right now are completely priced out regardless. There are plenty of people wanting to solo mine on their laptops, desktops, RPis... they effectively are completely priced out. It's a tough one for sure.

## jtgrassie | 2019-03-14T03:01:51+00:00
@SamsungGalaxyPlayer 
> Furthermore, GPU miners under RandomX are still better off than most options. They aren't as competitive as something built specifically for them of course, but they're better off than with SHA3. I don't think anyone other than GPU miners support constant hardforks to try and break ASICs. Furthermore, I think GPU miners will still benefit from the reliability of not having ASICs appear every so often, or at least that's our best guess. Are GPU miners really better off with frequent hardforks if they aren't competitive ~3 months of the year?

Very well put.

One other point worth flagging is that we are still very early days with RandomX. I'm sure some talented GPU developers will improve the GPU code for RandomX further. Almost all the effort I've seen thus far has been on the PoW implementation itself and CPU mining code.

I'd really hope the vocal GPU miners (and the rest of us), get behind RandomX, fund further work, test etc. Right now, forking regularly is just not an option, neither is ASIC embracing. We need to work together with the best option we have, and right now, that's RandomX.

## MoneroCrusher | 2019-03-14T03:16:57+00:00
> @MoneroCrusher your proposed solution may benefit GPU miners, but it severely harms the rest of the ecosystem. Committing to a 3/year hardfork schedule is tremendously difficult. Who knows if we even have the expertise to make 3 solid algorithms each year. Any fewer than 3 is likely to mean the status quo.
> 
I agree. I don't know if the developers can come up with more tweaks to CN/R. But I do believe there are still some valid options and I can't count them with 1 hand.
> Monero already threatens to hardfork whenever needed to break ASICs. 
> 
This is not the same as having the finger on the button. With my approach as soon as ASICs get detected they get forked off almost instantly, the algo would already be reviewed and is just waiting to be launched, **in case of a very unlikely attack**.
> I understand you claim that "game theory" will mean Monero will not need to actually go through these hardforks, but this is crazy in my opinion. 

Why is it crazy? It has worked for the US & Russia the past 50-60 years.
>ASIC manufacturers will still profit from the ramp up until detection, then they will have about a month of network dominance even in the best case.
> 
They won't have a month. The algo will be reviewed and ready to launch. Maybe 2 weeks at most. Empirical data suggest that they wouldn't break even their investment after 4 months and 2 weeks, therefore it wouldn't be launched in the first place if they're motivated by economics.
> RandomX is a compromise for GPU miners, yes. But they ultimately still have the following options:
> 
As of this moment it's not a compromise it's almost complete destruction. A Vega 64 has a theoretical max of 1200 h/s. **A $160 Ryzen does 3 times more than that, while being 3 times cheaper, while using 3x less power.**
> Mine Monero at a lower relative profit
> 
> Mine something else
> 
I dont think GPU miners that built dedicated rigs for Monero will be happy with this.
> 
> Furthermore, GPU miners under RandomX are still better off than most options. They aren't as competitive as something built specifically for them of course, but they're better off than with SHA3.

Why are you only quoting those 2 as possibilities? There can be evaluations of other algorithms too. For example CN/R + 1 GB memory hardness would also be a viable solution IMO and very easily implemented without a costly audit.

## JohnnyMnemonic22 | 2019-03-14T03:24:29+00:00
> This is a serious question BTW. I sincerely believe that we do not have infinite resources (in fact we don't even have comparable resources to other competing projects) and if we want to accomplish the most with what we have, we need to choose our battles not only carefully, but quite selectively. What do you think?

@iamsmooth I think we are in a very difficult position right now having to chose between the network and the community. Committing to SHA3 is a reasonably safe, straight-forward solution and I would support it if I knew it wouldn't lead to a major division. My fear is it could really hurt what this community's culture has grown into and what makes it great.

**It boils down to this question:** are we okay with the possibility of a divided community? If everyone thinks the security benefits and freed resources are worth that outcome, then at least we carefully considered all the ramifications before taking the plunge.

If that's not a possibility we're quite ready to face, we should wait and see with RandomX and evaluate our options when/if that doesn't work out, before making any potentially disruptive commitments.

## SamsungGalaxyPlayer | 2019-03-14T03:29:20+00:00
> They won't have a month. The algo will be reviewed and ready to launch. Maybe 2 weeks at most. Empirical data suggest that they wouldn't break even their investment after 4 months and 2 weeks, therefore it wouldn't be launched in the first place if they're motivated by economics.

You're forgetting everything else that goes into a release. *Even if* new PoW algorithms are ready to go at a moment's notice, everything else isn't. Suppose ASICs are discovered and the trigger is immediately set off. The Monero community still needs to do the following:

1. Notify people of the change

2. Identify which unmerged updates will make it into the release

3. Finish and test any important fixes, including bugs that were waiting for consensus to be adopted to reduce outside exposure

4. Merge all the code for the release and begin final testing

5. Begin translating any of the touched strings

6. Do the same processes for the GUI, some of which need to wait until the daemon is complete

7. Give exchanges, users, payment processors, miners, and other services a window to upgrade

8. Create update documentation to reduce user error

9. Make sure all other ecosystem wallets update, including MyMonero, Monerujo, Cake Wallet, etc. (this is a big one that will only get bigger)

10. Do last-minute checks with exchanges, mining pools, etc

11. Have a day or two of limited network activity as the difficulty adjusts

2 weeks to do all this, several times a year? And interrupt everything else that's going on? I want to opt-out of this.

> Why are you only quoting those 2 as possibilities? There can be evaluations of other algorithms too. For example CN/R + 1 GB memory hardness would also be a viable solution IMO and very easily implemented without a costly audit.

Besides you, I do not know of anyone that believes this is a good alternative. What would that give us, 3-4 months? What other consequences are there?

## jtgrassie | 2019-03-14T03:30:01+00:00
> For example CN/R + 1 GB memory hardness would also be a viable solution IMO

Which would put CPUs at an even greater disadvantage to what they currently are.

> A $160 Ryzen does 3 times more than that, while being 3 times cheaper, while using 3x less power

Which would be fantastic for hobby miners.

I appreciate you're an invested GPU miner, but constant tweaks to CN is definitely not the answer, and the best alternative is getting behind RandomX. There is no algorithm that has been developed that provably can work well for GPUs and not ASICs.

## iamsmooth | 2019-03-14T03:31:25+00:00
> are we okay with the possibility of a divided community

To speak frankly, I think it is bullshit, and I'm calling bullshit on it.

Yeah there are some GPU miners who may be mining Monero, _today_, because it happens to be more profitable than Eth or whatever. They mine whatever is profitable and generally don't care about Monero, aren't involved much if at all with Monero beyond mining it, wouldn't miss Monero once they move on to some other more profitable coin (or give up because there aren't any) and wouldn't be missed.

Most of the people I know in the Monero community who used to GPU mine have given it up because the profitability has not been there for years. In fact, even _after_ this last "anti-ASIC" fork, the profitability is still below where it was _before_ the first anti-ASIC fork, when GPU miners were crying bloody murder and begging for help because they could not compete (see link below). During most of the rest of the year, of course, it has been even lower. This is not the kind of environment consistent with a large community of Monero GPU miners. It just isn't.

There may be a few (or perhaps more like, _one_) dinosaur GPU miners left, who are making a lot of noise about it, likely out of stubbornness or ego rather than any actual mining economics, but that's about it.

Monero mining profitability chart:
https://bitinfocharts.com/comparison/monero-mining_profitability.html

## jtgrassie | 2019-03-14T03:36:02+00:00
Thank you @SamsungGalaxyPlayer! Those that think these forks are simple are those that have nothing to do with the upgrades other than updating their mining software. The effect on the whole ecosystem (developers, users, exchanges, businesses) is huge.

And @iamsmooth, I agree. 



## iamsmooth | 2019-03-14T03:39:02+00:00
> CN/R + 1 GB memory hardness

Not feasible at all. The structure of the cryptonight algorithm requires that iterations be increased proportionately with scratchpad size in order to ensure that the entire scratchpad is used. 1 GB would require increasing iterations by 500x and would increase compute time for one hash to around 10 seconds (ignoring further increase, probably, due to higher memory latency).

There was one cryptonote coin variant that tried to something like this and it was a disaster.

Please stop trying this at home.

## MoneroCrusher | 2019-03-14T03:42:10+00:00
I think it's a valid point that was raised earlier with regards to SHA-3 or generally ASICs. Once we're commited, there's no going back. With ASICs you're handing a lot of the political decision power to their owners, while this is not the case with commoditized hardware, as they are not as commited as ASICs.

I only support ASICs once they are truly commoditized and can be easily owned by a large amount of people which I doubt will ever happen because who the hell needs a device to look for SHA-3 hashes besides a SHA-3 miner?

@SamsungGalaxyPlayer 

1 + 7:
2 weeks notice to press a download button should be enough
2-6 + 8:
This naturally gets done before the 4 month mark.
9 Maybe it's possible to better compartmentalize the code, so in case there's only a PoW change the change could be done more modular and therefore it would almost be like drag & drop, to oversimplify it. I don't know how it's handled today.
10 They are subscribed to the newsletter, they'll know what to do.
11 That's the cost.

> 2 weeks to do all this, several times a year? And interrupt everything else that's going on? I want to opt-out of this.

You're forgetting that most likely it would never actually trigger.
@jtgrassie 

> Which would put CPUs at an even greater disadvantage to what they currently are.

**To be as bold as most in this topic:** who cares about CPU miners?

> Which would be fantastic for hobby miners.

I believe it's just much more competitive and also secure to be GPU minable than CPU minable with regards to competitiveness of large data-centers with huge EPYC clusters (those do 28 kh/s each) and botnets. And less resilient against nation state attacks by super computers. Summit Ridge isn't actually that good at mining GPU minable coins. But it would absolutely destroy Monero in the blink of an eye.

## MoneroCrusher | 2019-03-14T03:43:23+00:00
> Not feasible at all. The structure of the cryptonight algorithm requires that iterations be increased proportionately with scratchpad size in order to ensure that the entire scratchpad is used. 1 GB would require increasing iterations by 500x and would increase compute time for one hash to around 10 seconds (ignoring further increase, probably, due to higher memory latency).
> 
> There was one cryptonote coin variant that tried to something like this and it was a disaster.
> 
> Please stop trying this at home.

Check out Wild Keccak. Yeah it's no Cryptonight but it's an impressive algorithm.

## JohnnyMnemonic22 | 2019-03-14T03:44:02+00:00
> To speak frankly, I think it is bullshit, and I'm calling bullshit on it.

@iamsmooth You don't think there's a possibility of a network fork? Is it that unprecedented?

## iamsmooth | 2019-03-14T03:45:47+00:00
@JohnnyMnemonic22 No, I really don't. Because I don't think there will be a sufficient critical mass of people who are really willing to carry on the very difficult anti-ASIC crusade, with all of the effort investment that entails in terms of development, releases, and forks.

We're barely able to manage it now. Someone who tries to do that with only a portion of the community and resources will be overwhelmed and give up (if they even start).

## iamsmooth | 2019-03-14T03:46:52+00:00
@MoneroCrusher I'm aware of Wild Keccak. It is very ASIC-vulnerable if used in a larger coin. Sure, it could work as a candidate for a temporary fork, if you are willing and able to keep up with the fork-of-the-day routine.


## SamsungGalaxyPlayer | 2019-03-14T03:50:45+00:00
@MoneroCrusher as someone who has not been involved in the upgrade process before, I believe you are severely underestimating the effort involved. Furthermore, delaying other consensus changes (eg: suppose bug fix requires some work on the service's end) has its own set of consequences.

## jtgrassie | 2019-03-14T03:51:07+00:00
> To be as bold as most in this topic: who cares about CPU miners?

CPUs are the most commoditized hardware available for mining. If you don't want CPUs and only GPUs, you really don't care about egalitarian mining.


## iamsmooth | 2019-03-14T03:51:17+00:00
> Summit Ridge isn't actually that good at mining GPU minable coins. But it would absolutely destroy Monero in the blink of an eye.

No it wouldn't. It is only 12 MW facility, including GPUs, which isn't enough.

Technically speaking I don't know if this is true as I don't know the exact power efficiency of POWER9 running Cryptonight, but I very seriously doubt it is anything like 30-50 H/W, which is what would be needed.

## MoneroCrusher | 2019-03-14T03:54:57+00:00
@jtgrassie I didn't say I don't want CPU mining. I was just extrapolating to give you a feel of how GPU miners feel about your talks of them being obsolete. By "you" I mean by 90% of the people in this thread.
@iamsmooth The CPU hashrate and power expenditure wouldn't be the same with a CPU-only chain.

**Anyways** It doesn't really matter if we go RandomX, CN-R + 1GB or even dual RandomX / CN-R, ASICs will reappear with static PoWs. That's why a game theoretical approach as described above is crucial if ASICs want to be kept away.

## iamsmooth | 2019-03-14T03:56:51+00:00
> competitiveness of large data-centers with huge EPYC clusters

Nothing prevents people from running a small to mid size cluster of EPYC or similar Ryzen systems (or even just one) at home or in a small farm which is proportionately competitive according to the standards of the white paper (i.e. linear with power usage). 

In fact, Epycs are now mature enough that you can start to see a lot of used servers on eBay, which has often been a very efficient way to mine Monero in the past (have not looked at recent numbers, except to say that what I saw on eBay was certainly accessible to serious hobbyists in absolute $ terms).


## iamsmooth | 2019-03-14T03:57:57+00:00
@MoneroCrusher
> The CPU hashrate and power expenditure wouldn't be the same with a CPU-only chain

I disagree. If it isn't then it becomes very profitable and lots more people start mining it. Win.


## JohnnyMnemonic22 | 2019-03-14T03:59:39+00:00
> @JohnnyMnemonic22 No, I really don't. Because I don't think there will be a sufficient critical mass of people who are really willing to carry on the very difficult anti-ASIC crusade, with all of the effort investment that entails in terms of development, releases, and forks.

@iamsmooth Does it matter if they carry on the crusade or simply go away? I wasn't suggesting there would be a competitive threat as much a threat to the interest in the project and community culture.

## SamsungGalaxyPlayer | 2019-03-14T04:00:16+00:00
@iamsmooth I would go as far to say the CPU-dominated algorithms are *more likely* to adjust to price equilibrium than ASIC-dominated or even GPU-dominated, since nearly all devices can mine these and earn profits when the hashrate is below equilibrium. CPUs have the *most* flexibility of any hardware.

## SamsungGalaxyPlayer | 2019-03-14T04:01:56+00:00
@JohnnyMnemonic22 even if I don't completely agree with you, I appreciate that point.

## iamsmooth | 2019-03-14T04:02:28+00:00
@JohnnyMnemonic22 

> threat to the interest in the project

I would agree on that point.

I'm not a natural advocate for dropping ASIC-resistasnce really, but I'm looking at a variety of tradeoffs as I mentioned earlier and seeing a poor return, considering both the costs and benefits in terms of _actual achieved and anticipated success_ (as separated from what we might want to be the case).

## jtgrassie | 2019-03-14T04:03:07+00:00
@MoneroCrusher CPU hobby mining IS obsolete, and CPUs are the most commoditized chips. Your argument about data centers and botnets doesn't hold up. Botnets can operate on CPU or GPU and @iamsmooth and @SamsungGalaxyPlayer have given good rebuttals to your data-centre argument.

## jtgrassie | 2019-03-14T04:12:58+00:00
@iamsmooth 
> Because I don't think there will be a sufficient critical mass of people who are really willing to carry on the very difficult anti-ASIC crusade, with all of the effort investment that entails in terms of development, releases, and forks.

I'd agree with this if it were solely a choice for 6 monthly (or less) "tweaks" for ASIC resistance, but we have the option of RandomX for short to mid term ASIC resistance, maybe even longer term.

## iamsmooth | 2019-03-14T04:17:15+00:00
> but we have the option of RandomX for short to mid term ASIC resistance

Short term or mid term means continued forking and/or dropping ASIC-resistance on a less planned basis and with less progress to any sort of eventual stability, and more forks.

> maybe even longer term

With emphasis on "maybe", so again we are signing up for at least a risk of ending up in the very same morass again. And, further, I doubt _anyone_ believes it will work _very_ long term or indefinitely so this still guarantees _at least_ one more fork which would then need to happen when Monero is potentially larger in terms of community/ecosystem/nodes, both practically and politically harder to fork, with more at risk.


## MoneroCrusher | 2019-03-14T04:21:04+00:00
That's why I believe it's important to set it in stone now and approach it with the only true way of being able to beat the _technically_ unbeatable ASICs.
**Game Theory**

## SamsungGalaxyPlayer | 2019-03-14T04:21:08+00:00
@iamsmooth while I understand your perspective, I still believe that RandomX is the best option in the medium-term. I don't believe that SHA-3 will work well in the short-term since we will not have enough time to prepare (to the best of our efforts) an efficient ASIC market. I believe that the earliest Monero could reasonably consider a switch to SHA-3 would be around Fall 2020. RandomX offers a likely better alternative to constant network forks, pending the audit results. I'm still mostly in favor of the rough outline in the flow chat I made a [few comments back](https://github.com/monero-project/meta/issues/316#issuecomment-472589586).

## stoffu | 2019-03-14T05:09:41+00:00
I think this ASIC resistance vs ASIC freindliness debate is ultimately subjective because there are too many unknowns. I don't think one side can realistically convince the other side to change their mind.

I started to get involved in Monero in early 2017 and soon after I also got involved in Aeon. In my eyes, Aeon's primary objective has been to make the protocol as lightweight and accessible as possible while achieving some practical level of privacy which *might* be somewhat weaker than Monero's (but one can't conclusively say Aeon's privacy is broken because privacy is such a complex matter). While having contributed to Monero by submitting and reviewing pull requests, I've also contributed to Aeon first in the effort of rebasing the codebase to a more recent state in 2018 (https://github.com/aeonix/aeon/pull/7), then by applying upstream patches and emergency fixes.

I thought keeping the CONOP (cost of node operation) small to make sure that low end devices can practically run full nodes was still Monero's top priority, but the situation seems to be changing with the adoption of RandomX. The majority of people here seem to be willing to increase the CONOP by adopting a more complex PoW (whose memory requirement seems to grow over time) so as to maintain the anti-ASIC stance that originates in the CryptoNote whitepaper. I seriously think this is a wrong choice. I believe we must abandon ASIC resistance and make the protocol more stable and accesible.

This is even more true to Aeon since its reason for existence is to be more lightweight and accessible than Monero. Given this current trend, a few weeks ago I got convinced that it's the right time for Aeon to abandon ASIC resistance (https://github.com/aeonix/aeon/pull/103). My proposal was initially met with strong oppositions by the community members, but (somewhat surprisingly) a rough (albeit not unanimous) consensus seems to have been formed, and we're now in the phase of implementing it.

I'm fine with Monero adopting RandomX because there is Aeon which I believe will survive Monero. Some may laugh at me, but I'm serious. I'll consider Monero an important project *only code-wise*, and I'll keep contributing to Monero as before (so that Aeon can benefit later), but with an implicit assumption that Monero will fall apart in a not so far future. I don't care about the name of the coin that survives in the end (FWIW I was planning to launch a new SHA-3 CryptoNote if my proposal was declined); my sole objective is to realize a fair and sustainable currency protocol that can replace the corrupt fiat system.

My main problem with RandomX is my general doubt about the technical capability of *all* the Monero developers collectively, myself included. I don't understand why people can be so optimistic about what we as a tiny developer community have come up with in such a short period of time which has received no scrutiny on par with standardized algorithms. PoW is such an essential part of the protocol, and as an amateur developer I don't feel comfortable at all in playing games with it. I respect Bitcoin in that they dare not design a homebrew PoW algorithm and simply use SHA-256 instead.


## JustFranz | 2019-03-14T06:06:36+00:00
We can't take a pro GPU-POW stance just because miners have GPUs. You say datacenters can't buy consumer GPUs https://www.pcgamer.com/cryptocurrency-miners-are-renting-boeing-747s-to-ship-graphics-cards/

What about the people buying tens of thousands of GPUs at a time and building a whole datacenter for crypto mining? 

If a GPU friendly algo is ASIC friendly then we can't risk keeping it for more than a couple of months. Maybe when we are scrambling to find POW algorithms for a 3-4 times a year POW change, but in that case we are in deep shit anyway. We must prevent that from happening in the first place and our best chance for that is a CPU-POW, which is as far removed from an ASIC workload as possible. We have a POW ready for that (RandomX), and the clock started ticking for CN-R a while ago.

Sell your GPU when the time comes and buy CPU miners. You should be slowly selling them right now, before they lose value for gamers because new cards are released or if some GPU whale dumps 20,000 cards on you. If you pay for electricity and are marginally profitable then I don't see the point in risking ASICS, new GPUs, further fall in crypto, POW changes in coins etc wiping you out.

There is a chance that ProgPow on ETH will restore some GPU mining profitability, but when is that going to happen? If? Right on time for RX 780? I wouldn't hold my breath. Even if it'll happen ETH will later go on to commit cuicide on the difficulty bomb or POS, whichever comes first. Or they transition to POS and live, which is not out of the question of course.


@iamsmooth 
> Short term or mid term means continued forking and/or dropping ASIC-resistance on a less planned basis and with less progress to any sort of eventual stability, and more forks.
> 
> With emphasis on "maybe", so again we are signing for at least a risk of ending up in the very same morass again. And, further, I doubt _anyone_ believes it will work _very_ long term or indefinitely so this still guarantees _at least_ one more fork which would then need to happen when Monero is potentially larger in terms of community/ecosystem/nodes, both practically and politically harder to fork, with more at risk.

We are going to have to assume that RandomX, as it is if/when implemented, is going to be a mid term solution. Anything else would be foolish and set us up not to be prepared for another round of ASICs. I'm optimistic though and hope that RandomX will be a better at holding off ASICs and emergency forks won't be needed.

Nevertheless I'm of the opinion that we must start working on the future ASIC-POW thing immediately and assume that we'll be forced to execute the plan when its not ready or conditions not entirely favorable.

Is anyone of the opinion that the ASIC switch should be in October? Can you explain the rationale behind it, how it should happen and what would it result in?

@stoffu 

> I think this ASIC resistance vs ASIC freindliness debate is ultimately subjective because there are too many unknowns. I don't think one side can realistically convince the other side to change their mind.
> 
I favor pragmatism 

> I thought keeping the CONOP (cost of node operation) small to make sure that low end devices can practically run full nodes was still Monero's top priority, but the situation seems to be changing with the adoption of RandomX. The majority of people here seem to be willing to increase the CONOP by adopting a more complex PoW (whose memory requirement seems to grow over time) so as to maintain the anti-ASIC stance that originates in the CryptoNote whitepaper.

The RAM requirement is because computers have RAM and it would be a disadvantage if an ASIC didn't need any. Build cost smaller and no memory controller needed on ASIC die(s). RAM access times are also part of the efficiency gap bridging strategy (i think, can't remember). 

Pruned nodes make lightweight nodes possible and RandomX has a lightweight verification mode that is slower than a full node, but it doesn't rule out low end nodes. I don't know how the verification times compare, CNv-8, CN-R, RndX, RndX-light.

> I'm fine with Monero adopting RandomX because there is Aeon which I believe will survive Monero. Some may laugh at me, but I'm serious. I'll consider Monero an important project _only code-wise_, and I'll keep contributing to Monero as before (so that Aeon can benefit later), but with an implicit assumption that Monero will fall apart in a not so far future.

While I share your fatalistic view of the whole crypto space in that different experiments must be carried out and some of them will fail, we'll all learn though and future projects will benefit.

I would very much like for Monero not to die though, what do you suggest for the October fork?

> My main problem with RandomX is my general doubt about the technical capability of _all_ the Monero developers collectively, myself included.

An audit has to be made, what do you suggest as an alternative for October then?


## iamsmooth | 2019-03-14T08:45:53+00:00
@SamsungGalaxyPlayer I would be perfectly in favor of Fall 2020 as date-certain switch to an ASIC-friendly PoW, with RandomX used in the mean time.  (In effect, this is quite similar to the two-year transition-to-ASIC timetable being used by Grin, minus the dual-PoW mining, and I think they are getting that part of it reasonably close to right.)

That said, I also don't think there is anything wrong with an immediate switch and let the arms race begin. That's basically what happens now anyway, except that instead of going through it once, we reset the race and go through the worst and most dangerous phase of it repeatedly. I disagree it is necessary for there to be a pre-existing "efficient ASIC market" and in all plausibility there may not be one for many years _after_ it goes live and turns into a revenue-generating business (but I'm also not opposed to a year +/- period, which should be ample time for ASIC developers to get ready for "go time" given that they are already doing it in 3-4 months). 

I'm not in favor of your flowchart for several reasons including the likely non-viability of 'tweaks' as a successful method of bricking hypothetical RandomX ASICs as explained by @hyc (any such ASICs would likely be highly programmable and could be adapted to most if not all such tweaks).

We need to get off this crazy train. I would not go so far as @stuffu in claiming that AEON is going to outlast Monero, but I do strongly believe that we both putting Monero at great risk and even in the absence of a sudden catastrophe, slowly but surely doing severe damage to it by virtue of the approach we are on.

## umma08 | 2019-03-14T09:05:17+00:00
I think that we need to take a step back for a second, and refactor some of this discussion, mainly so we can all agree what we are actually talking about. I see it as the following - though i am open to being corrected.

The POW strategy currently (that there was/is consensus on) is for the following outcomes:

1. Ensure that the mining market remains as egalitarian as possible.

2. Ensure that mining distribution remains decentralised.

3. Ensure that no one entity can gain a performance advantage such that they gain the potential to 51% attack. 

If everybody agrees to this, the dangers are as follows:

4. Changing POW every X months is a large strain on Monero dev resources, and cannot continue.

5. Tweaks to POW algos increase chances of error, and cannot continue.

6. Attempting to design a new POW (RandomX) does not ultimately ensure that 1, 2, and/or 3 are met. 

## SChernykh | 2019-03-14T09:13:23+00:00
> My main problem with RandomX is my general doubt about the technical capability of all the Monero developers collectively, myself included.

I think me, @tevador and @hyc combined have 50+ years of software development experience, so I wouldn't say so. What we need is qualified review from hardware engineers and also an independent audit.

## SChernykh | 2019-03-14T09:23:07+00:00
And I also think that switching to ASIC-friendly algorithm in the foreseeable future is a BAD idea.

- There WILL be a monopoly
- There WILL be KYC requirement for ASIC buyers
- There WILL be import/export restrictions in certain countries
- There MIGHT be backdoors/kill switches in these ASICs

Are you all guys suggesting this went insane?

## iamsmooth | 2019-03-14T09:36:07+00:00
@SChernykh The things you write about KYC, import restrictions, etc. are quite plausibly true. The problem is that we (the 'insane' people suggesting this) simply do not believe this can be avoided, and we want to avoid compounding further damage in getting to the same place.

Yeah, it sucks. I don't know how long you have been around crypto but in my earliest days I remember the only practical ways to trade it were to meet someone in public, pay in cash and hopefully not get robbed or abducted (or arrested), there were a lot of questions about whether governments were going to ban it outright, even whether developers would be prosecuted simply for working on it (and how smart Satoshi was for staying anonymous otherwise he'd be arrested or maybe dead).

Things are a bit 'nicer' now in some ways, but the world does not owe us (and won't always give us) a risk-free and hassle-free crypto experience.

## SChernykh | 2019-03-14T09:44:00+00:00
> The problem is that we (the 'insane' people suggesting this) simply do not believe this can be avoided

The problem is that we can only believe/not believe now, we don't have technical analysis of RandomX yet. What if it holds well? What if ASICs don't have significant advantage? We're technical people here, we can't just believe something and plan our actions based purely on belief.

## fluffypony | 2019-03-14T09:48:10+00:00
@SChernykh and you’re not concerned that RandomX is going to make the cost of running a node exorbitantly high? If it was Cuckoo Cycle where the validation is trivial it would be great, but it looks like we’re just moving towards Ethereum style thinking where we don’t care about how heavy nodes are, we can just skip validation during sync for everything below the highest checkpointed block.

## SChernykh | 2019-03-14T09:51:33+00:00
The cost of running a node is 256 MB of memory, validation time is similar to Cryptonight in this case with 30-50% potential improvement because light validation mode doesn't use JIT compilation yet. If node has more than 4 GB of free memory, it can sync much faster than now with Cryptonight. I don't see where running a node is expensive, even Raspberry Pi 3 can do it in 64-bit mode easily.

## iamsmooth | 2019-03-14T09:52:11+00:00
> What if ASICs don't have significant advantage?

Then you wait a little while, the landscape changes, new ideas are conceived on how to approach it, and then they do. And then you have to fork and start all over.

That's the problem. This is an always-unstable yin-yang approach which puts the entire system at risk.

Once you stabilize the protocol then the competitive landscape can get as close as possible to its "lowest potential energy" state and stay there (whenever there is some incremental improvement, it will quickly be adopted restoring the system back to its safe low energy state _without_ requiring a whole cycle of: develop new PoW algorithm, tweak, deploy, fork, etc.).



## SChernykh | 2019-03-14T09:55:36+00:00
Ok, I see there are apparently two factions already: "ASIC fatalists" and "Traditionalists". Is this what we wanted? This debate already causes community split, what's worse it has potential to split dev team.

## umma08 | 2019-03-14T09:56:10+00:00
> RandomX is going to make the cost of running a node exorbitantly high?

@fluffypony  

is this not determined by the RAM requirement? 

Is this not a feature, in order to deter botnet/malware deployments of mining software, which are in turn a danger for public perception, and/or decentralisation (if they are controlled by one entity)?

## iamsmooth | 2019-03-14T09:57:42+00:00
@umma08 Deterring botnet deployments has never been a goal with egalitarian mining, in fact it is contrary to it. Not so much by direct intent, but that is the core nature of the problem. Botnets are just running on the same computers as ordinary people, which no one wants to deter. You can't deter one without deterring the other.


## umma08 | 2019-03-14T09:57:44+00:00
> Ok, I see there are apparently two factions already: "ASIC fatalists" and "Traditionalists". Is this what we wanted? This debate already causes community split, what's worse it has potential to split dev team.

if we keep saying a split will/is occuring, that is exactly what will happen. 

if we keep saying that we can reach consensus on the matter in a responsible, rational and educated manner, that is more likely to happen. 

## umma08 | 2019-03-14T09:59:28+00:00
> Botnets are just running on the same computers as ordinary people, which no one wants to deter. You can't deter one without deterring the other.

@iamsmooth but all the bots are controlled by the same entity. is that not incongruent with decentralisation?



## iamsmooth | 2019-03-14T10:01:40+00:00
The bots are not controlled by the same entity. There are many different botnets found over the years. The largest haven't even been close to large enough to be a threat. What you see in popular reporting about "big" Monero malware are articles about how a botnet mined the "huge" (to the reporter) profit of $300K over a period of several months, while not considering that Monero's mining is $100K/day (was much higher in the past).

But even if they were, there is nothing that can be done if you want egalitarian mining, except perhaps focusing on helping people secure their computers better.

## iamsmooth | 2019-03-14T10:08:25+00:00
@SChernykh 

> Ok, I see there are apparently two factions already: "ASIC fatalists" and "Traditionalists". Is this what we wanted?

When we started the approach of forking for ASIC-resistance last year it was well-recognized that it was going to lead to political and other problems. Now you are seeing some of them. It will get worse.



## umma08 | 2019-03-14T10:11:27+00:00
@iamsmooth 

> It will get worse.

i don't believe that - mainly as a fork with two properly competing chains affects privacy for both chains. 

It's robbing Peter to pay Paul.

Monero people, for all our faults, would not purposefully and continually negate their own agreement with the social contract in that manner. It's just not rational. 



## iamsmooth | 2019-03-14T10:20:23+00:00
> mainly as a fork with two properly competing chains affects privacy for both chains.

I never said anything about competing chains. I'm referring to the politicking and vested interests. As @fluffypony said, we already don't know if there are agents who have infiltrated from ASIC companies to push an agenda. They spend $5-10 million on a chip, what does it cost to pay a few operatives to undermine or attempt to manipulate a community? Or for that matter, people who just want to undermine Monero for whatever reason, and use this as a convenient wedge issue. If they're not here already (who knows), they're surely coming.

If you don't think it will be much, much worse in a year or two or three when Monero is worth  more (we hope, and if we don't wreck it by undermining confidence with all these dangerous forks and an inherently unstable approach to chain security) and RandomX is failing or failed, or maybe it is but people can't agree on even that fact, much less what to do about it, you are misguided.

## umma08 | 2019-03-14T10:24:44+00:00
> I never said anything about competing chains.

@iamsmooth if you think there will not be consensus on whether to remain ASIC resistant or not, i don't see how there will not be a fork at Time X, with competing chains thereafter. For example, one with RandomX, and one with SHA-3. 

It doesn't matter who is on either side of the fork, as overall privacy is affected for both chains - unless some mechanisms are built in pre-fork to counter for this (which may be the case - i am not sure). 

## iamsmooth | 2019-03-14T10:29:42+00:00
@umma08 I think there will probably not be competing chains because the added extra challenges and costs to doing it mean that the people who would potentially support a minority chain will likely just give up and quit and go work on something else instead. 

The practical challenges to a minority chain becoming viable are large. It barely worked (depending on who you ask) with ETC or BCH, which are much, much larger and got huge financial and other support from very wealthy supporters who aren't involved with this and probably view it as too small to pay attention or care. It didn't work with MoneroV, etc. and those likely had support from the ASIC developers themselves, which are huge businesses.

I can't guarantee it won't happen, maybe I'm wrong, but it isn't the biggest concern I have about where things are headed.

There are some mechanisms to address the privacy issues with chain splits, but they are imperfect. Better than originally when there was no mitigation though.

## JohnnyMnemonic22 | 2019-03-14T10:38:46+00:00
> I would be perfectly in favor of Fall 2020 as date-certain switch to an ASIC-friendly PoW, with RandomX used in the mean time. 

@iamsmooth what would the point of that be? If we’re going full-blown ASIC, why risk something going wrong with RandomX? Might as well just switch straight to SHA3. 

RandomX only seems to make sense if we decide ASIC resistance is worth enduring. 

## iamsmooth | 2019-03-14T10:57:33+00:00
@JohnnyMnemonic22 I think some people prefer that ASICs not come until there is ample lead time so ASICs can be developed ahead of time and ideally done with direct engagement between the community and ASIC developers to hopefully get some good actors involved. (A bit of wishful thinking going on there IMO, but I'm not going to argue against since I see a date-certain switch even in the moderate future as being better than the potential of an unending and dangerous morass.)

> Might as well just switch straight to SHA3

Fine with me. And, again, it is not because I do not like egalitarian mining or because I like ASICs or how the ASIC economy operates. I don't, but I see it as the least bad approach.


## dEBRUYNE-1 | 2019-03-14T11:18:23+00:00
>Ok, I see there are apparently two factions already: "ASIC fatalists" and "Traditionalists". Is this what we wanted? This debate already causes community split, what's worse it has potential to split dev team.

There are two sides in the current debate, which is merely natural and healthy. As far as I can see, there is no split and common ground can most likely be reached. 

In addition, the path of least resistance will cause the least negative overall consequences, even if that path is not the most optimal. 

## floridahaunted | 2019-03-14T11:38:42+00:00
Guys most of you think in too generalized manner, you attempt to predict too far future, you almost admit defeat in front of ASICs... It is a bad way methodologically.

We are living in the current iteration. There is a week passed after last hard fork to cn/r. First, it must be said, there is no FPGA or quick understanding how to program FPGA against cn/r. Technically it is possible in few hours or days. But we observe low hashrate still, week passed. So they CAN'T do that quickly at least.

Thus, fight against ASICs/FPGA is POSSIBLE. Furthermore, cn/r is quite simple algo with very basic levels of virtualization and randomization. Read my comment above, what if we introduce HARD levels of virtualization and randomization? There is physics: ASICs/FPGA can't be MUCH more profitable than CPU or GPU, if quite perfect mining algo is designed.

Today, let's focus on tasks how to add strong virtualization and randomization to the algo. RandomX with memory scratch-pad reduced from 4Gb to 256Mb (to support even Raspberry Pi) is good level of virtualization.

To add randomization we may consider external oracles like ones in Ethereum contracts or long hashes (sha512, etc) applied to concatenated transactions of last 100 blocks for example. Let's think in this direction.

Fundamental physics is on our side: if mining algo has sufficient levels of virtualization and randomization, ASIC/FPGA manufacturers MUST implement Intel-like CPU! Let them compete with Intel directly!


## SChernykh | 2019-03-14T12:01:25+00:00
> There is a week passed after last hard fork to cn/r. First, it must be said, there is no FPGA or quick understanding how to program FPGA against cn/r. Technically it is possible in few hours or days. But we observe low hashrate still, week passed. So they CAN'T do that quickly at least.

Not a week, only 5 days. Some argue that FPGAs or combined ASIC/FPGAs (which are reprogrammable) are already running at xmr.waterhole.io pool and suffered ~5.5x hashrate drop. They had 55-60 kh/s on each worker before the fork, now the same workers with same IDs mine at 10-12 kh/s. This is not a direct evidence though, it can be something else. Here's a screenshot of one such worker during the fork: https://imgur.com/a/qv50PQc

> Fundamental physics is on our side: if mining algo has sufficient levels of virtualization and randomization, ASIC/FPGA manufacturers MUST implement Intel-like CPU! Let them compete with Intel directly!

More like AMD, Ryzen is 10-20% more efficient on RandomX.

## xnbya | 2019-03-14T12:03:06+00:00
I agree that the current tweaking schedule is unsustainable, and expediting it would cause further harm to the network and to adoption, so we definitely need a long term solution. However I do not believe that now is the time to embrace ASICs for many reasons, many of which others have been brought up previously, in particular @Gingeropolous

All of the tweaks to cryptonight so far have done little to increase the resistance to ASICs, so why are we even surprised that they keep appearing. Claiming that resistance is futile following from this is giving up without even trying.

A lot of people are complaining about CPU/GPU performance ratios, however this is missing the bigger picture. As long as any commodity / freely available hardware has a similar performance/power ratio to the best ASICs, this will cause a level playing field and help prevent centralization. 

Switching to SHA3 when competitive ASICs are freely available would be an ideal solution, as long as monero is not a minority chain. We would speed up client sync times, and stop miners from jumping ship to more profitable coins, and be using a solid standard hash function. However I do not believe that such a market will appear any time soon.

This brings us to the current day, when most people only have access to CPUs and GPUs. RandomX is promising and a step in the right direction, even if this makes mining on GPUs unprofitable. I would argue that focusing just on CPUs would even be beneficial, since they are much more widespread. This does cause issues with monero mining being associated with botnets, so adding certain memory requirements may help prevent this. We could even explore adding requirements for miners to have the entire (perhaps pruned) chain locally, as verifying full nodes will already have this.

Regarding verification, adding a  256MB (or even 4GB) memory requirement to nodes is a small thing to ask for, particularly if the sync times are improved. We already pretty much have a requirement for nodes to have an SSD to function with any kind of acceptable speed. 

I believe that for the time being (1-2 years), we should go ahead with RandomX. As to what we should do following this, if and when ASICs are produced for it, should be left as a discussion for the future. We do not yet know what the future will hold, and how this may affect what we should do next.

## antanst | 2019-03-14T12:15:21+00:00
SHA256 is probably not a valid choice, unless I am missing something.

The problem with picking a PoW algorithm that a coin already has, especially a coin with substancially larger market cap, is that the lesser coin becomes immediatelly vulnerable to 51% attacks, and perhaps perpetually so while it's market cap is substancially lower.

## iamsmooth | 2019-03-14T12:18:09+00:00
@xnbya 
> Switching to SHA3 when competitive ASICs are freely available would be an ideal solution, as long as monero is not a minority chain

That will absolutely never happen. There will not be a competitive market developed if there are even any ASICs developed at all, unless a coin at least as large as Monero and probably larger provides a market for it. If it is a larger coin doing it then Monero would be a minority chain. If it is a smaller coin then there might be one or possibly two ASICs, but that's it.

_Maybe_ you could start to get some foundation for this if Monero (or some other coin, but again, it doesn't meet your criteria if the other coin is larger, and probably won't work if it is much smaller) were to announce well in advance that it is definitely going be adopting it. 

Other than that you are not going to get the necessary investment without a market existing for it. 

## fluffypony | 2019-03-14T12:53:17+00:00
Regarding claims of a split, the one thing we have going for us is that the ASIC resistant side already has a name, they can call it Monero SV for Saberhagen's Vision🤣 I'm really only kidding - please don't actually do that.

@JohnnyMnemonic22 You raise a good point. If I'm being brutally honest with myself, I'd prefer we go straight to SHA3 next and not touch RandomX at all. Buuuut that would lead to a very rocky start as ASIC manufacturers rush to be the first out the gate - we'd basically need to go through the "baptism of fire" that Bitcoin had (think: Butterfly Labs;)

So, basically:

1. Pre-committing to a SHA3 date that is too far in the future might lead to another large coin adopting SHA3 ahead of us

2. Pre-committing to a SHA3 date that is too soon might lead to ASIC manufacturers not being ready with competitive ASICs

@floridahaunted Binding to an external oracle is a non-starter, let's not think in that direction at all.

## iamsmooth | 2019-03-14T13:06:31+00:00
@fluffypony 

1. Doesn't matter much. We can always use a different sensible hash function, even a slightly different but equally secure SHA3 variant, if the goal is to avoid sharing hardware with another big coin.



## fluffypony | 2019-03-14T13:07:30+00:00
@iamsmooth true, didn't think about that

## bitlamas | 2019-03-14T13:10:46+00:00
> So, basically:
>     1. Pre-committing to a SHA3 date that is too far in the future might lead to another large coin adopting SHA3 ahead of us
>     2. Pre-committing to a SHA3 date that is too soon might lead to ASIC manufacturers not being ready with competitive ASICs

I think you dropped this one:
3. Not pre-committing to a SHA3 date, but pre-commiting to it if RandomX fails.

## iamsmooth | 2019-03-14T13:16:50+00:00
@vp1111 I think 3 is largely useless. Apart from the political problems of determining when or if RandomX has "failed", you aren't going to get ASIC developers creating chips "just in case" with no idea when or even if their chips will have a market. You will be left with a situation of RandomX having failed (hypothetically) and no good alternative.

@fluffypony On the other hand, making that late switch would then reset the clock, to the extent the idea is to get ASIC development work done ahead of the launch. This probably isn't ideal. By that time we might be pretty stuck with no good options.

@JohnnyMnemonic22 Another reason to plan on a RandomX sunset is that I really don't think anyone expects RandomX to work forever, even if it does work for "a while". If there is going to be a transition from RandomX to the next thing, and there is, then setting a date to make the switch probably makes the switch less chaotic. It may also serve to somewhat deter would-be RandomX ASICs, so at least during the period of RandomX being in use it has a better chance to perform as intended.


## fluffypony | 2019-03-14T13:23:28+00:00
@iamsmooth that's an interesting point - ie. if you're an ASIC manufacturer would you rather spend the effort building a RandomX ASIC, knowing that it's only going to work for X amount of time, or building a SHA3 ASIC knowing that you'll be among the first out the gate when the switch happens?

## Gingeropolous | 2019-03-14T13:23:44+00:00
> Another reason to plan on a RandomX sunset is that I really don't think anyone expects RandomX to work forever, even if it does work for "a while"

Can you define "work" ? 

## iamsmooth | 2019-03-14T13:26:59+00:00
@Gingeropolous Keep out ASICs (or other specialized "magic beans" hardware that isn't readily available to the public).

## bitlamas | 2019-03-14T13:27:06+00:00
@iamsmooth I think 1 and 2 are largely useless. Apart from the political problems of changing a core principle of the Monero Project, you can't guarantee that its (ASIC) market is ever going to become as commoditized as CPUs, ever. You will be left with a situation where Monero mining is centralized and manipulated by some few entities. Knowing its private features, who knows how governments and other powerful entities will act next.

Let me just remind you that your prediction that _**"it's impossible to avoid ASICs"**_ is just that, a prediction. I dislike the fact that this is being discussed as a definite truth. I think in the technological world we had too many brilliant minds predicting things erroneously for us to fall into the same trap.

## zexanana | 2019-03-14T13:34:54+00:00
I can't believe the fatalistic view by some people on this topic and in RandomX in particular. It has been stated throughout this discussion and countless reddit posts the fundamental advantages to maintain an ASIC free network. In my view, a network dominated by ASICs is bound to be permissioned, defeating the point of Monero. If we go for ASIC friendly algo next october, might aswell give up on the coin entirely.

Why are we not considering adopting RandomX as the long-term algo (with maybe 1 or 2 iterations if necessary) and let the market develop ASICs for RandomX. At least the profit margin will (probably) be much narrower. Community fund a bounty for an open-source RandomX ASIC design if you so fatally believe it will fail to resist ASICs.

Am i missing something? If we're going with ASIC resistance with an algorithm that is no widely used by any other coin, might as well be RandomX and take advantage of it.

I am in no way an expert, just have a electronics and computer engineering background, but i strongly believe RandomX has a strong chance of working out, with maybe 1 or 2 iterations over some years.

## Gingeropolous | 2019-03-14T13:37:16+00:00
@iamsmooth , ok, then I think I'm on a different page. I think an ecoysystem with asic equivalence is different than an ecosystem with failed asic resistance or an ecosystem with asic dominance. 

of course, there's then the state of failed asic equivalence. 

i think we need more data. 

## iamsmooth | 2019-03-14T13:37:17+00:00
@fluffypony All else being equal RandomX because you get to deploy it now rather than "someday" (at which point even if you do get a chance to use your chip, it might be bordering on obsolete). Enormous difference in risk. Plus RandomX being trickier, if you do figure out how to do it profitably, you are more likely to have and sustain a monopoly. 

Of course, all else is not equal, they are very different projects, and they're independent too (can do either or both, or one company can do one and another company the other).

## dEBRUYNE-1 | 2019-03-14T13:40:53+00:00
@zexanana 

>Why are we not considering adopting RandomX as the long-term algo (with maybe 1 or 2 iterations if necessary) and let the market develop ASICs for RandomX.

This has been discussed before in this thread:

>This is a bad idea. If you are going to allow ASICs, you'd want to adopt a simple algorithm that has the least possible amount of optimizations. This levels the playing ground and closes the gap between ASIC manufacturers. If you leave room for a lot of optimizations, you will probably end up with a single dominating manufacturer, which is potentially dangerous for the network. Hence, my suggestion to precommit to an ASIC friendly algorithm such as SHA3 in case RandomX fails.

---------------

>At least the profit margin will (probably) be much narrower.

We don't know that. The upper-bound efficiency advantage has been predicted as 2X. I have my doubts whether that will hold if Monero is sufficiently large though. 

>with maybe 1 or 2 iterations over some years.

We're trying to get away from the tweaks, which have been shown to be futile and potentially dangerous. Why anyone considers them as a valid strategy at this point is beyond me. 

-------------------

>is just that, a prediction

Likewise, this is a prediction as well:

>You will be left with a situation where Monero mining is centralized and manipulated by some few entities

## hyc | 2019-03-14T13:42:02+00:00
@fluffypony 
> that's an interesting point - ie. if you're an ASIC manufacturer would you rather spend the effort building a RandomX ASIC, knowing that it's only going to work for X amount of time, or building a SHA3 ASIC knowing that you'll be among the first out the gate when the switch happens?

That was exactly what I was getting at here 
https://www.reddit.com/r/Monero/comments/b0ebjl/the_triangular_shotgun_method_a_gametheoretical/eieamyh/

"Game theory" at work ;)

So far we've asked a couple times "define success or failure" and nobody has addressed this. The expectation is that nobody can build a RandomX ASIC that is more than 2x power efficient than a CPU. If a 5x or 10x ASIC appears, that is clearly a failure. Aside from that, we should be considering a goalpost like "contemporary mid-level CPU or GPU is no longer profitable at current price and hashrate" as a red flag. Another red flag may be "10% increase in hashrate per day while price is flat". Let's put some concrete conditions on this because right now the pro-SHA3 arguments are just handwaving with nothing but guesses. At least the RandomX design has rational justification for each of its design points, and reasons why we think it will perform as expected.

## bitlamas | 2019-03-14T13:42:51+00:00
@dEBRUYNE-1 yes, these are all predictions, unless you have some kind of crystal ball and can read the future. I dislike the fact that this argument (it's impossible to avoid ASICs) has been thrown around as a definite truth, that's my complaint.

## iamsmooth | 2019-03-14T13:43:02+00:00
@Gingeropolous I don't agree that ASIC equivalence will exist for the most part. No one will make the up front investment to develop ASICs that don't give them an advantage. If they do, once they become obsolete they won't develop a second generation that is also equivalent, they will just abandon it.

For the most part what you are calling ASIC equivalence sounds the same as ASIC resistance to me.

It could happen I guess by accident. Someone tries to develop and ASIC and it works but not as efficiently as they intended or expected, so it ends up being (unintentionally) equivalent. This seems like an edge case that can be ignored.




## tarris034 | 2019-03-14T13:43:55+00:00
F-Great, just when we had actual promise of longer term mining without ASIC's with RandomX, we are considering switching to ASIC friendly PoW...

At least wait till tail-emission kicks in, it will be better for the network due to coins being more evenly distributed rather than owned by some big company.

## SChernykh | 2019-03-14T13:45:58+00:00
> Great, just when we had actual promise of longer term mining without ASIC's with RandomX, we are considering switching to ASIC friendly PoW...

Exactly my thoughts, RandomX can hold until May 2021 when tail emission starts.

## fluffypony | 2019-03-14T13:48:03+00:00
@hyc any metric we design can be gamed, though, so I'm not sure if that's worthwhile. I'd be a lot more keen to have a sunset date in place - we can always push the sunset date out by 6 months if we feel RandomX is working perfectly.

@vp1111 "ASICs are inevitable" is a safer prediction than "RandomX might possibly work long-term".

@SChernykh I'd be ok with that, it's effectively a 2 year sunset period set in advance.

## dEBRUYNE-1 | 2019-03-14T13:48:20+00:00
What about this course of action if most people want to keep ASICs at bay until the tail emission?

- Implement RandomX in October 2018
- Switch to SHA3 once the tail emission starts
- In case RandomX fails before that date, switch to SHA3

(I'd personally support this course of action if it wasn't clear). 

## fluffypony | 2019-03-14T13:49:08+00:00
@dEBRUYNE-1 I would support that.

## hyc | 2019-03-14T13:49:51+00:00
I see no reason to set a sunset date at all, if RandomX continues to work.

## SChernykh | 2019-03-14T13:50:30+00:00
I agree with this condition:
> we can always push the sunset date out by 6 months if we feel RandomX is working perfectly.

## jtgrassie | 2019-03-14T13:50:34+00:00
> In case RandomX fails before that date,

Define failure?

## hyc | 2019-03-14T13:50:38+00:00
@fluffypony How can  "contemporary mid-level CPU or GPU is no longer profitable at current price and hashrate" be gamed?

## dEBRUYNE-1 | 2019-03-14T13:51:49+00:00
@jtgrassie 

>What is failure?

I agree with hyc here:

>If a 5x or 10x ASIC appears, that is clearly a failure.

## xnbya | 2019-03-14T13:52:23+00:00
> @fluffypony How can "contemporary mid-level CPU or GPU is no longer profitable at current price and hashrate" be gamed?

Someone who has sha3 asics ready can rent cpu/gpu compute and mine for a month/whatever period is set at a loss to encourage the switch. Again depends on real-world conditions which we don't know yet.

## bitlamas | 2019-03-14T13:52:45+00:00
@dEBRUYNE-1 I would not support that. If it's so clear that RandomX will absolutely fail and ASICs are going to be developed, then why not change when it fails? It's so clear it will fail. It's such an useless project. Let it fail, we may change it then :)

Or something in the lines of what @SChernykh and @hyc said. Push the date if mid-level CPU/GPU is still profitable.

## iamsmooth | 2019-03-14T13:53:16+00:00
@hyc. My view is that 2x is fatal. It will drive other miners off the network. Maybe a bit more slowly and maybe not _quite_ as completely but still to a functional degree.

I don't buy the argument about differences in electricity costs. Let's say your next door neighbor has the 2x ASIC and you have a CPU. If your next door neighbor is making a modest profit as is likely for mining under most conditions (outside of a big pump), then you are losing money and will quit. This makes mining slightly (on the margin of course, not literally significantly in the individual case) more profitable for your neighbor so he buys a second ASIC. In the end the network ends up being all ASICs apart from a few dorm miners and botnets who will still remain but will be reduced to even smaller rewards by the 2x high hash rate elsewhere. _2x is huge advantage in mining_. A massive, highly contentious battle was fought in the Bitcoin ecosystem over ASICboost which is 10-20%.

@SChernykh Okay so now it seems we are debating between Fall of 2020 and Spring of 2021. Pretty much the same thing to me. Though I don't personally think the "tail emission" means a damn thing in this context (why would it make any _qualitative_ difference if block rewards are 1 XMR or 0.61 XMR or 0.6 XMR? Maybe the cutoff should be 0.9 or 2.0 or some other random number. Why not?)

@hyc Because having a set date is the only chance to actually have a non-chaotic alternative available where ASICs are developed ahead of time and ready when SHA3 is activated. Some people seem to think this is very preferable but I'm not really sure. 

## dEBRUYNE-1 | 2019-03-14T13:55:01+00:00
@SChernykh - Little side note, I think you got the date wrong. According to Moneropedia it's ~May 2022

https://src.getmonero.org/resources/moneropedia/tail-emission.html

## Gingeropolous | 2019-03-14T13:55:41+00:00
@iamsmooth , right, but when asking how you define "if randomx works", you write

> Keep out ASICs (or other specialized "magic beans" hardware that isn't readily available to the public).

So if an ASIC (or magic beans hw) exists, but its 2x, has randomx succeeded? or failed? And if cpu advancements naturally deprecate these asics, did randomx succeed?

honestly, a sunset where we just switch to sha3 is bollox. I think we need to put the onus on the asic industry to produce the damn things before we switch. They are beholden to us. Why do we have to prove we failed? Why don't they prove the succeeded?

## fluffypony | 2019-03-14T13:56:04+00:00
@hyc 

> I see no reason to set a sunset date at all, if RandomX continues to work.

Because we want to move from reactive to proactive. Imagine if RandomX works for 3 years and then someone finds a way to get a 100x efficiency gain through the Magic Beans Coprocessor. We panic-fork to SHA3, but nobody has ASICs out for SHA3, so now we have a mess of companies scrambling to get ASICs out, and we have to basically go through the birthing pains Bitcoin already went through.

> How can "contemporary mid-level CPU or GPU is no longer profitable at current price and hashrate" be gamed?

At a particular market cap the entire hashrate will be made up of large, professional mining farms They can buy in bulk at cheaper prices than hobbyist miners. They can even cut a deal with a GPU manufacturer to buy the chips from them, and then they build a custom card at significantly reduced prices. They have access to renewable power that effectively gives them an electricity cost of $0 compared to the hobbyist miners. These aren't ASICs, but to your metric they would appear to be, as they would completely crowd out the hobbyist miner, and it would appear that a "contemporary mid-level CPU or GPU is no longer profitable".

## iamsmooth | 2019-03-14T13:56:56+00:00
@Gingeropolous 
> honestly, a sunset where we just switch to sha3 is bollox. I think we need to put the onus on the asic industry to produce the damn things before we switch. 

How in the hell can they do that when they don't know when we are switching?

## SChernykh | 2019-03-14T13:57:22+00:00
>  Okay so now it seems we are debating between Fall of 2020 and Spring of 2021. Pretty much the same thing to me. Though I don't personally think the "tail emission" means a damn thing in this context (why would it make any qualitative difference if block rewards are 1 XMR or 0.61 XMR or 0.6 XMR? Maybe the cutoff should be 0.9 or 2.0 or some other random number. Why not?)

May 2022 actually, I was wrong with dates. Qualitative difference between 0.61 XMR and 0.6 XMR is that the former is NOT tail emission.

## iamsmooth | 2019-03-14T13:58:02+00:00
> Qualitative difference between 0.61 XMR and 0.6 XMR is that the former is NOT tail emission.

So what, from the perspective of mining? Whether it is called "tail emission" or not makes no _substantive_ difference as far as I can tell. 

Maybe there is indeed some reward level where it makes sense to switch based on some sort of analysis of relevant factors. Why would we just arbitrarily decide that level is 0.6 and not, say, 1.5?


## dEBRUYNE-1 | 2019-03-14T13:58:17+00:00
@jtgrassie 

>What is failure?

To add to the previous comment, in general I'd consider failure as most other miners being driven out by ASICs. A situation similar to the situation on our network leading up to the scheduled protocol upgrade would clearly be classified as failure. 

## SamsungGalaxyPlayer | 2019-03-14T13:58:18+00:00
@iamsmooth in regards to the chart many comments back now, I added the tweaks as a placeholder for the period of time between when RandomX is implemented and the SHA3 resources are built out. Ideally, this gap is 0 days, but it could be 3-6 months.

We can argue what to do in this situation more if ASICs dominate over this short period. At the moment, I have a tweak. However, other options could be immediately switching to SHA3 despite not having any preparation, going back to a Cryptonight variant until these preparations are ready, or something else.

## dEBRUYNE-1 | 2019-03-14T13:59:25+00:00
>I think we need to put the onus on the asic industry to produce the damn things before we switch.

They won't produce anything unless we commit to a date or announce that we would be switching. 

## SChernykh | 2019-03-14T13:59:46+00:00
> Maybe there is indeed some reward level where it makes sense to switch based on some sort of analysis of relevant factors. Why would we just arbitrarily decide that level is 0.6 and not, say, 1.5?

Because it won't go lower than 0.6, which makes this level _different_ from any other level.

## hyc | 2019-03-14T14:01:44+00:00
@iamsmooth 
> My view is that 2x is fatal. It will drive other miners off the network. Maybe a bit more slowly and maybe not quite as completely but still to a functional degree.

There is currently a 2x dynamic in ETH mining and yet GPU farms are still the dominant hashrate. To me this disproves your "2x is fatal" assertion.

## dEBRUYNE-1 | 2019-03-14T14:01:58+00:00
It can also be argued that the tail emission date has some kind of sentimental value, as the initial emission would've been mined then. It would thus perhaps be better then to set the switch on this date than any other 'random' date. 

## tarris034 | 2019-03-14T14:02:24+00:00
> > I think we need to put the onus on the asic industry to produce the damn things before we switch.
> 
> They won't produce anything unless we commit to a date or announce that we would be switching.

exactly, why would they risk now that they know we are capable of emergency PoW change, with much more resources needed to spend on chip dev.

RandomX would require much more money and time to develop and we can "tweak" it once per year for that matter.

I think we are getting too much paranoid about those ASIC monkeys.

## dEBRUYNE-1 | 2019-03-14T14:03:22+00:00
>we can "tweak" it once per year for that matter.

Tweaking has proven to be a futile and potentially dangerous strategy. Why anyone would even consider to use it as strategy in the future is beyond me. Besides, [@hyc stated](https://www.reddit.com/r/Monero/comments/b064vz/discussion_of_the_future_of_the_pow_algorithm/eifalyd/) that tweaking would even be less effective with RandomX. 

## tarris034 | 2019-03-14T14:06:44+00:00
Going ASIC is like stepping into shit intentionally to avoid doing it by mistake. Hope the best for network.
Just my last 2c. See ya.

## jtgrassie | 2019-03-14T14:08:27+00:00
> Tweaking has proven to be a futile and potentially dangerous strategy.

I maybe wouldn't put it this strongly but in general agree.

Perhaps the sensible route is: RandomX next upgrade with a sunset date for switch to SHA3, if RandomX doing really well potentially push sunset date, if some serious issue with RX either revert to CN or forward sunset date.

## Gingeropolous | 2019-03-14T14:12:11+00:00
if sha3 asics are so cheap and easy to do, why don't the manufacturers just start adding sha3 chips to their current asics? Then they will be out in the wild.

there's a way to beat this chicken and egg. 

## iamsmooth | 2019-03-14T14:13:10+00:00
@hyc. The Ethereum mining profitability has crashed to sub-basement levels (far below where it was even pre-pump). I don't think it would satisfy your criteria for reasonably profitable on standard equipment at all.

There may be an installed base of GPUs that is still mining it using free hydropower in China or whatever, but it isn't profitable or accessible to someone without free or near-free electricity.

It also may be that the transition is still playing out, or that GPUs aren't actually dominant (how do we know?). Aren't a lot of the Ethereum ASICs of the secret/self-mining "bad actor" variety?

## dEBRUYNE-1 | 2019-03-14T14:15:44+00:00
>if RandomX doing really well potentially push sunset date,

We can't indefinitely push it out though (as it would deter ASIC manufacturers from starting development). Perhaps we should add a limit of 6 months (in case this path is chosen). 

## iamsmooth | 2019-03-14T14:16:00+00:00
@jtgrassie We can't push the sunset date or it undermines ASIC pre-investment.


## dEBRUYNE-1 | 2019-03-14T14:16:51+00:00
>We can't push the sunset date or it undermines ASIC pre-investment.

A 6 month push would still be acceptable I think. 

## SamsungGalaxyPlayer | 2019-03-14T14:17:24+00:00
@iamsmooth I generally disagree. If we have open designs ready (or otherwise help meet them halfway) and can commit to upgrade in 3-6 months, it seems like most manufacturers will be able to put something together.

## iamsmooth | 2019-03-14T14:20:35+00:00
@SamsungGalaxyPlayer If we're committing to upgrade at a particular time, whatever the lead time (including zero IMO, but certainly 3-6 months is fine), then its all good. What I'm objecting to is expecting manufacturers to spend their own money to get to production and then having some flexible launch date base on how RandomX is doing.


## fluffypony | 2019-03-14T14:20:46+00:00
@Gingeropolous I don't get what you're saying - why would they waste the money producing a SHA3 chip?

## SamsungGalaxyPlayer | 2019-03-14T14:22:13+00:00
> What I'm objecting to is expecting manufacturers to spend their own money to get to production and then having some flexible launch date based on how RandomX is doing.

This is why I prefer we **don't** set a firm sunset date years in advance. I think setting the sunset date 3-6 months after we are dissatisfied with RandomX is sufficient.

## antanst | 2019-03-14T14:23:35+00:00
> If sha3 asics are so cheap and easy to do, why don't the manufacturers just start adding sha3 chips to their current asics? Then they will be out in the wild.

Why would they do that? Are they going to spend millions just in case someone decides to use SHA3 as a PoW?

@SamsungGalaxyPlayer 
> This is why I prefer we don't set a firm sunset date. I think setting the sunset date 3-6 months after we are dissatisfied with RandomX is sufficient.

If our goal is to introduce ASICs in an as fair way as possible, there's no point in having RandomX and then indefinitely postponing SHA3 until we're not satisfied with RandomX, whatever that means. Nobody will build an ASIC "just in case" we switch at some point in the future.

If we go the ASIC way, and want to be taken seriously, better do it the right way and precommit to a date for the switch. It doesn't matter if it's going to be 1 year or two. It's the plan that matters and sticking to it.

## iamsmooth | 2019-03-14T14:28:32+00:00
> This is why I prefer we don't set a firm sunset date years in advance

Easy solution then. Set it six months or a year from now and be done with it. No further risk of whether or not RandomX actually works on a sustained basis, and ASIC developers can get started on whatever schedule is most efficient for them, be it 3-6 months or somewhat longer.

If we know where we are going to end up, then there's no reason to keep the network at risk with a speculative home-brew algorithm that _might_ work for any longer than necessary, nor to expose it to the risk of needing an urgent fork (and/or have yet another ASIC takeover of our "ASIC-resistant" algorithm which has both immediate security and reputation costs) at some inopportune time because the RandomX ASICs decided to wake up and appear according to their schedule and not ours.




## jtgrassie | 2019-03-14T14:35:48+00:00
I don't buy into the idea it's unfair to set a sunset and push it out, maybe indefinitely. ASIC manufacturers have shown themselves to be very agile, coupled with the fact that once they have a design, they just just delay a production run. Their investment is thus just in the design. It's a risk, but then look, they have been happy taking risks thus far, why would they not take on this risk?

## hyc | 2019-03-14T14:37:07+00:00
> Why would they do that? Are they going to spend millions just in case someone decides to use SHA3 as a PoW?

Why should we switch to SHA3 just in case multiple companies decide to build chips for it? What if only one company does? Monero still is small potatoes in market cap, why would more than one company bother? Why do we just *assume* that a fair and open ASIC market will materialize out of thin air, when no such thing has occurred over these many years for any other ASIC-mined coin?

## Gingeropolous | 2019-03-14T14:39:15+00:00
so we're back to "we'll switch to sha3 no matter how successful randomx is", so great. 

> If our goal is to introduce ASICs in an as fair way as possible, 

There is no fair way. ASICs don't exist in a fair fashion. 

This effectively sets in stone how block generation is performed. So there goes any attempts to further fix this underlying problem, including pool distribution and how pools distribute work. 

The easy solution is to switch to sha3 tomorrow. Lets end this charade now. I feel bad for all of us who have wasted our time.  

Good thing we can keep selling "blockchain solutions". Yes, Monero, the " privacy coin." 

I guess just one more thing. I didn't get into monero because it was a privacy coin. I got into monero because its the only damn cryptocurrency thats actually a cryptocurrency. To work, you need to be decentralized. To work, you need to be fungible. 

People that refer to Monero as a privacy coin are the same people that think "blockchain technology" is a thing. 

## dEBRUYNE-1 | 2019-03-14T14:40:28+00:00
>why would more than one company bother? 

Multiple companies developed an ASIC for the original CryptoNight algorithm, which can be considered vastly more complex than something like SHA3. 

## fluffypony | 2019-03-14T14:42:52+00:00
@hyc we have evidence in that 3 manufacturers had ASICs announced by the time we performed the first switch, plus another one (or maybe 1 of the 3) that has just had their ASICs forked off the network. In both these instances it was for an ASIC that was much more complex than a SHA3 ASIC, and on a network that was known to be hostile to ASICs, yet they did it anyway. How much more so would many of them not manufacture an ASIC for Monero? 

Also I'm not sure why you think that a fair and open ASIC market doesn't exist for Bitcoin? There are a bunch of manufacturers (https://www.asicminervalue.com/manufacturers), and they are easily accessible. There are just 2 GPU manufacturers and 3 CPU manufacturers that are at all relevant, and the barrier to entry to create a new GPU or CPU is incredibly, incredibly high. The barrier to entering the ASIC mining space is much lower.

## tarris034 | 2019-03-14T14:44:43+00:00
ASIC will kill home miners like it did to Bitcoin miners.
We just can't compete with large scale operations that are usually based in countries with much lower power cost.

Thus decreasing decentralization and security of the network.

## antanst | 2019-03-14T14:45:30+00:00
> Easy solution then. Set it six months or a year from now and be done with it. No further risk of whether or not RandomX actually works on a sustained basis, and ASIC developers can get started on whatever schedule is most efficient for them, be it 3-6 months or somewhat longer.

That sounds the most safe way to do this, agreed.  I always saw RandomX as a possible intermediary step that will allow us to avoid the tweak-and-fork mess for some time, but if the risk that comes with it is deemed substancially higher, then indeed your proposal is the safer way to go.

@jtgrassie ASIC manufacturers have proven to be very agile once the motives have already set in and they see (even short-term) profitability in their endeavour. Developing a new design to for a hypotherical PoW switch that may or may not happen in the future is a different story; that needs assurances and trust.

@hyc 
> Why should we switch to SHA3 just in case multiple companies decide to build chips for it? What if only one company does?

There's no way to know this, and it depends on multiple factors unknown until that time comes. But we can help *steer* it this (edit: the right) way.

## fluffypony | 2019-03-14T14:45:42+00:00
@tarris034 A higher market cap will kill home miners. What do you recommend we put in place to prevent Monero's market cap from going higher and thus attracting large-scale mining farms?

## tarris034 | 2019-03-14T14:46:44+00:00
I'm not fully against the idea, just wish it will be at tail emission.

## iamsmooth | 2019-03-14T14:47:11+00:00
@dEBRUYNE-1 
> Multiple companies developed an ASIC for the original CryptoNight algorithm

Well the price was higher, but you're right its likely a fair bit more challenging than SHA3

There have been three companies that produced ASICs for Sia as well, which is smaller than Monero in market cap (though not sure about mining rewards). It hasn't really worked out great so far, so not really something to seek to emulate, but on the narrow point of multiple companies producing ASICs, it is further evidence.

I don't really expect any sort of healthy ASIC market right away, possibly someday, but maybe never. What I see as the benefit is being able to stabilize the protocol and not have to do forks (including emergency forks) on a reactive basis, and get the process in motion to where if there is actually a chance of a healthy ASIC market forming eventually, we get there sooner by starting the process and not postponing the inevitable.


## hyc | 2019-03-14T14:48:01+00:00
Pretty much all of those ASIC manufacturers have also proven themselves untrustworthy
https://www.reddit.com/r/Bitcoin/comments/2huksd/psa_stop_buying_asic_mining_hardware_they_are_all/

We are literally rolling out the red carpet for scammers, by taking this path.

## fluffypony | 2019-03-14T14:49:19+00:00
@hyc that's a thread from 4 years ago, the market is very different now.

Edit: it literally warns people to stay away from Butterfly Labs, HashFast, and Cointerra😆

## zexanana | 2019-03-14T14:49:20+00:00
I wouldn't set a date until it is demonstrated it has failed, otherwise it is giving up before the battle started. Setting a date and then not honoring the change is not respectable.
In my opinion we would work on a way to measure the failure, if at all possible, and if failure is confirmed, enough time has passed (hopefully) and we can make a decision to switch to ASIC-friendly with more information and a more mature environment. At this point we may have more experienced developers and an even better RandomX version can be created.
If time is required for pre-ASIC development we can still resort to 2x 6 month tweaks to gain some time.
In my opinion all these risks (going back to tweaks, iterating on RandomX) far outweight the scenario of an ASIC dominante network.

## iamsmooth | 2019-03-14T14:50:04+00:00
@hyc 
> 4 years ago

That was a _VERY_ different environment. Indeed nearly all miner companies were scams. Ironically the one (and quite possibly the _only_ one) that entirely wasn't a scam back then was Bitmain.


## hyc | 2019-03-14T14:52:56+00:00
It hasn't changed all that much. 2018: https://coinatory.com/2018/08/03/watts-miners-asics-a-scam/

## fluffypony | 2019-03-14T14:55:10+00:00
@hyc that's a fake company with a fake announcement asking for pre-orders. I don't see how that's any different from a fake company announcing a RandomX miner that gets 10x efficiency gain and asking for preorders? Preventing that from happening is out of scope.

## hyc | 2019-03-14T15:00:11+00:00
How do you expect consumers to tell the difference?

Today, we know for a fact, if a competitive ASIC exists, *it will not be advertised* and any such fake company can immediately be spotted as a scam. Once you announce ASIC-compatibility, it will be much harder to know this until after people have lost their money.

## fluffypony | 2019-03-14T15:03:47+00:00
Doesn't matter, it's still out of scope. We shouldn't compromise the security of the network just because someone might be scammed somewhere along the way, otherwise we're back to centralised tweaks every 3 months.

Besides, if Ezekiel Osborne can claim to have invented Monero, some company is going to claim they have Monero ASICs and are accepting pre-orders. Just because we kick up a fuss doesn't mean it's going to stop people from throwing money at either Ezekiel or the fake ASICs.

## xnbya | 2019-03-14T15:08:11+00:00
@dEBRUYNE-1 
> Multiple companies developed an ASIC for the original CryptoNight algorithm, which can be considered vastly more complex than something like SHA3.

Take a look at the current hashrate distribution for ETN, which switched back to the original CryptoNight algorithm. (https://miningpoolstats.stream/electroneum) - 60% of hashrate controlled by a single entity. And this is with multiple manufacturers.

## Gingeropolous | 2019-03-14T15:10:32+00:00
> What I see as the benefit is being able to stabilize the protocol and not have to do forks (including emergency forks) on a reactive basis, 

So we're not going to do non-PoW forks anymore either?
 
> and get the process in motion to where if there is actually a chance of a healthy ASIC market forming eventually, we get there sooner by starting the process and not postponing the inevitable.

I think this is a fantasy.

Can't we just see how RandomX performs? I still don't get the fatalism. Lets let it run for a year, and then set in motion some sunsetting. Whats another year the asic manufactures have to wait? 

"Here's a cure that might save you"

"No thanks, I've seen it written in the heavens, this is my fate"

## tarris034 | 2019-03-14T15:11:18+00:00
ASIC is a failure all alone in terms of crypto. Even in Bitcoin big companies can't handle it and only the biggest ones survive - making it centralized in the end.

## Gingeropolous | 2019-03-14T15:11:28+00:00
i mean if randomx is a total dud, then i'll gladly eat my words and a couple ASICs. ASIC-stew. 

## dEBRUYNE-1 | 2019-03-14T15:14:58+00:00
@Gingeropolous 

>So we're not going to do non-PoW forks anymore either?

A fork with a PoW switch included is vastly more disruptive. I don't think anyone wants to get rid of scheduled protocol upgrades that don't include a change of the proof-of-work algorithm. 

@xnbya - There's little value in using that as example. ETN has a market cap of $65M and is using a complex algorithm (remember that CryptoNight was initially designed to be ASIC-resistant). Besides, my point was that multiple manufacturers existed (and not a single one). I didn't say anything about the hashrate distribution. 

## iamsmooth | 2019-03-14T15:15:25+00:00
@Gingeropolous 
> So we're not going to do non-PoW forks anymore either?

Read what I wrote: "on a reactive basis"

We can do development forks and roll out updates on a sensible schedule whatever turns out to be. Ideally they are pure improvements that are consistently non-contentious. Perhaps on occasion there _might_ be the need for an unplanned/emergency in case of a major bug, but at least that isn't baked into the plan and again should always be entirely non-contentious.

Discretionary forks that make a judgement on whose miners to brick when and why are very different, particularly when they on done in reaction to network conditions that aren't even always unambiguous.

## tevador | 2019-03-14T15:17:14+00:00
@iamsmooth 
> My view is that 2x is fatal. It will drive other miners off the network. Maybe a bit more slowly and maybe not quite as completely but still to a functional degree.

Aside from the differences in electricity price  (which I still think is a valid point), the situation is different for CPU-mineable algorithms. An ASIC or GPU farm cannot do anything but mine, but there are literally millions of CPUs in many datacenters across the world that sit idle most of the time and could mine with much lower operating cost than a dedicated basement CPU rig. 

I talked to one person in supportXMR pool chat who owns a hosting company and runs hundreds of single vCPU virtual machines that mine XMR when the host machine is not fully used (this is not visible to the customers). He gets money from hosting websites and mining at the same time.

Addtionally, there would be botnets and miners who don't care about operating costs as long as they can earn at least the minimum pool payment in reasonable time.

That's why I don't believe a 2x efficient ASIC would be too disruptive.

## MoneroCrusher | 2019-03-14T15:19:22+00:00
@dEBRUYNE-1 Could you please add [this](https://github.com/monero-project/meta/issues/316#issuecomment-472677985) to your list on top? 

## tarris034 | 2019-03-14T15:21:41+00:00
> @dEBRUYNE-1 Could you please add [this](https://github.com/monero-project/meta/issues/316#issuecomment-472677985) to your list on top?

I love this idea, very smart.

## SChernykh | 2019-03-14T15:24:53+00:00
Everyone seems to have forgotten that there is also a third alternative: FPGA-friendly algorithm.

If it turns out impossible to make ASIC-resistant CPU or GPU algorithm, FPGAs have much better chances for this. Why we even consider SHA-3? We can come up with FPGA algorithm which will eventually replace RandomX.

FPGAs are general purpose devices, they're more easily accessible to end users and they can be 10-100x faster than GPUs. Intel is planning to integrate FPGA in their future CPUs.

FPGAs at 16 nm process node are just as fast as 65 nm ASICs on anything, so performance gap between FPGA and ASIC on _any_ algorithm is much smaller. And it's possible to design an algorithm that can't be done faster on an ASIC than on FPGA.

## fluffypony | 2019-03-14T15:36:39+00:00
@xnbya 

> Take a look at the current hashrate distribution for ETN, which switched back to the original CryptoNight algorithm. (https://miningpoolstats.stream/electroneum) - 60% of hashrate controlled by a single entity. And this is with multiple manufacturers.

A single pool is not the same as a single entity. Monero has had a single pool creep up to 50% of the hashrate in the past despite not having ASICs, the only reason it changed is that people complained and some miners switched to another pool. Let's not muddy the waters with comparisons that are obviously incorrect, please.

@tevador By that argument then we're going to get nailed by botnets and malware, who have WAY more CPU power on tap than datacenters willing to mine Monero. It's also not going to work if those datacenters end up being priced out by mining farms with access to cheaper electricity.

## iamsmooth | 2019-03-14T15:36:41+00:00
@tevador We can get a pretty good estimate of the scale of "free" miners like you mention (botnets, sysadmins, etc.) by guestimating the hash rate when the price is relatively low and there are no ASICs, FPGAs, magic beans, on other exotic gear on the network. Obviously we never know with certainty what is on the network, but overall if you look at these numbers the estimate you get is quite low, 100 MH or less, possibly as low as 10-50 MH (normalized to CPU cryptonight). 

What happens when the price goes up is that the worldwide supply of these "free" miners is tapped out, and the equilibrium profitability then starts to rise (to the extent they were not tapped out, they would certainly join the network in even greater numbers in response to the higher revenue and push the profitability back down; I'm sure they do, but the extent is limited, because the profitability still is observed to go up a lot during significant price increases).

Given the current (presumed ASIC-ejected) hash rate of about 300 MH, that means these "free" miners represent somewhere between 10-30% of the network. If the rest switches to 2x ASICs then the total hash rate goes to about 500 MH and their share drops to 8-20%. That's not nothing; even 8-20% decentralized hash rate does add significant robustness to the network in general. But doesn't protect the network from a de facto ASIC takeover, and it also doesn't maintain profitability at a level where any significant number of non-"free" miners without ASICs can practically participate (in any sort of "egalitarian" sense). You end up with something like 80-90% ASICs and 10-20% non-ASICs (the latter being mostly "free" miners).

## iamsmooth | 2019-03-14T15:42:31+00:00
@fluffypony The evidence we've seen is that botnets get tapped out. Indeed in 2019 it's probably the case that every single botnet operator in the world knows about Monero mining by now and any botnet that by its nature is suitable for mining Monero is already mining it. Yet it doesn't represent the bulk of the hashrate or anything close (even during presumed non-ASICd windows).

@SChernykh Interesting point about FPGAs but I don't understand this:

> FPGAs at 16 nm process node are just as fast as 65 nm ASICs on anything, so performance gap between FPGA and ASIC on any algorithm is much smaller.

Many competitive ASICs are now being built on 28nm process (maybe/probably not the short-shelf-life cryptonight ones, but they are for other coins) and some are trying smaller. How will these 65nm-equivalent FPGAs be able to compete with that?


## SChernykh | 2019-03-14T15:45:13+00:00
> How will these 65nm-equivalent FPGAs be able to compete with that?

I'm talking about "ASICable" algorithms like SHA3. FPGAs will be competitive with 65nm ASIC. But if the algorithm is _designed_ for FPGA, 16nm ASICs and 16nm FPGAs will have the same performance.

## iamsmooth | 2019-03-14T15:47:10+00:00
@SChernykh 
> But if the algorithm is designed for FPGA, 16nm ASICs and 16nm FPGAs will have the same performance 

Okay, if you can demonstrate and prove out such an algorithm it certainly seems like an interesting approach. Maybe not even for Monero necessarily but if it did behave that way, it has properties that seems like they could be useful in general.


## SChernykh | 2019-03-14T15:52:29+00:00
@iamsmooth
>  if you can demonstrate and prove out such an algorithm it certainly seems like an interesting approach.

I'm not an FPGA designer, but I read FPGA discord a lot and heard such claims.

What's good about FPGAs is that they're general purpose and reprogrammable. You can mine with them one day and then do something else computationally hard the next day.

## tevador | 2019-03-14T15:53:21+00:00
@iamsmooth I don't think your estimate would hold up for RandomX. Right now, CPU miners (whether they mine for free or not) already compete with 2x more efficient GPUs. The relatively low price of XMR also has an effect on who chooses to mine (even "free" miners have to expend some work or capital to start mining).

## iamsmooth | 2019-03-14T16:04:54+00:00
@tevador If true then you can ignore the 2x increase on the rest of the network because it already counted, and you are still left with the original 10-30% "free" miners and 70-90% ASICs. Not that different.

Indeed your example of GPUs having a 2x advantage and dominating most of the non-"free" hash rate currently kind of demonstrates the point. 2x GPUs are economically equivalent to 2x ASICs.

## tarris034 | 2019-03-14T16:13:59+00:00
> @iamsmooth
> 
> > if you can demonstrate and prove out such an algorithm it certainly seems like an interesting approach.
> 
> I'm not an FPGA designer, but I read FPGA discord a lot and heard such claims.
> 
> What's good about FPGAs is that they're general purpose and reprogrammable. You can mine with them one day and then do something else computationally hard the next day.

ASIC's are even bricking them self by building new more efficient ones, not eco-friendly at all.

## MoneroChan | 2019-03-14T16:20:00+00:00
I propose we Exploit the ‘Cryptonight-R’ effects on the 'ASIC-ROI threshold' to buy us more time:

Here is how this exploit works:

- Previously, assume ASIC's always just ROI'ed before the hard fork, and the manufacturers Profited.

- Now, Cryptonight-R slows down ASICs so much it might actually be possible to destroy them "Before" they ROI.

- With Cryptonight-R, our Nuclear option (hard forks) are now 'A Major threat' to ASIC manufacturers, enough to cause stalemate, previously not practical.

- ASIC manufacturers know this. I've overheard ASIC users wishing we switch to RandomX because of CN-R's ability to create stalemate. ASIC manufacturers want us to waste a Relatively Very Powerful hard fork, so they can work on RandomX ASICs right away.

- I propose we use their own Nightmare against them.

I propose the following strategy based on the above:

1. We exploit the slower ASIC's reduced ability outrun the next "CNR to RandomX" fork.

2. We maintain Cryptonight-R as long as possible.

3. We prepare 'RandomX' in the background for a very rapid emergency hard fork when ASICs appear for CN-R.

4. This creates a “Very Special Situation” where ASICs won't be created (Nuclear Stalemate), because this time, any manufacturer knows they will lose money if they try to create ASICs. 

5. ASIC manufacturers will be unable to make a huge amount of ASICs that can mine fast enough to ROI, as they are too slow now with Cryptonight-R and they will be detected and will be destroyed before they ROI.

6. So by keeping Cryptonight-R active, with RandomX on standby as nuclear deterrence, ASICs won't be created for a long time, even if they can.

I don't know how long this stalemate can last, 6 months, 1 year, 2 years or more,
but what i do know for sure, is that we should not waste this unique opportunity offered to us by Cryptonight-R to create a Nuclear stalemate, and not just throw it away for RandomX (without at least bricking some ASICs first.)

Any thoughts?
@SChernykh 
@MoneroCrusher
@fluffypony 

## MoneroCrusher | 2019-03-14T16:27:37+00:00
@MoneroChan 
Love this idea. Switch the current SHA-3 "sunset" with RandomX.
I too think we shouldn't just dismiss Cryptonight-R because as I stated in my "game theory" article. I believe a 6 month fork schedule might already be enough with the current implementation.

It all depends on the cost of the manufacturers.
Imagine they targetted a 300% ROI for the 6 month schedule. If the CN-R claims are true, then this becomes 100% ROI and they won't make any profit and therefore not deploy any ASICs. It's definitely worth watching the effect of CN-R.

I don't like how everyone dismisses our current path as "failed", when in fact it has only failed *so far*, which in reality was only one algo, not two. Since CNv1 was not intended as ASIC deterrent but just a stop-gap.

## AirSquirrels | 2019-03-14T16:29:56+00:00
I can say that we’ve already adapted our RTL/Verilog to CN-R, and overall hashrate is identical to CNv2 with a 10% increase in area. This is on FPGAs with HBM where raw cost means the economics don’t work, but it does hamper the expectation that CN-R will significantly make ASICs slower, depending on their architecture.  

## tarris034 | 2019-03-14T16:31:28+00:00
> I can say that we’ve already adapted our RTL/Verilog to CN-R, and overall hashrate is identical to CNv8 with a 10% increase in area. This is on FPGAs with HBM where raw cost means the economics don’t work, but it does hamper the expectation that CN-R will significantly make ASICs slower, depending on their architecture.

Proves or just wind talking ?

## MoneroCrusher | 2019-03-14T16:34:00+00:00
You can't come in here saying that without any sort of proof (I mean you can, but why should we believe you). GPUhoarder said the BCU only did 5 kh/s on CNv8, which is negligible. In that case I have absolutely nothing against FPGAs.

I'm all for CPU, GPU and "fair" FPGA mining. ASICs, big no, since it's not egalitarian.

## SChernykh | 2019-03-14T16:34:31+00:00
@tarris034 FPGAs with HBM can do this indeed, they're just as good as GPUs when handling CN/R tweaks. GPUs didn't slow down, FPGAs with HBM don't have to slow down either.

What they failed to mention is that FPGAs with HBM can't do more than 5 kh/s both on CNv2 and on CN/R.

## AirSquirrels | 2019-03-14T16:42:00+00:00
@SChernykh is correct (we discuss this frequently). What I was alluding to was that v2 ASICs probably didn’t play into the latency game, just like FPGAs, and have gone to large pipelines with high latency. If that is true then the only cost of of CN-R aside from tapeout is about 10% more area. 

I was asked to comment on FPGAs in general and the options for ASIC resistance. There are certainly routed that can be taken. CN-R for one simply doesn’t have a long enough random math pipeline to make the cost of pipeline registers to hide the latency high enough. 

## SChernykh | 2019-03-14T16:45:57+00:00
@AirSquirrels I don't think CNv2 ASICs went for high latency-high throughput implementation. They need a lot of external (DDR or HBM) memory bandwidth for 128 KH/s, not really feasible.

The main question: Is FPGA-friendly algorithm possible? I mean the one where ASICs can't have an advantage.

## AirSquirrels | 2019-03-14T16:50:52+00:00
You can still go high latency on-chip on many chips. Depending on process node and target hash rate per chip, low hundreds of MB would be enough - including eDRAM options. 

## SChernykh | 2019-03-14T17:01:38+00:00
If you're right we'll see 1 GH/s by the end of June, but I don't think so. We know from nonce analysis that single CNv2 chip did 400 h/s (it probably had multiple cores to achieve this hashrate). It would require 51 GB/s bandwidth, one eDRAM chip is far from enough for this.

I'm more curious about FPGA-friendly algo. I would hate to buy SHA3 ASIC (and eventual doorstopper) to mine Monero in the future. General-purpose FPGA is so much better because it can be repurposed for basically anything else.

## MoneroCrusher | 2019-03-14T17:04:53+00:00
I'm not a fan of a FPGA-only algo since many people don't have the technicaly capability of handling them. Additionally no consumer grade PC will ever come with a FPGA, only thing I see in them are CPUs & GPUs. However, I very much welcome FPGA into the mining space for those that want to mine on them (no need to actively discourage them).

## SChernykh | 2019-03-14T17:10:15+00:00
@MoneroCrusher I only like it in the context "ASIC or FPGA". FPGA miners are also easier to create. Basically any startup company can order FPGA chips and develop bitstream and create a board for them. They won't have to go through "silicon wafers" production stage which is most cumbersome.

## MoneroCrusher | 2019-03-14T17:13:50+00:00
@SChernykh In that case yes, I'd also prefer that. But I think it's way too early to give up on ASIC resistance, we have only lost 1 battle so far.

## tevador | 2019-03-14T17:42:45+00:00
@iamsmooth If you insist on this analogy, you should realize that CPU mining is still profitable at half Vega efficiency (6 H/J) if you pay less than $0.1/kWh. This means a lot of people can still mine on their PC if they wish to join the network.

## tarris034 | 2019-03-14T17:50:20+00:00
We know it is possible to differentiate ASIC machines by nonce distribution analysis, would it be possible to reject shares by network based on that and allow blocks only from known pools to be accepted ?

Maybe we could block them somewhere else than changing PoW

## ArticMine | 2019-03-14T17:53:05+00:00
After reading through this thread and in particular the more recent comments, I am leaning  way more towards the RandomX approach than the SHA-3 approach. The key point is the question of the  ASIC advantage over for the sake of argument CPU. 100x ASIC  advantage is a world of difference over 2x. ASIC advantage. 

@iamsmooth

2x advantage ASICs are not economically equivalent to 2x advantage GPUs.  Not even close. GPUs have a much larger production run with resulting lower costs, one can switch between coins at will, have much higher resale value and a host of other uses.  Furthermore a 2x ASIC advantage is not a disaster quite the opposite it may be close to optimal and even better than no ASICs at all. The reality is that one cannot ignore the possibility of of ASIC co-existence which to a large degree is what is currently happening in the Ethereum network. 

@hyc  @tevador 

I feel that focusing on reducing the ASIC advantage to ~2x or less, a situation comparable to or lower than the the situation in Ethereum, as opposed to ASIC elimination, is the right approach.

@fluffypony

I agree with you entirely that security of the network is paramount and needs to take preference over ideals. There is a very critical aspect of security in crypto currency and especially in Monero. Security is fundamentally dependent upon software freedom, openness and decentralization and anything that is proprietary  becomes first and foremost a security threat.  This is especially the case when it comes to mining and verification. So yes, Windows is a security threat so is Apple's walled garden. Patents are a security threat. DRM a major security threat. Free software becomes a matter not of ethics or ideals, 35 years of rhetoric from RMS not withstanding, but of security,. Strong copylefts  such GPLv3 become powerful security tools. In summary ideals become security tools. 

@dEBRUYNE-1

If the objective is community harmony then it makes way more sense to me for the community to agree upon a set of criteria that would trigger us considering the implementation something like SHA-3 than a fixed timeline. Again let us take a look at Ethereum. How many times have they forked away the difficulty bomb? 

So what are the trade-offs here. The possibility of  a freer ASIC market with a high ASIC advantage, SHA-3  vs a small ASIC advantage with a high likelihood of ASIC co existence, RandomX. To me the latter is over the long term the far safer and more secure option. There is already considerable evidence from Ethereum of the viability of a small ASIC advantage, and the likelihood of ASIC co existence.. On the other hand the evidence from Bitcoin is that a competitive ASIC market is not guaranteed to be stable. There are powerful economic incentives to extract even the slightest advantage in ASIC design, and lock ti down with patents ,such as ASIC boost,  and DRM powered kill switches. Furthermore we have the situation where the majority of the Bitcoin hashrate is behind the Great Firewall of China. This has very serious security and regulatory implications, especially considering the current situation of adversity between the United States and China. 

To me the sane course of action is that we continue the current course of lowering the ASIC advantage with each POW change. This will mean RandomX in either fall 2019 or Spring 2020 depending on the audit  results and timing. The overall goal would be to lower the ASIC advantage to 2x or below. We remain open POW changes that improve the overall security and lower the ASIC advantage. When we reach a low ASIC advantage we become open to ASICs particularly if they are openly sold. The goal here should be co existence as opposed to elimination or domination. What about SHA-3? We some reluctance I would suggest this be kept on the table as a nuclear with the possibility of MAD (mutual assured destruction) last resort, To me the value here is more in the threat than in its execution. In any case if this needs to be deployed it can be done on relatively short notice in a matter of a few months not several years. 

## pallas1 | 2019-03-14T17:53:54+00:00
@tarris034 ASIC producers can work around it. Besides, accepting blocks from known sources only is adding a central authority, and is against the basic principles of crypto coins, IMHO.

## whitefire990 | 2019-03-14T18:03:29+00:00
As one of the leading FPGA developers, my suggestion is to fork to an equality algorithm such as X16R/X16RT/X16S.  I have (in other forums), provided extremely detailed analysis of the required die size, and process size, for an X16 ASIC and provided extremely compelling evidence that the cost of such an ASIC provides a very poor return on investment.  Without going through the 10 paragraphs I have posted elsewhere, unlike traditional ASIC machines where you have 128-512 small cheap 28-90nm chips, an X16 ASIC requires a single huge die at fairly advanced (<28nm) process.  Huge die's are extremely expensive due to reject rate, and the resulting 'ROI' or payback time of such an ASIC ends up being similar to the 16nm publicly available FPGA cards.  FPGA implementations of X16 algorithms are just around the corner, with several groups already claiming prototype success, although the ROI of FPGA's on X16's is not that much better than GPU's (5-10 times the speed of a 1080 Ti for 5-10 times the price).  For this reason, X16's represent (at the moment) the most equal field where all three types of hardware (gpu,fpga,asic) remain viable long term, promoting decentralization.  My analysis is further supported by the fact that Ravencoin alone has such enormous daily mining rewards (and has had such for a long time) that if an ASIC was extremely profitable to manufacture, it would have already been done.  Forking Monero to an X16 variant would eliminate the need for frequent and dangerous forks.  I'm happy to elaborate on any of these points if necessary.  Many other coins such as Bitcash and Gincoin have forked recently to X16 variants as they have come to similar conclusions.

## SamsungGalaxyPlayer | 2019-03-14T18:03:35+00:00
@ArticMine I appreciate your comments.

> 2x advantage ASICs are not economically equivalent to 2x advantage GPUs. Not even close. GPUs have a much larger production run with resulting lower costs, one can switch between coins at will, have much higher resale value and a host of other uses. Furthermore a 2x ASIC advantage is not a disaster quite the opposite it may be close to optimal and even better than no ASICs at all. The reality is that one cannot ignore the possibility of of ASIC co-existence which to a large degree is what is currently happening in the Ethereum network.

THANK YOU for acknowledging that risk is complicated. There are a whole host of factors that determine what equipment is used. ASICs with a 1% advantage, on one extreme, will not necessarily eventually dominate the network just because they are more efficient. There are a host of other factors:

1. ASICs can't mine anything else that's temporarily more profitable. CPUs and GPUs often have the flexibility of switching for temporarily more profits, or for any other purpose

2. ASICs may not be accessible to people, so they may still use GPUs and CPUs

3. Price volatility reduces the ability for profit-driven ASIC manufacturers to go "all-in," since they don't know what the expected future price will be. Some speculate that Bitmain lost millions of dollars from overproducing as Bitcoin's price fell. CPUs and GPUs have much better capacity to deal with future price uncertainty. ASICs can take some steps to leverage their risk, but it comes at a greater cost than the cost to other miners.

While there certainly are issues with HUGE advantages, we shouldn't dismiss something just because there may be SLIGHT advantages. 2x is probably pushing it, but it may not mean the sky is falling. And I believe this is the theoretical worst-case scenario (absent critical flaws).

## whitefire990 | 2019-03-14T18:30:44+00:00
Just to comment on the SHA3 fork possibility.  Currently the fastest SHA3 ASIC is the Baikal G28 which does SHA3 at 28GH/s although this function has not been unlocked to the public.  The Blackminer F1 (FPGA) does 21.6GH/s, the Bittware CVP-13 FPGA does 23GH/s and the Xilinx BCU1525 FPGA does 17GH/s.  A high end SHA-3 ASIC would have hash rates significantly higher than a SHA2-256 Bitcoin ASIC, so it would be in the dozens of TH/s at 7nm.

## tevador | 2019-03-14T18:33:03+00:00
@whitefire990
> X16 ASIC requires a single huge die at fairly advanced (<28nm) process

Does it, though? X11 uses 11 hashes, so X16 would require approximately 50% more die area per core (assuming roughly equal area per hashing function). Such ASIC would still smoke GPUs even though it would run slighlty suboptimally because some circuits would have to be used more than one time per hash (maximum theretical slowdown is 16x if all block hashes are the same). Taking existing X11 ASICs as a reference and dividing by 16, an X16R ASIC would be around 300 times more efficient than GTX 1070. 

## whitefire990 | 2019-03-14T18:37:02+00:00
An X16 ASIC requires 256 cores, not 16, since each of the 16 steps can be any of 16 functions.  So the size of the die would be 256/11 = 23 times bigger than an X11 ASIC.  An X16 block can consist of 16 consecutive groestl functions, or 16 consecutive cubehash functions, or one each of the 16 different functions, and so on.  An FPGA gets around that by reconfiguring the entire FPGA each block, but an ASIC cannot be reconfigured.  If you did create such a reconfigurable ASIC, it would be so incredibly similar to an existing high end FPGA it would not be worth tremendous investment to clone an existing chip.  You cannot re-use any of the cores more than once because this breaks the pipeline.  The moment you break the pipeline the speed of the chip drops approximately 100 times, since most of the hash functions pipelines are 100 clock cycles deep.

## SChernykh | 2019-03-14T18:42:33+00:00
@whitefire990 It only means that fully pipelined design is not feasible for X16. They can still do 16 very fast cores, one per each function and small programmable block which calls needed cores one by one. Only 1/16th of the chip is used at every single moment, but it's a small chip and every core is orders of magnitude faster than GPU/FPGA.

## timolson | 2019-03-14T18:43:04+00:00
IMO, ASIC’s are inevitable and the most fair thing is to have an easy-to-implement, ASIC-friendly PoW which encourages competition.

@fluffypony 
> There's also the very real risk of high-end FPGAs and similar

I’ve looked at FPGA’s across the market for many PoW’s and they are simply not economically viable compared to GPU’s.  SHA-3 -might- be an exception but we can test it ahead of time.

> choosing an algorithm that is easy to ASIC, is general purpose, and is easy to validate - I suggest SHA3

💯 Keccak would be an excellent choice for an ASIC-friendly PoW.  The f and C parameters may be changed from the SHA-3 values if you want a PoW unique to Monero, or they may be left as SHA-3 values if you want interoperability.  A Keccak ASIC would have the f and C parameters effectively hard-wired, because they are basically datapath widths aka number of wires/registers in the sponge function. Keccak with different params would be a different chip.


@SChernykh 
> if the algorithm is designed for FPGA, 16nm ASICs and 16nm FPGAs will have the same performance.

Not true. An ASIC on the same process will, as a rule of thumb, be about 5x faster than its FPGA implementation, and much MUCH cheaper. I can’t imagine any case where an ASIC would not be faster than an FPGA.


@Gingeropolous 
> Imagine we somehow swallow this proposed inevitability that ASICs are the only way. We switch to SHA3. A handful of manufacturers are onboard. Everythings going grand for, I dunno, 2 years. And then.
>
>Boom.
>
>The hashrate quadruples.

For what reason? If the PoW is simple to implement and has good research behind it, and the ASIC market is relatively commoditized, then I see no reason to believe someone will suddenly crack e.g. SHA-3.  Big performance multiples come from complicated unproven PoWs that are difficult to implement in hardware. You lay out a scary scenario, but on what evidence?

@iamsmooth 
>Many competitive ASICs are now being built on 28nm process (maybe/probably not the short-shelf-life cryptonight ones, but they are for other coins) and some are trying smaller.

Our “short shelf life” CN design was for 28nm, which was the “value” option in late 2017 / early 2018.  We believe other manufacturers used 16nm, and any chip we’d do now is probably 16/12nm.  I can’t imagine any new mining project using 28nm in 2019 and beyond.  It’s simply a legacy node at this point, and the NRE for 16nm vs 28nm is not very different.  There are some power details that might still make 28nm interesting for certain cases, but mostly no.

@whitefire990
> Without going through the 10 paragraphs I have posted elsewhere, unlike traditional ASIC machines where you have 128-512 small cheap 28-90nm chips, an X16 ASIC requires a single huge die at fairly advanced (<28nm) process. Huge die's are extremely expensive due to reject rate, and the resulting 'ROI' or payback time of such an ASIC ends up being similar to the 16nm publicly available FPGA cards.

28nm is not “advanced.” It is quite cheap actually. Also, the process is extremely stable and even large chips have high yields.  What you said was maybe true several years ago, but in 2019, no. Also, a 28nm ASIC will crush a 16nm FPGA, not even close.

IMO, X16 is a _horrible_ choice for an ASIC-friendly PoW for a few reasons: 1. It is extremely long and complicated to implement, roughly 16x more code than a simple hash.  This means a much longer development time and higher barrier to entry for competition.  2. Chained hashes are only as strong as the weakest link.  If any one of the sixteen hashes is cracked, then then entire PoW goes down.  Adding hashes WEAKENS security.

## tarris034 | 2019-03-14T18:45:48+00:00
> IMO, ASIC’s are inevitable and the most fair thing is to have an easy-to-implement, ASIC-friendly PoW which encourages competition.

Why would we make it easier for them ? let them suffer performance hits so CPU/GPU miners can still contribute to the network.



## MoneroCrusher | 2019-03-14T18:47:05+00:00
@timolson ASICs are inevitable from a technical perspective yes, but ASICs are not inevitable as a whole by combining multiple layers of anti-ASIC warfare (I explain this [here](https://github.com/monero-project/meta/issues/316#issuecomment-472677985))

## tevador | 2019-03-14T18:47:18+00:00
@whitefire990
> You cannot re-use any of the cores more than once because this breaks the pipeline. The moment you break the pipeline the speed of the chip drops approximately 100 times, since most of the hash functions pipelines are 100 clock cycles deep.

I understand pipelining, but why you could not interleave new and old hashes? You start 100 calculations in the pipeline and when the first one leaves the pipeline, you feed it back to the start of the pipeline. This would only cause a slowdown by a factor of 16. I'm pretty sure this works for pipelined CPU instructions with a 3-8 cycle pipeline (for example `aesenc`), so I don't understand why it wouldn't work with a long pipeline.

## SChernykh | 2019-03-14T18:47:25+00:00
> Not true. An ASIC on the same process will, as a rule of thumb, be about 5x faster than its FPGA implementation, and much MUCH cheaper. I can’t imagine any case where an ASIC would not be faster than an FPGA.

What about "random circuit" algorithm that uses the same building blocks as FPGA (LUTs, DSPs, Block RAMs) and changes every block?

## fluffypony | 2019-03-14T18:57:55+00:00
Yeah, guys, X16 is not even remotely an option. Apart from the obvious brokenness (it’s only as strong as it’s weakest link) you also have the risk of entire parts of the hash chain being circumvented through a variety of attacks. Let’s not waste brain power considering it.

## justinjja | 2019-03-14T18:59:18+00:00
Do you guys have a link I can read on that?
I haven't heard the "only as strong as it’s weakest link" before.

## timolson | 2019-03-14T18:59:33+00:00
> > Not true. An ASIC on the same process will, as a rule of thumb, be about 5x faster than its FPGA implementation, and much MUCH cheaper. I can’t imagine any case where an ASIC would not be faster than an FPGA.
> 
> What about "random circuit" algorithm that uses the same building blocks as FPGA (LUTs, DSPs) and changes every block?

Like ProgPoW or RandomX but for FPGA’s?  It seems even harder than for CPU’s.  FGPA’s have lots of variety and sizes and capabilities... which FPGA would you design for? They have proprietary synthesizers and the core LUT’s and architecture are different between Xilinx and Altera.  Are you going to design a PoW that uses a giant network of 4-bit logic tables and multipliers? You exclude FPGA’s based on 3-bit LUT’s. Are you going to make the logic network huge? Xilinx might have trouble since they partition their FPGA’s into tiles, whereas Alteras are better when synthesizing a single large netlist...

But in the end, a programmable ASIC could be made which conforms to the “random code” spec... a regular CISC or VLIW ASIC whose ISA aligns with the PoW should still easily outperform an FPGA simply on clock rate.  The flexible interconnect on an FPGA comes at the cost of slow clocks...

RandomFPGA could be tried but I’m skeptical... We don’t know yet if ProgPoW or RandomX work, and this one would be even harder. 

## MoneroCrusher | 2019-03-14T19:02:46+00:00
> Yeah, guys, X16 is not even remotely an option. Apart from the obvious brokenness (it’s only as strong as it’s weakest link) you also have the risk of entire parts of the hash chain being circumvented through a variety of attacks. Let’s not waste brain power considering it.

Let's also note waste too much time on focusing on ASIC friendliness. Let's start wasting time on it when you can buy ASICs at the cornerstore like you can buy candy at your local kiosk.

I believe CN-R + tweaks will last us a good while and in that time we can find a solution that perfectly satisfies both GPU and CPU miners in the meantime. RandomX might be a part of a solution for that, but since when do we have to rush things?

## fluffypony | 2019-03-14T19:03:26+00:00
@justinjja

https://crypto.stackexchange.com/questions/44444/can-chaining-hash-functions-reduce-security



## fluffypony | 2019-03-14T19:06:29+00:00
@MoneroCrusher You can’t buy GPUs like you can buy candy, so that’s false equivalence, unhelpful, and unnecessarily combatative. I’ll gladly leave the thread if you’re going to bring the discussion down to a puerile level.

## MoneroCrusher | 2019-03-14T19:11:02+00:00
It is a equivalence, I can buy candy at a kiosk like I can buy CPUs & GPUs at a computer hardware store.

You can buy CPUs and GPUs in basically every computer store in every country of the world. Can't say the same about SHA-2 (even with them being now on the market for almost 7 years) or SHA-3 ASICs. I don't think pre-commiting will bring us magic decentralization of ASIC hardware production.

Even at only 0.6 XMR and a price of $50 per XMR, that's still a business of a daily $22k. And it only gets worse with the price going higher. Do you consider Bitcoin mining to be decentralized and more importantly, egalitarian?

## whitefire990 | 2019-03-14T19:11:05+00:00
While I appreciate the many opinions, it is difficult to argue against hard facts.  Ravencoin/X16R is by far the largest mining market that has never been hit by an ASIC.   If, as people say, it is easy to ASIC, and it is broken, etc., then why have none of those things ever happened?  In my opinion, evidence is the best argument and the evidence right now supports that X16R is the most ASIC resistant algorithm.  If anyone is aware of a similarly large mining market that has never been hit by an ASIC, please post.  

## SChernykh | 2019-03-14T19:12:32+00:00
> why have none of those things ever happened?

Not happened... yet. X16R is relatively new. Designing 16 algorithms takes time if even FPGA groups haven't done it yet.

## fluffypony | 2019-03-14T19:13:07+00:00
@whitefire990 it has a marketcap smaller than Verge, so let’s not pretend that any manufacturer is even remotely motivated to produce ASICs for it.

## justinjja | 2019-03-14T19:13:38+00:00
It has higher mining reward per day than Monero last time I did the math.


## fluffypony | 2019-03-14T19:15:15+00:00
@justinjja that’s not nearly enough motivation for an ASIC manufacturer. They like to know that the millions of USD they’re pouring in are on a coin that will still be around in 6 months. Randomcoin number 54 still has a long way to go for that to be true.

## timolson | 2019-03-14T19:15:22+00:00
Dual-PoW comments

I’ve followed the Grin launch closely, where they have a dual-PoW system.  They split the mining rewards between two PoW variants, one ASIC-resistant variant, and one ASIC-friendly. Then they slowly increase the proportion of rewards allocated to the ASIC-friendly PoW.  The diffs of each PoW are adjusted separately to maintain the target mining reward payouts.

The idea is to ease the transition to ASIC miners but IMHO it fails for these reasons:

1. Starting with small rewards excludes small manufacturers. If the reward starts small, only the big players are going to be able to “eat” the NRE and start development of their chip in time for the larger rewards to hit.  Small companies which don’t have the bankroll for NRE must wait until there’s a larger market so they can recover their fixed expenses faster

2. Reward adjustment is ineffective. The market has simply adjusted the hashrate for each PoW to the point where the revenue-per-GPU is roughly the same for both variants.  You can control the diff, but you can’t control the hashrate.

## SamsungGalaxyPlayer | 2019-03-14T19:16:15+00:00
@MoneroCrusher @fluffypony let's take a step back. I think you both agree that "CPUs and GPUs are more accessible to most people than ASICs"

## justinjja | 2019-03-14T19:18:56+00:00
I'm not sure about that one, they know Monero (current mining algo) won't be here in 6 months, but that hasn't stopped them.

## tarris034 | 2019-03-14T19:19:59+00:00
> @MoneroCrusher @fluffypony let's take a step back. I think you both agree that "CPUs and GPUs are more accessible to most people than ASICs"

Accessibility shouldn't be measured by the fact anyone can buy it, rather that anyone already got one. 

## MoneroCrusher | 2019-03-14T19:20:15+00:00
@justinjja because the efficiency gain possible was too high. Maybe it will be different with CN-R. I'd welcome a wait-and-see approach than hastily rushing an unaudited & brand-new algo that we don't even know works. What if CN-R actually works this time? Why should we replace something that might work?
If they targetted a 300% ROI, then ASICs already won't come back with CN-R and 6 months, if @SChernykh claims hold water.

## pigfrown | 2019-03-14T19:20:37+00:00
Ravencoin may have a smaller marketcap than Verge but it has more than double the daily volume, which arguably may be more important to an ASIC manufacturer looking to ROI. 

Still 7 times less daily volume than Monero though, so the point still remains.

## tarris034 | 2019-03-14T19:21:41+00:00
> Ravencoin may have a smaller marketcap than Verge but it has more than double the daily volume, which arguably may be more important to an ASIC manufacturer looking to ROI.
> 
> Still 7 times less daily volume than Monero though, so the point still remains.

But is it real daily volume or only artificially pumped like that exchange did while ago to a Monero only to show in top exchange list ?

## fluffypony | 2019-03-14T19:21:42+00:00
New rule: posts about Ravencoin will be removed, please go shill your bags elsewhere.

## justinjja | 2019-03-14T19:25:43+00:00
Never owned Ravencoin, So certainly not shilling for it.
@timolson "Starting with small rewards excludes small manufacturers" define small?
2 small manufactures already announced asics for that coin.


## timolson | 2019-03-14T19:26:23+00:00
Fair ASIC Distribution

A big concern is that ASIC manufacturers will keep profitable hardware for themselves and only sell when the net-present-value of mining is less than the market demand for mining equipment... which somehow happens!

One solution is some kind of community-owned ASIC co-op.  Maybe it’s a nonprofit which commits to only selling miners publicly, at the same price for everyone, with no bulk discounts.

ASIC’s would be a lot less scary if the dev team and community controlled both the PoW AND the manufacturer...

## justinjja | 2019-03-14T19:27:21+00:00
Ya like siacoin, that worked well...


## justinjja | 2019-03-14T19:27:59+00:00
(that is sarcasm, you don't need to delete my post for shilling siacoin)

## dEBRUYNE-1 | 2019-03-14T19:32:10+00:00
The problem with Siacoin was that they forked off any other ASIC manufacturer. I think @timolson is trying to say that we can alleviate some of the concerns by building and selling ASICs ourselves. 

## MoneroCrusher | 2019-03-14T19:34:29+00:00
@dEBRUYNE-1 could you please add [10. Game Theoretical approach to ASIC resistance](https://github.com/monero-project/meta/issues/316#issuecomment-472677985) to your list in the OP?

## justinjja | 2019-03-14T19:34:31+00:00
I would assume making asics is hard, and we would probably have the same problem, someone like bitmain would release a better asic, before we even finished ours. 

## dEBRUYNE-1 | 2019-03-14T19:35:40+00:00
@MoneroCrusher - I'll try to find some time to edit the OP tomorrow (I have to add some other things as well). However, I don't think that option will ever realistically achieve traction in the community. 

## SamsungGalaxyPlayer | 2019-03-14T19:35:41+00:00
@justinjja we have a more level playing field if we are developing (or assisting the development of) ASICs for a PoW we aren't currently using.

## pigfrown | 2019-03-14T19:36:33+00:00
A community co-op that designed and built SHA3 ASICS might go a long way to removing some of the apprehension around the idea of ASICs.

Sia coin failed to compete because they were racing against an already established company and even admitted themselves they had very little hardware knowledge when they started with Obelisk.

The situation with SHA3 could be different.. the community can set the fork date well in advance, giving the manufacturers (and the community co-op) plenty of time to build their miners.

## timolson | 2019-03-14T19:37:02+00:00
> Never owned Ravencoin, So certainly not shilling for it.
> @timolson "Starting with small rewards excludes small manufacturers" define small?
> 2 small manufactures already announced asics for that coin.

“Small” as in Obelisk? I might guess their 2018 revenue to be in the $20-50m range.  It’s not Bitmain but it’s not small.  I chatted with Vorick about their Grin project and I won’t give details, but yes they burned a lot of their own money on R&D ahead of the coin launch, before announcing their project.

Not sure who you mean by the other “small” player.  Are you calling InnoSilicon small?  I know of a third Grin ASIC project, but they are not small either.

altASIC is small, as in startup-small, and we didn’t even try to raise money for a Grin ASIC.  We needed money before the coin even launched, with an uncertain market cap, and telling would-be ASIC investors that a coin launches with only 10% rewards going to ASIC’s, well you can imagine how that pitch would be received.

## MoneroCrusher | 2019-03-14T19:38:56+00:00
@dEBRUYNE-1 In my opinion: When not accepting a game theoretical approach, which is truly the only way to reach *true* ASIC resistance, you are automatically accepting the technical inevitability of ASICs and RandomX or any other solution will end us in the same spot we are in now, sooner or later. I think many people don't get that yet.

ASIC resistance is only possible by approaching it in a multi-dimensional way: 1. making it technically hard and expensive (like presumably RandomX, Cryptonight-R, Ethash, ProgPoW) and 2. combining that with a game theoretical approach of absolute economic risk, i.e. the "nuke" scenario in my post above, **ultimately requiring 0 hardforks to maintain**.

## timolson | 2019-03-14T19:42:55+00:00
There are a couple ways to ensure the community-owned manufacturer has a monopoly, if that is an interesting approach to you. One is to give them a head-start by keeping the PoW secret until the chip is ready. A longer term strategy is to “tax” all mining rewards to fund the community manufacturer. If the community company gets 10% of mining rewards just for being “blessed”, and if that co-op sells miners at or near cost, and if the PoW is not complicated enough to give large differences between manufacturers, then there’s no way for other ASIC makers to compete against at-cost or slightly subsidized ASIC’s.  The ASIC market is already thin-margin so any subsidy or at-cost sales would be hard to compete with.

## SamsungGalaxyPlayer | 2019-03-14T19:48:55+00:00
@timolson thanks for the comments, but I think these are unrealistic. I think we should focus the conversation a little bit broader.

> One is to give them a head-start by keeping the PoW secret until the chip is ready.

I think this is unlikely, since we want to use a rigorously-tested algorithm like SHA3. I think it's more realistic to say a community-supported design is ready to go on day 1 with a known algorithm. The intent isn't to make an organization that can outcompete forever.

> A longer term strategy is to “tax” all mining rewards to fund the community manufacturer.

I can't imagine this happening. This is extremely controversial.

## pigfrown | 2019-03-14T19:49:16+00:00
@timolson I think a community owned coop is a good idea, but not sure if trying to maintain a monopoly is a good idea for decentralisation (or public image).

As I understand it SHA3 is the goal because it is simple to implement which should encourage a more equal playing field for ASIC manufacturers. If this is the case, the community coop should still be able to stay relevant even when competing against others. 


## timolson | 2019-03-14T19:53:29+00:00
> Ya like siacoin, that worked well...

I’m not a fan of how Sia handled that situation, but it is different from what I propose.  Obelisk is a VC-funded for-profit corporation with external pressure to compete and be profitable. If Vorick hadn’t forked to make his miners profitable, he could potentially have been _personally_ sued by shareholders, because US corporate law is crazy like that.

If the Monero community owns the coop, or if it’s a nonprofit or B-corporation whose revenue comes from mining tax, the coop may act in the best interest of Monero, not in the best interest of for-profit VC shareholders.

## SamsungGalaxyPlayer | 2019-03-14T19:55:05+00:00
> If the Monero community owns the coop, or if it’s a nonprofit or B-corporation whose revenue comes from mining tax, the coop may act in the best interest of Monero, not in the best interest of for-profit VC shareholders.

I understand how it can be registered, I just don't see this happening. I personally do not support trying to maintain a coop/nonprofit that has a monopoly over mining.

## MoneroCrusher | 2019-03-14T19:55:43+00:00
Monero ASIC LLC. just the sound of it makes my stomach not feel good 😄 
Also that company would be susceptible to governmental pressure and potentially legally non-disclosable backdoors (gag order), i.e. a very central attack vector on the currency.

## SChernykh | 2019-03-14T19:58:03+00:00
"Mining tax" is a big no-no for Monero community. Pre-mine, mining tax = scam in people's eyes.

## timolson | 2019-03-14T20:00:48+00:00
@SamsungGalaxyPlayer 
> I think this is unlikely, since we want to use a rigorously-tested algorithm like SHA3.

You could announce Keccak, for example, but withhold the configuration of f and C.  Other manufacturers could have their parameterized Keccak implementations ready, but they couldn’t go to tapeout until f and C were revealed.

Witholding f and C values for Monero would in no way compromise the integrity of Keccak.

## MoneroCrusher | 2019-03-14T20:06:23+00:00
@timolson that's not the spirit of monero
For me Monero represents chaos, decentralization & innovation (and of course privacy). If there's any corporational tangents I'm out. Could as well suggest founding _The Monero Company_ 😄 

## timolson | 2019-03-14T20:12:09+00:00
Honestly I don’t love the community owned manufacturer idea that much either, but we’re brainstorming, right?

If the PoW is simple to implement and there’s enough lead time, I’d except the ASIC manufacturing market to be competitive and healthy from the beginning.

## MoneroCrusher | 2019-03-14T20:21:41+00:00
@timolson what's your estimation of ASIC efficiency of RandomX, ProgPoW, CryptonightR?
(That being the efficiencies of economical solutions, not some exotical experimental methods like quantum computing or other approaches but with approaches we have so far seen that are economically feasible, i.e. no/low IP ASICs)

## tarris034 | 2019-03-14T20:49:08+00:00
> @timolson that's not the spirit of monero
> For me Monero represents chaos, decentralization & innovation (and of course privacy). If there's any corporational tangents I'm out. Could as well suggest founding _The Monero Company_

Also suggesting that ASIC could be accessible to everyone is very selfish, I have 50 bucks in my bank account and can't afford specialized hardware, living from pay check to pay check for years but for 3 years now I am mining monero when in idle with my couple computers I got in home that are used by wife and kids.

ASIC Accessibility for me = 0%.
Even if I had the money, those ASIC machines are getting inefficient very quickly due to new better ones coming in, making the whole network full of sharks that eat small fishes like me.

## ghost | 2019-03-14T21:03:04+00:00
Expecting to prevent centralization of mining  is probably futile. We can't fight the Pareto distribution and win. The entities with the most resources will always be able to throw more CPUs, GPU,s FPGAs, or ASICs at it. 

However, preventing centralization of manufacturers _is_ possible, and that is probably best done through making the PoW ASIC friendly enough to encourage as many commercially available ASICs as possible. This will also lower the price and make them more accessible. 

Right now, we have  a PoW that is not defeating ASICs, but is still difficult enough to implement that only one or two sources can actually produce them. That's the worst scenario I can think of. Trying to be ASIC unfriendly has resulted in a very small number of ASIC manufacturers who are able to keep up. That creates centralization. An alternative like SHA3 would hopefully encourage a large number of ASIC manufacturers to enter the game, making them cheaper and widely available for hobbyists. That's a better deal than we have now IMO. 


## MoneroCrusher | 2019-03-14T21:04:50+00:00
> Right now, we have a PoW that is not defeating ASICs, but is still difficult enough to implement that only one or two sources can actually produce them.

You're talking about CNv2. It remains yet to be seen if ASIC manufacturers will be able to economically produce CN-R ASICs within the next 6 months.

## ghost | 2019-03-14T21:18:22+00:00
@MoneroCrusher 

True, we will have to see. However, we can't afford to have a similar situation as CNv2. 

To prevent centralization we either need to make  producing ASICs completely impossible, or ridiculously easy. Merely making it very hard is the worst possible outcome. 

## MoneroCrusher | 2019-03-14T21:21:37+00:00
@jsfierro I agree with your conclusion. Either make ASICs very easy (or alternatively go the @SChernykh route of creating a FPGA-only algo) or make them impossible through economic means and technical means combined. Personally I don't support the ASIC route (yet) because I'm fairly positive we will not reach a fair SHA-3 ASIC market (fair meaning you can buy them in literally every computer store from many manufacturers, we still can't see that with SHA-2 ASICs and they've hit the market 7 years ago).

## justinjja | 2019-03-14T21:40:14+00:00
Dual pow makes a lot of sense to me if the security of it can be worked out.
It sounds like Zcash still plans to do it, just not yet?
https://github.com/zcash/zcash/issues/3672#issuecomment-443919681

## SamsungGalaxyPlayer | 2019-03-14T21:57:43+00:00
@justinjja as discussed earlier in this issue, Zcash decided not to pursue the idea due to significant security concerns. Unless these have been dealt with, a dual solution is completely off the table for me.

## JustFranz | 2019-03-14T22:04:44+00:00
The free market has failed you!?! Communism!
I feel like this conversation is entering lala-land. 

Our next moves hinge on the results of RandomX audits, unless something out of our control happens first. We need to concentrate on what is tangible.

## needmoney90 | 2019-03-15T03:49:25+00:00
Okay, so I know it's been 6 blissful hours without any messages, but I've spent some time digesting the various viewpoints in the conversation, and I want to express where I'm at. 

1. Any sort of non-commodity hardware being required (in a 51% sense) to secure the network carries with it the risk of export controls and government licensure for devices that 'print money'. This is an existential threat.

2. If we decide to switch to an ASIC-friendly algorithm like SHA-3, we're stuck with it. We will have abandoned our chance at eventually adopting a truly ASIC-resistant algorithm, should one be developed at some point in the future. There is no turning back from this decision. 

3. I am aware of no developer with any credibility in this community who believes that a 3-month forking schedule is sane at our current market cap and ecosystem size. Even a 6-month fork schedule would be pushing our limits, and greatly increases ecosystem friction (app store approvals, exchange adoption, pool software updates, localization, code freezes/release builds, and way more that I'm not listing). The general consensus is leaning towards a 1-year fork schedule.

4. Adopting a GPU-friendly algorithm that isn't ASICable is, more and more, appearing to be a pipe dream. If we want to maintain GPU profitability, we will need to maintain a 3-month fork schedule, or ASICs will be de facto present on the network. This is unsustainable, as noted in point 3. It's unfortunate, but GPU miners will unfortunately need to either shift operations to another coin, or compete with the only commodity hardware that we believe has a chance at maintaining ASIC resistance - CPUs. There does not appear to be, in my opinion (after speaking with many many people in the community over the past week), any sort of critical developer mass willing to maintain a GPU-resistant Monero. It's possible that a critical amount of developer mindshare could be rallied around the idea of GPU resistance, but for the moment, the only proponents appear to be those who have significant vested interests in maintaining GPU profitability as a priority over network stability. I believe this to be backwards - the miners are here to serve the interests of the network, the network is not here to serve the interests of the miners. 

5. Any sort of precommitment that isn't included in the consensus layer is unable to take into account the future makeup of the community, and the progress that has occurred on ASIC-resistant PoW algorithms. While it seems like a good idea, I know that the me now cannot speak for the me in two years, let alone for the rest of the community. One prime example is the Hong Kong agreement. The project's leads and community can express strong opinions on how they feel at this very moment, but any sort of 'official' precommitment is misguided, in my opinion.

6. If RandomX fails, we must still take into consideration point 2. Even maintaining the facade of ASIC-resistance is enough to continue research and development. Even if we concede that ASICs must be present on the network for large stretches of time on a 1-year fork schedule, we could maintain a commitment to fork ASICs off yearly, in the hope that we eventually discover an algorithm that lowers the ASIC gap to near zero on commodity hardware. This option should not be discounted as a possibility, even if it carries some risk of existential threat. The financial incentive of knowing that your ASICs will be viable on the network for 10 out of 12 months every year could encourage multiple entities to be competitive interyear to produce network securing hardware, and gives them a potential recurring revenue stream. 

I'm currently leaning towards RandomX being our best shot at reducing the gap between ASICs and general purpose hardware, and I'm not too picky about which general purpose hardware we use, so long as it can be purchased in a store. Beyond that, I'm still on the fence. If anyone would like to continue my train of thought on any of these six points, I'm very interested to hear where you take them.

## Minthos | 2019-03-15T04:34:09+00:00
Option 6 is the only one that makes sense to me. Switch to RandomX as soon as it's been sufficiently validated and if necessary tweak it later to further improve its ASIC resistance.

ASIC resistance is a major feature that we should fight to keep for as long as possible. Maybe the day comes when we have to cave but we should push that day as far into the future as we reasonably can.

## tarris034 | 2019-03-15T07:12:28+00:00
CPU/GPU PoW is much safer for a small / medium mining operations, with big 10,000 CPU/GPU Farm you're only making 5-30 MH/s (depending on hardware) so a bigger market cap is not a threat to smaller miners, and you can always sell the hardware to gamers.

ASIC PoW is only good for big companies and even them go bankrupt as seen many times when the price drop.

In the end with ASIC you can mine profitable only in chosen countries with the lowest energy price and it is a race before the new more efficient ASIC come around and brick all your investment.

It's against decentralization which is fundamental for the whole project.

As other have said, Monero was all about closing the gap between CPU/GPU and specialized hardware, if you're going ASIC-friendly, please fork the coin and change the name.

## fluffypony | 2019-03-15T09:38:03+00:00
@tarris034 your description of a miner with $50 in the bank, living paycheck to paycheck, is unfortunately not representative of the bulk of miners that are even currently mining Monero. You’ll be edged out as Monero’s marketcap increases and more and more professional mining farms come onboard, whether they’re operating GPUs or CPUs or FPGAs or ASICs. You’re choosing the wrong hill to die on.

## tarris034 | 2019-03-15T10:18:31+00:00
@fluffypony yes I am a bad example, but the recent answer was for your yesterday question about growing cap market. with ASIC resistant PoW even with big resources a single entity can't grow that big to influence the whole network and the small and medium farms still have a chance.

Add to this that the new more efficient ASIC hardware is coming too fast, CPU and GPU have much longer life span.

## dEBRUYNE-1 | 2019-03-15T10:44:46+00:00
>with ASIC resistant PoW even with big resources a single entity can't grow that big to influence the whole network 

Conditional on ASIC resistance actually holding. Even that doesn't exclude the possibility of a single entity reaching a majority hashrate. 

## fluffypony | 2019-03-15T10:47:37+00:00
> with ASIC resistant PoW even with big resources a single entity can't grow that big to influence the whole network

In addition to what @dEBRUYNE-1 said, this is simply not true. We’ve already had a single entity (a mining pool) nearly eclipse 50% of the hashrate. ASIC resistance does NOT prevent 51% attacks, and may actually do the opposite (the NiceHash effect).

## tarris034 | 2019-03-15T10:48:55+00:00
mining pool is not a single entity, as you stated yesterday confronting other opinion on other coin @fluffypony 

## fluffypony | 2019-03-15T10:51:17+00:00
@tarris034 again, ASIC resistance has no effect on 51% attacks except maybe to increase the risk.

## tarris034 | 2019-03-15T10:52:13+00:00
51% attack is another subject that I wasn't referring to.

## fluffypony | 2019-03-15T10:53:08+00:00
What other type of influence is there? A single large entity can’t change the rules even if they control 90% of the hashrate.

## tarris034 | 2019-03-15T10:54:26+00:00
Difficulty for other mining operators, CPU/GPU farm with 90% of hashrate or even half of the network is rather far from reality.

And there's the decentralization aspect.

## fluffypony | 2019-03-15T10:57:37+00:00
I don’t understand what you’re arguing - that they can manipulate difficulty?

## tarris034 | 2019-03-15T11:03:53+00:00
ASIC farms are high risk, low life span investments that only few will do it on a big scale.

Small and medium farms will have no chance in competing with them and the difficulty increase from those big investors will kill all profits for small/medium farms especially in other than third world countries with normal energy costs.

Bitcoin scenario basically, the mining hardware sometimes gets obsolete before delivery.

## zexanana | 2019-03-15T11:52:10+00:00
This seems simple to me. Try RandomX, and if it doesn't work, figure a way to make the ASIC friendly transition (even if that means 1 or 2 algo tweaks after RandomX). The (apparently innocuous) plan of setting a date for the transition is much more controversial because it implies RandomX will fail. This will probably split the community. There is no need... Innovation takes risk.

And I want to note: I believe RandomX will probably not work at the first try. Engineering requires iteration. Failure, in my opinion, means maybe after 2nd or 3rd iteration we won't be able to keep ASIC resistance. But maybe I'm asking for too much.

## tarris034 | 2019-03-15T12:09:08+00:00
I think the fact alone that we are talking about surrendering to ASIC will encourage ASIC manufacturers to work against anti-ASIC PoW's even with a loss. 

## jtgrassie | 2019-03-15T12:35:52+00:00
@tarris034 
> mining pool is not a single entity

It actually behaves as one. The pool operator is the single entity. 

## tarris034 | 2019-03-15T12:43:20+00:00
> @tarris034
> 
> > mining pool is not a single entity
> 
> It actually behaves as one. The pool operator is the single entity.

Anyway, 51% attacks can happen on both ASIC-friendly and anti-ASIC network.

As @zexanana said, you can't win war without losing couple battles and going to war with gun in one hand and white flag in the other is a sure way to fail.

## antanst | 2019-03-15T13:34:27+00:00
I urge everybody that hasn't read @stoffu 's excellent proposal on AEON switching to SHA3 to do so: https://www.reddit.com/r/Aeon/comments/aw2xhn/proposal_to_switch_to_sha3_proof_of_work/

There are lots of arguments that have been recycled in this thread which completely ignore basic facts about how (and why) the markets around mining ecosystems are created and evolve.

## WhyIsThisSoSlow | 2019-03-15T14:30:03+00:00
Hey guys,

I made this account just to clarify something here.

I see that the oldies of Monero are kinda set for moving to an ASIC only network. I will not get into conspiracy theories of why this recently started happening and why they consider that no other solution is good anymore. I see that really good ideas have been proposed here to keep fighting centralization but they are just being turned down irrationally in my opinion. Something's fishy in Denmark!

My question is...

When you guys will decide to move to ASIC, can this please be announced properly on all possible places?
I ask this because like me, many others will leave and dump the coins at that time. And this should not surprise anyone.
 
Monero with ASIC acceptance is nothing different than another ordinary shitcoin.

Wish you all the best in the following split!

## floridahaunted | 2019-03-15T15:09:10+00:00
@WhyIsThisSoSlow , you do read my thoughts, your citation:
"I see that the oldies of Monero are kinda set for moving to an ASIC only network. I will not get into conspiracy theories of why this recently started happening and why they consider that no other solution is good anymore. I see that really good ideas have been proposed here to keep fighting centralization but they are just being turned down irrationally in my opinion. Something's fishy in Denmark!
"
is exactly what I think. IRRATIONAL mind virus does attack the community :(

From the science-based point of view, we have to focus on RandomX (or something similar one) adoption as next mining algo (if we get RandomX, just reduce memory scratch from 4Gb to 256Mb to support computational-weak, Raspberry Pi-like devices).

Then we add true randomness (I agree with @fluffypony, Ethereum-like oracles are bad idea in general). So, the best source of true randomness is a long one-way hash (512-4096 bit) of all the transactions concatenated from last 100-1000 mined and confirmed blocks on the blockchain.

Then, it appears almost like a theorem, ASIC/FPGA manufacturers MUST implement Intel-like CPU to compete against current Intel-like CPUs that are WIDELY available in the all local stores of all countries.

I believe, special mining-oriented ASIC/FPGA for particular complicated mining algos will NEVER be available in the all local stores of all countries. Thus, strong hardware monopoly will be established.

In any case, let's ASIC/FPGA manufacturers to compete directly against Intel/AMD CPUs. Sure, CPUs win!



## SChernykh | 2019-03-15T15:10:27+00:00
@WhyIsThisSoSlow @floridahaunted Interestingly, me @tevador  and @hyc (the ones who work on PoW) all agree that asic resistance is possible, we don't see the need to switch to SHA3.

## antanst | 2019-03-15T15:17:57+00:00
> I see that really good ideas have been proposed here to keep fighting centralization but they are just being turned down irrationally in my opinion. Something's fishy in Denmark!

That's a common misconception. Last-minute changes and frequent hard forks make Monero pretty centralized actually; much more than Bitcoin. Remember that for every protocol and PoW change, _someone_ (as in an ultimate authority, be it a person or a group of persons) has to make the ultimate decision on what goes to the source code. The Monero devs are well aware of this fact of course; to their credit they've always taken into account the community's rough consensus on many matters that may have proven to be controversial.

The centralization factor of sudden PoW decisions is much more important than pursuing the "egalitarian mining" pipe dream with endless hard forks, especially since this approach has proven to achieve the complete opposite as a result in both aspects of centralization (mining reward distribution & protocol changes). How many people understood the last-minute PoW changes of the last hard fork in detail? Are we sure there wasn't any hidden motive behind those changes? Hard forks should give rise to those kind of questions.

## WhyIsThisSoSlow | 2019-03-15T15:25:16+00:00
@SChernykh 

I appreciate you and all others that understand.

For me and many others that have money invested in this, an ASIC switch will mean the end of the project and what it stands for.

There is a big indubitable fact that gets ignored here. ASIC is not as available to every one as a GPU or CPU and thus it can never be considered a decentralized solution. NO ASIC coin is decentralized and it will never be unless you can get a ASIC with the same ease as a GPU and with no consequences or fear of the government.

Centralization is not just about fear of 51% attack. Centralization is monopoly of the coin and the power to do with it as you please in all aspects.

Monero as a concept will be destroyed as the PRO ASIC mentality continues and will be yet another coin added to the sitcoin list of projects that failed due to bad influence and ignorance of the core aspects. 



## tarris034 | 2019-03-15T15:26:20+00:00
@floridahaunted 
> When you guys will decide to move to ASIC, can this please be announced properly on all possible places?
> I ask this because like me, many others will leave and dump the coins at that time. And this should not surprise anyone.
> 
> Monero with ASIC acceptance is nothing different than another ordinary shitcoin.
> 
> Wish you all the best in the following split!

You got that right. The minute they announce ASIC PoW, I'm trading all my coins to BTC.

## floridahaunted | 2019-03-15T15:27:10+00:00
@antanst Fundamental physics makes it quite evident (see my comments above), that modified RandomX_256Mb algo depends on long_hash(last_100_block_transactions) will be the last hard fork. If ASIC/FPGA manufacturers can make a chip that is more effective than Intel/AMD CPU for such extremely virtualized and randomized mining tasks, let them, and no more hard forks! I believe, either Intel/AMD win or ASIC/FPGA will be just 10-20% more effective. In any case, it will be fine.

## SChernykh | 2019-03-15T15:29:35+00:00
@floridahaunted RandomX already has 256 MB mode for verification, 4 GB is only needed for mining.

## zexanana | 2019-03-15T15:32:08+00:00
@antanst , from @stoffu's proposal for aeon:

> I think the reasoning is that CN-R is expected to be somewhat better at resisting ASICs and not much more computationally expensive than the previous CN variants (unlike RandomX), so we can wait and see how successful this will be before going full ASIC friendly. 

He acknowledges there is a chance RandomX might work. He goes on to mention the downsides he sees with keeping ASIC resisting. In my opinion, the one that holds more weight:

> If we switch to CN-R now, and if ASICs do appear at some point (I believe they will), are we certain that we will switch to SHA-3 at that point? Won't there be someone claiming "I have an idea for a better ASIC resistant PoW, so let's try it and see"?

This is definitely a possibility. The question is whether it's a risk we have to take to keep the network decentralized and permisionless or not. In my opinion, abso-fucken-lutely!

I endorse Aeon to change to SHA-3. As I understand it (I might be wrong) Aeon is supposed to be a lighter version of Monero but also experimental. If they change to SHA-3 it's a way to make the ASIC market develop earlier. If Monero then decides to switch too there will already be some SHA-3 ASIC development.

## fluffypony | 2019-03-15T15:32:09+00:00
Anyone who’s been in this space for a while will attest to how dangerously centralised Monero is right now. The amount of centralisation pressure the anti-ASICs effort is creating is WAY worse than any apparent centralisation ASICs will bring.

Seriously, @SCherynkh, you’re basically the only person tweaking the PoW, with some last minute tweaks by @vtnerd. You shout down anyone who disagrees with your tweaks. There is a much greater chance that the people who tweak the PoW are compromised right now than that ASICs will bring about some sort of destruction.

Again - I have no problem with RandomX being brought to bear, but I do not believe this is a war we want to be in, it will do more to centralise Monero than *anything* else.

## SChernykh | 2019-03-15T15:33:43+00:00
@fluffypony RandomX is mostly tevador and hyc, which makes 3 devs already. I only proposed some limited improvements to RandomX.

## fluffypony | 2019-03-15T15:34:51+00:00
@SChernykh that’s great, but it’s irrelevant to my comment. Go back and read it again.

## SChernykh | 2019-03-15T15:36:26+00:00
I agree that tweaking PoW is useless from now on, but we'll have to change PoW at least one more time however. And I think that RandomX can hold for years.

## antanst | 2019-03-15T15:41:21+00:00
@tarris034 Your question has already been answered in this thread.

## hyc | 2019-03-15T15:47:08+00:00
@antanst 
> The centralization factor of sudden PoW decisions is much more important than pursuing the "egalitarian mining" pipe dream with endless hard forks, especially since this approach has proven to achieve the complete opposite as a result in both aspects of centralization (mining reward distribution & protocol changes). How many people understood the last-minute PoW changes of the last hard fork in detail? Are we sure there wasn't any hidden motive behind those changes? Hard forks should give rise to those kind of questions.

We knew this and asked these questions already, over a year ago. That was when we agreed to do small PoW tweaks while investigating a longer term PoW change. Nobody has ever wanted to keep doing endless last-minute minor PoW changes, that was never the plan. The plan was to do them as needed until a long-term PoW was available. That long-term PoW is now available and (after reviews) ready to deploy. It's frankly stupid to abandon the plan at this point and talk about shifting to ASICs, when the final stage of the plan is finally ready.

## justinjja | 2019-03-15T15:53:40+00:00
@tarris034 you always want to be the largest coin on your mining algo,
Otherwise you risk a super easy nicehash 51% attack.

## floridahaunted | 2019-03-15T16:03:49+00:00
@fluffypony I agree, our anti-ASIC hard fork schedule is a bad practice of centralization. But this practice is a logical consequence of our poor understanding of ASIC/FPGA nature and fundamental physics laws in mining point of view.

It is quite obvious, if mining algo will emulate the behavior of all the tasks that are typically being done by human on PC, with precision good enough, then ASIC/FPGA manufacturers will have to implement something like Intel/AMD CPU. Thus, generally speaking, it is not our competition, it is a competition of ASIC/FPGA manufacturers against Intel/AMD.

I've proposed adjusted_RandomX depends on long_hash(all_transactions_from_last_100_confirmed_blocks). I believe, it will be sufficient for the last hard fork we have to do (and no more hard forks).

@SChernykh No, I mean proportional reduction of memory scratch pad, i.e. 256Mb instead of 4Gb FOR MINING (not verification). It is needed to support weak CPUs like ARMs in Raspbery Pi, or old/weak PCs with low memory. I believe virtualization nature of RandomX is much more significant than actual memory amount we select for scratch pad.

## WhyIsThisSoSlow | 2019-03-15T16:06:24+00:00
Let me put this differently for the supporters of ASIC. What will Monero become if it is viewed as an ASIC coin that can be sucked dry by powerful ASIC creators? An ASIC "privacy" coin? I seem to recall them not doing so well. What would the price drop be after most miners sell the currency and create a mass sell scenario? Would ASIC creators still find the currency interesting after the value drops like a rock? Of course not, price will go down, asic creators will have no incentive to produce more asic because no one will want them. And thus the end of the Monero ASIC fork and the continuation of the Monero CPU/GPU. Is this really what we want to do with this project? Do we need do stray away from core principles? If ASIC is inevitable, let it be, the market will decide when to adopt ASIC, but if you ask me, thats not gonna be very soon if the difference in profitability is low due to a good algo. 



## SChernykh | 2019-03-15T16:06:56+00:00
@floridahaunted No, 256 MB is too weak, it's possible to create an ASIC with 256 MB on-chip memory. Plus, we don't want IOT devices and old weak PCs which are susceptible to malware to be botnet mining RandomX.

## ArticMine | 2019-03-15T16:07:52+00:00
@antanst 

I am aware of the report and there is a fundamental unstated assumption namely that the ASIC question is binary: dominance or elimination. This assumption has been shown to fail already in the Ethereum blockchain. The issue of course is the ASIC advantage. If the ASIC advantage is say 100x or more, very much the situation for example in Bitcoin or what would happen with SHA-3 then the assumption holds true and if the ASICs get a foothold in the network then they dominate. The reality on the Ethereum network for at least the ;last year is very different. ASICs are present but have not taken over and are in fact coexisting with GPU miners. The reason is very simple the ASIC advantage is not 100x but more like 2-4x. There current discussion in the Ethereum community regarding a POW change to lower the ASIC advantage to around 1.2x.  Monero may have been the first, but is certainly not the only major coin that is considering hard fork POW changes to deal with ASICs . My take is that RandomX would lead to a small ASIC advantage that while preventing ASIC dominance could very well allow for some ASIC coexistence.

@fluffypony 

One very significant risk of ASIC dominance is the current situation in Bitcoin where 60-70% of the Bitcoin hashrate is behind the Great Firewall of China. The creates a substation for a state sponsored Sharkpool https://sharkpool.cash/ attack. All the Chinese government would have to do is to quietly indicate to the principals behind the Bitcoin miners that their Social Credit would significantly increase it they did the patriotic thing and mine empty blocks. The dynamic is significant for the following reasons:

1) China has discouraged if not effectively banned the use of Bitcoin in China
2) China has tolerated if not encouraged the industrial mining of Bitcoin in China
3) 1) and 2) above effectively puts the Chinese government in control of a foreign financial network that is hardly used in China at all.
4) Even without  state encouragement the latency introduced by the Great Firewall of China encourages the mining of empty blocks. Furthermore the issue of latency due to the  Great Firewall of China has already impacted the blocksize scaling debate in Bitcoin.
5) The situation above gets magnified in Monero because of  the 2 min block time and the adaptive blockweight. **All it takes is 51% of the hashrate to effectively freeze the block weight in Monero at 300000 bytes which to all intensive purposes is changing the rules.**  
6) Even the potential threat as I described about of a foreign government been able to shut down a financial network with significant domestic use  would be of concern to a regulator once the regulator figures out the risk.. Consider the situation of the Bitcoin Lighting taking off in the United States and US regulators connecting the dots that the Chinese Government effectively controls this popular financial network . This is not theoretical. There is a  Chinese citizen currently under house arrest in Canada pending extradition to the US, over not unrelated fears. Chinese control of cellular networks. This arrest is at the core of a major diplomatic incident between China, Canada and the United States. 

One advantage of a low ASIC advantage and ASIC co existence is the economic incentive for an ASIC producer in China would be to sell for export as opposed to operate in China the ASICs produced.

@livinginformation 

I propose the above as an additional risk under 1) in your post. 

## floridahaunted | 2019-03-15T16:19:10+00:00
@SChernykh it is impossible to create ASIC with 4Gb? And never will be possible? I am sure it will be possible soon. Our main focus is to design mining algo that forces ASIC manufacturers to implement Intel-like CPU and thus to compete with Intel/AMD directly. This may be achieved by virtualization and randomization good enough.

What about malware, modern antiviruses made great progress in detecting hidden miners last year. But the problem is open "white" mining, when end-user does agree with it. In many cases end-user may prefer to agree with open mining at idle priority and low CPU usage, than to pay for software or to see highly abused Ads.

## SChernykh | 2019-03-15T16:22:40+00:00
@floridahaunted 4 GB will require external high-latency DRAM and memory controller. 256 MB can fit on-chip and it'll be an order of magnitude faster.

## dEBRUYNE-1 | 2019-03-15T16:28:22+00:00
>Our main focus is to design mining algo that forces ASIC manufacturers to implement Intel-like CPU and thus to compete with Intel/AMD directly. 

You're describing RandomX. 

## MoneroCrusher | 2019-03-15T16:28:36+00:00
> The centralization factor of sudden PoW decisions is much more important than pursuing the "egalitarian mining" pipe dream with endless hard forks, especially **since this approach has proven to achieve the complete opposite**

**PROVEN?** Is this how you go about life? Try once (literally, we just had 1 anti-ASIC algorithm so far) and if it doesn't work, throw the baby out with the bathwater?

I suggest seeing how Cryptonight-R goes and if it effectively blocks the ASICs in the 6 month window.

If that doesn't work then I suggest dual PoW with RandomX + Cryptonight-R-GPU + a **[pseudo](https://github.com/monero-project/meta/issues/316#issuecomment-472677985)** fork schedule into eternity. @dEBRUYNE-1 can you please add it to the list, so people know what it's about? It's been 2 days now.
10. Game Theoretical approach to ASIC resistance

## floridahaunted | 2019-03-15T16:33:40+00:00
@SChernykh agree, it is a risk that if we'll design mining algo not perfect enough. But if algo is perfect, there is no matter, whether memory fits on chip or not: they have to manufacture Intel-like CPU, by definition of perfectness. But I don't persist on actual values, if you strongly believe they are critical. Indeed, Intel-like CPU emulation may require 4Gb scratch pad... or may not. Let's focus on perfectness, virtualization and randomization and keep in mind open "white" mining that may be important to libertarian industry of future.

## dEBRUYNE-1 | 2019-03-15T16:36:04+00:00
>Try once

Arguably we've tried three times. 

- Original CryptoNight - ASICs eventually dominated the network
- First tweak - Some ASICs showed up, but did not dominate the network
- Second tweak - ASICs eventually dominated the network

I guess point two and three can be collapsed in a single point, as it falls under the PoW tweak strategy. RandomX will be our third try. Why anyone would continue trying if that fails is beyond me. 

>can you please add it to the list

I'll try to find some time later today. Like I said before, I have to add some other stuff and I want to make a single edit, which is going to take some time. 

## MoneroCrusher | 2019-03-15T16:47:25+00:00
> Arguably we've tried three times.

Original: That doesn't count, the fork schedule wasn't even known then
First tweak: doesn't count in my opinion, as it was only meant as a stop-gap and was a 1 line change
Second tweak: the first real tweak meant to make ASIC life harder (and it worked -> 128 kh/s)

If anything, I believe CNv2 was a fundamental success, but the schedule was still way too open even for 128 kh/s and their production economics.
Let's assume CN-R makes those 128 kh/s -> 40 kh/s.
I'm genuinely wondering if ASICs would come back for the 6 month period. When they have increased die area, increased complexity, increased production cost and less to no ROI.

also for the static-algo proponents, imagine:
What do you think ASIC manufacturers prefer to make an ASIC for?
1. a technically hard-to-implement (and untouched) algo but **static** (i.e. RandomX's 2-3x)
2. a technically hard-to-implement algo but dynamically and unpredictably changing (i.e. CryptonightR's 6-7x)

I'd bet it's 1.

If anything I believe 1. is a dream for ASIC manufacturers. They get a new untested, unaudited algorithm and if they crack the goldmine they can loot it and then instantly implicitly activate SHA-3 (also a dream for them) and also loot it from the beginning since they will have the info before everyone else does and can proactively pre-craft SHA-3 ASICs and have the honor to be the first company to scam the public with shady ASIC business and cement SHA-3 forever.
At that point Monero is an ASIC chain and it will not be reversible. At that point all spirit of Monero will be gone, and yes I agree, it will be another unegalitarian ASIC shitcoin.
So let's please not go down that path.

They're tired of good ol' Cryptonight and by making it economically less & less interesting they will eventually throw in the towel (especially when **commiting** [10. Game Theoretical approach to ASIC resistance](https://github.com/monero-project/meta/issues/316#issuecomment-472677985)).

## ArticMine | 2019-03-15T17:00:01+00:00
@dEBRUYNE-1 

Or we can argue there was only one try, the original Cryptonight. There is a fundamental difference between a tweak that simply buys time. and a POW change that has a material impact on the ASIC advantage.  The two changes in 2018 were tweaks that were well known at the time would not last. They were only justifiable a means to buy time until something better was developed. This something better is RandomX, which by most analysis is likely to have a very significant impact on the ASIC advantage.  I would consider Cryptonight-R in between, but there are those who believe it is more than that. 

Tweaks that  just buy time and have no material change in the ASIC advantage are unsustainable. There is little debate about that. POW changes that have a material impact, in a geometric sense, on the ASIC advantage are very much sustainable over the long term. Do that enough times and an ASIC advantage that allows for ASIC dominance will be gone. 

## zexanana | 2019-03-15T17:26:42+00:00
@ArticMine exactly.

Plus, I fear that if RandomX fails to meet the "below 2x ASIC gap difference", the crowd advocating for ASICs right now will have a huge force in changing to ASIC friendly. It is possible RandomX will fail but when the time comes, it will be necessary to evaluate degrees of failure (failed by what performance gap difference? how long until this was acheived?, etc...) and not rush into ASIC friendly.

> I guess point two and three can be collapsed in a single point, as it falls under the PoW tweak strategy. RandomX will be our third try. Why anyone would continue trying if that fails is beyond me.

We should continue trying because from some of the most technical people in this discussion, there is consensus that an algorithm **can** be designed to be ASIC resistant.

## fluffypony | 2019-03-15T17:30:55+00:00
> Let me put this differently for the supporters of ASIC. What will Monero become if it is viewed as an ASIC coin that can be sucked dry by powerful ASIC creators?

Since a significant portion of the supply is already in circulation I can’t pay much attention to someone who uses purposely emotive terms like “sucked dry”. Clearly that’s not possible. Be precise when describing risks and we can have a conversation.

## MoneroCrusher | 2019-03-15T17:36:29+00:00
@fluffypony that's still 432 XMR per day into all eternity. Definitely more interesting than Bitcoin 10-15 years from now and given that Monero should be a top 3 coin, and eventually will be (imo).

We will never see a fair SHA-3 market, just look over at Bitcoin. After 7 years it's still absolute shit with 60%+ of hashpower behind the firwall of China.
What makes you believe it will be different for Monero if going down that path?

## fluffypony | 2019-03-15T17:39:28+00:00
Why should Monero be a top 3 coin? Seems a silly assumption to base anything on.

Additionally, what makes you think 60% of Monero’s GPU hashrate isn’t currently behind the Chinese GFW? Where’s your proof to the contrary?

All I’m seeing are pipe dreams from a number of people who imagine Monero’s mining network is made up of Venezuelans with GPUs mining despite the power blackout🤦🏻‍♂️

## antanst | 2019-03-15T17:39:52+00:00
@hyc 
> The plan was to do them as needed until a long-term PoW was available. That long-term PoW is now available and (after reviews) ready to deploy. 

@ArticMine 
> My take is that RandomX would lead to a small ASIC advantage that while preventing ASIC dominance could very well allow for some ASIC coexistence.

I wish I could share your optimism about RandomX's long-term feasibility (where long term is measured in the span of years) without any further tweaks, but what history has taught us is that 1.PoW is _very hard_ to get right (I believe you saw that yourself after all the hard work of the promising RandomJS was discarded) and 2. that we've continuously been underestimating the ingenuity of the ASIC manufacturers when the right economic incentives are in place. And if RandomX proves to have flaws and require further tweaking a few months ahead, we will have followed an even more risky path to get to the same situation we're in right now. Or maybe worse.

I'm not a PoW expert though, so I hope I'm wrong and RandomX proves to be as solid and resilient as advertised.

@hyc 
>It's frankly stupid to abandon the plan at this point and talk about shifting to ASICs, when the final stage of the plan is finally ready.

Regardless of whether RandomX is deployed or not, my opinion has always been that shifting to ASICs should definitely _not_ be immediate but in the future, in a few years maybe. What's more important is that it's done in a controlled manner via setting a _plan_, proactively.

## MoneroCrusher | 2019-03-15T17:40:38+00:00
@fluffypony I say only switch to SHA-3 when it has really become fair, meaning you can buy them in every computer store from many manufacturers (like GPUs and CPUs), and no, Monero will not be able to "incentivize" a fair SHA-3 market, that is laughable at best and a pipe dream as well, as you like to put it.

Making the algo simple helps, as in, many startups can design it. But the powerhouse of production is still China and Innosilicon, Bitmain and others (which I believe to have very close ties if they're not even just shadow companies of one big ASIC manufacturer) have the large monopoly and nothing is going to change that.

## MoneroCrusher | 2019-03-15T17:46:38+00:00
@fluffypony on a less serious note: why should Ripple be a top 3 coin? The market will eventually figure out which projects are the real ones with substance behind them and not just PR and figdet spinners (literally 😄).

## WhyIsThisSoSlow | 2019-03-15T17:51:53+00:00
@fluffypony 
I get how “sucked dry” might have been perceived emotive but it was just a metaphor for the damage that ASIC monopoly can produce.
There is no point on discussing such insignificant flavors of communicative perception if the main idea remains the same.
ASIC will create an unhealthy monopoly that will affect the image of the Project and price of the coin.
This will in turn produce less profitability and the huge chain effect that will ultimately destroy the coin.
You guys are basing this to much on perfect technology and forget about the humans that are driven by profit.
Ask any marketing specialist and they will advise against ASIC in the current state of availability and because of the way availability can be manipulated.

Not a very good example but one that needs to be looked at is ETN. They decided on ASIC for the stability of the network. All things aside... its a booming project, except its now worth so little that not even ASIC producers will have any incentive to create for it soon.

Even if the above is not that good of an example, lessons can be learned from the bad aspects of ASIC monopoly.

## tarris034 | 2019-03-15T18:10:23+00:00
<some_coin_name_here> devs are using MTP to fight off ASIC with 4GB requirement so could be very similar approach as RandomX but I did not read into it yet.

Even if ASIC manufacturers optimize their hardware miners to be X times faster, it's still better than nothing (going fully ASIC).

Maybe increasing the memory requirement in future would be enough to fight off ASIC with on-chip memory, without the need to change how the PoW calculates the hashes.

I don't know if i'm right on this, ain't ASIC with external memory too slow to be a threat ? 

## fluffypony | 2019-03-15T18:21:20+00:00
@WhyIsThisSoSlow

ETN has a “mobile miner” for phones that literally doesn’t mine, but airdrops their premine. You literally couldn’t have picked a worse example.

## ArticMine | 2019-03-15T18:29:00+00:00
@zexanana 

The criteria I would use for failure is not failing to meet some arbitrary ASIC advantage say 2x but rather ASIC dominance. ASIC miner co existence with CPU miners and / or GPU miners  over a significant period of time is not failure and may even be more desirable than no ASICs at all. There are very important lessons here from what is going on in the Ethereum community including the discussion on further tightening the ASIC advantage. 

@fluffypony 

What proof do you have that 60% of the Monero GPU / CPU hashrate is behind the Great Firewall of China? The economics for this make no sense. The case that the 60%-70% of the Bitcoin hashrate is behind Great Firewall of China is well established and is a direct result of ASIC dominance. This is a historical fact. 

@fluffypony  @antanst 

My position is not based upon pipe dreams or wild ether dreams (pardon the pun) . I have to take into consideration the ASIC situation in Ethereum which is fundamentally very different from that in Bitcoin. The feasibility of tight ASIC advantages, with the likelihood of ASIC co existence  has already been proven on the Ethereum network. What this provides is evidence that what RandomX is trying to do is very feasible.  If one only looks at the Bitcoin ASIC experience i can see a possible although debatable case for SHA-3 at this time. If one also takes a serious look at the ASIC experience in Ethereum the case for SHA-3 at this time breaks down fast. 

## WhyIsThisSoSlow | 2019-03-15T18:30:11+00:00
@fluffypony 

This is why i said its not a good example. As a coin its not that similar but as a project its been booming and getting better and better with acceptances from many exchanges and so on (they even have a phone now, crazy right?). All that while its price is going down constantly after the ASIC switch.
Lets not filter only what we want from the examples provided here. I was obviously talking about the ASIC effect on the network after the fork and not on how similar the coin is.







## xiphon | 2019-03-15T19:00:37+00:00
**Implementing the algo that won't be 4x-??x profitable on ASICs is definitely possible**
Take a look at the Ethereum. Ethash is the best example of non ASIC-friendly algo. It is still most profitable on GPUs, although there are Ethash ASICs in the wild for quite a long time already.
And it even provides fast verification time on devices with small memory footprint.

**GPU is a commodity hardware** 
ASIC is not, and won't ever be

**GPUs have a variety of other use cases, is not feasible to control/prevent GPU supply chains**
Pretty easy for a random powerful third party to control/shutdown/takeover ASICs manufacturing and distribution channels

## pigfrown | 2019-03-15T19:38:13+00:00
Seems to me that all these arguments for GPU/ASIC reistance suggest that an ARM/smartphone based algo would be even better.

I am not seriously suggesting an ARM based RandomX, but would like to ask the people advocating sticking with ASIC resistance what they think of this idea? (Let's assume it's technically possible, which seems fair because many people are making the same assumption with regards to GPU ASIC resistance)

Here are some of the arguments:

> GPU is commodity hardware available off the shelf globally

Smartphones are much more common than GPUs, and much easier for people globally to acquire.

> GPUs are made by more manufacturers than ASICS/better distributed

GPUs are made by 2 manufacturers, there are more companies producing smartphones and they are far better distributed. (literally like candy in corner stores)

> GPUs have a variety of other use cases, is not feasible to control/prevent GPU supply chains

Smart phones have way more use cases than GPUs.

---

Why GPUs over smartphones?




## fluffypony | 2019-03-15T19:41:35+00:00
@WhyIsThisSoSlow sorry, but you lost all credibility when you mentioned ETN. Doubling down on that isn’t doing you any favours.

## fluffypony | 2019-03-15T19:43:28+00:00
@pigfrown only *one manufacturer* makes GPUs for smartphones, and that’s ARM. Please don’t derail the conversation with poorly researched suggestions.

## MoneroCrusher | 2019-03-15T19:43:42+00:00
> GPU is a commodity hardware
> ASIC is not, and won't ever be

This is the logical statement of the day.
Why should something become a commodity good if it only has one specific purpose - that is, to secure a cryptocurrency chain (that in itself is not even remotely close to any real world adoption yet)?

## hyc | 2019-03-15T19:49:05+00:00
@fluffypony No, there's also Qualcomm Adreno (which they bought from ATI) and Imagination's PowerVR. Anyway, it's sufficient to CPU-mine on smartphones, we don't really need to use their GPUs.

## WhyIsThisSoSlow | 2019-03-15T19:53:44+00:00
@fluffypony 

So discussing the issue and providing examples that show ASIC bad influence is hurting my credibility?

I am not here to try and compete in credibility with the oldies of Monero that are promoting ASIC.

The logic behind my statements is clear an can be seen by anyone reading this thread.

Just the fact that you blindly disagree with the logical points made by everyone here shows where this "debate" is heading.

This is just like me saying "oh wow fluffypony i can not give you credibility because you support ASIC" and i will refuse to acknowledge you even if you may have good points.

I understand your position gives you more "credibility" but the faith of this project can not be based on credibility over pure facts.



## fluffypony | 2019-03-15T19:56:29+00:00
@hyc you’re right, I’m misspoke and forgot about Qualcomm. Nobody’s using PowerVR except Mediatek, since Apple abandoned it😂

## fluffypony | 2019-03-15T19:59:23+00:00
@WhyIsThisSoSlow no clue what point you’re trying to make in that word salad. As I said, you discredited yourself the minute you tried to give credibility to a half-baked, unused, pointless clone of Monero. It’s better if you either pick different examples moving forward, or leave altogether. I doubt the Monero community has time for discussions centred around scammy clones of itself.

## MoneroCrusher | 2019-03-15T20:00:54+00:00
@fluffypony chill. He was just trying to make a point with the ASIC network of _the coin that shall not be named_, which is very clear if you read his post. Doesn't not make _the coin that shall not be named_ a shitty scamcoin.
I also don't see where he gave any credit to it, he actively said it's not a good example.

## fluffypony | 2019-03-15T20:08:11+00:00
@MoneroCrusher it’s a distraction. fin.

## WhyIsThisSoSlow | 2019-03-15T20:12:46+00:00
@fluffypony its kinda low to attack a person by referring to its statements as word salad, dont you think?

Who is loosing credibility now? Me? Or the people that prefer to be "grammar nazi" and refuse to acknowledge the logic?

I will stop this here as i do not want an ignorance war to be the main attraction of this topic.

<3 Monero


## JohnnyMnemonic22 | 2019-03-15T20:30:42+00:00
I don’t think @WhyIsThisSoSlow’s point was lost. 51% attacks are hardly the only concern of an ASIC dominated network, which is the topic where the above exchange originated. To suggest otherwise would be rather disingenuous. 

## Hueristic | 2019-03-16T01:36:19+00:00
> 
> 
> @WhyIsThisSoSlow @floridahaunted Interestingly, me @tevador and @hyc **(the ones who work on PoW**) all agree that asic resistance is possible, we don't see the need to switch to SHA3.

Well I'm sold



## MoneroChan | 2019-03-16T11:22:15+00:00
@tevador 's RandomX can be improved if we let CryptonightR's Random code run as long as possible.

We Will Gain The Following:

- 1. Critical intelligence on our enemies approach and effectiveness of handling Random programs (CNR, RandomX) and the option to modify RandomX's VM Parameters based on that.

- 2. Destroy Funding for a RandomX ASIC.
Once created, CNR ASICs are likely too slow now to ROI before a hardfork, so we can bankrupt the ASIC manufacturer, crippling their ability to make an ASIC for RandomX. 
(thus extending RandomX usable lifetime)

## tarris034 | 2019-03-16T12:49:52+00:00
I don't see why we should change PoW before another ASIC attack on the network, let them lose money on the current cn/r and only then change to RandomX.

## WhyIsThisSoSlow | 2019-03-16T14:26:53+00:00
There have been a number of good ideas passed around here in regards to continuing the ASIC resistance and a good compromise in my opinion is to try and mix them in a way that can create a general way of moving forward with this project.

1. Do not change to RandomX until we know ASIC have been created and they can have an unfair advantage (we can create a new topic to discuss the best way to establish this and what is considered unfair) This will give us time for point nr. 2.

2. Continue developing and improving RandomX (or other similar algo) to keep the ASIC advantage as low as possible and only perform an algo change fork if the unfair advantage from point 1 is reached.

The idea here is not bricking ASIC but reducing the unfair advantage till ( and if ) they become as easy to buy as a CPU for example. 

There is still the risk of governments banning them so in my opinion the PoW algo will always need to keep the ASIC/CPU performance ratio as close to equal as possible but this can be re-discussed in the future as many variables are unknown right now.

3. Mostly the same as nr 2 but with making sure the changes made brick curent asic as well so that we also gain more time to develop the algo even better. 
This is where game theory comes into play.


There might have been other good ideas in the topic that i may have overlooked that can be combined to the above principles to give more strength.

We need to continue this discussion and remember the freedom and privacy that Monero stands for.

<3 Monero



## tarris034 | 2019-03-16T14:49:20+00:00
The worst part here is that only a handful of people know about this discussion and majority of miners who love Monero don't even know their favorite coin can turn into ASIC-friendly shitcoin.

## fluffypony | 2019-03-16T14:54:01+00:00
@tarris034 Monero miners are going to get crowded out by professional miners if Monero continues to grow in market cap. It doesn’t matter what we do, that is an eventuality.

Using emotive language like “ASIC-friendly sh*tcoin” reveals that you’re either a total moron, or you're purposely trying to split the community. But it won’t work, the Monero community has survived attempts to splinter from people far better equipped than you.

## tarris034 | 2019-03-16T15:14:31+00:00
@fluffypony just told you how it is.

You can ask salty on supportxmr chat how I defended XMR and said if split happen, it will die the same way as XMO (we were arguing about RandomX), while you're at it you can ask him how I defended You from insults. And now you're calling me a total moron. Thanks man.

It's already crowded by professionals, I'm yet to see a farm capable of 700 MH/s on CPU/GPU.
CPU/GPU PoW is too expensive even for big investors to go 50% of the network, it isn't the same for ASIC as I explained before, unless you don't care about decentralization.

And Yes, ASIC-Friendly coins are ALL shitcoins. No exceptions.

## abhishek1104 | 2019-03-17T17:15:45+00:00
My vote is for ASIC resistance to be continued.Let Aeon / Wownero go ahead with ASIC friendly approach.

ASIC lovers may fork Monero and make their own coin no body is stopping them to do it.But please leave Monero !

## fluffypony | 2019-03-17T17:22:03+00:00
> My vote is for ASIC resistance to be continued.Let Aeon / Wownero go ahead with ASIC friendly approach.
> 
> ASIC lovers may fork Monero and make their own coin no body is stopping them to do it.But please leave Monero !

@abhishek1104 this is a meaningless comment that doesn't move the conversation forward in any way. Try some actual reasoning next time.

## abhishek1104 | 2019-03-17T17:30:22+00:00
Bro,my point is simple that I am with the people who support ASIC resistance for Monero to be preserved.
For me as long as Monero sticks to ASIC resistance I will keep supporting it ,the moment it adopts ASIC friendly ,for me it would be a just another random shit coin.

Do you know you can't even import ASICS in certain countries !

Anyways I rest my case,for you it might be just a random vote,but remember each contributor brings with himself/herself certain value to the project and the loss of each contributor is a tangible loss to the project (for you it might be a meaningless comment but for me it is not as I love Monero for being ASIC resistance along with other privacy features as a WHOLE)..

## tarris034 | 2019-03-17T17:34:52+00:00
@fluffypony 
Your interview: https://www.youtube.com/watch?v=A0bYmy88iGU
1:32 - History repeats itself fluffy, but now you're the one being gigantic douche nozzle.

I think you have your nose up your ass so far you can't reason like a normal person.

## tarris034 | 2019-03-17T17:37:29+00:00
> Bro,my point is simple that I am with the people who support ASIC resistance for Monero to be preserved.
> For me as long as Monero sticks to ASIC resistance I will keep supporting it ,the moment it adopts ASIC friendly ,for me it would be a just another random shit coin.
> 
> Do you know you can't even import ASICS in certain countries !
> 
> Anyways I rest my case,for you it might be just a random vote,but remember each contributor brings with himself/herself certain value to the project and the loss of each contributor is a tangible loss to the project (for you it might be a meaningless comment but for me it is not as I love Monero for being ASIC resistance along with other privacy features as a WHOLE)..

Most small and medium farm owners that I talked to said they will sell their XMR holdings if ASIC PoW happens.

If someone don't believe, go to any pool chat and ask for your self.

## fluffypony | 2019-03-17T17:41:24+00:00
> Bro,my point is simple that I am with the people who support ASIC resistance for Monero to be preserved.

Why?

> For me as long as Monero sticks to ASIC resistance I will keep supporting it ,the moment it adopts ASIC friendly ,for me it would be a just another random shit coin.

Why?

> Do you know you can't even import ASICS in certain countries !

Vietnam banned cryptocurrencies and then also banned ASICs. If Monero is banned in a country then ordinary, law-abiding citizens are going to be too afraid to use it, much less mine it, regardless of whether mining uses ASICs or otherwise.

> Anyways I rest my case,for you it might be just a random vote,but remember each contributor brings with himself/herself certain value to the project and the loss of each contributor is a tangible loss to the project (for you it might be a meaningless comment but for me it is not as I love Monero for being ASIC resistance along with other privacy features as a WHOLE)..

A contributor is a term that is specific to open-source projects, it refers to someone who has contributed code to the project. Please don't misuse the term. Additionally, if we keep attempting ASIC resistance and Monero becomes centralised it will lose a LOT more than some community members.

## fluffypony | 2019-03-17T17:43:27+00:00
> I think you have your nose up your ass so far you can't reason like a normal person.

This is unnecessarily aggressive and doesn't move the conversation forward.

## tarris034 | 2019-03-17T17:48:10+00:00
> > I think you have your nose up your ass so far you can't reason like a normal person.
> 
> This is unnecessarily aggressive and doesn't move the conversation forward.

You're right, sorry. I get too emotional sometimes when it comes to Monero.
I like your paranoid approach, anyone here can have some secret agenda but I'm not one of them.

## fluffypony | 2019-03-17T17:54:31+00:00
> Most small and medium farm owners that I talked to said they will sell their XMR holdings if ASIC PoW happens.

If the switch to something like SHA3 is locked in to the future then they're welcome to walk away, any hashrate vacuum will be filled by other miners.

Additionally, per [Crypto51](https://www.crypto51.app), it costs a mere $5218 to 51% attack Monero for an hour, vs. $353215 to attack Bitcoin for an hour. It even costs more to attack Bitcoin SV than to attack Monero!

The reason for this is simple: ASICs attract large, professional mining farms, who are heavily invested in securing the network because their ASICs can't do anything else. When you are the largest cryptocurrency for a given algorithm, and ASICs exist, then the only way for anyone to attack you is to either manufacture, buy, or rent more equipment than is independently mining on the network. For CPU / GPU coins it's different, large scale farms will mine whatever is most profitable, without caring at all about a single network.

## tarris034 | 2019-03-17T18:00:22+00:00
According to the linked site the attack is still too expensive (for longer period) to be a realistic threat and there's not enough hashrate to buy from nicehash.

I doubt there's any company/bad actor selling only 1 hour of that much hashrate, and I doubt anyone has that much power to sell.

If you link me to buy offer for 51% hashrate, I will believe. That's about renting, Buying hardware to make that attack is unrealistic. (renting hardware from usual suppliers is out of the game, too expensive for anyone and it's not allowed by most companies to mine crypto)

## justinjja | 2019-03-17T18:06:38+00:00
That site just estimates the cost to 51% as 51% of the blockreward * price,
Not an actual cost to 51% the coin.


## justinjja | 2019-03-17T18:10:19+00:00
Take Dash for instance, 
Genisis mining could easily 51% that coin.
It would cost them nothing to do (they would actually make money 51%ing it), 
until Dash forks and it costs them Millions of dollars worth of bricked hardware.

## justinjja | 2019-03-17T18:16:08+00:00
The "Nicehashable" percent is not right either.

Currently 4% of CNR hashrate is on nicehash,
But if you put in an offer to pay 10x the going rate for CNR hashrate.
Every gpu on nicehash would automatically switch to CNR.
There is something like 200k gpus on nicehash.
Not enough to 51% Monero, but fairly close.

## tarris034 | 2019-03-17T18:29:58+00:00
> There is something like 200k gpus on nicehash.

Where did you get that number from ? just dividing the hashrate from other gpu-minable coins ? or is there some place on the site you can view ?


## JustFranz | 2019-03-17T18:35:06+00:00
How is a switch to an ASIC pow supposed to happen so that Monero is not left at the mercy of factors that it can't control or influence? I can't envision a scenario like that in the next 2-3 years and there is no point predicting beyond that. 

How long have we worked on the hardware wallet? I have limited faith in our ability to even fund an ASIC design. Its going to have to be done by other companies for their own benefit.

As per this Monero Talk https://youtu.be/ItgMCasTP4k?t=3439 it takes a month to roll out ASICs for a cryptonight algo. Once ASICs appear for an algo, a tweak won't buy you meaningful time to prevent ASIC breakeven ROI + profit. Only an emergency fork that bricks those ASICs can do that, emergency forks are not sustainable. Maybe we can plan for a single one and that is only if its for carrying us over to something more sustainable.

A non ASIC POW can not afford to be more GPU friendly or FPGA friendly if that means that it would make for a more efficient ASIC implementation, which would increase incentive for ASIC production and reduce ROI time, for a price point. Sorry GPU owners.

I'm not convinced that a POW is not possible that could not meaningfully reduce the efficiency difference between CPU and theoretical ASIC, enough to prevent/delay and eventually significantly reduce its impact on the network. Perhaps to a point where even co-existence is possible, no POW meddling needed, efficiency competition between CPU and ASIC generations. One has the benefit of production node, R&D and economies of scale, the other the purpose built nature of it.



## SChernykh | 2019-03-17T18:41:03+00:00
@fluffypony What changed since September last year?

https://github.com/monero-project/monero/pull/4218#issuecomment-418086651

> Note that I'm not the decider of things; if the community decides it wants to be ASIC resistant forever who am I to do otherwise. But beyond that, @SChernykh is correct - it is my hope that we stave off ASICs until there is an algorithm we can switch to that is sufficiently commoditised.

## fluffypony | 2019-03-17T19:17:53+00:00
> @fluffypony What changed since September last year?

This last fork. It was an absolute mess, way too centralised, totally wrecked the release engineering, and was reactive. We've tried staving off ASICs, and thus far we've failed.

RandomX seems like a nuclear bomb that will have an impact on minimum spec required to run a node, as well as IBD and sync for years to come. It increases CONOP to try win a war that we always knew could not be won.

I'm...*ok* with RandomX as a stopgap with a future commitment to a lightweight algorithm that doesn't exacerbate CONOP, but I've been around long enough to know that it's never going to be more than a stopgap, and an undesirable one at that.

## jetbird747 | 2019-03-17T19:21:42+00:00
1. Fork to RandomX later this year.

2. Starting now, create a currency that is a variant of Monero utilizing SHA3 that is embraced by the Monero community. The sole purpose of this currency would be to start the process of getting SHA3 Asics to market.

3. In the future, convert Monero to SHA3 if it makes sense at the time.

## fluffypony | 2019-03-17T19:24:02+00:00
> * Fork to RandomX later this year.
> * Starting now, create a currency that is a variant of Monero utilizing SHA3 that is embraced by the Monero community. The sole purpose of this currency would be to start the process of getting SHA3 Asics to market.
> * In the future, convert Monero to SHA3 if it makes sense at the time.

I don't think this is viable. What happens to the block rewards and subsequent transactions that happen on that independent coin between now and when the conversion happens? What emission curve would it use? There's no way to make it workable, all we'll end up with is a split.

## justinjja | 2019-03-17T19:36:23+00:00
Ethash shows that asic resistance isn't impossible,
Asics have maybe a 2x advantage per watt over gpus?
And that algo is old in crypto years.

Especially if we are willing to switch to a CPU or GPU only algo.
I think trying to support such dissimilar devices on the same algo is why ASICs are always pop up on Cryptonight

## fluffypony | 2019-03-17T19:46:37+00:00
> Ethash shows that asic resistance isn't impossible,
> Asics have maybe a 2x advantage per watt over gpus?
> And that algo is old in crypto years.

Linzhi's ASICs have an 8x power advantage over existing Ethash ASICs. If Ethereum doesn't switch to PoS then what do you think could happen over the next few years?

## justinjja | 2019-03-17T20:46:12+00:00
That doesn't even exist yet does it?
People can claim anything.
a 400W FPGA was rumored to do 2.1GH/s on ethash for months, it was all fake.

## SChernykh | 2019-03-17T20:56:04+00:00
> This last fork. It was an absolute mess, way too centralised, totally wrecked the release engineering, and was reactive. We've tried staving off ASICs, and thus far we've failed.

Because Cryptonight design is weak, tweaking it doesn't help. RandomX design is not weak. I agree we should stop rushed forks and just come up with fixed release schedule, no matter whether ASICs appear or not. Their advantage will be smaller with CryptonightR and not significant at all with RandomX.

> RandomX seems like a nuclear bomb that will have an impact on minimum spec required to run a node, as well as IBD and sync for years to come. It increases CONOP to try win a war that we always knew could not be won.

It can be won if ASICs are not much more efficient. It's possible, and we haven't even tried the real ASIC-resistant algo yet.

> I'm...ok with RandomX as a stopgap with a future commitment to a lightweight algorithm that doesn't exacerbate CONOP, but I've been around long enough to know that it's never going to be more than a stopgap, and an undesirable one at that.

It doesn't really increase cost of node operation. The biggest part in this cost is blockchain size, not compute requirement.

## SChernykh | 2019-03-17T21:07:32+00:00
If you look at VPS prices, even $3 VPS (the first I found in Google: 1 vcore, 2 GB RAM, 20 GB SSD) can handle RandomX compute, but it doesn't have enough space for blockchain. It can still handle pruned node, even with RandomX. If you need non-pruned node, $13 VPS with 80+ GB SSD already has 2 vcores and 8 GB RAM which is enough for fast-verification mode. The main limiting factor here is disk space, not processor/memory.

## JustFranz | 2019-03-17T21:17:07+00:00
We need real comparison data between CNv-8 (whatever the last one was called), CN-R and both modes of RandomX. So these opposing claims of performance can be put to rest and get a definitive answer.

To me it seems like the current algo is about 20 blocks second verification upon IBD and its the same/faster on randomX.

https://github.com/tevador/RandomX/issues/25

## ArticMine | 2019-03-17T21:33:23+00:00
@fluffypony

> This last fork. It was an absolute mess, way too centralised, totally wrecked the release engineering, and was reactive. 

I agree this last fork was handled poorly. First it was not solely due to ASICs. Fear over the "Big Bang Attack" was as significant or more a factor in the rush. Contrast this with how the ASIC fork was handled in the spring of 2018. My take is that we could have stuck to our release schedule and the additional risk for the possible attacks was less than the risk that was created by rushing the process.

I was more involved with the "Big Bang" side of things. The reality is that I had to come up with a new algorithm in under a week, and @moneromooo-monero  had to code it,  and all had to be tested and reviewed also against very tight deadlines. All for an attack that i described three years ago and was significantly  more expensive than a 51% attack.  

On the ASIC side we also managed to also throw out a significant portion of the CPU hashrate through a lack of notice and documentation and many of the pools were caught off guard. The latter was obvious right after the fork. 

The issue with the last fork is the need for a proper balance of the risks involved between waiting and allowing more time for the possible attack vs rushing and significantly increasing the risk of a fatal bug in the code. Solving the ASIC issue one way or another is not going to address the very serious issues with the last fork that you have have very properly pointed out. 

Edit:

> Linzhi's ASICs have an 8x power advantage over existing Ethash ASICs. If Ethereum doesn't switch to PoS then what do you think could happen over the next few years?

CPUs are going to make significant gains over the Ethash ASICs. Seriously when the ASIC advantage is tight then leapfrogging between different technologies can actually occur. There is a huge difference between 8x and the 100+x that something like SHA-3 will lead to. Furthermore this is with no reaction from the Ethereum community. There is also considerable discussion there  about changing the POW algo to lower the ASIC advantage further. Monero may have been the first major coin to go after ASICs using forks, but at least another much larger chain is considering the very same thing. 

## jetbird747 | 2019-03-17T22:39:21+00:00
> > * Fork to RandomX later this year.
> > * Starting now, create a currency that is a variant of Monero utilizing SHA3 that is embraced by the Monero community. The sole purpose of this currency would be to start the process of getting SHA3 Asics to market.
> > * In the future, convert Monero to SHA3 if it makes sense at the time.
> 
> I don't think this is viable. What happens to the block rewards and subsequent transactions that happen on that independent coin between now and when the conversion happens? What emission curve would it use? There's no way to make it workable, all we'll end up with is a split.
-------------------------------------------

I was looking at the angle where somewhere in the crypto universe the SHA3 algo seed would be planted. No required connection to the monero project, other than potential support from peers. The purpose of this would be to try to get sha3 ascis built and matured prior to the potential need for monero.


## justinjja | 2019-03-17T22:51:22+00:00
SHA3 (or it's varriants) are already used on a few coins. Smartcash, 0xbtc, ZenProtocol, Maxcoin.
Even Ethash asics do SHA3/Keccak (+ lots of memory bandwidth)

## AirSquirrels | 2019-03-17T23:12:51+00:00
To clarify my stake in this ecosystem, Monero is my largest crypto holding - and I have more that was purchased than mined.

Going pure ASIC with an algorithm such as SHA-3 is much much more likely to end with a centralization of at least manufacturing in any long time scale. All of the ASIC cost/performance structures benefit significantly from economies of scale, which favors a monopoly or duopoly. 

With that said, if you go this route you don’t necessarily need ASICs day one, though they will come quickly.  I and others would happily provide optimized design basis. There are enough broadly distributed (at least as much so as current Monero hashrate) FPGAs right now to make up at least 150,000 GPUs of SHA3 hashrate. 

SHA3 FPGA to ASIC performance/watt delta will be lower than SHA256, and there would likely be be a period of natural transition.

Ultimately RandomX does seem fairly reasonably hardened. I would argue that if it is truly successful, an ASIC-Like manufacturer will just fill boards with power optimized x86 cores (existing chips, tuned) at margins far below consumer / bulk hardware. Centralization of specialized hashpower amongst those with cost advantage compounded by power advantage is inevitable. 

@fluffypony is right - the constant forking and effort level into the PoW development, which is hardy the most important part of a coins ecosystem, carries far more risk and does far more damage than the actual intangible/inevitable risk of concentration of hashpower.

I have also mentioned to some in private that there are entities shopping for HUGE amounts of XMR hashpower in re-purposable hardware, at price points that will never ROI. There are influencing forces at play in this debate far beyond the motivations of commenters here.

My suggestions:
1. Fork to RandomX as soon as reasonably possible, and ignore sudden CN-R hashrate as any kind of a clear indicator that the battle of ASIC resistance is won. I can estimate from our own internals and watching other manufacturer pipelines that the FPGA market alone will have new hardware entering production at a rate equivalent to at least ~100MH/month on CN-R starting before May. I seriously doubt that hashpower will point to XMR, but a motivated actor could. Performance is roughly 120H/W. 

2. If RandomX fails and specialized hardware appears, move on. Let the market for that hardware evolve, or pursue a SHA3 fork then.

3. Consider dual-PoW.  Allow FPGAs and then ASICS on something like SHA3 to slowly onboard over time. 



## emesik | 2019-03-17T23:18:26+00:00
> I have also mentioned to some in private that there are entities shopping for HUGE amounts of XMR hashpower in re-purposable hardware, at price points that will never ROI. There are influencing forces at play in this debate far beyond the motivations of commenters here. 

State actors attempting to derail the strong privacy solution they cannot control?

## SChernykh | 2019-03-18T00:23:16+00:00
> I can estimate from our own internals and watching other manufacturer pipelines that the FPGA market alone will have new hardware entering production at a rate equivalent to at least ~100MH/month on CN-R starting before May

Can you clarify? Are you talking about FPGAs with HBM memory?

## AirSquirrels | 2019-03-18T00:51:11+00:00
Yes - HBM enabled FPGAs from both vendors and a number of manufacturers 

## lookfirst | 2019-03-18T02:57:05+00:00
> Vietnam banned cryptocurrencies and then also banned ASICs.

@fluffypony 

I live in Vietnam (for 3 years) and I have personally mined here, with ~5MW of ASICs, inside a Viettel (govt military telco) data center no less. This statement is totally untrue. You are reading old headline news articles, barely understanding them, you have no understanding of how things work in Vietnam. Then, quoting them as if they are the truth.

They didn't ban CC, they banned buying and selling things with CC in an effort to protect their national currency, which makes total sense. For the record, [trading USD is also banned](https://vietnamnews.vn/society/468533/man-fined-4000-for-exchange-of-100.html) except at licensed dealers.

## fluffypony | 2019-03-18T05:10:27+00:00
@lookfirst I couldn’t find any other articles to backup his point except a small Russian town preventing someone from importing ASICs. To your point, then, the fear over ASIC imports being restricted seems entirely overblown, as the situation in Vietnam proves.

## dEBRUYNE-1 | 2019-03-18T07:58:57+00:00
>If RandomX fails and specialized hardware appears, move on. Let the market for that hardware evolve, or pursue a SHA3 fork then.

Quoting myself:

>This is a bad idea. If you are going to allow ASICs, you'd want to adopt a simple algorithm that has the least possible amount of optimizations. This levels the playing ground and closes the gap between ASIC manufacturers. If you leave room for a lot of optimizations, you will probably end up with a single dominating manufacturer, which is potentially dangerous for the network. Hence, my suggestion to precommit to an ASIC friendly algorithm such as SHA3 in case RandomX fails.

## antanst | 2019-03-18T08:14:03+00:00
> Hence, my suggestion to precommit to an ASIC friendly algorithm such as SHA3 in case RandomX fails.

Let me repeat my questions with that approach then:

- We need to define the conditions under RandomX is deemed a failure. Will they be strictly technical, or they will include possible cases of ASIC appearance?
- If the answer to the above is yes, then how are these conditions going to be defined? A sudden hash rate spike? How about a smoother but ever-increasing hash rate curve?

If we don't think about those questions before we deploy RandomX, we'll soon be back to the "let's see how it goes, and if we smell ASICs we fork" joke mentality, and we're steering ourselves towards an even more dangerous and controversial upgrade in the future.

## SChernykh | 2019-03-18T08:22:52+00:00
@dEBRUYNE-1 
> This is a bad idea. If you are going to allow ASICs, you'd want to adopt a simple algorithm that has the least possible amount of optimizations. This levels the playing ground and closes the gap between ASIC manufacturers. If you leave room for a lot of optimizations, you will probably end up with a single dominating manufacturer, which is potentially dangerous for the network. Hence, my suggestion to precommit to an ASIC friendly algorithm such as SHA3 in case RandomX fails.

Even with SHA3 ASICs you will have one dominating manufacturer. Efficiency is not only about algorithm, it's also about supply chain optimizations and economies of scale. Right now it will be Bitmain. The ASIC market is just not mature enough yet.

## tarris034 | 2019-03-18T08:42:20+00:00
@AirSquirrels 

> 1. Fork to RandomX as soon as reasonably possible

I still don't see why we should rush RandomX deployment, we should let them lose time and money on CN/R first.


> I can estimate from our own internals and watching other manufacturer pipelines that the FPGA market alone will have new hardware entering production at a rate equivalent to at least ~100MH/month on CN-R starting before May.

What that even means ? Nvidia / Intel / AMD are producing much more hardware capable of running CN/R, yet we don't see hills of hashrate hitting XMR.

FPGA is too expensive and doubt any big investor would buy into it knowing it will be bricked minute after RandomX deployment.

Precommit to an ASIC friendly algorithm will encourage ASIC manufacturers to work against us at a loss, sure way to lose war against this attackers.

> I have also mentioned to some in private that there are entities shopping for HUGE amounts of XMR hashpower in re-purposable hardware, at price points that will never ROI. There are influencing forces at play in this debate far beyond the motivations of commenters here.

That's just spreading unnecessary panic, I see nothing wrong with big investors buying hardware that's available for everyone and you can't call it "XMR hashpower" until it's used for that case.

## fluffypony | 2019-03-18T08:53:49+00:00
@SChernykh I can see that argument, but you also can’t deny that there are loads of other Bitmain competitors now. It’s a matter of a couple of years - at most - for Bitmain to lose the last vestiges of whatever dominance it once had.

## MoneroCrusher | 2019-03-18T10:49:53+00:00
@fluffypony not even too long ago basically every single online store (e.g. Bitmain, Innosilicon, Baikal, Ebang etc.) looked almost the same with slightly different colors (they have slightly changed in the meantime).

Who says they are not all just fronts for one big shadow company in the back?
If I had to run an ASIC monopoly and wanted to appear "decentralized" that is exactly what I would do.

I prefer manufacturers like Intel, Samsung, AMD, Nvidia, ARM etc. who have many places of manufacturing, inluding USA, Vietnam, Taiwan, China, Malaysia, Thailand, South Korea, Japan and others... **whose primary business is not crypto**
ASIC manufacturing with single purpose devices (crypto mining) is fundamentally flawed in co-dependence of decentralization.

@fluffypony Personally I feel you are underestimating the importance of ASIC resistance that the Monero community places upon the project.
What has changed in the last 12 months?

@AirSquirrels So what is their hidden agenda? Push Monero to SHA-3 so they can build a huge SHA-3 ASIC business like for SHA-256, milking & scamming the community for a decade?

## tarris034 | 2019-03-18T10:55:32+00:00
We should ask our self, why ASIC manufacturers put so much effort into mining XMR while they could invest their money in better, longerterm investments.

I think they are just building it's way towards mass adoption of cryptocurrency knowing XMR will be one of the prominient cryptocurrencies if not THE cryptocurrency and they want to be able to produce and sell hardware for it.

Their plan is to force Monero devs into switching to ASIC PoW, so they could produce their hardware at minimal costs.

So far they are succeeding with their plan and I have already wrote why it is bad for the network.

## lookfirst | 2019-03-18T10:58:09+00:00
> We should ask our self, why ASIC manufacturers put so much effort into mining XMR while they could invest their money in better, longer term investments.

For profit.

## tarris034 | 2019-03-18T10:59:54+00:00
> > We should ask our self, why ASIC manufacturers put so much effort into mining XMR while they could invest their money in better, longer term investments.
> 
> For profit.

if they were after profit, they would invest in longer term plans that would yield them more profit in the end.

They are "investing" in the future by controlling it. Centralization of power was never so high now that we have devs talking about switching to ASIC.

It's basically THEIR(ASIC manufacturers) forced decision, not ours.

## dEBRUYNE-1 | 2019-03-18T11:02:20+00:00
@antanst 

>We need to define the conditions under RandomX is deemed a failure.

Earlier in the thread, we deemed failure as ASICs having a large efficiency advantage and thus driving out almost all other miners. A few pointers we can use are:

1. Look at the hashrate distribution. If a single entity manages to gain the vast majority of the hashrate, it's quite obvious they have a significant efficiency advantage. I'd consider a hashrate distribution similar to the hashrate distribution leading up to the most recent scheduled protocol upgrade a clear failure. 

2. GPU profitability in comparison with other coins. Whilst there are some ways to game this (as @fluffypony described earlier), I think it would still be a reasonable indicator, especially if there are multiple ASIC manufacturers that managed to tape out an efficient ASIC (they will get greedy if they spot competition and add their ASICs to the network as fast as possible). 

3. Looking for any irregularities in nonce patterns. 

4. Compare efficiency advantage if an ASIC manufacturer decides to publish and thus sell an ASIC for RandomX.

--------------------

@SChernykh 

>Even with SHA3 ASICs you will have one dominating manufacturer. 

That's speculation as long as we are theorizing. 

>Efficiency is not only about algorithm, it's also about supply chain optimizations and economies of scale. 

My point was that *if* RandomX fails and we decide to embrace ASICs, it would make little sense not to switch to an ASIC friendly algorithm such as SHA3. Besides, you'd also enjoy significant verification performance improvements. That is, SHA3 is significantly better with respect to verification performance than RandomX. 

## tarris034 | 2019-03-18T11:10:39+00:00
@dEBRUYNE-1 
> My point was that _if_ RandomX fails and we decide to embrace ASICs, it would make little sense not to switch to an ASIC friendly algorithm such as SHA3. Besides, **you'd also enjoy significant verification performance improvements.**

For the cost of much less decentralization and only single country of hardware origin. I rather have less "significant" performance. 


## dEBRUYNE-1 | 2019-03-18T11:20:05+00:00
@tarris034 - You didn't properly read my comment. It related to a scenario where we embrace ASICs and have to choose between RandomX (this assumes RandomX fails) and SHA3. 

## MoneroCrusher | 2019-03-18T11:27:01+00:00
Somebody from Cryptoslate contacted me after the ASIC nonce analysis and wanted to do a small interview about ASICs, I haven't heard back from them in weeks so here is my answer I gave to them, which applies to this thread very well:

**1. I wanted to get your personal feelings about ASIC proliferation on the Monero network. Why is it important to combat ASICs (in your opinion)?**

Personally I first got in touch with Bitcoin back in 2012 and I learned that you can “mine” it with your computer. I was very curious and I mined it for a short period of time with my discrete Nvidia GPU that I had in my workstation. I was fascinated from the get-go and saw my balance go up by incredibly small amounts. I wanted more & I then decided that I wanted to get into ASIC mining (in 2013) and was ready to kill my piggybank for it.

I teamed up with a friend and we wanted to do a small scale mining operation, nothing big, like $20k. We then looked around and the main players back then were Bitfury and Butterfly Labs. We were immediately put off by the large amounts of negative feedback and scam accusations, where people would write in forums how they'd order stuff in March, were promised to get it delivered by April, then they eventually got their stuff in October but by that time the hardware was already 2 generations old and useless. So many people back then invested their hard-earned money into ASIC miners with the hope of mining Bitcoin but all they got in the end was worthless scrap metal.

We also looked around and contacted several firms in Shenzhen to buy directly from but we were too small fish with our $20k. So we ended up not going through with it, because it was so hard to get ASICs fairly without having special relations with the manufacturers.

The situation today has gotten a bit better with Bitcoin ASICs but to be honest it's still pretty bad. **ASIC manufacturers and customers are competitors, the manufacturers always have to walk a line between self-mining and selling their hardware and they will always optimize their risk in such a way, that they will get the maximum profit for the least amount of risk. They do not have the customers best interest at heart - the customer is their risk buffer.**

The problem is that they don't focus their business on a margin, I've watched them price their ASICs according to what an equivalent in GPU mining hardware would make and during crypto bubbles they ramp up their prices 1:1 with the price growth, while renowned companies like Intel, AMD, Nvidia, Samsung and others have a public image to maintain.

In the 2017/2018 "crypto mania" we haven't seen RX 570 GPUs go for $4500 (the max I've seen it go was $300-350 from online shops), but we did see Antminer S9 (and other ASICs) go for up to $3500 from the manufacturer(s) and even more in the aftermarkets. While today both devices almost have the same price. Guess which device will never break even and will have a small fraction of resale 
value...

I did a small comparison of what $2100 invested in RX 470 would've gotten you vs. what an Antminer S9 (price in June 2016: $2100) would've gotten you when buying both devices end of June 2016, the S9 mining only Bitcoin and the RX 470 mining only Ethereum until today:
![image](https://user-images.githubusercontent.com/32360383/54526253-7a663d00-4976-11e9-9263-9a8207eaf3b1.png)

You'd instinctively think that a device that is made only for mining and that has absolutely no other usecase to be better than some general consumer hardware, right? That has never been the case anytime from 2009 to 2019, for the average hobby miner.

An ASIC is not the problem itself, many devices in your daily life use ASICs (e.g. toasters). The problem is the business practices of the cryptocurrency ASIC manufacturers and that their lives depend on crypto. They are your competitors, not your partners. It's going to take a very long time to build that trust, if it's even possible anymore. The past 10 years have been anything but an optimal relationship with ASIC manufacturers from the consumer perspective and it's going to take years to build trust. Promises serve nothing, if ASIC manufacturers want to see coins adopt ASICs, they have to change their practices for good and I doubt it will happen anytime in the near future.

I'll show you another reason why:
![image](https://user-images.githubusercontent.com/32360383/54526318-af728f80-4976-11e9-8068-263ba113345b.png)
 
The less Bitcoins there are to mine, the more the manufacturers will be ready to become more "fair". But relatively speaking the later they become honest - which they are incentivized to - the less there is for hobby miners to get from the big emission pot.

We are still in a relatively steep curve of new emission, so why should they give up their unique position of plentiful access to new Bitcoins (or any other cryptocurrency)?

That's why it's important to be ASIC resistant, so everyone has the equal chance to mine cryptocurrency. Ultimately cryptocurrency will have a much greater reach and adoption that way, because emission will be more fairly distributed and decentralization directly correlates with network effect and growth.

**2. Is it worth the effort and potential risk to continually change mining algorithms?**

That's a tough one. The idea of continuous and unpredictable forks is to economically disincentivize ASICs because technically they are just inevitable. But as laid out in my above answer the business practices are very shady, so they're not an option unless they start changing, which is accompagnied by a fundamental flaw (fig. 2).

The other approach is to create algorithms like ProgPoW and RandomX that specifically target a certain breed of generalized hardware and use them to their full extend. The problem with that approach though is that energy usage oftentimes doubles because the goal is to use 100% memory bandwidth and 100% core in a GPU, for example. The issue with that is that the more electricity you have to use, the more hobby miners are at a disadvantage. Mostly those algos still end up seeing ASICs with 2-3x efficiency, and according to basic economic theory a more efficient machine will always replace the less efficient one over a period of time.

So in my opinion the ideal practice would be to have an algorithm like Ethash (memory hard), which has proven to be excellent at keeping ASICs to a minimum (efficiency-gain-wise speaking only 2x-3x) and keep forking it in unpredictable ways at a less regular schedule like maybe once a year to discourage ASICs economically. I would then do this as long as 99% of the emission isn’t mined and then switch to a very simple and easily ASIC-able algorithm (like SHA3) and let them slowly take over for the remaining transactional market. This practice would allow for the broadest and fairest distribution of 99% of the emission.

A note regarding RandomX & Monero:
I absolutely believe that hyc, Tevador, SChernykh and others have created a beautiful piece of software that allows for CPU mining only. The problem I see with CPU mining is that hobby miners are at a great disadvantage to professional data-centers and botnets.

While with GPU mining hobby miners are in a very unique position in it that they actually have better cost-effectiveness than even the biggest data-centers you could imagine, like Google or Amazon. Reason being that GPUs are sold in two categories: Enterprise & Consumer. The consumer grade GPUs are not sold to big datacenters and they’d have no use for them. Thus hobby GPU miners have an enormous cost advantage because they get much more bang for the buck with regards to mining and they can absolutely cheap out on literally every other component:

- Gen1/2 x1 PCIE speed with cheap risers ($2 a pop)
- 2-core CPUs ($30)
- minimum RAM ($35)
- Cheap motherboards where you can stuff in 12/13 GPUs (-> you can’t cheaply do that with CPUs) ($70-100)
- Open air rigs ($30-40)
- Ignoring dust and cheaply cool rigs or even a farm with big industrial fans (also cheap)

12 RX 570 will cost you about $1800 (new with 3 years warranty). So we have a pure compute vs. rig cost ratio of about 10:1.
A professional data-center manager would find themself in fetal position if they had to work under such circumstances. The average hobby miner doesn’t care as long as the rig is producing cryptocurrency. That’s why GPU mining is the best shot we’ve got at preserving dedicated & decentralized hobby mining. But I would very much welcome a dual PoW mechanism that preserves both CPU & GPU mining in Monero with a dynamic block reward algorithm between CPUs & GPUs. Many people get into this space by trying for themselves and seeing the system work and a lot more people have CPUs to try it on, usually after getting a taste, most people want to build something dedicated to it and that’s much easier, cheaper & effectively done with GPUs.

**3. Given your research, is there a way the Monero community can make monitoring nonce-forensics and other metrics to detect ASICs more systemized?**
 
Yes I absolutely believe so and that's not just limited to Monero. A takeover of ASICs is a huge change in a network's dynamics. Even if they try to perfectly and stealthily take over a network by analyzing every single possible parameter and implementing it in a way they believe would be undetectable, there's still a very unpredictable aspect: How are the rest of the miners going to react to the changes like increased hashrate? They can't predict that to the nonce and that's where specialized tools should be developed, that will be able to pick up the finest nuances and alert the community in case anything strange is happening.

## tarris034 | 2019-03-18T11:54:29+00:00
With RandomX 1x CPU can be as fast as ~7 GPU's on current PoW so it's much more efficient, I don't see a problem selling GPU's and buying into CPU farm if I was one of the farmers. 

Keeping up GPU profitable for the sake of miners who invested their money puts the whole network at risk as it's much easier to make FPGA efficient miner that would eat CPU/GPU farms.

Mining was never meant to be an investment.
If you made it to be one, it's your problem.

Also don't see any problem with professional data centers mining, it doesn't hurt the decentralization as there are more data centers than GPU farms.

With RandomX monero would get more "green" than any other coin especially ones that are minable with door stoppers, good for reputation.

## SChernykh | 2019-03-18T12:00:11+00:00
> While with GPU mining hobby miners are in a very unique position in it that they actually have better cost-effectiveness than even the biggest data-centers you could imagine, like Google or Amazon. Reason being that GPUs are sold in two categories: Enterprise & Consumer. 

The same applies to server/desktop CPUs, motherboards, RAM. CPU farm built around some middle-end desktop CPUs like Ryzen 5 2600, cheap micro-ATX motherboard and cheap non-ECC DDR4 memory will be 2-3 times more efficient per $. Datacenters also usually spend _a lot_ $$$ for hundreds of GB of RAM in each server which is not really needed in RandomX,

## WhyIsThisSoSlow | 2019-03-18T12:05:49+00:00
Can i get some pros and cons on what i suggested here? 

Please be on point and don't deviate from the sugestions too much. 

If they are bad, please give plausible arguments as to why and provide better alternatives or improvments. 

https://github.com/monero-project/meta/issues/316#issuecomment-473534816

## tarris034 | 2019-03-18T12:13:22+00:00
> Can i get some pros and cons on what i suggested here?
> 
> Please be on point and don't deviate from the sugestions too much.
> 
> If they are bad, please give plausible arguments as to why and provide better alternatives or improvments.
> 
> [#316 (comment)](https://github.com/monero-project/meta/issues/316#issuecomment-473534816)

Those are good ideas but we shouldn't close our minds in pros/cons box, we must try to think beyond that 0/1 logic otherwise SHA3 may seem like a great idea.

How the situation would look if there was no attack from the ASIC manufacturers, would we still want ASIC PoW ? or rather have our crypto be available to mine on ANY hardware with profit ?

They are trying to change our path of thinking, but it only makes us stronger with each new PoW.

## fluffypony | 2019-03-18T12:14:15+00:00
@WhyIsThisSoSlow 

> 1. Do not change to RandomX until we know ASIC have been created and they can have an unfair advantage (we can create a new topic to discuss the best way to establish this and what is considered unfair) This will give us time for point nr. 2.

That's reactive and centralised, and it has to stop.

> 2. Continue developing and improving RandomX (or other similar algo) to keep the ASIC advantage as low as possible and only perform an algo change fork if the unfair advantage from point 1 is reached.

As I understand it, RandomX can't really be tweaked much further, and - again - we're trying to get away from centralised, reactive forks.

> The idea here is not bricking ASIC but reducing the unfair advantage till ( and if ) they become as easy to buy as a CPU for example.

RandomX ASICs are *never going to be commoditised*, even if Monero is the world's reserve currency. SHA3 ASICs have a shot because they will be cheap to design and manufacture.

> There is still the risk of governments banning them so in my opinion the PoW algo will always need to keep the ASIC/CPU performance ratio as close to equal as possible but this can be re-discussed in the future as many variables are unknown right now.

Governments can just ban mining Monero, they don't need to ban ASICs. It's not difficult to detect Monero mining traffic, and - again - it's either going to be hugely effective (people are too afraid to even use Monero, much less mine it) or entirely ineffective (see @lookfirst's [comment above](https://github.com/monero-project/meta/issues/316#issuecomment-473751846)).

> 3. Mostly the same as nr 2 but with making sure the changes made brick curent asic as well so that we also gain more time to develop the algo even better.

No clue what this means.

## MoneroCrusher | 2019-03-18T12:18:53+00:00
> > While with GPU mining hobby miners are in a very unique position in it that they actually have better cost-effectiveness than even the biggest data-centers you could imagine, like Google or Amazon. Reason being that GPUs are sold in two categories: Enterprise & Consumer.
> 
> The same applies to server/desktop CPUs, motherboards, RAM. CPU farm built around some middle-end desktop CPUs like Ryzen 5 2600, cheap micro-ATX motherboard and cheap non-ECC DDR4 memory will be 2-3 times more efficient per $. Datacenters also usually spend _a lot_ $$$ for hundreds of GB of RAM in each server which is not really needed in RandomX,

That's true. But I argue with GPU it's actually much more competitive from this perspective.
And you didn't include the botnet problem into the equation with CPU only.

I'm not saying to stop CPU mining, but I'm saying to not stop GPU mining by doing a dual PoW. Why do we have to rush this? We can implement a dual PoW algo in April 2020, enough time to evaluate one in that time.

## tarris034 | 2019-03-18T12:21:03+00:00
> > > While with GPU mining hobby miners are in a very unique position in it that they actually have better cost-effectiveness than even the biggest data-centers you could imagine, like Google or Amazon. Reason being that GPUs are sold in two categories: Enterprise & Consumer.
> > 
> > 
> > The same applies to server/desktop CPUs, motherboards, RAM. CPU farm built around some middle-end desktop CPUs like Ryzen 5 2600, cheap micro-ATX motherboard and cheap non-ECC DDR4 memory will be 2-3 times more efficient per $. Datacenters also usually spend _a lot_ $$$ for hundreds of GB of RAM in each server which is not really needed in RandomX,
> 
> That's true. But I argue with GPU it's actually much more competitive from this perspective.
> Although
> And you didn't include the botnet problem into the equation.
> 
> I'm not saying to stop CPU mining, but I'm saying to not stop GPU mining by doing a dual PoW. We do we have to rush this? We can implement a dual PoW algo in April 2020, enough time to evaluate one in that time.

You can't fight botnets, from AV companies reports it seems most of them are gaming machines, so good at CPU and GPU mining. Dual PoW = twice as much risk of getting pwnd by FPGA / ASIC.

## MoneroCrusher | 2019-03-18T12:22:41+00:00
You could also argue you're halving the effect of a pwnage. If RandomX gets pwned then there's still the other half. If CN-R-GPU gets pwned then there's still RandomX. The pwned one could get deactivated in a HF and fixed in the meantime.

## tarris034 | 2019-03-18T12:25:54+00:00
> You could also argue you're halving the effect of a pwnage. If RandomX gets pwned then there's still the other half. If CN-R-GPU gets pwned then there's still RandomX. The pwned one could get deactivated in a HF and fixed in the meantime.

You can't just turn off one of the PoW's, community wouldn't like it. There's more probability of GPU PoW getting owned and we're increasing the needed PoW changes from which we are trying to get rid off here.

You can still mine with GPU on RandomX, just not so efficient. It's not bricking them entirely.

## antanst | 2019-03-18T12:41:50+00:00
@dEBRUYNE-1 
> 1.Look at the hashrate distribution. If a single entity manages to gain the vast majority of the hashrate, it's quite obvious they have a significant efficiency advantage. 

The problems with this is that unless we're sure there have been ASICs on the table, we are waging a war against generic efficiency advantages. What if a huge botnet comes into place? How about a very optimized GPU miner taking advantage of something that slipped the devs' minds? We might as well disincentivise mining alltogether and be done with it.

>2. GPU profitability in comparison with other coins. 

From what I've read so far after RandomX GPUs will become unprofitable in most cases, especially if it really takes off.

> 
>3.Looking for any irregularities in nonce patterns.
> 
>4.Compare efficiency advantage if an ASIC manufacturer decides to publish and thus sell an ASIC for RandomX.
> 

OK, maybe nonce patterns and definitely an ASIC manufacturer announcing an ASIC are serious indicators that ASICs have already appeared on the network.
 
My point still stands: We've been doing this all along. There's absolutely nothing RandomX alone gives us towards the long term stability and decentralization aspects of the project other than a hopefully larger ASIC resistance window. When time comes (and it will) we'll have the same issues as now but in a much more dire position.

## fluffypony | 2019-03-18T12:43:05+00:00
> @fluffypony not even too long ago basically every single online store (e.g. Bitmain, Innosilicon, Baikal, Ebang etc.) looked almost the same with slightly different colors (they have slightly changed in the meantime).
> 
> Who says they are not all just fronts for one big shadow company in the back?
> If I had to run an ASIC monopoly and wanted to appear "decentralized" that is exactly what I would do.

How do we know Nvidia and AMD aren't run by one big shadow company? It's because they're clearly in competition with each other. Same goes for ASICs. Conspiracy theories have their place, but let's not get carried away. You should probably start your reading here: https://github.com/libbitcoin/libbitcoin-system/wiki/ASIC-Monopoly-Fallacy

> I prefer manufacturers like Intel, Samsung, AMD, Nvidia, ARM etc. who have many places of manufacturing, inluding USA, Vietnam, Taiwan, China, Malaysia, Thailand, South Korea, Japan and others... **whose primary business is not crypto**
> ASIC manufacturing with single purpose devices (crypto mining) is fundamentally flawed in co-dependence of decentralization.

On the contrary, at a particular market cap mining will end up being highly specialised regardless of what you do. Even if we have some sort of magical decentralised tweaking mechanism every 3 months, at a sufficiently high cap someone will just create an ARM-powered board that can run 128 GPUs without the need for a commercial motherboard and CPU. Open-source drivers for Linux already exist, so we're one or two engineering steps away from something like that. Even more efficiency gains can be had by a cabal of mining farms cutting a deal with a GPU manufacturer to buy the chips in bulk, and engineering the boards themselves.

Such engineering work could easily come from a single manufacturer who may, or may not, choose to mine on it without releasing it publicly, or mine on it before repackaging it and selling it to mining farms, etc. Therefore, at a sufficiently large marketcap, Monero has the same risks whether we resist ASICs or embrace them.

> @fluffypony Personally I feel you are underestimating the importance of ASIC resistance that the Monero community places upon the project.
> What has changed in the last 12 months?

We are getting increasingly more centralised with each fork. If you take the PoW changes out of it the forks are fine, and we could comfortably move to one a year now already, but because of the PoW changes we're locked in - and we're even making ASIC manufacturers more and more sneaky by revealing how we spot them (eg. nonce analysis).

In view of the above, it is clear that Monero's mining will face the same risks whether we reject ASICs or not. The key difference is that if we continue this path of rejecting ASICs no matter what then we most assuredly centralise development of Monero (which has legal implications for developers), and if we embrace ASICs then for a short period of time there may be a single dominant manufacturer. The former situation has no hope of improving; the latter, however, will follow the same path that Bitcoin mining has, with Bitmain's attempt at a monopoly collapsing under its own weight, whilst manufacturers like BitFury and Halong go from strength to strength.

## WhyIsThisSoSlow | 2019-03-18T12:46:42+00:00
> @fluffypony 
> 
>> That's reactive and centralised, and it has to stop.

I understand how this can be considered centralised but... Why is reactive bad? Do we not react if a bug is found that can cause harm to the network and the investments in it? How is this different from reacting to an ASIC that harms the network and the investment in it with different possible attacks? 
There is no such thing as a non reactive coin or else they would have been gone a long time ago.

> > As I understand it, RandomX can't really be tweaked much further, and - again - we're trying to get away from centralised, reactive forks.

There is no such thing as perfect and thus everything can be improved. I am sure that new ways of improving the egalitarian mining will be developed with time and if they are needed. All that matters is that we don't just give up when something is not as easy as it was before.

>> RandomX ASICs are _never going to be commoditised_, even if Monero is the world's reserve currency. SHA3 ASICs have a shot because they will be cheap to design and manufacture.

If you ask me NO MINING ASIC will ever be commoditised but with this we can give a fair chance to those that believe it will eventually be as easy to get one as it is to buy a CPU.

>> Governments can just ban mining Monero, they don't need to ban ASICs. It's not difficult to detect Monero mining traffic, and - again - it's either going to be hugely effective (people are too afraid to even use Monero, much less mine it) or entirely ineffective (see @lookfirst's [comment above](https://github.com/monero-project/meta/issues/316#issuecomment-473751846)).

Governments can do both. They can ban ASIC and they can ban Monero. It is pretty easy to keep mining and transacting via VPN and other means of hiding your trafic.

On the other hand it's not that easy to import a banned item. If this happens Drugs or ASIC will be more or less the same in the eye of the Governments.

>> No clue what this means.

It means that instead of accepting ASIC with close to equal performance, we always take measures in the fork so that we brick them entirely and thus they will know that every time they are detected the chain will fork and brick them.

This is a not so elegant way of dealing with things but it was proposed by people.  


## tarris034 | 2019-03-18T12:52:16+00:00
@WhyIsThisSoSlow 
> It means that instead of accepting ASIC with close to equal performance, we always take measures in the fork so that we brick them entirely and thus they will know that every time they are detected the chain will fork and brick them.
> 
> This is a not so elegant way of dealing with things but it was proposed by people.

I like this approach, they are hostile to us, we should be more aggressive.
Fight fire with a grenade and don't negotiate with terrorists. That's a good approach.

What if some government decided to build ASIC that's more efficient than any other ASIC manufacturer around ? We would become government coin ? another FIAT ?

ASIC manufacturers are more prone to being controlled by governments because of their specific usage, they can't ban or control Intel or Nvidia for that matter.

And I would be more afraid of control than ban.
Just remember, .1 competitor in this game is FIAT.

## fluffypony | 2019-03-18T13:00:32+00:00
> I like this approach, they are hostile to us, we should be more aggressive.
> Fight fire with a grenade and don't negotiate with the terrorists. That's a good approach.

How on earth are they terrorists and hostile? They have NO OBLIGATION to release their ASICs publicly, and all I've seen them do is be capitalists. Is the Monero community now expected to be anti-capitalist??

Consider: even after we announced that we were forking the last lot of ASICs off the network, they had over a month where they knew they were going to get kicked off. They had every reason to start attacking Monero, they could even have pulled off several 51% attacks towards the end, or just screwed with the network just like we were screwing with them. They chose not to *because miners are not the boogie man* regardless of whether they are ASIC miners or otherwise. Stop trying to paint them as terrorists, it's just ridiculous.

> What if some government decided to build ASIC that's more efficient than any other ASIC manufacturer around ? We would become government coin ? another FIAT ?

What if some government just built a server farm that is 50% of Monero's mining hashrate? It wouldn't even cost them that much.

> ASIC manufacturers are more prone to being controlled by governments because of their specific usage, they can't ban Intel or Nvidia for that matter.

Which government do you imagine is going to do this without an uproar? All of them?

## tarris034 | 2019-03-18T13:04:27+00:00
They will not kill their future investment, as I said before - mining is only a small part of the big picture in which they are creating their way to manufacture ASIC on a big scale.

What's bad about it is that it's not our decision to go ASIC PoW, but their in the end.
Not calling them terrorists directly, just used the known sentence to describe the situation.

The biggest supercomputers in the world got *only* around 9k CPU's so far like the Summit.

## zexanana | 2019-03-18T13:13:07+00:00
> There's absolutely nothing RandomX alone gives us towards the long term stability and decentralization aspects of the project other than a hopefully larger ASIC resistance window. When time comes (and it will) we'll have the same issues as now but in a much more dire position.

@antanst this is your belief, not a fact. Again, RandomX might prove to be more resilient than people are assuming here. we need to test

## tarris034 | 2019-03-18T13:15:11+00:00
> > There's absolutely nothing RandomX alone gives us towards the long term stability and decentralization aspects of the project other than a hopefully larger ASIC resistance window. When time comes (and it will) we'll have the same issues as now but in a much more dire position.
> 
> @antanst this is your belief, not a fact. Again, RandomX might prove to be more resilient than people are assuming here. we need to test

ASIC manufacturers will work on new ASIC until there's a hope Monero devs will surrender, they don't care about mining XMR, if they did - they would probably earn more by directly buying the coins than mining them with their own built hardware that took much time and money to even develop.

They would rather mine other coin that's easier and has no policy of being anti-ASIC and trade for monero if that's the case, but we all know they don't need to mine any coin at all if they wanted to invest.

## fluffypony | 2019-03-18T13:15:40+00:00
> They will not kill their future investment, as I said before - mining is only a small part of the big picture in which they are creating their way to manufacture ASIC on a big scale.

How is mining a small part of the picture? They are ASICs *specifically for mining*, so I don't get what bigger picture there is.

## tarris034 | 2019-03-18T13:17:47+00:00
> > They will not kill their future investment, as I said before - mining is only a small part of the big picture in which they are creating their way to manufacture ASIC on a big scale.
> 
> How is mining a small part of the picture? They are ASICs _specifically for mining_, so I don't get what bigger picture there is.

Already posted my opinion on this:

https://github.com/monero-project/meta/issues/316#issuecomment-473862873
https://github.com/monero-project/meta/issues/316#issuecomment-473864219


## fluffypony | 2019-03-18T13:22:10+00:00
> Already posted my opinion on this:
> 
> [#316 (comment)](https://github.com/monero-project/meta/issues/316#issuecomment-473862873)
> [#316 (comment)](https://github.com/monero-project/meta/issues/316#issuecomment-473864219)

Oh good, a conspiracy theory. The boogie man ASIC manufacturers want to control Monero, that's why they're spending money taping out ASICs😂 Please let's not derail the conversation with stuff like this, it's one step away from creating a fork of Monero because Blockstream want to control it🤦🏻‍♂️ We have ample evidence that ASIC manufacturers are profit-seekers, and no evidence that there's some grand conspiracy.

## tarris034 | 2019-03-18T13:28:46+00:00
Let me pass that sarcastaball.

We ASIC manufacturers are **wasting** money to design and produce **bricks** that good for 3 months of mining. WooHoo.

It's a good theory because I doubt they are so stupid to invest in such a volatile thing.

## tarris034 | 2019-03-18T13:29:19+00:00
> I suspect Tarris034, Monerocrusher, and WhyIsThisSoSlow are the same person. Call it a hunch.

That's a straight insult without any proofs.

## tarris034 | 2019-03-18T13:31:38+00:00
> I think its fairly obvious, but I'll let everyone else come to their own conclusions.

stop trolling, we are discussing here.

## tarris034 | 2019-03-18T13:34:09+00:00
> We have ample evidence that ASIC manufacturers are profit-seekers

I will not argue with that.

## MoneroCrusher | 2019-03-18T13:34:30+00:00
> > @fluffypony not even too long ago basically every single online store (e.g. Bitmain, Innosilicon, Baikal, Ebang etc.) looked almost the same with slightly different colors (they have slightly changed in the meantime).
> > Who says they are not all just fronts for one big shadow company in the back?
> > If I had to run an ASIC monopoly and wanted to appear "decentralized" that is exactly what I would do.
> 
> How do we know Nvidia and AMD aren't run by one big shadow company? It's because they're clearly in competition with each other. Same goes for ASICs. Conspiracy theories have their place, but let's not get carried away. You should probably start your reading here: https://github.com/libbitcoin/libbitcoin-system/wiki/ASIC-Monopoly-Fallacy

How can you compare Nvidia, AMD and Intel being run by shadow companies that operate in literally every country of the world for more than 30-40 years to a few Chinese ASIC companies popping up over the past 3-4 years **exclusively in one single country; heck even mostly in one single city**
Where do you guesstimate the chance for a shadow company being behind higher?
> 
> > I prefer manufacturers like Intel, Samsung, AMD, Nvidia, ARM etc. who have many places of manufacturing, inluding USA, Vietnam, Taiwan, China, Malaysia, Thailand, South Korea, Japan and others... **whose primary business is not crypto**
> > ASIC manufacturing with single purpose devices (crypto mining) is fundamentally flawed in co-dependence of decentralization.
> 
> On the contrary, at a particular market cap mining will end up being highly specialised regardless of what you do. Even if we have some sort of magical decentralised tweaking mechanism every 3 months, at a sufficiently high cap someone will just create an ARM-powered board that can run 128 GPUs without the need for a commercial motherboard and CPU. Open-source drivers for Linux already exist, so we're one or two engineering steps away from something like that. Even more efficiency gains can be had by a cabal of mining farms cutting a deal with a GPU manufacturer to buy the chips in bulk, and engineering the boards themselves.

I agree with the first sentence. But your fictious 128 GPU board won't change much, I already laid out how GPU compute to "periphery" ratio is already at 10:1 with readily available MBs on the market. Changing the amount of motherboards and CPUs needed doesn't influence that efficiency gain a lot.
However, the key point is that everyone can do what you laid out. With ASICs you can't, as they are monopolized and it's hard to get foothold in China and start manufacturing ASIC chips. Mysteriously your supplier will "suddendly" go out of supply and other strange things start happening.
Eventually I agree a step to ASICs makes sense.
But we are very far away from that step. IMO at least 5-10 years.
> 
> Such engineering work could easily come from a single manufacturer who may, or may not, choose to mine on it without releasing it publicly, or mine on it before repackaging it and selling it to mining farms, etc. Therefore, at a sufficiently large marketcap, Monero has the same risks whether we resist ASICs or embrace them.
> 
> > @fluffypony Personally I feel you are underestimating the importance of ASIC resistance that the Monero community places upon the project.
> > What has changed in the last 12 months?
> 
> We are getting increasingly more centralised with each fork. If you take the PoW changes out of it the forks are fine, and we could comfortably move to one a year now already, but because of the PoW changes we're locked in - and we're even making ASIC manufacturers more and more sneaky by revealing how we spot them (eg. nonce analysis).

The PoW can be publicly reviewed and if the miner community disagrees with it they can choose to not mine on the new chain.
> 
> In view of the above, it is clear that Monero's mining will face the same risks whether we reject ASICs or not. The key difference is that if we continue this path of rejecting ASICs no matter what then we most assuredly centralise development of Monero (which has legal implications for developers), and if we embrace ASICs then for a short period of time there may be a single dominant manufacturer. The former situation has no hope of improving; the latter, however, will follow the same path that Bitcoin mining has, with Bitmain's attempt at a monopoly collapsing under its own weight, whilst manufacturers like BitFury and Halong go from strength to strength.

As I said many times, I am for ASICs once we are sure they are produced, marketed and sold in a fashion that keeps up with AMD/Nvidia/Intel fashion and once 99% of the initial supply is mined (at the earliest).
But that's far away in the future. I think we should keep focusing on egalitarian & decentralized mining in the meantime.

## WhyIsThisSoSlow | 2019-03-18T13:37:20+00:00
ASIC makers are not the boogeyman. They are just companies that have the means to exploit the hash advantage vulnerability. They do not care about the coin, they only care about profits.
They mine it until its not proffitable anymore and then dump the unprofitable ASIC to the market to make even more profit from naive people that think the cat and mouse game will ever change by itself. 


Like any other vulnerability we need to treat it as is and patch it everytime it affects the network and/or the core concept of the coin.

Until they are equal to normal miners or mass produced and as available as a CPU i shal always see them as an exploit of the code. 

## MoneroCrusher | 2019-03-18T13:39:13+00:00
Highly agree with treating ASICs on the net like a software bug.
Decentralization  and egalitarianism are features of Monero, if that feature is threatened then treat the threat as you would treat a critical software bug.
Same thing IMO.

## tarris034 | 2019-03-18T13:42:23+00:00
Treat it as DDoS attack on profitability, because that was the effect in the end of them mining.
I'm not against capitalism(quite contrary) but it's against fair market and even in capitalism there are rules against monopolies.

## tarris034 | 2019-03-18T13:45:44+00:00
> [willfull ignorance that the devs won't maintain a four-month fork schedule intensifies]
> 
> Seriously, your motives are very clear. The devs have already said they won't fork more than once every six months, and probably every year is the viable thing at the moment. You will unfortunately have to split off an altcoin if you want to be that bleeding edge. Sorry, but that's the reality of the situation, no amount of sock puppet accounts will change that my dude.

+1 your own comments and talking about me having different accounts... I will leave this for other to judge.

We are all against changing PoW that much often, if you read the whole conversation you would know.

## fluffypony | 2019-03-18T13:47:06+00:00
So ASICs are a DDoS attack on profitability, even at only 2x profitability, but it's totally fine if miners gain an edge through bulk purchasing, low-price electricity, or more efficient software? Sorry but it goes both ways. By this logic I'm going to start treating CPU / GPU miners as a cancer that is forcing the devs to make unnecessary, dangerous, and centralised forks. Hashtag cut out the cancer.

## tarris034 | 2019-03-18T13:48:53+00:00
If it was so simple I would agree with you.

also please ban this a$$, i'm not continuing conversation with kids around.

## MoneroCrusher | 2019-03-18T13:50:55+00:00
@Sockpuppet2
lmao I literally said like 10 posts above that the ideal scenario would be to fork once a year.
If you're too lazy to look it up here you go:

> So in my opinion the ideal practice would be to have an algorithm like Ethash (memory hard), which has proven to be excellent at keeping ASICs to a minimum (efficiency-gain-wise speaking only 2x-3x) and keep forking it in unpredictable ways at a less regular schedule like maybe once a year to discourage ASICs economically. I would then do this as long as 99% of the emission isn’t mined and then switch to a very simple and easily ASIC-able algorithm (like SHA3) and let them slowly take over for the remaining transactional market. This practice would allow for the broadest and fairest distribution of 99% of the emission.

The alternative would be to do not a 4 month fork schedule but a **pseudo** 4 month fork schedule, as I have explained [here](https://github.com/monero-project/meta/issues/316#issuecomment-472677985).
@dEBRUYNE-1 reminder for debruine again to add it please, 5 days have passed.

## JustFranz | 2019-03-18T13:54:23+00:00
Everyone, turn down the conspiracy crap and all other kinds of crap too. We need an evidence based, rational approach for this.

1.  Do we gain anything by having RandomX as a stopgap and waiting a year? 2 years? 3? 4?
2. What are we waiting for?
3. If we don't gain anything then what do we do this October fork?




## MoneroCrusher | 2019-03-18T13:55:50+00:00
If Monero would commit to it for all eternity they wouldn't even tape out ASICs for the first batch.
Determination is the key.
This insecurity we have right now is exactly where the ASIC manufacturers want us, in order to push Monero to ASICs faster in order to be able to scam & milk the community at large with their shitty tactics and behaviour.

## MoneroCrusher | 2019-03-18T13:58:24+00:00
also, I have no clue who @tarris034 and @WhyIsThisSoSlow are and have no association with them.

Hard to imagine that community members value decentralization, huh?

## WhyIsThisSoSlow | 2019-03-18T14:03:41+00:00
I do not see the point of this topic anymore if we start mocking each other.

If this is a pathetic attempt to discourage ideas from any of the parties involved i highly encourage everyone to ignore the spam.




## justinjja | 2019-03-18T14:04:19+00:00
Don't worry about Sockpuppet2, his name is sock puppet, and his account is 35 mins old. lol

Why do we think an easy algo (sha3) will result in closer hashrates between asic manufactures?
The top SHA3 FPGA miner does 17GH/s and the next closest competitor is 12GH/s
Thats a pretty big difference for the exact same hardware.

Better and bigger manufactures will all kinds of tricks up their selves. 

## fluffypony | 2019-03-18T14:04:39+00:00
> If Monero would commit to it for all eternity they wouldn't even tape out ASICs for the first batch.
> Determination is the key.
> This insecurity we have right now is exactly where the ASIC manufacturers want us, in order to push Monero to ASICs faster in order to be able to scam & milk the community at large with their shitty tactics and behaviour.

Sorry, but no. We have direct evidence to the contrary. Per [the blog post that was put up by the community in February, 2018](https://getmonero.org/2018/02/11/PoW-change-and-key-reuse.html) - "we will perform an emergency hard fork to curb any potential threat from ASICs if needed". We demonstrated our resolve by immediately tweaking to knock existing ASICs off the network, and then tweaking it again in October, 2018, even though we didn't need to (as there were no ASICs).

And yet despite that threat, our public resolve, and the evidence that we're willing to follow through, someone managed to design, tape out, and deploy an ASIC on to the network after the October hard fork. @JustFranz has asked for evidence-based discussion, not unsubstantiated claims and random conspiracy theories.

## fluffypony | 2019-03-18T14:07:11+00:00
> Don't worry about Sockpuppet2, his name is sock puppet, and his account is 35 mins old. lol
> 
> Why do we think an easy algo (sha3) will result in closer hashrates between asic manufactures?
> The top SHA3 FPGA miner does 17GH/s and the next closest competitor is 12GH/s
> Thats a pretty big difference for the exact same hardware.
> 
> Better and bigger manufactures will all kinds of tricks up their selves.

I think the gap starts to close the closer they get to 7nm. Right now the monumental jumps in Bitcoin ASIC efficiency have largely been attributed to manufacturing improvements, rather than massive changes in actual circuit design. I'd expect that, if we give them 2 years, ASIC manufacturers will go straight to 7nm or thereabouts, and spend the money on larger tapeouts to take advantage of economies of scale. In other words, it will lead to less of an arms race.

## MoneroCrusher | 2019-03-18T14:09:16+00:00
@fluffypony The response to that is so obvious that I must ask, have you even read my post that explains on how it would actually achieve its goal? I feel like I'm circling with my arguments and opponents to my idea don't understand or don't read my posts.

I very logically explained in every step how this would work and why it would work. And it's a different strategy to the statement on the blog post you posted.

If you want to disprove me, show me some empirical data or logical arguments showing or explaining how this approach wouldn't work.

## tarris034 | 2019-03-18T14:11:02+00:00
https://getmonero.org/2018/02/11/PoW-change-and-key-reuse.html

The risks of going ASIC mentioned in this post still hold true.

## WhyIsThisSoSlow | 2019-03-18T14:13:04+00:00
CPU and ASIC will both improve in technology and the manufacturing process. This is a given of evolution.

The question is do we want our network to be decentralized and mined by CPU`s that are currently a commodity or do we want it ASIC centralized and at the mercy of a hand full of entities from 1 country that do not plan the product to be sold before its almost obsolete ?


## MoneroCrusher | 2019-03-18T14:13:06+00:00
As I reiterated several times it's a different thing if you have the finger on the button from the first day an ASIC sees the light of the day.

## pigfrown | 2019-03-18T14:15:19+00:00
> As I reiterated several times it's a different thing if you have the finger on the button from the first day an ASIC sees the light of the day.

You still need to reliably detect ASICs. Seems like there is a lot of scope for manufacturers to be sneaky here... you are giving them a big incentive to be sneaky as well... don't get caught and the PoW won't fork.

## fluffypony | 2019-03-18T14:15:39+00:00
@MoneroCrusher sounds very, very centralised, and puts the devs at regulatory risk. If Monero ever becomes like that I want nothing to do with it.

## tarris034 | 2019-03-18T14:18:41+00:00
> > As I reiterated several times it's a different thing if you have the finger on the button from the first day an ASIC sees the light of the day.
> 
> You still need to reliably detect ASICs. Seems like there is a lot of scope for manufacturers to be sneaky here... you are giving them a big incentive to be sneaky as well... don't get caught and the PoW won't fork.

We are suppose to stick with the facts, so far they haven't manage to hide it.

## justinjja | 2019-03-18T14:19:24+00:00
How would you know?
Maybe they had asics on cnv1 and we just didn't see them.

## fluffypony | 2019-03-18T14:19:46+00:00
@tarris034 100%, but so far they haven’t been incentivised to do so.

## MoneroCrusher | 2019-03-18T14:19:49+00:00
@pigfrown I absolutely expect them to become sneakier. However, they can try to be as sneaky as they want, they will never be able to perfectly hide their nonces and sudden decrease in mining profit on commodity hardware.
If they want to mine they can choose to mine on commodity hardware as well.

## tarris034 | 2019-03-18T14:19:57+00:00
> How would you know?
> Maybe they had asics on cnv7 and we just didn't see them.

if they had a design that can hide it, why they didn't use it last time ?

## justinjja | 2019-03-18T14:20:17+00:00
Who is to say it was the same person

## MoneroCrusher | 2019-03-18T14:24:46+00:00
> @MoneroCrusher sounds very, very centralised, and puts the devs at regulatory risk. If Monero ever becomes like that I want nothing to do with it.

By your definition of centralization every code contribution ever made to Monero is centralized.

I'm actually OK with PoW algo production being centralized (and obviously you were OK with it too for the past 12 months).
There's a big difference. Miners and community can review the code and either accept it or reject it. What's centralized about it?



## tarris034 | 2019-03-18T14:29:44+00:00
Probably because not many people can actually understand the PoW code at enough level to find a secret door that could be hidden mathematically or programmatically in the code.

That makes it centralized in some sort of way but I'm judging the situation from my point of view (noobs view) and don't know how many people in the community are actually understanding the code.

## MoneroCrusher | 2019-03-18T14:31:41+00:00
The only place a cryptocurrency can become centralized is in mining and validating nodes.

Open source code:
1. Submitted by centralized person or group
2. Reviewed by others

There's a flaw in your definition of centralization. If you show me how someone as a single person or group can be decentralized, let me know.
So all Open source code ever made is "centralized" in the very nature that 1 contributor = 1 brain and 1 brain = centralized.

## AirSquirrels | 2019-03-18T14:34:47+00:00
It would be very very easy to manage the nonce visibility issue. Watching profitability vs GPU or CPU is also a few levels removed from proof of ASICs.

@fluffypony is very right - any kind of non-automated ASIC kill switch is highly centralized and non-deterministic.

I’m leaning towards either maintaining a community committed fork schedule with PoW changes or just freezing the PoW. 

However even a committed fork schedule with no reaction button still needs a centralized team of devs (who could be doing more productive things) to imagine new even more convoluted PoW algorithms - one of which at some point is bound to introduce a small or large vulnerability. These are not light issues.

I also disagree that CPUs are somehow completely ASIC proof. Any fixed algorithm, even a random reduced instruction set one such as RandomX, could at some point have at least some efficiency gains developed for it. I also don’t know how good modern CPU wafer yields are, but I could imagine the cost of building a CPU for crypto with various non-fatal flaws could be cheaper than a mainstream processor at some scale.

Right now are the majority of miners GPU or CPU? If the majority of miners are GPU, and RandomX kills GPUs anyway, then why not just go straight to ASIC? Most of the arguments tend to be about miners protecting their current investment.

I agree also with @fluffypony that as we slam up against the 7nm process node wall, especially on a mature and studied algorithm like SHA3, we likely have the most level launching playing field for ASICs that has historically existed. A major coin line XMR switching to support ASICs on a given hard date wouldn’t represent nearly the risk that historical would be ASIC manufacturers faced. It is very likely several competing groups would be able to raise or source large scale investment because the opportunity is so big and clear. 





## MoneroCrusher | 2019-03-18T14:39:29+00:00
> It would be very very easy to manage the nonce visibility issue. Watching profitability vs GPU or CPU is also a few levels removed from proof of ASICs.

Tell me how?

ASICs could be detected 3 times. Why wasn't it done? I argue that it's impossible to perfectly hide ASICs by trying to make it as undetectable as possible. They can't predict all factors and in what fashion GPU & CPU miners leave the network. This opens the gap wide up for any detection tools.

## WhyIsThisSoSlow | 2019-03-18T14:40:03+00:00
To clear things up, i have no incentive to be PRO any kind of hardware that is used on mining. I have money invested in Monero like everyone here and am obviously invested in keeping this project as free,decentralized and private as humanly possible. Thus the idea of ASIC is a total no go until it fits that criteria. 

These current limitations of everything ASIC are not compatible with the Monero ideology so we need to stop poking at it until it fits those needs.

## tarris034 | 2019-03-18T14:41:09+00:00
>Right now are the majority of miners GPU or CPU? If the majority of miners are GPU, and RandomX kills GPUs anyway, then why not just go straight to ASIC? Most of the arguments tend to be about miners protecting their current investment.

Even GPU rigs (with usually x7 GPU) all got at least 1 CPU that will be more efficient on RandomX than this GPU's combined. Granted, they usually have some cheap CPU but can upgrade with no problem.

If we stop thinking for a moment about ASIC, CPU mining is the best option as it's available in every house and every company, bringing the decentralization further.

## MoneroCrusher | 2019-03-18T14:44:51+00:00
@tarris034 no it won't. virtually all GPU rigs have a 2 core Celeron or Pentium. All GPUs rigs would instantly become useless.

Even 8x Vega rigs use a celeron as it perfectly works for mining CN.

## tarris034 | 2019-03-18T14:45:31+00:00
> @MoneroCrusher  no it won't. virtually all GPU rigs have a 2 core Celeron or Pentium. All GPUs rigs would instantly become useless.
> 
> Even 8x Vega rigs use a celeron as it perfectly works for mining CN.

Yes, sorry I have corrected my self. They are not useless, just sell GPU's and buy CPU's, you will still have enough to buy more rigs.

Still better option than going fully ASIC.

## MoneroCrusher | 2019-03-18T14:47:58+00:00
@tarris034 that's one possibility. Why not dual PoW if it can be achieved safely? Would grant more mining hardware diversity: CPUs, GPUs, FPGAs, allow all commodity HW

## tarris034 | 2019-03-18T14:48:52+00:00
> @tarris034 that's one possibility. Why not dual PoW if it can be achieved safely? Would grant more mining hardware diversity: CPUs, GPUs, FPGAs, allow all commodity HW

I have expressed my self on dual pow earlier, in short: the simpler, the better. Dual PoW is far from simplicity.

## MoneroCrusher | 2019-03-18T14:49:36+00:00
Grin has done it. So have others.

## tarris034 | 2019-03-18T14:50:05+00:00
Most of people smoke cigarettes, is it good ?
Analogically speaking, it's better to have one solid door, than two doors or for that matter, a wall full of doors.

## MoneroCrusher | 2019-03-18T15:02:33+00:00
lol
Cigarettes are proven to be unhealthy.
Dual PoW could work just fine.

To anyone arguing simple is better, tell me why your DNA is backed up trillions of time in your body and why does every DNA strand have a dualistic architecture? In case of failure it can be rebuilt.
![image](https://user-images.githubusercontent.com/32360383/54539479-7fd37f80-4996-11e9-810e-47d55d024510.png)
~~Many~~ All systems in nature are dualistic.


Same can be said about a dual PoW. If one algo fails, the other is here to safe the day.

This is the argument against "simple is better", yes simple is more elegant and "beautiful", but in case it fails it has catastrophic consequences.
Obviously nature chose being resilient than being simple is the safer choice.

In terms of Monero it will also keep the community together and thus makes Monero stronger. In case of a pwnage, the pwned algo can be disabled with a HF and can be fixed in the time where it's deactivated.

## tarris034 | 2019-03-18T15:04:22+00:00
I wouldn't compare DNA to PoW situation, crypto is far from millions years of evolution.

## MoneroCrusher | 2019-03-18T15:06:00+00:00
@tarris034 Cryptocurrency, cryptography, communication and maths are also a form of evolution of the past hundreds of thousands of years.

## tarris034 | 2019-03-18T15:09:03+00:00
I will leave dual pow discussion to more experienced community members.

## MoneroCrusher | 2019-03-18T15:10:42+00:00
So to make a counter analogy:
Every single Monero node on the planet is a "cell", like the 10 trillion cells in your body that have a backup of your DNA.
And in it's very core foundation, which is the process of mining and validating in cryptocurrency, have a system that is dualistic and more resilient to failure. This is the dual strand in case of the DNA.

Safe > "Beautiful"/simple

IMO a dual PoW is actually more "beautiful". That's of course in the eye of the beholder.

## MoneroCrusher | 2019-03-18T15:16:00+00:00
@Sockpuppet2 For clarification: I did not mine Monero 2 weeks leading up to the hardfork. I left in Januay when ASICs came online. I can tell you CPU miners did the same.
I don't see the problem.

## justinjja | 2019-03-18T15:21:15+00:00
Lots of technical people start with crypo as miners.
Doesn't mean he is only here for mining profit now.

## tarris034 | 2019-03-18T15:23:01+00:00
Why would community split if they can just adjust with no big problem ? they already got rigs capable of mining RandomX efficiently with little upgrade.

Wasn't monero at first minable only by CPU ? if so, back to the roots.

## MoneroCrusher | 2019-03-18T15:23:55+00:00
@Sockpuppet2 How are CPU miners not here for themselves? I say having GPUs, CPU and FPGA miners is even better for the network.

As a miner: Yes I'm here for profit.
As a Monero enthusiast: I also would love to see Monero having a big and bright future.

Sorry to break it to you, the mining game is figuratively speaking 99% consisting of profit-oriented miners. Cryptocurrency is designed that way. Nothing bad about it.

## tarris034 | 2019-03-18T15:25:20+00:00
Profit is incentive to mining, it must be profitable otherwise no one would mine it.

## JustFranz | 2019-03-18T15:25:54+00:00
This is getting unbearably hard to read. Every time I open the thread I must click to load new messages 10 times and every time I must scroll down to find the load messages button again.

We have a week left until the meeting, how can we ensure that the following discussions are as constructive as possible and do not get lost? Should a new issue be opened? Or is the conversation unrecoverable? 

## justinjja | 2019-03-18T15:26:40+00:00
I think a big coin with a cpu-only pow would be super interesting.
Even though right now I have everything except CPU's mining (GPU, FPGA and ASIC)

## tarris034 | 2019-03-18T15:29:39+00:00
There would be no network without miners, but it was always the miner that had to adjust for the network and that shouldn't change.

## MoneroCrusher | 2019-03-18T15:29:44+00:00
@Sockpuppet2 I can tell you in my case I also bought a lot of RX 550/560 with 2 GB memory with the sole intention in mind of mining Monero. So that's a commitment, right?

## tarris034 | 2019-03-18T15:30:36+00:00
I would call it gambling, like with any other investment.

## MoneroCrusher | 2019-03-18T15:31:36+00:00
Anyways, if dual PoW can be achieved it should be done.
The network will be bigger, more diverse & much stronger and resilient to failure. Not the other way around. But it has to be developed and I don't know if the devs want to.

## tarris034 | 2019-03-18T15:32:55+00:00
> Anyways, if dual PoW can be achieved it should be done.
> The network will be bigger, more diverse & much stronger and resilient to failure. Not the other way around. But it has to be developed and I don't know if the devs want to.

Who wouldn't want more diversified network, and more hardware compatibility.
The problem here is that GPU PoW has proven less secure than CPU PoW.

(by less secure I mean't prone to FPGA/ASIC)

## MoneroCrusher | 2019-03-18T15:33:07+00:00
sure, you just asked me if I made any commitment to Monero. There, I provided you with one.

## MoneroCrusher | 2019-03-18T15:34:12+00:00
@tarris034 There was never a GPU PoW used in Monero. If that's not true please let me know when that was the case.
Ethash is a GPU PoW and only has 2x ASICs. Same as RandomX ASICs likely would have.

So in a dual PoW you have RandomX for CPUs (2x speedup possible) and CN-R-Memory-hard for GPUs (2x speedup possible).
This way you have 2 equally secure algos, but as I argued above, dualism provides better security and resiliency to failues.

## tarris034 | 2019-03-18T15:35:37+00:00
> @MoneroCrusher  There was never a GPU PoW used in Monero. If that's not true please let me know when that was the case.

I was thinking about other crypto coins.

> Ethash is a GPU PoW and only has 2x ASICs. Same as RandomX ASICs **likely would have**.

It's all theory right now.

Also keep in mind your 2GB cards would be bricks anyway on similar to Ethash GPU PoW as it has 3 gigabytes of VRAM min. requirement.

## WhyIsThisSoSlow | 2019-03-18T15:36:36+00:00
Can we all focus on the network for a change and leave profits aside? Lets continue and improve RandomX and make this network as decentralized as possible. We can discuss if dual PoW is good in another thread if necessary. As i see the majority here agree that RandomX is the way to go even if that means GPU`s will have a lower hash rate. We keep going in circles with short burst of comments that provide nothing to the future of the coin.

## tarris034 | 2019-03-18T15:40:34+00:00
> @WhyIsThisSoSlow if you're pro RandomX, we're on the same page. GPU miners will unfortunately get shafted to a significant degree.

We are not against GPU miners, it's how nature dictated it's current state. I wouldn't mind if this was vice-versa situation.

## MoneroCrusher | 2019-03-18T15:46:56+00:00
As I have said in lots of previous posts:
Objectively speaking (ignoring my investment) CPU mining provides less advantage to dedicated hobby miners:.
It's:
- susceptible to botnets
- easier for state actors to carry out attacks

I like CPU mining though and almost wanted to do an EPYC/Threadripper/Ryzen farm when I planned on doing my Monero farm but didn't go through with it because the cost advantage is reduced drastically with CPUs. Everything becomes really expensive. Big datacenters and botnets have a huge advantage there.

On the other hand, with GPU mining the hobbysists have the big advantage against virtually anyone else.

It doesn't mean I want to see only one of the things being implemented.
Dual PoW is the way to go (additionally coupled with a game theoretical approach, or in the biology analogy: programmed cell death)

## zexanana | 2019-03-18T15:47:51+00:00
As people have said, investments have risk. GPU miners can still try to sell their GPUs once RandomX kick in. It's not like they're ASICs...

## tarris034 | 2019-03-18T15:49:46+00:00
Even ASIC ain't free from botnets as shown with the recent virus that infected them.

## MoneroCrusher | 2019-03-18T15:50:37+00:00
@tarris034 my GPUs have never touched the open internet (implying dedicated miners protect their investment)
CPUs will always be number one for botnets.

## tarris034 | 2019-03-18T15:52:02+00:00
> @tarris034 my GPUs have never touched the open internet (implying dedicated miners protect their investment)
> CPUs will always be number one for botnets.

But they are not a threat. (would require REALLY big network to be a threat)
And big networks like this are getting busted pretty quickly.

## justinjja | 2019-03-18T15:53:38+00:00
If CPU/GPU/Both doesn't matter, why did we make RandomX vs just tweaking ethash or progpow and using that?
Does it achieve something that those don't?

## tarris034 | 2019-03-18T15:54:31+00:00
> If CPU/GPU/Both doesn't matter, why did we make RandomX vs just tweaking ethash or progpow and using that?

they are being far from perfect as well ? because we are not another s-coin that copy/paste ?
this is not sarcasm, i'm really asking.

## hyc | 2019-03-18T15:55:05+00:00
@justinjja We started designing RandomJS before ProgPow existed. In fact I consulted with them on ProgPow's design after I had published my notes on randprog.

## MoneroCrusher | 2019-03-18T15:55:16+00:00
@tarris034 CPU hashrate and power consumption of the network will be much smaller because it's much more expensive to run a CPU farm.
therefore easier to attack for botnets and state actors

Maybe we should open up a discussion for dual PoW exploration.

## tarris034 | 2019-03-18T15:57:12+00:00
> @tarris034 CPU hashrate and power consumption of the network will be much smaller because it's much more expensive to run a CPU farm.
> therefore easier to attack for botnets and state actors
> 
> Maybe we should open up a discussion for dual PoW exploration.

There's plenty of companies that would utilize their idle cpu cycles, I think we shouldn't worry about insufficient hashrate to secure the network against bad actors.

## zexanana | 2019-03-18T15:59:50+00:00
@MoneroCrusher  I think you are the only one advocating for dual PoW.

## MoneroCrusher | 2019-03-18T16:01:09+00:00
@tarris034 Nothing stops those companies from doing that now. Also nothing stops them from doing that in a dual PoW. As I said: The more diversity and participants, the more secure the chain.

## tarris034 | 2019-03-18T16:02:25+00:00
> @tarris034 Nothing stops those companies from doing that now. Also nothing stops them from doing that in a dual PoW.

As of now CPU mining is cramped by the GPU mining farms as we discussed earlier.


## justinjja | 2019-03-18T16:02:46+00:00
@zexanana I would much rather see a dual PoW.

I hear some people here saying it can't be done securely.
Then I also see a handful of coins already doing it.

I wouldn't know which is right...

## MoneroCrusher | 2019-03-18T16:06:47+00:00
CPU owners have all the incentive to fight a dual PoW because as it stands now, RadomX-pure would enrich them much more. So why all the negativity towards GPU miners? Maybe also ask the motives of people pushing for RandomX. Do they maybe own companies with lots of servers?

Dual PoW is a fair solution to all and keeps community peace.

RandomX for CPUS
CN-R-Memory-hard for GPUs (alternatively could also use "ethash-CN variant")

## fluffypony | 2019-03-18T16:08:02+00:00
@justinjja there are also a bunch of coins doing PoS, Masternodes, and idiotic scaling techniques like gigabyte blocks. Just because something is being done and they’ve thus-far survived doesn’t mean it’s safe. Every competent piece of investigation into it has established it cannot be done safely enough, and besides, it’s complexity that invites edge-case risk.

## zexanana | 2019-03-18T16:08:41+00:00
What do you mean CPU owners? Server farms? I am a CPU owner, and a 2x GPU owner. It seems everything is being considered a conspiracy. The discussion seems a bit far from a rational analysis right now.

## tarris034 | 2019-03-18T16:09:27+00:00
@zexanana 
a little dose of paranoia is healthy.

## MoneroCrusher | 2019-03-18T16:10:08+00:00
your arguments don't show how a dual PoW would be worse, on the opposite I think it provides more resiliency to complete failure of the chain (meaning complete pwnage by a single entity)

Everyone likes to keep pointing that Zcash failed to do it. Since when do you consider a centralized coin that is led by the Zcash Company a source of truth and authority?
I'd suggest Monero looking into it by themselves.

## tarris034 | 2019-03-18T16:17:25+00:00
@MoneroCrusher read more about dual pow, especially about the time locking of mined coins. cure worse than the disease. it's not as simple and easy as it may seem. (I'm still reading into it and like it less with every minute)

## justinjja | 2019-03-18T16:20:08+00:00
"Every competent piece of investigation into it has established it cannot be done safely enough"
Where are these investigations?

Locking coins isn't needed is it? that is just Zcash being centralized AFAIK

@SChernykh Didn't seem convinced Dual PoW was a lost cause, last I saw...

## MoneroCrusher | 2019-03-18T16:22:24+00:00
@fluffypony So how come Grin implemented dual PoW? I don't think they're incompetent idiots.

## tarris034 | 2019-03-18T16:33:03+00:00
@MoneroCrusher GPU PoW can be easier optimized for FPGA if i'm not wrong, what's then ? Triple PoW ? seems it's another dead end.

## MoneroCrusher | 2019-03-18T16:34:25+00:00
FPGAs have 5 kh/s on CNV2. A Vega does 2kh/s while being 10x cheaper. I couldnt care less about FPGAs as a miner. Also they are commoditized and readily available

## tarris034 | 2019-03-18T16:35:19+00:00
> FPGAs have 5 kh/s on CNV2. A Vega does 2kh/s while being 10x cheaper. I couldnt care less about FPGAs as a miner.

Well, the difference is not far from **top** CPU's so why not mine RandomX on GPU ? There's probably some room for optimizations in the long run (hope not, it would make it weaker at the same time for it's meant purpose)

Also it would be easier if GPU farms just adjust to the network, why we should all get at risk with dual pow ? only so investment gamblers had the chance for a better ROI ?

## MoneroCrusher | 2019-03-18T16:43:08+00:00
No, I laid out my reasoning above as you are surely aware

## tarris034 | 2019-03-18T16:43:45+00:00
> I couldnt care less about FPGAs as a miner

Then this sentence does not make sense.

## MoneroCrusher | 2019-03-18T16:44:33+00:00
lol this is some really advanced sockpoppet self-talk, don't you think @Sockpuppet2 😃 

## vtnerd | 2019-03-18T17:15:41+00:00
Multiple PoW schemes splits the hashrate of "honest" miners. Even if one algorithm targeted CPU and another GPU, anyone looking to buy equipment to protect the network ends up deciding on an algorithm to target. An attacker gets to decide which PoW algorithm is cheapest to go after. I could look at some other chains dual PoW approach, but I'm very skeptical.

## justinjja | 2019-03-18T17:39:12+00:00
To 51% the network, you would need to have 51% of both POW chains.
At least that is the only way Dual PoW makes any sense to me.

## tarris034 | 2019-03-18T17:45:36+00:00
Rotational PoW would be a little better remedy maybe than dual PoW but I'm against such complexities.

## justinjja | 2019-03-18T17:47:11+00:00
Zcash didn't like alternating dual pow, because they were worried about hardware that could target both POW's.

But Zcash was talking about doing 2 equihash varriants, I think that would be much harder with RandomX and a gpu optimized cryptonight algo.

## vtnerd | 2019-03-18T18:00:32+00:00
> To 51% the network, you would need to have 51% of both POW chains.

This would imply that a miner needs to find a solution to all PoW algorithms before submitting a new block. Grin is trying to control outcomes with different mining rewards for each algorithm that shifts over time.

> But Zcash was talking about doing 2 equihash varriants, I think that would be much harder with RandomX and a gpu optimized cryptonight algo.

The choice of algorithms is irrelevant for my criticism - it applies to any selection of algorithms.

## tarris034 | 2019-03-18T18:00:55+00:00
How about dual blockchain and some balancer/splitter between that would keep 50% balance of hashrate between them to defend from 51% attack ?

Does it make any sense ?

## vtnerd | 2019-03-18T18:02:05+00:00
> How about dual blockchain and some balancer/splitter between that would keep 50% balance of hashrate between them ?
>
> Does it make any sense ?

That sounds like the verge disaster, although there is probably a way to less terrible than they did.

## tarris034 | 2019-03-18T18:02:37+00:00
> > How about dual blockchain and some balancer/splitter between that would keep 50% balance of hashrate between them ?
> > Does it make any sense ?
> 
> That sounds like the verge disaster, although there is probably a way to less terrible than they did.

I'm not aware of their situation as I was focusing only on Monero.

## vtnerd | 2019-03-18T18:04:12+00:00
> I'm not aware of their situation as I was focusing only on Monero.

Read about it before saying anything further about this sub-sub-topic. This type of system will add additional knobs for attackers to turn.

## tarris034 | 2019-03-18T18:09:12+00:00
You're talking about dual mining verge with Eth ? if so, that's not entirely what I had in mind with dual blockchain.

I was thinking to have x2 XMR blockchains, the splitter/balancer would do 50%/50% hashrate split so 51% attack is impossible.

## justinjja | 2019-03-18T18:10:42+00:00
I'm not following @vtnerd 

Say you want to do a 51% attack,
You sell a bunch of Monero to an exchange, withdraw the Bitcoin, then do your 51% attack to revert the transaction.

But if the algo alternates between CPU and GPU, and you only have GPUs (or an ASIC that does the GPU algo), then you could only revert 1 block. 

## pallas1 | 2019-03-18T18:14:06+00:00
And the miners would mine for nothing half of the time? Or just stay idle? Doesn't seem like a good solution...

## tarris034 | 2019-03-18T18:14:27+00:00
> And the miners would mine for nothing half of the time? Or just stay idle? Doesn't seem like a good solution...

no. it would be transparent to them. their hashrate would go either to solve block from .1 or .2 blockchain.

## pallas1 | 2019-03-18T18:16:53+00:00
If I'm on the CPU algorithm, I can not solve a GPU block. I cannot either solve a future block....

## tarris034 | 2019-03-18T18:17:15+00:00
> If I'm on the CPU algorithm, I can not solve a GPU block. I cannot either solve a future block....

I'm talking single PoW, dual blockchain.

## justinjja | 2019-03-18T18:17:42+00:00
So you cut your power usage in half, or you mine another coin, either is a benefit to a miner,
And would encourage more people to mine monero.

## tarris034 | 2019-03-18T18:18:26+00:00
> So you cut your power usage in half, or you mine another coin, either is a benefit to a miner,
> And would encourage more people to mine monero.

no cutting in half for miners, that's not my idea of how it would work.

No matter how much power you would throw at it, it would still equal to 50/50.

## timolson | 2019-03-18T18:20:59+00:00
> Even with SHA3 ASICs you will have one dominating manufacturer. Efficiency is not only about algorithm, it's also about supply chain optimizations and economies of scale. Right now it will be Bitmain. The ASIC market is just not mature enough yet.

WhatsMiner is beating Bitmain in performance, and there are lots more manufacturers now than just one year ago.  The ”Bitmain monopoly” argument is not true anymore.

## tarris034 | 2019-03-18T18:21:45+00:00
> > Even with SHA3 ASICs you will have one dominating manufacturer. Efficiency is not only about algorithm, it's also about supply chain optimizations and economies of scale. Right now it will be Bitmain. The ASIC market is just not mature enough yet.
> 
> WhatsMiner is beating Bitmain in performance, and there are lots more manufacturers now than just one year ago. The ”Bitmain monopoly” argument is not true anymore.

But there's still country of origin "monopoly" if i'm right ?

## justinjja | 2019-03-18T18:28:36+00:00
Whatsminer = 33TH/s and uses 2150W = 65W/th
S15 = 28TH/s and uses 1600W = 57W/th
bitmain looks better?

Am I looking at the wrong miners @timolson 

## dEBRUYNE-1 | 2019-03-18T18:28:52+00:00
@tarris034 

Not all ASIC manufacturers are located in China nowadays. As I said before, the situation has improved a lot in comparison to a few years ago. 

## tarris034 | 2019-03-18T18:38:10+00:00
btw, forget what i was saying about dual blockchain and splitting, it does not make sense because that 50% of bad actor hashrate on one of the blockchains could still be bigger than 51% of good hashrate.

## justinjja | 2019-03-18T18:39:07+00:00
Alternating it is :D

## tarris034 | 2019-03-18T18:39:28+00:00
> Whatsminer = 33TH/s and uses 2150W = 65W/th
> S15 = 28TH/s and uses 1600W = 57W/th
> bitmain looks better?
> 
> Am I looking at the wrong miners @timolson

This hardware changes so quickly there's almost no point of comparing them.

## justinjja | 2019-03-18T18:40:42+00:00
I guess? the S9 was around for like 2 years though.

## tarris034 | 2019-03-18T18:45:00+00:00
The big trio Intel/AMD/Nvidia are all from California.. so i think i don't mind having one country of origin for ASIC. IBM from New York :dancer: 

## WhyIsThisSoSlow | 2019-03-18T18:52:51+00:00
I truly think that hinting to an ASIC PoW change at this point is like beating a dead horse. I truly belie most of the Monero community will be anti-ASIC until ASIC will become as available as a CPU.

## tarris034 | 2019-03-18T21:19:49+00:00
> I truly think that hinting to an ASIC PoW change at this point is like beating a dead horse. I truly belie most of the Monero community will be anti-ASIC until ASIC will become as available as a CPU.

I don't like the ASIC PoW idea but it's a circle - there won't be ASIC for Monero available because we brick them and have the policy to do so again and again. 

We are at war with ASIC manufacturers, we can either surrender or keep fighting.
Having in mind what's best for the community and network.


## antanst | 2019-03-18T21:54:18+00:00
> I truly think that hinting to an ASIC PoW change at this point is like beating a dead horse. I truly belie most of the Monero community will be anti-ASIC until ASIC will become as available as a CPU.

I guess you can do that, if you define "most of the community" the vocal 3-4 people that have been posting here the last few days, and you ignore everything that many developers have been saying so far in this chat.

## tarris034 | 2019-03-18T22:05:26+00:00
> > I truly think that hinting to an ASIC PoW change at this point is like beating a dead horse. I truly belie most of the Monero community will be anti-ASIC until ASIC will become as available as a CPU.
> 
> I guess you can do that, if you define "most of the community" the vocal 3-4 people that have been posting here the last few days, and you ignore everything that many developers have been saying so far in this chat.

This discussion can't represent whole community, that's obvious.

But just ask random people on random pool chat what they think about it or better yet create a reddit post because this github thread in "issues" is not seen by most people.

Reddit is good place for communication because it's visited by most miners/general Monero community and it's easy to see if account was created 15min ago or was it used for FUD / trolling.

## MoneroCrusher | 2019-03-18T23:16:22+00:00
With regards to dual PoW and block reward I had the following in mind:
First equalize the hash/W between CPUs and GPUs (this means giving a ~100% boost to CPUs from status quo).
The block rewards are then continually & dynamically adjusted depending on how much each chain contributes to security in the form of wattage.

i.e. CPUs PoW provide 62% of the hashrate and GPU PoW provides 38% of the hashrate.
This would mean that the reward equalizer algo would adjust block rewards accordingly and on a continuous basis, just like difficulty does now.

Giving a fixed 50% share is dangerous and also unfair.
Imagine CPUs would be 10% of the GPU hashrate but getting 50% of the rewards. That'd also be pretty easy to pwn.

## justinjja | 2019-03-19T01:58:48+00:00
Hashrate between the 2 is irreverent, 50/50 split is much simpler.
And If cpu's are way more profitable, that will just attract more cpus,
nothing dangerous about it.

## JustFranz | 2019-03-19T02:12:28+00:00
it has been said already, dual POW is unsafe. concentrate on making it safe, not on dividing the money. If it isn't dśafe then its a no-go.

## justinjja | 2019-03-19T02:14:35+00:00
Hence me saying do 50/50 because it is simpler....

## justinjja | 2019-03-19T02:16:03+00:00
I say dual POW is safe, and I'll give more proof than anyone who has said it isn't safe:
GRIN exists.

## lookfirst | 2019-03-19T02:53:50+00:00
> GRIN exists.

That doesn't mean it is safe. It means it hasn't been successfully attacked. Yet.

## vtnerd | 2019-03-19T03:11:11+00:00
> Say you want to do a 51% attack,
> You sell a bunch of Monero to an exchange, withdraw the Bitcoin, then do your 51% attack to revert the transaction.
>
> But if the algo alternates between CPU and GPU, and you only have GPUs (or an ASIC that does the GPU algo), then you could only revert 1 block.

The total throughput of the attacker is the important factor - obtaining 51% of all algorithms is not necessary. An attacker with 60% hashpower on one algorithm needs to rent less hashpower for the other algorithm, etc. An attacker also the has option to use the rented hashpower with a more profitable chain when the "primary" (60%) algorithm is being mined to offset the costs of the attack.

My initial thoughts are that this is likely better than the typical dual-PoW approaches, but it doesn't seem obviously preferable to a single PoW algorithm since it will still splits honest participants who are forced to optimize for one algorithm or the other with their hardware purchases. In the worse case, the hardware of honest miners are completely idle during one of the algorithms which would seem to obviously lower the security of the system. Perhaps you can dig up a research article on this technique, otherwise someone would have to do the equivalent to begin considering it.

> So you cut your power usage in half, or you mine another coin, either is a benefit to a miner,
And would encourage more people to mine monero.

Is this in reference to your alternating suggestion?


> i.e. CPUs PoW provide 62% of the hashrate and GPU PoW provides 38% of the hashrate.
This would mean that the reward equalizer algo would adjust block rewards accordingly and on a continuous basis, just like difficulty does now.

The total security of the system is still the cost of attacking the most vulnerable algorithm. I still don't see a convincing argument to split hashpower up.

FWIW, I also think that forking GPUs off the network is probably a bad idea. And just from the perspective of a theoretical dedicated Monero enthusiast who bought GPUs to support the network now has to trash that investment. I'm not sure how many of those people actually exist.

> I say dual POW is safe, and I'll give more proof than anyone who has said it isn't safe:
GRIN exists.

Grin's proposal is different than any of the other schemes I've seen. I've got some initial thoughts that I would prefer not to share immediately. I have also yet to see any analysis on the security of their approach when compared to a single pow system. A link to such a document would be nice.

## justinjja | 2019-03-19T03:21:34+00:00
The way I see it,
CPU's can be 51%ed with botnets or a new new asics
GPU's can be 51%ed with Nicehash or a new new asics

but if you do alternating, you have to do 1 of each, which is harder.
You could argue that by splitting the POW you make each of those attack vectors 1/2 has hard.
I think that is true for nicehash, but not the other 3.

Getting a bot net from 0 to 1,000,000 cpus seems hard,
Getting a botnet from 1,000,000 to 2,000,000 seems easier.

As for making an asic, the R&D would have to be a large percentage of cost & effort.
So 2 algos means 2x the R&D.

## justinjja | 2019-03-19T03:23:49+00:00
@vtnerd "Is this in reference to your alternating suggestion?"
Ya, compared to running 2 algos at the same time, you effectively cut the miners power usage in half.
And by doing that you will incentivize more miners, and more security.
(at least that is how it works in my head... lol)


## justinjja | 2019-03-19T03:33:42+00:00
@lookfirst as Andreas Antonopoulos would say,
Grin's POW is at least 14 Million dollars safe,
Time will tell if it is more than that. 

## lookfirst | 2019-03-19T04:12:17+00:00
> @lookfirst as Andreas Antonopoulos would say,
> Grin's POW is at least 14 Million dollars safe,
> Time will tell if it is more than that.

He wouldn't say that. He would say (and has said): ["bitcoin is the next bitcoin"](https://twitter.com/aantonop/status/986465155939741696)

Market Cap isn't even a real number in the context of crypto. It is just `number of outstanding shares * price` and regardless, $14m isn't enough to get hackers out of bed.

## justinjja | 2019-03-19T04:28:04+00:00
What? market cap is market cap, just like the market cap of a public company is stock price * number of shares.

## lookfirst | 2019-03-19T06:02:56+00:00
Three reasons market cap does not apply to crypto, any one of them validates the argument:

1. A crypto currency isn't a public company. There are no 'shares'.
1. A crypto currency can lose shares. They can never be traded again.
1. Depending on the currency (ie: Monero for this context), there is an infinite supply. A public company would require a recap.

## fluffypony | 2019-03-19T06:06:10+00:00
I think the point is that the only PoW currencies that are sufficiently large to have *serious* resources thrown at them are Bitcoin and Ethereum, possibly Litecoin as well.

## tarris034 | 2019-03-19T07:59:38+00:00
@vtnerd 


> FWIW, I also think that forking GPUs off the network is probably a bad idea. And just from the perspective of a theoretical dedicated Monero enthusiast who bought GPUs to support the network now has to trash that investment. I'm not sure how many of those people actually exist.

It is bad to throw potential mining equipment off the network but we shouldn't think of it in terms of investment trashing but in terms of security, and as far as I know, CPU algorithms are much safer for the network as we speak.

Miners have always adjusted, if there were ASIC for Monero right now, every professional miner would dump CPU/GPU's and buy into ASIC mining.

They didn't bought GPUs to support the network in the first place, but to earn money so lets not play the victim card here. As evidence, whenever other coin was more profitable they all switched, like in recent ASIC attack, instead of securing the network, most miners that I know switched to <coin_that_i_shall_not_name>.

Also they had plenty of time for ROI, if they didn't - it means they did it wrong.

Still, This situation is not as bad as it is on ASIC coins where you have to change hardware whenever there's a release of much more efficient one making your current hardware unprofitable and almost unsalable. The efficiency hit on CPU is not as drastic and you can usually continue mining with older equipment.

And Dual PoW is a bad idea all around in my opinion, it complicates, it brings another algo to maintain, it gives more options for attackers.

## MoneroCrusher | 2019-03-19T11:07:43+00:00
@vtnerd 
> FWIW, I also think that forking GPUs off the network is probably a bad idea. And just from the perspective of a theoretical dedicated Monero enthusiast who bought GPUs to support the network now has to trash that investment. I'm not sure how many of those people actually exist.

Well, I very much agree with that. 
I can speak for myself:
I have _well over_ 1000 RX 550 2GB GPUs that I **only and specifically bought for Monero mining**.
I knew I wouldn't be able to mine Ethereum with them because of the RAM requirement. I very well could've bought 4GB GPUs but I specifically only wanted to do Monero mining and went with 2 GB because I had absolutely no interest in Ethereum and I knew that I would be able to mine Monero for a long time because Monero wants to keep mining accessible to CPUs (which I very much support by the way), implying a low memory requirement.

I can tell you there are many other RX 550/560 2GB owners in the Monero community.
**Those will become absolutely useless in RandomX.**

So in that regard a dual PoW will also be of benefit, if the leadership of Monero is looking to avoid potential problems.

I can also attest to being a Monero enthusiast:
I encourage my financial transactions to be made in cryptocurrency and will even shortly do another one (quite large transaction) with a very well respected firm that I told about Monero and they're going to accept it now, thanks to my encouragement to them and telling them about the benefits of it. They even said they will keep it instead of converting to fiat.

This is just one example, I wrote dozens of E-mail to all sorts of institutions and shops and told them about cryptocurrency and especially about the fungibility & privacy of Monero **and maybe you can even pay with Monero in some shops today because I dedicated a lot of my time spreading the love for Monero**.

By maliciously attacking the investment of people like me, Monero doesn't do itself a favour and might actually suffer from it and the result of a potential community split. And result in slower growth of it.

Monero is where it is because of the people in the past that actively spread adoption.
Cut that **massive network effect** out and you significantly slow down adoption and even hurt it by officially becoming "botnet coin", becuase I'm pretty sure the largest permanent residents & miners of Monero will be big botnets.

## fluffypony | 2019-03-19T11:16:13+00:00
So basically we mustn't do what is best to secure the network and minimise edge-case risk, we must do what is best to protect your investment...? That doesn't sit well with me because:

1. You should've priced a PoW change in to your investment.
2. You can mine some other GPU-mineable coin and trade it into Monero.

*No matter what decision we make we're going to anger some miners and please others*. I'm deeply sorry, but the aim here is not to please a certain class of miner, nor is it to help a certain class of miner achieve profitability.

## MoneroCrusher | 2019-03-19T11:37:06+00:00
**No, not my investment, _our_ investment.** Quite a difference there.

I'm saying you're actively hurting Monero by actively excluding a huge portion of its network and implicit network effect that it carries.

Would you rather have 1000 Monero enthusiasts spreading adoption and making the network stronger, or would you rather have 10'000?

Actually a better analogy would be:
Would you rather have 10'000 enthusiasts spreading Monero adoption and keep the 10'000
or
Would you rather have 10'000 enthusiasts spreading Monero adoption and cut them down to 1000

I already argued how a dual PoW can actually add more resiliency to the network against malicious behaviour.

Very strange how many in the Monero community like @dEBRUYNE-1 point out to Zcash's failed evaluation of dual PoW, yet they constantly ridicule Zcash on social media and other platforms, also including you there. That's called cherry-picking.

**I ask again, since when do we have to rush things?**
We can evaluate a potential dual PoW solution that may actually work.

Even @tevador one of the main devs of RandomX is open to a dual PoW as evidenced [here.](https://www.reddit.com/r/Monero/comments/aovypq/randomx_asic_resistant_pow_community_feedback/eg5ew98)

 @fluffypony Please tell me which miner you are going to piss off with a dual PoW?
Maybe strong RandomX-pure proponents will be pissed off, ever thought about it?
I can tell you: botnet owners, state actors and huge server farm owners will be pissed off.

A dual PoW solution includes CPU miners, GPU miners and FPGA miners. All commodity hardware.

## fluffypony | 2019-03-19T12:05:01+00:00
> Would you rather have 10'000 enthusiasts spreading Monero adoption and cut them down to 1000

Most miners are capitalists and simply do not care. They are not enthusiasts spreading Monero adoption.

> That's called cherry-picking.

I can tell you a bunch of things that ZCash is doing that's amazing. Have you seen Sonic? It solves the trusted setup issue in a very elegant way.

I can also point out a bunch of things they're doing wrong, which I often do, but it doesn't change the fact that many of their staff are extremely talented. You seem to suggest throwing the baby out with the bathwater.

> We can evaluate a potential dual PoW solution that may actually work.

You're literally the only one on this thread asking for a dual PoW. You're like the people who think Monero should switch to PoS. They certainly exist, but it's dead in the water and never happening.

> Even @tevador one of the main devs of RandomX is open to a dual PoW as evidenced here.

Appeal to authority. Dual PoW introduces needless complexity and edge-cases that we simply are not required to deal with.

> Please tell me which miner you are going to piss off with a dual PoW?

The professional ones that like their network stable.

> I can tell you: botnet owners, state actors and huge server farm owners will be pissed off.

So then the solution is to skip RandomX and go straight to SHA3 ASICs :)

## MoneroCrusher | 2019-03-19T12:12:54+00:00
> > Would you rather have 10'000 enthusiasts spreading Monero adoption and cut them down to 1000
> 
> Most miners are capitalists and simply do not care. They are not enthusiasts spreading Monero adoption.

True, but some miners bought hardware to specifically mine Monero with nothing else in mind. You're suggesting destroying their investment.
> > We can evaluate a potential dual PoW solution that may actually work.
> 
> You're literally the only one on this thread asking for a dual PoW. You're like the people who think Monero should switch to PoS. They certainly exist, but it's dead in the water and never happening.

Funny how you think I'm the only one. I think you have a strong bias here or you clearly didn't read through the thread.
there are 3 main developers of RandomX: @hyc @tevador @SChernykh of which two suggested a dual PoW might be possible and would make sense to do.
> 
> > Even @tevador one of the main devs of RandomX is open to a dual PoW as evidenced here.
> 
> Appeal to authority. Dual PoW introduces needless complexity and edge-cases that we simply are not required to deal with.

You're completely ignoring the benefits it can provide.
> 
> > Please tell me which miner you are going to piss off with a dual PoW?
> 
> The professional ones that like their network stable.

Very biased answer. I consider myself a professional miner.
> 
> > I can tell you: botnet owners, state actors and huge server farm owners will be pissed off.
> 
> So then the solution is to skip RandomX and go straight to SHA3 ASICs :)

Maybe 5 years from now when ASIC manufacturers will be fair & more diverse. Suggesting that Monero will somehow magically "incentivize" SHA-3 ASICs is grapsing at straws. Have you seen it happen with Bitcoin? Maybe a _liiiitttle_ bit after what, 7-8 years?

## tarris034 | 2019-03-19T12:17:21+00:00
@MoneroCrusher You can't blame Monero for your gambling, because that's what every investment is.

Professional miners will just adjust, your hardware will not be bricked, it's not Monero-ONLY hardware.
You can sell it and adjust to the new PoW or mine something else and trade.

Either way whatever you do, this thread is not about investments.

## justinjja | 2019-03-19T12:26:33+00:00
The latest updates I have seen from zcash suggest dual pow is delayed so they can figure out reward time locking. Not something monero needs.

Also wow zcash...
" I’ve decided that it is better for the users"
https://forum.zcashcommunity.com/t/the-final-nu2-blossom-network-upgrade-goals/32449

Staeting to sound like fluffy ponys stance on dual pow, at least fluffy pony doesn't openly say it like that. 

## tarris034 | 2019-03-19T12:30:00+00:00
From their voting pool I can see majority is against dual PoW.
There are also some good points made there about it being less secure and problematic.

## MoneroCrusher | 2019-03-19T12:42:08+00:00
It seems like most of you have already made your minds up and defend your beliefs and positions because it's the most easy and comfortable thing to do.
I argued as a Monero enthusiast and miner: It's the best for Monero if as many people as possible participate and if the mining rewards are as widely distributed as possible. _**If**_ it's possible to do so with a dual PoW and it's safe to do so with a dual PoW, it certainly should be done, don't you agree?

## tarris034 | 2019-03-19T12:45:24+00:00
I base my opinion solely on facts, I suggest you to try seeing it from Monero perspective, not from your investment perspective.

## MoneroCrusher | 2019-03-19T12:46:03+00:00
It's not a fact that dual PoW is unsafe and impossible.

## tarris034 | 2019-03-19T12:46:39+00:00
> It's not a fact that dual PoW is unsafe and impossible.

It is possible - fact.
It is unsafe - fact.

Just read more about it.

## JustFranz | 2019-03-19T12:49:51+00:00
@MoneroCrusher 

I'm sorry about your investment, its never fun seeing someones effort in jeopardy.

Here is the situation, ASICs are made for CN algo in 1 month. We can't keep this POW.

If we go dual POW then the GPU POW will have to be sufficiently resistant to ASICs (what does that even mean at this point in the discussion?). If that was possible then we could just go with that POW only. Even if the CPU pow was better at ASIC reistance, having 2 POW is a worse solution and you are better of with 1 that does the job.

I see 4 scenarios here for Monero and all of them leave you screwed.

1. No agreement is reached on ASICs and we will have to adopt the most ASIC hard algo that we have, that is RandomX, and then we hope for the best. You have until October, if ASICs don't come before that.

2. An agreement is reached on ASICs for the 2020 April fork and we do not go to a new algo in the meantime. The current algo gets ASIC'ed in a few months and your GPUs are useless on Monero.

3. ASIC algo in 2019 October fork, meanwhile an ASIC is made for Monero, it ROIs and your GPU are worthless.

4. RandomX in 2019 October and ASIC algo a year+ after. Maybe an ASIC will come before October, make your GPU worthless for Monero mining.

I don't see us having a GPU algo after October, after that it has to be SHA-3 or RandomX.


## abhishek1104 | 2019-03-19T12:58:27+00:00
@JustFranz 

I will say 

Irrespective of anything involved it is better to have a mining algo which supports the commodity hardware (i.e. cpu/gpu) than ASICs only.

That said in case some new research comes which assures dual pow to be safe then there is nothing wrong to go for it. (Assumption ASICS performance comparable with cpu/gpu).



## tevador | 2019-03-19T13:00:35+00:00
> Even @tevador one of the main devs of RandomX is open to a dual PoW as evidenced here.

I have since changed my opinion and recommend *against* using a dual PoW, given the security issues that it brings to the network.

Actually, your version of dual PoW with dynamic block rewards it just about the worst solution that has all the disadvantages of dual PoW and no benefits. The network would be primarily secured by one type of hardware (GPUs), because nobody would mine the CPU algorithm due to low rewards. The low difficulty of the CPU PoW would allow the network to be attacked very easily by any medium-sized datacenter or small botnet. This is a complete opposite of what you'd want in a dual PoW - about the same cost of attack for both algorithms. This is the main reason why a single PoW is more secure.

## MoneroCrusher | 2019-03-19T13:08:24+00:00
@JustFranz you don't need to be sorry for me, be sorry for Monero losing thousands of users and enthusiasts when going through with it and actively destroys the investments of hundreds if not thousands of people.

Sufficiently resistant:
I think 2x is sufficiently resistant with a longer term tweaking schedule like 1x per year. Possible with Ethash variation or CN-R-Memory-hard

So there's the solution.

Scenario that works out:
Dual PoW with RandomX and CN-R-Memory-Hard

@tevador 
Why would CPU profitability be lower? In my suggestion the hash/W between CPU and GPU is normalized first.
I would say it's unsafe to split it 50:50 or something. Mining rewards should be distributed according to how much electricity is spent, not what type of hardware you mine with.

## zexanana | 2019-03-19T13:13:26+00:00
Monero will not lose thousands of users and enthusiasts. It might lose many GPU miners but will probably win a lot more (individual miners as a metric, not hashrate).

## abhishek1104 | 2019-03-19T13:16:07+00:00
@tevador ,
There is not even an iota of doubt that all people support the security of network to be the primary concern.

@JustFranz ,
Even in the worst case scenario - Why should we prefer an algo which is solely min-able through ASICS ONLY over commodity hardware including GPUs ? 

Even 5X performance over ASICS is OK rather than ONLY ASICS approach. 

## tevador | 2019-03-19T13:19:26+00:00
@MoneroCrusher 
You got it backwards. You have to make the mining rewards split 50:50 so that each PoW reaches the same level of security via competition.

If you artificially modify the block reward, you will have a less secure blockchain. Note that Grin doesn't modify the block rewards, but increases the target difficulty to phase out one of the algorithms.

## MoneroCrusher | 2019-03-19T13:19:56+00:00
I think you have a too optimistic view. As I said, your grandma is not going to strain her tablet battery to mine Monero and eventually burn down her house.
With CPU-only you'll have a few large botnets and maybe some on-off server farms offloading idle-time to the network. You'll have almost no dedicated miners, which are very good for a network.

Also you're missing out the bigger picture:
There is an entity that is actively producing CN ASICs at a loss in order to push a bigger agenda:

1. First get rid of GPU miners (the most loyal and dedicated miners)
2. Then push RandomX profitability down the shitter with some huge ARM SoC clusters or even an ASIC that will push Monero to SHA-3, their ultimate end-goal.

If that happens Monero will lose a lot of its appeal and ASIC manufacturers can start milking the community.

## MoneroCrusher | 2019-03-19T13:21:32+00:00
@tevador No, why should you artificially prop up the reward of one half if it doesn't meet its "obligation" (security contribution to the network).
Both the CPU and the GPU chain will have exactly the same chance of reaching 50% of the reward.

In my scenario it's pure competition of CPUs vs. GPUs. That's a good thing and they also have the same hash/W. Nothing artificial about it.

## abhishek1104 | 2019-03-19T13:26:41+00:00
@MoneroCrusher ,

I will say be it CPU /GPU - whatever but not ASICs ONLY (Our approach never have been GPU resistant , but ASICs resistant)

## MoneroCrusher | 2019-03-19T13:27:40+00:00
I don't want to see ASIC on the network at all because they're not easily accessible commodity hardware like CPUs, GPUs and FPGAs.
Until that changes: no ASICs.

## tevador | 2019-03-19T13:31:46+00:00
@MoneroCrusher 
> No, why should you artificially prop up the reward of one half if it doesn't meet its "obligation" (security contribution to the network).
Both the CPU and the GPU chain will have exactly the same chance of reaching 50% of the reward.

Again, you got it backwards. You have to pay more to the less secure half so that its hashrate increases and the security matches the other algorithm.

If you do the opposite - "punish" one of the algorithms for not having enough hashrate, you will end up with 0 hashrate in it.


## AirSquirrels | 2019-03-19T13:34:16+00:00
While this thread has gotten way off topic, I have a couple toss ins.

1. Thousands of people bought FPGAs to mine CN last summer. Monero changed in a way that burned their investment. Monero is not to blaim, although those users most likely represented some of the most capitalistic.

2. RandomX isn’t “impossible” on GPU. It is just hard, and definitely not designed for it. Sure it will likely be less efficient than CPU mining, but I’m not aware of any serious optimized effort to implement it for GPU yet. 

## MoneroCrusher | 2019-03-19T13:34:20+00:00
@tevador Why should one breed of hardware have less hashrate in its chain than the other when they have the same hash/W? Literally contradicts everyone in this whole thread, that all claim CPU hashrate & power usage (as a whole network) will be the same as now under RandomX.

## jtgrassie | 2019-03-19T13:40:56+00:00
@abhishek1104 
> I will say be it CPU /GPU - whatever but not ASICs ONLY (Our approach never have been GPU resistant , but ASICs resistant)

That is not strictly true if you refer back to the CryptoNote whitepaper (s.5):

"Our primary goal is to close the gap between CPU (majority) and GPU/FPGA/ASIC (minority) miners."

One could say RandomX precisely meets this goal.

## tevador | 2019-03-19T13:42:04+00:00
@MoneroCrusher For example some big GPU farm could buy enough hashrate to push the CPU rewards to zero. Once the rewards reach zero, they will never recover because nobody will mine for free.

I suggest you to read about the concept of stable/unstable equilibrium.

## MoneroCrusher | 2019-03-19T13:42:51+00:00
@jtgrassie 
TBH It's reasonable to say that as of March 2019 GPU miners are the big decentralized majority when it comes to crypto and also hashcat.

## jtgrassie | 2019-03-19T13:45:53+00:00
@MoneroCrusher I wasn't making a judgement/assessment about the current state, just correcting a statement made by @abhishek1104.

## JustFranz | 2019-03-19T13:46:34+00:00
@MoneroCrusher 
> I think 2x is sufficiently resistant with a longer term tweaking schedule like 1x per year. Possible with Ethash variation or CN-R-Memory-hard

We have 2x with RandomX (we can't be 100% sure that it isn't more in favor of ASIC) and RandomX is so low level that no meaningful tweaks are possible. A tweakable algo has to be high level and high level algo means that the possible ASIC advantage is bigger.

A 6 month algo tweak schedule is unsustainable and as we can see it doesn't work either. An ASIC can be created and deployed in a month or 2.

Regarding the logic of 50:50 split, if each algo is mined with hardware in the same efficiency class, meaning no super ASICs/FPGAs, then both will reach equilibrium and will be burning electricity roughly equivalent to the mining reward. That is the only fair way to do it + its simple.

What you are describing is a convoluted method to reach the same ratio of CPU/GPU miners that we have now, only that it won't work. Hash rates are just numbers and they are absolutely strictly just numbers when comparing two different POW algos.

You pay for security with mining rewards. If you make it 50/50 then its going to get filled 50/50. If you make it 20/80 then that is going to be the ratio of mining (measured by cost to the miners). Your dynamic idea won't work. Think about it a little. You want the network to be 50/50, you make the rewards 50/50 and people will come for those rewards. Any kind of unevenness of rewards per watt will disappear shortly or get evened out as profit seeking miners switch over.

I don't know how to make it more clear.

>No, why should you artificially prop up the reward of one half if it doesn't meet its "obligation" (security contribution to the network).

You aren't propping anything, you are setting the pay for security and you will be getting mining security that costs about that amount of XMR across the whole network. Your tug-of-war system is stupid, sorry.

## abhishek1104 | 2019-03-19T13:51:06+00:00
@jtgrassie ,

My point was mainly if we have to chose among commodity hardware's and ASICS, i would prefer first for obvious reasons -- readily available ,no as such BANs,KYC etc.

That said i support CPU (primarily) ,GPU both and also Random-X ,it will even be minable on GPUs .

But no ASIC only where there is no place for CPUs/GPUs.


## MoneroCrusher | 2019-03-19T13:56:32+00:00
@tevador Same can be said about the opposite.
One could build in a very simple "kickstarter" function.
Reset the reward between the two like every e.g. 10000 blocks so every hardware type has the chance to re-establish itself

@JustFranz 

> We have 2x with RandomX (we can't be 100% sure that it isn't more in favor of ASIC) and RandomX is so low level that no meaningful tweaks are possible. A tweakable algo has to be high level and high level algo means that the possible ASIC advantage is bigger

According to your assesment Ethash is a high-level algo, yet it only has 2x ASICs. Memory hardness seems to work apparently.

> A 6 month algo tweak schedule is unsustainable and as we can see it doesn't work either. An ASIC can be created and deployed in a month or 2.

In the post above I said with a 2x efficiency gain **once** a year should be enough. I didn't say 6 months.

> Regarding the logic of 50:50 split, if each algo is mined with hardware in the same efficiency class, meaning no super ASICs/FPGAs, then both will reach equilibrium and will be burning electricity roughly equivalent to the mining reward. That is the only fair way to do it + its simple.

No, the fair thing is to let the two compete against each other with same hash/W. Anything else is insecure. If we assume same hash/W they should naturally be in fair competition.
But if for some reason one chain contributes less hashrate, then it should be much easier to attack that weaker chain and rent some hash for the other chain.

> What you are describing is a convoluted method to reach the same ratio of CPU/GPU miners that we have now, only that it won't work. Hash rates are just numbers and they are absolutely strictly just numbers when comparing two different POW algos.

No, currently CPUs have a worse hash/W, thus they are the smaller proportion. In my attempt the hash/W get equalized for CPUs vs GPUs before the deployment of dual PoW.

> You aren't propping anything, you are setting the pay for security and you will be getting mining security that costs about that amount of XMR across the whole network. Your tug-of-war system is stupid, sorry.

Let's assume one chain is centralized, then they could just take off hashrate and still get 50% of the reward. Everyone needs to be in competition. CPUs vs. GPUs vs FPGAs. No need to create safespaces and guaranteed incomes for either chain.

Everyone gets paid for the security they provide, the way it should be.

## fluffypony | 2019-03-19T14:00:54+00:00
> @tevador Why should one breed of hardware have less hashrate in its chain than the other when they have the same hash/W? Literally contradicts everyone in this whole thread, that all claim CPU hashrate & power usage (as a whole network) will be the same as now under RandomX.

By this logic you should be pushing for quadruple mining: CPU, GPU, FPGA, and ASIC.

## MoneroCrusher | 2019-03-19T14:01:46+00:00
@fluffypony I actually would if ASICs were commodity hardware.

## fluffypony | 2019-03-19T14:02:31+00:00
> @abhishek1104
> 
> > I will say be it CPU /GPU - whatever but not ASICs ONLY (Our approach never have been GPU resistant , but ASICs resistant)
> 
> That is not strictly true if you refer back to the CryptoNote whitepaper (s.5):
> 
> "Our primary goal is to close the gap between CPU (majority) and GPU/FPGA/ASIC (minority) miners."
> 
> One could say RandomX precisely meets this goal.

Hah, I didn't even realise it made that distinction! I think that puts an end to the "but the whitepaper says" argument once and for all.

## tevador | 2019-03-19T14:21:27+00:00
@MoneroCrusher 

> @tevador Same can be said about the opposite.

Yes, that's why your dynamic rewards proposal is a not a good idea. It brings instability into the system.

> One could build in a very simple "kickstarter" function.
> Reset the reward between the two like every e.g. 10000 blocks so every hardware type has the chance to re-establish itself

10000 blocks is more than enough for the system to become unstable and be 51% attacked via the weaker algorithm.

Clearly you care just about your GPU mining profits and not about the network security. This is evident from the following:

* Your proposal focuses on block rewards and not other issues of dual PoW such as difficulty adjustment mechanism.
* You see "CPU miners" and "GPU miners" as two competing sides where one must claim victory over the other.


## MoneroCrusher | 2019-03-19T14:28:25+00:00
@tevador 

> 10000 blocks is more than enough for the system to become unstable and be 51% attacked via the weaker algorithm.

you know the meaning of "e.g."? It was an example. Obviously I just made up this number for the sake of an example. And no you need 51% of the whole network to execute attack as far as I know.

> Clearly you care just about your GPU mining profits and not about the network security. This is evident from the following:
> 
> 1. Your proposal focuses on block rewards and not other issues of dual PoW such as difficulty adjustment mechanism.
> 2. You see "CPU miners" and "GPU miners" as two competing sides where one must claim victory over the other.
> 

Well I also argue it adds more resiliency against malicious behaviour and that it will keep community peace by allowing CPUs, GPUs and FPGAs.

1. It's a very central problem for security if one chain is centralized but is still guaranteed to get 50% of the reward. They will then just reduce their effort and still get 50%. -> weaker network
2. Therefore competition of GPUs vs. CPUs vs. FPGAs is better in that case, as long as they have similar hash/W everything is fair.

## JustFranz | 2019-03-19T14:31:17+00:00
@MoneroCrusher 
> One could build in a very simple "kickstarter" function.
> Reset the reward between the two like every e.g. 10000 blocks so every hardware type has the chance to re-establish itself

What if a chain was centralized (your scenario) and for the kickstarter function brought his machines online, after that it takes a percentage of them offline/switches to another coin to get better profits. This kind of mechanism would encourage all kinds of miners to point their hardware at Monero for the duration of the "kickstarter function" and then pull back.

Mining pools, whales etc. already do this for the smaller coins. They game the difficulty algos.

> According to your assesment Ethash is a high-level algo, yet it only has 2x ASICs. Memory hardness seems to work apparently.

Memory is getting cheaper/faster. You can't rely on memory anymore. You just need more of it. BTW, wouldn't a memory hard algo ruin your RX 550s?

> In the post above I said with a 2x efficiency gain **once** a year should be enough. I didn't say 6 months.

I don't understand. A high level algo will likely have higher possible efficiency than 2x. Also tweaks don't work, you'll have to swap out the whole algo. That 1 year is long enough anyway to get ASIC'ed. A tremendous amount of work for what exactly? 

> No, the fair thing is to let the two compete against each other with same hash/W. Anything else is insecure. If we assume same hash/W they should naturally be in fair competition.

What do you think hash rate is and what does it signify? Explain in your own words. You have two different classes of hardware made on many different process technologies working on two different algorithms. How do you equalize them to the same hash/W when everything about them is so different?
Only way to control either side is by setting the mining reward and for security you want them to be equal.

> But if for some reason one chain contributes less hashrate, then it should be much easier to attack that weaker chain and rent some hash for the other chain.

This is different how from your dynamic scenario where the POW sides will be different anyway?

> No, currently CPUs have a worse hash/W, thus they are the smaller proportion. In my attempt the hash/W get equalized for CPUs vs GPUs before the deployment of dual PoW.

By twisting the POWs into co-dependent pretzels? You want to do so much work and risk so much for something that is just a number. Hash rate is just a number!

> Let's assume one chain is centralized, then they could just take off hashrate and still get 50% of the reward. Everyone needs to be in competition. CPUs vs. GPUs vs FPGAs. No need to create safespaces and guaranteed incomes for either chain.

(see my first bit of the reply above)
If one POW side is centralized then why do we have it anyway?

You pay for the security you want. You don't throw money out there and see what you get. Its not guaranteed income, its guaranteed pay for a guaranteed security profile that you desire for a coin.

If you want dual-POW then you shouldn't be advocating for the most flawed and broken version of it.


## zexanana | 2019-03-19T14:55:36+00:00
As it has been said, GPU will probably still be profitable because scaling a CPU operation is not yet trivial (in constrast to GPUs). Give RandomX enough time and we might see specialized hardware being able to house many server grade CPUs. This is not bad because the marginal cost per CPU between this and a home setup can't possibly be very big.

## MoneroCrusher | 2019-03-19T14:55:43+00:00
> @MoneroCrusher
> 
> > One could build in a very simple "kickstarter" function.
> > Reset the reward between the two like every e.g. 10000 blocks so every hardware type has the chance to re-establish itself
> 
> What if a chain was centralized (your scenario) and for the kickstarter function brought his machines online, after that it takes a percentage of them offline/switches to another coin to get better profits. This kind of mechanism would encourage all kinds of miners to point their hardware at Monero for the duration of the "kickstarter function" and then pull back.

You're confusing something. The kickstarter scenario would only be required in the dynamic reward algorithm scenario, in that scenario they don't have a guaranteed 50%, so they will not lower their rewards.
Kickstarter function, as the name implies is here to help a minority chain (should there be one) give a periodical chance to become as strong or stronger than the other chain.
> 
> > According to your assesment Ethash is a high-level algo, yet it only has 2x ASICs. Memory hardness seems to work apparently.
> 
> Memory is getting cheaper/faster. You can't rely on memory anymore. You just need more of it. BTW, wouldn't a memory hard algo ruin your RX 550s?

I believe anything over >500MB can't be run on-chip. External memory = slow. So no I don't believe RX 550 would be bad for that. They can mine ethash well with DAG <2GB
> 
> > In the post above I said with a 2x efficiency gain **once** a year should be enough. I didn't say 6 months.
> 
> I don't understand. A high level algo will likely have higher possible efficiency than 2x. Also tweaks don't work, you'll have to swap out the whole algo. That 1 year is long enough anyway to get ASIC'ed. A tremendous amount of work for what exactly?

Ethash doesn't seem have more than 2x. My statement stays the same. Let me know if you know of a super-efficient ASIC for ethash, I don't know of any existing ones.
> 
> > No, the fair thing is to let the two compete against each other with same hash/W. Anything else is insecure. If we assume same hash/W they should naturally be in fair competition.
> 
> What do you think hash rate is and what does it signify? Explain in your own words. You have two different classes of hardware made on many different process technologies working on two different algorithms. How do you equalize them to the same hash/W when everything about them is so different?
> Only way to control either side is by setting the mining reward and for security you want them to be equal.

Hashrate is how many solutions can be found in a given time. And yes, I know it's basically a meaningless number without anything else attached.
Anyways, you can very easily equalize it:
Just tweak the algo so CPUs and GPUs have the same hash/W in CN then just do the switch to RandomX for CPUs and have a constant act as a divisor that internally normalizes hashrates and then know how much each chain is contributing.
Alternatively tweak RandomX in such a way that it shows the same hashrate as in CN (after making the hash/W equalization in CN).
> 
> > But if for some reason one chain contributes less hashrate, then it should be much easier to attack that weaker chain and rent some hash for the other chain.
> 
> This is different how from your dynamic scenario where the POW sides will be different anyway?

It's very different, please re-read. I said in a 50/50 fixed scenario a centralized entity is incentivized to reduce their hashrate because their 50% is guaranteed. In the dynamic scenario they have no such incentive because they need to compete with other hardware.
> 
> > No, currently CPUs have a worse hash/W, thus they are the smaller proportion. In my attempt the hash/W get equalized for CPUs vs GPUs before the deployment of dual PoW.
> 
> By twisting the POWs into co-dependent pretzels? You want to do so much work and risk so much for something that is just a number. Hash rate is just a number!

No, just dual PoW. Simple and beautiful. If possible. Otherwise I don't advise for dual PoW, if it can't be done safely.
> 
> > Let's assume one chain is centralized, then they could just take off hashrate and still get 50% of the reward. Everyone needs to be in competition. CPUs vs. GPUs vs FPGAs. No need to create safespaces and guaranteed incomes for either chain.
> 
> (see my first bit of the reply above)
> If one POW side is centralized then why do we have it anyway?

See my answer above. You're confusing incentives in 50/50 vs. dynamic scenario.
> 
> You pay for the security you want. You don't throw money out there and see what you get. Its not guaranteed income, its guaranteed pay for a guaranteed security profile that you desire for a coin.
> 
> If you want dual-POW then you shouldn't be advocating for the most flawed and broken version of it.

I'm open to talk of course, we don't need to do dynamic adjustment, but so far I believe it to be the fairest and safest option. I can be convinced otherwise (not implying that I need to be convinced, I'm not the king of Monero and can decide of its fate 😄 )

## MoneroCrusher | 2019-03-19T14:58:25+00:00
> As it has been said, GPU will probably still be profitable because scaling a CPU operation is not yet trivial (in constrast to GPUs). Give RandomX enough time and we might see specialized hardware being able to house many server grade CPUs. This is not bad because the marginal cost per CPU between this and a home setup can't possibly be very big.

It's the opposite. CPUs are less competitive for home miners than GPUs are. We will not magically see 10 Ryzen MBs, that's very expensive stuff I odn't even know if it's possible. The max I've seen are 4 and they cost thousands of dollars (not for Ryzen)

## tarris034 | 2019-03-19T15:07:38+00:00
> > As it has been said, GPU will probably still be profitable because scaling a CPU operation is not yet trivial (in constrast to GPUs). Give RandomX enough time and we might see specialized hardware being able to house many server grade CPUs. This is not bad because the marginal cost per CPU between this and a home setup can't possibly be very big.
> 
> It's the opposite. CPUs are less competitive for home miners than GPUs are. We will not magically see 10 Ryzen MBs, that's very expensive stuff I odn't even know if it's possible. The max I've seen are 4 and they cost thousands of dollars (not for Ryzen)

@MoneroCrusher 

There are extension cards with CPU like SBC - Single Board Computer:
FS-A79 - PICMG 1.3 Full-size SBC with support for Intel Core 8th Generation Processors

Also there were some Intel CPU accelerator cards if I remember ? I'm not that much into server grade equipment.

I remeber about ~18 years ago some small graphic company announced a PCI(or was it AGP?) board which could take multiple desktop CPU's like 6 or 8 of them (can't remember) and with their firmware act like a GPU. Don't know if they managed to release it.

## justinjja | 2019-03-19T15:11:55+00:00
@tevador I can see issues with some of the ways you would do dual pow.
What issues are there with 50/50 rewards, and spliting cpus to even number blocks, gpus to odd number blocks?

In my head this seems simple, stable and secure.

## MoneroCrusher | 2019-03-19T15:14:41+00:00
@tarris034 I don't even want to see the price of stuff like that. There's a reason multi CPU boards are expensive. You can't just put more CPUs on the lanes of one central CPU like you can do with GPUs, but I'm not really an expert but I've looked into it when planning my farm but I eventually stopped investigating when I saw prices.
As I mentioned earlier, I wanted to do a Ryzen farm at first, but it's impossible to have multiple CPUs onboard cheaply, so I went with GPUs.

## tarris034 | 2019-03-19T15:19:15+00:00
@MoneroCrusher it could be possible to build farm consisting of cheap micro-atx mobos, the price of the cheapest mobo + good CPU is still less than one good GPU. It's less power hungry as well.

## justinjja | 2019-03-19T15:19:38+00:00
Mining specific CPU boards will come, if RandomX holds, especially if we have another bull run.
All you need is 1 or 2 sticks of ram, and a sata port, a vga port, an ethernet  port, a usb port, and a bios.
All the other IO on a mobo can be left off.

You could fit about 4 CPU's in a standard atx board like that.
It would effectively be 4 computers on 1 board

## tarris034 | 2019-03-19T15:36:52+00:00
> Mining specific CPU boards will come, if RandomX holds, especially if we have another bull run.
> All you need is 1 or 2 sticks of ram, and a sata port, a vga port, an ethernet port, a usb port, and a bios.
> All the other IO on a mobo can be left off.
> 
> You could fit about 4 CPU's in a standard atx board like that.
> It would effectively be 4 computers on 1 board

RandomX + This config = everyone can build his own "ASIC" miner.

Those ASIC manufacturers could switch their manufacturing to fit RandomX by producing mobos for multiple CPU's, would have lot of buyers... 

## MoneroCrusher | 2019-03-19T15:42:11+00:00
I think we should work on what we have and not based assumptions of future bull markets and that multi CPU MBs will then be as plentiful as normal MBs (as effectively a GPU mining MB basically is, just with split up lanes). Big difference there in architectural changes and production cost.

## justinjja | 2019-03-19T15:46:54+00:00
That's fine, what we do have is:
1) A majority of monero users who don't mine(yet), and have a computer with 4gb ram
2) cheap matx ryzen boards that could be stacked about 1/2 as power dense as a gpu rig, for people who want to go larger scale.

## MoneroCrusher | 2019-03-19T15:50:58+00:00
Problem isn't power density, it's cost-efficiency of home miners vs server farms and botnets.
With CPUs home miners don't have a big advantage. vs. server farms (economies of scale) an botnets (illegal)
While with GPUs the advantage is dozenfolds because of the MBs, both against server farms & botnets.

However, dual PoW allows for every commodity hardware.

## tarris034 | 2019-03-19T15:52:12+00:00
@MoneroCrusher There are computing centers with GPUs as well, we don't see them storming the gates of profitability. Botnets for ETH GPU PoW is nothing new, and XMR GPU mining botnets were already found by AV companies as described in their reports. Nothing new.

> However, dual PoW allows for every commodity hardware.

It was already said it has too many flaws to be implemented.


## MoneroCrusher | 2019-03-19T15:56:25+00:00
I'm spinning in circles here so I'll just copy paste my old answer to this:

> The problem I see with CPU mining is that hobby miners are at a great disadvantage to professional data-centers and botnets.
> While with GPU mining hobby miners are in a very unique position in it that they actually have better cost-effectiveness than even the biggest data-centers you could imagine, like Google or Amazon. Reason being that GPUs are sold in two categories: Enterprise & Consumer. The consumer grade GPUs are not sold to big datacenters and they’d have no use for them. Thus hobby GPU miners have an enormous cost advantage because they get much more bang for the buck with regards to mining and they can absolutely cheap out on literally every other component:
> - Gen1/2 x1 PCIE speed with cheap risers ($2 a pop)
> - 2-core CPUs ($30)
> - minimum RAM ($35)
> - Cheap motherboards where you can stuff in 12/13 GPUs (-> you can’t cheaply do that with CPUs) ($70-100)
> - Open air rigs ($30-40)
> - Ignoring dust and cheaply cool rigs or even a farm with big industrial fans (also cheap)
> 12 RX 570 will cost you about $1800 (new with 3 years warranty). So we have a pure compute vs. rig cost ratio of about 10:1.
> A professional data-center manager would find themself in fetal position if they had to work under such circumstances. The average hobby miner doesn’t care as long as the rig is producing cryptocurrency. That’s why GPU mining is the best shot we’ve got at preserving dedicated & decentralized hobby mining. But I would very much welcome a dual PoW mechanism that preserves both CPU & GPU mining in Monero with a dynamic block reward algorithm between CPUs & GPUs. Many people get into this space by trying for themselves and seeing the system work and a lot more people have CPUs to try it on, usually after getting a taste, most people want to build something dedicated to it and that’s much easier, cheaper & effectively done with GPUs.
> 

However, it was correctly pointed out that datacenters sometimes run hundreds of GB of RAM which makes them expensive. On the other hand they order thousands of EPYC so they get massive economies of scale.

But you can't deny that GPU miners are a dozenfold more cost-efficient in comparison to them.

## tarris034 | 2019-03-19T15:57:53+00:00
@MoneroCrusher copy/pasting is lack of effort to come with new logical points.

CPU mining is much more efficient.

## MoneroCrusher | 2019-03-19T15:58:06+00:00
Seems like you don't like facts after all?
No it isn't. Read through my copy-paste and you'll understand why.

## tarris034 | 2019-03-19T15:59:51+00:00
> Seems like you don't like facts after all?
> No it isn't. Read through my copy-paste and you'll understand why.

I have read it already and I don't agree as you would guess from what I wrote earlier.

You're just trying to extend your mining operation, that's it.

I guess what I'm trying to say here is, I'm sorry but I'm not sorry.
It was your call to invest in Monero which was never meant as an investment but as a store of value and for usage.

## MoneroCrusher | 2019-03-19T16:01:12+00:00
That's a starting point. So what exactly makes you think GPU rig setups are not more cost efficient than CPU setups vs big serverfarms & botnets?

## JustFranz | 2019-03-19T16:02:56+00:00
@MoneroCrusher
> Kickstarter function, as the name implies is here to help a minority chain (should there be one) give a periodical chance to become as strong or stronger than the other chain.

After the kickstart function, is the reward fixed until the next kickstart? If its not fixed then why not have a fully dynamic chain that responds well? What is the point of the function? The kickstart period of one chain will have to be compared to the other, you can stack one side for the duration of the kickstarter function and suppress the other side.

> No, the fair thing is to let the two compete against each other with same hash/W. Anything else is insecure. If we assume same hash/W they should naturally be in fair competition.

If one side of the POW ends up with a minority power/upkeep/hardware cost for their network then you can 51% the whole network much easier. Its best to ensure equality by making the rewards fixed and equal. This way the network will fill to mine it and reach an equilibrium that is close to breakeven with both sides spending an equal effort, that is the most secure. Your network is as secure as the weakest POW network, having them equal is the maximum.

> Just tweak the algo so CPUs and GPUs have the same hash/W in CN then just do the switch to RandomX for CPUs and have a constant act as a divisor that internally normalizes hashrates and then know how much each chain is contributing.

The purpose of the POW is to be ASIC resistant, it uses however many W as it needs and it does as many hashes for W as it happens to do. You must not start tweaking them for other hash rate/ power use. How do you equalize the hash rate/w across Intel, Amd, ARM and all of the different generations of their CPUs? Same for GPU. 

> It's very different, please re-read. I said in a 50/50 fixed scenario a centralized entity is incentivized to reduce their hashrate because their 50% is guaranteed.

Why even have one of the sides if it tends to get centralized? IF they can just take 50% off, that would indicate that they have some huge (read ASIC) advantage and they have inflated the hash rate so much that even the cheapest CPU/GPU miner is in the red several fold.

If the monopolized miner reduces their mining so much that it is profitable for others to join then the void will be quickly filled by other profit seeking miners. If the miner can reduce their mining and maintain same profits and nobody else can join, then that means that the network was overpaying for security. At all times the mining reward will be providing maximum security that it can buy. 

The 50% of a side is guaranteed but others can always join the network and take a cut. It will be in equilibrium.

For block verification you want hashing to be as easy as possible (we have to juggle ASIC resistance). You don't start slowing one POW down or speeding the other up if that means a sacrifice in other areas.




## AirSquirrels | 2019-03-19T16:02:59+00:00
Infrastructure outside of GPU or CPU chip is 1/10 of Capital cost to deploy.

If I’m a large farm I can put together more hashing power more than 10% cheaper than a small home miner every time - no matter whether CPU/GPU/FPGA/or ASIC. That is just how the current world economy works - buying in bulk, sweetheart deals with large buyers, etc.



## tarris034 | 2019-03-19T16:03:07+00:00
@MoneroCrusher not gonna repeat my self again and again.

## MoneroCrusher | 2019-03-19T16:23:21+00:00
@AirSquirrels I'd be **very** interested in how you achieve a 1/10 cost in CPU.
With GPUs very easy, every home miner can do it. Let me know how it can be done with CPUs, I wouldn't know of one single possible way.
@tarris034 you have never explained how you believe a GPU rig is not more cost-effective than a CPU rig for a home miner **in comparison to botnets and big datacenters**. Let me foreshadow: not possible

@JustFranz 

> After the kickstart function, is the reward fixed until the next kickstart? If its not fixed then why not have a fully dynamic chain that responds well? What is the point of the function? The kickstart period of one chain will have to be compared to the other, you can stack one side for the duration of the kickstarter function and suppress the other side.

It was a response to tevador's worry. He said in the case of one side dominating (which theoretically shouldn't happen from a hash/W perspective when both are equal) the hashrate that the other chain will be very small and not incentivized to "fight back" to gain back block reward share.
Thus I proposed to reset the reward algorithm all X blocks, so in the case this happen, this small minority chain always has the chance to re-establish itself.

> If one side of the POW ends up with a minority power/upkeep/hardware cost for their network then you can 51% the whole network much easier. Its best to ensure equality by making the rewards fixed and equal. This way the network will fill to mine it and reach an equilibrium that is close to breakeven with both sides spending an equal effort, that is the most secure. Your network is as secure as the weakest POW network, having them equal is the maximum.

I understand your point, however, if one of the two chains centralizes, then the centralized party is incentivized to lower their hashrate because they are entitled to a 50% reward no matter what they contribute, thus lowering the potential security on purpose for equal reward and less expenditure.
An all out competition will prevent this.
Why are you so worried about it? Do you believe one chain will dominate the other with same hash/W?

> Intel, Amd, ARM and all of the different generations of their CPUs? Same for GPU.

Well you just real-life test them and tweak them to be within **e.g.** 10% margin.

> Why even have one of the sides if it tends to get centralized? IF they can just take 50% off, that would indicate that they have some huge (read ASIC) advantage and they have inflated the hash rate so much that even the cheapest CPU/GPU miner is in the red several fold.

I'm saying IF it gets centralized, the network doesn't get weaker because then they won't take off hashrate because they lose money that way, this doesn't have to be ASIC. In the other scenario the hashrate gets taken off and network is more vulnerable to a short term attack.

## justinjja | 2019-03-19T16:24:30+00:00
@MoneroCrusher go spec out a server on dell.com.
https://www.dell.com/en-us/work/shop/productdetailstxn/poweredge-r7425

economies of scale wont beat the fact that server grade hardware is much more expensive than consumer grade stuff. Those servers are built to be highly reliable and redundant, all adding cost.

## tarris034 | 2019-03-19T16:31:06+00:00
We should make another thread for this discussion called 
"How to extend GPU mining without worrying about the network"

## MoneroCrusher | 2019-03-19T16:31:33+00:00
@justinjja for those Specs a home miner could probably do 50% off if he really optimizes. That's a 2x gain vs. datacenters (ignoring that they buy thousands of those and get a better price than listed on that website).

Now imagine what a 12x GPU system would cost in a server system with enterprise GPUs (costing $2000-3000 each that hash on Vega level). 
That's about $50000 for enterprise
and about $5000 for hobby
so a 10x optimization in cost efficiency for GPU rigs.

As I said, GPU mining is in a very unique position.
All said: I don't advocate to stop CPU mining, I just advocate to not stop highly decentralized and cost-effective GPU mining.

## AirSquirrels | 2019-03-19T16:35:50+00:00
If I go spec out a board that runs say 8 Ryzen Threadripper CPUs with nothing wired but UARTs, dimm slots, and a microSD card to boot a kernel off of + power supplies, the CPUs+Mem (compared to GPU+Mem) are easily 90% of the cost for me to build that board.  With a reasonable $1-2M farm scale investment, producing that board enmasse is no problem.

That is simply something a home miner can’t do. I’m not saying the home miner war is lost, I’m saying that bar none, large farm scale operation can beat it - and in a large enough coin they’ll be motivated to do it. Especially since the CPUs can just be removed from their slots and sold. 

## zexanana | 2019-03-19T16:40:15+00:00
I've read that botnets can only contribute to the hasrate up to a limit. They usually run on outdated software. Point can be made that a very sleek vulnerability in current software can be hacked to make a lot of current PCs mine for a malicious somebody. That was also true until today and is not a Monero specific risk, so we shouldn't worry about this scenario.
Server farms are welcome, in my opinion. There are thousands of them, are geographically distributed, they can serve other purposes (so their incentive will probably to mine while idle) and apart for the huge multi-national company ones, i think most of them won't have the hashrate to 51% attack. The big ones that might have sufficient power, let's not forget that this stuff has to be implemented by people, engineers, there is the risk of these companies being caught doing this which is probably not worth it for their image.
So I don't see botnets or server farms as a problem to RandomX.

This discussion has derailed because of your incessant will to ignore people's arguments because you want to protect your investment. You will still be able to sell your GPUs or keep mining on them. I will not comment anymore about this.

## justinjja | 2019-03-19T16:50:48+00:00
 50% off?

Most datacenters will be running a something like Dual Epyc 7601 with 512GB ram
(I'm being generous, most dataceners run Xeons)
That has a sticker price of $22,000 
Probably pay about 1/2 that in bulk.

Guessing that would have a hashrate of about 3500?
Vs a super cheap Ryzen 1600 build for about $250 that has a hashrate of about 500

EDIT: $22,000 before adding any disks lol

## MoneroCrusher | 2019-03-19T17:00:17+00:00
@AirSquirrels That's interesting. Thanks for the explanation. Didn't know that would be possible so cheap. 
@zexanana We're here for "Discussion of the future of the PoW algorithm" correct?

> "I've read that botnets" 

source?

I'm getting too tired of this.

The underlying base for everything is:
If you can safely allow GPUs, CPUs and FPGAs mining in equilibrium and competition or if you can allow CPUs only. Which one would you choose and why? Which one attracts more diversity? Which one has more inherent network effect? Ultimately, which one represents more decentralization & strength?

Think about it.

## AirSquirrels | 2019-03-19T17:02:59+00:00
I fail to see why we are discussing commercial grade datacenter deployment. If you are talking about existing data centers - cost is already spent and mining would be a supplemental way to get revenue from hardware when it is mining. 

No one is going to build a enterprise grade data center to mine monero. They’ll build new and spend the same money on to get cost effective hardware cheaper than a home consumer can with their gamer markup. 

The only person a home miner has a cost advantage against for new mining specific hardware is an idiot who spends money without thinking. Professional miners won't be doing that.



## tarris034 | 2019-03-19T17:03:18+00:00
Here are the current prices in my local shop if an amateur miner would like to build a mining rig

Gigabyte GA-A320M-H - 52.97 USD
AMD Ryzen 7 1700 3GHz - 264.85 USD
Transcend 4GB 2666MHz U-DIMM (JetRam) CL19 - 24.90 USD
iBOX Cube II 500W - 23.57 USD

366,29 USD / 4100 H/s = 0,089339024 USD per H


MSI B450 GAMING PLUS - 118.83 USD (the cheapest they sell with enough PCI-E)
AMD A6-9500 3.50GHz - 47.42 USD
MSI Radeon RX 570 ARMOR OC 8GB - 211.55 USD
MSI Radeon RX 570 ARMOR OC 8GB - 211.55 USD
MSI Radeon RX 570 ARMOR OC 8GB - 211.55 USD
MSI Radeon RX 570 ARMOR OC 8GB - 211.55 USD
MSI Radeon RX 570 ARMOR OC 8GB - 211.55 USD
Transcend 4GB 2666MHz U-DIMM (JetRam) CL19 - 24.90 USD (4GB was the smallest they sell)
iBOX Cube II 700W - 34.14 USD

1283,04 USD / 4000 H/s = 0,32076 USD per H

Cost of hardware:
**RandomX = 0,089 USD per H
CN/R on GPU = 0,320 USD per H** 

Power usage:
1x RX 570: ~85W
1x AMD Ryzen 7 1700: ~82W

**RandomX =  0,02 W per H
CN/R on GPU =  0,10 W per H** 


Source of performance figures:

https://github.com/tevador/RandomX
https://monerobenchmarks.info/

@MoneroCrusher add to this that CPU is much simpler to setup, no need to modify GPU firmware and tinker with drivers to get the best results.

## justinjja | 2019-03-19T17:06:12+00:00
@AirSquirrels home miners have advantages too.
No rent, no employees.

## MoneroCrusher | 2019-03-19T17:07:27+00:00
@tarris034 lol how can you even compare RandomX hashrate to CN/R? Different worlds.

## tarris034 | 2019-03-19T17:08:57+00:00
> @tarris034 lol how can you even compare RandomX hashrate to CN/R? Different worlds.

We were arguing what's more efficient for mining, clearly RandomX on CPU is much cheaper solution.

Unless you got some GPU PoW in mind. If so, give me a figure for RX 570 to recalculate.

## MoneroCrusher | 2019-03-19T17:21:10+00:00
You can't compare a CPU on a CPU algo to a GPU on a CPU/GPU algo.

Let me fix up your calculation for you:

> Here are the current prices in my local shop if an amateur miner would like to build a mining rig
> 
> Gigabyte GA-A320M-H - 52.97 USD
> AMD Ryzen 7 1700 3GHz - 264.85 USD
> Transcend 4GB 2666MHz U-DIMM (JetRam) CL19 - 24.90 USD
> iBOX Cube II 500W - 23.57 USD
> 
> 366,29 USD / 500 H/s = 0,732 USD per H
> 
> any generic mining MB with 12/13 slots - 80 USD
> Intel Celeron  - 30 USD
> 12x RX 570 4 GB - $150 ea
> 4GB RAM - 24.90 USD
> 2x 1200W Server PSU - 60
> 
> 1995 USD / 12600 H/s = 0,158 USD per H

This is for CN/R

## tarris034 | 2019-03-19T17:23:32+00:00
@MoneroCrusher just give me firgure for GPU PoW on RX 570 so we can get over it.
You are advocating for dual PoW one for CPU and one for GPU, obviously the one for CPU would be RandomX as of now, what's your GPU PoW in mind ?

## MoneroCrusher | 2019-03-19T17:25:00+00:00
You're confusing something. What I'm talking about is the compute to periphery ratio.
This is obviously better with GPUs since you can stuff 12/13 GPUs in a MB and you can't do the same with a CPU as a home miner.

## tarris034 | 2019-03-19T17:26:18+00:00
Speak numbers, give me the H/s on your GPU PoW, unless you want CPU PoW to be throttled to give incentive for GPU miners...

## JustFranz | 2019-03-19T17:26:22+00:00
@MoneroCrusher 
How will your dynamic block reward work?

> Well you just real-life test them and tweak them to be within **e.g.** 10% margin.

You can hash rate/w **normalize** the two algorithms for 1 piece of hardware each, at a certain voltage and certain frequency. That is it and that does not tell you anything. You are going to have to know/predict the whole mining network composition, do it based on that and ignore the fact that new hardware with different properties will get released in the future. What you are proposing can not be done.

You can not make the hashrate actually W **equal** for those 2 pieces of hardware for certain settings, firmware, OS and drivers.

>If one of the two chains centralizes,

Lets say monopolizes 

>then the centralized party is incentivized to lower their hashrate because they are entitled to a 50% reward no matter what they contribute

That half of the POW gets 50%. He is not guaranteed anything. You are talking about an ASIC like efficiency advantage, your POW has already failed. But lets continue and ignore the ASIC part.

You monopolize by outcompeting others. If a monopoly can reduce the hash rate and not hurt their profits (lets ignore those with free electricity mining too) then they have outcompeted those closest in efficiency several fold. Them being able to reduce hash rate and maintain same profits with no additional miners joining, that means the miner was providing too much security, consider the increased hash rate a freebie.

From a hash rate size point you already got the highest possible security that anyone could provide. The cheapest provider on earth is giving 100% of it. You can't buy more hash rate for the same money.

>thus lowering the potential security on purpose for equal reward and less expenditure.

Only if the miner is super efficient (ASIC like efficiency) and even then the whole mining reward couldn't buy you more hashrate from anywhere else. You can't ask the miner to give you more for less in return. The hash rate cutback by the ASIC monopoly does not change the security situation meaningfully. What they'll do instead on your dynamic POW is devour the other side too by inflating their hash rate even higher.

If its a normal market with GPU/CPU miners then any reduction will be met with an increase from somewhere else.

For a guy with a 1000 GPUs, you don't seem to get stuff or purposely don't.



## tarris034 | 2019-03-19T17:30:51+00:00
> For a guy with a 1000 GPUs, you don't seem to get stuff or purposely don't.

As far as we know he can be just a bad actor from other coin trying to mess things up for Monero.
(no offense, just saying)

Still waiting for the numbers and PoW you had in mind.
As far as I remember, there was a talk about CN/R for GPU and RandomX for CPU on this dual nonsense.

## justinjja | 2019-03-19T17:36:23+00:00
No tinfoil hats are needed to explain MoneroCrusher.
He just looks like a gpu miner and a Monero fan.

## tarris034 | 2019-03-19T17:38:35+00:00
> No tinfoil hats are needed to explain MoneroCrusher.
> He just looks like a gpu miner and a Monero fan.

He does not need to prove anything. If he says he got X GPU's, lets talk about people with X GPU's. Does not need to be one of them.

## MoneroCrusher | 2019-03-19T17:58:50+00:00
@tarris034 You're still confusing stuff. Irrespective of hashrate (which doesn't matter at all since I'm assuming normalized hash/W), the compute to periphery ratio will be better with GPUs than with CPUs (since you can stuff $5000 worth of Vega GPUs in one $80 motherboard very cheaply).
I said this sentence 3 times now I think, what's hard to understand about it?
Please tell me so I know and can explain you again.

@JustFranz 
I already explained it but I'll gladly do it again:
It will somewhat be similar to the difficulty algo (using x blocks of the past and calculating normalized hashrate with the constant we talked about before to arrive at proportions, each chain is contributing in raw power (Megawatt)).
The algo then continuously with every new block adjusts the reward according to how much power is provided by each chain.

Let's say CPUs provide 30MW (or normalized hashrate) of power and GPUs Provide 30MW (or normalized hashrate) of power, then the reward is split 50/50 between GPUs and CPUs.

> You can not make the hashrate actually W equal for those 2 pieces of hardware for certain settings, firmware, OS and drivers.

Yeah you most definitely can within some margin, that's why I said e.g. 10%
New hardware grows across the board, not just one manufacturer, so no readjustment needed, it's mostly just shrinking processes (12 nm, 7 nm etc).

> That half of the POW gets 50%. He is not guaranteed anything. You are talking about an ASIC like efficiency advantage, your POW has already failed. But lets continue and ignore the ASIC part.

Replace "your POW" with RandomX or CN-R-Memory-hardness because that's what I proposed.
You completely ignore that I say the centralization likely wouldn't happen but it's just there as a security measure that in the unlikely case it DOES happen you won0t have this scenario.
Why do you want 50/50 split in the first place?
If we can achieve same hash/W across the board, wouldn't you want competition between those hash/W devices? Why would you want to segregate them? I don't see the benefit.



## tarris034 | 2019-03-19T18:00:01+00:00
> You're still confusing stuff. Irrespective of hashrate (which doesn't matter at all since I'm assuming normalized hash/W), the compute to periphery ratio will be better with GPUs than with CPUs.
I said this sentence 3 times now I think, what's hard to understand about it?
Please tell me so I know and can explain you again.

Normalized = throttled right ? so you want CPU to be less efficient so GPU can still mine ? 

## MoneroCrusher | 2019-03-19T18:00:51+00:00
No, that's not what I said at all

## tarris034 | 2019-03-19T18:01:22+00:00
> No, that's not what I said at all

Define normalization because there are different methods.

## MoneroCrusher | 2019-03-19T18:04:17+00:00
Compute to periphery ratio means how much money you have to spend in pure computing power vs. "accesoires" like RAM, MB, cables etc.
Which is around 1:10 with GPUs for home miners and RX 570 and around 1:20 for Vega rigs

## tarris034 | 2019-03-19T18:05:37+00:00
> Compute to periphery ratio means how much money you have to spend in pure computing power vs. "accesoires" like RAM, MB, cables etc.
> Which is around 1:10 with GPUs for home miners and RX 570 and around 1:20 for Vega rigs

I have added power usage as well to my calculations: https://github.com/monero-project/meta/issues/316#issuecomment-474471530

Which algo would you like for GPU ?

## MoneroCrusher | 2019-03-19T18:06:41+00:00
No, I do not basically want throttling. Read through the posts and think. I'm not endlessly repeating myself
I would love to see CN-R-Memory-Hard as a GPU algo and RandomX as CPU algo. And no, CN-R-Memory-Hard doesn't exist.

## tarris034 | 2019-03-19T18:08:42+00:00
> No, I do not basically want throttling. Read through the posts and think. I'm not endlessly repeating myself
> I would love to see CN-R-Memory-Hard as a GPU algo and RandomX as CPU algo. And no, CN-R-Memory-Hard doesn't exist.

Lets stick to what is available at the moment.

## WhyIsThisSoSlow | 2019-03-19T18:10:53+00:00
Why are you guys even discussing stuff like this? Making this thread harder to read by providing chat-like responses is not helping anyone.

Please @MoneroCrusher document your ideas somewhere and present a paper of the new algo that you invision. After you have it ready with solid concepts that have not failed already for other coins you can propose it to the community. Or you can open e separate topic to develop it further. Until it is ready, there is no point of this discussion and proposition in this topic.





## tarris034 | 2019-03-19T18:12:51+00:00
@WhyIsThisSoSlow I agree with you we made too much spam here talking about wind.
But the thread is titled "**Discussion** of the future of the PoW algorithm"
So we are discussing.

BTW 50/50 reward split could be abused for X blocks, it's not a good solution.

## justinjja | 2019-03-19T18:24:05+00:00
Explain this please? "50/50 split could be abused for X blocks"

## tarris034 | 2019-03-19T18:25:18+00:00
> Explain this please? "50/50 split could be abused for X blocks"

Lets say we take into account 100 blocks for normalization, bad actor could switch between PoW's, increase it on the one side then mine on the other before next normalization comes into play.

Mainly that's why we've seen ASIC hashrate fluctuation, they have played with the diff to earn more.

## justinjja | 2019-03-19T18:28:04+00:00
Oh ok, I though you were talking about alternating, not parallel

## WhyIsThisSoSlow | 2019-03-19T18:28:54+00:00
I totally agree with you guys as discussing things will always attract improvements, but this is not the place/topic to develop and discuss new hypothetical algorithms. You guys have been mostly off topic for hours now and added so many irrelevant spam to this that the main ideas have been buried under. Please open a new topic for this and stop treating this thread as an Chat/Irc channel.

## MoneroCrusher | 2019-03-20T07:52:09+00:00
As you can see in OP, dual PoW is a proposed solution for the future of PoW, so we discussed that. But I agree it should go from chat-like to thought-out post-like.

## tevador | 2019-03-22T14:53:37+00:00
RandomX 0.3.3 has been released with significantly improved verification performance.

I have compared the performance of 4 different machines in CN/R (current Monero PoW) and RandomX.

|CPU|Architecture|RAM|OS|AES|
|---|------------|---|--|---|
AMD Ryzen 7 1700|x86_64|16 GB DDR4|Ubuntu 16.04|HW|
Intel Core i7-8550U|x86_64|16 GB DDR4|Windows 10|HW|
Intel Core i3-3220|x86_64|2 GB DDR3|Ubuntu 16.04|software|
Raspberry Pi 3|armv7l|1 GB DDR2|Ubuntu 16.04|software|

These machines should be a good testing sample representing low-end, mid-range and high-end systems.

For RandomX, I used version 0.3.3: https://github.com/tevador/RandomX
For CN/R, I used xmrig version 2.14.1: https://github.com/xmrig/xmrig

RandomX has 2 modes: "light" mode requiring 256 MiB of memory and "full" mode, which requires 2 GiB of memory.

### Single threaded performance

Table lists the performance using 1 CPU thread.

|CPU|CNv0|CN/R|RandomX (light)|RandomX (full)|
|---|----|----|---------------|--------------|
AMD Ryzen 7 1700|70 H/s|68 H/s|68 H/s|590 H/s|
Intel Core i7-8550U|79 H/s|74 H/s|94 H/s|770 H/s|
Intel Core i3-3220|29 H/s|26 H/s|78 H/s|-|
Raspberry Pi 3|3.1 H/s|1.0 H/s|3.2 H/s|-|

### Multi-threaded performance

The number of threads was selected for maximum performance (hashes per second).

|CPU|CNv0|CN/R|RandomX (light)|RandomX (full)|
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

|CPU|CNv0|CN/R|RandomX (light)|RandomX (full)|
|---|----|----|-----------|--------------|
AMD Ryzen 7 1700|31 minutes|32 minutes|31 minutes|28 minutes|
Intel Core i7-8550U|65 minutes|84 minutes|135 minutes|38 minutes|
Intel Core i3-3220|400 minutes|400 minutes|95 minutes|-
Raspberry Pi 3|26 hours|79 hours|24 hours|-|

In this case, there is a large difference especially for low-end machines without hardware AES, where RandomX is much faster than CN/R even in "light" mode.

### Time to verify a new incoming block

This is important in case of a DoS attack attempt and also for pools, which have to verify a large number of hashes.

|CPU|CNv0|CN/R|RandomX (light)|RandomX (full)|
|---|----|----|-----------|--------------|
AMD Ryzen 7 1700|14.3 ms|14.7 ms|14.7 ms|1.7 ms|
Intel Core i7-8550U|12.7 ms|13.5 ms|10.6 ms|1.3 ms|
Intel Core i3-3220|34.0 ms|38.2 ms|12.8 ms|-|
Raspberry Pi 3|320 ms|1000 ms|310 ms|-|

In this case, RandomX is faster across the board, allowing much faster verification for higher-end systems and systems without hardware AES.

I hope this helps to alleviate some of the concerns about the performance of RandomX.

## tevador | 2019-03-22T16:24:23+00:00
I have added results for CNv0 (original CryptoNight) to the tables above.

## timolson | 2019-03-22T17:25:57+00:00
> Whatsminer = 33TH/s and uses 2150W = 65W/th
> S15 = 28TH/s and uses 1600W = 57W/th
> bitmain looks better?
> 
> Am I looking at the wrong miners @timolson

That Whatsminer unit is a 16nm process, and you’re comparing it to Bitmain’s 7nm chip.  The fact that the two are anywhere close to each other says that Whatsminer has much better engineering.  When Whatsminer decides to move to 7nm, they will be well ahead of Bitmain.  It was a smart economic/business choice to start at 16nm until they ramp up sales and revenue...

And to whomever was saying that ASIC’s are not commoditized, WTF? There are now many vendors, and the margins are thin. That’s the very definition of a product being commoditized.

## AirSquirrels | 2019-03-22T17:43:36+00:00
@timolson what I have been hearing is the move to 7nm is at most 15% more efficient. That seems to be reflected in your numbers. 

## timolson | 2019-03-22T17:53:09+00:00
Economics of GPU/CPU Mining

There was a lot of noise and misinformation about prices for industrial miners vs home miners.

I’ve run medium-to-large scale mining operations with both GPU’s and CPU’s and there is no way for a home user to come close to industrial mining costs.  Not for equipment, not for power.  Not for CPU’s or GPU’s or ASIC’s.  Whoever quoted Dell prices on hardware is insane.  Miners use the cheapest equipment they can get, and they buy it for much cheaper than you can get it retail.  Their power and cooling is cheaper, too.

The PoW and whether it’s a CPU, GPU, or ASIC has little to no bearing on the economies of scale achieved by big miners. You cannot save home mining by changing the PoW.

The fact is that home miners who think they’re profitable almost always ignore their labor or electricity costs, or they don’t depreciate their hardware, or some other accounting trick.  You might think you’re making money mining, but probably you’re in the red if you actually keep accurate accounting.

If RandomX does turn out to be ASIC-resistant, large miners will simply print big mobos with lots of CPU’s on them.  It is not nearly as difficult or expensive as someone mentioned.  In fact, altASIC might build and sell such a thing if the devs won’t go aggro on us for doing so.  But one of those multi-CPU units would be much cheaper capex than your gaming machine.  MUCH cheaper.  So it’s not like an ASIC-resistant PoW would stop large miners from having better/cheaper equipment and significant economies of scale compared to home miners.

A lot of people seem to think that an ASIC-resistant PoW will save the profitability of home mining.  I don’t agree at all. Economies of scale exist whether it’s CPU’s or ASIC’s.  Even if your capex is the same as big miners’, you don’t have 3¢ power, do you? Oh you’re lucky and have 5¢ power? Sorry, big miners still save 40% compared to you.

All this talk of stopping big miners and saving home mining is simply a fantasy.  Home mining can never compete with large scale mining. It’s a law of economics you learn in your first semester.

## AirSquirrels | 2019-03-22T17:59:48+00:00
@timolson 100% on point on every point. This echos what I have also said in this thread.

## timolson | 2019-03-22T18:03:28+00:00
> @timolson what I have been hearing is the move to 7nm is at most 15% more efficient. That seems to be reflected in your numbers.

Putting a simple performance number on a process jump is too simplistic, but if I had to do it, I’d say it’s closer to 30%.  Bitmain’s S9 to S15 is a jump of 100 W/TH down to 57 which is more than 40%.

If we compare Whatsminer’s current 16nm chip against Bitmain’s S9, which is Bitmain’s best 16nm chip, the S9 gets around 100 W/TH compared to Whatsminer’s 65, using the exact same manufacturing process.

Whatsminer has the tech.  Mark my words.  Bitmain dominance is ending.

## tarris034 | 2019-03-22T18:29:54+00:00
@timolson 

Having a PoW that is almost literally converting any home computer into a specialized ASIC mining machine with no investment aside from electricity bill brings much more decentralization to the network and even big scale mining operations won't stop small miners incentive from having even the slightest chance of earning something out of their idle CPU cycles.
 *You mean by running this app in background I get free pizza every week/month? I'm in!*

Going large with RandomX will be even harder than it was to this day with CPU/GPU mining PoW, the largest mining farm that I've seen had 4000 GPU's (genesis mining, if real) - that's only 3 MH/s on 750 H/s per card performance on all current and past PoW's if they used something similar to RX 470.

So going anti-ASIC will indeed save home mining, as it was doing to this day.

And by home mining I'm thinking small to medium mining operations as well, with ASIC PoW there will be much more incentive for big mining operations as we have already seen on Bitcoin, when even largest mining operations struggle to get any ROI and often bankrupt.

On RandomX there's much less chance of farmers going bankrupt, even big ones as data centers as they did not invest any money and are using the hardware they already had laying around in dust when idle.

Unless you got some much bigger than 4k GPU's mining farm example today to abolish my opinion and more than one or two of them.

*PS, when I asked genesis mining what GPU they used on their live chat, their representative by the name of "Betty" first linked me to their "Technology" site where I could find that info, then when I told there's no such info she said she don't know what GPU they are using, that's why I said *if real*.  

>The fact is that home miners who think they’re profitable almost always ignore their labor or electricity costs

ALL miners of small to medium capacity that I know are **very** aware of their costs and risks.
If someone is contributing to the network at 0 profit or even red zone, it's not bad for the network in anyway.

>If RandomX does turn out to be ASIC-resistant, large miners will simply print big mobos with lots of CPU’s on them.

Nothing new, we've seen mobos with 20 GPU's support like ASUS B250, it didn't broke home mining.
Actually, it made it even stronger.

As I see it, ASIC-friendly PoW put's the whole network on a ROI mercy as opposed to CPU PoW which could be run by everyone today.

I'm not saying only CPU/GPU PoW is good and ASIC are all bad and ugly.
But I'm yet to see some validation for it as I've read all pros and cons in this thread and some other places and I'm still not convinced enough to make such radical move aside from being forced by ASIC companies that constantly attack our network.

I'd say, lets give as much time as possible for developers to polish RandomX and see it in action before surrendering this war. If the performance of ASIC will be close to the predicted numbers, we have nothing to worry about.

## OrvilleRed | 2019-03-22T20:30:17+00:00
> I’ve run medium-to-large scale mining operations

Thank you for posting here. I appreciate the resulting the signal-to-noise increase.

> You cannot save home mining by changing the PoW.

I don't think saving the family cryptofarm is the goal here.

I  think the goal is to protect the network from any one attacker, by virtue of decentralization via maximal commoditization.

From what you say, it sounds to me like RandomX may be acheiving that.



## tarris034 | 2019-03-22T21:02:56+00:00
@denisgoddard 
Talking about noise, it's already been said many times in this thread that this is all about keeping the network secure and not about investments people have made or about giving chance to small miners.


## timolson | 2019-03-22T23:47:14+00:00
>I don't think saving the family cryptofarm is the goal here.
>
>I think the goal is to protect the network from any one attacker, by virtue of decentralization via maximal commoditization.

Agree 100% here, but...

> From what you say, it sounds to me like RandomX may be acheiving that.

Absolutely not.  Let's assume RandomX works and everyone must use a CPU to mine.  CPU's are a highly centralized market, with basically only AMD, Intel, and ARM as competitors.  Two of these companies are located within a mile of each other in Santa Clara, California, while ARM is in Cambridge, England.  Is that what you call decentralization?

CPU's are very complex and difficult to build, so only a few large companies can even try.  Building an ASIC miner is not even 1% of the work compared to making a CPU, which allows many more companies to enter the market.

If you really do need a CPU-complexity chip to mine RandomX, then what happens when AMD uses their considerable IP in CPU's and GPU's to release the Radeon RandomX, while at the same time Bitmain can't compete, nor can InnoSilicon or Obelisk or Halong or BitFury or WhatsMiner... We already have competition from multiple continents in the ASIC miner market, and it's still young.  Why destroy that by moving to an AMD/Intel duopoly?

Binding the PoW to CPU's is a step backwards in terms of competition, and it's a huge gamble in terms of RandomX being a complex PoW that could harbor secret optimizations.

If we are talking about commoditization of industrial miners, then an easy-to-implement ASIC-friendly PoW like Keccak will result in the most commoditized market conditions, because any chip maker can compete, not just the behemoths.  If the PoW is simple and hardware-friendly, there will be lots of competition with similar hashrates.

## hyc | 2019-03-23T02:01:26+00:00
> If we are talking about commoditization of industrial miners, then an easy-to-implement ASIC-friendly PoW like Keccak will result in the most commoditized market conditions, because any chip maker can compete, not just the behemoths. If the PoW is simple and hardware-friendly, there will be lots of competition with similar hashrates.

This is still a fantasy. Assuming that the algorithm is an even playing field, and there are no optimizations to be made, the behemoths still have economies of scale that will decrease their production costs, that the smaller chip makers will never be able to compete with.

But both of these assume that the behemoths actually care enough to participate. It's not clear to me that they care. Granted, GPU mining as a huge chunk of Nvidia's revenue and the lack of it last year took a large dent out of their profitability, but Nvidia is also a lot smaller than Intel.

The fact that Intel and AMD dominate with x86 hasn't prevented IBM from still making a profit on POWER, and SPARC and MIPS systems still exist as well. It's far from a locked in duopoly, and all of these players in the CPU market have been far more honorable in their business practices than e.g. bitmain. (Well, ok, except for the anti-competitive crap that Intel keeps pulling to sabotage AMD...)

## zexanana | 2019-03-23T04:15:25+00:00
This is a trade-off between manufacturer decentralization and hardware decentralization no? On the one hand, you might have some more manufacturers (you won't have many, it's still a very capital intensive business). On the other, there will be few large and very large mining companies/operations.
Comparing to RandomX, you will have the AMD/Intel duopoly but then you have many more possible miners which already have the hardware available to them. Every office, data center, university and the home miner will have the opportunity to mine.
I think hardware decentralization is worth more than manufacturer decentralization, especially because with RandomX, the hardware is CPUs. AMD/Intel have no incentive to harm the network because they would be losing customers. There is no risk of "banning" CPU manufacturing because the world runs on them. Also, if RandomX is successful, then your "Radeon RandomX" GPU argument is not valid because this is simply a more advanced processor. As it has been said, there are only so many things you can strip from a normal CPU and these optimizations are the 2x improvement we are talking about (as a worst estimate).

> [...] and it's a huge gamble in terms of RandomX being a complex PoW that could harbor secret optimizations.

This is my main concern, which basically means RandomX fails. It is worth a try in my opinion

## tarris034 | 2019-03-23T05:42:11+00:00
Never seen ASIC in any local hardware shop, they are available only in some Internet shop specific ASIC importers with long delivery times or *out of order* sign.
*did not check the junkyard, might be full of them*

I can buy CPU/GPU in **every** hardware shop, in any country.

Still did not see any valid reason for going ASIC-friendly, aside from long term speculations, theories and conspiracies.

*x86 centralization.. ASIC companies living in a harmony... give me a break*

## tevador | 2019-03-23T10:31:10+00:00
>  CPU's are a highly centralized market, with basically only AMD, Intel, and ARM as competitors. Two of these companies are located within a mile of each other in Santa Clara, California

Intel and AMD are publicly traded companies and are subject to much higher scrutiny and regulation than semiconductor startups in China. I'm sure their shareholders would not be very happy if Intel decided to for example apply KYC to their CPUs.

>  what happens when AMD uses their considerable IP in CPU's and GPU's to release the Radeon RandomX

The annual mining revenue of Monero is less than $40 million, which is about 0.6% of AMD's annual revenue ($6.5 billion in 2018). AMD can make a lot more money in the server market and their Zen CPUs are already very efficient at RandomX. They have basically nothing to gain from designing specialized hardware for mining.


## MoneroCrusher | 2019-03-23T10:56:29+00:00
So what stops anyone from building huge ARM A53 SoC low-power clusters that will leave both AMD and Intel CPU owners in the dust?
Those won't ever be accessible in your newegg.com store. With GPUs however, it's a whole different story, I don't see any efficiency gains that big players have over smaller home miners in GPU mining. For sure more effective setups, cheaper cooling, and cheaper electricity on the other hand they also have big rent, labour cost, taxes and other considerable costs associated with running a large-scale setup.

After all this discussion I still believe if we have many types of commodity hardware competing against each other, we'll have the most robust & healthy mining ecosystem, which could be accomplished with a dual PoW, if executed properly:
FPGAs, GPUs, CPUs will all be fairly competing and a natural equilibrium will establish.

RandomX for CPUs
Cryptonight-R-GPU (_or alternatively ethash_) for GPUs and FPGAs

@tarris034 that was a response to @timolson 's GPU/CPU are the same post (from home miner to megafarm perspective). Please stop commenting every my post if you have nothing useful to add, I'd rather see your post as spam, than mine which is a response to another poster's arguments.

## tarris034 | 2019-03-23T11:10:43+00:00
@MoneroCrusher we have already talked about pros and cons of dual PoW and GPU PoW.

Now you're just pushing your agenda to extend your mining operation, please stop it as it becomes only spam.

You have added nothing to the discussion we already had and this is not private discussion but public so I can and will comment on every spam you make.

## tarris034 | 2019-03-26T16:47:33+00:00
ASIC companies shitting their pants and claiming unrealistic designs (Sonia-Chen) on RandomX thread:
https://github.com/tevador/RandomX/issues/31

Grab some popcorn, It's getting hilarious.

BTW, her company was recently accused of 51% attack on one of the coins.
*nice people, good people*

## WhyIsThisSoSlow | 2019-03-26T17:12:08+00:00
Interesting discussion over-there but Sonia`s intentions seem to be shady based on how she will not be on point most of the time.

This interview is also interesting:

https://www.youtube.com/watch?v=ZZZF4BqIDrk

Kristy Leigh Minehan (OhGodAGirl) has some interesting ideas regarding decentralization.

I am especial interested if her idea of adapting the Monero PoW to only allow a list of valid CPU/GPU ID`s . This should be a valid solution for decentralization moving forward after RandomX.  In short, based on what she said, a PoW could be created to only allow known CPU or GPU with valid ID`s as miners and reject anyone else. This would be a way to ensure only decentralized/commodity hardware is used and added on the network. 

I am personally in doubt that those ID`s can not be spoofed but i do not have much knowledge in that exact area.

I would love a new topic on this if you guys find it plausible.


## hyc | 2019-03-26T17:16:46+00:00
@WhyIsThisSoSlow no, using chip IDs is pure garbage. https://twitter.com/hyc_symas/status/1109509488091062272

Most of her suggestions in that interview were garbage.

## tarris034 | 2019-03-26T17:19:31+00:00
> To those who want monero to be ASIC friendly: What do you think about ASIC importation banning in some countries ? Is that not an issue ?

*Report Links 74% of Bitcoin Mining to China, Sees Threat to Network*
https://bitcoinmagazine.com/articles/report-links-74-bitcoin-mining-china-sees-threat-network/

Going ASIC-friendly will centralize the network, as it was discussed in this thread with pure logic and as seen in real life scenario on other coins which are already ASIC-friendly.

ALL (if i'm correct) ASIC companies that are into mining are based in China, that means China companies/citizens got the best deal due to lack of import tax, so any big player who will want best deal will create mining facility in China. Why it's bad ? for once, because we are at the mercy of their government which are known for being brutal in many aspects, not only crypto.

@WhyIsThisSoSlow 
>Interesting discussion over-there but Sonia`s intentions seem to be shady based on how she will not be on point most of the time.

Exactly, she is too smart to make such stupid claims.

## WhyIsThisSoSlow | 2019-03-26T17:20:06+00:00
@hyc 
Good to know then! Sounded to good to be true. 

## timolson | 2019-03-26T17:43:42+00:00
> idea of adapting the Monero PoW to only allow a list of valid CPU/GPU IDs

Just drop the blockchain part and use SGX.

FFS what has the crypto community come to? Pushing for device ID’s and a two-manufacturer CPU duopoly?

## tarris034 | 2019-03-26T17:50:27+00:00
> > idea of adapting the Monero PoW to only allow a list of valid CPU/GPU IDs
> 
> Just drop the blockchain part and use SGX.
> 
> FFS what has the crypto community come to? Pushing for device ID’s and a two-manufacturer CPU duopoly?

Going this track of thinking the best PoW would be one that signs job with our government issued ID number, just to make sure it's decentralized as much as possible and free of ASIC.

## timolson | 2019-03-26T17:55:57+00:00
@tarris034 
> Report Links 74% of Bitcoin Mining to China

And 0% of CPU’s are made in China. 100% of CPU’s, both Intel and AMD, are made in the USA or in close allies Israel and Ireland*.

I’m starting to wonder whether you actually care about decentralization, or whether you just hate China.


> ALL (if i'm correct) ASIC companies that are into mining are based in China

That’s an absurd claim to put in writing...



\* some fraction of AMD’s new 7nm CPU’s will move to TSMC for the first time in 2020.

## tarris034 | 2019-03-26T18:02:21+00:00
>And 0% of CPU’s are made in China. 100% of CPU’s, both Intel and AMD, are made in the USA or in close allies Israel and Ireland.

But still, you can buy them anywhere in the world for practically the same price.
https://www.extremetech.com/computing/273063-amds-chinese-joint-venture-now-shipping-homegrown-x86-cpus

>I’m starting to wonder whether you actually care about decentralization, or whether you just hate China.

Would be hard to hate China as I'm writing on Chinese made keyboard wearing Chinese clothes and eating Chinese food, I'm basically living in China.
I'm starting to worry for Chinese government, if they stop exporting, I will die naked out of starvation.
..Oh wait, they not the only one producing food and clothing. Can't be said the same about ASIC miners.

>That’s an absurd claim to put in writing...

Could you link here some proofs of other countries involved in building their own ASIC for mining?
Still it's not that much of issue for one country origin, the problem here is the import tax, add to this the cheap energy and all of the big players will make their facilities in China, as always.

## timolson | 2019-03-26T18:25:15+00:00
I know of at least two North American mining operations that have cheaper power than anything in China.

US ASIC manufacturers include Obelisk and Mineority.  Genesis Mining has a big presence in Iceland. Russia is building SHA chips, and GMO of Japan started such a project but cancelled. I also know of a BTC chip being designed in South America... When Venezuela recently had major power outages, the number of BTC transactions dropped significantly: That’s usage not mining, but my point is that cryptocurrency interest and usage is global.

This whole “China owns crypto mining” narrative is just not true.  Also, no one seems to be distinguishing Taiwan and China.  Maybe they reunite someday but currently almost all mining ASICs are made in Taiwan, not China...

## timolson | 2019-03-26T18:57:14+00:00
@tarris034 
> https://www.extremetech.com/computing/273063-amds-chinese-joint-venture-now-shipping-homegrown-x86-cpus

This article you quoted has some important points for CPU-lovers to consider:

- Only Intel and AMD have the IP to build a modern CPU
- AMD can only compete with Intel because it gained a license for x86 in a lawsuit.
- Special legal entities were required for AMD to be allowed to build China-domestic CPU’s
- These CPU’s are basically identical to AMD’s own brand, and China cannot make them independently of AMD’s IP, which is subsequently tied to Intel’s x86 IP
- A huge part of CPU design is what’s called Physical Design which is how you lay out the circuitry for a specific foundry process.  AMD will have done all their physical design work for Global Foundries in the US.  If China wants to make the chips domestically, a new physical design is almost certainly required, and this physical design work is a big reason why AMD and Intel have fast CPU’s. RandomX needs this physical design process to be big and complicated for its CPU-device-binding to work economically.  Either RandomX works and all miners (CPU’s) are made in the USA under strict legal conditions, or RandomX doesn’t work and fast miners can be made anywhere.

All of this screams centralized control to me.  The US owns CPU’s and is not about to let that dominance go.

## JustFranz | 2019-03-26T19:09:46+00:00
@WhyIsThisSoSlow The device ID thing would only work if the only miners in existence were:
1. Released by a central authority
2. Closed source
3. Heavily obfuscated piece of software running in a VM like VMProtect3
4. That software created encrypted POW block candidates in a "secure" environment, those can only be decoded and verified by a black box central server(s), then the blocks are distributed to the rest of the network.

This works until the program gets unpacked and reverse engineered. You also kill the decentralized crypto coin with this.
You can also lie to the black box software doing the mining.


How can an expert like her spew garbage like that and exhibit magical thinking to this extreme degree? A bullet intercepting drone mining Monero to pay for itself? WTF? A bullet intercepting drone, WTF? In police CQC environments? And it worked by flying itself into the path of it? What is it made of, how fast is it? Can we make an ERC-20 token for it?

## justinjja | 2019-03-26T19:15:53+00:00
@timolson 
ARM, RISC-V, MIPS Open... They aren't Intel/AMD, but certainly way way larger than minority (basically scammers btw) and Obelisk.

## WhyIsThisSoSlow | 2019-03-26T19:17:22+00:00
@timolson 

This is just getting silly at this point. Its not about where they are made, its about how easy you can get them and how hard would it be for them to get restricted. As you might know Intel/AMD/Any other proper company, have regulations and can not be compared to unregulated private Chinese companies in any way.

Your are basically comparing oranges to apples. As long as these mining ASIC are not a commodity, they will be a threat to decentralization and freedom.

@JustFranz 
That drone part was really funny. 
I only liked the concept of those iD`s preventing ASIC`s in a way, but was skeptical of the entire thing as well.









## tarris034 | 2019-03-26T19:47:21+00:00
Let's also stop talking about Intel/AMD/IBM/Other x86 manufacturer monopoly here, those are big companies competing with each other and at least we know for sure they will not be banned as they are not made for specific usage.

## timolson | 2019-03-26T19:49:15+00:00
> ARM, RISC-V, MIPS Open...

I do not think any of these will be competitive, assuming RandomX works. We’ll have Intel and AMD and that’s it.  I can technically write a CPU in under a month, too, but that doesn’t mean anything. Intel and AMD have vast amounts of IP and patents which not only make their chips fast but also legally prevent competition from entering the CPU market. Even if I knew how to compete with them, AMD and Intel could sue me out of business before I even started.

It sounds like you people simply trust AMD and Intel to be nice. WTF?

Just admit this is not about decentralization. It’s about keeping it so your home CPU can make a few cents each month. “ASIC’s = bad because I don’t have one.”

Think like a large miner who CAN make their own chip. Why would a large miner want their upstream supplier to be pinned to two large US corporations? Never. You’d want control over your supply chain. Which Venezuelan revolutionary is pushing for US control of crypto mining?

## tarris034 | 2019-03-26T19:51:57+00:00
@timolson can't find any of the mentioned companies by you having ASIC miner for sale, I have found only some pre-orders.

So It's still only one country of origin, also lets not mention Genesis mining here, they have very bad reputation and they couldn't answer me even one simple question what kind of GPU's they are using.

>Just admit this is not about decentralization. It’s about keeping it so your home CPU can make a few cents each month. “ASIC’s = bad because I don’t have one.”

Let's keep it professional and talk about the facts. The intentions could be this or other for everyone in this discussion, it shouldn't really matter.

What matters is the security of the network, and still can't see why some unknown small company making simple ASIC chips should be trusted on the same level as Intel/AMD/IBM.

The discussion in the linked tevador thread with one of the ASIC manufacturer is not helping their reputation, trying to discourage the development by claiming how easy they can make RandomX ASIC, easier than the one for Bitcoin. 

## JustFranz | 2019-03-26T22:36:56+00:00
Aslo, all of you should know that there is a post meeting version of this discussion and we should concentrate on the issues brought up in it https://github.com/monero-project/meta/issues/321

This one is a mess and should be archived.

## jwinterm | 2019-03-27T00:29:15+00:00
How can you not find obelisk? This is literally the first result if you
search for "obelisk ASIC":  
https://obelisk.tech


Also, Bitfury is a very large bitcoin ASIC company based in Georgia that
doesn't sell directly to the public, but they work with hut-8 which is a
publicly traded Canadian company that mines with bitfury hardware and
hydroelectric power in Canada.

On Tue, Mar 26, 2019, 12:52 tarris034 <notifications@github.com> wrote:

> @timolson <https://github.com/timolson> can't find any of the mentioned
> companies by you having ASIC miner for sale, I have found only some
> pre-orders.
>
> So It's still only one country of origin, also lets not mention Genesis
> mining here, they have very bad reputation and they couldn't answer me even
> one simple question what kind of GPU's they are using.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/meta/issues/316#issuecomment-476820533>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AFrhk36sHztXcxC2PWMXCVjAoyD6bJ7Wks5vanpggaJpZM4bqRg6>
> .
>


## tarris034 | 2019-03-27T08:12:22+00:00
I've been on their site, can't find any order option.

## SamsungGalaxyPlayer | 2019-03-28T04:25:23+00:00
@johnny1021 as discussed earlier in this issue, you are describing the status quo. The Monero community already forks to remove ASICs when found. The previous upgrade was moved forward a month to specifically address this. I do not understand how this proposal is different than anything else that MoenroCrusher and others have already suggested ('game theory').

There are many moving parts in an upgrade, more than just changing the PoW algorithm. It's not feasible to expect such quick turnarounds from the Monero ecosystem at its current size, let alone if it grows larger. This leads to undesirable consequences to Monero contributors and the rest of the ecosystem.

## johnny1021 | 2019-03-28T05:13:57+00:00
@SamsungGalaxyPlayer Sorry, I didn't look through all the comments. Please ignore my suggesion. Sorry for the interrupt. I will delete my comment then.

## SamsungGalaxyPlayer | 2020-03-10T20:41:36+00:00
@dEBRUYNE-1 can you please close this? We can open a new discussion if we want to revisit this for a future upgrade imo.

# Action History
- Created by: dEBRUYNE-1 | 2019-03-12T07:58:22+00:00
- Closed at: 2020-06-05T15:26:05+00:00
