---
title: Existing sub address(s) no longer display - but still work.
source_url: https://github.com/monero-project/monero-gui/issues/3162
author: ronohara
assignees: []
labels: []
created_at: '2020-10-17T09:10:33+00:00'
updated_at: '2020-10-17T12:12:44+00:00'
type: issue
status: closed
closed_at: '2020-10-17T12:12:43+00:00'
---

# Original Description
I had two extra subaddresses from the main wallet - and they still work because I just sent a test from Cake Wallet to one of them.

But when I opened up the accounts page they do not display(they used to). Other new ones which are now called 'accounts' but still have the '8' subaddress prefix, that I add do get displayed. 

file 1 main account ..  plus two new 'accounts' that I just added as per the Accounts page
file 2 - the test transaction to the old subaddress '89cq...' which no longer shows in the account page but still works.

![temp1](https://user-images.githubusercontent.com/4027321/96333356-3f9c1d80-1061-11eb-8caa-8454ef54632c.jpg)
![temp2](https://user-images.githubusercontent.com/4027321/96333360-43c83b00-1061-11eb-868f-55fdfce9c4fc.jpg)





# Discussion History
## rating89us | 2020-10-17T11:24:26+00:00
Probably you restored your wallet and the older subaddresses are not being displayed. But the wallet should display a subaddress after detecting an older receiving transaction. I'm not sure if it is currently looking ahead subaddresses until finding it.

## selsta | 2020-10-17T11:31:38+00:00
@ronohara 

Look on the Receive page. Every account has its own subaddresses so look through all 3 of them to find your address.

## ronohara | 2020-10-17T12:01:05+00:00
@rating89us - wallet has never been restored.

## rating89us | 2020-10-17T12:09:13+00:00
Account page displays only the first address (address #0) of each account. If you want to see the remaining subaddresses inside each account, you have to select the account and open Receive page. For example:

To see subaddresses of account #0, select account #0 in Account page, and then open Receive page.
To see subaddresses of account #2, select account #2 in Account page, and then open Receive page.

## ronohara | 2020-10-17T12:12:43+00:00
@rating89us  -- Ah I see ... all good

# Action History
- Created by: ronohara | 2020-10-17T09:10:33+00:00
- Closed at: 2020-10-17T12:12:43+00:00
