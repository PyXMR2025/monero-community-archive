---
title: The tail emission is too low?
source_url: https://github.com/monero-project/research-lab/issues/150
author: MichaelTen
assignees: []
labels: []
created_at: '2025-10-11T01:13:44+00:00'
updated_at: '2025-10-26T10:33:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The tail emission is too low? 

mining needs to be profitable? 

try increasing the tail emissions a bit. thanks and limitless peace.

(closed: https://github.com/monero-project/monero/issues/10144) 

i was told on Matrix to maybe post on Monero Research lab github more appropriately. ty ty 

# Discussion History
## MichaelTen | 2025-10-11T06:41:29+00:00
would increasing the tail emissions have unintended consequences? or would it simply make mining profitable for more individuals? or would more botnets just bring mining back to a mostly unprofitable equilibrium? 

## tevador | 2025-10-11T11:50:07+00:00
1. Changing the tail emission would be a contentious hard fork with a significant risk of splitting Monero into two different currencies.
2. Increasing the tail emission rate would not have any impact on mining profitability in the long term. The network hashrate increases until the average reward per hash matches the marginal cost per hash.

## MichaelTen | 2025-10-26T07:41:27+00:00
In relation to point 2 - Botnets throw off the whole equilibrium perhaps because their cost per hash is basically zero. They can keep mining profitably long after normal miners stop, which pushes the network hashrate higher than it “should” be and drives out many of those that would be paying real electricity costs.

I think the tail emission issue is connected to the bot net problem. 

https://github.com/monero-project/research-lab/issues/149

5 Percent of Monero in Circulation Was Mined Through Malware, Research Finds
https://cointelegraph.com/news/5-percent-of-monero-in-circulation-was-mined-through-malware-research-finds

Smominru Monero mining botnet making millions for operators
https://www.proofpoint.com/us/threat-insight/post/smominru-monero-mining-botnet-making-millions-operators

Point 1 - if contentious, then yes, agreed, quite likely.  

## tevador | 2025-10-26T10:32:24+00:00
Both of these botnet reports are from the time when Monero was still using CryptoNight. It's unclear how botnets affect RandomX specifically. If botnets are 5% of the network hashrate, I don't think it would have any significant impact on profitability.

I see no evidence that raising the tail emission would have a noticeable long-term impact on mining profitability.

Also the whole premise of this issue is wrong. Mining is not supposed to be profitable for everyone. It's a free market. Miners with a high marginal cost per hash will naturally drop out and be replaced by miners with lower costs.

# Action History
- Created by: MichaelTen | 2025-10-11T01:13:44+00:00
