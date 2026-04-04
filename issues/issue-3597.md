---
title: compiled executables not working on the server
source_url: https://github.com/monero-project/monero/issues/3597
author: skinderis
assignees: []
labels:
- invalid
created_at: '2018-04-10T15:26:57+00:00'
updated_at: '2018-08-15T12:25:00+00:00'
type: issue
status: closed
closed_at: '2018-08-15T12:25:00+00:00'
---

# Original Description
I compiled binary files (monerod and monero-wallet-rpc) and try to run them on another machine on docker container and get this error:
```
./start.sh: line 3:     6 Illegal instruction     (core dumped) ./monerod --restricted-rpc --confirm-external-bind --non-interactive --config-file /root/monero/data/monero.conf --detach
./start.sh: line 3:     6 Illegal instruction     (core dumped) ./monerod --restricted-rpc --confirm-external-bind --non-interactive --config-file /root/monero/data/monero.conf --detach
./start.sh: line 3:     5 Illegal instruction     (core dumped) ./monerod --restricted-rpc --confirm-external-bind --non-interactive --config-file /root/monero/data/monero.conf --detach
./start.sh: line 3:     5 Illegal instruction     (core dumped) ./monerod --restricted-rpc --confirm-external-bind --non-interactive --config-file /root/monero/data/monero.conf --detach
./start.sh: line 3:     6 Illegal instruction     (core dumped) ./monerod --restricted-rpc --confirm-external-bind --non-interactive --config-file /root/monero/data/monero.conf --detach
./start.sh: line 3:     6 Illegal instruction     (core dumped) ./monerod --restricted-rpc --confirm-external-bind --non-interactive --config-file /root/monero/data/monero.conf --detach
./start.sh: line 3:     6 Illegal instruction     (core dumped) ./monerod --restricted-rpc --confirm-external-bind --non-interactive --config-file /root/monero/data/monero.conf --detach
```

Have someone had this issue before?

# Discussion History
## moneromooo-monero | 2018-04-10T15:32:25+00:00
Are you running on the same architecture ? If same arch, the original might have been built with instructions specific to the "version" (for instance, NEON for some ARMs).

## moneromooo-monero | 2018-07-19T21:44:31+00:00
I'll close this unless the details requested above are given soon.


## moneromooo-monero | 2018-08-15T11:31:13+00:00
+invalid


# Action History
- Created by: skinderis | 2018-04-10T15:26:57+00:00
- Closed at: 2018-08-15T12:25:00+00:00
