---
title: Constant "error::out_of_hashchain_bounds_error" errors when syncing
source_url: https://github.com/monero-project/monero/issues/8726
author: c0inthrow3r
assignees: []
labels: []
created_at: '2023-01-31T21:15:27+00:00'
updated_at: '2023-03-05T05:41:40+00:00'
type: issue
status: closed
closed_at: '2023-03-05T05:41:40+00:00'
---

# Original Description
I opened my old monero wallet after 2 years? maybe, started syncing. Syncing is going very slowly like it used to be but now there's another problem, errors like this are printed constantly and syncing doesn't look like it's working at all now. 

Most of the time the progress bar says "Waiting for daemon to sync" / "Daemon blocks remaining <500 000+>" and this number goes down very slowly. Every now and then it changes to "Wallet is synchronized" / "Daemon is synchronized (<2 000 000+>)", the upper progress bar flashes, and then it changes back.

But now there are lots of these errors and the remaining blocks number just goes UP not down. 

I have tried --block-sync-size arg with different values like 500, 200, 1500. Performance is not improved bu I think these errors maybe more common?

```
I Monero 'Fluorine Fermi' (v0.18.1.2-release)
Forking to background...
2023-01-31 20:59:11.398	E Blocks start before blockchain offset: 0 2720000
2023-01-31 20:59:11.455	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 20:59:12.994	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 20:59:23.049	E Blocks start before blockchain offset: 0 2720000
2023-01-31 20:59:23.075	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 20:59:24.448	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:00:05.683	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:00:05.723	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:00:07.128	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:00:17.185	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:00:17.208	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:00:18.717	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:00:28.777	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:00:28.802	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:00:34.216	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:01:14.326	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:01:14.353	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:01:15.671	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:01:26.505	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:01:26.551	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:01:27.906	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:01:37.983	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:01:38.022	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:01:39.451	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:01:49.499	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:01:49.530	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:01:51.136	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:02:01.204	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:02:01.241	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:02:07.829	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:02:17.900	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:02:17.946	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:02:19.239	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:02:29.348	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:02:29.417	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:02:35.159	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:02:45.239	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:02:45.274	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:02:46.482	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:02:56.588	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:02:56.622	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:03:06.544	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:03:36.634	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:03:36.673	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:03:38.497	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:03:48.571	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:03:48.612	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:03:50.410	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:04:00.481	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:04:00.506	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:04:02.101	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:04:44.527	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:04:44.553	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:04:46.487	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:04:56.562	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:04:56.593	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:04:58.533	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:05:11.339	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:05:11.380	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:05:12.694	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:11:31.701	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:11:31.734	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:11:33.053	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:11:43.114	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:11:43.156	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:11:44.414	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error
2023-01-31 21:11:54.476	E Blocks start before blockchain offset: 0 2720000
2023-01-31 21:11:54.499	E !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::out_of_hashchain_bounds_error
2023-01-31 21:11:55.755	E (m_blockchain.size() == stop_height || (m_blockchain.size() == 1 && stop_height == 0) ? false : true). THROW EXCEPTION: error::wallet_internal_error 
```

# Discussion History
## selsta | 2023-01-31T21:17:20+00:00
What hardware are you running monerod on? How long have you been syncing? Also try to use the default settings regarding  `--block-sync-size`.

## c0inthrow3r | 2023-01-31T21:21:24+00:00
@selsta my CPU is Core i7 3770 and 16Gb RAM, 4 TB Seagate HDD for blockchain, I think GPU does not matter. 
I used the default value at first but it was slow... I started experimenting to make it faster. I will try again with defaults, thanks. 

## selsta | 2023-01-31T21:22:17+00:00
Using a SSD will significantly speed up sync. How long have you been syncing and how much did you progress?

## c0inthrow3r | 2023-01-31T21:26:45+00:00
Hm I don't know how long but I'll estimate, I think maybe 20 or 30 hours total now (after I opened the wallet this year...), progressed a few GBytes into the blockchain file.

It was slow, like very very slow when I downloaded the blockchain originally... But now I saw those errors, lots of them. It always makes me think if my blockchain is corrupt. 

Ok, I started with default value for `--block-sync-size` and now the remaining blocks number instantly decreased! Just coincidence, or does this mean I shouldn't touch that option? :o 

## selsta | 2023-01-31T21:30:34+00:00
Is `out_of_hashchain_bounds_error` a wallet error? If yes try to let the daemon sync and then try to sync your wallet.

## c0inthrow3r | 2023-01-31T21:33:24+00:00
@selsta I'm not sure... but I think it may be, it says `wallet_internal_error`...
Syncing daemon vs syncing wallet is a little confusing to me. Every now and then it indeed says it's synchronizing the wallet... most of the time it's waiting for daemon to sync.

Also, a question... What work / how much must be done to sync a received block into the local blockchain? Basically if slow HDD is the bottleneck it must require lots of data to/from disk... But what steps does it take?

## selsta | 2023-01-31T21:34:58+00:00
Blocks have to be verified, which means loading a lot of small amount of historical blockchain data for the verification process. Random IO speeds are important for sync and SSD helps significantly.

## selsta | 2023-03-05T05:41:40+00:00
This issue should be solved after you have fully synced up your daemon. If you continue to have issues please comment and I'll reopen.

# Action History
- Created by: c0inthrow3r | 2023-01-31T21:15:27+00:00
- Closed at: 2023-03-05T05:41:40+00:00
