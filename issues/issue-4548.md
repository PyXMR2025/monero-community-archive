---
title: 'Excessive restrictions on spending: lack of user control over coin spending
  conditions'
source_url: https://github.com/monero-project/monero-gui/issues/4548
author: jLucasvf
assignees: []
labels: []
created_at: '2026-01-13T16:08:04+00:00'
updated_at: '2026-01-13T16:58:40+00:00'
type: issue
status: closed
closed_at: '2026-01-13T16:49:22+00:00'
---

# Original Description
## Summary
The Monero GUI imposes restrictive spending limitations that significantly reduce user control and autonomy. Users should have the ability to override automatic spending restrictions based on their own judgment.

## Issues

### 1. Mandatory Lock Period on Recently-Received Coins
The GUI automatically prevents spending coins for a set number of blocks after receiving them. While this may be safe by default, there should be a toggle or setting allowing users to override this restriction if they choose to accept the risk.

**Current behavior:**
- Users cannot spend coins until a hardcoded number of blocks have passed
- No user-configurable option to modify this threshold
- Takes away user autonomy in managing their own funds

**Desired behavior:**
- Add a settings option to customize or disable the minimum block confirmation requirement
- Let users decide their own acceptable risk/time tradeoff

### 2. Large Portions of Funds Locked After Each Transaction
After sending a transaction, a large percentage of the wallet balance becomes unspendable for an extended period. This creates a serious usability issue where users cannot access most of their funds.

**Current behavior:**
- Major portions of the balance are blocked from spending after transactions
- Users cannot freely manage their coins
- Unclear why this restriction exists or how long it lasts

**Desired behavior:**
- Reduce or eliminate unnecessary fund locking
- If locking is required, provide clear information and user controls
- Allow users to override restrictions if they understand the implications

### 3. Forced Full Daemon Synchronization to Verify Double-Spend Prevention
The GUI requires syncing a full daemon just to verify that you haven't already spent certain coins (checking key image history). This is unnecessary overhead for users who know they haven't double-spent.

**Current behavior:**
- Must fully sync monerod daemon just to verify key images haven't been used
- No option to bypass this verification if you trust yourself
- Forces massive resource/bandwidth usage just for this one check

**Desired behavior:**
- Allow advanced users to manually provide the specific blocks containing their key images
- Let users verify double-spend prevention themselves without full daemon sync
- Users who understand the risk should be able to skip this step entirely

## General Request
**Give users more control.** The current restrictions treat users as if they cannot make informed decisions about their own money. Advanced options should be available for users who understand the implications and want more autonomy over their funds.

## Impact
- Users are locked out of spending their own money arbitrarily
- New users become frustrated with the wallet
- Power users cannot configure the wallet for their specific use case

# Discussion History
## nahuhh | 2026-01-13T16:48:53+00:00
AI slop?

## selsta | 2026-01-13T16:49:12+00:00
The 10 block limit is a network consensus rule, it can't be skipped by the GUI. The other suggestion also does not make sense, even when manually specifying key images you need a fully synced node to interact with the network.

## nahuhh | 2026-01-13T16:58:40+00:00
> ## Summary
> The Monero GUI imposes restrictive spending limitations that significantly reduce user control and autonomy. Users should have the ability to override automatic spending restrictions based on their own judgment.


Here lies the problem. This statement is incorrect. Monero GUI does not impose any restrictions beyond what the underlying protocol _requires_.

> ## Issues
> 
> ### 1. Mandatory Lock Period on Recently-Received Coins
> The GUI automatically prevents spending coins for a set number of blocks after receiving them. While this may be safe by default, there should be a toggle or setting allowing users to override this restriction if they choose to accept the risk.
> 
> **Current behavior:**
> - Users cannot spend coins until a hardcoded number of blocks have passed
> - No user-configurable option to modify this threshold
> - Takes away user autonomy in managing their own funds
> 
> **Desired behavior:**
> - Add a settings option to customize or disable the minimum block confirmation requirement
> - Let users decide their own acceptable risk/time tradeoff


This is by consensus. Funds on the monero network cannot be spent until 10 block confirmations (approximately 20 minutes) have passed. Unlike BTC, monero transactions reference 15 other transactions, and a block reorg can change the order of the referenced decoys (ring members) causing your transaction to be invalidated. Waiting 10 blocks is a security measure to prevent invalidated transactions.

> ### 2. Large Portions of Funds Locked After Each Transaction
> After sending a transaction, a large percentage of the wallet balance becomes unspendable for an extended period. This creates a serious usability issue where users cannot access most of their funds.
>
> **Current behavior:**
> - Major portions of the balance are blocked from spending after transactions
> - Users cannot freely manage their coins
> - Unclear why this restriction exists or how long it lasts
> 
> **Desired behavior:**
> - Reduce or eliminate unnecessary fund locking
> - If locking is required, provide clear information and user controls
> - Allow users to override restrictions if they understand the implications

Each transaction that you receive XMR is stores as a separate input. When you spend an input, you spend the whole input and receive change for the difference between the spent amount and the size of the input used.

Think of it like having $100 bills and spending $5. You get $95 in change, and that change is part of the same on-chain transaction as the $5 — meaning both require 10 confirmations before they are spendable.

> ### 3. Forced Full Daemon Synchronization to Verify Double-Spend Prevention
> The GUI requires syncing a full daemon just to verify that you haven't already spent certain coins (checking key image history). This is unnecessary overhead for users who know they haven't double-spent.
> 
> **Current behavior:**
> - Must fully sync monerod daemon just to verify key images haven't been used
> - No option to bypass this verification if you trust yourself
> - Forces massive resource/bandwidth usage just for this one check
> 
> **Desired behavior:**
> - Allow advanced users to manually provide the specific blocks containing their key images
> - Let users verify double-spend prevention themselves without full daemon sync
> - Users who understand the risk should be able to skip this step entirely


Slop. You can use remote nodes. There is not and has never been a requirement to run your own node.

# Action History
- Created by: jLucasvf | 2026-01-13T16:08:04+00:00
- Closed at: 2026-01-13T16:49:22+00:00
