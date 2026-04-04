---
title: Schedule meeting to discuss the future of the PoW algorithm.
source_url: https://github.com/monero-project/meta/issues/315
author: dEBRUYNE-1
assignees: []
labels: []
created_at: '2019-03-11T11:46:54+00:00'
updated_at: '2020-03-09T21:40:47+00:00'
type: issue
status: closed
closed_at: '2020-03-09T21:40:47+00:00'
---

# Original Description
I think we can all agree the current strategy of periodically tweaking the PoW algorithm is not working and is even potentially dangerous. As such, we have to come up with a long-term strategy. This meeting is meant to merely discuss our options and not yet make a decision. I do think, however, that if we make a decision, we should pre-commit to a timeline. This removes any future friction and uncertainty and allows us to focus on the protocol. 

Regarding the date, I have a few suggestions:

Saturday March 16 - 17:00 UTC
Sunday March 17 - 17:00 UTC
Saturday March 23 - 17:00 UTC
Sunday March 24 - 17:00 UTC

Perhaps we should also add a suggested date that is a non-weekend day? 

# Discussion History
## el00ruobuob | 2019-03-11T12:01:45+00:00
If i am correct, there is a community workgroup meeting this saturday march 16th, isn't it @SamsungGalaxyPlayer ?  
On Sunday March 24th, is a dev meeting already, quoting @rehrar on yesterday's meeting: `<rehrar> Next weeks is community meeting, and we want to be desynced from them, so next meeting two weeks?`

We could add the subject to the 16th community meeting (usually heavy loaded) or to 24th dev meeting, or we pick up either the 17th or 23th.

## hyc | 2019-03-11T13:11:25+00:00
Just to be clear: certainly, continual changes of the PoW as a policy, is unsustainable. We knew that from the outset. But to say "it isn't working" is inaccurate. The 6 month changes were only meant to brick existing ASICs and buy us time to develop a longer term PoW. AFAICS these changes have fulfilled their purpose. RandomX is now complete and just needs to be reviewed/audited/tested.

Don't lose sight of the bigger picture; we knew this was how things would play out.

Still worth it to explore other options, other PoW algorithm candidates, and longer term timelines. But starting from an perspective of "what we've done hasn't been working, we need to fix it" is incorrect and sets a too pessimistic tone for the discussion.

## dEBRUYNE-1 | 2019-03-11T13:23:59+00:00
>The 6 month changes were only meant to brick existing ASICs and buy us time to develop a longer term PoW.

They were also meant to keep ASICs away (for at least 6 months) and improve ASIC resistance with each iteration. Both those objectives have failed, as ASICs appeared on the network after a mere three months following the second tweak. We can thus logically conclude they aren't working.  

## JustFranz | 2019-03-11T14:25:43+00:00
> > The 6 month changes were only meant to brick existing ASICs and buy us time to develop a longer term PoW.
> 
> They were also meant to keep ASICs away (for at least 6 months) and improve ASIC resistance with each iteration. Both those objectives have failed, as ASICs appeared on the network after a mere three months following the second tweak. We can thus logically conclude they aren't working.

Or they worked out the design for v7 in the first 6 months, as soon as the tweaks for v8(9) were known they started making required changes and upon completion committed to manufacturing the ASIC. 7 and 8 were major tweaks meant to brick existing ASICs, the algos themselves were not meaningfully ASIC resistant and not at all on their own. The (degree of)change was and the promise of change is.

Monero is cheaper than it was when they started and CN-R should have closed the efficiency gap between GPU and ASIC further. The economics of the system have changed, in addition to CN-R being much more difficult to implement.

Its an ongoing process and CN-R is a major deviation from past POW algos and RandomX will be too. 

Too early for timelines. I'd like to see an audit of RandomX from the POV of a CPU/ASIC expert for whom there is not an incentive to exaggerate, dodge questions or lie.

I think there is confusion around what it means and takes to be ASIC resistant.

## Gingeropolous | 2019-03-11T15:33:46+00:00
of those dates i could do

 Sunday March 24 - 17:00 UTC

> I do think, however, that if we make a decision, we should pre-commit to a timeline.

I think its too early to make a decision. RandomX needs to be both 1) audited and 2) put out in the wild. 

> They were also meant to keep ASICs away (for at least 6 months) and **improve ASIC resistance with each iteration.** Both those objectives have failed, as ASICs appeared on the network after a mere three months following the second tweak. We can thus logically conclude they aren't working.

It us unknown whether the bolded statement was a failure as you state. Based on analyses and estimate by sech1, this round of asics was some massive percent less efficient... something like 20x as opposed to the original cryptonight of 100x. And perhaps we can never know because this will require the actual hardware, none of which is easy to obtain (even the first round of asics)... which is itself concerning. 

Also, I know there has been some speculation that CNv1 ASICs appeared, but are you referring to CNv2 ASICs? (the most recent ramp up?) I never saw massive hashrates with CNv1 like we did with CNv2. 

> They were also meant to keep ASICs away **(for at least 6 months)**

That was the hope, that was not really the goal. The goal, from the blog post, which is our best stated common ground on this matter at this point, is:

> Furthermore, in order to maintain its goal of decentralization and to provide a deterrent for ASIC development and to protect against unknown or undetectable ASIC development, the Monero team proposes modifying the Cryptonight PoW hash every scheduled fork, twice a year.

I think what we *can* conclude is that it has failed as a deterrent for ASIC development. I.e., even if a network has planned proof of work changes, an ASIC developer will still develop ASICs. Though, honestly, I think these are just a test of our resolve. If an ASIC manufacturer can profit from a 3 month run, *and* it also chips away at our fortitude to resist ASIC infiltration, then there is that much more incentive to produce the ASICs. 

Although, we have never seen this round of ASICs, so we still do not know if this was just some FPGA or some other configurable hardware that found a way to massively speed up the PoW. 

## dEBRUYNE-1 | 2019-03-11T16:21:28+00:00
>I think its too early to make a decision. RandomX needs to be both 1) audited and 2) put out in the wild.

My point is to opt for a timeline to avoid friction in the future. For example, we could audit RandomX (as far as I could see, it is almost ready) and implement it in October *and* commit to switching to an ASIC friendly algorithm 1.5 or 2 years thereafter. I am worried that if we don't precommit, friction will be created in the future. That is, let's say someone manages to make a RandomX ASIC and ramps up the hashrate significantly (e.g. a sudden +30-50%). You can be reasonably certain there will be a controversial debate in the community similar to the debate when ASICs ramped up the hashrate with 30-50% on CNv2. Furthermore, that would again take valuable time away from developing the protocol. 

>none of which is easy to obtain 

This is due to our current stance to preserve ASIC resistance. It effectively leads to ASIC manufacturers mining in secret and never publishing their ASICs. 

>(even the first round of asics)

Do you mean the ones that mined the original CryptoNight algorithm? Because at the end several manufacturers put them up for sale. 

>but are you referring to CNv2 ASICs? (the most recent ramp up?) 

I am referring to CNv2, yes (I used second tweak in my previous comment). 

>That was the hope, that was not really the goal.

This seems to be leading to a debate about semantics, which is rather pointless in my opinion. 

## dEBRUYNE-1 | 2019-03-11T16:22:52+00:00
As an administrative side note, ArticMine asked me in PM for a place to hold some pre-discussion. Do you guys think it would be best to open a new and separate issue for this? 

## SamsungGalaxyPlayer | 2019-03-11T16:56:15+00:00
@dEBRUYNE-1 would it be a separate meeting or mean that this meeting is extended? What are the goals of the pre-discussion?

## dEBRUYNE-1 | 2019-03-11T17:08:10+00:00
This is a fairly complex issue and ArticMine stated that some of its aspects would benefit from an in-depth discussion. A separate ticket would also allow the discussion to continue outside of the meeting and we can refer to things during the meeting. Furthermore, I don't think we'll be done after a single meeting :-P 

I suppose we can continue the discussion on the separate ticket and utilize this ticket for actually scheduling the meeting(s). 

## JustFranz | 2019-03-11T17:09:00+00:00
You want to agree on a timeline when we have not even explored what an ASIC mined XMR mining network could look like, should look like or probably would end up looking like. Its not just a matter of making an algorithm and telling people to go ahead and make ASICs, we could do that tomorrow for CN-R and the end result wouldn't be any different than if we did it 2 years from now.

We have not even totally agreed on ASICs. There is so much we just do not know and you want to make a quick decision. The immediate future is quite unclear regarding the POW and you want to make clear future statements and goals with concrete timelines without figuring out the stuff inbetween. I do not see that working. 



## dEBRUYNE-1 | 2019-03-11T17:19:38+00:00
>You want to agree on a timeline when we have not even explored what an ASIC mined XMR mining network could look like, should look like or probably would end up looking like.

That's what these meetings and discussion are for. Furthermore, we aren't starting from scratch. 

https://github.com/monero-project/monero/issues/3387

>We have not even totally agreed on ASICs. 

You're acting like I insinuated we did. I never said we totally agreed. 

>you want to make a quick decision.

I don't, you're twisting my words. I want to have extensive decisions before we come to an agreement (and thus a decision). We cannot dwell on the subject forever though.

>I do not see that working.

I don't see a future where we decide things regarding the PoW algorithm on the fly working either. There will be a lot of friction, especially if Monero matures further. Do we really want to have this debate when Monero's ecosystem is, say, ten times bigger? Besides, like I said, it will take away precious development time. 

## tevador | 2019-03-11T20:16:18+00:00
I should be able to attend on any of those dates, but a separate issue should also be open so more people can participate in the discussion.

## Gingeropolous | 2019-03-11T20:16:53+00:00
yeah, i'd be up for a pre-discussion on a separate thread as well. 

## fireice-uk | 2019-03-11T20:55:03+00:00
Do you want me to send in someone from Ryo to talk about CN-GPU?

## dEBRUYNE-1 | 2019-03-11T21:14:06+00:00
@tevador & @Gingeropolous - All right, I'll open a separate ticket then. 

@fireice-uk - Everyone is welcome to join and voice their input. 

## iamsmooth | 2019-03-11T21:18:30+00:00
> But to say "it isn't working" is inaccurate. The 6 month changes were only meant to brick existing ASICs and buy us time to develop a longer term PoW

I don't agree with this. Bricking ASICs after 6 months is useless if they have already been on the network for a significant period of time by then, which is not only undermining the egalitarian mining goal, but grossly insecure to the extent that it means there may only be *one* miner.

The original premise was that it wouldn't be feasible to turn around ASIC designs in less than six months (or, at least, no more than a month or two before, not enough time to make it worth it). That all seems very doubtful now. 

The only way to make this approach safe would be to _significantly_ increase the frequency of forks not only to the point where ASICs developed on the already-observed (or at least strongly suspected) cycle are impossible but there is also a safety margin beyond that. So that would be something like 2-3 months. Some have (entirely legitimately) raised objections to this on the basis of it being impractical to finalize and roll out releases, and also dangerous in that it multiplies the opportunities for error. 

> Don't lose sight of the bigger picture; we knew this was how things would play out

I disagree with that too. The premise was that minimum development cycle for ASICs was six months, or at least not much less. It seems that is not the case (this may not have been wrong at the time, but with the crypto market no longer in full bubble mode, maybe it is easy to get faster turnaround now).

We did indeed anticipate that forking every six months forever was not desirable, and it was a temporary approach pending a longer term solution, but this was absolutely never because we expected ASICs (possibly created by only one developer who then becomes the sole miner) to appear after three months, and I don't think anyone is on board with that. (Also, this was why the current fork was pushed up as much as possible ahead of the six-month schedule.)

> But starting from an perspective of "what we've done hasn't been working, we need to fix it" is incorrect and sets a too pessimistic tone for the discussion.

On the contrary, I think it is entirely accurate. It is better described as very realistic than pessimistic. Pessimism would be negative expectations of the future.

## iamsmooth | 2019-03-11T21:36:35+00:00
@Gingeropolous 
> I think its too early to make a decision. RandomX needs to be ...

The network doesn't wait. A decision needs to be made. That may be to continue the same strategy, even though it hasn't worked and has likely left the network in a very dangerous state (which by the way, was predicted/warned by some of the skeptics of the approach; maybe we should listen to them at least _somewhat_ more now, since their predictions have been demonstrated to likely be correct). Or it might be something else.

The schedule of RandomX is certainly a factor, but it isn't a determination of anything. We are not obligated to wait for it, nor is it predetermined what we do in the meantime while we wait. All of this is open to reexamination given new evidence (or for any other reason).


## xmranon | 2019-03-11T21:37:57+00:00
Poor Smooth. He fought this battle with Aeon and here we are with monero having a similar discussion. 

I agree with nailing this down sooner rather than later, just to get it out of the way. I’m very excited for RandomX, but as stated in this thread by others, it’s not a permanent solution. Knowing the next step is pretty important to keeping our eye on the ball re: the protocol writ large. 

## xmranon | 2019-03-11T21:39:57+00:00
Also: even in the ASIC discussion with the manufacturer it was mentioned that Monero is only “safe” with CNR as a result of price. If we see an increase in price, we may be sprinting for RanX in the same fashion as we did CNR if there’s no plan laid out prior. 

## iamsmooth | 2019-03-11T21:43:07+00:00
"Safe as a result of price" is another way of saying "unsafe", although I suppose it is a matter of degree. If the price would need to increase by 100x, then I guess that's pretty safe, but only 2-10x is pretty unsafe.

When the network is in an unsafe state, then yes that is problem worthy of addressing.

## JohnnyMnemonic22 | 2019-03-11T22:55:38+00:00
Regardless of the technical challenges, we have to consider that ASIC resistance (or egalitarian mining) is a significant part of Monero's identity. If an ASIC-friendly PoW is the goal, forking the project may be a more responsible course of action than potentially alienating a large portion of the community that values hardware independence.

## apertamono | 2019-03-11T23:11:36+00:00
Let's take a look at how open ASICs are working for Siacoin:

![Siastats hashrate March 2019](https://user-images.githubusercontent.com/22837744/54163679-0f8aa280-445a-11e9-8c1c-8e82fc250a9d.png)

A pro-ASIC strategy is not guaranteed to be safe even if could be egalitarian in theory.

I agree with @JohnnyMnemonic22 that we should stick to our principles as long as possible and not give up ASIC resistance before giving it a serious try. Let's focus on getting RandomX audited first.

## bitlamas | 2019-03-12T00:05:53+00:00
> Regardless of the technical challenges, we have to consider that ASIC resistance (or egalitarian mining) is a significant part of Monero's identity. If an ASIC-friendly PoW is the goal, forking the project may be a more responsible course of action than potentially alienating a large portion of the community that values hardware independence.

I would like to leave my opinion on this matter here.

While I can understand the purely technical arguments in favor of adopting ASICs, to me it seems dangerous to treat Monero as a tool where the mining process doesn't have any kind of social implication -- and for some reason nobody seems to discuss these implications. As already stated, the fact that Monero is anti-ASIC is not pettiness, it is part of the core of the project and there is a specific reasons for this: egalitarian mining.

How long have we been fighting ASICs? As far as I know, it hasn't even been 2 years since we've been doing research on PoW and forking to avoid them. Is that long enough for us to simply abandon this feature and accept that Monero mining will be provided by a select group of manufacturers, in which the logistics and distribution process is very far from the availability of CPUs and GPUs worldwide?

Today our instance is that the money of this protocol can be printed by anyone who has a computer or graphics card. Regardless of the physical location of this person. He/she does not need to ask permission from anyone, from any manufacturer, from any government. Nobody even needs to know that this person is printing money. He/she can do it anonymously. That in my view is an integral part of the protocol.

And I repeat, I understand the pro-ASIC arguments, but I have my doubts in abandoning that battle so, so quickly, only because we are currently failing.

How long will it take for governments to require ASIC manufacturers to have special permits? How long will it take for everyone who buys ASICs to be on a special list, classified as "people capable of printing money"? How long do you think it will take for the mining process to be completely controlled by a few entities? Perhaps decentralized enough not to allow a 51% attack on the network, but is this the ONLY attack we should defend ourselves?

Perhaps most of the people involved in a more advanced and technical level of the protocol (like the people commenting here) live in countries or regions where there is no need to worry about this type of limitation. Perhaps the majority here need not worry about the absurd logistical problems involved in importing ASICs into countries that are not classified as "first world". Perhaps these people don't deserve to participate in the mining process.

I also understand the argument that if Monero becomes extremely valuable, even if it is resistant to ASICs, the network will have too high a difficulty for a person with a consumer-grade computer to really make money. I understand this argument, but I don't accept it so easily.

There are two reasons why I believe that this argument is not good enough: the first is that there are millions of people living with less than $1 per day, and maybe, for these people, making "a few dollars" a month can make a difference. Whole communities could pool-mine and keep the money inside their local community. The second is that this argument completely ignores the existence of thousands of small and medium-sized businesses around the world that have half a dozen computers and one or two servers. This opens a very important path of profitability for many people on the planet. In a society educated about blockchain and mining, most of these companies could increase their profitability by using 20% (or any other optimized value) of desktop and server processing to mine Monero during business hours -- and even during idle times if electricity is cheap or subsidized. Perhaps this is not worth fighting for.

The moment we accept defeat in the war against ASICs, we are accepting that Monero becomes a network on which to participate in the process of printing money you will need to ask permission. I particularly don't like this. I don't want to ask anyone for permission. But I will have no other option if it becomes the case.

Anyway, I write this just to remind decision makers that there are implications that go beyond the technological details of the protocol. I will not pretend to have a perfect solution to this problem, because I do not have one, but it discourages me to see that, in my opinion, some people are eager to abandon this war without really exploring all viable alternatives.

And if, in the end, we really lose this war, then fine. But I'd like us to fight more against that centralizing power before simply assuming it's useless.

## iamsmooth | 2019-03-12T00:09:28+00:00
@JohnnyMnemonic22

> Regardless of the technical challenges, we have to consider that ASIC resistance (or egalitarian mining) is a significant part of Monero's identity. If an ASIC-friendly PoW is the goal, forking the project may be a more responsible course of action than potentially alienating a large portion of the community that values hardware independence

That's a fair point but...the only currently-available way to _actually accomplish_ ASIC-resistance aka hardware-independence is to significantly accelerate the forking schedule, something which a good portion of the current developers (as well as likely a large portion of the community) see as impractical and very dangerous.

You can't have everything, no matter how badly you want it.

## BigslimVdub | 2019-03-12T00:43:34+00:00
I like your foward thinking @debruyne-1. 

I believe that as of right now, RandomX is best fit for Monero since it is not focused on lightweight chain structure but more so ultimate privacy and network stability. However if there is still a possibility of ASICS with unfair mining advantage, I believe that Monero and its community may need to figure a way to work with this industry for the best long term use case. We must not forget FPGA mining and new eFPGA that can (and most likely are being) used on CN coins.  Just my 2c

## apertamono | 2019-03-12T00:45:42+00:00
@iamsmooth You say that as if it's a fact. Where's your evidence that accelerating the forking schedule is necessary when using a randomized algo? AFAIK we're the first project to do this.

By the way, we'll be discussing ASIC resistance at [a meetup in the Netherlands on Thursday](https://www.meetup.com/monero-meetup-utrecht-nl/events/259622383/). I can ask Dutch community members for their opinion. At least, if the Core Team agrees that it's useful to have this debate.

And if deviating from the fundamentals of the CryptoNote whitepaper is on the table, shouldn't we consider merged mining and proof of stake too? I'm not trolling, I never brought this up because I know these alternatives are taboo for good reasons, but if our POW has failed, shouldn't we consider whether any POW might be unsafe for a coin with a market cap below $1B or $10B?

Going back to the question of failing to meet our goals, @dEBRUYNE-1 said:
> They were also meant to keep ASICs away (for at least 6 months)

Of course @hyc is too modest to say "I told you so", but he did predict it would [take only 3 months](https://twitter.com/edbwt/status/1093945974744068097) for ASIC producers to catch up.

## JustFranz | 2019-03-12T01:02:04+00:00
I'd like if the full RandomX documentation was ready before a meeting took place. It'd also be nice if it had CPU internals and ASIC manufacturing related reasoning attached to it.

Regarding the pace of upgrades, to me it seems like we are still in a phase where we can push out meaningful updates to the software every 6 months, in addition to POW tweaks. So we do not need to be beholden to the POW.


We have certain assumptions about RandomX that I feel we must investigate and then make a decision. The main ones being:

We assume that CPUs are efficient at what they do and that there is no free performance left on the table with the implementations of the instructions that RandomX uses.
We assume that by making the algorithm sufficiently random the ASIC will have to essentially recreate the efficient CPU core that can execute those instructions.

Forcing an ASIC maker to produce a state of the art CPU with those instructions, minus other bits that RandomX does not use.

To me it seems that it is true that you can have a sufficiently random algorithm that an ASIC needs to be a CPU.

## iamsmooth | 2019-03-12T02:34:36+00:00
@iamsmooth 
> You say that as if it's a fact. Where's your evidence that accelerating the forking schedule is necessary when using a randomized algo? AFAIK we're the first project to do this.

Most of the developers still view CN-R as a pretty modest tweak. If we want any sort of confidence that the network is being protected from a single rogue ASIC then we can't rely on magical assumptions that a relatively small change to the algorithm will have a dramatic impact on the demonstrated (or at least strongly suspected) fastest release cycle for ASICs.


## hyc | 2019-03-12T02:59:36+00:00
Just as a point to ponder - a 4 month algorithm change schedule would be sufficient. An entirely new chip can be produced in 3 months, but with only 1 month to run, it would be hard pressed to reach positive ROI.

I'm not currently suggesting we switch to a 3 fork/year schedule. Just pointing out that it's possible to beat them even without a long term algorithm.


## SamsungGalaxyPlayer | 2019-03-12T03:09:26+00:00
I personally believe that Monero has a social contract to pursue ASIC-resistance. While this can change, I agree with @vp1111 that options that seek to maintain this property should be considered first.

RandomX isn't perfectly documented of course, but a lot of existing work went into it. I think it's at least slightly unfair to claim that RandomX will only provide as much ASIC-resistance as the Cryptonight tweaks. It's a completely different design.

While an ASIC-friendly PoW may make sense in the long-term, I think it certainly is less preferable to RandomX in the near 6-12 month future. Ideally, we want to have a number of manufacturers on board, and potentially even an open ASIC design that is competitive. All of this certainly wouldn't fit in the September or even April 2020 upgrade. I think this change would need to be about 2 years away.

I don't know if we have enough information to say ASIC-friendly algorithms will function better than RandomX or similar in a >2 year time horizon. We may have a better idea after RandomX is implemented in something.

## lacksfish | 2019-03-12T03:29:48+00:00
I'm more on the side of allowing ASICs to develop long term and the mining market to mature in that sense. I am a proponent of thinking about increasing hashrate as good for consensus and security.

I'd be happy to join a fruitful discussion on the matter anytime. It's currently difficult to discuss on reddit as I'm rate-limited on the Monero subreddit.. 

It could also be interesting to invite the ASIC producer that engaged in the conversation on IRC the other day (logs are on reddit)

## OrvilleRed | 2019-03-12T03:39:24+00:00
> increasing hashrate as good for consensus and security.

This is not the case. If 51% of the hashrate is controlled by one entity, it doesn't matter whether that's one kilohash, one gigahash, or one terahash per second -- the coin is susceptible to 51% attacks and can no longer be trusted.

Increased hashrate is good only if and to the degree which it makes it more difficult for a single entity to obtain that 51%. Many of us who are concerned about ASICs are concerned precisely because we judge it more likely that a single (or small consortium of) ASIC producer(s) could acquire 51% of the total hash rate. In contrast, we prefer GPU (and even better, CPU) mining because there is a much bigger and more diverse set of people with access to such resources; as such, it is less likely that 51% of the hashes would be controlled by any one of them.

> It could also be interesting to invite the ASIC producer that engaged in the conversation on IRC the other day

Indeed! Any productive feedback we can get from any ASIC maker is absolutely to be welcomed! Hell, I'll buy the beer & pizza if it helps bring them to the table!


## hyc | 2019-03-12T03:42:52+00:00
For example - a small project typically takes 6 months from reserving production time until fabricated chips are delivered. 4 months from submitting design, to production. https://www.mosis.com/db/pubf/fsched?ORG=TSMC 

## iamsmooth | 2019-03-12T05:56:57+00:00
In the case of continuing ASIC resistance, I would be in favor of speeding up the algorithm change cycle. That happened this time anyway, on an unplanned basis, due to community pressure to accelerate the fork. 

Continuing the old schedule appears like a pretty busted strategy, with it appearing that someone was still able to create secret ASICs  both times (though more obvious in the case of the most recent fork).

ASIC-resistance is defensible when it keeps _all_ ASICs away, but not at all when it keeps _all but one_ ASICs away. _That's actually worse than doing nothing_.




## dEBRUYNE-1 | 2019-03-12T07:59:18+00:00
I've opened #316 as a place of discussion. Let's reserve this ticket for scheduling the meetings and move the discussion to #316. 

## dEBRUYNE-1 | 2019-03-16T14:58:40+00:00
I am going to set the meeting time to **Sunday March 24 - 17:00 UTC** in #monero-dev, as on Sunday typically the most people are available and this gives us another week to suck in all related information before we continue the discussion. I personally think most has been said now on the other issue. Thus, let's try to find some common ground regarding the future in this discussion. 

Ping:

@iamsmooth 
@fluffypony 
@hyc 
@JohnnyMnemonic22 
@tevador 
@binaryFate 
@SamsungGalaxyPlayer
@vp1111
@ArticMine 
@SChernykh
@Gingeropolous 

And anyone else that I forgot.   




## jwinterm | 2019-03-16T15:08:09+00:00
@hyc MOSIS is a service that allows researchers to combine multiple designs onto a single wafer/maskset for small production runs so that people who only want a small number of chips can share the cost of mask production and other overhead. I don't think it's indicative of a realistic timeframe except maybe as absolute upper bound.

These guys are offering 8 week turnaround from tapeout:
https://www.baysand.com/solutions/asic/



## ta32 | 2019-03-17T22:27:44+00:00
is there going to be a recording of this meeting? or is it going to be streamed?
@dEBRUYNE-1

## JustFranz | 2019-03-17T22:39:57+00:00
> is there going to be a recording of this meeting? or is it going to be streamed?
> @dEBRUYNE-1

its a text chat meeting

## el00ruobuob | 2019-03-18T15:14:51+00:00
@dEBRUYNE-1, #monero #monero-community or #monero-dev?
or #monero-pow?

## dEBRUYNE-1 | 2019-03-21T12:35:32+00:00
@el00ruobuob: -dev I guess. 

@ta32: logs will be published. 

## el00ruobuob | 2019-03-21T14:11:16+00:00
> @ta32 : logs will be published.

I'll make sure they will.

## dEBRUYNE-1 | 2019-03-24T15:05:47+00:00
PoW meeting in ~2 hours in -dev. 

## SamsungGalaxyPlayer | 2019-03-24T19:48:59+00:00
Logs: https://repo.getmonero.org/monero-project/monero-site/blob/b87354501b6343f9146f331805ddadc45696f728/_posts/2019-03-24-logs-for-the-dev-meeting-held-on-2019-03-24.md

## dEBRUYNE-1 | 2019-03-25T15:56:06+00:00
Discussion continues in #321. 

## SamsungGalaxyPlayer | 2020-02-09T18:00:41+00:00
@dEBRUYNE-1 can we please close this?

# Action History
- Created by: dEBRUYNE-1 | 2019-03-11T11:46:54+00:00
- Closed at: 2020-03-09T21:40:47+00:00
