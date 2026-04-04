---
title: GUI wallet v0.16.0.0 error outputs in terminal loading blocks
source_url: https://github.com/monero-project/monero/issues/6652
author: downystreet
assignees: []
labels: []
created_at: '2020-06-13T18:05:50+00:00'
updated_at: '2022-02-19T04:30:11+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:30:11+00:00'
---

# Original Description
I just downloaded the new GUI wallet v0.16.0.0 and its got some error outputs in the terminal when its loading the wallet blocks.
 2020-06-13 17:52:20.082	I Monero 'Nitrogen Nebula' (v0.16.0.0-release)
Forking to background...
2020-06-13 17:53:19.400	E wrong number of additional derivations
2020-06-13 17:53:19.767	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2020-06-13 17:53:57.492	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error


# Discussion History
## moneromooo-monero | 2020-06-13T18:30:24+00:00
The "wrong number of additional derivations" is fine. Some tx is just weird on the chain. The other one is only fine if it recovers, which it's supposed to. Does it recover ?

## downystreet | 2020-06-13T18:38:24+00:00
What do you mean by recover? The wallet itself seems to be working fine and is loading the blocks but there is no more output in the terminal after what I submitted, however it isn't finished loading all of the blocks yet. It's about 60% done loading the blocks after approximately 45 minutes.

## moneromooo-monero | 2020-06-13T18:56:58+00:00
I meant "it does not print it again and otherwise continues working normally", which it seems to be doing. This error can happen if you load a wallet on a blockchain from which the top blocks have been removed (unlikely in normal use, but happens when debugging). If it prints this once then goes on happily, all is fine. Just be on the lookout for anything not working just in case.

## downystreet | 2020-06-13T19:02:48+00:00
Alright, I'll keep an eye out. I wasn't debugging, all I did was download it and start it up, so its whatever the default blockchain address is.

## downystreet | 2020-06-13T22:04:27+00:00
Here is the rest of the terminal after loading the blocks:
2020-06-13 20:16:10.671	E wrong number of additional derivations
2020-06-13 20:20:08.080	W Transaction extra has unsupported format: <f6cff1edd1a7861ed13d494dd4ae7c4a7f42b5c3bf91457310d2166722c1316f>
2020-06-13 20:20:09.313	W Failed to generate key derivation from tx pubkey, skipping
2020-06-13 20:22:54.120	W Failed to generate key derivation from tx pubkey, skipping
2020-06-13 20:37:22.600	W Transaction extra has unsupported format: <97ef64005b33f2ff9764b5537ad565159bc95419b07a3070e90a63ac7f5c9988>
2020-06-13 20:37:22.603	W Transaction extra has unsupported format: <58013973b0ccbf74d2d4ecca6d46356655bc27d1ef7649a02212ee670f853048>


## moneromooo-monero | 2020-06-13T23:22:02+00:00
These are all fine.

# Action History
- Created by: downystreet | 2020-06-13T18:05:50+00:00
- Closed at: 2022-02-19T04:30:11+00:00
