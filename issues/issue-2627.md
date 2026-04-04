---
title: 'monero-wallet-rpc: Failed to create directory : No such file or directory'
source_url: https://github.com/monero-project/monero/issues/2627
author: Cyclenerd
assignees: []
labels: []
created_at: '2017-10-10T13:32:44+00:00'
updated_at: '2017-10-15T17:48:19+00:00'
type: issue
status: closed
closed_at: '2017-10-15T17:48:19+00:00'
---

# Original Description
Hi,

I'm on the current software (git master) version. Unfortunately, starting the program `monero-wallet-rpc` does not work:

```
nils@cryptocurrency wallets $ /home/nils/monero/build/release/bin/monero-wallet-rpc --testnet --rpc-bind-port 8080 --disable-rpc-login --wallet-file ~/wallets/NilsTestnetViewOnly --log-level 1
Monero 'Helium Hydra' (v0.11.0.0-86e9de5)
Logging to /home/nils/monero/build/release/bin/monero-wallet-rpc.log
2017-10-10 13:17:55.312     7f0042282740        WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:1853   Loading wallet...
Wallet password: *****
2017-10-10 13:17:58.780     7f0042282740        WARN    wallet.wallet2  src/wallet/wallet2.cpp:2478     Loaded wallet keys file, with public address: A28mJmhP3fSTHoJmQ2V41Phed9Yo5HXUw7bS43HZRGG6D4FNodjkync9kMN77v64EkgWrc4kEk6StZHfFfpmmwwsEiD5Z8z
2017-10-10 13:17:59.728     7f0042282740        ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:162    Failed to create directory : No such file or directory
2017-10-10 13:17:59.729     7f0042282740        ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:1894   Failed to initialize wallet rpc server
```

monero-wallet-rpc.log: https://paste.fedoraproject.org/paste/jq2ys7HZ5a6Evf~SRJfwtg

I'm not sure if I'm doing something wrong or whether it's a bug.

Best regards
Nils

# Discussion History
## moneromooo-monero | 2017-10-10T13:37:27+00:00
Fixed by https://github.com/monero-project/monero/pull/2592

## Cyclenerd | 2017-10-10T13:59:09+00:00
OK, thanks for the quick feedback. So it is a 🐛. I wait for the merge and then try again.

## jabiers | 2017-10-12T00:47:52+00:00
same issue.
Doesn't work with wallet-file


## KelvinJones | 2017-10-12T05:11:51+00:00
Same here. 
@moneromooo-monero how do we cherry-pick this from scratch?  I'll need to re-compile but that's no problem.  You've helped me get my pool daemon up and synch'd, now I just need the rpc wallet to work using this fix.  Should I use this fix or is there something better?


## moneromooo-monero | 2017-10-12T07:30:17+00:00
git checkout -b with-2592
git fetch origin pull/2592/head:2592
git cherry-pick 2592

When you want to get back to master:
git checkout master


## moneromooo-monero | 2017-10-15T17:45:52+00:00
+resolved

# Action History
- Created by: Cyclenerd | 2017-10-10T13:32:44+00:00
- Closed at: 2017-10-15T17:48:19+00:00
