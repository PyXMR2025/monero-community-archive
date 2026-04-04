---
title: 1 input or 2 inputs？
source_url: https://github.com/monero-project/monero/issues/8224
author: shrBest
assignees: []
labels: []
created_at: '2022-03-23T03:33:42+00:00'
updated_at: '2022-03-23T17:12:28+00:00'
type: issue
status: closed
closed_at: '2022-03-23T17:12:28+00:00'
---

# Original Description
When making a transaction, is the number of transaction inputs related to the transaction amount? For example, when I want to pay a small amount, I can use one output. The transaction input is 1. When I want to pay a large amount, I need several outputs to pay. At this time, the transaction input is 2.
Is that right？

# Discussion History
## jeffro256 | 2022-03-23T14:01:57+00:00
Yes, that's more or less correct. If you own 2 outputs of amount 5 each, and you try to spend more than 5, then you have to use both outputs as inputs to your spending transaction. 

## selsta | 2022-03-23T17:12:28+00:00
Closing as this is more of a general question and not a bug report.

# Action History
- Created by: shrBest | 2022-03-23T03:33:42+00:00
- Closed at: 2022-03-23T17:12:28+00:00
