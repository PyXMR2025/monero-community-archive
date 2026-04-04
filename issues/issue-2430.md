---
title: 'merchants: remove godex.io'
source_url: https://github.com/monero-project/monero-site/issues/2430
author: TheFuzzStone
assignees: []
labels: []
created_at: '2024-11-28T19:24:15+00:00'
updated_at: '2025-03-20T09:50:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I propose to remove the exchanger 'godex.io' from the merchant list.

The reasons:

1. If a user checks his BTC, USDT, etc. before sending to this exchanger it does not guarantee that the exchanger will not force him to do KYC/AML;

2. Even after verification of the address by 'godex.io' support, which has USDT (TRC20) that were bought on OTC market without KYC/AML, support can't give a definite answer whether they can accept USDT (TRC20) from me or I will be forced to go through KYC/AML;

Screenshots of correspondence taken a couple minutes ago:

![Screenshot_20241128_190706](https://github.com/user-attachments/assets/ac35cfe4-434b-4f55-b323-e84304b19f2d)

![Screenshot_20241128_190729](https://github.com/user-attachments/assets/e59135b6-91b7-4ec3-aece-d7861abd6164)

![Screenshot_20241128_190818](https://github.com/user-attachments/assets/58c16be5-cbdc-4949-94bb-0d36f0c43404)

![Screenshot_20241128_190848](https://github.com/user-attachments/assets/bf8a9ed2-6a2c-493a-b415-e0cf89bbe63b)

![Screenshot_20241128_191034](https://github.com/user-attachments/assets/918a36db-305e-4e28-83cd-da82c221f018)


# Discussion History
## monerobull | 2024-11-29T13:56:51+00:00
Black boxes deciding who is innocent and who is guilty. These guys should be removed.

## fheroes2bugs | 2025-03-20T08:59:38+00:00
Also, speaking about merchants, community member created topic, gathering information:
https://np.reddit.com/r/Monero/comments/1j36jlt/update_regrading_monero_exchange_ecosystem/

Not only godex has KYC risks, also SimpleSwap, ChangeNow and StealthEX.

![Image](https://github.com/user-attachments/assets/c7a76a12-a65d-492b-8808-92c1792fa8b0)

For me, Exch.cx looks the best at the moment, since we in monero care about privacy.



## monerobull | 2025-03-20T09:50:33+00:00
Honestly just put Trocador on there by itself, it clearly communicates which exchanges pose a KYC risk and which doesn't. Essentially outsourcing the validation of the swapper list from the getmonero.org maintainers to Trocador.

# Action History
- Created by: TheFuzzStone | 2024-11-28T19:24:15+00:00
