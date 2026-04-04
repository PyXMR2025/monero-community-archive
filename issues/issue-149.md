---
title: bot nets (preventing/stopping)?
source_url: https://github.com/monero-project/research-lab/issues/149
author: MichaelTen
assignees: []
labels: []
created_at: '2025-10-11T00:45:25+00:00'
updated_at: '2026-02-25T14:18:14+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
has there been any discussion how to modify Monero XMR protocol to stop or prevent or disincentivize botnets?

started here first. closed (https://github.com/monero-project/monero/issues/10145) 

# Discussion History
## fluffypony | 2025-10-11T03:21:54+00:00
A computer mining Monero is a computer mining Monero. It's not our job to police who is operating the computer and under what circumstances.

Even if we had to hypothetically come up with some way of doing this (practically impossible), should we also have them prove they're paying for electricity to prevent stolen electricity being used?

We are not gatekeepers.

## MichaelTen | 2025-10-11T06:38:51+00:00
its not literally policing. 

unless one has abnormally inexpensive or free power, mining monero is not profitable. 

bot mining may play a role in reducing profitability . 

ethics aside, - reducing the ability for bot mining of monero - i.e. done without user consent could make mining monero intentionally be closer to profitable or profitable for more people? 

the hash rate is going up. the price is going up. but XMR usage is basically flat for the last 3 years. 

perhaps profitable mining could help on ramp more users to XMR and might increase liquidity and eventually increase transaction # count. 

"should we also have them prove they're paying for electricity to prevent stolen electricity being used?" <-- no. 

it would seem a way of deterring bot nets would be somehow having monero mining maybe do something on windows or linux systems which inherently shows the user or admin of the system something is going on.. 

like anti cheat systems for video games. 

"Even if we had to hypothetically come up with some way of doing this (practically impossible),"

everything is practically impossible until someone figures out how to implement it. 

This is "research-lab" ... i am curious if others have thoughts on this. I am not sure how many actually participate in  research-lab

so... if you don't think its worth even considering OK. maybe others do. ty ty for your feedback and thoughts on the matter. limitless peace. 

## fluffypony | 2025-10-11T12:19:20+00:00
Even if you could have "monero mining maybe do something on windows or linux systems which inherently shows the user or admin of the system something is going on" that can't be done in the kernel of the miner, which is just a hashing algorithm. Mining software that doesn't do this would be trivial to create.

I say it's practically impossible because of how computers and operating systems and mining and cryptography works, not because there's some unknowns that exist. The solution to botnet mining is ASICs, not trivially defeated software tricks, and the Monero community has rejected ASICs.

## MichaelTen | 2025-10-26T07:33:04+00:00
Bitcoin did not exist until the byzantine general problem was solved. 

Perhaps this is an analogous dilemma for Monero. 

It seems impossible to solve until it isn't. 

How could any ethical Monero user support the nonconsensual botting of computers? 


## MichaelTen | 2025-11-01T18:05:37+00:00
I have been thinking about ways to make CPU mining fairer and to discourage botnets from dominating hashpower. what if miners actually had to prove they possessed the full blockchain, not just compute hashes through a lightweight proxy (as is the case currently)? for good faith miners, needing some storage to mine may be an ok trade off it they did not have to compete against bot nets for profitability. 

how it might be made possible... 

To make this idea real, you’d need a consensus rule or pool-side proof mechanism that requires miners to demonstrate full-chain possession. a few possible models come to mind:

Challenge-response proofs: the protocol could issue random block-hash challenges from anywhere in the chain; the miner would need to respond with valid data chunks quickly. failure to respond would disqualify them from earning rewards.

Proof-of-storage / proof-of-replication hybrids: something akin to Arweave or Filecoin but paired with Monero-style proof-of-work.

Chain-integrity work: embed a hash of random old blocks directly into the mining algorithm, forcing miners to read real blockchain data continuously... linking disk i/o to mining eligibility.

This would be a significant change, but potentially realistic if miner and dev consensus agrees that botnets are a significant problem for good faith miner profitability. 

that last one feels the cleanest to me. it keeps the process cpu-bound while making it storage-aware enough that botnets without full local chains couldn’t compete.

## PPPDUD | 2026-02-25T14:18:13+00:00
> Bitcoin did not exist until the byzantine general problem was solved.
> 
> Perhaps this is an analogous dilemma for Monero.
> 
> It seems impossible to solve until it isn't.
> 
> How could any ethical Monero user support the nonconsensual botting of computers?

It's not like we're just mining for the sake of mining, we have a financial incentive and the botnets defend us from threats like Qubic.

# Action History
- Created by: MichaelTen | 2025-10-11T00:45:25+00:00
