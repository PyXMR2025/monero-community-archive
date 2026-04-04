---
title: Run a local RPC wallet.
source_url: https://github.com/monero-project/monero/issues/7609
author: chenluyong
assignees: []
labels: []
created_at: '2021-03-16T17:13:17+00:00'
updated_at: '2022-02-19T00:17:29+00:00'
type: issue
status: closed
closed_at: '2022-02-19T00:17:29+00:00'
---

# Original Description
use `window 7 x64  v0.17.1.9-release` 

`monerod` run args look like `monerod.conf`
```
# /etc/monero/monerod.conf

# Data directory (blockchain db and indices)
data-dir=../bitmonero  # Remember to create the monero user first

# Log file
log-file=./monerod.log
max-log-file-size=0            # Prevent monerod from managing the log files; we want logrotate to take care of that

# P2P full node
p2p-bind-ip=0.0.0.0            # Bind to all interfaces (the default)
p2p-bind-port=18080            # Bind to default port

# RPC open node
rpc-bind-ip=0.0.0.0            # Bind to all interfaces
rpc-bind-port=18081            # Bind on default port
confirm-external-bind=1        # Open node (confirm)
restricted-rpc=1               # Prevent unsafe RPC calls
no-igd=1                       # Disable UPnP port mapping

# Slow but reliable db writes
db-sync-mode=safe

# Emergency checkpoints set by MoneroPulse operators will be enforced to workaround potential consensus bugs
# Check https://monerodocs.org/infrastructure/monero-pulse/ for explanation and trade-offs
enforce-dns-checkpointing=1

out-peers=64              # This will enable much faster sync and tx awareness; the default 8 is suboptimal nowadays
in-peers=1024             # The default is unlimited; we prefer to put a cap on this

limit-rate-up=1048576     # 1048576 kB/s == 1GB/s; a raise from default 2048 kB/s; contribute more to p2p network
limit-rate-down=1048576   # 1048576 kB/s == 1GB/s; a raise from default 8192 kB/s; allow for faster initial sync
```

running success.
```
F:\projects\2021\xmr\bin\Monero GUI Wallet>"F:\projects\2021\xmr\bin\Monero GUI Wallet\monerod.exe" --config-file=./monerod.conf
2021-03-16 16:54:07.362 I Monero 'Oxygen Orion' (v0.17.1.9-release)
2021-03-16 16:54:07.364 I Initializing cryptonote protocol...
2021-03-16 16:54:07.364 I Cryptonote protocol initialized OK
2021-03-16 16:54:07.365 I Initializing core...
2021-03-16 16:54:07.365 I Loading blockchain from folder ../bitmonero\lmdb ...
2021-03-16 16:54:31.538 I Loading checkpoints
2021-03-16 16:54:36.502 I Core initialized OK
2021-03-16 16:54:36.503 I Initializing p2p server...
2021-03-16 16:54:36.514 I p2p server initialized OK
2021-03-16 16:54:36.515 I Initializing core RPC server...
2021-03-16 16:54:36.535 I Binding on 0.0.0.0 (IPv4):18081
2021-03-16 16:54:37.645 I core RPC server initialized OK on port: 18081
2021-03-16 16:54:37.668 I Starting core RPC server...
2021-03-16 16:54:37.670 I core RPC server started ok
2021-03-16 16:54:37.671 I Starting p2p net loop...
2021-03-16 16:54:38.671 I
2021-03-16 16:54:38.675 I **********************************************************************
2021-03-16 16:54:38.680 I The daemon will start synchronizing with the network.This may take a long time to complete.
2021-03-16 16:54:38.682 I
2021-03-16 16:54:38.684 I You can set the level of process detailization through "set_log <level|categories>" command,
2021-03-16 16:54:38.686 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg,*:WARNING).
2021-03-16 16:54:38.688 I
2021-03-16 16:54:38.690 I Use the "help" command to see the list of available commands.
2021-03-16 16:54:38.692 I Use "help <command>" to see a command's documentation.
2021-03-16 16:54:38.694 I **********************************************************************
2021-03-16 16:54:40.736 I
2021-03-16 16:54:40.737 I **********************************************************************
2021-03-16 16:54:40.738 I You are now synchronized with the network. You may now start monero-wallet-cli.
2021-03-16 16:54:40.740 I
2021-03-16 16:54:40.741 I Use the "help" command to see the list of available commands.
2021-03-16 16:54:40.742 I **********************************************************************
2021-03-16 16:56:43.042 I SYNCHRONIZED OK
```

Than running `wallet-rpc` error, commond:

./monero-wallet-rpc --rpc-bind-ip 0.0.0.0 --rpc-bind-port 28080 --password Aa123456 --wallet-file testwallet --rpc-login root:123456 --log-level 3

output information:
```
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Oxygen Orion' (v0.17.1.9-release)
2021-03-16 16:47:21.031 I Setting log level = 3
2021-03-16 16:47:21.031 I Logging to: F:\projects\2021\xmr\bin\Monero GUI Wallet\monero-wallet-rpc.log
Logging to F:\projects\2021\xmr\bin\Monero GUI Wallet\monero-wallet-rpc.log
2021-03-16 16:47:21.033 W Loading wallet...
2021-03-16 16:47:21.034 I [PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2021-03-16 16:47:21.040 D Address 'http://localhost:18081' is local
2021-03-16 16:47:21.040 I Daemon is local, assuming trusted
2021-03-16 16:47:21.040 D Device 0 Created
2021-03-16 16:47:21.041 I setting daemon to http://localhost:18081
2021-03-16 16:47:21.041 I [PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2021-03-16 16:47:21.076 I Generating SSL certificate
2021-03-16 16:47:22.320 I ringdb path set to C:\ProgramData\.shared-ringdb
2021-03-16 16:47:22.370 I [PARSE URI] regex not matched for uri: ^((.*?)://)?(\[(.*)\](:(\d+))?)(.*)?
2021-03-16 16:47:22.403 I Generating SSL certificate
2021-03-16 16:47:23.183 E portable_storage: wrong binary format - signature mismatch
2021-03-16 16:47:23.183 E !r. THROW EXCEPTION: error::invalid_password
2021-03-16 16:47:23.183 W /home/ubuntu/build/monero/src/wallet/wallet2.cpp:4353:N5tools5error16invalid_passwordE: invalid password
2021-03-16 16:47:23.183 D Problems at ssl shutdown: uninitialized
2021-03-16 16:47:23.184 D <Invalid UTF-8 in log>2021-03-16 16:47:23.184 D <Invalid UTF-8 in log>2021-03-16 16:47:23.186 D Problems at ssl shutdown: uninitialized
2021-03-16 16:47:23.186 D <Invalid UTF-8 in log>2021-03-16 16:47:23.186 D <Invalid UTF-8 in log>2021-03-16 16:47:23.188 E Wallet initialization failed: invalid password
```

system throw exception `invalid_password`???
I didn't set any password before running `monero-wallet-rpc`


[《monero-wallet-rpc-reference》](https://monerodocs.org/interacting/monero-wallet-rpc-reference/)
There is also no instruction in this tutorial on how to set the parameters about `monero-wallet-rpc`.

# Discussion History
## moneromooo-monero | 2021-03-18T09:59:50+00:00
You did not set any password on creation, but set a password on load, and are wondering why it's not working ? I feel like I'm missing something. Did you misspeak somewhere ?

# Action History
- Created by: chenluyong | 2021-03-16T17:13:17+00:00
- Closed at: 2022-02-19T00:17:29+00:00
