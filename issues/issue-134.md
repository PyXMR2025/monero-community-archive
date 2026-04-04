---
title: TEE-assisted Censorship-Resistant Block Template Production
source_url: https://github.com/monero-project/research-lab/issues/134
author: kayabaNerve
assignees: []
labels: []
created_at: '2025-07-27T01:51:58+00:00'
updated_at: '2025-08-09T00:18:53+00:00'
type: issue
status: closed
closed_at: '2025-08-09T00:18:53+00:00'
---

# Original Description
Currently, any actor on the Monero network can censor blocks/transactions from their node and produced block templates. The following posits a design which would limit the ability to censor blocks/transactions to those who are able to break a TEE, while simultaneously introducing a bound that block producers have a qualified TEE available.

We require the TEE serve as a black box capable of running the necessary programs. We require the TEE be able to maintain confidential state (without a break) and maintain a 32-byte state *without an adversary being able to trigger a roll back*.

We first describe the representation of non-confidential data. A Merkle tree is used, such that all values are committed to within the tree root. With every read and write, the Merkle path is checked for integrity to prevent the database from being unexpectedly altered. While authenticated encryption would be eligible here to prevent substituting non-TEE values, it'd be insufficient to prevent rolling the state back.

The TEE is required to be able to validate Monero blocks and decide on a best chain.

The TEE is also required to be able to handle a 'message'. We do not assume the IO is secure, but we do assume we can spawn the TEE with a message as input and obtain a response.

The messages are three-fold:
- Censored Block
- Connect
- Opaque

The CB message introduces a block to the graph, with the TEE validating it. The Connect message initiates a key exchange, with the TEE attesting to its state and forming a secure tunnel. An opaque message is any message within an instantiated tunnel, albeit completely indistinguishable to any other opaque message.

Once decrypted, the opaque message would have one of the following subtypes:
- Ping
- Transaction
- Block Announcement

A tunnel must exchange messages with a consistent bandwidth pattern, using pings to fill the gaps. If a ping isn't responded to within an acceptable latency, the tunnel collapses and must be re-instantiated.

A transaction message is used to publish a transaction into an encrypted mempool within the TEE. The TEE attests fair handling of the transaction (lack of censorship expect for configurable parameters applied to agreed upon relay rules, fair prioritization within the block body, etc.) by attesting their program executed when announcing blocks they produce.

A block announcement is sent over any tunnel *of sufficient age*. TEE-following nodes (nodes within a TEE or who follow the ones within a TEE) determine the best chain as the chain with most work *whose tip was received over a well-maintained channel*. This ensures blocks are only added if the adder had time to broadcast their own transactions for a chance at inclusion.

If a majority of service providers follow this chain, the non-TEE Monero will have little value. If a majority of hash power adopts such a solution, nodes with no preference for TEEs will follow regardless.

The issues are three-fold:
1) Throughput. The Monero blockchain is now limited to the processing power of the TEE. Additionally, opaque messages would require a constant storage access pattern (as to not reveal what data they're operating over), requiring non-trivial disk throughput.
2) Network topology. All TEE-following nodes on the network must have a tunnel to the block producer to accept their blocks. This is unless a majority of hash power network amongst each other, causing the chain naturally with the most work to be propagated to all other nodes using existing Proof of Work rules.
3) Centralization regarding who can produce a block template. An approved TEE is now a requirement. Publishing censorship-resistant TXs, and receiving censorship-resistant blocks, do not require a TEE however. Only a client library capable of verifying TEE attestations (possible without proprietary code) would be required.

There's also further commentary on how changes to the code creating block templates would now effectively be a hard fork, but that's less important IMO.

If successfully adopted, selfish mining/censorship attacks would require a TEE compromise however. While these happen frequently, their ability to exploited is much less frequent than every second of the day, which is less than when a malicious miner can currently act on Monero.

I personally hate TEEs and believe this to be centralizing. I also believe PoW has its risks, and the Monero community will not agree on a PoS solution. If this technology had sufficient performance, and the TEE-kneejerk reaction was avoided, I believe this could contribute to Monero overall. I'll also note the Ethereum ecosystem (Flashbots possibly most notably?) Has done extensive work on block builders and fairness, and they do have designs incorporating the Intel SGX, which may be worth referring to. The above is solely an initial sketch, without prior experience with the subject, on how the design *could* look.


# Discussion History
## kayabaNerve | 2025-07-27T02:08:23+00:00
Relevant: https://writings.flashbots.net/block-building-inside-sgx

## SyntheticBird45 | 2025-07-28T17:07:01+00:00
> 134 shrinks the set of potential block builders from block builders with a CPU we compile to to block builders with a CPU we compile to
> But now the CPU is a TEE
> Sorry, I don't make the rules :C
> It also redefines the best chain rule premised on local view of lack of censorship
> It also doesn't cause the system to fail if a TEE is compromised, and doesn't have any vendor lock-in.
> We just gain resistance against censorship, including selfish mining.
> Which of Monero's premises is this fighting?
> It's a trade-off on decentralization of hardware vs security of consensus
> It's also likely a bad idea due to the topology issues
> Go discuss it on the issue instead of having your own knee-jerk reaction that no one is discussing it because they'd only have knee-jerk reactions :C
> :p

I'm not attempting to undermine the advantages that you explained already. Just two points.

> doesn't have any vendor lock-in.

There are no RISC-V cpu out there with a TEE. and ARM in its great far-west tradition do not make TrustZone support mandatory. 
Beside hardware not all operating systems have support for it, see FreeBSD. And Android only expose a very small set of API for interacting with it. Mainly for key storage purposes. I'm not sure Apple exposes its secure enclave, i think its mainly used by OS and Firmware.

In practice this effectively locks block producer behind Intel, AMD and Altra CPUs. 

> Which of Monero's premises is this fighting?

As you already deduced: 

> Decentralization: The utility of Monero depends on its decentralised peer-to-peer consensus network - **anyone should be able to run the monero software, validate the integrity of the blockchain, and participate in all aspects of the monero network using consumer-grade commodity hardware.**

May this appear as a knee-jerk reaction one is obligated to at least quote once: 
- https://sgx.fail/
- https://github.com/google/security-research/security/advisories/GHSA-4xq7-4mgh-gp6w
- https://googleprojectzero.blogspot.com/2022/05/release-of-technical-report-into-amd.html

This isn't the first time TEE has been broken and it won't be the last. Securing consensus based on an impossible to review, prove or simulate process might not be in the project advantage imo. That is acknowledging the unlikely and short-lived scenario of seeing the TEE being breached and taken advantage of.


## jeffro256 | 2025-07-28T17:22:40+00:00
How does this setup prevent censorship? How can one tell the difference between a transaction ping / connection being blocked and an honest liveness failure? We can assume the TEE is secure, but some hardware has to feed the TEE the notification of a transaction and that ostensibly can be compromised.

## kayabaNerve | 2025-07-28T18:07:52+00:00
https://riscv.org/blog/2024/10/towards-generic-risc-v-tee-ecosystem-with-penglai-and-op-tee/

https://docs.keystone-enclave.org/

re: RISC-V ^

re: ARM: The lack of required support for TrustZone does not equate to a lack of CPUs with TrustZone. Modern Google Pixels appear to expose TrustZone via https://source.android.com/docs/security/features/trusty ?

I'll also quote https://googleprojectzero.blogspot.com/2017/07/trust-issues-exploiting-trustzone-tees.html?m=1 for the following,

> Within the Android ecosystem, two major TEE implementations exist; Qualcomm’s “QSEE” and Trustonic’s “Kinibi”.

> The collection contains more than 45 different firmware images from many different vendors, including Google, Samsung, LG and Motorola

While an article on the failures of TEEs as seen within Android phones, it covers roughly a decade of support for TEEs within Android devices (though their eligibility here is a separate discussion).

The question is if we could accept a TEE as sufficiently consumer-grade re: miners (who already are likely to have more notable hardware) to justify censorship possibilities being reduced to the duration for which a TEE exploit is actively viable (a distinct metric than the frequency of attacks being possible).

## kayabaNerve | 2025-07-28T18:54:26+00:00
Also, due to the reduced risk of template delegation, it would be possible to run P2Pool such that anyone can volunteer a template producer and the system only requires one satisfy a liveness requirement?

That's if they all share a template, so any TEE can reveal the template once mined (as premature reveal allows preventing fair ordering). That's the trickier comment... Presumably, that'd be:
1) A way to export encrypted templates among TEEs.
2) We don't consider blocks received over a well-maintained connection for the best chain. We consider blocks for which we received a commitment that such a block would be fair ordered for the best chain. Such commitments aren't immediately trivial but are possible. This allows separating the TEE which performed fair ordering from the entity which publishes the block.

## spirobel | 2025-07-29T03:49:02+00:00
from a conceptual standpoint TEE is worse than a trusted setup. way worse. 

## kayabaNerve | 2025-08-08T17:09:12+00:00
If we moved all gossip into TEEs, requiring every node in gossip have a TEE, that likely solves the topology issues even though it makes the requirement on a TEE much more widespread.

There is one concern where a malicious miner can:
- Spawn a TEE node
- Feed it selfishly-mined blocks
- Get a valid template off the selfishly mined blocks
- Use that TEE-certified template to retroactively certify the selfishly-mined blocks as the best chain

Instead of requiring the TEE sign block templates, I believe it'd have to distribute block templates, but then sign the finally produced block. That way, if an honest block is received and the best chain moves from the selfishly-mined blocks to the honest chain, the formally issued template for the selfishly-mined blocks won't be accepted even if a valid PoW is found for it.

Then, we just require that no TEE start signing any blocks until enough time has passed the network SHOULD have issued a valid block, allowing it to update its view of the block which should be built on if necessary.

## kayabaNerve | 2025-08-08T17:16:35+00:00
Clarifying: Non-TEE nodes could still follow the chain. They just couldn't relay blocks.

## kayabaNerve | 2025-08-08T20:18:07+00:00
I believe we can achieve a design solely requiring integrity, not confidentiality. Most TEE breaks break their confidentiality, not their integrity, AFAIK, so this would be much preferred. The original design's focus on confidentiality to prevent censoring likely is unnecessary for the desired 'best-case' implementation of this proposal.

## kayabaNerve | 2025-08-09T00:18:53+00:00
When a connection is open, it must be reconciled (the existence of their blockchains agreed on and the mempools mutually acknowledged) before being considered healthy and eligible for use. I don't believe I prior acknowledged that bound.

---

@j-berman noted an attack where the honest network `A` is connected to a malicious node `E`, with the malicious node having controllable inbound/outbound latency. While we can require latency between nodes not exceed a specific time bound, a malicious adversary can put an infinite amount of nodes between `A` and `E` (each satisfying the individual-connection latency limit) to achieve infinite inbound/outbound latency.

The solution would appear to a per-connection latency limit _and_ a limit on how many nodes may sit between the block producer and the node which accepts the block. This would a limit on the _diameter_ of the P2P network graph.

If we have each node service 12 connections, a maximum diameter of 16, and a maximum latency of 5 seconds, then:
- We could support 12**16 nodes
- Transactions would be gossiped within 90 seconds (assuming we gossip via flooding all connections with all messages)

The issue would be a malicious attacker can now on-purposely create P2P network connections such that:
- They are 15 blocks nested
- They connect to nodes they chose as the 16th node
- Nodes they choose will accept their blocks, no one else will

This allows an adversary with a majority of hash power to split the network, though nodes will still only follow a blockchain that didn't censor their transactions.

Presumably, a node would need to accept blocks from nodes it has a tunnel to with sufficiently low latency. This re-introduces the original topology problem noted, where all nodes must have a tunnel to all miners. Alternatively, if the attacker is of minority hash power, they will eventually have to sync someone else's blocks, and will eventually sync other peoples' transactions.

---

Further discussing with @j-berman, it was noted how an adversary with majority hash power can also mine their own longest chain on their own network, connect to the actual Monero network (where both the malicious network and the Monero network sync each other's blockchains, yet maintain their view of the best block), before one more block is mined on the longest chain to force a deep re-org _and_ a censoring of all transactions except the highest-paying transactions mutually-valid across both blockchains within the next block.

For a re-org of size `n`, we could require it only be accepted if we have a health connection where we don't just observe one block mined on top (without censoring), yet `n` blocks mined, meaning an adversary can at most halve the network's throughput? That doesn't change an adversary with 51% can effect an arbitrarily deep reorganization however.

---

I believe the unfortunate TL;DR is that local observations are insufficient to achieve global consistency across the network. While this is a somewhat-obvious statement, the existence of the TEE black boxes appear insufficient to circumvent it as posited here. This proposal, by not modifying Nakamoto consensus, fails to overcome the failings of Nakamoto consensus even if it may limit the impact some attacks when the adversary doesn't have a majority of hash power. Accordingly, I'll withdraw this proposal.

# Action History
- Created by: kayabaNerve | 2025-07-27T01:51:58+00:00
- Closed at: 2025-08-09T00:18:53+00:00
