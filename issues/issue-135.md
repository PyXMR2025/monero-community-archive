---
title: Finality Layer
source_url: https://github.com/monero-project/research-lab/issues/135
author: kayabaNerve
assignees: []
labels: []
created_at: '2025-08-08T18:34:56+00:00'
updated_at: '2026-01-25T01:51:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
We can introduce a finality layer to Monero to prevent deep re-orgs. If the finality layer is sufficiently responsive, we can also use it to reduce the 10-block lock. This issue means to define criteria for and explore a finality layer.

Requirements:
- Achieve BFT consensus
- Prevent re-orgs
- Be runnable regardless of hardware/anonymity

Nice-to-haves:
- Achieve finality in less than 20 minutes
- Prevent censoring blocks

In order to achieve BFT consensus, we require defining a set of validators. The most trivial way to do this is via XMR, with other options existing (assigning anyone who mines a block `1 stake`, a secondarily mined token, etc). We'd define a set of validators for some time period, then update the list with the next epoch.

For the choice of consensus algorithm, we would be looking for _asynchronous BFT_ algorithms in order to ensures nodes can be run over _latent/erratic connections_ (such as Tor or i2p). I've personally chronicled some here [here](https://github.com/serai-dex/serai/issues/333), my personal preference at this time being https://eprint.iacr.org/2024/677. It doesn't have optimal communication complexity, and does have larger bandwidth usage, but we shouldn't have to be too concerned about the constants when discussing a block time on the scale of minutes (not seconds). The communication complexity will prevent thousands of participants in consensus however.

Validators could do one of two things:
- Agree on a historical block, cementing it on-chain
- Agree on a freshly mined block, adding it to the chain

The former only requires we come to consensus once every N minutes. The latter requires we come to consensus every two minutes. It'd remove the 10-block lock however, as any block actually added on-chain would be finalized.

Note if the finality layer stalls, finality does. As service providers should only accept finalized blocks, and ideally we come to consensus less than every 20 minutes _and_ re-define the 10-block lock as the finalized-block lock (where finalizations from the finality layer are then mined into the next block added to the blockchain), this would be effectively equivalent to a chain stall (even if the chain itself continues to be added to). Note that a captured finality layer can be used to censor blocks from being added to the blockchain.

If we adopt the timelock proposal described in #129, for private timelocks indistinguishable from normal transactions, a validator can use a ZK proof to claim their 'stake' on the finality layer without revealing which output was the staking transaction. We would still require knowing the sum amount of stake, so every Monero output would be extended with a _non-forward-secret_ ElGamal commitment _encrypted to the current validator set_ of either the output's amount (if a staking transaction) OR `0` (if not a staking transaction). This way, the validators can decrypt the next validator set's total stake as necessary to evaluate if a sufficient threshold has been reached. If malicious, the validators can also decrypt individual outputs to see if they're stake TXs/for how much, but this is still _more private_ than publishing stake transactions out-right (another option, which itself may be fine). This would require the current validator set perform a DKG, which I've done work on for Serai and should be able to shortly publish security proofs for a competent, applicable scheme (which I've implemented for Serai). A slashing mechanism still must be defined if we don't publicly reveal stake outputs on the Monero blockchain itself. Presumably, we allow the finality layer to trace any validator who misbehaved, prove to the Monero blockchain they are slashing an output used for staking, and slash arbitrary staking outputs accordingly.

# Discussion History
## kayabaNerve | 2025-08-08T18:38:47+00:00
I personally like the definition where validators achieve consensus however often, and we replace the 10-block lock with a finalized-block lock. If we optimize the consensus layer enough, it'll be instant finality. Else, it'll be whenever finality.

We can presumably require any staking transactions be for a flat amount of XMR, and if we get over-subscribed w.r.t. validators and current finality layer performance, we can shrink the validator set to a set maximum capacity by random elimination _while simultaneously_ increasing the XMR stake required moving forward (so the next set of candidates won't be larger than the maximum capacity).

## kayabaNerve | 2025-08-09T00:27:02+00:00
A malicious 51% of hash power can still censor transactions. We'd likely have to require transactions be eligible to be _force-included_ via the PoS layer to prevent this, or we'd have to revisit #134 which fundamentally didn't work _because_ it couldn't define finality and was always at risk of deep re-orgs (which this issue solves). Force-inclusion would be by:

1) Having the PoS finality layer produce a finalization, including any force-included transactions
2) Including the finalization on the PoW blockchain, therefore including the force-included transactions
3) Only finalizing blocks which include the prior issued finalization

As for submitting transactions to be force-included to the PoS layer, that's a more complicated discussion. Presumably, we'd have the PoS validators attempt to include it in the traditional methods, and then after locally observing `n` blocks it could have been included in yet wasn't (despite being accepted to the mempool), propagating it for inclusion within a finalization?

## kayabaNerve | 2025-08-09T00:43:56+00:00
It should be noted, under this proposal, the primary purpose of PoW is two-fold:

1) To advance the chain on a consistent time interval (whereas the PoS finality layer finalizes a block whenever it manages to achieve consensus). If the PoS finality layer achieves latency of less then two minutes, which will be variable on set size and network topology yet still likely IMO, then this is irrelevant.

2) To reduce the complexity of consensus. Instead of attempting to come to consensus on a set of transactions to define as the next block (potentially hundreds of TXs eligible for inclusion), the nodes are only attempting to come to consensus on a block (and there should only be one or two blocks for any given block height).

## runatyr1 | 2025-08-12T05:47:50+00:00
Hi @kayabaNerve I was thinking how to use the existing PoW in Monero but achieve a large consensus (~90%) before the normal 2 block time in the PoW chain. Please note I have limited dev experience and may be making incorrect 
assumptions - just sharing these ideas in case they're useful for discussion.


PoW-Derived Fast Finality Layer
Sybil resistance: Only recent miners can solve micro-puzzles
No additional staking: Uses existing PoW infrastructure  
Overlay design: Doesn't interfere with base consensus
Optional initially: Can be tested without protocol changes

Overview:
It uses micro-puzzle based on recent block from PoW layer to locally verify honest miner quickly. Then adds its own shortened signature (nullifier) to the accumulator or detects if its duplicate (already voted) ie no change. If it changed the accumulator broadcasts the new message with new vote. There is an initial network discovery phase where we can determine the expected signature accumulator size. After some time the signature reaches the threshold size which means certain percent of miners have signed, eg 90%. 

More detail:
Verify valid miner locally and fast, before adding signature (sybil resistance):
Miner solves micro-puzzle using recent immutable block (N-100) as seed
If it was able to solve the micro-puzzle locally from a recent block it means its a valid miner
Challenge = hash(block_N-100 + block_N-1 + miner_pubkey)
Must find nonce where:  hash(nonce + pubkey)  < difficulty_target
Nullifier = hash(nonce + miner_pubkey + current_block_hash)

Signature accumulator and deduplicator:
Signature_accumulator = [nullifier_A, nullifier_B, nullifier_A, nullifier_C]
final_hash = hash(sorted(uniq(signature_accumulator)))

Broadcast:
Node broadcasts (block_hash, current_signature_accumulator)
Random 30sec delay protects from initial broadcast storm
Each miner adds their nullifier: new_accumulator = hash(old_accumulator + my_nullifier)
Re-broadcast the updated signature_accumulator if it changed 
Or not rebroadcast if it doesn't change (already signed)

Network size discovery and consensus threshold:
Initial network discovery phase broadcasts nullifiers to estimate total miner count (discovered_network_size)
Expected_max_accumulator_size = discovered_network_size * 0.90 (if we want 90% participation target)
Consensus reached when: len(unique_nullifiers) >= Expected_max_accumulator_size

## kayabaNerve | 2025-08-12T06:41:46+00:00
PoW on top of PoW wouldn't work. While we can define stake as the amount of blocks mined within the last 24 hours, that wouldn't increase security against an adversary who can maintain a 51% attack for 24 hours.

## kayabaNerve | 2025-08-12T16:46:06+00:00
Asynchronous BFT isn't inherently more centralized than partially-synchronous BFT. One works with asynchronous networks (networks where the adversary controls when messages are routed) and one works with asynchronous networks for safety (safety holds even when the network is asynchronous) yet synchronous networks for liveness (progress is only made when the network satisfies various timing assumptions).

Asynchronous BFT is a more complicated field field however. The immediate partially-synchronous BFT algorithms (such as Tendermint, HotStuff) are near optimal if not optimal for their choices, while asynchronous BFT algorithms will be notably slower.

The reason to focus on asynchronous BFT is because progress occurs as it can, not as everyone can respond to messages within one second. This will allow people to run validators behind networks such as Tor, i2p, Nym, etc, with the only impact being how often finalizations occur, not if they are at all. This same property also causes some high-performance networks to use asynchronous BFT as the overhead of the consensus algorithm can be better realized than hard timings of partially-synchronous BFT (in asynchronous BFT, everyone moves forward when ready, while in partially-synchronous BFT, everyone must wait for timers to expire even if all messages have already been received).

## techmetx11 | 2025-08-13T17:50:48+00:00
Forwarding the comment I made in [#136](https://github.com/monero-project/research-lab/issues/136#issuecomment-3184452081) because I think it's more relevant here:

> The finality layer could be a modified form of PoS, where you can get a stake on the blocks you've mined (this can be tied to the P2Pool coinbase transactions too) but if you send over any rewarded XMR, it will be deducted from the amount of stakes you currently have.
> 
> This would mean:
> 
> 1) the richest people in Monero aren't just gonna get a ton of stakes over others
> 2) centralized pools would be the minority in the the list of validators, unless they heavily increase their fees or refuse to pay out miners
> 3) this would benefit independent miners, big or small, over pools


## FocuzJS | 2025-08-14T05:57:43+00:00
My proposal is for a PoW-bonded finality gadget 

Each block includes an ephemeral finality key and splits its coinbase into a regular reward and a time-locked bond; the next M PoW winners each add a tiny signature vote (e.g. Ed25519 in the header/extra) to finalize the block K deep; when ≥2/3 of those votes are seen, nodes mark that block finalized and reject any reorg conflicting with it; if a miner double-votes on competing forks with the same key, a short equivocation proof burns that block’s bond, while honest miners’ bonds unlock only after their votes have finalized.

This enables a slashable, in-protocol finality with no external/long-lived validators.

For example: 
  K = 20 (vote on blocks ~20 deep to avoid tip churn)
  M = 100 (collect votes from the next 100 winners)
  Threshold = 67 votes (≥2/3),
  Bond = 15–25% of the coinbase, unlock after ~K+M+Δ blocks. (Higher = stronger deterrent, worse miner cashflow; too low = cheap to bribe.)

With this, a block at height 1,000 becomes finalized once, say by height ~1,120, 67 of the next 100 blocks voted for it. After that, nodes won’t follow any chain that rewrites height 1,000.

To rewrite a finalized block, an attacker must convince dozens of recent PoW winners to equivocate and get slashed. This puts an additional price tag on deep reorgs while remaining completely PoW. 

Unfortunately I don't believe this alone achieves either of the nice to haves but I find it to be more aligned with the Monero ethos and more digestible finality mechanism than the former.

## kayabaNerve | 2025-08-14T07:09:35+00:00
@FocuzJS You can't use PoW descending from the block you want to finalize to finalize it. That would trivially allow multiple equivocations. 

## techmetx11 | 2025-08-15T15:30:54+00:00
> Firstly, we should try to force at the network level that it is entirely run over a single anonymity network, preferably I2P as it is designed better for this kind of workload, this makes it significantly harder to target/attack by well resourced attackers
> (fixes easy to target)

Impossible to actually enforce at the network-level, I guess only individual nodes or software can care about where you're being connected.

> We should absolutely NOT allow delegation (dPoS) which is structurally centralising by design, but choose a model closer to Ethereum, where you must stake your own XMR only, now I know that Liquid Staking has centralised Ethereum away from its ideological goals, but I do not believe this will happen in Monero because we lack smart contracts, we should also ensure unbonding action is possible straight away

What about centralized exchanges (CEXs)? What about someone who has a massive reserve of XMR they can use (like the richest people of Monero)?
There should be some form of decentralized delegation like P2Pool, and not just let the PoS finality layer be taken over by people who have very deep pockets


## techmetx11 | 2025-08-15T15:40:18+00:00
> But yes it would be the richest 256 to 512 ideological aligned cyperpunks which also happen to have sufficient technical experience

You do not know what they're aligned with or if they're even "cypherpunks", They are just validators

## techmetx11 | 2025-08-15T15:54:03+00:00
> > You do not know what they're aligned with or if they're even "cypherpunks", They are just validators
> 
> Okay that is true I concede, we cannot be sure they are "cypherpunks", but the only people willing to lock up XMR for a minimum of 1 year would be people who believe in the token long term (for at least 1 year anyway) by definition

Well I am willing to agree with this, If there's a bond lock, then the richest can't just stake or unstake whenever they want. (and their funds are perfect for this)
But I think requiring an anonymity layer should be reserved for individual implementations of Monero (also I don't know about dragging I2P as a dependency to the main implementation), rather than a change to the network consensus.
1 year is also a bit extreme, Maybe 1 month bond-lock

## techmetx11 | 2025-08-15T19:02:23+00:00
> Thats the point, it filters for only those truly aligned with the network long term,
> dis-incentive for both CEX's staking and perhaps more importantly, out of protocol staking pools, which could capture the network.

How about 3 months? 1 year seems a little too extreme

## techmetx11 | 2025-08-15T19:16:40+00:00
> > How about 3 months? 1 year seems a little too extreme
> 
> I could see 3 months working too, the only reason to have a lower bonding period is to accommodate those that might want to unbond and sell, which is obviously against the protocol's health
> 
> We want validator to come online, stay online and put care, attention and dedication towards maintaining and optimising their validator security and performance
> 
> Perhaps the correct way to find the right bonding period, is to start on the far end with 1 year, if we do not see enough validators come online, then slowly reduce the bonding period in steps towards 3 months,
> 
> This way the market will tell us what the correct number is.

Even if you chose a duration, wouldn't the validators be able to unbond whenever they like after 1 year/3 months/1 month?
Unless they have to rebond again to continue earning rewards on staking (this can be done manually by user intervention or configured to be automatic)

## techmetx11 | 2025-08-15T19:31:32+00:00
> A validator issues an unbond command to the network, they would stop earning rewards and be ejected from consensus and then only after 1 year after issuing the command they will get their initial XMR bond back, not 1 year after starting to validate

Oh I see, I was mistaken. That actually makes more sense
3 months is still more reasonable than 1 year. We don't want to disincentivize validators too much with the bond-lock time 

## techmetx11 | 2025-08-15T19:48:12+00:00
> Perhaps the correct way to find the right bonding period, is to start on the far end with 1 year, if we do not see enough validators come online, then slowly reduce the bonding period in steps towards 3 months,

Developers are not gonna keep hard-forking just to adjust the bonding period just right. It would be a waste of resources and would probably hurt the coin with each frequent hard fork.
There should be a reasonable amount of time from the first change, like 1 month or 3 months

## techmetx11 | 2025-08-15T19:57:33+00:00
> Because the finality layer is a separate network and codebase/binary, we can do rapid hard forks without the same drawbacks as a traditional monerod core hardfork

Realistically, you cannot seperate the finality layer like this, it HAS to be completely apart of Monero's network in order to act on PoW-mined blocks (or at least, without being yet another permissioned system and has its own problems regarding stability)

> At worst, we lose finality for a bit until the finality layer comes back online (a super majority of validators upgraded to new version)

So someone can simply DDoS the finality network to disable it?

Seperating the finality layer sounds like you're negating the benefits by making yet another point of failure

## techmetx11 | 2025-08-15T20:15:09+00:00
> > Realistically, you cannot seperate the finality layer like this, it HAS to be completely apart of Monero's network in order to act on PoW-mined blocks (or at least, without being yet another permissioned system)
> 
> Im not sure I agree with this, the mental model I had in my head, is it would look quite similar to Ethereum exection layer (Monero PoW chain) and beacon chain (Monero PoS chain), ad pretty sure I saw it mentioned to be proposed as 2 separate networks linked together, probably reading each other over an RPC/WSS interface

I think Ethereum has this design because they have smart contracts, while Monero doesn't, so we shouldn't need a seperate chain

> 
> > So someone can simply DDoS the finality network to disable it?
> 
> This is one of the reasons I am arguing for enforcing it to be default over I2P, to make it much harder to identify and attack a validator, either technically or by abusing corruptible legal systems
> 
> If the entire network ran as a darknet finality layer, the validators would over time build long lived I2P tunnels to each other, an attacker even if they enter the I2P darknet would only be able send a DDoS over their I2P tunnel to a validator, and an I2P tunnel isnt big enough to to allow enough bandwidth down to cause resource starvation the validators machine
> 
> And of course you cannot identify the clearnet IPv4 address to attack via traditional means
> 
> They would of course though, be susceptible to any I2P specific vulnerabilities

I think it would be better if it was just a finality layer inside the Monero chain, rather than making a seperate chain
Darknet stuff should be up to the individual implementations

## kayabaNerve | 2025-08-16T02:06:13+00:00
Ethereum uses a separate binary because the components infrequently interact, it allows developers to only write one (an execution or consensus client) however they'd like, and they can be mixed and matched (due to a standardized RPC between the two).

The finality layer cannot exist on the Monero blockchain because the Monero blockchain isn't stable (hence the finality layer). It'd be a peer-to-peer network (presumably not its own blockchain) which observes the Monero blockchain. One could either build it into monerod or as its own binary.

Since we currently have two blockchain node implementations, it'd make sense to be its own program so both can immediately use it. Building it into monerod would require Cuprate reimplement it.

Additionally, depending on how the two layers interact, most users may not need to run a finality layer node, so it may be slimmer to keep the two separate.

## ovhpse | 2025-08-16T13:04:15+00:00
Hello,

I have been reading all the interesting conversations about the finality layer, and it's great to see so much intelligence being put at finding a long term solution that would prevent a future reorg attack.

I see that the opponents to PoS worry that it will lead to centralization and lazy gains for whales and I would like to present a potential solution to this issue.

The core idea is to make PoS operationally risky and burdensome to limit centralization and ensure that staking require a great dedication to the network, while also advantaging small stakers.

Consider the following constraints on staking:
- The Monero daemon on the staking node must have access to the stacking wallet private key.
- We know how much stake each node have.
- We limit the amount of stake possible per wallet.

This make the staking nodes an interesting target for attackers looking to steal XMR, which is the intended effect. Staking won't be a passive activity (especially for the delegated kind), but will require to actually work to secure your node.

As we will have different kind of stakers with skills in different technologies, the network will strengthen by having a pool of well secured nodes using different kind of setup:
- Different OS and Linux distributions.
- Some running as a service, some in containers.
- Different CPU architectures (maybe some exotic stuff, like RISC-V, ARM CHERI, PPC...).
- Different hardening ideas.
- Running in a variety of location, from on-premise to different clouds.
- Different network topologies.
- In the future, different Monero daemon implementations.

Why does this advantage the small stakers over large stakers:
- Large stakers have to maintain many nodes, so they will have the same overhead as small stakers per stacked XMR.
- They can automatize the installation, but then an attacker may detect nodes of the same family by different kind of probing techniques, one node breached can rapidly lead to the other ones getting the same treatment.
- They can diversify their deployment type, but they need to have a larger skill set encompassing different technologies.
- They can outsource the management, but it is a cost and they need someone they really trust.
- Also they might better choose to not put all their wealth in a risky enterprise like this.

It should be noted that if a node fail to validate transactions, it shouldn't be slashed, but just quarantined. We should ensure that emergency shutdown or network disconnection is a viable defense strategy. This will also ensure that not everyone will go to high SLA cloud providers.

On the Monero side, the implementation should take the form of a small new daemon, let's call it the signing daemon. To start staking, you will need to:
- Start the signing daemon, which will open a socket (Unix or IP), and wait for the private key.
- Launch a small command line utility that ask for the private key, and register it in the daemon.
- The daemon will encrypt the key in memory as password managers do.
- The `monerod` daemon, configured for staking, will poll a `ready` endpoint on the signing daemon socket.
- When the key is registered, the daemon will signal it's readiness, and `monerod` can start staking.
- The daemon have endpoints to sign staking related things (like block signing), but can't sign regular transactions. It protect at least the staker from having the private key in clear-text configuration files or in the `monerod` memory space (internet exposed).

I know we could go further in the signing daemon hardening (mlock, memory zeroing, optional TEE...), but it's a good start.

Otherwise I don't think the Monero team should give any help about the node hardening, it would defeat the goal of diversifying the installation methods while putting responsibilities on the Monero dev team they should not have. We should also advise peoples to not share everything about their hardening so we avoid that a large part of the network run the same `shutdown_on_suspicous_activity.py` and expose the network to a large scale DoS attack.

I also think the staking nodes should accept incoming connections. The network can't work with outgoing connections only nodes and for the moment there is no incentive to build a node accepting incoming connections outside of having an altruistic mindset.

We need many small, talented stakers who think differently to secure the network, and I think this proposal could help us reach this goal.

## ovhpse | 2025-08-16T15:09:00+00:00
@Deltamax1 

The whole point of my proposal is to address the "lazy staking" issue, which is a legit concern IMHO. Peoples would want to take this risk to be able to collect staking rewards. Maybe the proposal is too harsh and could be relaxed. But I think making staking a risky business would reduce centralization pressure and incite stakers to run well secured nodes. I don't expect small stakers to be physical targets, they will just have to sustain remote attacks on their nodes.

Low block rewards doesn't reduce centralization, quite the contrary. You will break-even only if you don't pay for the node (exchange based staking), or if you have very much to stake.

## techmetx11 | 2025-08-16T16:16:35+00:00
My initial idea was to only be able to stake coinbases (mined XMR), They are public outputs which means others already know how much you got in mined XMR (and whether if they're spent, but that applies to any outputs), you can't just stake XMR obtained from other sources (which incentivizes PoW), and can be slashable by invalidating coinbase outputs

Nothing more, really

## techmetx11 | 2025-08-16T16:51:44+00:00
> The daemon will encrypt the key in memory as password managers do.

> * The daemon have endpoints to sign staking related things (like block signing), but can't sign regular transactions. It protect at least the staker from having the private key in clear-text configuration files or in the `monerod` memory space (internet exposed).

If your threat profile includes the attacker being able to read keys from your RAM, you might aswell give up on this until you get a CPU that can read and decrypt straight inside the die (like AMD Secure Memory Encryption)
 
> This make the staking nodes an interesting target for attackers looking to steal XMR, which is the intended effect. Staking won't be a passive activity (especially for the delegated kind), but will require to actually work to secure your node.

Why should this be intended? Should it be intended that if I mine on my computer, I should be sleeping near it in case somebody breaks in and steals it?

## kayabaNerve | 2025-08-16T18:29:51+00:00
While we can require stakers hold the private key in RAM, painting a target, we can also simply require a key to use for consensus. This would allow coins stored on a hardware wallet to be staked, without loading the seed into the validator, and still requires access to the coin's private key _to some degree_. Controlling how rewards are distributed in a complimentary fashion can likely significantly hamper, even if it can't out-right prevent, delegated validation.

## sethforprivacy | 2025-08-16T19:14:09+00:00
The vast majority of the details here are above my pay grade, but I will just say that I've always loved how Decred handles hybrid PoW/PoS to allow stakers to act as a finality layer (of sorts), with only blocks signed off my a majority of selected stakers able to be added to the chain, while also allowing stakers to slash PoW mining rewards when malicious activity is detected (i.e. mining empty blocks or mining in secret) even if that activity is technically consensus-compliant.

There is more detail in their docs, but note that I am only referring to the consensus aspects of their staking, not the governance aspects (i.e. voting on forks) for the purposes of this ticket.

https://docs.decred.org/proof-of-stake/overview/

## yonder83 | 2025-08-19T20:21:36+00:00
The whole finality layer idea sounds like an overly complicated solution to a problem that doesn’t really exist. The fear of a 51% attack turned out to be unfounded. The network’s hashrate has been steadily increasing, which indicates ongoing interest in mining. People genuinely trust Monero in its current, functioning form. Tweaks like this can easily cause more harm to the project than good. No PoS mechanisms or Finality Layers should be introduced.

## PPPDUD | 2025-08-22T16:30:41+00:00
Stakes? Second token? Layer‽ Is this some Tari jargon I'm not grasping?

## WrinklyEarpieceDiagram | 2025-08-24T00:41:53+00:00
cc: @reubenyap @QuantumExplorer

$FIRO and $DASH both have implemented masternodes of some kind of hybrid system with masternodes seems like maybe a good idea for Monero?

However they aren’t a “finality layer” in the same sense as the final‑state commitment mechanisms you find in many proof of stake (PoS) blockchains.

## kayabaNerve | 2025-08-24T14:28:56+00:00
Chain locks have already extensively come up in reference @WrinklyEarpieceDiagram 

## kayabaNerve | 2025-08-25T09:12:53+00:00
If finality stalls for an extended amount of time, one measure could be an inactivity bleed (restoring synchronous consensus) or the community could perform a social slash by hard forking to slash all current validators and restart the selection process.

## runatyr1 | 2025-08-27T20:32:58+00:00
Hi @kayabaNerve  my understanding is that this are the methods mentioned by the proposal so far.

- Using XMR holdings directly (traditional staking)
- Assigning one stake to anyone who mines a block
- Using a secondary mined token

But what about instead, using locked mined XMR?  

We could create a special public miner address for each miner where mining rewards are accumulated, if rewards are not withdrawn after a few months you gain validator status. If you sell rewards you loose validator status.  

It helps to protect against:
- Rented hash attack
- Qubic-like sell + pump shitcoin scheme
- Big XMR holders taking over

We could call it locked miner reward validation or something different than PoS as it is not the same of the traditional PoS where you deposit funds which is also very contentious issue for the community. 

The miners that haven't sold their mined XMR and become validators could also get increased rewards, to incentivize this long-term miner reward locking. Eventually they could withdraw certain percent of their rewards without loosing validator status and increased rewards.

## taoeffect | 2025-08-27T20:46:23+00:00
I have not looked at this in depth, however, any proposal to add an additional consensus mechanism to XMR has the following issues:

- It will create a significant amount of complexity, especially PoS, which is insanely complicated compared to PoW
- It will increase the attack surface on the network, as now it will be possible to attack either consensus mechanism to take down the entire chain. EDIT: so this proposal is strictly a worsening of security over the status quo.
- PoS, specifically, suffers from the buyout attack, which PoW does not. If you do not know what the buyout attack is, you probably shouldn't be even suggesting this.

## PPPDUD | 2025-08-27T22:05:21+00:00
> Hi [@kayabaNerve](https://github.com/kayabaNerve) my understanding is that this are the methods mentioned by the proposal so far.
> 
> * Using XMR holdings directly (traditional staking)
> * Assigning one stake to anyone who mines a block
> * Using a secondary mined token
> 
> But what about instead, using locked mined XMR?
> 
> We could create a special public miner address for each miner where mining rewards are accumulated, if rewards are not withdrawn after a few months you gain validator status. If you sell rewards you loose validator status.
> 
> It helps to protect against:
> 
> * Rented hash attack
> * Qubic-like sell + pump shitcoin scheme
> * Big XMR holders taking over
> 
> We could call it locked miner reward validation or something different than PoS as it is not the same of the traditional PoS where you deposit funds which is also very contentious issue for the community.
> 
> The miners that haven't sold their mined XMR and become validators could also get increased rewards, to incentivize this long-term miner reward locking. Eventually they could withdraw certain percent of their rewards without loosing validator status and increased rewards.

Interesting! This would also incentivize HODLing of mined XMR, which helps keep the price stable.

Edit: Wouldn't this cause privacy issues for p2pool miners? On p2pool, all miners have to reveal their primary address where rewards are sent, and the amounts mined are publicly visible. In a system where withdrawals are disincentivized, this could bring us closer to a BTC level of privacy.

## PPPDUD | 2025-08-27T22:10:52+00:00
> > The daemon will encrypt the key in memory as password managers do.
> 
> > * The daemon have endpoints to sign staking related things (like block signing), but can't sign regular transactions. It protect at least the staker from having the private key in clear-text configuration files or in the `monerod` memory space (internet exposed).
> 
> If your threat profile includes the attacker being able to read keys from your RAM, you might aswell give up on this until you get a CPU that can read and decrypt straight inside the die (like AMD Secure Memory Encryption)
> 
> > This make the staking nodes an interesting target for attackers looking to steal XMR, which is the intended effect. Staking won't be a passive activity (especially for the delegated kind), but will require to actually work to secure your node.
> 
> Why should this be intended? Should it be intended that if I mine on my computer, I should be sleeping near it in case somebody breaks in and steals it?

You expect to _sleep_ next to a cryptominer?

## runatyr1 | 2025-08-27T23:05:15+00:00
@PPPDUD thanks for checking the idea

_> Edit: Wouldn't this cause privacy issues for p2pool miners? On p2pool, all miners have to reveal their primary address where rewards are sent, and the amounts mined are publicly visible. In a system where withdrawals are disincentivized, this could bring us closer to a BTC level of privacy._

I think it could work like this:
1- input primary wallet address to miner software for withdrawals (same behavior)
2- p2pool miner software derives a special public address that has funds visible, to verify miner rewards are locked and earn validator status (new behaviour)
3 - mining happens and accumulates rewards in that public address and eventually become a validator
4- miner may trigger a withdrawal in the miner software which would be automatically made to the primary wallet address from step 1. If it doesn't leave enough locked funds, validator status is lost (and thus extra rewards).

Those funds held in public addresses can't really be used for transactions so it would not affect privacy. You could only leave them there, and people will know the miner is holding some funds, but that doesn't link to miner real identity or their physical location and if they decide to withdraw, funds return to the normal Monero privacy system

Also something about implementation it seems this change is easier for p2pool as you could track locked rewards without error using those side-chains. For centralized pools it could be acceptable to risk that the pool operator don't track locked rewards correctly, they could fail to pay locked rewards in the future. That would facilitate implementation as it doesn't seem possible to control centralized custom pool miners. It's also an incentive to use p2pool instead of centralized.

## taoeffect | 2025-08-27T23:37:08+00:00
Replying to @Deltamax1:

> There is basically no finality guarantees now, how would for security reasons a finality layer that only adds on top of PoW be somehow be worse than the status quo?

I suppose let me repeat myself again, and perhaps quote the proposal author, @kayabaNerve, who also says in the OP:

> this would be effectively equivalent to a chain stall (even if the chain itself continues to be added to). Note that a captured finality layer can be used to censor blocks from being added to the blockchain.

So this proposal is an AND operation. You take `SecurityOf(Consensus 1)`, and you `AND` it together with `SecurityOf(Consensus 2)`.

Previously, `Security(monero) = SecurityOf(Consensus 1)`.

With this proposal: `Security(monero) = SecurityOf(Consensus 1) ⋂ SecurityOf(Consensus 2)`

Thus a strict reduction in security, and more concretely, the security is reduced to whichever is easiest to attack, so it's more like: `Security(monero) = min(SecurityOf(Consensus 1), SecurityOf(Consensus 2))`

> By buyout attack do you mean something like a bribe? Because that is something absolutely that can happen in PoW

No.

I was surprised to see that if you asked an LLM it would be able to answer this question for you accurately. At least Opus 4.1 and GPT-5 both answered correctly.

A buyout attack is like a 51% attack except much worse, because it has no ongoing cost. Whereas with a 51% attack there's a possibility of a fight, with a buyout attack it's immediately game over.

## taoeffect | 2025-08-28T02:15:22+00:00
BTW if the goal here is to introduce finality to Monero there's really no reason to mess with the consensus layer and introduce more bugs and security problems.

A significantly simpler, safer, and more straightforward method is to have full nodes define a chain length past which they won't accept re-orgs, and boom there's your "finality layer".

## taoeffect | 2025-08-28T17:34:19+00:00
> I see, so the only difference is there's no on-going cost. Is this a conditional factor for your opinion on the matter? Because wouldn’t PoW still exist under the finality layer?

Once again, the system's security would be lowered to the lowest consensus mechanism when they are coupled like this, so PoW becomes irrelevant here.

Regarding my opinion, I've also stated it rather clearly: if you want finality, there is no reason to engage in self-harm. Finality is easily done with PoW alone as a simple constant in full nodes that defines the maximum allowable re-org. For all I know this already exists in Monero, and if it doesn't, it would be a very simple change to introduce.

> While mostly true that there would be a reduction to the weakest link it would not yield worse security than present as the weakest link is already in place.

The weakest link is not "already in place", if you are comparing PoW to PoS. PoW has significantly stronger security properties than PoS. It doesn't suffer from a buyout attack vulnerability.

While not all PoS algorithms use classical 2/3 quorum designs, the one linked in the OP appears to, which means 33% is enough to cause problems, as opposed to PoW, which is higher at 51%, and again, doesn't have a buyout attack problem.

> Mind you an adversary would also have to be mining simultaneously as finality doesn't give them control over block creation.

Except that it does, per OP:

> Note that a captured finality layer can be used to censor blocks from being added to the blockchain.

Regarding the math, AFAICT the equation is `x / (x + s) = 1/3` => `x = s / 2` where `s` is current stake size and `x` is how much you'd need to break consensus. So, this statement (and others like it) are incorrect:

> R: 1% of total XMR with staked would be worth ~50M. An adversary would need 100M.

With 50M staked you'd need `50 / 2` = `25M` to break consensus.

> Can you explain how that helps "Bolstering PoW to be Resistant to 51% Attacks, Censorship, Selfish Mining, and Rented Hashpower"? I can see how it might help solve deep reorgs but not necessarily the more immediate problems.

I'm not sure what your questions in this section are about. What "more immediate problems"?

This thread, and that thread, afaict, were spawned out of concern with regard to a mining pool either doing a deep re-org or having the potential to do a deep re-org.

So having full nodes reject such re-orgs fully addresses that problem in a more secure and simpler way than adding a PoS layer that would certainly significantly reduce Monero's security in both theoretical terms as well as practical terms.

With regard to running over Tor, I'm not sure why that's being brought up, but having full nodes reject long re-orgs is also more efficient over Tor than adding another consensus layer.

So in every single regard, whether it is the security perspective, or the performance perspective, or the simplicity perspective, the full-node approach is better.

> Under the scenario above wouldn't it now be impossible to fix under the canonical chain? So there goes that.

No idea what you're talking about.

> And once a genuine attack is successful confidence plummets, price drops, miners are disincentivized on spending hash, security drops, determined attackers now control more of the relative hash-rate. And until the attackers give up. Though not always it's usually marks the beginning of the end of the coin.

This is not a property unique to PoW. A successful attack on PoS would have similar properties, except worse, because the attacker would become a permanent fixture of the chain, requiring a manual hard fork to fix.

> Are hard forks impossible under a PoS finality layer?

Incidentally this raises an interesting question as Monero is supposedly a privacy coin, I'm wondering how this would be addressed in Monero with PoS. Monero is all about hiding who owns how much, but with a PoS system you'd need to know that information as otherwise you probably wouldn't be able to dislodge the attacker even with a hard fork.

> But sure it may not deterministic as PoS only the cost to attack is still multiple times higher.

I don't think you've shown this, as at one point the math was off for 1/3 stake, and also you didn't explain how you got `~$120k` as the cost to attack PoW. This part of the convo is somewhat irrelevant to the arguments I made, but I'm still curious what your reasoning is for that number.

> I'm just looking at eth and they have 35 million eth staked at ~4,500 per coin thats a total of $157.5B an adversary needs to get 2/3rd in a buyout would $105B and at the open market it would be $315B. They seem to be doing OK.

That's for getting 2/3 of the stake, but attacks of varying sorts can be done cheaper at 1/3 and 1/2 levels. Again, it bears repeating that all of these discussions of "costs to attack" are irrelevant as adding PoS doesn't improve the security of Monero, but makes it worse. Adding PoS on top of PoW doesn't magically make the PoW portion safer. PoW can still be attacked just the same, and all you're doing is adding a whole bunch of new code that can also be exploited.

It's like saying, "Oh no, burglars are entering the house through the front door! Let me add a back door too!"

If you want finality for PoW just have the full nodes enforce it. Way easier, safer.

## kayabaNerve | 2025-08-29T05:40:26+00:00
For the record, I'm largely not participating here as I find it too noisy. I'm hopeful my work on a book will resolve a lot of this, without me commenting on every message.

I want to clarify the introduction of a PoS finality layer would not be the worst of two security models. With the transition to a PoS finality layer, PoW's problem of unbounded reorganizations (its failure mode) is no longer defined. Instead, the discussion is on if finality stalls (preventing advancing the bound for which reorganizations are possible).

A maximum reorg depth is a horrible finality layer. It'd requires a completely synchronous network to work, as in, blocks immediately propagate over the entire network _and_ nodes are never offline. Else, net splits would simply be explicitly possible _even if the adversary can only cause them intermittently_.

## PPPDUD | 2025-08-29T14:37:12+00:00
> [@PPPDUD](https://github.com/PPPDUD) thanks for checking the idea
> 
> _> Edit: Wouldn't this cause privacy issues for p2pool miners? On p2pool, all miners have to reveal their primary address where rewards are sent, and the amounts mined are publicly visible. In a system where withdrawals are disincentivized, this could bring us closer to a BTC level of privacy._
> 
> I think it could work like this: 1- input primary wallet address to miner software for withdrawals (same behavior) 2- p2pool miner software derives a special public address that has funds visible, to verify miner rewards are locked and earn validator status (new behaviour) 3 - mining happens and accumulates rewards in that public address and eventually become a validator 4- miner may trigger a withdrawal in the miner software which would be automatically made to the primary wallet address from step 1. If it doesn't leave enough locked funds, validator status is lost (and thus extra rewards).
> 
> Those funds held in public addresses can't really be used for transactions so it would not affect privacy. You could only leave them there, and people will know the miner is holding some funds, but that doesn't link to miner real identity or their physical location and if they decide to withdraw, funds return to the normal Monero privacy system
> 
> Also something about implementation it seems this change is easier for p2pool as you could track locked rewards without error using those side-chains. For centralized pools it could be acceptable to risk that the pool operator don't track locked rewards correctly, they could fail to pay locked rewards in the future. That would facilitate implementation as it doesn't seem possible to control centralized custom pool miners. It's also an incentive to use p2pool instead of centralized.

Monero is currently having an influx of new miners, so we probably shouldn't try to change the way their favorite decentralized pool works on the outside.

## taoeffect | 2025-08-29T16:25:34+00:00
> A maximum reorg depth is a horrible finality layer. It'd requires a completely synchronous network to work, as in, blocks immediately propagate over the entire network and nodes are never offline.

~~As this is a total lie, at this point I consider you to be a malicious actor trying to compromise Monero, because only a malicious actor would say something so obviously untrue while simultaneously pushing to significantly degrade Monero's security.~~

~~There is nothing requiring blocks to "immediately propagate over the network" or to ensure "nodes are never offline" in order to enforce a maximum re-org depth.~~

EDIT: OK, I may have misunderstood what you were saying, @tevador gave an explanation below that I think is what you were trying to say here, so my apologies for being trigger-happy with accusations if that is the case.

> Else, net splits would simply be explicitly possible even if the adversary can only cause them intermittently.

Net splits are possible, on every single PoW chain (*EDIT: and PoS chain), with or without a node-enforced finality layer.

You're [asking the community to fund you 200XMR/~$52k](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/604) to write a book describing what is essentially a HOWTO guide on how to degrade Monero's security and maintainability under the guise of improving security. I sincerely hope the community didn't take you up on that offer, but if they did the headlines will write themselves.

## tevador | 2025-08-29T18:04:33+00:00
@taoeffect Max reorg depth is vulnerable to permanent chain splits (e.g. two parts of the network will continue on separate chains and won't ever merge together again). That can be done by an attacker releasing an alt chain that exactly exceeds the max reorg depth just as the finalizing block is being propagated. Network nodes will select the chain they see first. The same applies to new nodes joining the network. They can't know which chain was the first one.

Let me quote Satoshi Nakamoto's e-mail from November 2008 (emphasis mine):

> This touches on a key point.  Even though everyone present may see the shenanigans going on, there's no way to take advantage of that fact. 
>
>**It is strictly necessary that the longest chain is always considered the valid one. Nodes that were present may remember that one branch was there first and got replaced by another, but there would be no way for them to convince those who were not present of this.**  We can't have subfactions of nodes that cling to one branch that they think was first, others that saw another branch first, and others that joined later and never saw what happened.  The CPU power proof-of-work vote must have the final say.  The only way for everyone to stay on the same page is to believe that the longest chain is always the valid one, no matter what.

Source: https://www.metzdowd.com/pipermail/cryptography/2008-November/014832.html

## taoeffect | 2025-08-29T18:10:57+00:00
@tevador Your reply isn't a reply to the debate at hand, although it may seem like one.

The concern and desire for a "finality solution" was triggered by a desire to address deep-reorgs in a way that prevents them from happening.

That desire is in direct conflict with the quote from Satoshi that you shared above.

Look at:

>  The only way for everyone to stay on the same page is to believe that the longest chain is always the valid one, no matter what.

Vs:

> "I want to make sure deep re-orgs never happen"

Satoshi's words are essentially saying, "Learn to live with the deep reorgs you little [expletive removed]".

And the people here are saying they don't want to do that, that they want to prevent them from happening.

Well, in a 200-block deep re-org you're going to have a lot of damage done if you allow it, and you *might* have a lot of damage done if you don't allow it.

## tevador | 2025-08-29T18:17:22+00:00
If you want to "make sure deep re-orgs never happen", you have to use something other than PoW. That was my point. I was responding to your claim that:

> Finality is easily done with PoW alone as a simple constant in full nodes that defines the maximum allowable re-org.

Max reorg depth is a horrible solution I would never recommend, although I'm not a proponent of Proof of Stake either.

## taoeffect | 2025-08-29T18:19:57+00:00
> If you want to "make sure deep re-orgs never happen", you have to use something other than PoW

Not true, you can stick with PoW and have a max re-org depth. That is a solution, perhaps you consider it to be horrible, but it is a solution.

> although I'm not a proponent of Proof of Stake either

Thank goodness!

So if we take a brief break to discuss non-"finality layer"-type solutions, another solution to this class of problem is for the good miners to fight the bad miners by spinning up more machines and clobbering the 51% attacker. I am personally fine with such a suggestion.

## tevador | 2025-08-29T18:49:13+00:00
> That is a solution, perhaps you consider it to be horrible, but it is a solution.

A solution worse than the problem it's trying to solve is not a real solution.

With Satoshi Nakamoto's PoW, you can start your node after a year of being offline, it will sync and you will instantly agree on the state of the chain with every other node that's online.

With your "solution", you'll have to maually input the alt-chain that the shop you are trying to buy coffee from is currently on. Note that Proof of Stake has the same problem. It's called [weak subjectivity](https://ethereum.stackexchange.com/questions/15659/what-is-weak-subjectivity).

For people who fundamentally disagree with a finality-layer based solution, I recommend to give a thumbs down to the OP and refrain from posting in this issue.

My non-finality layer solutions are discussed here: 

- #98 
- #144 

If you have a different solution, please open your own research-lab issue.



## taoeffect | 2025-08-29T22:39:11+00:00
*Edited my reply above to @kayabaNerve to add:

> EDIT: OK, I may have misunderstood what you were saying, @tevador gave an explanation below that I think is what you were trying to say here, so my apologies for being trigger-happy with accusations if that is the case.

Replying to @Deltamax1:

> .6 XMR per block • ~720 blocks per day = 432 XMR daily security budget.

Thanks, I see what you're saying. So the actual cost to attack if you're using this number, assuming you're using other people's hardware, would be this number plus some additional amount for a bribe plus some additional amount to fight off defenders. If you're using your own hardware it would be that previous amount, minus the bribe, plus the cost of owning and operating the hardware.

So let's say it's more like XMR/day * 5 or times 10 (for using other people's hardware), it would still be less than the staking amounts, I'll give you that. Still my arguments are:

- to some attackers both of these numbers (cost to attack PoW, and cost to attack PoS) are small
  - btw, pulling off an attack on PoW makes you more identifiable than attacking PoS where it's easier to be anonymous. The reason being is that if you bribe someone now they know who you are, and if you use your own hardware, that's way more expensive and also kinda hard to hide, so PoW has a real-world-consequences deterrent that PoS doesn't necessarily have
- with the hybrid approach they can still pick PoW to attack and ignore PoS
- buyout attack a new possibility
- you'd be creating a code maintenance nightmare (=> ++bugs, ++vulns)

At the cost of all of these issues (and maybe others), you'd maybe protect from long re-orgs, but you wouldn't protect from 51% PoW attacks, those would still be a thing, so what's the point? Is such a trade-off worth it? IMO, no.

> For example I like a Tevador's Publish or Perish proposal.

On this we both agree. 👍 

## runatyr1 | 2025-08-30T20:05:32+00:00
Hi @taoeffect  and @tevador   I see you are arguing about PoS concerns such as buyout attack and security vulnerabilities.  I wrote a proposal that seems to have been ignored and might solve those issues, could you please consider it? 

It is, assigning validator status from locked mining rewards. So, miners that don't sell (or sell only a small part) gain validator status allowing them to participate to finalize blocks and earn higher rewards than non-validator miners. 

This would require a special public miner address that monerod auto-creates and allows the system to verify the miner has not withdrawn the funds. This should not compromise privacy since if someone withdraws, it will go to a normal private monero wallet. And while the funds are in the public miner wallet the network only knows that an unknown miner has X amount of balance in it and that is has not withdrawn funds after X amount of time allowing it to determine validator status. 

This system would incentivize long term mining to hold rewards and gain validator status and it would prevent rented hash power attacks, or merge mining where mined XMR is sold to buy another token. It also prevents attackers with large amount of funds to stake, as the "stake" can only be derived from existing miner rewards being accumulated. 

The buyout attacks in this case would be someone buying access to long-term miners that have validator status. This could be mitigated requiring that validator status also depends on signing the blocks with the same server private key. If someone buys and changes the keys it would loose validator status. If someone buys and keeps the same keys it creates risk for both parties, it's better than the current way easier hash power rent attack. This could be done by checking: the public key is still in authorized_keys, that ssh is active and that ssh password login is disabled (basic security measure). This ensures a miner doesn't have a different key for signing blocks than the one that is used for access to the server and complicates a buyout attack.



## taoeffect | 2025-08-30T20:34:35+00:00
@runatyr1 Thanks for bringing my attention to your proposal, indeed I skipped over it.

Yes your proposal does sound like a ~~much more secure~~ more secure way of doing PoS on top of PoW *under certain circumstances*. Yes it does help protect against buyout attacks (EDIT: if deployed before a 51% attack, otherwise it offers no protection and actually gives the attacker the potential to buyout the chain) because it requires going through the hardware ownership (whether yours or someone else's).

I'm not sure about the authorized_keys business as I doubt Monero private keys can be tied to SSH like that but that too sounds like a creative idea worth considering (although how would you prove it that SSH keys are being used? And if you could prove that, wouldn't you instantly deanonymize yourself?)

So, I am less hostile to the proposal in that form, but still not terribly thrilled as it might count as unnecessary complexity. I'd also be curious to hear @tevador's thoughts on it.

## taoeffect | 2025-08-30T21:52:38+00:00
@runatyr1 I should also mention that while your proposal makes it harder for an "outside force" with a lot of capital alone to take over the chain, it would not be a solution as a response to a 51% attack that just happened. 

I.e. if there's first a 51% attack, and then this is deployed, it wouldn't solve anything (EDIT: and would give the 51% attacker even more firepower in the form of a free buyout attack opportunity). 

Where it might help is if it's first deployed, and then there's a 51% attack at a later date, it would act as a buffer against the 51% attacker, potentially, and it could lead to a chain stall (depending on what the 51% attacker did). 

Likewise, it could "help" in a net split scenario where miners are split into two spheres by stopping the chain instead of allowing a large re-org to take place when they reconnect. 

## taoeffect | 2025-08-31T16:16:13+00:00
*Made a couple edits to my two comments above and also should add that a buyout attack isn't the end of the world necessarily as the traditional response to it has been that the attacker would have their funds slashed via a followup HF that the community would presumably rally around. Which is I suppose a reasonable deterrent to such attacks, but if the attacker is ideologically motivated and wants to crash the price of XMR along with their holdings then such a deterrent wouldn't apply.

Where PoS could provide a useful feature is in that other scenario I mentioned above of a chain split caused by a network partition. If you wanted Monero to halt block production under such a circumstance, PoS could help with that. EDIT: But alternative approaches to that problem, like creating/using technologies to prevent such network partitions from occurring in the first place (think satellites and anti-censorship), might make more sense to pursue. 

## tevador | 2025-09-11T05:34:01+00:00
To make this proposal less contentious, I would suggest to make it a soft fork. It could then be viewed as a more decentralized alternative to [DNS checkpoints](https://github.com/monero-project/monero/issues/10064). A soft finality layer would be automatically accepted by the whole network (via the longest chain rule) if a mining majority starts enforcing it.

Technical details should be provided how to make it work under the current consensus rules. I'd imagine we could use tx_extra for the required metadata and it would be better to avoid using the legacy time locks, which are scheduled for removal.

## PPPDUD | 2025-09-11T21:09:46+00:00
> To make this proposal less contentious, I would suggest to make it a soft fork. It could then be viewed as a more decentralized alternative to [DNS checkpoints](https://github.com/monero-project/monero/issues/10064). A soft finality layer would be automatically accepted by the whole network (via the longest chain rule) if a mining majority starts enforcing it.
> 
> Technical details should be provided how to make it work under the current consensus rules. I'd imagine we could use tx_extra for the required metadata and it would be better to avoid using the legacy time locks, which are scheduled for removal.

We should not rely on tx_extra, because it has already gotten a bad reputation with many people, and I don't want to see a perfectly-good proposal go to waste over something like that.

## tevador | 2025-09-11T22:36:25+00:00
> We should not rely on tx_extra, because it has already gotten a bad reputation with many people, and I don't want to see a perfectly-good proposal go to waste over something like that.

I don't agree with your argument. The protocol still allows tx_extra for non-consensus data associated with a transaction. It's been limited to 1060 bytes, but that should be enough for the required use case. All alternatives are even more ugly (embedding custom data in output keys etc.).

## PPPDUD | 2025-09-12T15:40:23+00:00
> > We should not rely on tx_extra, because it has already gotten a bad reputation with many people, and I don't want to see a perfectly-good proposal go to waste over something like that.
> 
> I don't agree with your argument. The protocol still allows tx_extra for non-consensus data associated with a transaction. It's been limited to 1060 bytes, but that should be enough for the required use case. All alternatives are even more ugly (embedding custom data in output keys etc.).

I agree that using tx_extra would be a good idea _in theory_, but you might have trouble explaining how it isn't wasting space in the blockchain to people who just started running their own node.

## tevador | 2025-09-12T16:56:13+00:00
> I agree that using tx_extra would be a good idea in theory, but you might have trouble explaining how it isn't wasting space in the blockchain to people who just started running their own node.

You are going off topic. Most likely, the benefits of a well-implemented finality layer would far exceed the cost of a few extra bytes in a handful of staking transactions.

## taoeffect | 2025-09-12T19:43:01+00:00
> Most likely, the benefits of a well-implemented finality layer would far exceed the cost of a few extra bytes in a handful of staking transactions.

Could you please articulate what you see are the benefits of a "well-implemented finality layer"?

Specifically, could you please state:

1. Under what circumstances you see deep-reorgs happening (under the assumption that a finality layer is for preventing them; perhaps you think it's for something else as well, in which case, please state what other problems you see it addressing)
2. What the likelihood of each circumstance is
3. Why a "well-implemented finality layer" is the best solution as opposed to alternatives
4. EDIT: Why the benefits outweigh the above-mentioned risks discussed in the comments in this thread

## tevador | 2025-09-12T21:05:33+00:00
1. The malicious pool currently attacking Monero stated that they will attempt deep reorgs of up to 29 blocks. Source: https://xcancel.com/c___f___b/status/1962083649186062617#m
2. Given their hashrate, the likehood of them causing a 10+ deep reorg is quite high.
3. The alternative, currently being discussed and implemented, are [rolling DNS checkpoints](https://github.com/monero-project/monero/issues/10064), which is a more centralized solution than a finality layer. Another alternative is [Publish or Perish](https://github.com/monero-project/research-lab/issues/144), which works against selfish mining, but can't prevent deep reorgs. Those are the 3 soft-forking solutions on the table.
4. I can't answer that, but if we are going to deploy DNS checkpoints, a PoS checkpointing layer would be an improvement. I think it would be quite safe to deploy it as a soft fork. If the network doesn't accept it, it would simply never activate.

## PPPDUD | 2025-09-12T21:46:59+00:00
> 1. The malicious pool currently attacking Monero stated that they will attempt deep reorgs of up to 29 blocks. Source: https://xcancel.com/c___f___b/status/1962083649186062617#m

And we should trust a crypto bro attempting to cause mass panic why?

## taoeffect | 2025-09-12T21:56:06+00:00
> The malicious pool currently attacking Monero stated that they will attempt deep reorgs of up to 29 blocks. Source: https://xcancel.com/c___f___b/status/1962083649186062617#m

Uh huh. Let's see what this guy is aiming at... Oh, [I see](https://xcancel.com/c___f___b/status/1963871812845973662#m):

> Without #Monero going PoS, nobody will invest significant money into $XMR, so there will be no bullrun for Monero.

So, he's just straight up lying right here in order to manipulate his audience into thinking that PoS will create a bullrun and will address consensus-attacks.

This is obviously a deliberate lie on his part as we know that the #1 cryptocurrency does not use PoS and is not considering switching to it (for very good reason).

So the person you're referencing as attacking Monero clearly has an agenda to get Monero to switch to PoS.

I dunno, should we humor him and do it?

lol.

Once again folks: switching to PoS will not fix consensus problems. It can prevent deep re-orgs from happening at the cost of exposing Monero to:

1. A significantly more complicated codebase filled with more bugs
2. A buyout attack
3. Instead of a deep re-org, a total chain stall, which some could argue is just as bad as a deep-reorg
4. Wasted developer effort and morale

These are new risks Monero would be taking on, for no reason, and as a reminder, the 51% attack would still be there too, completely unmitigated.

I think we shouldn't listen to the guy attacking Monero both via his mining pool and via his words and ideas.

## tevador | 2025-09-12T22:13:50+00:00
> And we should trust a crypto bro attempting to cause mass panic why?

We don't trust him. Monero Research Lab is monitoring their pool and so far they have achieved several reorgs 8-9 blocks deep and they have been more than 10 blocks ahead at times, but chose not to reorg.

> switching to PoS will not fix consensus problems

A PoS checkpointing layer is not "switching to PoS".

> Instead of a deep re-org, a total chain stall

No, that cannot happen with a checkpointing layer. At worst, there won't be any checkpoints produced, but the chain will progress just fine.

## taoeffect | 2025-09-12T22:16:41+00:00
> A PoS checkpointing layer is not "switching to PoS".

Thanks for clarifying that.

> No, that cannot happen with a checkpointing layer. At worst, there won't be any checkpoints produced, but the chain will progress just fine.

I was going off of the proposal in the OP, which says (emphasis mine):

> As service providers should only accept finalized blocks, and ideally we come to consensus less than every 20 minutes and re-define the 10-block lock as the finalized-block lock (where finalizations from the finality layer are then mined into the next block added to the blockchain), **this would be effectively equivalent to a chain stall (even if the chain itself continues to be added to).**

## tevador | 2025-09-12T22:32:26+00:00
> I was going off of the proposal in the OP, which says (emphasis mine):

OP proposed a hard forking solution. The soft forking solution would keep the 10-block lock and it would be up to service providers if they demanded a checkpointed block or just a certain number of confirmations.

A stalled soft finality layer would not prevent transactions outputs from being spent etc. In fact, it would work completely fine even for someone running an old node version without any support for the finality layer. They would just follow the longest chain as before, which would just happen to be checkpointed.

I suggest readers to look up the difference between a hard fork and a soft fork.

## taoeffect | 2025-09-12T22:37:26+00:00
How about service providers just monitor the the weather on Monero and increase the amount of time they wait before considering transactions finalized during stormy conditions?

## PPPDUD | 2025-09-12T23:21:26+00:00
> This is obviously a deliberate lie on his part as we know that the [#1](https://github.com/monero-project/research-lab/pull/1) cryptocurrency does not use PoS and is not considering switching to it (for very good reason).
> 

Monero is great, but I don't think that there is any such thing as a superior cryptocurrency. We should avoid such bragging, for pride quickly devolves into tribalism (and has done so many times in the past).

## taoeffect | 2025-09-12T23:24:37+00:00
> Monero is great, but I don't think that there is any such thing as a superior cryptocurrency. We should avoid such bragging, for pride quickly devolves into tribalism (and has done so many times in the past).

If that's a joke it's a good one. 😆

(If not, I was referring to Bitcoin's market cap.)

## PPPDUD | 2025-09-12T23:24:58+00:00
Before anybody else panics, please read these ancient World War II posters from the UK:
<a title="UK Government, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Keep-calm-and-carry-on-scan.jpg"><img width="256" alt="Keep-calm-and-carry-on-scan" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Keep-calm-and-carry-on-scan.jpg/256px-Keep-calm-and-carry-on-scan.jpg?20181007092500"></a>

<a title="UK Ministry of Information, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Freedomisinperilposter.jpg"><img width="256" alt="Freedomisinperilposter" src="https://upload.wikimedia.org/wikipedia/commons/8/88/Freedomisinperilposter.jpg?20150708002612"></a>

## PPPDUD | 2025-09-12T23:27:24+00:00
> > Monero is great, but I don't think that there is any such thing as a superior cryptocurrency. We should avoid such bragging, for pride quickly devolves into tribalism (and has done so many times in the past).
> 
> If that's a joke it's a good one. 😆
> 
> (If not, I was referring to Bitcoin's market cap.)

I am not joking. I don't usually make jokes that are hard to figure out. This post is not sarcastic.

## tevador | 2025-09-13T09:07:35+00:00
Please avoid off topic discussion. This is not a place for chatting.

Especially, @PPPDUD - there is not a single comment from you here actually related to a finality layer.

@Rucknium Can you please moderate the discussion?

## PPPDUD | 2025-09-13T13:31:43+00:00
> Please avoid off topic discussion. This is not a place for chatting.
> 
> Especially, [@PPPDUD](https://github.com/PPPDUD) - there is not a single comment from you here actually related to a finality layer.
> 
> [@Rucknium](https://github.com/Rucknium) Can you please moderate the discussion?

I will leave now.

## tevador | 2025-09-14T10:29:45+00:00
> Specifically, could you please state:
> 
>  1. Under what circumstances you see deep-reorgs happening (under the assumption that a finality layer is for preventing them; perhaps you think it's for something else as well, in which case, please state what other problems you see it addressing)
>
>  2. What the likelihood of each circumstance is
> 

I can give a more definitive answer now. Today at around 6:00 UTC, there was an 18 blocks deep reorg, permanently breaking more than 100 transactions. So deep reorgs are a reality, not a likelihood.


<img width="500" height="1194" alt="Image" src="https://github.com/user-attachments/assets/a195c5eb-093a-41a7-960a-c0fb76bd919d" />




## tevador | 2025-09-14T10:38:23+00:00
> No, that cannot happen with a checkpointing layer. At worst, there won't be any checkpoints produced, but the chain will progress just fine.

Correcting myself here: the soft checkpointing layer can also stall the chain if 2/3 of the stake is malicious and an invalid checkpoint is created.

## kayabaNerve | 2025-09-14T11:34:41+00:00
Any finality layer can be done as a soft fork if it doesn't require slashing, though the lack of timelocks would make the project potentially infeasible _if_ there's a requirement for coins to be locked. I believe it'd incur some trust assumption regarding locked stake (usage of a TEE to assert a key will only be made available after some point in time).

1/3rd of the stake being malicious is sufficient to produce two distinct checkpoints, by splitting the honest 2/3rds into two honest halves misled by the double-signing malicious 1/3rd.

## taoeffect | 2025-09-14T15:05:47+00:00
> Today at around 6:00 UTC, there was an 18 blocks deep reorg, permanently breaking more than 100 transactions. 

I recommend:

1. The community give official guidance to providers and users to increase the wait time before considering blocks finalized (18 * 2 = approximately 1 hour wait) 
2. Creating a blog post on how to run a fast monero miner, and maybe (if it makes sense) point it to some good pool
3. Put out a call that monero needs good miners to fight this troublemaker 

## runatyr1 | 2025-09-15T01:02:00+00:00
Hi @taoeffect I talked with you previously about locked miner rewards validation layer, but after further analysis I understood the PoS finality layer originally proposed in this issue is actually more conservative and feasible. It doesn't affect the current PoW consensus mechanism (as long as the finality check is optional for vendors).

I'm not an expert dev, just a concerned average tech person and I understand now why the community fears and backlashes on this proposal: because they don't understand it, they think bad actors could buy a lot of XMR and "take control of the chain".

I think I understand clearly now how this proposal affects the protocol: 
- PoW miners keep finding blocks (unchanged by finality layer)
- Block data validation keeps happening cryptographically, you can't add fake transactions (unchanged by finality layer)
- Validators/stakers simply agree on blocks to mark them as final to prevent deep reorgs. 
- If a bad actor had a huge stake (67%+)  and continued facilitating a 51% attack by certain miner finalizing their blocks the community could slash their stake so it is an unlikely situation. 
- If the validation layer fails, the chain doesn't stall (as long as it's an optional finality) - it continues exactly as Monero works today, just without the finality check. 
- So the impact is: vendors that implemented this check would stall unless they decide to fallback and continue confirming after their chosen amount of blocks like they currently do.
- Attacking would require both majority mining power AND majority stake, making attacks significantly more expensive than current 51% attacks

Is my understanding correct? 

Could you clarify if this proposal intends finality to be a consensus rule (hard fork) or optional security feature (soft fork)?

I do think optional finality is the way to go:
-  It's an additional security guarantee
- doesn't give excessive power to the finality layer 
- allows users to make the final choice of how to confirm their transactions, eg fallback on confirmation after X blocks like they currently do if the finality layer fails/stalls
- the chain doesn't stall if the finality layer fails

## taoeffect | 2025-09-17T16:56:12+00:00
> If a bad actor had a huge stake (67%+) and continued facilitating a 51% attack by certain miner finalizing their blocks the community could slash their stake so it is an unlikely situation.

No. Slashing doesn't work in that scenario.

EDIT: oh, sorry, I misread. You're saying HF to slash. Yeah this was discussed earlier IIRC.

> If the validation layer fails, the chain doesn't stall (as long as it's an optional finality) - it continues exactly as Monero works today, just without the finality check.

If that were true, then I see no point to the finality layer. What purpose is it serving if it's not working and everyone continues to rely on PoW?

No, the point of a PoS checkpointing layer, however it's done, would be to stall the chain in event of disagreement. If the chain doesn't stall, there is no point to it afaict.

> Attacking would require both majority mining power AND majority stake, making attacks significantly more expensive than current 51% attacks

Attacking what? What attack?

Again, there is nothing that I've seen in any of these proposals that creates an improvement in security, but rather the opposite, now there are two things to attack and either one could be used to cause problems.

> Could you clarify if this proposal intends finality to be a consensus rule (hard fork) or optional security feature (soft fork)?

No, because multiple proposals have been made at this point, and I don't have a full understanding of them all because none of them is fully specified. But they all seem like a bad idea to me.

> It's an additional security guarantee

You've yet to show this. And I don't think you can until the "it" of that sentence is fully and clearly specified anyway. That's step #1, and then if it's fully specified, it's most likely not an "additional security guarantee" anyway, but a tradeoff with potential new security pitfalls.

From what I can tell, the Monero community does not appear to care about this attack at all.

Instead of [putting out a call for help or warning anyone about the attack and to raise the wait time](https://github.com/monero-project/research-lab/issues/135#issuecomment-3289616643), they haven't said a thing:

- https://x.com/monero
- https://www.getmonero.org/blog/

So, if the Monero community isn't taking this attack seriously and taking the most simple and basic of steps to warn users to wait longer, I certainly won't be taking this risky PoS proposal seriously either.

## taoeffect | 2025-09-17T18:36:59+00:00
> No. Slashing doesn't work in that scenario.

Sorry, I missed the word "community" there. Edited my comment to add:

> EDIT: oh, sorry, I misread. You're saying HF to slash. Yeah this was discussed earlier IIRC.

## runatyr1 | 2025-09-17T20:33:33+00:00
@taoeffect thanks for the reply, here is some feedback.

> >If the validation layer fails, the chain doesn't stall (as long as it's an optional finality) - it continues exactly as Monero works today, just without the finality check.
> 
> If that were true, then I see no point to the finality layer. What purpose is it serving if it's not working and everyone continues to rely on PoW?

The purpose is, if the optional finality layer marks blocks 1, 2 and 3 as final, there cannot be reorgs passed that point. So it can be the main checkpoint for vendors to consider a transaction confirmed.  Like Kayaba mentioned initially, if the optional finality layer is fast enough, even the standard 10 block wallet wait time could be reduced.

But, if the finality layer were to stall, vendors could fallback to waiting X amount of blocks like they currently do. 

In my opinion being optional is better because you can guarantee no reorgs while the finality layer works correctly, but if an issue where to happen, you won't be stalling the chain which is way worse than fallback to pure PoW.


> Attacking what? What attack?

Selfish mining / long reorgs. Basically what is happening now. If you had an optional finality layer you would need both a large percent of PoW miner hashpower + finality layer majority.

> You've yet to show this

Yes of course, the only way to show/deminstrate this idea, is to implement the code and let it be independently tested. But, I'm not a Monero protocol dev. I would like for example Kayaba (the OP) taking a look at this "optional finality" scenario. But I know he has a lot of work and also too many people writing in this github issue.

> Monero community does not appear to care about this attack at all.
> taking the most simple and basic of steps to warn users to wait longer

I think your concern is valid. The X account and blog should warn users to increase confirmations, but, this is a decentralized protocol, the X account and blog doesn't represent the whole of Monero protocol. For example this github issue and the parent one show Monero devs are working on solutions. Once someone is able to demonstrate a solution works fine in all required scenarios it will gain more momentum.

> I certainly won't be taking this risky PoS proposal seriously either.

I think it's only risky if it's mandatory PoS, but if it is optional then in the worst case scenario, it simply reverts to the current behavior of pure PoW, as described above. 


I hope some Monero dev could share an opinion on doing this as an optional finality layer.. maybe it is a good solution..

## taoeffect | 2025-09-17T22:27:54+00:00
> I think your concern is valid. The X account and blog should warn users to increase confirmations, but, this is a decentralized protocol, the X account and blog doesn't represent the whole of Monero protocol

.... .... I'm not claiming that they represent the whole of Monero, and I think that's irrelevant. They should be warning users.

@tevador said more than 100 transactions were broken. Seems like whoever is running the blog and the twitter should let people know that they should wait longer.

I think all that's really needed to address this issue is a "Monero Weather Report" status page with a big dial that goes from red to green and says how long people should wait before considering transactions confirmed.

![Image](https://github.com/user-attachments/assets/8d0658fb-e561-4ad9-874c-1a0f7af2d6a8)

Once people get used to this idea, the problem will solve itself IMO.

## yonder83 | 2025-09-18T08:37:10+00:00
> Your suggestion is, we just accept longer finality times? I get it that works, but for me that runs completely counter to Monero fulfilling Bitcoin's original promise
> 
> Monero: A Peer-to-Peer Electronic Cash System
> 
> There is no way Monero could ever be used in the physical world in that case, nobody can wait around that long, that's one of the benefits of a finality layer is it greatly reduces the wait time, increasing IRL UX

Perhaps the original idea behind Monero (and Bitcoin) was to be a peer-to-peer electronic cash system, but real-world use has shown that this isn’t really possible. In my view Monero is more like a secure Layer 1 solution.

The 10-block waiting period is actually a positive feature, and it could even be longer — 20 or more. Locking mined coins also helps to reduce immediate selling pressure.



## taoeffect | 2025-09-18T15:37:22+00:00
> Your suggestion is, we just accept longer finality times?
I get it that works, but for me that runs completely counter to Monero fulfilling Bitcoin's original promise
> 
> Monero: A Peer-to-Peer Electronic Cash System
> 
> There is no way Monero could ever be used in the physical world in that case,

Even if there were no ongoing attack, no malicious miners, as a Layer 1 Monero would still not be suitable for a "p2p electronic cash system in the real world".

For this [you need L2s like Lightning in order to keep the network decentralized as it scales](https://arxiv.org/abs/1801.04335).

## tevador | 2025-09-18T16:18:42+00:00
@taoeffect There are several alternatives to a finality layer, but this is not the place to propose or discuss them.

## hamidrezaa693-afk | 2025-11-11T00:56:03+00:00
Melon and additional information on 

## hamidrezaa693-afk | 2025-11-11T00:56:38+00:00
Bolder **telencephalon**

## hamidrezaa693-afk | 2025-11-11T00:56:52+00:00
Made a mony shslana

## hamidrezaa693-afk | 2025-11-11T01:03:44+00:00
> [@FocuzJS](https://github.com/FocuzJS) You can't use PoW descending from the block you want to finalize to finalize it. That would trivially allow multiple equivocations.

Selopoe in my house in my life is good to birjandi a eeeeee a copy tryino in the e and j in the e a copy tryino a long day today so we will be getting

# Action History
- Created by: kayabaNerve | 2025-08-08T18:34:56+00:00
