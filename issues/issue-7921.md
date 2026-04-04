---
title: '[FR] monero-wallet-rpc get_address and create_address should create addresses
  and accounts if out of range'
source_url: https://github.com/monero-project/monero/issues/7921
author: elibroftw
assignees: []
labels: []
created_at: '2021-09-07T18:14:48+00:00'
updated_at: '2022-06-10T03:57:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
There should be an optional parameter for get_address so that the wallet-RPC creates the out of range accounts and addresses instead of returning an out of range error. This helps developing payments solutions and integrating monero.

It would also help if it was possible to create accounts up to a certain index, or addresses up to a certain index instead of having to make repeated calls.

# Discussion History
## plowsof | 2022-06-10T03:26:38+00:00
I think you want to use create_address ? https://monerodocs.org/interacting/monero-wallet-rpc-reference/#create_address

creating multiple addresses can be done without the use of the wallet rpc. for example using monero-python (offline address creation at specific indices) 

## elibroftw | 2022-06-10T03:54:08+00:00
Back then, I had a custom algorithm that would use addresses based on availability. Now I just call create_address for a specific account, so the only thing that would be nice is if create_address(x) would create accounts up to x instead of raising an error that the account does not exist.
![image](https://user-images.githubusercontent.com/21298211/172986831-3d2bb642-cbb5-449f-88aa-b4879fc9ae67.png)
This is the code I have to use. That's an extra 7 lines of code to account for the edge case where the wallet opened in the RPC  had not created the account which would occur if I needed to horizontally scale.
I'm a person who thinks about this kind of thing, so a naive programmer would simply use `create_address(IDX)` without realizing this possible edge case and when they decide to horizontally scale, things would break.

# Action History
- Created by: elibroftw | 2021-09-07T18:14:48+00:00
