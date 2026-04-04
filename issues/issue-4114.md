---
title: can't restore wallet from Secret spend key in monero GUI
source_url: https://github.com/monero-project/monero/issues/4114
author: apufvqsp
assignees: []
labels:
- invalid
created_at: '2018-07-09T07:04:36+00:00'
updated_at: '2018-07-09T08:56:59+00:00'
type: issue
status: closed
closed_at: '2018-07-09T08:56:59+00:00'
---

# Original Description
1. i special e80678b0953f01f461807044320322136d23288cad057e8c7de8cf2cffdeba39 as my Secret spend key
2.i use “./monero-wallet-cli --generate-from-spend-key e80678b0953f01f461807044320322136d23288cad057e8c7de8cf2cffdeba39 --testnet” restore my wallet 

i got view key "de1692fb3f73969bf342113d98af46ec02de3e343f845a278bace2f87a80e60c" and address "9tpmzrGnEso2cqRwN6zEaL5y4e7kfuSJecRgmttMPpBx1rKT7Gbq2ND6YbvZXm8crH2DircVUeYHze63eMXnrnA4UHkZUsH"

and i can sent tx from this wallet 
“transfer unimportant 9sXXpRtxYgh5yMYexKccr4dx35JM8rc1e8M7UDBfFCQmSgau1mQxTLk3j8MStt4CCnd8C99BGTw9uQ4DqhwtKq8r32pBpxe 0.01 032b653960304d73a62c5a60265b4a0458a59d276fa24a25a08a433983235cc8”

3. but i can't restore wallet from Secret spend key in monero GUi
<img width="930" alt="wx20180709-150301 2x" src="https://user-images.githubusercontent.com/17980580/42435457-39b91998-8389-11e8-8b8c-4f78f8b66d45.png">

**why monero-wallet-cli is ok bug monero GUi can't restore wallet from Secret spend key!!!**



# Discussion History
## moneromooo-monero | 2018-07-09T08:52:56+00:00
I don't know but (1) don't paste your secret keys on the internet or you'll get robbed and (2) if it's a GUI bug, report it on the GUI repo (https://github.com/monero-project/monero-core/issues).

+invalid

# Action History
- Created by: apufvqsp | 2018-07-09T07:04:36+00:00
- Closed at: 2018-07-09T08:56:59+00:00
