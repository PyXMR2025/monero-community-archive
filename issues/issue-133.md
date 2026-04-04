---
title: Proof-of-Work-Enabled Relay ("PoWER")
source_url: https://github.com/monero-project/research-lab/issues/133
author: j-berman
assignees: []
labels: []
created_at: '2025-07-21T23:43:06+00:00'
updated_at: '2025-10-20T22:28:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Overview

128-input FCMP++ txs currently take >3s to verify on high-end machines. There is room for further optimization, however, it's estimated that verification of high input txs will be far from instant. Additionally, creating invalid txs is effectively instantaneous.

This presents a DoS vector: a malicious actor would be able to spam a node with high input junk txs, forcing the node to waste cycles verifying junk. The problem is made worse if the malicious actor has access to many IP's.

To mitigate this, we propose tx relayers require PoW on connection in order to relay high-input txs. Thus, nodes can cheaply verify the PoW, raising the cost of attack from effectively 0 to >0.

Finally, since 8-input txs verify in ~150-200ms (further optimizations are potentially on the table), and since we have had problems in the past with blanket bans on PoW algorithms (e.g. Windows banning software that ships with RandomX), we do not require PoW-enabled relay for txs with less than or equal to 8 inputs. As such, wallet implementers can avoid shipping PoW algorithms with their software and limit max tx input counts to 8.

This proposal was initially discussed in this MRL meeting: https://github.com/monero-project/meta/issues/1197

## PoW Algorithm

The current proposed algorithm is Equi-X, since it enables fast verification, has a light memory footprint, and should not trip up antivirus software flagging RandomX.

## Difficulty Requirement

Ideally, there would be a difficulty adjustment that increases as the node receives high input txs. However, this presents synchronization challenges (e.g. wallet submits, difficulty increases, wallet's PoW is now too low, wallet's submission fails, wallet must redo PoW).

Instead, we suggest a fixed difficulty that takes as long to construct as it takes to verify a 128-input proof on a reference machine. Thus, an attacker is obligated to expend a similar amount of CPU power as the node does in verifying. Suggested [here](https://libera.monerologs.net/monero-research-lab/20250723#c544099-c544104).

## p2p/RPC changes

As suggested by @Boog900, a node that relays txs may require PoW a single time per connection in order to relay >8-input txs over the connection.

## Wallet API changes

The wallet API should support devs who want to specify a max input count for tx construction.

## Other Considerations

### Fingerprint-ability

Wallets that choose to only support up to 8-input txs may end up sticking out (bursts of 8-input txs may suggest this e.g.).

# Discussion History
## kayabaNerve | 2025-07-21T23:49:13+00:00
Why not use Tor's PoW algorithm which has a far faster verification time and should be similarly CPU-focused?

## UkoeHB | 2025-07-22T01:32:51+00:00
> Ideally, there would be a difficulty adjustment that increases as the node receives high input txs. However, this presents synchronization challenges (e.g. wallet submits, difficulty increases, wallet's PoW is now too low, wallet's submission fails, wallet must redo PoW).

Instead of filtering txs on a fixed difficulty, they can filter on the minimum of a range of difficulties (e.g. 10 minutes worth). The core wallet would use the newest difficulty value when doing PoW (although alternative implementations could exploit the window).

## j-berman | 2025-07-22T02:59:03+00:00
@UkoeHB can you expand on that idea a bit?

______

@kayabaNerve I think Equi-X (tor's algorithm) would be ok. Below is my best argument for RandomX light over Equi-X for our use case, but I'm fine with Equi-X too. Note here is @tevador's rationale for Equi-X in tor: https://github.com/tevador/equix/blob/master/devlog.md

When considering just the DoS, RandomX light's 15ms verification time is effectively irrelevant because we expect 8 input txs to take over 10x that to verify (the malicious actor is incentivized to DoS via fake 8-input txs).

Ignoring future optimizations to verification, 15ms PoW verification would add a ballpark estimated max overhead of roughly 10% for processing newly relayed 9-input txs, and maybe 1% for 128-input txs, which seems a fairly small cost added to tx relay. If that materializes into something that noticeably impacts UX, I would think we have more significant problems.

Benefits of RandomX light over Equi-X:
- ASIC resistant
- RandomX is already used in the Monero repo which means it'll be a simpler process to integrate

Benefits of Equi-X over RandomX light:
- Negligible verification time
- Negligible memory footprint
- Potentially less likely to be flagged by antivirus (i.e. irrational) policy

I'd argue it could make sense to take the ASIC resistance win considering the above rationale. Compared to tor, since Monero is a tradeable asset that could be shorted e.g., there is potentially a more significant monetary incentive to attack this DoS vector via an ASIC (and thus there is potentially stronger incentive to develop one). I don't have a particularly strong opinion on it though, I think Equi-x would be fine too and it would be fairly simple to adjust if an ASIC appears since this wouldn't require a fork.


## kayabaNerve | 2025-07-22T13:08:21+00:00
Equi-X was also designed to avoid notable speedups via GPUs and FPGAs.

## j-berman | 2025-07-22T13:29:10+00:00
But not to avoid notable speedups via ASICs, which is the main advantage of RandomX light over Equi-X

## UkoeHB | 2025-07-23T02:21:20+00:00
> @UkoeHB can you expand on that idea a bit?

The synchronization problem is that the node's current difficulty can change after a client queries it, possibly invalidating txs built with the queried value. If a specific difficulty value remains 'valid' for some timespan after it is created (pushed to the head of the difficulty sequence), then clients would have time to query the most recent difficulty, construct a tx, and submit it. When validating txs, nodes just need to validate against the lowest difficulty in that timespan instead of the difficulty at the head of the difficulty sequence.

## j-berman | 2025-07-23T17:28:48+00:00
Got it. I think a v1 with fixed difficulty is a sensible start to raise the cost to an attacker from 0 to >0, and I would advocate for a change toward dynamic difficulty adjustment if we find that a fixed difficulty is insufficient. There are some edges to work through with that approach (client requests difficulty toward the end of a timespan and difficulty adjusts upward immediately after constructing, what if the timespan is still adjusting insufficiently to thwart an attacker, what if an attacker raises the difficulty for honest submissions), and it adds a bit more meat to nodes (stateful temporary difficulty tracking/adjusting). I think the effort to harden for all edge cases and its implementation may not be worth the gain from a simple fixed difficulty for v1.

## UkoeHB | 2025-07-23T18:03:12+00:00
> client requests difficulty toward the end of a timespan and difficulty adjusts upward immediately after constructing, what if the timespan is still adjusting insufficiently to thwart an attacker, what if an attacker raises the difficulty for honest submissions

The timespan would be a rolling window. Other than that, yeah I agree some design for the difficulty adjustment algo would be needed and probably not necessary for v1.

## cryptozoidberg | 2025-07-25T14:47:24+00:00
if i may as quick question - did you consider to charge more fee for computationally heavy transactions? as a hashing power is a resource after all, which might be bought/rented

## j-berman | 2025-07-25T18:31:38+00:00
> did you consider to charge more fee for computationally heavy transactions?

The DoS vector is a malicious actor crafting invalid txs, so the fee does not go to anyone

## cryptozoidberg | 2025-07-26T20:23:36+00:00
> > did you consider to charge more fee for computationally heavy transactions?
> 
> The DoS vector is a malicious actor crafting invalid txs, so the fee does not go to anyone

oh i see, thanks for clarifying! 
picking up right hash function might be a quite challenging thought, using heavy hash could cause some complications. 

I don't know how FCMP works in terms of protocol, just curious if this intuitive idea might work - if transaction has, for example 10 inputs(10 key images), and 0,1,2... was verified ok but last one was intentionally crafted as broken, is there any chances to black list then first 9 key images on tx pool level, so an attacker won't be able to use those key images again? It's not completely eliminate problem but it make attack more expansive - attacker now need to pay fee for transactions that would generate multiple cheap outputs than could be used only one time.


## kayabaNerve | 2025-07-27T05:50:02+00:00
That would allow malleating third-party transactions to (soft-)burn arbitrary outputs unless a binding signature was added during relay (though that'd be via a randomly weighted combination of all inputs and still of linear time complexity to verify).

## j-berman | 2025-07-28T23:21:27+00:00
Highlighting two main points of discussion from [last MRL meeting](https://libera.monerologs.net/monero-research-lab/20250723#c544006-c544165). 

1) PoW for each relayed tx vs. PoW per wallet & p2p connection.
2) RandomX light vs. Equi-X

### PoW per-tx vs. per-connection

@boog900 raised the point of requiring PoW on connection attempts (instead of on tx relay) in order to avoid needing to deal with txs sitting in the pool longer than 10 blocks. I think this is a reasonable proposal, since it would obligate an attacker to expend the same amount of CPU in order to relay a single bad tx (assuming we modify nodes to ban connections that relay txs that fail to verify).

@jeffro256 argues that this may incentivize malicious nodes to flood the network, causing honest nodes seeking other honest nodes to instead connect to malicious nodes and repeatedly do wasted PoW calculations, potentially opening another DoS vector that way.

Unconfirmed, but I personally *think* malicious nodes already *can* hold connections without responding for a longer period than the time it takes to even calculate the proposed PoW, thus holding connections hostage with the same effect (or potentially even worse), and I'm not 100% convinced a 1-2s PoW would incentivize notably worse behavior.

### RandomX light vs. Equi-X

Both @boog900 and @kayabaNerve have expressed support for Equi-X on grounds of our use case being roughly equivalent to tor's.

@jeffro256 expressed support for RandomX because the daemon would already have a RandomX scratchpad loaded for block verification, and if Equi-X is complex, voiced support to avoid adding the additional dependency ([source](https://libera.monerologs.net/monero-research-lab/20250723#c544130)). This raises a valid point worth clarifying imo too: since RandomX light and RandomX are interchangeable, and since the daemon would have the RandomX scratchpad loaded already, the daemon can actually just reuse RandomX verification, which @tevador notes [here](https://github.com/tevador/equix/blob/master/devlog.md#randomx) is expected to take 2ms. Wallets with tight memory constraints can choose to use RandomX light instead of RandomX in order to construct the PoW's.

I personally contend we have a set of circumstances and context distinct from tor that justify the decision to use RandomX over Equi-X.

## Boog900 | 2025-07-29T13:04:49+00:00
> the same amount of CPU in order to relay a single bad tx

If we include attacks on multiple nodes using the same tx, then PoW per connection is better, as you need PoW for each connection.

> assuming we modify nodes to ban connections that relay txs that fail to verify

The node just needs to drop the connection, which IMO would be better than a ban and is already currently done.

---

> RandomX scratchpad loaded for block verification

RandomX has 2 types of lookup tables: the cache and the dataset. The cache is 256 MB and is used for light mode, the dataset is 2GB and is used for fast mode. `monerod` by default only uses light mode, so does have a cache built but doesn't have the full dataset.

Also, if we were to use PoW per connection, nodes would not necessarily have a cache built. If they are far behind the peer they are connecting to, they would have to construct a new cache.

## j-berman | 2025-07-29T15:16:44+00:00
Valid points

Another lingering question I'm curious about. The RandomX description states:

> The fast mode is suitable for "mining", while the light mode is expected to be used only for proof verification.

I'm wondering if this means wallets would end up needing to use the fast mode to construct the PoW. If that's the case, I think Equi-X is definitely looking more suitable, as we wouldn't want wallets burdened with an additional 2 GB requirement out of the box to support this feature.

## Boog900 | 2025-07-29T15:49:31+00:00
light vs fast mode just trades speed for lookup table size. If we were to tune the difficulty of the PoW for light mode then anyone who uses fast mode would be able to compute the PoW way faster than intended, so yes we would probably need to tune for fast mode. 

## j-berman | 2025-07-29T15:54:23+00:00
Now wondering how long it would take to construct a PoW using light mode that takes fast mode 1-2s on commodity hardware

## cryptozoidberg | 2025-07-29T19:19:25+00:00
> That would allow malleating third-party transactions to (soft-)burn arbitrary outputs unless a binding signature was added during relay (though that'd be via a randomly weighted combination of all inputs and still of linear time complexity to verify).

sorry, how someone can soft-burn third-party transaction's outputs? if the ones that is to be blacklisted was valid meaning whoever creating it must at least have control over those outputs 

UPD: Nevermind, i think i figured this

## Boog900 | 2025-07-30T19:43:44+00:00
> Now wondering how long it would take to construct a PoW using light mode that takes fast mode 1-2s on commodity hardware

I just did a quick test and got 8s, if we use tevador's numbers: 15ms vs 2ms this is pretty much what I would have expected.  

## j-berman | 2025-07-30T20:51:34+00:00
An additional 7s or 2GB is a fairly significant cost to impose on wallets imo. I'm content with Equi-X personally.

## FocuzJS | 2025-07-31T02:09:40+00:00
Some stats on the non-linearity of verification time due to EquiHash usage in Equi-X run on my 8700k.

```
> ./equix-bench --nonces 5000 --start 5000 --threads 12
Solving nonces 5000-9999 (interpret: 0, hugepages: 0, threads: 12) ...
1.993200 solutions/nonce
2276.089782 solutions/sec. (12 threads)
122691.984773 verifications/sec. (12 threads for verification)

> ./equix-bench --nonces 5000 --start 5000 --threads 1
Solving nonces 5000-9999 (interpret: 0, hugepages: 0, threads: 1) ...
1.993200 solutions/nonce
368.073084 solutions/sec. (1 thread)
26873.007645 verifications/sec. (1 thread for verification)
```

equix-bench is only 43kb -- the additional dependency is likely negligible.

## hinto-janai | 2025-10-07T17:31:31+00:00
Last updated: 2025-10-15.

Here's an impl proposal, choices are gathered from here and recent MRL discussion.

Assumptions:
- The PoW algorithm used is EquiX
- PoWER is only mandatory for public interfaces that allow relaying transactions (where those transactions have >8 inputs)
- PoW must only be provided once per "unique" connection
- PoW difficulty is fixed

PoWER will be mandatory for high-input transactions in the following interfaces:

- P2P
- Restricted RPC
	- [`relay_tx`](https://docs.getmonero.org/rpc-library/monerod-rpc/#relay_tx)
	- [`/send_raw_transaction`](https://docs.getmonero.org/rpc-library/monerod-rpc/#send_raw_transaction)
- ZMQ
	- [`send_raw_tx`](https://github.com/monero-project/monero/blob/8e9ab9677f90492bca3c7555a246f2a8677bd570/src/rpc/daemon_handler.cpp#L104)
	- [`send_raw_tx_hex`](https://github.com/monero-project/monero/blob/8e9ab9677f90492bca3c7555a246f2a8677bd570/src/rpc/daemon_handler.cpp#L105)

## Parameters

General parameters that could be tuned.

| parameter                 | value   | description |
|---------------------------|---------|-------------|
| `POWER_INPUT_THRESHOLD`   | 8       | PoWER is mandated for transactions with input counts greater than this (for interfaces in which PoWER is used)
| `POWER_TARGET_DIFFICULTY` | ?       | Fixed difficulty used by nodes
| `POWER_MAX_ACTIVE_NONCES` | 100,000 | Maximum amount of pending challenge slots allowed in memory for RPC/ZMQ (rough estimate: `16-byte nonce` + `8-byte expiry` + `16-byte address` + `2-byte port` * `100,000` = 4.2 megabytes). This could be a config option.

## Challenge
The challenge for all interfaces is:

```
H = equix(nonce)
```
where `nonce` is a random 128-bit integer.

## P2P
The changes for P2P are:
- 2 fields to the `COMMAND_HANDSHAKE` response, a 128-bit `nonce` field and 64-bit `difficulty` field; each unique connection generates a new nonce
- 1 new command, `COMMAND_POWER_SOLUTION` (`2010`), to enable high-input transaction relay on that particular connection as long as it is open

The exchange between nodes:

1. `Node A` sends `COMMAND_HANDSHAKE` request
2. `Node B` sends `COMMAND_HANDSHAKE` response
3. `Node A` calculates a solution and sends `COMMAND_POWER_SOLUTION`
4. `Node B` marks `Node A` as valid to relay high-input transactions

Nonces are held in a map of `<connection, nonce>` until either the connection is dropped or the solution is provided.

## RPC/ZMQ
A new endpoint is added, it returns:
```cpp
struct power_challenge {
	// Random nonce used as challenge
    std::array<std::uint8_t, 16> nonce;

	// Challenge expiry time in UNIX seconds
    std::uint64_t expiry;

	// Target difficulty for valid PoW
    std::uint64_t difficulty;
};
```

Existing TX relay endpoint requests will have an optional field added where the solution to `power_challenge` must be provided for high-input transactions, otherwise they are rejected.

Nonces are held in a map of `<connection, (nonce, expiry)>` until the connection is dropped, the solution is provided, or the `expiry` is reached.

## Penalties
Penalties dealt by the node when the client fails to comply with PoWER.

| failure mode  | penalty |
|---------------|---------|
| Missing PoW   | ?
| Expired PoW   | ?
| Incorrect PoW | ?
| Malformed TX  | ?

## Issues
- The RPC/ZMQ endpoints can be spammed to take up slots; it must have a limit to avoid memory exhaustion
- `difficulty` must be sanity checked as a malicious node could set it high
- Wallets will need access to more state, high input transactions with offline wallets may be more complex; private APIs (e.g. unrestricted `send_raw_transaction`) could calculate the PoW if not already found?

## hinto-janai | 2025-10-20T22:28:24+00:00
Point from the last [MRL meeting](https://libera.monerologs.net/monero-research-lab/20251015#c599518-c599603):

### Requiring held RPC connections for high-input transactions 
@Boog900 proposed requiring RPC clients to hold their connection to relay high-input transactions, this would be a simpler implementation and would allow RPC to operate like P2P. Boog also noted that this is already the current behavior for `wallet2` and `monero-oxide`.

@jeffro256 noted this would break developer flows.

I agree with jeffro, although it could be a tradeoff worth taking as IMO the tracking of state and connections for RPC connections gets complicated, assuming:
- an RPC client connects twice, once for the challenge, once to submit TX + PoW
- the node marks the client as valid to relay high-input transactions without further PoW (PoW per connection)

Then the RPC client must be identified on further connections:
- ports are not reliable identifiers if the client is connecting/disconnecting
- the IP by itself can work although that means shared IPs (VPN, Tor exit) only require PoW once
- unique challenge data as the identifier means PoW can be shared
- unique challenge data + IP would be better although this can still be worked around

Alternatively, PoW per connection for P2P/ZMQ and PoW per TX for RPC seems okay to me as it avoids relying on network details.

# Action History
- Created by: j-berman | 2025-07-21T23:43:06+00:00
