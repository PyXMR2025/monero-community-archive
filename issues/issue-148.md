---
title: Nodes stop accepting txs in pool, pool total byte size tally seems incorrect
source_url: https://github.com/seraphis-migration/monero/issues/148
author: j-berman
assignees: []
labels:
- upstream
created_at: '2025-10-08T21:38:57+00:00'
updated_at: '2025-12-08T19:32:31+00:00'
type: issue
status: closed
closed_at: '2025-12-08T19:32:30+00:00'
---

# Original Description
Present on Monereo's master branch too (tested by @nahuhh). Should open an issue with more context upstream.

# Discussion History
## nahuhh | 2025-10-08T23:27:07+00:00
```
2025-09-28 00:57:18.031 I Pruning tx <7a0894e7e05d77b55d697789651e70b4549c17e6e8c26958d5724b0b8ca89dbb> from txpool: weight: 12101, fee/byte: 1.1e+07
2025-09-28 00:57:18.031 I Pruned tx <7a0894e7e05d77b55d697789651e70b4549c17e6e8c26958d5724b0b8ca89dbb> from txpool: weight: 12101, fee/byte: 1.1e+07
2025-09-28 00:57:18.031 D Transaction removed from pool: txid <7a0894e7e05d77b55d697789651e70b4549c17e6e8c26958d5724b0b8ca89dbb>, total entries in removed list now 3900
2025-09-28 00:57:18.031 D Erased 8 old transactions from removed list, leaving 3892
2025-09-28 00:57:18.033 I Pool weight after pruning is larger than limit: 649404464/648000000
```

Log lvl 2 from private fcmp testnet

the 3892 txs was definitely _not_ greater than 648000000bytes.

During this time, my txpool(s) would show exactly 1 tx via print_pool[_[stats|sh]]

## nahuhh | 2025-10-26T23:54:43+00:00
Similar, but not seeing the incorrect txpool size

Pool shows 1tx. evicting incoming txs

```
2025-10-26 23:50:19.579 D Using 0.000000019000/byte fee                                                                                                             23:50:19 [64/293128]
2025-10-26 23:50:19.579 D RCT cache: tx <69c2e3e1f2013adbb9edb99ea95fca2faab96337286d366049ae493bee561038> missed                                                                       
2025-10-26 23:50:19.629 D DB map size:     354445434880                                                                                                                                 
2025-10-26 23:50:19.629 D Space used:      42518470656                                                                                                                                  
2025-10-26 23:50:19.629 D Space remaining: 311926964224                                                                                                                                 
2025-10-26 23:50:19.629 D Size threshold:  0                                                                                                                                            
2025-10-26 23:50:19.629 D Percent used: 11.9958  Percent threshold: 90.0000                                                                                                             
2025-10-26 23:50:19.631 I Transaction added to pool: txid <69c2e3e1f2013adbb9edb99ea95fca2faab96337286d366049ae493bee561038> weight: 6498 fee/byte: 20000, count: 2                     
2025-10-26 23:50:19.631 D DB map size:     354445434880                                                                                                                                 
2025-10-26 23:50:19.631 D Space used:      42518470656                                                                                                                                  
2025-10-26 23:50:19.631 D Space remaining: 311926964224                                                                                                                                 
2025-10-26 23:50:19.631 D Size threshold:  0                                                                                                                                            
2025-10-26 23:50:19.631 D Percent used: 11.9958  Percent threshold: 90.0000                                                                                                             
2025-10-26 23:50:19.631 I Pruning tx <69c2e3e1f2013adbb9edb99ea95fca2faab96337286d366049ae493bee561038> from txpool: weight: 6498, fee/byte: 20000                                      
2025-10-26 23:50:19.631 I Pruned tx <69c2e3e1f2013adbb9edb99ea95fca2faab96337286d366049ae493bee561038> from txpool: weight: 6498, fee/byte: 20000                                       
2025-10-26 23:50:19.631 D Transaction removed from pool: txid <69c2e3e1f2013adbb9edb99ea95fca2faab96337286d366049ae493bee561038>, total entries in removed list now 15853
2025-10-26 23:50:19.633 D tx added to pool: <69c2e3e1f2013adbb9edb99ea95fca2faab96337286d366049ae493bee561038>
2025-10-26 23:50:19.634 D bulletproof+ clawback: 0
2025-10-26 23:50:19.634 D bulletproof+ clawback: 0
```

## j-berman | 2025-10-28T00:20:36+00:00
#194 should help with this

## j-berman | 2025-10-30T23:35:45+00:00
Added comment: reorged (or popped block) txs count toward the pool weight, and are not pruned. If not mined, they will linger in the pool until they're kicked by the idle loop after 7 days (or pool is manually flushed).

## j-berman | 2025-12-08T19:32:30+00:00
Fixed by #194

# Action History
- Created by: j-berman | 2025-10-08T21:38:57+00:00
- Closed at: 2025-12-08T19:32:30+00:00
