---
title: Invalid Subaddress - Not sure if my implementation is right. Need help.
source_url: https://github.com/monero-project/monero/issues/4400
author: satheshhmax
assignees: []
labels:
- invalid
created_at: '2018-09-18T10:00:51+00:00'
updated_at: '2018-09-18T11:40:58+00:00'
type: issue
status: closed
closed_at: '2018-09-18T11:40:58+00:00'
---

# Original Description
I am building an exchange with monero as one of the coins. I started implementing monero a week back and its completed now. When I was trying to send coins to my address from binance/kraken it rejects saying its invalid address.  

So if anyone can help me confirm my understanding of monero implementation is correct.

First I created a Wallet and an account under that wallet. So got a base address which starts with 47xxx.. and its considered as valid as per monero address validation. 
For all other users who get registered I created subaddress under the same account and assign them to users accordingly. 

All thos subaddress starts with 8C.. for which I am getting invalid address while trying to send coin from other exchanges like Binance.

I have 3 questions,
1. Can subaddress be assigned to users in exchange for them to deposit/withdraw?
2. Right now I am not generating payment_id for the address. Is it required or useful to have payment_id for each address?
3. How can I generate address starts with 4.. so it's considered as valid address while trying to transfer coins from other exchanges?

Sorry if the above questions are very basic as I'm trying to understand how monero works for an exchange.

Thanks in advance.

# Discussion History
## moneromooo-monero | 2018-09-18T10:10:11+00:00
You seem to be doing it correctly. Binance and Kraken have probably not updated their system to support subaddresses, or have manual address validation that's rejecting them. Payment IDs are mostly obsoleted by subaddresses. There is *one* address that starts with 4 per wallet. You will just need to ping Binance/Kraken to complain they're out of date. Thankfully they just have to update their monero software (they'll have to prior to the october fork anyway) and ensure they don't have custom code to "pre-validate" addresses (or fix that custom code).


## satheshhmax | 2018-09-18T10:15:39+00:00
That explains. Thanks for the quick response.

## moneromooo-monero | 2018-09-18T10:47:44+00:00
If you ping them, you can stress that they don't have to change the way they do things (ie, they don't have to support subaddresses for deposits), just allow these addresses for withdrawals, and monero-wallet-rpc will do the right thing.

## moneromooo-monero | 2018-09-18T11:39:39+00:00
Not a bug, closing.

+invalid

# Action History
- Created by: satheshhmax | 2018-09-18T10:00:51+00:00
- Closed at: 2018-09-18T11:40:58+00:00
