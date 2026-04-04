---
title: Small block attack vector
source_url: https://github.com/monero-project/research-lab/issues/156
author: Har01d
assignees: []
labels: []
created_at: '2025-12-19T20:20:48+00:00'
updated_at: '2026-01-20T21:03:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Consider a scenario where Monero is popular and has a good inflow of transactions requiring the dynamic block algo to kick in.

Under the current ruleset, a malicious miner with just about 33% (like Qubic) of the hashrate has an almost 100% chance of constantly resetting the short-term median back to the floor (currently 300 kB) by simply occasionally mining 50+ of the latest 100 blocks as empty or below the floor in size.

Employing this vector results in a constantly clogged blockchain and the dynamic block algo not working as intended.

# Discussion History
## ArticMine | 2025-12-31T15:08:47+00:00
I will first comment on the new scaling parameters, 8x on MN and 1.2x on ML, that were agreed to at the December 17th, 2025 MRL meeting. These parameters, especially 1.2x on ML are very tight, and could cause problems under certain circumstances in the short term. this being said they are necessary in order to provide a reasonable amount of time to fix the outstanding code issues. 

In order to the scaling to work properly ML needs to as much as possible track the actual adoption rate with MN being very close to ML under normal circumstances. The surge in MN above ML is designed to address short term holiday shopping demand, In particular MN  is designed to address  the expected difference in transaction rates between December 23rd and December 25th due to holiday shopping. The surge factor 8x is the bare minimum based upon historical VISA data. This surge factor is not intended to compensate for an ML that lags  the actual adoption over a period longer than 50000 blocks. The type of attack described in this issue is one of the possible issue that could arise. 

The question now becomes is the growth rate of ML at 1.2x too low? For this we can look at historical rates of growth for Bitcoin, Litecoin, Ethereum and Monero. I will consider growth rate above 20000 transactions per day. If we look at both Litecoin and Ethereum we see in 2017 we see growth rates of ~6.5x over a 6 month period  and ~30x over a year period  respectively in 2017. On the other hand if we look at Bitcoin between 2012 and 2017 we find a growth of about 2x per year.  

https://bitinfocharts.com/comparison/transactions-btc-eth-ltc-xmr.html#log&alltime

Is the growth rate of ML too low at 1.2x?  This depends on the type of growth that Monero sees in the short to medium term. If it is the Bitcoin model then 1.2x would be fine, since the 2.5x on ML would handle the growth well. On the other hand if we see the type of growth of Litecoin or Ethereum then  a rate of 2x on ML is necessary to avoid problems. 

The proper course of action at this point in my view is to go with the proposed 8x on MN and 1.2x on ML, for the FCMP++ fork and review these limits to consider 16x on MP and 2x on ML after the code issues are fixed. We will need to pay very close to attention to growth of Monero adoption in the next two years, in particular whether we see lag in ML and whether the current suppression of Monero adoption by the lobbying efforts of the blockchain surveillance companies continues. 

Edit: typo

# Action History
- Created by: Har01d | 2025-12-19T20:20:48+00:00
