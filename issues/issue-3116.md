---
title: '"Spendable Funds"'
source_url: https://github.com/monero-project/monero-gui/issues/3116
author: pullup
assignees: []
labels: []
created_at: '2020-09-27T17:52:30+00:00'
updated_at: '2020-10-04T22:27:06+00:00'
type: issue
status: closed
closed_at: '2020-10-04T22:27:06+00:00'
---

# Original Description
Is there no way to disable this child lock "spendable funds" stuff? Incredibly annoying. 
It even makes my entire balance unspendable when I send one transaction outwards, how on Earth does that make sense?

# Discussion History
## rating89us | 2020-10-02T22:12:41+00:00
No, it's a privacy feature that protects you from spending the same output multiple times in a short period of time, which would compromise your privacy.

If you don't want this to happen anymore, you should send multiple transactions to your wallet, which will create multiple outputs. This way when you spend one output, your wallet won't have the entire balance locked.

## pullup | 2020-10-04T22:06:55+00:00
> No, it's a privacy feature that protects you from spending the same output multiple times in a short period of time, which would compromise your privacy.
> 
> If you don't want this to happen anymore, you should send multiple transactions to your wallet, which will create multiple outputs. This way when you spend one output, your wallet won't have the entire balance locked.

Have you not considered the merchant application where their concern is for their client's privacy and not their own? Not everyone using XMR is in it for their own privacy, some just want to enable their customers to have total privacy.

## xiphon | 2020-10-04T22:27:06+00:00
Duplicate of https://github.com/monero-project/monero/issues/5810 where you'll find useful info/links, feel free to continue the discussion there

# Action History
- Created by: pullup | 2020-09-27T17:52:30+00:00
- Closed at: 2020-10-04T22:27:06+00:00
