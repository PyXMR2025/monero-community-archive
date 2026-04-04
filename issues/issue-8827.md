---
title: '[Proposal] Improve PoW verification at the next hard fork'
source_url: https://github.com/monero-project/monero/issues/8827
author: tevador
assignees: []
labels:
- proposal
created_at: '2023-04-22T12:10:13+00:00'
updated_at: '2025-08-15T07:58:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm proposing a small change to the PoW algorithm to be implemented at the next hard fork (together with Seraphis).

As opposed to the previous PoW changes, this one is completely unrelated to ASIC resistance.

The purpose of the change is to enable a very fast partial verification of the PoW. Essentially, my proposal is to replace the final Blake2b hash with a double Blake2b hash. Technical details are in this issue: https://github.com/tevador/RandomX/issues/258

Additionally, a new 32-byte field (the intermediate hash) would be added to the block header. This would increase the blockchain size by about 8 MB per year, which is negligible given the large benefits that this change would bring.

What are the benefits?

* Enhanced denial-of-service (DoS) protection of all nodes in the network. PoW verification typically consumes about 15 milliseconds of CPU time and can become a DoS vector if a malicious actor started flooding the network with invalid blocks. My proposal allows for pre-verification that takes only 300 nanoseconds and makes such DoS attacks ineffective.

* Significant performance boost for [light nodes](https://github.com/monero-project/research-lab/issues/69) that rely solely on PoW verification. Light nodes could only verify the PoW partially and do full RandomX validation only for the top N blocks. This would reduce their CPU demands by up to 4 orders of magnitude.

* Better security for wallets using untrusted remote nodes. Malicious remote nodes can feed wallets fake blockchain data. With this proposal, wallets could partially verify the integrity of the blocks received from untrusted remote nodes with the cost of a few hashes.

# Discussion History
## hyc | 2023-04-22T14:39:13+00:00
Sounds like a big win. Aside from the 8MB size overhead, what are any other potential downsides?

## tevador | 2023-04-22T16:17:14+00:00
The blockchain grows at around 40 GB/year at the moment, so the space overhead of this change would be about 0.02%.

The additional hash calculation would reduce hashrate by about 0.02%, which is also negligible and I don't think miners would object (or even notice).

AFAIK there has never been a change of the block header format before, so this would be the first time, but I don't think it would cause problems. And Seraphis already completely changes the block format anyways.

We would need to support both versions of RandomX, but the RandomX repository can easily support that as there are no changes to the internals, so "v2" can be realized by adding 1 function to the public API.

I can't think of any major drawbacks.



## SChernykh | 2023-04-22T17:26:47+00:00
What prevents faking the intermediate hash? An attacker can just run Blake2b miner to produce valid intermediate hashes.
Edit: found it in [#258](https://github.com/tevador/RandomX/issues/258) - so 1 minute to generate the fake intermediate hash on GPU?

## tevador | 2023-04-22T17:32:51+00:00
> What prevents faking the intermediate hash? An attacker can just run Blake2b miner to produce valid intermediate hashes.

Yes, they can do that, it would cost about 1 minute with a high-end GPU to produce such a hash. You would need a large GPU farm to mount a DoS attack on the network.

Currently it takes *no effort* to produce a fake block and force the target node to spend CPU time running RandomX.

## moneromooo-monero | 2023-04-22T17:49:50+00:00
That sounds lke a great improvement, and one that doesn't really need to wait for seraphis (which I assume will be about two years ?)

## tevador | 2023-04-22T17:57:31+00:00
> doesn't really need to wait for seraphis

This change needs a hard fork and AFAIK there are no hard forks planned before seraphis, which I'm assuming to happen in 2024.

## jtgrassie | 2023-04-22T21:33:40+00:00
Fully support this. 

On deployment, yes needs a hard fork, but we don't need to wait for a seraphis fork – I assume we'll have a hard fork before seraphis, as we'll likely have bulletproof++ ready much earlier (as just one example).

## selsta | 2023-04-22T21:38:54+00:00
I'd also be in favour of deploying BP++ and this RandomX change before Seraphis.

## hundehausen | 2023-04-27T12:38:02+00:00
This improvement is so big, I wouldn't want to wait two years to make it happen. We can hard fork whenever we have improvements. 

## MaxXor | 2025-08-15T07:58:42+00:00
Feels like it should be put back on the agenda?

# Action History
- Created by: tevador | 2023-04-22T12:10:13+00:00
