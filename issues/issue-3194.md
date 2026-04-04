---
title: daemon ignores '--data-dir' when running on testnet
source_url: https://github.com/monero-project/monero/issues/3194
author: leonklingele
assignees: []
labels: []
created_at: '2018-01-28T07:01:03+00:00'
updated_at: '2018-01-28T22:48:46+00:00'
type: issue
status: closed
closed_at: '2018-01-28T07:03:07+00:00'
---

# Original Description
The `--data-dir` argument seems to be ignored when starting the daemon with `--testnet`:

```bash
$ monerod --data-dir /srv/share/testnet/ --rpc-bind-ip 127.0.0.1 --restricted-rpc \
    --p2p-bind-ip 0.0.0.0 --db-sync-mode safe --fluffy-blocks --log-level 1 --testnet
```

It keeps storing files inside `/root/.bitmonero/testnet/`

```bash
$ lsof -p $(pidof monerod) | grep testnet
monerod 10142 root  mem       REG              0,158 16809984   62850 /root/.bitmonero/testnet/lmdb/data.mdb
monerod 10142 root  mem-r     REG              0,158     8192   62849 /root/.bitmonero/testnet/lmdb/lock.mdb
monerod 10142 root    4w      REG              0,158  4407871   62847 /root/.bitmonero/testnet/bitmonero.log
monerod 10142 root   14ur     REG              0,158     8192   62849 /root/.bitmonero/testnet/lmdb/lock.mdb
monerod 10142 root   15u      REG              0,158 16809984   62850 /root/.bitmonero/testnet/lmdb/data.mdb
monerod 10142 root   16u      REG              0,158 16809984   62850 /root/.bitmonero/testnet/lmdb/data.mdb
```

Reproduced with latest master (6ed314854cf87a7eb5810ef8a5dd707b4b9295e7).

# Discussion History
## leonklingele | 2018-01-28T07:03:07+00:00
Oops, there's a `--testnet-data-dir`. Sorry for the confusion.

## leonklingele | 2018-01-28T07:50:15+00:00
What's the reason for an additional flag to specify the testnet data dir? Why not reuse `--data-dir`? (@moneromooo-monero maybe?)

## leonklingele | 2018-01-28T22:48:46+00:00
`--testnet-data-dir` is being removed in #3170.

# Action History
- Created by: leonklingele | 2018-01-28T07:01:03+00:00
- Closed at: 2018-01-28T07:03:07+00:00
