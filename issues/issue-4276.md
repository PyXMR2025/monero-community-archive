---
title: 'Windows: Can''t to send my moneros'
source_url: https://github.com/monero-project/monero-gui/issues/4276
author: developergames2d
assignees: []
labels: []
created_at: '2024-02-12T14:34:24+00:00'
updated_at: '2024-02-12T15:23:26+00:00'
type: issue
status: closed
closed_at: '2024-02-12T15:18:00+00:00'
---

# Original Description
https://youtu.be/HWNU-CSeakc
I screened the video with this error.
I restored my wallet from high 0 and connected to remote node. But I can't to send my moneros!
If I rescanned my balance the error is not going anywhere.

# Discussion History
## selsta | 2024-02-12T14:49:45+00:00
How did you generate this wallet? Did you change around the source code? Does this also happen on other platforms other than Windows?

## developergames2d | 2024-02-12T14:56:59+00:00
> How did you generate this wallet? Did you change around the source code? Does this also happen on other platforms other than Windows?

I generated it with [lincoins-master](https://xmr.llcoins.net/). The first 2 and last 2 hexadecimal-seed symbols are 0.
No, I didn't change, this is official wallet.
In other platforms I see some output transactions from account # 0, but I didn't see any transactions from subaccounts # 1 and # 2 of account # 0.

## selsta | 2024-02-12T15:09:42+00:00
Does your primary address really have 11111111111 in the middle?

## developergames2d | 2024-02-12T15:14:27+00:00
> Does your primary address really have 11111111111 in the middle?

Yes it has.

## selsta | 2024-02-12T15:14:40+00:00
Why did you send funds to this address? Everyone can generate the private key and steal your funds.

## developergames2d | 2024-02-12T15:16:11+00:00
> Why did you send funds to this address? Everyone can generate the private key and steal your funds.

I did not send to this any moneros, I just rescanned this address, but monero-gui writes that it has 10 moneros.

## selsta | 2024-02-12T15:18:00+00:00
You claimed they are "your" monero so it seemed like you have sent them to this address.

It says 10 monero because it's not a valid seed. It requires a source code change to see the correct balance.

## developergames2d | 2024-02-12T15:21:11+00:00
> You claimed they are "your" monero so it seemed like you have sent them to this address.
> 
> It says 10 monero because it's not a valid seed. It requires a source code change to see the correct balance.

Thanks, but it would be nice if your application worked with any Seed.

## plowsof | 2024-02-12T15:23:25+00:00
Developergames2d stop spamming this repo with useless issues. Asking for help to drain the infamous "Abbey seed" wallet?  Whats next, how to access the general fund view wallet moneros?

# Action History
- Created by: developergames2d | 2024-02-12T14:34:24+00:00
- Closed at: 2024-02-12T15:18:00+00:00
