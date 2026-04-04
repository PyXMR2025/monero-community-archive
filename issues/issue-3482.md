---
title: Potential issue with Lithium Luna' (v0.12.0.0-master-8361d60)
source_url: https://github.com/monero-project/monero/issues/3482
author: Admiral-Noisy-Bottom
assignees: []
labels:
- invalid
created_at: '2018-03-23T00:42:17+00:00'
updated_at: '2018-04-07T22:08:47+00:00'
type: issue
status: closed
closed_at: '2018-03-27T23:48:49+00:00'
---

# Original Description
If I run testnet using "Lithium Luna' (v0.12.0.0-master-8361d60)" and when a payment is sent to the pool wallet the monero-wallet-rpc says;

_2018-03-23 00:18:55.146	[RPC0]	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:5269	Requested ring size 4 too low for hard fork 7, using 7_

followed by;

_2018-03-23 00:18:55.894	[RPC0]	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:7316	needed_money > unlocked_balance_subtotal. THROW EXCEPTION: error::not_enough_unlocked_money_

The pool wallet never receives the block reward, but it does try to send payments to each miner. This strikes me as a Monero issue rather than a pool issue because nothing changed for the pool. The only difference is the release of Monero being used.

When using "'Helium Hydra' (v0.11.1.0-release)" everything works just fine. The wallet receives funds and transfers to miners without issue.


# Discussion History
## moneromooo-monero | 2018-03-23T10:48:31+00:00
What is the "refresh-from-block-height" value when you run "set" in monero-wallet-cli ?
Also, please use a sensible title.

## Admiral-Noisy-Bottom | 2018-03-23T21:11:56+00:00
refresh-from-block-height = 875158

Also, the daemon still says I'm 80 days ahead which is an improvement on 187 days like it was.

_2018-03-23 21:12:05.443	[P2P6]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:310	[45.79.81.196:28080 OUT] Sync data returned a new top block candidate: 1123841 -> 1066057 [Your node is 57784 blocks (80 days) ahead]_

Sorry about the title, I couldn't think of anything better at the time.


## moneromooo-monero | 2018-03-23T22:26:25+00:00
You're just on a wrong chain. Did you sync that chain with the current code ?

## Admiral-Noisy-Bottom | 2018-03-24T03:48:16+00:00
Yes, I did. The binaries were built from source. Typing alt-chain-info says 0. 

Because I'm stuck and can't proceed until this is resolved I've exported the chain up to an earlier height. I'm in the process of importing it. If that doesn't sort the problem out I'll have to delete the chain and let it sync from scratch.

## plavirudar | 2018-03-25T01:26:53+00:00
You need to pop blocks off the chain using `monero-blockchain-import`. 

## Admiral-Noisy-Bottom | 2018-03-25T08:49:48+00:00
That's what I ended up doing. I then let the daemon sync and after awhile it said there was an alternative chain.

I'm not bothered much right now because after letting it sync up again the pool began paying miners, so I'm happy with that.

Damn the monero-blockchain-import takes a life time :)

Thanks for your help.

## moneromooo-monero | 2018-03-27T23:25:36+00:00
+invalid

## gituser | 2018-04-07T22:08:47+00:00
I had pretty much the same issue. My old monerod has been running for 10+ hours since the fork and got ahead at about 300+ blocks. 
Just updating didn't resolve the situation, the wallet (in cli and in rpc) still reported that it's ahead by 300+ blocks, but in logs I could see that there is some reorg is happening.

So, to be sure, I've re-synced whole blockchain and now it's correctly reporting latest block height.

And yes, you can use `monero-blockchain-import` to speed up things ..

# Action History
- Created by: Admiral-Noisy-Bottom | 2018-03-23T00:42:17+00:00
- Closed at: 2018-03-27T23:48:49+00:00
