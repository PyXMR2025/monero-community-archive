---
title: 'Wallet RPC: add address index filter to get_balance'
source_url: https://github.com/monero-project/monero/issues/4168
author: artyomsol
assignees: []
labels: []
created_at: '2018-07-23T13:34:11+00:00'
updated_at: '2018-08-16T19:09:00+00:00'
type: issue
status: closed
closed_at: '2018-08-16T19:09:00+00:00'
---

# Original Description
 In case of hundreds / thousands / millions of managed subaddresses the `get_balance` response of the RPC API will become a huge JSON as of current implementation.
 An `address_index` parameter (array of unsigned int; (Optional) List of subaddress indices to return from an account) should be added to optionally filter the "per_subaddress" array of the method response.
 Totals for the account balance ("balance"  and "unlocked_balance") should be calculated for the all of subaddresses despite of the filter parameter specified.


# Discussion History
## stoffu | 2018-07-23T14:59:20+00:00
#4171 

## stoffu | 2018-07-23T22:53:04+00:00
I've closed #4171 because it was tailored to the wrong use of subaddresses: if you need to issue millions of subaddresses to handle many users' deposits, you should use the `create_account` command for each user. Accounts are meant for managing individual users' balances, while subaddresses within the same account (i.e. having the same major index) are meant to be used for issuing one-time throwaway addresses (i.e. ShapeShift scenario in #2056).


## artyomsol | 2018-07-23T23:18:35+00:00
@stoffu Sorry but your doubt  is irrelevant to the issue you've solved. It does not matter  what for a wallet owner need to create millions of subaddresses. Having ShapeShift scenario you will face a trouble when `get_balance` will return ALL subaddresses in response all the time. While you will be interesting in some limited set of recently issued throwaway addresses.

## stoffu | 2018-07-24T00:43:03+00:00
> Having ShapeShift scenario you will face a trouble when get_balance will return ALL subaddresses in response all the time. 

This is not the case unless you only receive funds and never spend them; when spending them, the change goes back to the base address (minor index = 0) such that the funds accumulate in the base address.

Anyway, I reopened #4171 as it doesn't change the default behavior and seems harmless.


## moneromooo-monero | 2018-08-16T18:54:29+00:00
+resolved

# Action History
- Created by: artyomsol | 2018-07-23T13:34:11+00:00
- Closed at: 2018-08-16T19:09:00+00:00
