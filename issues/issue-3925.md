---
title: Can't Create Transaction; Not enough money to transfer
source_url: https://github.com/monero-project/monero-gui/issues/3925
author: elibroftw
assignees: []
labels: []
created_at: '2022-05-17T20:56:20+00:00'
updated_at: '2022-05-24T18:56:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If I manually enter the amount to send, I get this error.
![image](https://user-images.githubusercontent.com/21298211/168908299-03897609-44c8-4b79-a91a-13189e7be04c.png)

I think the message should show (send - fee) so that I don't have to manually do it myself. Or at least add a button to subtract the fee from one of the addresses I'm trying to send to.

I'm trying to send myself my entire balance as 4 parts in order to prevent locking my own funds when I use Monero in the future.

# Discussion History
## selsta | 2022-05-24T18:55:38+00:00
This isn't trivial to solve as you don't know the exact fee beforehand. That's why there is a specific `(all)` button. The error message should be updated to be more clear about the missing fee.

# Action History
- Created by: elibroftw | 2022-05-17T20:56:20+00:00
