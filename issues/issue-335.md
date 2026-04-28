---
title: 'Derive type not supported for this hybrid address device: 2'
source_url: https://github.com/seraphis-migration/monero/issues/335
author: j-berman
assignees: []
labels: []
created_at: '2026-04-25T00:38:26+00:00'
updated_at: '2026-04-27T20:34:02+00:00'
type: issue
status: closed
closed_at: '2026-04-27T20:34:02+00:00'
---

# Original Description
Reported by @nahuhh:

```
2026-04-24 23:27:00.089 D     { core = { onetime address = '<fb9fe308b326be77624e6728ee136e870497af8e41278c3dfc78bcc098977518>', amount = 69.418831091646 }, block_inde23:27:00 [0/35962]
 1, external = 1 }                                                                                                                                                                       
2026-04-24 23:27:00.089 D     { core = { onetime address = '<3c6c9a8125406c6989702c389f8a7962aa41dedebd1322508ffc7cbf9d518492>', amount = 69.418562659006 }, block_index = 1011, carrot =
 1, external = 1 }                                                                                                                                                                       
2026-04-24 23:27:00.089 D Trying input selection with 2 tx inputs                                                                                                                        
2026-04-24 23:27:00.090 E Derive type not supported for this hybrid address device: 2                                                                                                    
2026-04-24 23:27:00.093 E Derive type not supported for this hybrid address device: 2                                                                                                    
2026-04-24 23:27:00.121 E Derive type not supported for this hybrid address device: 2                                                                                                    
2026-04-24 23:27:00.122 D make all proofs for transaction proposal: 2-in 16-out, with 15 normal payment proposals, 1 self-send payment proposals, and a fee of 199242000000 pXMR         
2026-04-24 23:27:00.122 E Derive type not supported for this hybrid address device: 2                                                                                                    
2026-04-24 23:27:00.124 E Derive type not supported for this hybrid address device: 2                                                                                                    
2026-04-24 23:27:00.145 E Derive type not supported for this hybrid address device: 2                                                                                                    
2026-04-24 23:27:00.147 E Derive type not supported for this hybrid address device: 2                                                                                                    
2026-04-24 23:27:00.160 E Derive type not supported for this hybrid address device: 2                                                                                                    
2026-04-24 23:27:00.162 E Derive type not supported for this hybrid address device: 2                                                                                                    
2026-04-24 23:27:00.165 D Making FCMPs and BP+ proofs for transaction proposal: 2-in 16-out, with fee of 0.199242000000                                                                  
2026-04-24 23:27:00.165 D Requesting FCMP path from tree cache for onetime address <05f57715b2184dc6179aa06a96cf644f5f64ac54f4acc11aa21281e17113e353>                                    
2026-04-24 23:27:00.165 D Output pubkey has torsion: <9b2e4c0281c0b02e7c53291a94d1d0cbff8883f8024f5142ee494ffbbd088071>                                                                  
2026-04-24 23:27:00.167 D Requesting FCMP path from tree cache for onetime address <1fa2aadfccb48e2920cde662e61d80bc8562d6f9ff937d6a05b7200110fb8ff0>                                    
2026-04-24 23:27:00.167 D Output pubkey has torsion: <9b2e4c0281c0b02e7c53291a94d1d0cbff8883f8024f5142ee494ffbbd088071>  
```

> This is from the stdout of wallet-rpc when sending a tx

# Discussion History
## j-berman | 2026-04-25T01:40:11+00:00
Looks related to #315

## jeffro256 | 2026-04-27T18:15:19+00:00
Yes, it is a duplicate of #315 AFAICT 

## jeffro256 | 2026-04-27T20:34:02+00:00
Resolved by #336 

# Action History
- Created by: j-berman | 2026-04-25T00:38:26+00:00
- Closed at: 2026-04-27T20:34:02+00:00
