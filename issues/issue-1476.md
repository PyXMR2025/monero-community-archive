---
title: Monero daemon crash (ge_frombytes_vartime failed at 208)
source_url: https://github.com/monero-project/monero/issues/1476
author: gituser
assignees: []
labels: []
created_at: '2016-12-20T10:42:21+00:00'
updated_at: '2016-12-20T22:46:32+00:00'
type: issue
status: closed
closed_at: '2016-12-20T22:46:32+00:00'
---

# Original Description
Using monero Monero 'Wolfram Warptangent' (v0.10.0.0-c36cb54) (compiled myself)

and it crashes for some reason (on testnet):

```
PoW:	<5c15bad0b8a2d968c76bcec10f9a20b45bd614fd1a074a716670763a660b0000>
difficulty:	58207
2016-Dec-18 22:33:57.400606 [P2P9]----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 802120
id:	<14169ef251ecd9e00b419682afbaa4735a208b7a176eefe89f3de567f5c1b5eb>
PoW:	<8e1f2173f7cc4efb50d9324ce2816486de36616f136cdfa1cc7952f2f0430000>
difficulty:	58842
2016-Dec-18 22:33:57.415781 [P2P9]----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 802121
id:	<04413235b2c0630e60f068369038d3bd90f1d9c28f4112eb2cf14be24e441679>
PoW:	<8fe3254212d1c30a9d6a3ca2ad5348ac6699561baeb50a0ca7ad8fc4b24a0000>
difficulty:	57575
2016-Dec-18 22:33:57.430962 [P2P9]----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 802122
id:	<b3883123d7e9090cd3eb849f7588c7ce16e57f0f22cc6aa51a9ee26e03a1c78d>
PoW:	<afef43a05ccf8974ef4f0da2aaed785fa366c9c6ffe96e9d26ea885c29440000>
difficulty:	57199
2016-Dec-18 22:33:57.543368 [P2P9]ERROR /home/build/monero/monero/src/ringct/rctOps.cpp:208 ge_frombytes_vartime failed at 208
2016-Dec-18 22:33:57.543392 ERROR /home/build/monero/monero/src/ringct/rctOps.cpp:208 ge_frombytes_vartime failed at 208
```

was it fixed in recent builds ?

let me know if there is anything else needed

# Discussion History
## ghost | 2016-12-20T15:05:38+00:00
Hi @gituser Please try again with the latest release (0.10.1) and let us know if this still happens :)

## gituser | 2016-12-20T15:29:07+00:00
I've tried `v0.10.1` now monero is not crashing anymore, but stuck in the background with CPU usage from 70 to 250% for quite long time.

I've already done full resync (removed old .bitmonero directory).

Last messages are:

```
2016-Dec-20 18:26:26.853078 [P2P5]----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 803686
id:	<5ab8fabbf8907b424915ac86e967925d6b9143fb3acccd51ac4ce2e1b9f78773>
PoW:	<feb3c6e28d699951df02c96124fe1b28c8d9238cc5c311ec289151e1caab0000>
difficulty:	21771
2016-Dec-20 18:26:26.868639 [P2P5]----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 803687
id:	<264732d817635397307592702f0c7d3d591e7fbadc2e5c01e16128bc9538d3dc>
PoW:	<7e8dc7a276c229d344183eac899c370f3c38bcf4bf5ae318ac02f45725a80200>
difficulty:	21769
```

Tried restarting it a couple of times and noticed as well these errors:
```
2016-Dec-20 17:51:50.461310 [RPC1]ERROR /home/build/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:355 Exception at [connection<t_protocol_handler>::handle_read], what=Attempting to get output pubkey by index, but key does not exist
2016-Dec-20 17:51:51.310638 [RPC1]ERROR /home/build/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:355 Exception at [connection<t_protocol_handler>::handle_read], what=Attempting to get output pubkey by index, but key does not exist
2016-Dec-20 18:07:18.186128 [RPC0]ERROR /home/build/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:355 Exception at [connection<t_protocol_handler>::handle_read], what=Attempting to get output pubkey by index, but key does not exist
```

## gituser | 2016-12-20T22:46:32+00:00
nevermind, I've figured it out, the reason is because of the fork happened on the testnet network.

so, restoring the wallet from seed solved this issue and monerod is no longer crashing.

thus, i'm closing the issue.

# Action History
- Created by: gituser | 2016-12-20T10:42:21+00:00
- Closed at: 2016-12-20T22:46:32+00:00
