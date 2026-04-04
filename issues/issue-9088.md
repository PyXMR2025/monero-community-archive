---
title: 'Can I to see balance after out transaction after creating only-view wallet? '
source_url: https://github.com/monero-project/monero/issues/9088
author: developergames2d
assignees: []
labels:
- question
created_at: '2023-12-16T03:58:10+00:00'
updated_at: '2024-01-02T15:45:42+00:00'
type: issue
status: closed
closed_at: '2024-01-02T15:45:42+00:00'
---

# Original Description
Can I to see balance after out transaction after creating only-view wallet on monero-gui? I notice that Monerujo on Android can to see my "change" value after the outgoing transaction.
I didn't set seed on Monerujo.

# Discussion History
## selsta | 2023-12-16T04:04:22+00:00
You have to import key images to get the correct balance in your view only wallet.

## developergames2d | 2023-12-16T04:24:06+00:00
> You have to import key images to get the correct balance in your view only wallet.

Is it safe? I don't want to move private send key or seed on online computer with only-view wallet. 

## selsta | 2023-12-16T04:26:02+00:00
Your seed should not be entered on an online computer, that's why you have to exchange key images and outputs between the offline wallet and the view only wallet.

Did you read this? It explains the concept: https://monerodocs.org/cold-storage/offline-transaction-signing/

# Action History
- Created by: developergames2d | 2023-12-16T03:58:10+00:00
- Closed at: 2024-01-02T15:45:42+00:00
