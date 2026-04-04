---
title: Problem with broadcasting SECOND out transaction
source_url: https://github.com/monero-project/monero/issues/9087
author: developergames2d
assignees: []
labels:
- question
created_at: '2023-12-15T21:53:22+00:00'
updated_at: '2023-12-16T04:04:38+00:00'
type: issue
status: closed
closed_at: '2023-12-16T04:04:38+00:00'
---

# Original Description
I use monero-gui. When I sent first out transaction after offline signing, all was ok with the exception of error-message (but moneros was send). But when I try to create, offline-sign second output transaction from the same wallet, creating and offline signing was ok, but after trying broadcast I have error message like "double spending" and moneros didn't go to output wallet. I am sure I have selected a new transaction file (they were marked as 1 and 2).

# Discussion History
## selsta | 2023-12-16T02:21:21+00:00
> exception of error-message

What did the error message say?

Did you export / import outputs and key images first before creating the second transaction?

## developergames2d | 2023-12-16T02:25:31+00:00
> > exception of error-message
> 
> What did the error message say?
> 
> Did you export / import outputs and key images first before creating the second transaction?

Empty error message like "error with signing" without error code.
No, don't import because it didn't need for the first transaction... 

## selsta | 2023-12-16T02:26:15+00:00
It needs it for the second transaction, otherwise it will try to double spend the same outputs.

## selsta | 2023-12-16T02:35:00+00:00
Also reminder that you have to set your remote node as trusted in Settings -> Node to import outputs.

# Action History
- Created by: developergames2d | 2023-12-15T21:53:22+00:00
- Closed at: 2023-12-16T04:04:38+00:00
