---
title: Crypto++ and upcoming change for byte definition due to C++17
source_url: https://github.com/monero-project/monero/issues/2178
author: noloader
assignees: []
labels: []
created_at: '2017-07-17T11:41:17+00:00'
updated_at: '2017-07-17T12:44:38+00:00'
type: issue
status: closed
closed_at: '2017-07-17T12:44:38+00:00'
---

# Original Description
The Crypto++ library is getting ready to change its definition for `byte`. More information can be found at:

* [std::byte](https://www.cryptopp.com/wiki/Std::byte) on the Crypto++ wiki

* [Issue 442, Test C++17 byte change with dry runs from various projects](https://github.com/weidai11/cryptopp/issues/442)

Recommendations for user programs which use the library can be found at:

* [std::byte | Fixing Programs](https://www.cryptopp.com/wiki/Std::byte#Fixing_Programs) on the Crypto++ wiki

My apologies for opening an issue. Please label it as an enhancement or feature request.


# Discussion History
## moneromooo-monero | 2017-07-17T12:11:56+00:00
Thanks for the heads up. Monero itself doesn't use cryptopp, it's kovri that does. I don't think we can move issues between repos, so could you please open one on https://github.com/monero-project/kovri/issues instead ?
Opening an issue is the right way to do this, anonimal will tag as appropriate.

## noloader | 2017-07-17T12:44:38+00:00
@moneromooo-monero, Ack will do. Sorry about the extra noise.

# Action History
- Created by: noloader | 2017-07-17T11:41:17+00:00
- Closed at: 2017-07-17T12:44:38+00:00
