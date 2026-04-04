---
title: 'WARN Error calling gettransactions daemon RPC: r 1, status Failed to parse
  and validate tx from blob'
source_url: https://github.com/monero-project/monero/issues/4655
author: JPaulMora
assignees: []
labels:
- duplicate
created_at: '2018-10-19T00:21:08+00:00'
updated_at: '2018-10-19T08:48:59+00:00'
type: issue
status: closed
closed_at: '2018-10-19T08:48:59+00:00'
---

# Original Description
```
2018-10-19 00:13:54.243 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
2018-10-19 00:14:14.539 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
2018-10-19 00:14:35.027 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
2018-10-19 00:14:55.323 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
2018-10-19 00:15:15.615 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
2018-10-19 00:15:36.703 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
2018-10-19 00:15:56.995 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
2018-10-19 00:16:17.287 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
2018-10-19 00:16:37.579 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
2018-10-19 00:16:57.871 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
2018-10-19 00:17:18.163 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
2018-10-19 00:17:38.455 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
2018-10-19 00:17:58.751 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
2018-10-19 00:18:19.043 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
2018-10-19 00:18:40.207 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
2018-10-19 00:19:02.331 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
2018-10-19 00:19:22.731 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:2504     Error calling gettransactions daemon RPC: r 1, status Failed to parse and validate tx from blob
```

Wallet-RPC is filling my logs with this message, using Linux 16.04 Monero release version from getmonero. I'd like to know what is this and if its a problem as a pool?

# Discussion History
## scmlxmr | 2018-10-19T07:45:09+00:00
I am getting similar error as well on daemon. Its throwing this error every 200ms ! 

2018-10-19 07:43:54.566 [RPC0]  ERROR   cn      src/cryptonote_basic/cryptonote_format_utils.cpp:185    Failed to parse transaction from blob

## scmlxmr | 2018-10-19T07:51:08+00:00
Apparently closed in #4636 

## moneromooo-monero | 2018-10-19T08:44:52+00:00
+duplicate

# Action History
- Created by: JPaulMora | 2018-10-19T00:21:08+00:00
- Closed at: 2018-10-19T08:48:59+00:00
