---
title: Transactions sent to high `AddressIndex` addresses are not visible in wallet.
source_url: https://github.com/monero-project/monero/issues/8138
author: 3h5t4tvz8etx1op2
assignees: []
labels: []
created_at: '2022-01-09T18:01:49+00:00'
updated_at: '2022-02-18T23:03:22+00:00'
type: issue
status: closed
closed_at: '2022-02-18T23:03:22+00:00'
---

# Original Description
I run a site, which generate every address for each visitor. So many addresses are left unused. And after checking my view only wallet on the server I've seen many transactions coming to addresses with AddressIndex around 200, 400, 500 but none of that can be seen in my monero-gui wallet (nor in monerujo and cake)

# Discussion History
## ndorf | 2022-01-09T18:14:09+00:00
Not sure how one would accomplish this in the GUI, but if you can open the wallet in the CLI, the following commands should fix it:

`set subaddress-lookahead 50:1000`
`rescan_bc`

## 3h5t4tvz8etx1op2 | 2022-01-09T19:23:02+00:00
thanks @ndorf! Could you please tell me what does 50 and 1000 mean in that command?

## 3h5t4tvz8etx1op2 | 2022-01-10T04:43:19+00:00
Sadly - after even changing the numebrs to 50 and 2000 transactions send to address with account id ~1300 are have not been seen.

## JustFranz | 2022-01-10T14:48:32+00:00
50 is account and 2000 is subaddress. With that command you will not see transactions in accounts 51 and up and it will not see transactions in accounts 1-50 if they do not have transactions in the first 2000 subaddresses or if there is a gap of 2000 subadrersses with no transactions on any of the 50 accounts.

I would generate the subaddresses and assign them to your visitors when they need them. Each time a visitor sends XMR it should be to a new subaddress. You save on scanning time, database size and will not have this issue.

## selsta | 2022-01-10T17:08:26+00:00
@3h5t4tvz8etx1op2 do you generate a new account or a new address for each user?

if it's account then try `set subaddress-lookahead 1000:10` and then `rescan_bc`.

## 3h5t4tvz8etx1op2 | 2022-01-10T20:23:55+00:00
@JustFranz sadly I can't do that, the UX tradeoff is too big in my case, and I do use old addresses when they expire, but gaps of ~2k are frequent.

@selsta that was addresses. I've just re-coded the program to move the funds directly to my main address so there will be no problem with huge indexes.

## SamsungGalaxyPlayer | 2022-01-10T21:44:00+00:00
You can fiddle with the lookahead values to raise/reduce the number of accounts/addresses as needed. If this is an outrageously huge number, take some steps to reduce the display of subaddresses unless a user is more likely to send funds to it. If you only need 1 account and you need a bunch of subaddresses, set the lookahead to `1:10000` on desktop CLI for roughly similar performance as the default afaik, and then you can set up the auto-forward to the main address so it will appear in Cake Wallet. 

Edit: at that point I would recommend just using a separate seed for that Cake Wallet if possible for security reasons.

## selsta | 2022-01-10T21:45:06+00:00
Performance generally should stay the same, only RAM usage increases with more subaddresses.

## 3h5t4tvz8etx1op2 | 2022-01-11T04:43:21+00:00
@SamsungGalaxyPlayer that's what I ended up with, just swaping the funds whenever certain amount is there, this is not the ideal solution for me - but it for sure works.

## 3h5t4tvz8etx1op2 | 2022-01-11T04:43:59+00:00
However, I think that there should be option to specify the subaddress-lookahead in all wallets, or at least in the `gui` wallet

## SamsungGalaxyPlayer | 2022-01-11T04:44:44+00:00
I've added a note on the Cake Wallet side to support different lookahead values 👍

## 3h5t4tvz8etx1op2 | 2022-01-11T04:45:49+00:00
according to @selsta - how big is the memory footprint? I remember that in `core` bitcoin wallet the `wallet.dat` file was growing bigger and bigger with more addresses.

## selsta | 2022-01-11T22:48:48+00:00
@3h5t4tvz8etx1op2 I don't have any numbers, you'll have to try it out

# Action History
- Created by: 3h5t4tvz8etx1op2 | 2022-01-09T18:01:49+00:00
- Closed at: 2022-02-18T23:03:22+00:00
