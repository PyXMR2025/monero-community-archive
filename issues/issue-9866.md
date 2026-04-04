---
title: 'Performance & Cleanup: Needless Inheritance and Heap Allocations with TransactionInfo'
source_url: https://github.com/monero-project/monero/issues/9866
author: Tzadiko
assignees: []
labels: []
created_at: '2025-03-25T22:19:50+00:00'
updated_at: '2025-03-27T02:24:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I noticed a pattern in the codebase where we have classes postfixed with Impl. I thought this means that they're looking to implement the PIMPL idiom (e.g. TransactionInfoImpl inerhits from TransactionInfo), but here Impl actually just refers to an implementation of the virtual interface (TransactionInfo is actually an interface). The use of inheritance here isn't needed. It increases the size of any instance of the class (via the inclusion of the virtual table pointer). Furthermore, objects of type TransactionInfo are created with `new`, which is a heap allocation (is slow, and not needed in this context).  

I'd like to remove TransactionInfoImpl, and move the implementation into TransactionInfo, removing the virtual keyword from the class entirely. I'll then replace alls to `new TransactionInfoImpl` in `transction_history.cpp` with just the creation of the object on the stack. TransactionHistoryImpl, PendingTransactionImpl and UnsignedTransactionImpl are other examples.

Also, many of these classes are their own friends, which doesn't make any sense.

# Discussion History
## Tzadiko | 2025-03-25T22:50:04+00:00
Tangentially related to: https://github.com/monero-project/monero/issues/9461, albeit taking it a step further, recognizing pointers aren't needed at all.

## selsta | 2025-03-25T22:53:31+00:00
Would this break wallet2_api compatibility? Is it visible in git history why this design was chosen? From what I can tell this is not performance relevant code, so the benefits would be more in simplifying the code.

## Tzadiko | 2025-03-25T23:20:34+00:00
> Would this break wallet2_api compatibility?

I'm not sure. What would that mean / how would I do that? For example, I notice some methods on TransactionHistoryImpl aren't used (e.g. transaction(int index) in `transaction_history.h`). I can do one of two things:

1. Have it return an optional, instead of a pointer (as a result of my change).
2. Delete it since it's not referenced in our codebase.

If it's not referenced in our codebase, and I delete it, is it possible I break something outside our codebase that I'm not familiar with? I know refresh and count are definitely called in our codebase, but I'm not sure what a breaking change looks like.

Is a good way to test it to build the GUI wallet and see that the transaction info / transaction history works?

>  Is it visible in git history why this design was chosen? 

No. Looks like the initial author thought there would be multiple implementations of a TransactionInfo, but in the past 9 years there hasn't been a single one, so the pattern (inheritance) was implemented prematurely.

> From what I can tell this is not performance relevant code, so the benefits would be more in simplifying the code.

From the issue I linked above, looks like people are in agreement that this part of the code needs a modernization / cleanup.

## Tzadiko | 2025-03-27T02:24:01+00:00
I updated the PR description showing that my change didn't break the GUI.

# Action History
- Created by: Tzadiko | 2025-03-25T22:19:50+00:00
