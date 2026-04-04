---
title: Wallet User Repeater to Dissociate User IP (WURDUIP)
source_url: https://github.com/monero-project/research-lab/issues/82
author: Gingeropolous
assignees: []
labels: []
created_at: '2021-02-17T04:29:09+00:00'
updated_at: '2021-05-31T20:37:33+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Work in progress. Hope to get out of my head and maybe ignite some fires in other heads or find a way to kill the idea. 

# Problem.

Wallet users using remote nodes can have their IP address associated with a transaction. When a wallet user [W] connects to a remote node [RPC], the [W] downloads blockchain data. The only information leaked here is that the IP address of [W] is a monero wallet user. When the [W] forms a transaction, the [W] requests output data from the [RPC] node. This is the first breach of information, and is the breach that WURDUIP mitigates. Finally, when the [W] crafts a transaction (Tx) and pushes the Tx to the network, the [RPC] node can associated the Tx with the IP of [W]. This is a second breach of information, but is already mitigated using dandelion (where [W] can push a TX over the standard p2p protocol). 

Existing infrastructure steps

1. [W] connects to [RPC], downloads data. - info leak of a monero user at a given IP (relatively low, no different than existing p2p)
2. [W] forms a transaction, requests outputs O[1-11] from [RPC] - info leak high
3a. [W] pushes transaction. In old setups, this occurs with the same RPC node that the data was downloaded from in 1. - info leak high
3b.  In newer setups (like the GUI, and I think the CLI), [W] pushes the tx over the p2p network, where dandelion is used. 

WURDUIP addresses #2. The first thought was for [W] to simply connect to RPC-1 node for wallet refresh, and then connect to a different RPC-2 node for Tx data requests, and then connect to a different RPC-3 node to push the tx. However, here RPC-2 can clearly link the IP of [W] with the tx. Even if you distributed the data request from [W] to multiple RPC nodes, they could still track the output when it enters the blockchain. 

# Solution 1

Use tor or some other such thing. However, if this is the solution for IP protection, why implement dandelion? Potential discussion regarding utility / appropriateness of public remote node infrastructure. 

# Solution 2 - WURDUIP

Pronounced "word up", obviously. 

Detailed in steps

1. [W]allet connects to [RPC] node for refresh. Upon final sucking of all the bandwidth, [W] disconnects from [RPC] 
2. [W] then begins to craft a transaction (Tx), requires data for outputs  O[1-11]. Requests O[1-11] from node [A]. 
3. [A] sends data to [W]. [A] also sends request to node [B] for same O[1-11]. 
4. Node [B] sends data to [A] and requests same data from [C]. 
5. Node [C] sends data to [B] and requests same data from [D].
6. goto 4 (replacing nodes obviously) until some random n 

Observe that no node in the chain of repeaters can tell if IP that requested the information is the original [W]. This is similar to the dandelion stem phase. 

[W] <-> [A] <-> [B] <-> [C] <-> [D] <-> [E]

# The general protection afforded

### Suppose there is an attacker [X] that wants to spy on remote node users and associated IP addresses with transactions. 

[W] <-> [A] <-> [X] <-> [C] <-> [D] <-> [E]

[W] <-> [X] <-> [B] <-> [C] <-> [D] <-> [E]

[W] <-> [A] <-> [B] <-> [C] <-> [X] <-> [E]

X is not able to determine where they are in the chain. 

# Potential attacks

### Suppose the attacker launches many nodes. 

[W] <-> [A] <-> [X] <-> [C] <-> [X] <-> [E]

[W] <-> [X] <-> [X] <-> [X] <-> [X] <-> [X]

At some saturation of node space, the attacker is able to identify the TX creators IP address. 
Statistics / math needed here to determine stem length that can accommodate serious Sybil attack
Note that cheap node mimicry is possible, as these repeaters don't verify. Can be mitigated with strong peer list protections. 

### Suppose the attacker decides to not repeat

[W] <-> [A] <-> [X] 

[W] <-> [A] <-> [B] <-> [C] <-> [X]

Attack is ineffective, because [W] still obtained information and [X] still does not know where they are in the chain.

### Suppose the attacker floods the repeat

[W] <-> [A] <-> [B] <-> [C] <-> [X] <==> [D-V]

This would cause a repeat chain cascade in all [D-V] nodes. Some nodes would overlap. This attempted ddos would fizzle out as nodes would not repeat a TX that they've already repeated. 

Note potential ddos exists in the buffer for storing history of repeats. 

### Timing attacks

Presumably they exist. At this point presume that using a similar random timer thing as in dandelion can mitigate. Needs more thought.

# General concerns

Originally pitched to various monero IRC channels. Only feedback was a general concern with introducing new stuff to the p2p layer that could increase potential attack vector. 




# Discussion History
## UkoeHB | 2021-02-17T12:24:44+00:00
> Wallet users using remote nodes can have their IP address associated with a transaction.

Can you go into more detail on this?

## UkoeHB | 2021-02-17T18:34:47+00:00
> When the [W] forms a transaction, the [W] requests output data from the [RPC] node. This is the first breach of information, and is the breach that WURDUIP mitigates.

During the remote node sync process could you record some outputs in anticipation of making transactions? Then each time you sync, add new outputs while thinning out the old ones (decoy selection has higher density of recent outputs, so the db of prepped decoys only need a high density of recent outputs). Not sure how much storage is 'enough' (maybe have a setting like 'enough to make 100 tx', then query remote nodes like normal if you run out of decoys).

## Gingeropolous | 2021-02-17T21:19:32+00:00
> During the remote node sync process could you record some outputs in anticipation of making transactions? 

Maybe? But this could conflict with potential wallet - server behavior (namely, fast-forward or downloading and scanning of specific blocks instead of entire history)

## Gingeropolous | 2021-02-18T01:31:30+00:00
@UkoeHB , I rather like the idea. So it's sorta like a pre-fetch. 

OK, so it achieves the same goals as WURDUIP. At the gut level it feels like it'd be simpler.

Primary downside of WURDUIP is additional bloat to p2p layer.

Primary downside of tx pre-fetch would be wallet side storage of unverified chain data. Hrm, that could be it. [X] could feed you bad chain data, and when you go to create a transaction with those bad outputs, the tx would be rejected by the first node that is meant to relay - unless, I think dandelion doesn't even check the integrity of the tx. So the tx would make it all the way to a fluff before verification? So the wallet user would have failed txs, but the TX wouldn't be linked to an IP. 

Immediate thought for mediation would be to implement headers-first sync in the wallet / daemon, but then you may lose any instant-on stuff. Also could connect to multiple remote nodes and compare data. 

Beyond that this idea just needs some details / figuring out regarding how much of the chain to pre-fetch and how often the cache would be updated. I mean, the wallet is already downloading all of this data (I think?), I guess it just needs to store some of it for future use. 

## Gingeropolous | 2021-02-18T18:59:48+00:00
Well, say your wallet is offline for a week. When you connect to refresh, your going to download chain data to refresh. Or, if fast-forward gets implemented, you won't. So then, say you don't download new information. So now you have to request random outputs O[1-2000] from a remote RPC node to freshen up your prefetched cache. If you go and then make a transaction with O[1-11], that RPC node knows that it was your IP if it sees a union between O[1-2000] and O[1-11].

Unless all node request the same random outputs to fill the prefetch cache? 

## UkoeHB | 2021-05-31T20:37:33+00:00
Not sure... I think it only works if you download all on-chain outputs, then just discard most of them.

# Action History
- Created by: Gingeropolous | 2021-02-17T04:29:09+00:00
