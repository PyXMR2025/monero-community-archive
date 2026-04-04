---
title: Encourage miners to use environmentally-friendly setup
source_url: https://github.com/monero-project/monero/issues/8343
author: Kreyren
assignees: []
labels: []
created_at: '2022-05-19T20:06:46+00:00'
updated_at: '2022-07-20T00:50:16+00:00'
type: issue
status: closed
closed_at: '2022-07-20T00:50:16+00:00'
---

# Original Description
Cryptocurrencies around the world are contributing to making the global warming crisis significantly harder to manage[1] with some juridistictions arguing for a crypto ban due to this reasoning[2].

As such proposing to dedicate this issue to finding solutions on how to make monero more environmentally-friendly.

### References
1. Wikipedia article on the environmental impact of cryptocurrencies https://wikipedia.org/wiki/Environmental_impact_of_cryptocurrencies?lang=en
2. NCBC Report on The New York plans to ban bitcoin mining https://www.cnbc.com/2022/05/05/new-york-bitcoin-mining-moratorium-proceeding-through-state-house.html

# Discussion History
## Kreyren | 2022-05-19T20:11:31+00:00
#### My Proposal - Increase a block rewards to miners with environmentally-friendly setup

Proposing to implement rules and guidelines to create a decentralized certificate authority that would implement their way of verifying that the miner's setup is environmentally-friendly and issues their cryptographic certificate that when verified would increase the block rewards for the miner (requiring X amount of certificate authorities to be eligible for the increased reward to avoid misuse of the system).

## nahuhh | 2022-05-19T20:39:32+00:00
> #### My Proposal - Increase a block rewards to miners with environmentally-friendly setup
> 
> Proposing to implement rules and guidelines to create a decentralized certificate authority that would implement their way of verifying that the miner's setup is environmentally-friendly and issues their cryptographic certificate that when verified would increase the block rewards for the miner (requiring X amount of certificate authorities to be eligible for the increased reward to avoid misuse of the system).

Yeah.. thats a big fat NO from me.

## Kreyren | 2022-05-19T20:42:20+00:00
> Yeah.. thats a big fat NO from me. -- @nahuhh 

why not? and do you have an alternative solution?

## nahuhh | 2022-05-19T20:45:01+00:00
Solution to? 
You need a problem in order to have a solution.

## Kreyren | 2022-05-19T20:45:56+00:00
> Solution to? You need a problem in order to have a solution.

Problem was proposed in OP:

> Cryptocurrencies around the world are contributing to making the global warming crisis significantly harder to manage[1] with some juridistictions arguing for a crypto ban due to this reasoning[2].

## selsta | 2022-05-19T20:48:22+00:00
I don't think what you are proposing is possible in a non centralized way and even then it could easily be tricked.

## nahuhh | 2022-05-19T20:53:04+00:00
> > Solution to? You need a problem in order to have a solution.
> 
> Problem was proposed in OP:
> 
> > Cryptocurrencies around the world are contributing to making the global warming crisis significantly harder to manage[1] with some juridistictions arguing for a crypto ban due to this reasoning[2].

Global warming caused by my ryzen 3600 consumer series CPU?
How is that a monero problem and not a proprietary amd problem?
(I wholly disagree with your "monero is killing the planet" assessment. Mining monero is pretty effecient)

Some jurisdiction is going to ban me from using my CPU?
What are you talking about?

@selsta 
For back story, he says monero is a failed project because he cant make money on it. His solution ia raising the block reward.

I dont know when this certificate stuff was thought up. I disagree with him on that as well, for the same reasons you state

## Kreyren | 2022-05-19T21:01:01+00:00
> I don't think what you are proposing is possible in a non centralized way and even then it could easily be tricked. -- @selsta 

I think that the issue of tricking could be mitigated by requiring X amount of certificates to be elligible, but the issue is ensuring that those authorities are actually doing what they are expect to do and not issue certificates to non-eco systems

In terms of adapting the verification in layer i think it's worth exploring verification through checking where the miner is located e.g. if they are in finland helsinky then it's likely that they use a green energy, but that can be mitigated by using VPN/Proxies etc..

In terms of already present infrastructure i was thinking that we could establish a "green" mining pools where their admins would have method to verify that the miner is eco-friendly and presented that to the community for verification to then do the increased block rewards per-pool basis.

Optionally to provide different point of view the method currently used in system administration is the admin paying for the certificate authority to check their systems and then release the certificate i don't know how much could this process be adapted to monero to not harm the privacy

## Kreyren | 2022-05-19T21:05:55+00:00
> (I wholly disagree with your "monero is killing the planet" assessment. Mining monero is pretty effecient) -- @nahuhh 

i am not saying that monero is killing the planet i said that crypto is contributing to the miss-management of global warming crisis

> For back story, he says monero is a failed project because he cant make money on it. His solution ia raising the block reward. -- @nahuhh 

That's false i said in matrix XMR group that i see monero as a failed coin due to the exchanges reportedly having paper monero to dictate it's value and manipulate the market to the point when they are able to do ponzi scheme based on informations given to me by the community members.
I see monero as a project the best implementation of crypto atm

> Some jurisdiction is going to ban me from using my CPU? What are you talking about? -- @nahuhh 

I am not familiar with the politics surrounding New York's ban on bitcoin i am focusing on EU politics when i constantly hear the argument of "one visa transaction takes 200x less energy and harms the planet significantly less then one BTC transaction" so with this issue i want to make monero more likable for further implementation as there is a growing number of EU politicians who like it from a technological view.

## hyc | 2022-05-20T02:07:36+00:00
> create a decentralized certificate authority

Yeah, no such thing. Creating a certificate authority implies centralization. This proposal is not logical and not implementable.

## ghost | 2022-05-21T06:15:34+00:00
>Cryptocurrencies around the world are contributing to making the global warming crisis significantly harder to manage[1]

Gold mining also makes the global warming crisis harder to manage. The question is whether the energy spent mining gold or securing monero transactions is worth they utility they provide. If the energy usage of PoW is a fundamental flaw (which I believe it is), then you are better off trying to increase the utility-per-joule than try to reinvent it completely, especially when cryptocurrencies count for <1% of global electricity usage, and electricity usage is a fraction of global CO2 emissions itself (https://upload.wikimedia.org/wikipedia/commons/0/0b/Global_GHG_Emissions_by_Sector_2016.png)

>with some juridistictions arguing for a crypto ban due to this reasoning[2].

I doubt juridistictions will be able to ban RandomX CPU mining. Such a ban would be incredibly difficult to enforce.

>Proposing to implement rules and guidelines to create a decentralized certificate authority that would implement their way of verifying that the miner's setup is environmentally-friendly and issues their cryptographic certificate that when verified would increase the block rewards for the miner (requiring X amount of certificate authorities to be eligible for the increased reward to avoid misuse of the system).

Your proposed solution is laughable. I take it you would need to have some sort of institution go around the globe and inspect people's mining setups so you can issue these mining licenses and hope that they don't change it after you leave. At that point, why not just have the CAs sign all blocks, eliminating the need for miners altogether? That is effectively what proof of stake is, just with more CAs. What stops a CA from selling signatures on the black market for kickbacks? What stops a miner from using their certificate from a solar-powered miner to authenticate their blocks mined from a coal-powered mine across the globe?

The problem is that there are minor but fundamental flaws in the nature of cryptocurrencies, and your proposed ""solution"" is to set up some sort of abuse-prone kafkaesque bureaucratic nightmare to fix it.

If you are so concerned about the emissions of PoW cryptocurrencies, and you are so willing to sacrifice any and all decentralization to achieve power efficency, then go work on a centralized payment system like GNU Taler or a Proof-of-Stake cryptocurrency like Nano instead. your efforts will be well received there.

## ghost | 2022-05-21T06:38:32+00:00
> I am not familiar with the politics surrounding New York's ban on bitcoin i am focusing on EU politics when i constantly hear the argument of "one visa transaction takes 200x less energy and harms the planet significantly less then one BTC transaction" so with this issue i want to make monero more likable for further implementation as there is a growing number of EU politicians who like it from a technological view.

That rhetoric of "one visa transaction takes 200x less energy and harms the planet significantly less then one BTC transaction"  is misleading. 

Firstly, when the vast majority of the miner's payout is block rewards as opposed to fees (as bitcoin's currently is), then the amount of electricity that a miner will be willing to spend on mining to break even is not related to the demand for bitcoin transactions. That is to say, bitcoin miners will spend about the same amount of energy nowadays mining a block whether or not the block is full of transactions. So making a transaction does not increase the energy usage of bitcoin by that much.

Secondly, bitcoin's block size is unnecessarily small (1MB) so the transactions-per-block are unnecessarily low, thus the energy-per-transaction is unnecessarily high relative to most other cryptocurrencies including monero, litecoin, etc.

Lastly, a visa transaction isn't comparable to a monero transaction. Credit card companies sell your transaction data to advertisers, monero is private. Credit card transactions can be reversed or cancelled or have their funds seized by a centralized authority, cryptocurrency transactions are designed to prevent double spending. Credit card transactions are insecure and depend on public information (you use the same number to spend/receive a bank wire, for example) or easily phish-able information like your name address and SSN, cryptocurrency transactions are secure and use public/private key cryptography.

> > Yeah.. thats a big fat NO from me. -- @nahuhh
> 
> why not? and do you have an alternative solution?

It alarms me that you don't seem to understand just how backwards your solution is. Your solution is the equivalent to converting your car into a horse-and-carriage to improve it's fuel economy.

## Kreyren | 2022-05-23T11:35:06+00:00
> Your proposed solution is laughable. I take it you would need to have some sort of institution go around the globe and inspect people's mining setups so you can issue these mining licenses and hope that they don't change it after you leave -- @ethark (https://github.com/monero-project/monero/issues/8343#issuecomment-1133545283)

There is already multiple entities who focus on the certification of various technological infrastructure e.g. https://www.hetzner.com/assets/Uploads/Oomi-sertifikaatti-tuuli+vesi-Hetzner-2021.pdf who are then responsible for the enforcement.

So from a management point of view monero can just declare list of recognized certifiers and then any miner providing proof of their certificate can then be recognized as using ecological system.

(at least that's how it works practically for system administration for monero this process just has to be proven cryptographically)

> At that point, why not just have the CAs sign all blocks, eliminating the need for miners altogether? -- @ethark (https://github.com/monero-project/monero/issues/8343#issuecomment-1133545283)

No, in my proposal you can always mine without the certificate, but having the certificate is going to increase your rewards.

> What stops a CA from selling signatures on the black market for kickbacks? -- @ethark (https://github.com/monero-project/monero/issues/8343#issuecomment-1133545283)

Two answers:
1. Going through the use of entities who focus on certification such as the one provided above -> This is mitigated.
2. Going through the fully decentralized method where anyone can be a certifier -> My idea of the implementation is escrow-like service that inspects the miner's setup and then certifies it appropriately. If there is a process of punishing escrows who abuse the system and reliable way to report these for action then i see that as manageable system

>  What stops a miner from using their certificate from a solar-powered miner to authenticate their blocks mined from a coal-powered mine across the globe? -- @ethark (https://github.com/monero-project/monero/issues/8343#issuecomment-1133545283)

First thing that comes to mind is fingerprinting the system so that if the hardware changes the certificate fails.

> If you are so concerned about the emissions of PoW cryptocurrencies, and you are so willing to sacrifice any and all decentralization to achieve power efficency -- @ethark (https://github.com/monero-project/monero/issues/8343#issuecomment-1133545283)

i don't want to sacrifice on decentralization with this proposal and proposed ways to make this process decentralized without any limits on the current system in place.

## Kreyren | 2022-05-23T11:47:48+00:00
> That rhetoric of "one visa transaction takes 200x less energy and harms the planet significantly less then one BTC transaction" is misleading. -- @ethark (https://github.com/monero-project/monero/issues/8343#issuecomment-1133548333)

It is missleading, but it's the most common argument i keep hearing and that is efficient as argument against crypto.

> It alarms me that you don't seem to understand just how backwards your solution is. Your solution is the equivalent to converting your car into a horse-and-carriage to improve it's fuel economy. -- @nahuhh

More like having the economy in place to make it economical to upgrade the system while rewarding people for doing their part to manage climate change.

So in your car analogy using imaginary values say pizza delivery guy using car for delivery making constantly 24 pizza deliveries per day and making 300 USD/EUR (12.5 USD per 1 pizza).

Ideologically my solution expects to reward the guy for not polluting the earth so assuming that engine swap for an electric or even buying a new electric car is ~2000 EUR/USD (assuming that they sell their modern/modernized car) it would take ~7 days for the guy to be able to afford it while having to pay for essentials such as food and not having any motivation to do this upgrade.

I want to announce that if the delivery driver is using e.g. an electric car that they will be rewarded 5% on each delivery -> This makes it significantly more economical to do the upgrade especially for a long-run while providing additional funding to do the upgrade.

## nahuhh | 2022-05-23T13:33:56+00:00
> not polluting the earth so assuming that engine swap for an electric or even buying a new electric car is 

Do you think electric cars run on solar and wind power? Or that lithium MINING for battery production is environmentally friendly? Or perhaps battery disposal is? 

@Kreyren, close this please.

## ghost | 2022-05-23T14:10:54+00:00
> No, in my proposal you can always mine without the certificate, but having the certificate is going to increase your rewards.

It doesn't matter because miners with the cert will outcompete miners without. This is just letting the CAs dominate the network with an extra step.

> First thing that comes to mind is fingerprinting the system so that if the hardware changes the certificate fails.

Care to enlighten us as to how you might feasibly accomplish such a thing? Seeing as it will be absolutely necessary for the system to function at all...

>    Going through the use of entities who focus on certification such as the one provided above -> This is mitigated.
>    Going through the fully decentralized method where anyone can be a certifier -> My idea of the implementation is escrow-like service that inspects the miner's setup and then certifies it appropriately.

It's not fully decentralized at all. Becoming a CA effectively requires the permission of a top-level CA. Who decides who gets to be a top-level CA? Having multiple tiers of CAs doesn't address the problem at all, it just multiplies it.

> If there is a process of punishing escrows who abuse the system and reliable way to report these for action then i see that as manageable system

Do you have any idea how such a system might be implemented in the first place? At this point, the "decentralized" system you've described for handing out these mining licenses is more complicated than the rest of monero itself.

> i don't want to sacrifice on decentralization with this proposal

well, you've failed seeing as your proposal basically defeats the purpose of PoW cryptocurrencies in the first place.

> I want to announce that if the delivery driver is using e.g. an electric car that they will be rewarded 5% on each delivery -> This makes it significantly more economical to do the upgrade especially for a long-run while providing additional funding to do the upgrade.

In any real-life situation the environmental cost could simply be reflected in the cost of fuel, perhaps through some tax. That's an example of a simple, effective incentive structure that doesn't require pervasive surveillance like what you have described here.

The purpose of the car/carriage example is to say that what you are describing is repurposing something initially built for one thing for such a completely different purpose that it is inefficient at accomplishing either purpose (Imagine a horse trying to pull a heavy gas car, it's over-complicated and inefficient).

If you want an energy-efficient currency, then fork this and make it PoS. PoS has the same trust assumptions you are already making, and it hardly uses any energy at all. There's no need for all this complicated intermediary crap.

## ghost | 2022-05-23T14:19:53+00:00
Sorry if that last message came off as a bit too negative. But you have to understand that what you're describing is completely ridiculous, which is why others have strongly disagreed with it here even if they did not decide to refute it point-by-point.

## Cactii1 | 2022-07-20T00:49:08+00:00
I propose that we close this "issue".

# Action History
- Created by: Kreyren | 2022-05-19T20:06:46+00:00
- Closed at: 2022-07-20T00:50:16+00:00
