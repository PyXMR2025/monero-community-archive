---
title: 'Save the network: Disincentivize usage of high hash-rate pools'
source_url: https://github.com/xmrig/xmrig/issues/2277
author: t-anon
assignees: []
labels: []
created_at: '2021-04-17T15:23:04+00:00'
updated_at: '2021-04-29T22:24:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
As per [MiningPoolStats](https://miningpoolstats.stream/monero), two Monero pools operate nearly 60% of the Monero hashrate (minexmr.com at ~40% and supportxmr.com at ~20%). This is _very_ unhealthy for Monero as a whole, as this makes the security of the network dependent on the opsec of two operators. 

**A resourced entity like a nation-state need only target these two individuals to attack the network and break its legitimacy.** And this is if we assume the operators _don't_ collude, for which there is enormous monetary incentive.

XMRig is in the unique position of being able to help decentralize the network in order to make it healthy. We should discuss the best way to accomplish this. Some suggestions:

For users attempting to use "dangerous pools" that occupy >1% hash rate, we can begin implementing the following increasingly aggressive measures:
- [ ] Remove them from the list of default pools
- [ ] Throw a warning when choosing such a pool (perhaps a warning that must be manually acknowledged)
- [ ] Blacklist them, _silently_ redirecting usage to a randomly selected less-used pool (perhaps cycling among such pools every few minutes)

For the first one, **the configuration wizard absolutely should not be assisting in the consolidation of hash power.** The defaults should be changed and entering a high hashrate pool should not be discouraged (throw a warning). However, this won't help migrate any existing hash power, it will just help new miners take a closer look at what they're doing.

The second measure is a more aggressive one, that may help migrate _some_ existing hash power, though users are still likely to ignore any warning.

The last measure is most aggressive, and ethically questionable, but it is also the most likely to result in a migration of existing hashpower. **This can also be done today,** simply by starting with blacklisting the top 5 pools and having a hardcoded list of 50-100 pools that the client will randomly redirect to if one of the top 5 are used. As the next version of XMRig is released and used or incorporated in downstream products, we will see a much-needed decentralization of hash rate. Since this transition is silent, it would be transparent to users.

--- 

Over time we should lower the threshold from 1% to something less, since even 1% means that only 50 people need to be compromised for tomorrow's currency to be broken. Down the line, perhaps a P2P method could be implemented that dynamically creates pools for XMRig users, with the client either creating or connecting to one of these pools by default and cycling through them periodically.

Some may argue that solving this problem is outside of the purview of XMRig, and that XMRig should be a tool agnostic to network politics. I would argue that XMRig is the only entity able to practically solve this problem in any reasonable timeframe, and that as a tool developed by people that care about Monero, it cannot be agnostic to network politics to begin with.

# Discussion History
## SChernykh | 2021-04-17T17:32:27+00:00
> Remove them
Blacklist them

Censorship, even with good intentions, is a bad idea. The two pools in question are in the middle of the list on xmrig.com/wizard so I don't think clueless newbies would intentionally choose them. Adding more small pools to the list is better idea.

## t-anon | 2021-04-17T21:13:57+00:00
@SChernykh I think the discussion of censorship is a bit more nuanced. Blacklisting dangerous pools most definitely helps the health of the Monero network, and therefore helps its users.  Does blacklisting these pools restrict the freedom of miners? Sure. But it's also perhaps the only measure that can actually help decentralize hash power before someone takes advantage of the current issue.

We can't just say censorship is bad and hold our hands up. The alternative - not censoring - is very much likely to be even worse.

## t-anon | 2021-04-17T23:15:38+00:00
At the very least, I think we should have prominent warnings displayed if someone uses a high hashrate pool.

## xmrig | 2021-04-18T05:56:17+00:00
We will not start war against network (pool) neutrality and implement any sort of block/black lists. Small pools should outperform by better marketing/service/UI/etc it's the only right way. Yes this way is really hard.

About the wizard I don't think it is popular enough to change things, but top pools have link to it so users may figure out there are other pools.

## Spudz76 | 2021-04-20T11:24:11+00:00
Small pools must have better payout than large ones: problem fixed.

Miners go where profits are best (low fees) and payouts always work on schedule (no downtime/ineptitude).  I use MoneroOcean which is probably worst for Monero Blockchain since I rarely mine actual Monero (they payout XMR for every supported coin - a feature nobody else has therefore I'm never switching pools... unless there was a cheaper one with multicoin that works as well).  So then how would you censor that sort of spitting on the Monero blockchain for higher profit?

Censorship is only right before it comes for you, and it will always come around.  Very large nope, there.

## AllGasNoStakes | 2021-04-29T15:46:33+00:00
I think the key is to reward the bigger pools less like @Spudz76 said.
This is done in the Cardano network in a similar fashion(despite being PoS) where there is a maximum size above which the rewards dwindle.
No censorship just a little push to not join those pools!

## ArKam | 2021-04-29T22:24:24+00:00
I’m currently setting up a 48 nodes cluster composed with rPI 4B+ , if xmrig is available for linux on AARCH64 I’ll be happy to make those workers join the xmrig.eu pool.

# Action History
- Created by: t-anon | 2021-04-17T15:23:04+00:00
