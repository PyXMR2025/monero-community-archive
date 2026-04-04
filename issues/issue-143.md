---
title: The  true target is consensus to change the PoW.
source_url: https://github.com/monero-project/research-lab/issues/143
author: Asbestos999
assignees: []
labels: []
created_at: '2025-08-21T16:46:51+00:00'
updated_at: '2026-01-25T01:53:50+00:00'
type: issue
status: closed
closed_at: '2025-08-25T18:29:45+00:00'
---

# Original Description
Current Proof of Work based on RandomX is working as intended. We just need more miners, whose numbers are steadily increasing over the years, as can be seen in the difficulty charts.

It seems to me that it's working too well, and state-sponsored actors are doing their best to trigger discussions about changing the current PoW.

I base this on numerous AI-generated articles, amplified by bots, claiming that we are already on the path to changing the current PoW and increasing number of propositions here to change it.

The current situation is that the attack is collapsing and has accomplished nothing... or has it? After all, we are discussing changing something that is working and only getting stronger over time, thanks to the effectiveness of the tail emission.


# Discussion History
## RB90909 | 2025-08-22T12:01:55+00:00
RandomX works well until it doesn’t; a state actor could simply build a CPU farm (data center) or rent hash power, while malicious actors might exploit botnets. Qubic has demonstrated that the threat is real. Relying solely on RandomX could prove to be fatal.

## Asbestos999 | 2025-08-22T14:15:20+00:00
> RandomX works well until it doesn’t; a state actor could simply build a CPU farm (data center) or rent hash power, while malicious actors might exploit botnets. Qubic has demonstrated that the threat is real. Relying solely on RandomX could prove to be fatal.

Pubic has demonstrated that the well-decentralized PoW we have now works, and a 51% attack has proven to be too expensive even for a state-sponsored actor.

There isn't enough RandomX hashrate available on the market to rent for a 51% attack.

"Exploit" botnets? You can't exploit them - you could try creating your own botnet, but it's nearly impossible for one to grow large enough to carry out a successful 51% attack and every botnet master is too happy with making money on Monero mining.

Some computing centers available for rental don't even allow cryptocurrency mining.

Creating a CPU mining farm capable of executing a 51% attack is currently financially out of reach for any government - it's not even worth considering.

The network is getting stronger every year, and making any changes doesn't make sense. If we continue to grow at the pace we have over the past decade, no one will even dream of reaching 51%. In another ten years, reaching even 1% will likely be impossible.

And BTW, saying "RandomX works well until it doesn't" is the stupidest thing a living creature can say, as you can start any argument with it.

...The Sun works well until it doesn't...
...Aliens could simply destroy it...

Should we start packing ?

## PPPDUD | 2025-08-22T16:27:57+00:00
> RandomX works well until it doesn’t; a state actor could simply build a CPU farm (data center) or rent hash power, while malicious actors might exploit botnets. Qubic has demonstrated that the threat is real. Relying solely on RandomX could prove to be fatal.

Qubic is falsifying self-reported statistics to lower the price of XMR. ~30% control (what they really achieved) did not give them absolute power and just freaked out new investors.

Bad actors already mine XMR with powerful botnets, and they still haven't managed any meaningful attacks on the blockchain.

What would you propose instead, proof-of-stake? Look at Ethereum and Solana, two major PoS chains. Both require powerful computers in order to participate as a validator. Both XMR nodes and miners have relatively low hardware requirements, though there is a much steeper decline in efficiency as hardware gets worse.

## Asbestos999 | 2025-08-23T08:05:20+00:00
> > Creating a CPU mining farm capable of executing a 51% attack is currently financially out of reach for any government - it's not even worth considering.
> 
> What? Are you being serious? Daily security budget is around 100k-110k. Total cost of equipment starting from scratch is around $320M.
> 
> There are CPU farms in that cost and more. And though not as efficient there are GPU farms in the billions and growing.
> 
> Any one or a combination of which could be discretely contracted to attack.
> 
> Every CPU the US government has in its possession in some form is probably enough.

You make me laugh.


AMD EPYC 9654 96-Core Processor - $6,949.99
AMD EPYC 9654 96-Core Processor - $6,949.99
GIGABYTE MZ73-LM1 Motherboard (two sockets) - $946.00
V-COLOR DDR5 96GB (24GBx4) 8000MHz CL40 - $1,391.99
SUPERMICRO CSE-826BE1C4-R1K23LPB 2U - $1,551.99
Kingston NV3 M.2 2280 500GB - $38.99


hashrate: 184818

Price Source: newegg


At current 4.87 GH/s total network hashrate, adversary would need 5.07 GH/s to have 51% which would result in total net hash at 9.94 GH/s

5070000000 / 184818 (one dual CPU rig) = 27432 Rigs

27432 RIGS * 17829 USD = 489,085,128 USD (but with such big demand, the price would increase a lot)

So, a private entity would need to somehow justify to a government that spending half a billion dollars on hardware alone, and probably another half a billion on the infrastructure to handle such a massive farm, is in fact a good attack strategy.

Before they could even finish the project, the total network hashrate would probably increase again, as it has been doing for over a decade now, forcing them to beg for more money on their project.

And for Monero to be hurt, they would need to double-spend a large transaction-meaning they’d have to do it on a legitimate centralized exchange, because that’s where the liquidity is.

And that’s not even counting the electricity bill.

Your 320$ Million would barely be enough for cables alone.

You can’t comprehend the scale. The numbers may seem easy, but in the real world it’s economically and physically undoable.

Also, we’re talking about an ideal scenario where there is only one adversary, if there is more than one, they will practically destroy themselves and only add to the security of the network for the time being.


## RB90909 | 2025-08-23T12:13:01+00:00
> So, a private entity would need to somehow justify to a government that spending half a billion dollars on hardware alone, and probably another half a billion on the infrastructure to handle such a massive farm, is in fact a good attack strategy.
> 
> Before they could even finish the project, the total network hashrate would probably increase again, as it has been doing for over a decade now, forcing them to beg for more money on their project.

They don't need to buy hardware since there is plenty of computing power available through cloud providers; they just need to rent it, mine XMR, and sell XMR to recover some of their expenses. As the price of XMR drops, mining by legitimate miners who actually pay for electricity will decrease, leading to a cascading effect & reduced security. 

I am not suggesting a complete shift to ASIC PoW, but a dual PoW model like Tari with a hybrid PoS could be beneficial in the long run.

## Asbestos999 | 2025-08-23T12:24:11+00:00
> > So, a private entity would need to somehow justify to a government that spending half a billion dollars on hardware alone, and probably another half a billion on the infrastructure to handle such a massive farm, is in fact a good attack strategy.
> > Before they could even finish the project, the total network hashrate would probably increase again, as it has been doing for over a decade now, forcing them to beg for more money on their project.
> 
> They don't need to buy hardware since there is plenty of computing power available through cloud providers; they just need to rent it, mine XMR, and sell XMR to recover some of their expenses. As the price of XMR drops, mining by legitimate miners who actually pay for electricity will decrease, leading to a cascading effect & reduced security.
> 
> I am not suggesting a complete shift to ASIC PoW, but a dual PoW model like Tari with a hybrid PoS could be beneficial in the long run.


SHOW ME where you can rent enough hardware to sustain 5 GH/s without getting banned for cryptocurrency mining.

Why is no one doing it?

You know what would be beneficial? Staying with the current PoW that has already proven it’s working and only getting stronger with time.

What you’re suggesting is bringing more attack vectors, and I suspect you know it.

Isn’t it a coincidence that just as Monero’s hashrate started to rise significantly (before the Pubic attack), suddenly there is a lot of talk about changing PoW? Too scared that it will be immune to such attacks?

[https://bitinfocharts.com/comparison/monero-difficulty.html#alltime](https://bitinfocharts.com/comparison/monero-difficulty.html#alltime)

We are being played like little kids with all the FUD about the current PoW.

Social engineering at its best, using scare tactics, a few programmers on a government payroll, and an army of bots.
I’m not surprised that they-whoever it is (government, competition, blockchain analytics companies)-have chosen this route, it’s the easiest, most efficient, and cheapest way to destroy the project.

BTW, renting is far more expensive than building and then selling the used hardware.

Even IF a big company like Microsoft with Azure agreed to such a large contract (which I bet would have to be long-term, as they would need to invest a lot), it would cost about $157.7 million per month to rent it or even more.

Congrats, you just made the attack MUCH more expensive.

> As the price of XMR drops, mining by legitimate miners who actually pay for electricity will decrease

This will, in turn, hurt the attacker because he can no longer:

>  they just need to rent it, mine XMR, and sell XMR to recover some of their expenses.

Due to RandomX, every miner is on the same level. Plus, there are botnets that don’t care at all and mine regardless of the price, as they are always in profit.

Historically, the network hashrate has increased even when the price was dropping.

Microsoft Azure:

> Effective December 1, 2022, Microsoft updated its Universal License Terms for Online Services—which covers Azure—to explicitly ban crypto mining unless you obtain written pre-approval from Microsoft.
Acceptable Use Policy:
> 
> “Neither Customer, nor those that access an Online Service through Customer, may use an Online Service … to mine cryptocurrency without Microsoft’s prior written approval.”
> 
> Microsoft explained the change as necessary because crypto mining can:
> 
> Disrupt or impair services, and
> 
> Be associated with cyber fraud, abuse attacks, and unauthorized access.
> 
> Exceptions: Crypto mining may be considered only in specific cases-for testing and research purposes related to security detection. Otherwise, it remains disallowed.

Every other renting company has similar rules, so good luck, I guess.

And as I said before, double spending would need to be done on a large transaction-this would mean attacking a legitimate centralized trading platform (bank robbery) and it would end with a long sentence in federal prison.

Other than FUD, these attacks-even if successful-are totally worthless.


## PPPDUD | 2025-08-23T15:08:56+00:00
Offtopic, but can we please remain civil here? Qubic is spelled with a Q, and this is not the place for bad puns. If we judge Qubic, it should be on their merits, not the name.

## Asbestos999 | 2025-08-23T16:59:21+00:00
> Offtopic, but can we please remain civil here? Qubic is spelled with a Q, and this is not the place for bad puns. If we judge Qubic, it should be on their merits, not the name.

It’s **Q**ubic? Now it sounds even less serious.

Anyway, even if all the governments of the world wanted to attack Monero-yes, of course they could do it.

But it’s **unrealistic**, even for a single government, to allocate such a high budget for such a pointless attack, when they can more easily target the community, which is the subject of this discussion as there was no successful double-spend and I doubt we will see one.

A sane approach would be to give the current mining scheme a few more years to grow, instead of forcing miners to host a full node or adopt some other unnecessary measure which will more likely introduce new vectors of attack and discourage a good percentage of miners or make it more centralized.

> It's not ideal to depend on the state for such a thing. Also KYC information is be bought on the DNM so catching them isn't guaranteed.

So you’re saying that a billion-plus project to attack Monero would rely on a stolen account from a DNM?
Nice one. I’d love to see the funding request letter describing this incredible plan.

> Also it's better than an attack doesn't happen in the first place. You don't need to double spend on a CEX, they just happen to have the most liquidity for now. That likely changing as XMR gets delisted everywhere.

Oh yes, more FUD, please, MORE. It's never enough...

;--

The guy behind the QQQQubic is now claiming to be S. Nakamoto.

https://qpools.qubicdisciple.info/  (it was linked on the qubic site, so I suppose it's "official")

This link revealed after clicking "release the beast" and then on the icon of cat that popped up:
https://matildaonqubic.com/

Scroll down.... seriously.... seems like a work of his GF or something.
Warning - It's cringy AF.

## Asbestos999 | 2025-08-24T07:17:26+00:00
> > But it’s unrealistic, even for a single government, to allocate such a high budget for such a pointless attack, when they can more easily target the community, which is the subject of this discussion as there was no successful double-spend and I doubt we will see one.
> 
> You can just keep ignoring how relatively cheap it is to attack the network and pretend otherwise. That doesn't help your case.

Well, it doesn’t help your case, either.

> > So you’re saying that a billion-plus project to attack Monero would rely on a stolen account from a DNM?
> > Nice one. I’d love to see the funding request letter describing this incredible plan.
> 
> So you just misunderstood those points completely.

I understood it fully and completely.

> > A sane approach would be to give the current mining scheme a few more years to grow, instead of forcing miners to host a full node or adopt some other unnecessary measure which will more likely introduce new vectors of attack and discourage a good percentage of miners or make it more centralized.
> 
> This current approach has lead us to now. If it's so wonderfully secure and amazing you wouldn't see so much talk about it at least not those that are well known and respectable community members. And miners that constantly complain that mining is minimally profitable to downright unprofitable.

The last thing that will trigger any change in PoW is miners’ profitability.
Respected members (and that doesn’t include you or me) are always looking for better solutions. So far, we haven’t found any, and pushing for change due to scaremongering is not a good approach.

> Also what's wrong with forcing miners to have a full node? I think it's a very reasonable demand. It also pushes out botnet masters which is extremely desirable. Or the other RandomX solution like time weighted blockchain?

Botnets are honest miners contributing to the decentralization and security of the network. You may not like it as a miner who pays for electricity, but that’s the truth - they are beneficial for the network.

Also, botnet masters are already using xmrig-proxy to handle all the work from one place, they would just spin up a full node on that machine.

It wouldn't surprise me if that's the goal of all this FUD-to decrease the hashrate that is immutable to price attacks.

> Storage space is one of the few things that have improved and gotten cheaper over time.
> 
> And in my comment about wanting a more secure network and how XMR is getting delisted in more places (like Canada just a few days ago) you replied
> 
> > Oh yes, more FUD, please, MORE. It's never enough...
> 
> Ok as nicely as I can say it I believe you're just having a largely unserious dialogue. Very little of what you said has actually helped your case.

What case are you referring to?

> Your only valid argument so far has been possibility of more attack vectors as more gets added in. But this is a possibility for anything every time something gets added in.

You simply don’t fix something that’s working unless there are substantial improvements to be made - and so far, every new idea has its own set of problems.

I’m done replying to you, as we’re just going in circles. You clearly have an agenda and are pushing for changes no matter what.

An over-billion-dollar attack vector is not a realistic one. If money were no object, we would have already been taken out by ASICs. It’s not that it’s not doable-it’s just too expensive.

/Over&Out.

## RB90909 | 2025-08-24T19:38:39+00:00
> 
> The last thing that will trigger any change in PoW is miners’ profitability. Respected members (and that doesn’t include you or me) are always looking for better solutions. So far, we haven’t found any, and pushing for change due to scaremongering is not a good approach.
> 
They already proposed a hybrid model to keep miners happy 
> 
> You simply don’t fix something that’s working 
> 
its simply not working, botnets have not been able to scale up when there is a attack 

## Asbestos999 | 2025-08-25T07:23:02+00:00
> > You simply don’t fix something that’s working
> 
> its simply not working, 

You're wrong - there was no successful 51% attack. So.... It works.

> They already proposed a hybrid model to keep miners happy

You're talking about the LLM generated junk? (https://github.com/monero-project/research-lab/issues/138)

> botnets have not been able to scale up when there is a attack

**Botnets have already saved Monero.** You can easily check how much of the current hashrate comes from botnets - hint: Waves. And no - these are not legitimate servers spinning up, these are infected computers switching on and off. That’s why it’s gradually going down and up. If it weren’t botnets, it would be a square wave and it would be reversed (right now it's going down at night).

https://miningpoolstats.stream/monero

## PPPDUD | 2025-08-25T15:32:10+00:00
> > > You simply don’t fix something that’s working
> > 
> > 
> > its simply not working,
> 
> You're wrong - there was no successful 51% attack. So.... It works.
> 
> > They already proposed a hybrid model to keep miners happy
> 
> You're talking about the LLM generated junk? ([#138](https://github.com/monero-project/research-lab/issues/138))
> 
> > botnets have not been able to scale up when there is a attack
> 
> **Botnets have already saved Monero.** You can easily check how much of the current hashrate comes from botnets - hint: Waves. And no - these are not legitimate servers spinning up, these are infected computers switching on and off. That’s why it’s gradually going down and up. If it weren’t botnets, it would be a square wave and it would be reversed (right now it's going down at night).
> 
> https://miningpoolstats.stream/monero

If you're saying LLM-generated junk because of me, you might find it useful to consider that I don't think it's junk.

## PPPDUD | 2025-08-25T15:41:33+00:00
> > 489,085,128 USD
> 
> Thanks, 320M was affordable but 489M? Unaffordable by governments. Nothing has ever costed a government more money...
> 

For context, the TSA has a budget of more than 11 billion dollars in the United States. The NSA has a budget of about 73 billion dollars. That means that under the $489M estimate, the NSA alone could orchestrate 150 attacks on XMR if they stopped everything else and did mass layoffs.

## PPPDUD | 2025-08-25T17:56:52+00:00
> [@PPPDUD](https://github.com/PPPDUD)
> 
> That comment I made was sarcastic. My whole point in the reply was that a government at least the US and probably most western governments can easily afford 480 Million in capital cost for CPU's, they probably already do own it. Though even that is not necessary to attack the network. And since it's CPU's it won't get bricked from an hardfork that changes the mining algorithm. Not that I'm for ASIC's.

I was trying to add to your point a bit.

## Asbestos999 | 2025-08-25T18:01:08+00:00
The truth is - if they could do it (NSA, TSA, or aliens from another f planet) - they would have attacked Monero ten years ago, when it was much easier.

Maybe there are too many legal obstacles. 
Maybe they just don’t have the cojones.
Maybe they are using Monero them self and need it.

A guy well known for scamming created a fake AI cryptocurrency and openly admitted he never had more than ~34% of the hashrate. He was faking it and got caught paying influencers (yeah, that f cancer) and “news” sites to spread lies about a successful 51% attack. On top of that, he used an army of bots to pump this nonsense on pathological sites - the so-called social platforms.

Are we really digging it?

The most important factor is decentralization - and we have it.
As of today, the Monero network is more secure than Bitcoin, because all it takes to compromise Bitcoin’s security is a few knocks on the doors. That’s it.

Remember the China ban? When Bitcoin’s hashrate dropped by 65% in just a few days - from 197 EH/s to 68 EH/s?
Yeah. Numbers don’t mean s if it’s centralized.

I have other things to do, but keep the discussion going. I’ll read it, even if I don’t respond.

**/Over&Out.** 

> That means that under the $489M estimate

PS. The full estimate is well above 1 billion USD, more likely 2 billion, and I wouldn't hold my breath that it will be sufficient.

## Rucknium | 2025-08-25T18:29:45+00:00
I will close this issue. This would be a good discussion for Reddit or [monero.town](https://monero.town/) .

# Action History
- Created by: Asbestos999 | 2025-08-21T16:46:51+00:00
- Closed at: 2025-08-25T18:29:45+00:00
