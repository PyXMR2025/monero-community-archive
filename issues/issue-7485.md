---
title: Error built target daemonizer
source_url: https://github.com/monero-project/monero/issues/7485
author: samuk190
assignees: []
labels: []
created_at: '2021-03-09T12:16:08+00:00'
updated_at: '2021-03-09T13:17:59+00:00'
type: issue
status: closed
closed_at: '2021-03-09T13:17:51+00:00'
---

# Original Description
make[2]: *** No rule to process target '/home/samuel/Ferramentas/boost_1_66_0/stage/lib/libboost_chrono.so', necessary for 'bin/monero-wallet-rpc' .  Stop.
make[1]: *** [CMakeFiles/Makefile2:3409: src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Erro 2
make: *** [Makefile:160: all] Erro 2


How i can solve?

# Discussion History
## samuk190 | 2021-03-09T13:17:58+00:00
nevermind it was wrong boost installation

# Action History
- Created by: samuk190 | 2021-03-09T12:16:08+00:00
- Closed at: 2021-03-09T13:17:51+00:00
