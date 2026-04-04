---
title: newbie brainstorm question?
source_url: https://github.com/monero-project/monero/issues/9780
author: dbee01
assignees: []
labels:
- question
created_at: '2025-02-07T16:55:23+00:00'
updated_at: '2025-02-09T10:26:09+00:00'
type: issue
status: closed
closed_at: '2025-02-09T10:26:08+00:00'
---

# Original Description
Hi everyone,

I’m a blockchain noob but i’m picking it up as i go along. To help me learn i’m playing devil’s advocate and trying to picture attack vectors to the Monero network.

I’m especially interested, given the current political climate, as to how an operational agency might attack the Monero network and how it could be hardened against such an attack…

The most likely attack from the 3 letter army would surely be the addition of Sybil nodes to the network i think followed by a possible Eclipse attack. Given that an army of Monero nodes could be created in VM’s behind a single (or multiple)  ip's and unleashed on the network if i understand correctly? 

I’m positing a possible network defence for this attack. I’m calling it the Phalanx Defence. Really,  i'm just learning though,  so feel free to pick holes. Here goes:

At the moment the block template consists of the block header (the proof-of-work, timestamp and hash of previous node) along with the Transaction Layer (ring signatures, ring confidential transaction and stealth address).

What if the verified nodes were able to form a phalanx to protect themselves against Sybil nodes? Every time the Concensus Protocol rejected a transaction from a node, that node loses a small degree of credibility in the blockchain network.

We could call this the Node Trust score and it could be stored and relayed from one node to another by adding the node trust score to the blockchain transaction layer ie. Ring signature, ring confidential transaction, stealth address AND the node trust score.

The idea would be, existing verified nodes would have a very high node trust score but newer Sybil nodes would be outcast quickly since they don’t have node trust. This node trust algorithm would be weighted to reflect the most recent transactions first. Kinda like a decentralised Page Rank system Google used for SEO. An Amazon Product Review comparison may be more apt.

Where can i go to learn more about Monero? Where does my idea go wrong?

# Discussion History
## selsta | 2025-02-07T18:26:43+00:00
This would not work for multiple reasons. One issue is that a sybil attack is often purely passive, so there is no "rejected transaction" happening in the first place from these nodes so you don't know which node is bad and which is not.

Also what does it mean if a node is less credible? What consequences does that have?

The miner would be able to increase or decrease the "trust score" of any IP, and other nodes would have to accept it since they don't know what happened to other nodes or what was submitted to them.

## dbee01 | 2025-02-08T00:19:14+00:00
Hi selsta, 

Thanks. I didn't relise Sybil nodes were passive. Can you elaborate please? 

So,  as nodes become less credible they get cast out of the Phalanx ie.  The Monero network gradually becomes a superhighway of credible nodes communicating with themselves on the network only. Eg.  It'd take time for node z to build trust but very little time for node z to lose trust.

Does the miner have access to the transaction layer? I figured that would be the domain of the networking protocol only?  eg. dandelion++

## dbee01 | 2025-02-08T05:56:52+00:00
So,  i've had a look at the Dandelion++ academic paper.  This network protocol has it's own more eleoquent version of the Phalanx Defence i posited above.  

In Dandelion++,  during the stem phase of node propagation. The protocol uses a mechanism called the _first spy estimator_ to gauge the trustworthiness of transactions.   

The mechanism observes the time it takes for a transaction to propagate, how many relays it goes through, and which nodes receive it first. I guess it makes more sense to evaluate transactions as opposed to nodes? 

The ultimate goal is to preserve anonymity on the network and defeat Byzantine General attacks. The Anonymity Metrics used include Precision and Recall described by,:

`
D​(v) 	=𝟙​(𝙼​(Xv)=v)∑u∈VH𝟙​(𝙼​(Xu)=v) 	

R​(v) 	=𝟙​(𝙼​(Xv)=v), 	
`

 This is all fascinating. I'm nerding out... 



## selsta | 2025-02-09T10:26:08+00:00
Yes, we use Dandelion++ since around 2020. Closing this as general discussions or ideas like this are better suited on other platforms.

# Action History
- Created by: dbee01 | 2025-02-07T16:55:23+00:00
- Closed at: 2025-02-09T10:26:08+00:00
