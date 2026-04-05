---
title: Failed to verify FCMP++ proof on mining
source_url: https://github.com/seraphis-migration/monero/issues/172
author: bvcxza
assignees: []
labels: []
created_at: '2025-10-12T18:57:09+00:00'
updated_at: '2026-03-09T16:59:30+00:00'
type: issue
status: closed
closed_at: '2026-03-09T16:59:30+00:00'
---

# Original Description
On monerod:
```
2025-10-12 18:41:55.860	I Monero 'FCMP++ / Carrot alpha stressnet' (v0.19.0.0-alpha.1.1-f76c469de)
...
start_mining 9xxxxxxxxxxxxxxx 2
Mining to a testnet address, make sure this is intentional!
2025-10-12 18:48:36.874	I Miner thread was started [0]
2025-10-12 18:48:36.875	I Miner thread was started [1]
2025-10-12 18:48:52.573	E Failed to verify FCMP++ proof
2025-10-12 18:52:46.928	E Failed to verify FCMP++ proof
2025-10-12 18:52:46.951	E Failed to verify FCMP++ proof
2025-10-12 18:52:46.974	E Failed to verify FCMP++ proof
...
```

Maybe related #46 

# Discussion History
## nahuhh | 2025-10-12T22:53:49+00:00
Probably due to a deep reorg

if you're still getting this, check `alt_chain_info` or a reorg that is greater than 10 or more blocks

## bvcxza | 2025-10-12T23:31:33+00:00
```
2025-10-12 23:29:15.658	E Failed to verify FCMP++ proof
2025-10-12 23:29:15.678	E Failed to verify FCMP++ proof
2025-10-12 23:29:15.698	E Failed to verify FCMP++ proof
2025-10-12 23:29:15.718	E Failed to verify FCMP++ proof
2025-10-12 23:29:15.739	E Failed to verify FCMP++ proof
2025-10-12 23:29:32.893	I Miner thread was started [0]
2025-10-12 23:29:32.893	I Miner thread was started [1]
alt_chain_info
0 alternate chains found:
2025-10-12 23:29:53.220	I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 2853043
2025-10-12 23:29:53.220	I id:	<440169840f35647452c51397e2a26743629e59c8820b682ff2da4104e50bd3be>
2025-10-12 23:29:53.220	I PoW:	<d3e16a3678d2e31c1f1980df1d30c9468de09f59473f455ccb175a2540430000>
2025-10-12 23:29:53.220	I difficulty:	178008
```

## nahuhh | 2025-10-13T01:52:09+00:00
You must have restarted your node, there were many alt chains today, and a 19 block reorg seed on my node

if its causing you issies, you'll have to do a `flush_txpool` to get rid of the log spam

## bvcxza | 2025-10-14T22:06:52+00:00
Node restarted and mining with no errors today

## j-berman | 2026-03-09T16:59:30+00:00
Doesn't seem an issue

# Action History
- Created by: bvcxza | 2025-10-12T18:57:09+00:00
- Closed at: 2026-03-09T16:59:30+00:00
