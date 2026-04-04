---
title: Different SEED after recovering wallet!
source_url: https://github.com/monero-project/monero/issues/9110
author: developergames2d
assignees: []
labels:
- question
created_at: '2024-01-02T00:23:35+00:00'
updated_at: '2024-01-03T07:04:44+00:00'
type: issue
status: closed
closed_at: '2024-01-02T15:45:22+00:00'
---

# Original Description
I create new wallet:
SEED:
gadget haggled wade judge buying verification setup problems august mowing imbalance hashing slower wolf enjoy bypass jabbed tawny tossed pests poker gourmet ruling aisle aisle
Hexadecimal Seed:
1065d19680de20cd7f55a1650d13a8f50728a1460d925e6889ed52055ee9c14a

Private Spend Key:
5c15fa221752d76c26e2c2d9922b2ca20728a1460d925e6889ed52055ee9c10a
Address:
47LEUKEfr6m25epoRUi2XD29pbCP1vZJSEqVH6iTa8ehKMAr2KU32xoTBNHYH6JuYVT8RFwQQqBocKWUhb2o3PBJUQ8fBRr

After recovering this wallet in monero-gui I have my keys but **other SEED**!

Screenshots:

01
![image](https://github.com/monero-project/monero/assets/106807841/e20636d0-e26a-4296-8b4f-ffd010d5a6a0)


02
![image](https://github.com/monero-project/monero/assets/106807841/0ab2aaf4-d4bd-4947-bab8-09aa586c5522)
![image](https://github.com/monero-project/monero/assets/106807841/90b3ce43-4891-4eee-ac8a-9ee56691cfd5)




# Discussion History
## selsta | 2024-01-02T02:27:47+00:00
How did you create this seed?

## developergames2d | 2024-01-02T02:58:13+00:00
> How did you create this seed?

Generate 64-hexadecimal seed **_1065d19680de20cd7f55a1650d13a8f50728a1460d925e6889ed52055ee9c14a_** and past to addresstests on https://github.com/luigi1111/xmr.llcoins.net/tree/master/site

After I past seed to addressgen and get all keys.

## rbrunner7 | 2024-01-02T15:44:15+00:00
Monero private keys do not use the full 256 bits. They don't go up to 2^256-1, but if I understand that correctly only up to 2^252 + 27742317777372353535851937790883648493. Keys larger than this "magic" number get "reduced" with a modulo op to fit into the range. If somebody use a process that comes up with fully random 256 bits, they can hit such key over the limit.

So, nothing is really wrong I would say, you can use a wallet with such a "seed discrepancy". Or, if you find this all a bit strange and worrying, you can continue to generate random hex numbers with 64 digits until you hit one that is small enough and will not produce such an anomaly.

## developergames2d | 2024-01-03T07:04:44+00:00
> 1065d19680de20cd7f55a1650d13a8f50728a1460d925e6889ed52055ee9c14a

When I try to set first 2 hex-digits to 0, it not works, but when I try to set last 2 digits to 0, all is OK.

# Action History
- Created by: developergames2d | 2024-01-02T00:23:35+00:00
- Closed at: 2024-01-02T15:45:22+00:00
