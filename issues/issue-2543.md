---
title: Viewspans / Forward-Secure Addresses
source_url: https://github.com/monero-project/monero/issues/2543
author: needmoney90
assignees: []
labels: []
created_at: '2017-09-27T21:11:39+00:00'
updated_at: '2018-01-08T13:16:28+00:00'
type: issue
status: closed
closed_at: '2018-01-08T13:16:28+00:00'
---

# Original Description
Problem: 
 - Providing viewkeys to use light wallets currently compromises incoming transactions to your wallet on an ongoing basis. With the near release of a major light wallet (Mymonero), we face a situation where the vast majority of the transactions on the network are coming from light wallets. This could be a major detriment to privacy, as law enforcement or government agencies can run many nodes for users to connect to, or coerce companies like MyMonero to give up viewkeys, exposing transactions retroactively and on an ongoing basis.


Proposed solution: 
 - Viewspans, or forward-secure deposit addresses (name suggested by Surae). Viewspans are addresses that have an expiration date (and beginning) built in. They would be generated via a hierarchical deterministic scheme, where viewspans overlap with each other (for example, viewspan 1 covers a timespan of t0 to t30, viewspan 2 covers a timespan of t20 to t50, viewspan 3 covers a timespan of t40 to t70, etc). The overlap would cover more time than the current mempool ejection policy specifies.

 - Viewspans differ from subaddresses in that each viewspan has it's own unique viewkey. When a user wants to sync their wallet with a remote node(s), they send the pair (viewkey, block range). The node then returns all identified transactions associated with that viewkey within the given range.


Benefit: 
 - Viewspans would prevent light nodes from compromising your transaction history on an ongoing basis. Once MyMonero and other light wallets become the norm, this will be a serious issue. I think research on viewspans (or some other solution to this problem) should be prioritized.

# Discussion History
## ghost | 2017-09-27T21:19:38+00:00
Is homomorphic encryption of any use here, allowing the external wallet to provide an encrypted view key which the node uses to search for results without knowing the content of the results?

The node could return a set of distracting results as well, so that a smart coder couldn't watch their own node's traffic and only the wallet requester would know which response was actually correctly linked to the original query.

## b-g-goodell | 2017-09-28T21:09:21+00:00
Well, I think there *may* be possibilities inching toward a solution in forward-secure key exchange systems. Not necessarily suggesting a name. I will post some papers as I find them, if I find any that seem relevant.

## Gingeropolous | 2017-11-11T12:46:53+00:00
This will also be useful for auditing purposes. If cryptocurrencies remain taxed the way they currently are, it is beneficial if you can prove when you received your monero. If you can provide a viewspan for a given blockheight, you can prove to an auditor that you received Monero at that blockheight without revealing your entire financial status. 

## stoffu | 2017-11-11T14:12:20+00:00
FWIW the proof of incoming transfer can be done without giving up the view key and on the per-tx basis by showing the ECDH shared secret. The implementation is in #2487.

## dEBRUYNE-1 | 2018-01-08T13:05:46+00:00
+resolved

# Action History
- Created by: needmoney90 | 2017-09-27T21:11:39+00:00
- Closed at: 2018-01-08T13:16:28+00:00
